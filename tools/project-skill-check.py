#!/usr/bin/env python3
"""Check basic structure for JarvisOS project-specific skills."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Status",
    "Owner",
    "Trigger",
    "Non-Triggers",
    "Local Context",
    "Ownership Boundary",
    "Delegation Boundary",
    "Hard Boundaries",
    "Default Workflow",
    "Outputs",
    "Verification",
    "Dogfood Evidence",
    "Sunset",
    "Promotion Lane",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def project_skills_dir(project_root: Path) -> Path:
    direct = project_root / "company" / "project-skills"
    if direct.exists():
        return direct
    return project_root


def has_heading(text: str, name: str) -> bool:
    return bool(re.search(rf"^##+\s+{re.escape(name)}\b", text, re.MULTILINE | re.IGNORECASE))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="Project root or project-skills directory")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    skills_dir = project_skills_dir(root)
    errors: list[str] = []
    warnings: list[str] = []

    if not skills_dir.exists():
        errors.append(f"Project skills directory does not exist: {skills_dir}")
    elif not skills_dir.is_dir():
        errors.append(f"Project skills path is not a directory: {skills_dir}")

    skill_files: list[Path] = []
    if not errors:
        skill_files = sorted(path for path in skills_dir.glob("*.md") if path.name not in {"index.md", "README.md"})
        if not skill_files:
            warnings.append(f"No project skill files found in {skills_dir}")

        if len(skill_files) >= 2 and not (skills_dir / "index.md").exists():
            errors.append("Two or more project skills exist but index.md is missing.")

        if (skills_dir / "index.md").exists():
            index_text = read_text(skills_dir / "index.md")
            for skill_file in skill_files:
                if skill_file.name not in index_text and skill_file.stem not in index_text:
                    warnings.append(f"Project skill may be missing from index.md: {skill_file.name}")

        for skill_file in skill_files:
            text = read_text(skill_file)
            if not re.search(r"^#\s+Project Skill:", text, re.MULTILINE):
                errors.append(f"{skill_file.name}: missing '# Project Skill:' title.")
            for section in REQUIRED_SECTIONS:
                if not has_heading(text, section):
                    errors.append(f"{skill_file.name}: missing section '{section}'.")
            if "TODO" in text or "TBD" in text:
                warnings.append(f"{skill_file.name}: contains TODO/TBD placeholder.")

    print("# Project Skill Check")
    print()
    print(f"Project root: `{root}`")
    print(f"Project skills directory: `{skills_dir}`")
    print(f"Project skill files: {len(skill_files)}")
    print()

    if errors:
        print("## Errors")
        for error in errors:
            print(f"- {error}")
        print()

    if warnings:
        print("## Warnings")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if not errors:
        print("Project skill structure passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
