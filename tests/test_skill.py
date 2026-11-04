"""The Claude Code skill and plugin manifests stay consistent with the code."""

import json
import re
from pathlib import Path

import pytest

import spm_ultra
from spm_ultra.registry import DIRECTORATES, REFERENCES, all_agents, tag, upstream
from spm_ultra.skillgen import SKILL_DATA_RULE, agent_file, directorate_file, render_all

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "spm-ultra"
GENERATED = render_all()


@pytest.mark.parametrize("rel", sorted(GENERATED))
def test_reference_file_up_to_date(rel):
    path = SKILL / "references" / rel
    assert path.exists(), f"missing {path}; run spm-ultra --write-skill"
    assert path.read_text() == GENERATED[rel], f"{rel} is stale; run spm-ultra --write-skill"


def test_no_orphan_reference_files():
    on_disk = {p.relative_to(SKILL / "references").as_posix()
               for p in (SKILL / "references").rglob("*.md")}
    assert on_disk == set(GENERATED)


def test_skill_frontmatter():
    text = (SKILL / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "SKILL.md needs YAML frontmatter"
    fm = m.group(1)
    assert re.search(r"^name: spm-ultra$", fm, re.M)
    desc = re.search(r"^description: (.+)$", fm, re.M).group(1)
    assert 100 < len(desc) <= 1024


def test_skill_md_points_at_real_files():
    text = (SKILL / "SKILL.md").read_text()
    for ref in set(re.findall(r"references/[\w./-]+\.md", text)):
        assert (SKILL / ref).exists(), ref
    for folder in ("references/directorates/", "references/agents/"):
        assert folder in text and (SKILL / folder).is_dir()


@pytest.mark.parametrize("aid", [a.id for a in all_agents()])
def test_every_agent_has_skill_instructions(aid):
    a = next(x for x in all_agents() if x.id == aid)
    text = GENERATED[agent_file(a)]
    assert f"Agent {aid} [{tag(aid)}]" in text and a.mandate in text
    assert SKILL_DATA_RULE in text
    for r in REFERENCES[aid]:
        assert r in text
    mesh = GENERATED["mesh.md"]
    assert f"| {tag(aid)} | {a.name} | {', '.join(tag(u) for u in upstream(aid))} |" in mesh


@pytest.mark.parametrize("d", DIRECTORATES, ids=lambda d: d.key)
def test_directorate_file_lists_its_agents(d):
    text = GENERATED[directorate_file(d)]
    for a in d.agents:
        assert f"`references/{agent_file(a)}`" in text
    assert f"briefs/directorate_{d.id}.md" in text


def test_manifests_agree():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    entry = next(p for p in market["plugins"] if p["name"] == plugin["name"])
    assert plugin["version"] == entry["version"] == spm_ultra.__version__
    for s in plugin["skills"]:
        assert (ROOT / s / "SKILL.md").exists()
