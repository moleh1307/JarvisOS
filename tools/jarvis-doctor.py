#!/usr/bin/env python3
"""JarvisOS public-template diagnostic.

Run from the public template root:

    python tools/jarvis-doctor.py

The doctor checks the public-safe surfaces agents commonly forget before
commit/push. It does not replace project tests, Docusaurus builds, or human
review; it catches structural drift and obvious private leaks.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable


ROOT_MARKERS = ["AGENTS.md", "README.md", "VERSION", "codex-skill/jarvis-os/SKILL.md"]
REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "VERSION",
    "CHANGELOG.md",
    "codex-skill/jarvis-os/SKILL.md",
    "codex-skill/jarvis-os/references/skill-dictionary.md",
    "codex-skill/jarvis-os/references/reference-router.md",
    "codex-skill/jarvis-os/references/task-cards.md",
    "templates/company-mode/work-order.md",
    "tools/skill-dictionary-check.py",
    "website/sidebars.js",
    "website/package.json",
]
IGNORED_PARTS = {".git", "node_modules", "build", ".docusaurus"}
PRIVATE_PATTERNS = [
    r"/Users/",
    r"Desktop/JARVIS",
    r"/Volumes/",
    r"melihkarakose",
    r"academic-paper-review",
    r"(?:API[_-]?KEY|SECRET|TOKEN|PASSWORD)\s*[:=]",
]
ALLOWED_PRIVATE_MATCHES = [
    "~/.codex",
    "$HOME/.codex",
    "id-token:",
]


def find_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate
    raise SystemExit("Could not find JarvisOS public template root.")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def iter_text_files(root: Path) -> Iterable[Path]:
    suffixes = {".md", ".mdx", ".txt", ".json", ".js", ".jsx", ".ts", ".tsx", ".yml", ".yaml", ".toml", ".py"}
    for path in root.rglob("*"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        if path.name == "package-lock.json":
            continue
        if path == root / "tools/jarvis-doctor.py":
            continue
        if path.is_file() and (path.suffix in suffixes or path.name in {"VERSION", "README", "CHANGELOG"}):
            yield path


def run_git(root: Path, *args: str) -> str | None:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=str(root),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.strip()


def check_required_paths(root: Path, errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            errors.append(f"Missing required path: {rel}")


def check_version(root: Path, errors: list[str], warnings: list[str]) -> None:
    version_path = root / "VERSION"
    if not version_path.exists():
        return
    version = read_text(version_path).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"VERSION is not semver-like: {version!r}")
        return

    readme = read_text(root / "README.md") if (root / "README.md").exists() else ""
    changelog = read_text(root / "CHANGELOG.md") if (root / "CHANGELOG.md").exists() else ""
    package_json_path = root / "website/package.json"
    package_lock_path = root / "website/package-lock.json"

    if f"version-{version}" not in readme and f"version: {version}" not in readme:
        errors.append(f"README does not appear to show version {version}.")
    if f"## {version} " not in changelog and f"## {version} -" not in changelog:
        errors.append(f"CHANGELOG has no top-level entry for {version}.")

    for path in [package_json_path, package_lock_path]:
        if path.exists():
            try:
                data = json.loads(read_text(path))
            except json.JSONDecodeError as exc:
                errors.append(f"{path.relative_to(root)} is not valid JSON: {exc}")
                continue
            if data.get("version") != version:
                errors.append(f"{path.relative_to(root)} version is {data.get('version')!r}, expected {version!r}.")
            if path.name == "package-lock.json":
                root_pkg = data.get("packages", {}).get("", {})
                if root_pkg.get("version") != version:
                    errors.append(f"website/package-lock.json root package version is {root_pkg.get('version')!r}, expected {version!r}.")

    if version.endswith(".0"):
        warnings.append("VERSION ends in .0; verify this was intentional for a public patch.")


def check_skill_references(root: Path, errors: list[str]) -> None:
    skill_path = root / "codex-skill/jarvis-os/SKILL.md"
    if not skill_path.exists():
        return
    text = read_text(skill_path)
    refs = sorted(set(re.findall(r"`(references/[^`]+?\.md)`", text)))
    for ref in refs:
        if not (skill_path.parent / ref).exists():
            errors.append(f"SKILL.md references missing file: {ref}")

    router_path = skill_path.parent / "references/reference-router.md"
    if router_path.exists():
        router = read_text(router_path)
        refs.extend(re.findall(r"`([^`]+?\.md)`", router))
        for ref in sorted(set(refs)):
            if ref == "SKILL.md":
                continue
            if ref.startswith("references/"):
                target = skill_path.parent / ref
            elif "/" not in ref and (router_path.parent / ref).exists():
                target = router_path.parent / ref
            else:
                continue
            if not target.exists():
                errors.append(f"Reference router mentions missing file: {ref}")


def check_sidebar(root: Path, errors: list[str]) -> None:
    sidebar_path = root / "website/sidebars.js"
    docs_root = root / "website/docs"
    if not sidebar_path.exists() or not docs_root.exists():
        return
    text = read_text(sidebar_path)
    ids = re.findall(r"'([^']+)'", text)
    for doc_id in ids:
        # Ignore labels and non-doc string values by requiring slash-free docs or known doc paths.
        candidates = [docs_root / f"{doc_id}.md", docs_root / f"{doc_id}.mdx", docs_root / doc_id / "index.md"]
        if "/" in doc_id or any((docs_root / f"{doc_id}{ext}").exists() for ext in [".md", ".mdx"]):
            if not any(path.exists() for path in candidates):
                errors.append(f"Sidebar doc id has no matching doc file: {doc_id}")


def check_private_leaks(root: Path, errors: list[str]) -> None:
    compiled = [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in PRIVATE_PATTERNS]
    for path in iter_text_files(root):
        rel = path.relative_to(root)
        text = read_text(path)
        for line_no, line in enumerate(text.splitlines(), start=1):
            if any(allowed in line for allowed in ALLOWED_PRIVATE_MATCHES):
                continue
            for label, pattern in compiled:
                if pattern.search(line):
                    errors.append(f"Possible private/local leak {label!r} at {rel}:{line_no}")


def check_git(root: Path, warnings: list[str]) -> None:
    status = run_git(root, "status", "--short")
    if status is None:
        warnings.append("Git status unavailable.")
    elif status:
        warnings.append("Git worktree is dirty.")

    branch = run_git(root, "branch", "--show-current")
    if branch and branch != "main":
        warnings.append(f"Current branch is {branch!r}, not 'main'.")


def main() -> int:
    root = find_root(Path.cwd())
    errors: list[str] = []
    warnings: list[str] = []

    check_required_paths(root, errors)
    check_version(root, errors, warnings)
    check_skill_references(root, errors)
    check_sidebar(root, errors)
    check_private_leaks(root, errors)
    check_git(root, warnings)

    print("# JarvisOS Doctor")
    print()
    print(f"Root: `{root}`")
    print()

    if errors:
        print("## Errors")
        for item in errors:
            print(f"- {item}")
        print()

    if warnings:
        print("## Warnings")
        for item in warnings:
            print(f"- {item}")
        print()

    if not errors:
        print("No blocking structural issues found.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
