# How To Use SPM Ultra

Step by step recipes. For how the system is wired, see [`workflows/`](../workflows/README.md).

## 1. Install

```bash
git clone https://github.com/Waleed178-del/spm-ultra.git
```
```bash
cd spm-ultra && pip install -e '.[dev]'
```
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

## 2. Write a good idea brief

The intake gate needs three things. Missing any one stops the run with 3 diagnostic questions.

| Must state | Weak | Strong |
|---|---|---|
| Primary goal | "grow a business" | "300 paying clinics" |
| Timeline | "soon" | "12 months" |
| Budget | "some money" | "250,000 USD seed" |

Also state team size, price idea, geography and any hard constraint. Every fact you give becomes a GIVEN figure. Everything else becomes ASSUMED.

Save it as `idea.md`.

## 3. Choose a run mode

| Goal | Command | Calls |
|---|---|---|
| Check the plumbing, free | `spm-ultra --dry-run --file idea.md` | 0 real |
| Test one agent | `spm-ultra --agent 12 --file idea.md` | 1 |
| Cheap screening pass | `spm-ultra --file idea.md --worker-effort low` | about 40 |
| Standard analysis | `spm-ultra --file idea.md` | about 40 |
| Agents align with each other | `spm-ultra --file idea.md --mesh-rounds 1` | about 70 |
| With live cited web data | `spm-ultra --file idea.md --web` | about 40, plus searches |
| Maximum rigor | `spm-ultra --file idea.md --mesh-rounds 1 --web --worker-effort high` | about 70, plus searches |

Add `-v` to watch each agent dispatch and complete.

## 4. Answer the intake gate

If you see exit code 2 and three questions:

```bash
spm-ultra --file idea.md --answers "Goal: 300 clinics. Timeline: 12 months. Budget: 250k USD."
```

## 5. Read the output

Open `runs/<timestamp>/blueprint.md` first. Then trace any number backwards:

1. Find the tag next to the claim, e.g. `[A12]`.
2. Open `runs/<timestamp>/agents/agent_12.md` for the specialist's reasoning, assumptions and references.
3. If it was disputed, check `audit.json` and `reconciliations.md`.
4. With `--mesh-rounds`, compare `agents/first_pass/agent_12.md` with `agents/agent_12.md`. The **Alignment Notes** say what changed and which peer caused it.

## 6. Referencing

Every output carries three kinds of references:

| Kind | Where | Example |
|---|---|---|
| Peer tags | every agent and the blueprint | `[A06, A12]` |
| Framework references | each agent's **References** section | Porter, HBR (1979) |
| Web sources (`--web` only) | **Web Sources** list appended to the agent output | links to the pages cited |

Without `--web`, agents have no live data. Every market figure is ASSUMED and the agent states which source would confirm it. Treat these as hypotheses to verify.

## 7. Test the agents

Offline, no cost. Runs over 300 checks, about 12 per agent:

```bash
pytest
```

Live, one real API call per agent (30 calls). Checks that each agent returns its required sections, tags a peer, labels figures and quantifies:

```bash
SPM_LIVE=1 pytest tests/test_live_agents.py
```

One agent only:

```bash
SPM_LIVE=1 pytest tests/test_live_agents.py -k "12"
```

## 8. Customize

| Change | Edit | Then |
|---|---|---|
| An agent's mandate | `DIRECTORATES` in `spm_ultra/registry.py` | `pytest` |
| An agent's references | `REFERENCES` | `spm-ultra --write-diagrams` |
| Who reads whom (mesh) | `DEPENDENCIES` | `spm-ultra --write-diagrams`, `pytest` |
| Audit cross checks | `MANDATORY_CROSS_CHECKS` | `spm-ultra --write-diagrams` |
| Output format | `spm_ultra/prompts.py` | `pytest` |

The tests enforce the mesh rules: no self loops, no dead ends, every agent links to another directorate, and charts match the code.

## 9. Troubleshooting

| Symptom | Fix |
|---|---|
| HTTP 429 rate limit | `--concurrency 3` |
| `RefusalError` | Rephrase the idea, or check `stop_details` in the message |
| `hit max_tokens` warning | The output was cut off. Lower effort or shorten the idea |
| Fallback beta rejected by your account | `--no-fallback` |
| Blueprint feels generic | Add more GIVEN facts to the idea, use `--mesh-rounds 1` |
