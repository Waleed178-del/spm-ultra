from pathlib import Path

import pytest

from spm_ultra.diagrams import FILES, render_all
from spm_ultra.registry import DIRECTORATES, mesh_edges, tag

WORKFLOWS = Path(__file__).resolve().parent.parent / "workflows"


@pytest.mark.parametrize("name", list(FILES))
def test_committed_charts_are_up_to_date(name):
    path = WORKFLOWS / name
    assert path.exists(), f"missing {path}; run spm-ultra --write-diagrams"
    assert path.read_text() == FILES[name](), f"{name} is stale; run spm-ultra --write-diagrams"


def test_mesh_chart_contains_every_edge():
    text = render_all()["04-agent-mesh.md"]
    for src, dst in mesh_edges():
        assert f"{tag(src)} --> {tag(dst)}" in text


def test_every_agent_has_a_reference_card():
    text = render_all()["07-agent-reference.md"]
    for d in DIRECTORATES:
        for a in d.agents:
            assert f"### {tag(a.id)}: {a.name}" in text

