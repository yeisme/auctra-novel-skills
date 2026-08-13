#!/usr/bin/env python3
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = sorted(ROOT.glob("*/*/SKILL.md"))
errors: list[str] = []

for skill_file in SKILL_FILES:
    skill_dir = skill_file.parent
    text = skill_file.read_text(encoding="utf-8")
    name = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
    description = re.search(r"^description:\s*([^\n]+)$", text, re.MULTILINE)
    if not name or name.group(1).strip() != skill_dir.name:
        errors.append(f"{skill_file}: frontmatter name must equal {skill_dir.name}")
    if not description or not description.group(1).strip():
        errors.append(f"{skill_file}: missing description")
    metadata = skill_dir / "agents" / "openai.yaml"
    if not metadata.is_file():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")

if len(SKILL_FILES) != 48:
    errors.append(f"expected 48 Skills, found {len(SKILL_FILES)}")

if errors:
    print("FAIL: Auctra Novel Skills validation failed")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"PASS: validated {len(SKILL_FILES)} Auctra Novel Skills")
