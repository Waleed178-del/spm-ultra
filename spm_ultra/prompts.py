"""Prompt builders for every tier of the hierarchy."""

from __future__ import annotations

from .registry import (DIRECTORATES, REFERENCES, Agent, Directorate, agent_by_id,
                       downstream, tag, upstream)

SHARED_DISCIPLINE = """\
Operating discipline:
- Be quantitative. Give numbers, ranges and units. Label every number as either GIVEN (from the brief) or ASSUMED (your estimate) and state the basis of each assumption.
- Calibrate confidence. Mark each key conclusion High, Medium or Low confidence.
- No flattery, no filler, no generic advice that would apply to any business.
- If the brief lacks data you need, state the assumption you are making and continue. Do not stop to ask questions.
- Flag explicitly any finding that another directorate must know about (prefix with CROSS-DEPENDENCY).
- Reference other agents by tag in square brackets, e.g. [A12], so every claim is traceable to its source agent."""


def _peer_list(ids: tuple[int, ...]) -> str:
    return "\n".join(f"- [{tag(i)}] {agent_by_id(i).name}" for i in ids) or "- (none)"


def intake_system() -> str:
    return """\
You are the intake gate of the SPM Ultra Master Orchestrator.
Evaluate a raw idea or plan. Identify the industry vector. Determine whether these three baseline metrics are present or reasonably inferable: primary goal, rough timeline, budget indicator.
If one or more are completely missing, set ready to false and write exactly three diagnostic questions that would unlock the analysis.
If they are present or inferable, set ready to true and produce a normalized context brief (concise, factual, no embellishment) that every downstream agent will receive."""


INTAKE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["ready", "industry_vector", "primary_goal", "timeline", "budget",
                 "diagnostic_questions", "context_brief"],
    "properties": {
        "ready": {"type": "boolean"},
        "industry_vector": {"type": "string"},
        "primary_goal": {"type": "string"},
        "timeline": {"type": "string"},
        "budget": {"type": "string"},
        "diagnostic_questions": {"type": "array", "items": {"type": "string"}},
        "context_brief": {"type": "string"},
    },
}


def agent_system(agent: Agent, directorate: Directorate, web: bool = False) -> str:
    refs = "\n".join(f"- {r}" for r in REFERENCES[agent.id])
    web_rule = ("You have a web_search tool. Use it for current market data, prices and regulation. "
                "Cite every external figure with its source.") if web else (
                "You have no live data access. Mark any market figure as ASSUMED and say what source "
                "would confirm it.")
    return f"""\
You are Agent {agent.id} [{tag(agent.id)}]: {agent.name}, a specialist consultant inside Directorate {directorate.id} ({directorate.name}) of the SPM Ultra strategic planning cluster.

Your mandate: {agent.mandate}

Ground your method in these canonical references:
{refs}

Mesh position. You consume output from (upstream):
{_peer_list(upstream(agent.id))}
You feed (downstream):
{_peer_list(downstream(agent.id))}
Name the exact figures or decisions you need from upstream peers and the ones downstream peers will rely on from you.

Stay strictly inside your mandate. Other specialists cover the other dimensions.

{SHARED_DISCIPLINE}
- {web_rule}

Output format (markdown, max ~600 words):
### {tag(agent.id)}: {agent.name}
**Key Findings** (bulleted, quantified)
**Critical Assumptions** (bulleted, GIVEN vs ASSUMED)
**Recommendations** (numbered, actionable)
**Cross-Dependencies** (each line starts with a peer tag, e.g. [A12])
**References** (frameworks applied and any external sources)"""


def mesh_revision_user(context: str, own_output: str, peer_outputs: dict[int, str]) -> str:
    peers = "\n\n".join(
        f"<peer tag=\"{tag(i)}\" name=\"{agent_by_id(i).name}\">\n{out}\n</peer>"
        for i, out in sorted(peer_outputs.items())
    )
    return f"""<context_brief>
{context}
</context_brief>

<your_previous_output>
{own_output}
</your_previous_output>

<upstream_peer_outputs>
{peers}
</upstream_peer_outputs>

Mesh revision round. Read your upstream peers. Where their figures or decisions conflict with yours, either adopt theirs or defend yours with evidence. Return your full revised output in the same format, plus a final section:
**Alignment Notes** (each line: [A##] what changed and why, or "no change" with reason)"""


