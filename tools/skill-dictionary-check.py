#!/usr/bin/env python3
"""Check JarvisOS Skill Dictionary syntax and optional installed-skill coverage."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "codex-skill/jarvis-os/SKILL.md").exists() and (candidate / "VERSION").exists():
            return candidate
    raise SystemExit("Could not find JarvisOS public template root.")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_name(skill_md: Path) -> str | None:
    text = read_text(skill_md)
    if not text.startswith("---"):
        return None
    match = re.search(r"^name:\s*['\"]?([^'\"\n]+)['\"]?\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def installed_skills(root: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for skill_md in sorted(root.rglob("SKILL.md")):
        name = frontmatter_name(skill_md)
        if name:
            found[name] = skill_md
    return found


def dictionary_entries(path: Path) -> tuple[set[str], dict[str, str]]:
    text = read_text(path)
    names = set(re.findall(r"^- Skill:\s*`([^`<>]+)`\s*$", text, re.MULTILINE))
    paths = {
        name: value
        for name, value in re.findall(
            r"^- Skill:\s*`([^`<>]+)`\s*$.*?^\s+- Path:\s*`([^`]+)`\s*$",
            text,
            re.MULTILINE | re.DOTALL,
        )
    }
    return names, paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dictionary", default=None, help="Path to skill-dictionary.md")
    parser.add_argument("--skills-root", default=None, help="Optional installed skills root for coverage checks")
    parser.add_argument("--ignore", action="append", default=[])
    args = parser.parse_args()

    root = find_root(Path.cwd())
    dictionary = Path(args.dictionary).expanduser() if args.dictionary else root / "codex-skill/jarvis-os/references/skill-dictionary.md"

    errors: list[str] = []
    warnings: list[str] = []

    if not dictionary.exists():
        errors.append(f"Dictionary does not exist: {dictionary}")
    else:
        entries, entry_paths = dictionary_entries(dictionary)
        if "Skill Dictionary" not in read_text(dictionary):
            errors.append("Dictionary does not appear to be the JarvisOS Skill Dictionary.")

        for name, raw_path in sorted(entry_paths.items()):
            if "<" in raw_path or raw_path.startswith("~/.codex/skills/skill-name"):
                continue
            target = Path(raw_path).expanduser()
            if target.is_absolute() and not target.exists():
                warnings.append(f"Absolute path for {name} does not exist on this machine: {raw_path}")

        if args.skills_root:
            skills_root = Path(args.skills_root).expanduser()
            if not skills_root.exists():
                errors.append(f"Skills root does not exist: {skills_root}")
            else:
                installed = installed_skills(skills_root)
                ignored = set(args.ignore)
                missing = sorted(set(installed) - entries - ignored)
                for name in missing:
                    errors.append(f"Installed skill missing from dictionary: {name} ({installed[name]})")

    print("# Skill Dictionary Check")
    print()
    print(f"Dictionary: `{dictionary}`")
    if args.skills_root:
        print(f"Skills root: `{Path(args.skills_root).expanduser()}`")
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
        print("Skill Dictionary check passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
