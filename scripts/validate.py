#!/usr/bin/env python3
"""Dependency-free structural and privacy checks for the public package."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "strategy-bp"
SKILL = PLUGIN / "skills" / "strategy-bp" / "SKILL.md"
REFERENCES = PLUGIN / "skills" / "strategy-bp" / "references"
EXPECTED_REFERENCES = {
    "commercial-viability.md",
    "competitor-research.md",
    "evidence-standard.md",
    "market-sizing.md",
    "research-protocol.md",
    "source-map.md",
    "user-research.md",
}
PRIVATE_PATTERNS = (
    re.compile(r"/Users/[^/\s]+"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|password|access[_-]?token)\s*[:=]\s*[^\s]+"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"validation failed: {message}")


manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
require(manifest["name"] == "strategy-bp", "unexpected plugin name")
require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]) is not None, "invalid version")
require(manifest["skills"] == "./skills/", "invalid skills path")
require(manifest["author"]["name"] == "Strategy BP", "unexpected public author")

marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())
require(marketplace["name"] == "strategy-bp", "unexpected marketplace name")
require(len(marketplace["plugins"]) == 1, "marketplace must contain one plugin")
require(marketplace["plugins"][0]["name"] == "strategy-bp", "unexpected marketplace plugin")

skill_text = SKILL.read_text()
require(skill_text.startswith("---\nname: strategy-bp\n"), "invalid Skill frontmatter")
require({path.name for path in REFERENCES.glob("*.md")} == EXPECTED_REFERENCES, "reference set mismatch")
for name in EXPECTED_REFERENCES:
    require(f"references/{name}" in skill_text, f"Skill does not route {name}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        raise SystemExit(f"validation failed: unexpected binary file: {path.relative_to(ROOT)}")
    for pattern in PRIVATE_PATTERNS:
        require(pattern.search(text) is None, f"private marker in {path.relative_to(ROOT)}")

print("Strategy BP package validation passed")