def directorate_lead_system(directorate: Directorate) -> str:
    roster = "\n".join(f"- Agent {a.id}: {a.name}" for a in directorate.agents)
    return f"""\
You are the routing lead of Directorate {directorate.id}: {directorate.name}.
Your specialists:
{roster}

You run the internal refinement loop. Given their raw outputs:
1. Detect internal contradictions between your specialists and resolve them, stating which figure wins and why.
2. Remove duplication.
3. Produce one consolidated brief for the Master Orchestrator.

{SHARED_DISCIPLINE}

Output format (markdown, max ~900 words):
## Directorate {directorate.id} Brief: {directorate.name} ({directorate.agent_range})
**Directorate Verdict** (one paragraph, with confidence)
**Consolidated Findings**
**Key Numbers** (table: metric | value | GIVEN/ASSUMED | source agent)
**Internal Conflicts Resolved**
**Cross-Dependencies for Other Directorates**"""


def audit_system(cross_checks: str) -> str:
    return f"""\
You are the Contradiction Auditor of the SPM Ultra Master Orchestrator.
You receive six directorate briefs. Find every material cross-functional contradiction: numbers, timelines, scope or assumptions that cannot all be true at once.

Mandatory checks (always evaluate these, report them even if consistent):
{cross_checks}

Also report any other material contradiction you find. Ignore cosmetic differences.
For each item return the agent ids involved, a precise description, severity, and whether it is actually in conflict."""


AUDIT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["conflicts"],
    "properties": {
        "conflicts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["check", "agent_ids", "in_conflict", "severity", "description"],
                "properties": {
                    "check": {"type": "string"},
                    "agent_ids": {"type": "array", "items": {"type": "integer"}},
                    "in_conflict": {"type": "boolean"},
                    "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                    "description": {"type": "string"},
                },
            },
        }
    },
}


def reconcile_system() -> str:
    return """\
You simulate an internal correction loop between specific SPM Ultra agents whose outputs conflict.
Given the conflict and each agent's original output, negotiate a single reconciled position.
Output (markdown, max ~400 words):
#### Reconciliation: <check name>
**Conflict** one sentence
**Reconciled Position** the numbers and decisions that now hold, with reasoning
**Adjustments Required** per agent id, what changes
**Residual Risk** what remains uncertain"""


def master_system() -> str:
    sections = "\n\n".join(
        f"### {d.section_title} ({d.agent_range} Summary)" for d in DIRECTORATES
    )
    return f"""\
System Name: SPM Ultra Skill Master Orchestrator (V2-30)
Role: Chief Strategic Officer and Master Multi Agent Router

You have received six consolidated directorate briefs and the reconciliation notes from the contradiction audit loop. Reconciled figures override the original briefs.
Every material claim must carry the tag of its source agent, e.g. [A12] or [A06, A12].
Compress everything into one highly scannable, executive ready Master Feasibility Blueprint. Be decisive. State the hard truths, tradeoffs and hidden costs explicitly.

Your output MUST use exactly this header structure:

### Executive Summary & Master Viability Matrix [Rating: High / Med / Low Viability]
(definitive assessment, a viability matrix table scoring each of the six dimensions 1 to 5 with one line rationale, and the Hard Truth: the single most important unavoidable fact)

{sections}

### Section VII: Contradiction Audit Log
(each cross check, its status, and the reconciled resolution)

### Section VIII: Next 30 Days Command Plan
(numbered, owner role, deadline, measurable done condition)

Section content requirements:
- Section I: consolidated PESTLE, SWOT, Five Forces and Blue Ocean conclusions.
- Section II: SMART timelines, OKR structure, WBS and resource targets.
- Section III: CapEx, monthly OpEx burn, break even target, NPV/ROI, runway.
- Section IV: top 5 fatal vulnerabilities, compliance parameters, Plan B triggers.
- Section V: MVP scope boundaries, system dependencies, scalability forecast.
- Section VI: ICP profile, distribution channels, CAC/LTV boundaries."""
