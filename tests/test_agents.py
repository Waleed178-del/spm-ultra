"""Offline tests run once per agent (30 x each test). No API key needed."""

import asyncio

import pytest

from spm_ultra.orchestrator import MasterOrchestrator, MockLLM
from spm_ultra.prompts import agent_system, mesh_revision_user
from spm_ultra.registry import (DEPENDENCIES, DIRECTORATES, MANDATORY_CROSS_CHECKS, REFERENCES,
                                agent_by_id, all_agents, directorate_of, downstream, tag,
                                upstream)

AGENT_IDS = [a.id for a in all_agents()]
CONTEXT = "SENTINEL-CONTEXT: dental scheduling SaaS, GCC, 12 months, 250k USD"


@pytest.fixture(scope="module")
def full_run():
    llm = MockLLM(conflict_checks=len(MANDATORY_CROSS_CHECKS))
    result = asyncio.run(MasterOrchestrator(llm, mesh_rounds=1).run(CONTEXT))
    return llm, result


def _call(llm, prefix):
    matches = [c for c in llm.calls if c.label.startswith(prefix)]
    assert len(matches) == 1, f"expected exactly one call for {prefix!r}, got {len(matches)}"
    return matches[0]


# --------------------------------------------------------------------------- definition


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_definition_complete(aid):
    a = agent_by_id(aid)
    assert a.name.strip() and len(a.mandate) > 30
    assert REFERENCES[aid], "every agent needs at least one canonical reference"
    assert aid in DEPENDENCIES


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_mesh_links_valid(aid):
    ups = upstream(aid)
    assert ups, "every agent must read at least one peer"
    assert aid not in ups, "no self loops"
    assert len(set(ups)) == len(ups), "no duplicate links"
    assert all(1 <= u <= 30 for u in ups)
    assert downstream(aid), "every agent must feed at least one peer (no dead ends)"


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_reaches_other_directorates(aid):
    own = directorate_of(aid).id
    linked = {directorate_of(x).id for x in (*upstream(aid), *downstream(aid))}
    assert linked - {own}, "every agent must be wired to at least one other directorate"


# --------------------------------------------------------------------------- prompt


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_prompt_contents(aid):
    a, d = agent_by_id(aid), directorate_of(aid)
    p = agent_system(a, d)
    assert f"Agent {aid} [{tag(aid)}]" in p
    assert a.mandate in p and d.name in p
    for ref in REFERENCES[aid]:
        assert ref in p
    for u in upstream(aid):
        assert f"[{tag(u)}] {agent_by_id(u).name}" in p
    for x in downstream(aid):
        assert f"[{tag(x)}] {agent_by_id(x).name}" in p
    for section in ("Key Findings", "Critical Assumptions", "Recommendations",
                    "Cross-Dependencies", "References"):
        assert f"**{section}**" in p
    assert "no live data access" in p
    assert "web_search tool" in agent_system(a, d, web=True)


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_mesh_revision_payload(aid):
    peers = {u: f"OUT-{u}" for u in upstream(aid)}
    msg = mesh_revision_user(CONTEXT, f"OWN-{aid}", peers)
    assert CONTEXT in msg and f"OWN-{aid}" in msg and "Alignment Notes" in msg
    for u in upstream(aid):
        assert f'<peer tag="{tag(u)}"' in msg and f"OUT-{u}" in msg


# --------------------------------------------------------------------------- runtime routing


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_dispatched_once_with_context_only(full_run, aid):
    llm, _ = full_run
    c = _call(llm, f"agent {aid:02d} ")
    assert CONTEXT in c.user
    assert "<specialist_outputs>" not in c.user and "<peer" not in c.user, "pass 1 must be isolated"
    assert c.effort == "medium"


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_mesh_round_sees_exactly_upstream_peers(full_run, aid):
    llm, _ = full_run
    c = _call(llm, f"mesh {aid:02d} ")
    seen = {int(t[1:]) for t in __import__("re").findall(r'<peer tag="(A\d\d)"', c.user)}
    assert seen == set(upstream(aid))
    for u in upstream(aid):
        assert f"[mock output for agent {u:02d} " in c.user


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_agent_output_reaches_its_lead_only(full_run, aid):
    llm, result = full_run
    own = directorate_of(aid)
    marker = f"[mock output for mesh {aid:02d} "
    assert result.agent_outputs[aid].startswith(marker)
    assert result.first_pass[aid].startswith(f"[mock output for agent {aid:02d} ")
    for d in DIRECTORATES:
        lead = _call(llm, f"directorate {d.id} lead")
        assert (marker in lead.user) == (d.id == own.id)
    assert marker not in _call(llm, "audit").user
    assert marker not in _call(llm, "master blueprint").user


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_reconciliation_gets_raw_output_only_when_involved(full_run, aid):
    llm, _ = full_run
    marker = f"[mock output for mesh {aid:02d} "
    for name, left, right in MANDATORY_CROSS_CHECKS:
        c = _call(llm, f"reconcile: {name}")
        assert (marker in c.user) == (aid in (*left, *right))


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_single_agent_runner(aid):
    llm = MockLLM()
    out = asyncio.run(MasterOrchestrator(llm).run_agent(aid, CONTEXT))
    assert out == f"[mock output for agent {aid:02d} {agent_by_id(aid).name}]"
    assert llm.usage.calls == 1


@pytest.mark.parametrize("aid", AGENT_IDS)
def test_web_flag_reaches_agent(aid):
    llm = MockLLM()
    asyncio.run(MasterOrchestrator(llm, web_research=True).run_agent(aid, CONTEXT))
    assert llm.calls[0].web is True
    assert "web_search tool" in llm.calls[0].system
