# Skill Dictionary

Use this dictionary when a task may match a standalone/domain skill and the user has not named the skill explicitly.

The live Codex skill list remains authoritative for what is actually available in a session. This dictionary is a compact routing aid so agents can choose intelligently without reading every `SKILL.md`.

## Routing Contract

1. Scan this dictionary when the task is research, math, paper review, knowledge-base work, skill work, plugin/tool work, visual asset work, or another specialized workflow.
2. Pick at most one lead skill for the main deliverable.
3. Add supporting skills only when they uniquely improve a subtask.
4. Read only the chosen candidate skill files, plus narrow references only when triggered.
5. If no dictionary entry fits, use normal JarvisOS routing and the live skill list.
6. Do not claim a skill was used unless its instructions were read and materially followed.

## Maintenance Rule

When a project creates, installs, removes, renames, or materially changes a skill, update the local Skill Dictionary in the same work order.

Use a dictionary check when available:

```bash
python3 tools/skill-dictionary-check.py
```

For local deployments with additional installed skills, pass the skills root:

```bash
python3 tools/skill-dictionary-check.py --skills-root "$HOME/.codex/skills"
```

## Entry Template

Copy this shape for local/domain skills. Keep entries short enough to scan.

```markdown
- Skill: `skill-name`
  - Lane: domain / workflow area.
  - Lead when: the skill owns the main deliverable.
  - Support when: the skill uniquely improves a subtask.
  - Do not use when: common false trigger.
  - Read first: `SKILL.md`; deeper references only when triggered.
  - Path: `~/.codex/skills/skill-name/SKILL.md`
```

## Skill Families

Use the live skill list first, then treat these as routing families:

- JARVIS continuity/governance skills: lead project memory, Specialist Mode, handoffs, work orders, closeout, and R&D governance.
- Research/domain skills: lead the subject-specific method, rubric, verification, and output format.
- Skill creation/installation skills: lead creating, installing, or updating reusable Codex skills.
- Visual/image skills: lead bitmap generation, image editing, art-direction-specific asset work, or visual UI craft when directly relevant.
- Browser/GitHub/mail/calendar/document/spreadsheet/presentation/plugin skills: lead tool-specific operations when the relevant plugin is available.

JarvisOS supports domain/plugin skills with memory, artifact hygiene, approval boundaries, and closeout. It should not replace the domain skill's technical method.

## Project-Specific Skills

Some Specialist Mode projects may define local project skills under `company/project-skills/`.

Use them when:

- the active project has `company/project-skills/index.md`;
- the index trigger matches the current project task;
- the project skill adds local context or local verification beyond installed/global skills.

Do not use them when:

- an installed/global skill fully owns the task and the project skill adds no local value;
- the project skill is stale, contradicted by current project evidence, or marked retired;
- the task is one-off and a work-order checklist is enough.

When project skills are created or updated, use `project-skill-incubator.md` and run the project-skill checker.
