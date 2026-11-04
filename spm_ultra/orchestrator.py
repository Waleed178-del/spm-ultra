"""SPM Ultra Master Orchestrator: intake, parallel dispatch, refinement, audit, blueprint."""

from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

from . import prompts
from .registry import DIRECTORATES, MANDATORY_CROSS_CHECKS, Directorate, agent_by_id

log = logging.getLogger("spm_ultra")

DEFAULT_MODEL = "claude-opus-5-5"


# --------------------------------------------------------------------------- LLM backends


class LLM(Protocol):
    async def complete(self, *, system: str, user: str, effort: str, max_tokens: int,
                       schema: dict | None = None, label: str = "") -> str: ...


@dataclass
class Usage:
    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0


class RefusalError(RuntimeError):
    pass


class ClaudeLLM:
    """Anthropic API backend. Streams every call, adaptive thinking, server side refusal fallback."""

    def __init__(self, model: str = DEFAULT_MODEL, max_concurrency: int = 8,
                 use_fallbacks: bool = True) -> None:
        from anthropic import AsyncAnthropic

        self.client = AsyncAnthropic()
        self.model = model
        self.sem = asyncio.Semaphore(max_concurrency)
        self.use_fallbacks = use_fallbacks
        self.usage = Usage()

    async def complete(self, *, system: str, user: str, effort: str, max_tokens: int,
                       schema: dict | None = None, label: str = "") -> str:
        output_config: dict[str, Any] = {"effort": effort}
        if schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": schema}
        kwargs: dict[str, Any] = dict(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            thinking={"type": "adaptive"},
            output_config=output_config,
        )
        if self.use_fallbacks:
            kwargs["betas"] = ["server-side-fallback-2026-07-01"]
            kwargs["fallbacks"] = "default"

        async with self.sem:
            log.info("dispatch  %s", label)
            async with self.client.beta.messages.stream(**kwargs) as stream:
                msg = await stream.get_final_message()

        self.usage.calls += 1
        self.usage.input_tokens += msg.usage.input_tokens
        self.usage.output_tokens += msg.usage.output_tokens

        if msg.stop_reason == "refusal":
            raise RefusalError(f"{label}: request declined ({msg.stop_details})")
        if msg.stop_reason == "max_tokens":
            log.warning("%s hit max_tokens; output truncated", label)
        log.info("complete  %s", label)
        return "".join(b.text for b in msg.content if b.type == "text")


class MockLLM:
    """Offline backend for dry runs and tests. Returns deterministic placeholder output."""

    def __init__(self) -> None:
        self.usage = Usage()
        self.labels: list[str] = []

    async def complete(self, *, system: str, user: str, effort: str, max_tokens: int,
                       schema: dict | None = None, label: str = "") -> str:
        self.usage.calls += 1
        self.labels.append(label)
        if label == "intake":
            return json.dumps({
                "ready": True, "industry_vector": "mock", "primary_goal": "mock goal",
                "timeline": "12 months", "budget": "$100k", "diagnostic_questions": [],
                "context_brief": user,
            })
        if label == "audit":
            return json.dumps({"conflicts": [
                {"check": name, "agent_ids": list(a) + list(b), "in_conflict": i == 0,
                 "severity": "high" if i == 0 else "low", "description": "mock"}
                for i, (name, a, b) in enumerate(MANDATORY_CROSS_CHECKS)
            ]})
        return f"[mock output for {label}]"


# --------------------------------------------------------------------------- pipeline


@dataclass
class Intake:
    ready: bool
    industry_vector: str
    primary_goal: str
    timeline: str
    budget: str
    diagnostic_questions: list[str]
    context_brief: str


@dataclass
class RunResult:
    intake: Intake
    agent_outputs: dict[int, str] = field(default_factory=dict)
    briefs: dict[int, str] = field(default_factory=dict)
    conflicts: list[dict] = field(default_factory=list)
    reconciliations: list[str] = field(default_factory=list)
    blueprint: str = ""

    def save(self, out_dir: Path) -> None:
        (out_dir / "agents").mkdir(parents=True, exist_ok=True)
        (out_dir / "briefs").mkdir(parents=True, exist_ok=True)
        (out_dir / "intake.json").write_text(json.dumps(self.intake.__dict__, indent=2))
        for aid, text in sorted(self.agent_outputs.items()):
            (out_dir / "agents" / f"agent_{aid:02d}.md").write_text(text)
        for did, text in sorted(self.briefs.items()):
            (out_dir / "briefs" / f"directorate_{did}.md").write_text(text)
        (out_dir / "audit.json").write_text(json.dumps(self.conflicts, indent=2))
        (out_dir / "reconciliations.md").write_text("\n\n".join(self.reconciliations))
        (out_dir / "blueprint.md").write_text(self.blueprint)


