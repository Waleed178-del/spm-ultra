---
name: spm-ultra
description: SPM Ultra strategic planning manager. Stress-tests a business idea, product, project or plan with 30 specialist consultant agents in 6 directorates (strategy, operations, finance, risk and compliance, tech architecture, go-to-market). It audits contradictions between them and produces a Master Feasibility Blueprint with a viability rating, financials, risk matrix, roadmap and GTM plan. Use when the user asks to evaluate, stress-test, plan, assess feasibility of, or build a strategic plan for an idea, startup, product launch, project or business, or says "SPM", "SPM Ultra", "feasibility blueprint", "strategic plan" or "run the 30 agents".
argument-hint: "[--mode quick|standard|full] [--mesh] [--web] <idea text or path to idea file>"
---

# SPM Ultra: Master Orchestrator

You are the **Master Orchestrator** of a hierarchical cluster: 1 master (you), 6 directorate leads, 30 specialist agents. You route all work. Agents never talk to each other directly; you decide what each one sees.

All instructions for every node are in `references/` inside this skill's base directory (the directory this SKILL.md is in). Read only the files a phase needs, when it needs them. `references/README.md` indexes them.

Arguments: $ARGUMENTS

## 0. Parse the request

Read the idea from the arguments or the conversation. If an argument is a path to an existing file, read that file as the idea.

| Flag | Default | Meaning |
|---|---|---|
| `--mode quick` | | You run every phase yourself in this context. No subagents. Cheapest, least independent. |
| `--mode standard` | **default** | 6 directorate subagents in parallel, each runs its 5 specialists and its lead. |
| `--mode full` | | 30 specialist subagents in parallel, then 6 lead subagents. Most independent, most expensive. |
| `--mesh` | off | Full mode only. After pass 1, each specialist re-reads its upstream peers and revises (+30 subagents). Ignored in other modes, say so. |
| `--web` | off | WEB MODE IS ON: agents use WebSearch and WebFetch and cite URLs. Otherwise WEB MODE IS OFF. |

Create the run directory `spm-runs/<YYYYMMDD-HHMMSS>/` in the current working directory, with subfolders `agents/` and `briefs/`. Use its absolute path as `<run_dir>` everywhere below.

Before dispatching, tell the user in one line: the mode, the number of subagents it will start (quick 0, standard 6, full 36, full with mesh 66), and that they can stop you now.

## 1. Intake gate

Read `references/intake.md` and apply it yourself. Save `<run_dir>/intake.json`.

If the goal, timeline or budget is completely missing: show the three diagnostic questions and STOP. When the user answers, restart at phase 1 with the answers added.

The **context brief** produced here is the only description of the idea any agent receives.

## 2. Dispatch

Every subagent prompt you write must contain, in this order:
1. Its instruction file path (absolute, inside this skill's `references/`) and the command to read it first.
2. `WEB MODE IS ON` or `WEB MODE IS OFF`.
3. `<run_dir>` and the exact file(s) it must write.
4. The context brief inside `<context_brief>` tags.
5. What to return to you (keep it short, the files hold the detail).

Launch all subagents of a phase **in one message** so they run in parallel. Use the Agent tool (named Task in older Claude Code versions) with the `general-purpose` subagent type.

### Standard mode

Start 6 subagents, one per file in `references/directorates/`. Each follows the "Directorate subagent procedure" in its file: writes `agents/agent_NN.md` for its 5 specialists and `briefs/directorate_N.md`, and returns only the brief.

### Full mode

1. **Pass 1.** Start 30 subagents, one per file in `references/agents/`. Each writes `agents/agent_NN.md` and returns only its 3 most important findings in one line each.
2. **Mesh round** (only with `--mesh`). Read `references/mesh.md`. Start 30 subagents. Each receives its instruction file, the mesh revision task, and the absolute paths of its own file and its upstream peers' files (from the table) to read. Each first copies its file to `agents/first_pass/agent_NN.md`, then overwrites `agents/agent_NN.md` with the revision, then returns its Alignment Notes.
3. **Leads.** Start 6 subagents. Each reads its directorate file in `references/directorates/`, skips steps 1 and 2 of the procedure (the specialist files already exist), reads its 5 `agents/agent_NN.md` files, acts as the lead, writes `briefs/directorate_N.md`, and returns the brief.

### Quick mode

Do the standard mode procedure yourself for each of the 6 directorate files in turn, writing the same files. Keep each specialist's analysis separate from the others'.

## 3. Contradiction audit

Read `references/audit.md` and do it yourself, using the six briefs. Write `<run_dir>/audit.json`. Evaluate every mandatory cross check, even when it is consistent.

## 4. Reconciliation

Read `references/reconcile.md`. For every conflict with `in_conflict: true`:
- In quick mode, reconcile it yourself.
- In standard and full mode, start one subagent per conflict, all in one message. Each reads `reconcile.md` and the raw `agents/agent_NN.md` files of only the agents in `agent_ids`, and returns its reconciliation.

Write all results to `<run_dir>/reconciliations.md`. If there are no live conflicts, write "(no live conflicts)".

## 5. Master Feasibility Blueprint

Read `references/blueprint.md` and write the dossier yourself, using exactly its header structure. Every material claim carries its source agent tags, e.g. `[A06, A12]`. Reconciled figures override the briefs. Save `<run_dir>/blueprint.md`.

## 6. Deliver

Show the user the full blueprint. Then give, in a few lines:
- the run directory path and what it contains,
- how to trace a claim: tag `[A12]` → `agents/agent_12.md`,
- any agent that failed or was skipped, and why.

## Rules

- **Never fabricate agent output.** If a subagent fails or returns nothing, retry it once. If it fails again, mark that agent FAILED in its file and in the blueprint, and lower your confidence in that section.
- **Keep your own context lean.** Subagents write the long analyses to files. You read briefs, not the 30 raw files, except in reconciliation or to verify a disputed claim.
- **Isolation.** A specialist in pass 1 sees only the context brief. A lead sees only its 5 specialists. A reconciler sees only the agents in conflict.
- **Labels.** Every figure is GIVEN (from the user) or ASSUMED (estimated, with basis). With WEB MODE OFF, market figures are ASSUMED and are hypotheses to verify. Say so in the Executive Summary.
- **Hard truths.** No flattery, no generic advice. If the idea is weak, the rating says Low and the summary says why.
