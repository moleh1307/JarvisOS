---
title: Reference Router
description: How agents choose the right JARVIS OS reference files.
---

# Reference Router

JARVIS OS is modular. Agents should not load every rule for every task.

The Reference Router helps choose the smallest useful reference bundle.

## Routing Questions

Before deep work, ask:

- Does the message contain an actual task, or is it only a bare JARVIS OS invocation?
- Is this Light Mode or Specialist Mode?
- If Specialist Mode, what exact project or workflow is the target?
- Is this continuation, greenfield setup, adoption, public artifact, visual craft, QA, release, research, workflow feedback, or recovery?
- Does the task depend on tools or permissions?
- Does the task change durable memory?
- Could stale memory mislead the work?
- Which reference files are needed now?

## Common Routes

| Task | Reference |
| --- | --- |
| multiple skills apply | `references/skill-composition.md` |
| common task checklist | `references/task-cards.md` |
| bare JARVIS OS invocation with no task, mode, project, or target | stay in the main skill mode chooser and ask whether to use Core or Specialist Mode |
| work order lifecycle | `references/task-lifecycle.md` |
| memory writes or stale memory | `references/memory-discipline.md` |
| greenfield project setup | `references/greenfield.md` |
| existing project adoption | `references/adoption-takeover.md` |
| public-facing artifact | `references/public-artifacts.md` |
| visual/craft critical work | `references/creative-preproduction.md` and `references/visual-concept-pipeline.md` |
| continuation/status/closeout | `references/continuation.md` |
| self-improvement | `references/self-improvement-reflexes.md` |
| `JarvisOS Skill Ticket`, cross-project contribution, or skillset extraction | `references/cross-project-contributions.md` |
| skill or skillset creation/review | `references/skill-quality-standard.md` |
| bare Specialist Mode request with unclear target | stay in the main skill target gate and ask for the project/folder; do not bind to JARVIS R&D because `company/` exists |
| R&D loop | `references/rd-idea-loop.md` |

## Stop Rule

Stop retrieving when the next action can be handled with useful confidence.

Do not read more files just to feel exhaustive.
