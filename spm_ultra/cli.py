"""Command line entry point: `spm-ultra "your idea"`."""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from datetime import datetime
from pathlib import Path

from .orchestrator import DEFAULT_MODEL, ClaudeLLM, MasterOrchestrator, MockLLM
from .registry import DIRECTORATES


def _parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="spm-ultra",
                                description="SPM Ultra: 30 agent strategic planning orchestrator")
    p.add_argument("idea", nargs="?", help="Idea text, or omit and use --file / stdin")
    p.add_argument("-f", "--file", type=Path, help="Read the idea from a file")
    p.add_argument("-a", "--answers", help="Answers to the intake diagnostic questions")
    p.add_argument("-o", "--out", type=Path, help="Output directory (default runs/<timestamp>)")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--concurrency", type=int, default=8, help="Max simultaneous API calls")
    p.add_argument("--worker-effort", default="medium",
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--lead-effort", default="high",
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--master-effort", default="high",
                   choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--mesh-rounds", type=int, default=0,
                   help="Peer mesh revision rounds: each agent re-reads its upstream peers (+30 calls per round)")
    p.add_argument("--web", action="store_true",
                   help="Give specialists the web_search tool and append cited sources")
    p.add_argument("--agent", type=int, metavar="N",
                   help="Run only specialist N (1-30) against the idea, skipping intake. For testing")
    p.add_argument("--write-diagrams", type=Path, nargs="?", const=Path("workflows"), metavar="DIR",
                   help="Regenerate the workflow charts from the registry and exit")
    p.add_argument("--write-skill", type=Path, nargs="?", const=Path("skills/spm-ultra"),
                   metavar="DIR", help="Regenerate the Claude Code skill references and exit")
    p.add_argument("--no-fallback", action="store_true",
                   help="Disable server side refusal fallback")
    p.add_argument("--dry-run", action="store_true", help="Run the full pipeline offline with a mock model")
    p.add_argument("--list-agents", action="store_true", help="Print the cluster map and exit")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args()


def _print_map() -> None:
    print("[ 1 Master Orchestrator ]")
    for d in DIRECTORATES:
        print(f"  Directorate {d.id}: {d.name} ({d.agent_range})")
        for a in d.agents:
            print(f"    {a.id:>2}. {a.name}")


def main() -> int:
    args = _parse()
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    if args.list_agents:
        _print_map()
        return 0
    if args.write_skill:
        from .skillgen import write_all as write_skill
        print(f"{len(write_skill(args.write_skill))} files written to {args.write_skill}/references")
        return 0
    if args.write_diagrams:
        from .diagrams import write_all
        for path in write_all(args.write_diagrams):
            print(path)
        return 0

    if args.file:
        idea = args.file.read_text()
    elif args.idea:
        idea = args.idea
    elif not sys.stdin.isatty():
        idea = sys.stdin.read()
    else:
        print("error: provide an idea, --file, or pipe text on stdin", file=sys.stderr)
        return 1

    llm = MockLLM() if args.dry_run else ClaudeLLM(
        model=args.model, max_concurrency=args.concurrency, use_fallbacks=not args.no_fallback)
    orch = MasterOrchestrator(llm, worker_effort=args.worker_effort,
                              lead_effort=args.lead_effort, master_effort=args.master_effort,
                              mesh_rounds=args.mesh_rounds, web_research=args.web)
    if args.agent is not None:
        if not 1 <= args.agent <= 30:
            print("error: --agent must be 1 to 30", file=sys.stderr)
            return 1
        print(asyncio.run(orch.run_agent(args.agent, idea)))
        return 0
    result = asyncio.run(orch.run(idea, args.answers))

    if not result.intake.ready:
        print("Intake gate: baseline metrics missing. Answer these and rerun with --answers:\n")
        for i, q in enumerate(result.intake.diagnostic_questions, 1):
            print(f"  {i}. {q}")
        return 2

    out = args.out or Path("runs") / datetime.now().strftime("%Y%m%d-%H%M%S")
    result.save(out)
    print(result.blueprint)
    u = llm.usage
    print(f"\n---\nSaved to {out}/  |  calls={u.calls} in={u.input_tokens} out={u.output_tokens}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
