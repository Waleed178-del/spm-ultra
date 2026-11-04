"""Live tests against the Claude API: one real call per agent (30 calls).

Skipped unless SPM_LIVE=1 and ANTHROPIC_API_KEY are set, because every run costs money.

    SPM_LIVE=1 pytest tests/test_live_agents.py -n 8      # with pytest-xdist
    SPM_LIVE=1 pytest tests/test_live_agents.py -k "12"   # one agent
"""

import asyncio
import os
import re

import pytest

from spm_ultra.orchestrator import ClaudeLLM, MasterOrchestrator
from spm_ultra.registry import agent_by_id, all_agents, tag

pytestmark = pytest.mark.skipif(
    not (os.environ.get("SPM_LIVE") == "1" and os.environ.get("ANTHROPIC_API_KEY")),
    reason="live API test: set SPM_LIVE=1 and ANTHROPIC_API_KEY",
)

REFERENCE_IDEA = (
    "Launch a B2B appointment scheduling SaaS for independent dental clinics in the UAE and "
    "Saudi Arabia. Goal: 300 paying clinics in 12 months. Budget: 250,000 USD seed. "
    "Team: 2 engineers, 1 founder doing sales. Price idea: 79 USD per clinic per month."
)
REQUIRED = ("Key Findings", "Critical Assumptions", "Recommendations", "Cross-Dependencies",
            "References")


@pytest.mark.parametrize("aid", [a.id for a in all_agents()])
def test_live_agent_output_contract(aid):
    orch = MasterOrchestrator(ClaudeLLM(max_concurrency=1), worker_effort="low")
    out = asyncio.run(orch.run_agent(aid, REFERENCE_IDEA))

    assert f"{tag(aid)}: {agent_by_id(aid).name}" in out, "missing agent header"
    for section in REQUIRED:
        assert section in out, f"missing section {section}"
    assert re.search(r"\[A\d\d", out), "no peer referenced by tag"
    assert re.search(r"\d", out), "no quantified finding"
    assert "GIVEN" in out or "ASSUMED" in out, "figures not labelled GIVEN/ASSUMED"
