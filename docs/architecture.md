# Architecture

## Tiers

| Tier | Count | Code | Effort | Role |
|---|---|---|---|---|
| Intake gate | 1 | `MasterOrchestrator.intake` | medium | Structured JSON: ready flag, 3 diagnostic questions, normalized context brief |
| Specialists | 30 | `_run_directorate` | worker (medium) | One narrow mandate each, quantified markdown |
| Directorate leads | 6 | `_run_directorate` | lead (high) | Internal refinement loop, consolidated brief |
| Auditor | 1 | `_audit` | master (high) | Structured JSON list of cross checks and conflicts |
| Reconcilers | 0 to N | `_reconcile` | lead (high) | Correction loop fed the raw outputs of only the conflicting agents |
| Master | 1 | `_blueprint` | master (high) | Final dossier, reconciled figures override briefs |

## Context isolation

Specialists see only the context brief. Leads see the brief plus their 5 specialists. The master sees the 6 briefs, never the 30 raw outputs. This is the token bottleneck control: the final call reads roughly 6 briefs instead of 30 reports.

Reconcilers are the exception. They receive the raw outputs of the specific agents in conflict, because reconciling numbers needs the original evidence, not a summary.

## Reliability

- Every call streams (`get_final_message`) to avoid HTTP timeouts on long outputs.
- Adaptive thinking on every call. Depth is controlled by `effort` per tier.
- Server side refusal fallback (`fallbacks: "default"`) is on by default. A refusal that survives fallback raises `RefusalError`.
- `max_tokens` truncation is logged as a warning.
- A semaphore caps concurrency (`--concurrency`) so 30 parallel calls do not trip rate limits.

## Extending

- Add or edit agents in `registry.py`. Topology tests assert 6 x 5 with ids 1 to 30; update them if you change the shape.
- Add cross checks to `MANDATORY_CROSS_CHECKS`.
- Swap backends by implementing the `LLM` protocol (`complete(system, user, effort, max_tokens, schema, label)`).
