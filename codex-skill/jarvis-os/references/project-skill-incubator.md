# Project Skill Incubator

Use this reference when a Specialist Mode project starts developing repeated project-local workflows that may deserve project-specific skills.

Project skills let a project team become sharper over time without polluting global JARVIS OS. They are local operating procedures with triggers, non-triggers, workflow, verification, and review triggers.

## Core Principle

Do not create a project skill because the team had one clever moment. Create one when repeated project-local work would be safer, faster, or higher-quality if captured as an executable local workflow.

Project skills are local by default. Promote them to global JarvisOS only after dogfood evidence or cross-project evidence.

## Storage

For Specialist Mode projects, store project skills under:

```text
<project-root>/company/project-skills/
```

Recommended files:

- `index.md`: compact dictionary of project skills;
- `<skill-slug>.md`: one project skill per file;
- optional `verification/`: diagnostic outputs from project-skill checks.

For non-Specialist projects, prefer a project note, checklist, or playbook first.

## Promotion Ladder

1. Observation: repeated friction, repair, or quality judgment.
2. Project playbook: lightweight checklist in project memory or a work order.
3. Project skill candidate: trigger, non-trigger, workflow, verification, and sunset trigger.
4. Dogfood: use the candidate on real project work.
5. Project skill: promote locally only if it improved execution.
6. Global candidate: create a JarvisOS Skill Ticket only if the pattern appears useful beyond this project.

## Creation Gate

Create a project skill only when all are true:

- the workflow is repeated or predictably recurring;
- the project has local context that a global skill would not know;
- manual repetition has meaningful cost or risk;
- the workflow can be written as executable steps;
- triggers and non-triggers are clear;
- outputs and verification are observable;
- the skill has a review/sunset trigger.

Use a project memory note, task checklist, or work-order acceptance criterion instead when the behavior is one-off, vague, mostly taste, or already covered by an installed/global skill.

## Project Skill Shape

Each project skill should include:

- title and status;
- owner role;
- trigger phrases or task moments;
- non-triggers;
- local context required;
- ownership and delegation boundaries;
- hard boundaries and no-fake rules;
- default workflow;
- expected outputs and artifact status;
- verification and repair path;
- dogfood evidence;
- sunset/review trigger;
- promotion lane: local-only, watch, or global-candidate.

Use the project skill template when available:

```text
templates/company-mode/project-skill.md
```

## Verification

When project skills exist, run the project-skill checker before closeout if the task creates, changes, promotes, retires, or relies on a project skill:

```bash
python3 tools/project-skill-check.py <project-root>
```

The checker validates structure and obvious drift. It does not replace dogfood evidence or role review.

## Use During Project Work

At the start of meaningful Specialist Mode work:

1. Check whether `company/project-skills/index.md` exists.
2. If it exists, scan it before choosing project workflow.
3. Use a project skill only if its trigger applies and it adds local context, constraints, or verification.
4. Prefer installed/global domain skills when the task is general and the project skill adds no local value.
5. If a project skill is stale or wrong, create a repair work order instead of silently following it.

Do not claim a project skill was used unless the index and the triggered project-skill file were actually read.

## Promotion To Global JARVIS

Promote a project skill to global JARVIS only when at least one is true:

- the same workflow appears in multiple projects;
- the user explicitly asks to generalize it;
- failure to generalize would likely repeat a high-impact mistake;
- a project skill has enough dogfood evidence to become a reusable domain skill.

Promotion path:

1. Create a JarvisOS Skill Ticket.
2. Apply Skill Quality Standard.
3. Run anti-bloat review.
4. Decide whether it belongs as global skill, JARVIS reference, template, checker, eval seed, or rejected/local-only pattern.

## Anti-Patterns

- Creating project skills for one-off tasks.
- Turning project taste into global rules.
- Making project skills so broad they trigger for everything.
- Letting stale project skills override live evidence.
- Duplicating installed/global skill instructions instead of referencing them.
- Claiming a project skill was used when the file was not read.
