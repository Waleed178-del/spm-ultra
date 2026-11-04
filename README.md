# SPM Ultra

**Strategic Planning Manager.** A hierarchical multi agent orchestrator that stress tests any idea across strategy, operations, finance, risk, technology and go to market, then compresses the result into one executive Master Feasibility Blueprint.

Built on the Claude API (`claude-opus-5-5` by default).

## Topology

A flat network of 30 agents causes token bottlenecks and conflicting directives. SPM Ultra uses a **Hierarchical Cluster Topography**: 30 specialists grouped into 6 directorates, each with a routing lead that reports to one Master Orchestrator.

```
                  [ 1 Master Orchestrator ]
                              │
   ┌──────────┬──────────┬────┴─────┬──────────┬──────────┐
   ▼          ▼          ▼          ▼          ▼          ▼
 Dir 1      Dir 2      Dir 3      Dir 4      Dir 5      Dir 6
Strategy  Operations  Finance   Risk/Legal  Tech/Arch    GTM
 A1–5      A6–10      A11–15    A16–20     A21–25     A26–30
```

| # | Directorate | Agents |
|---|---|---|
| 1 | Strategic & Market Intelligence | SWOT, PESTLE, Porter's Five Forces, Blue Ocean, Trend & Horizon |
| 2 | Operational Roadmap & Target Mapping | SMART, OKR Cascader, Sprint & WBS, Resource Allocation, Change Management |
| 3 | Financial Feasibility & Economic Modeling | CapEx, OpEx Runway, Break Even, Monetization, NPV & ROI |
| 4 | Risk, Compliance & Adversarial Stress Testing | Pre Mortem, Probability/Impact, Regulatory, SPOF Auditor, Disaster Recovery |
| 5 | Product, Tech Stack & Architecture | MVP Scope, Dependency Mapper, UX Flow, Scalability & Tech Debt, Vendor Evaluator |
| 6 | Commercialization & GTM | ICP Profiler, GTM Channels, Positioning, CAC vs LTV, Scale & Retention |

Full definitions live in [`spm_ultra/registry.py`](spm_ultra/registry.py). Run `spm-ultra --list-agents` to print the map.

## Lifecycle

```
Idea ─▶ Intake gate (goal / timeline / budget, else 3 diagnostic questions)
     ─▶ Parallel dispatch: 30 specialists run concurrently
     ─▶ 6 directorate leads run internal refinement and emit consolidated briefs
     ─▶ Contradiction audit (structured JSON) across all briefs
     ─▶ Reconciliation loops between the specific conflicting agents
     ─▶ Master Feasibility Blueprint
```

Mandatory cross checks (`MANDATORY_CROSS_CHECKS`):

- Operational Roadmap (A6–10) vs OpEx Runway (A12)
- Scale parameters (A24) vs CapEx (A11)
- Stack and vendor choices (A22, A25) vs OpEx (A12)
- CAC/LTV (A29) vs break even volume (A13)
- Compliance requirements (A18) vs MVP scope (A21)

## Install

```bash
git clone https://github.com/Waleed178-del/spm-ultra.git
cd spm-ultra
pip install -e '.[dev]'
export ANTHROPIC_API_KEY=sk-ant-...
```

## Use

```bash
spm-ultra "Launch a scheduling SaaS for dental clinics in the GCC. 12 month horizon, 250k USD seed budget."
```

```bash
spm-ultra --file idea.md -v --out runs/dental
```

If the intake gate finds the goal, timeline or budget missing, it prints three diagnostic questions and exits with code 2. Answer and rerun:

```bash
spm-ultra --file idea.md --answers "Goal: 500 paying clinics. Timeline: 18 months. Budget: 400k USD."
```

Offline smoke test of the whole pipeline (no API calls):

```bash
spm-ultra --dry-run "any idea"
```

### Output

Each run writes to `runs/<timestamp>/`:

| File | Content |
|---|---|
| `blueprint.md` | Final Master Feasibility Blueprint |
| `intake.json` | Normalized context brief |
| `agents/agent_XX.md` | Raw output of each of the 30 specialists |
| `briefs/directorate_N.md` | Consolidated directorate briefs |
| `audit.json` | Every cross check and its conflict status |
| `reconciliations.md` | Correction loop results |

Blueprint schema: Executive Summary & Viability Matrix, Sections I–VI (one per directorate), VII Contradiction Audit Log, VIII Next 30 Days Command Plan.

### Options

| Flag | Default | Purpose |
|---|---|---|
| `--model` | `claude-opus-5-5` | Model for every tier |
| `--concurrency` | 8 | Max simultaneous API calls (lower it if you hit 429s) |
| `--worker-effort` | medium | Effort for the 30 specialists |
| `--lead-effort` | high | Effort for directorate leads and reconciliations |
| `--master-effort` | high | Effort for audit and final blueprint |
| `--no-fallback` | off | Disable server side refusal fallback |

## Cost and latency

One run is about **40 API calls**: 1 intake, 30 specialists, 6 leads, 1 audit, 0 to 5 reconciliations, 1 master. Specialist calls are parallel, so wall time is roughly four sequential stages, not forty. Token spend scales with idea length and effort; lower `--worker-effort` to `low` for fast screening passes and keep `high` for decisions that matter.

## Use without code

[`prompts/master_orchestrator.md`](prompts/master_orchestrator.md) is a single paste ready system prompt that simulates the full cluster inside one chat. It is cheaper but weaker: one model simulating 30 agents in one context cannot run genuinely independent analyses or real reconciliation loops.

## Library use

```python
import asyncio
from spm_ultra import ClaudeLLM, MasterOrchestrator

result = asyncio.run(MasterOrchestrator(ClaudeLLM()).run("your idea"))
print(result.blueprint)
```

## Tests

```bash
pytest
```

## License

MIT
