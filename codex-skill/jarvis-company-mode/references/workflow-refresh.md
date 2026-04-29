# Workflow Refresh

Use this when an older active Specialist Mode / Company Mode chat needs to adopt newer installed JARVIS rules without restarting the whole project.

The goal is to reconcile the live project state with the latest workflow, then continue. It is not a license to rewrite the project, dump the whole rule list into chat, or create a second company layer.

## Triggers

Run this playbook when:

- the user says `workflow refresh`;
- JARVIS or Specialist Mode / Company Mode was updated while an older project chat stayed active;
- the project has stale behavior such as passive `ok` replies, missing role headers, missing operating mode, stale review gates, or outdated GitHub/version/QA assumptions;
- the project is missing newer but relevant `company/` fields.

## Refresh Procedure

1. Start with a roster-backed role header. Use Chief of Staff for normal refresh/routing, Skill Engineer for skill/template fixes, Workflow Architect for workflow diagnosis.
2. Read the latest installed `jarvis` and `jarvis-company-mode` `SKILL.md` files.
3. Read live project state:
   - `company/team-roster.md` if it exists
   - `company/current-state.md`
   - `company/task-board.md`
   - `company/integration-log.md` if it exists
   - active work order and relevant role memory
   - `README.md`, `CHANGELOG.md`, or version files when repo/public status matters
4. Detect only consequential gaps. Common gaps:
   - missing or stale roster-backed role headers;
   - missing `Operating mode`;
   - stale `ready-for-user-review` gates where internal review should apply;
   - passive acknowledgement behavior;
   - vague next tasks such as "Founder should...";
   - stale README/changelog/version/QA/GitHub state.
5. If files need changes, create or use a small workflow-refresh work order. Preserve the interrupted/active task.
6. Patch the smallest durable state needed:
   - add missing current-state fields that affect routing;
   - update task-board status and exact next task;
   - update role memory only if role behavior/state materially changed;
   - update visible repo docs only when public/project status changed.
7. Continue the next unblocked task under the latest rules. Do not stop at "refresh complete" if the project can continue.

## What Not To Do

- Do not paste the full Specialist Mode / Company Mode rule set into the README, chat, or project state.
- Do not rewrite all company files just because the skill changed.
- Do not create a new company layer when one already exists.
- Do not ask the user for routine approval to update workflow state.
- Do not change source/product/research work during refresh unless the active work order requires it.

## Completion Report

Report compactly:

- refreshed files or "no file changes needed";
- adopted workflow deltas in short form, not a copied rule list;
- verification performed;
- blockers, if any;
- `Next task:` with the exact next work order or action.

Use `Decision needed:` only when refresh exposes a real escalation boundary such as destructive changes, credentials/cost, private-memory risk, protected-branch risk, or a strategic direction conflict.
