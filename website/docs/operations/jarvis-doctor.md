---
sidebar_position: 5
---

# Jarvis Doctor

Jarvis Doctor is a deterministic public-template diagnostic.

Run it before committing or pushing public-safe JarvisOS changes:

```bash
python tools/jarvis-doctor.py
```

It checks common closeout mistakes:

- required public-template files exist;
- `VERSION`, README badge, changelog, and website package metadata agree;
- `jarvis-os` references named in the skill/router exist;
- Docusaurus sidebar doc IDs point to real docs;
- obvious private/local path and secret patterns are absent;
- git worktree/branch state is visible.

Jarvis Doctor reduces agent memory burden. It turns several manual checks into one command.

## What It Does Not Replace

It does not replace:

- Docusaurus build;
- tests or lint;
- rendered screenshot QA;
- release review;
- human judgment;
- private stale-dashboard checks inside Melih's live vault.

For docs changes, still run:

```bash
cd website
npm run build
```

For public releases, still verify git status, commit, and push deliberately.

## Expected Result

A clean run prints:

```text
No blocking structural issues found.
```

Warnings can still appear for non-blocking issues such as a dirty worktree before commit.

