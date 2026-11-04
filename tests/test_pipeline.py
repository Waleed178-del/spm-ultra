import asyncio

from spm_ultra.orchestrator import MasterOrchestrator, MockLLM
from spm_ultra.prompts import master_system
from spm_ultra.registry import DIRECTORATES, MANDATORY_CROSS_CHECKS, all_agents


def test_topology_is_6_by_5():
    assert len(DIRECTORATES) == 6
    assert all(len(d.agents) == 5 for d in DIRECTORATES)
    assert [a.id for a in all_agents()] == list(range(1, 31))


def test_cross_checks_reference_real_agents():
    for _, left, right in MANDATORY_CROSS_CHECKS:
        assert all(1 <= i <= 30 for i in (*left, *right))


def test_master_prompt_has_all_sections():
    text = master_system()
    for d in DIRECTORATES:
        assert d.section_title in text
    assert "Executive Summary & Master Viability Matrix" in text


def test_full_pipeline_dry_run(tmp_path):
    llm = MockLLM()
    result = asyncio.run(MasterOrchestrator(llm).run("Launch a B2B SaaS for clinics"))
    assert len(result.agent_outputs) == 30
    assert len(result.briefs) == 6
    live = [c for c in result.conflicts if c["in_conflict"]]
    assert len(result.reconciliations) == len(live) == 1
    # intake + 30 agents + 6 leads + audit + reconciliations + master
    assert llm.usage.calls == 1 + 30 + 6 + 1 + len(live) + 1
    result.save(tmp_path)
    assert (tmp_path / "blueprint.md").exists()
    assert len(list((tmp_path / "agents").iterdir())) == 30


def test_mesh_round_adds_30_calls(tmp_path):
    llm = MockLLM()
    result = asyncio.run(MasterOrchestrator(llm, mesh_rounds=1).run("idea"))
    assert llm.usage.calls == 1 + 30 + 30 + 6 + 1 + 1 + 1
    assert len(result.first_pass) == 30
    result.save(tmp_path)
    assert len(list((tmp_path / "agents" / "first_pass").iterdir())) == 30
