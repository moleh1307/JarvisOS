---
title: Project Skill Incubator
description: How Specialist Mode projects can grow local project skills without bloating global JARVIS OS.
---

# Project Skill Incubator

Project Skill Incubator is for repeated project-local workflows.

It lets a project team become sharper over time while keeping global JARVIS OS clean. The default path is local first: capture the workflow inside the project, dogfood it, and only promote it globally if evidence proves it generalizes.

## Use It When

- A Specialist Mode project repeats the same workflow, repair, QA check, or local judgment.
- The workflow depends on local project context.
- Doing it manually creates meaningful cost or risk.
- The project team can write executable steps and verification.

## Do Not Use It When

- The task is one-off.
- A normal work-order checklist is enough.
- An installed/global skill already owns the workflow.
- The proposed skill is broad advice rather than executable procedure.

## Storage

Store project skills under:

```text
<project-root>/company/project-skills/
```

Recommended files:

- `index.md`: compact project skill dictionary.
- `<skill-slug>.md`: one local project skill.
- `verification/`: optional diagnostic outputs.

## Promotion Ladder

1. Observation.
2. Project playbook/checklist.
3. Project skill candidate.
4. Dogfood on real project work.
5. Active local project skill.
6. JarvisOS Skill Ticket only when cross-project value appears.

## Verification

Use the checker when project skills are created, changed, promoted, retired, or relied on:

```bash
python3 tools/project-skill-check.py <project-root>
```

The checker validates structure. It does not replace dogfood evidence, project judgment, or stale-skill review.

## Promotion

Promote a project skill to global JARVIS only when:

- the same workflow appears in multiple projects;
- the user explicitly asks to generalize it;
- the failure mode is high-impact enough to justify global behavior;
- dogfood evidence shows the skill works beyond one local trick.

Otherwise keep it local.