class MasterOrchestrator:
    """Hierarchical cluster: Master -> 6 directorate leads -> 30 specialists."""

    def __init__(self, llm: LLM, worker_effort: str = "medium",
                 lead_effort: str = "high", master_effort: str = "high") -> None:
        self.llm = llm
        self.worker_effort = worker_effort
        self.lead_effort = lead_effort
        self.master_effort = master_effort

    # 1. INTAKE ANALYSIS
    async def intake(self, idea: str, answers: str | None = None) -> Intake:
        user = f"<raw_idea>\n{idea}\n</raw_idea>"
        if answers:
            user += f"\n<diagnostic_answers>\n{answers}\n</diagnostic_answers>"
        raw = await self.llm.complete(system=prompts.intake_system(), user=user,
                                      effort="medium", max_tokens=8000,
                                      schema=prompts.INTAKE_SCHEMA, label="intake")
        return Intake(**json.loads(raw))

    # 2. SYNCHRONOUS DISPATCH + internal directorate refinement loop
    async def _run_directorate(self, d: Directorate, context: str,
                               result: RunResult) -> None:
        payload = f"<context_brief>\n{context}\n</context_brief>"
        outputs = await asyncio.gather(*[
            self.llm.complete(system=prompts.agent_system(a, d), user=payload,
                              effort=self.worker_effort, max_tokens=16000,
                              label=f"agent {a.id:02d} {a.name}")
            for a in d.agents
        ])
        for a, out in zip(d.agents, outputs):
            result.agent_outputs[a.id] = out

        specialist_block = "\n\n".join(
            f"<agent id=\"{a.id}\" name=\"{a.name}\">\n{out}\n</agent>"
            for a, out in zip(d.agents, outputs)
        )
        result.briefs[d.id] = await self.llm.complete(
            system=prompts.directorate_lead_system(d),
            user=f"{payload}\n\n<specialist_outputs>\n{specialist_block}\n</specialist_outputs>",
            effort=self.lead_effort, max_tokens=16000, label=f"directorate {d.id} lead",
        )

    # 3. CONTRADICTION AUDIT LOOP
    async def _audit(self, context: str, result: RunResult) -> None:
        checks = "\n".join(
            f"- {name}: agents {list(a)} vs agents {list(b)}"
            for name, a, b in MANDATORY_CROSS_CHECKS
        )
        briefs = "\n\n".join(
            f"<brief directorate=\"{d.id}\">\n{result.briefs[d.id]}\n</brief>"
            for d in DIRECTORATES
        )
        raw = await self.llm.complete(
            system=prompts.audit_system(checks),
            user=f"<context_brief>\n{context}\n</context_brief>\n\n{briefs}",
            effort=self.master_effort, max_tokens=16000,
            schema=prompts.AUDIT_SCHEMA, label="audit",
        )
        result.conflicts = json.loads(raw)["conflicts"]

        live = [c for c in result.conflicts if c["in_conflict"]]
        result.reconciliations = list(await asyncio.gather(*[
            self._reconcile(c, context, result) for c in live
        ]))

    async def _reconcile(self, conflict: dict, context: str, result: RunResult) -> str:
        evidence = "\n\n".join(
            f"<agent id=\"{aid}\" name=\"{agent_by_id(aid).name}\">\n"
            f"{result.agent_outputs.get(aid, '(no output)')}\n</agent>"
            for aid in conflict["agent_ids"] if 1 <= aid <= 30
        )
        return await self.llm.complete(
            system=prompts.reconcile_system(),
            user=(f"<context_brief>\n{context}\n</context_brief>\n\n"
                  f"<conflict>\n{json.dumps(conflict, indent=2)}\n</conflict>\n\n{evidence}"),
            effort=self.lead_effort, max_tokens=16000,
            label=f"reconcile: {conflict['check']}",
        )

    # 4. UNIFIED OUTPUT GENERATION
    async def _blueprint(self, context: str, result: RunResult) -> None:
        briefs = "\n\n".join(
            f"<brief directorate=\"{d.id}\">\n{result.briefs[d.id]}\n</brief>"
            for d in DIRECTORATES
        )
        audit = json.dumps(result.conflicts, indent=2)
        recon = "\n\n".join(result.reconciliations) or "(no live conflicts)"
        result.blueprint = await self.llm.complete(
            system=prompts.master_system(),
            user=(f"<context_brief>\n{context}\n</context_brief>\n\n{briefs}\n\n"
                  f"<audit>\n{audit}\n</audit>\n\n<reconciliations>\n{recon}\n</reconciliations>"),
            effort=self.master_effort, max_tokens=64000, label="master blueprint",
        )

    async def run(self, idea: str, answers: str | None = None) -> RunResult:
        intake = await self.intake(idea, answers)
        result = RunResult(intake=intake)
        if not intake.ready:
            return result
        context = intake.context_brief
        await asyncio.gather(*[self._run_directorate(d, context, result) for d in DIRECTORATES])
        await self._audit(context, result)
        await self._blueprint(context, result)
        return result
