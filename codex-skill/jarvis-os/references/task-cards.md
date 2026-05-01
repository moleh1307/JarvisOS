# Task Cards

Use this reference when the task type is clear but the agent would otherwise need to synthesize many JARVIS OS rules before acting.

Task cards are compact execution checklists. They do not replace deeper references. If a card exposes higher risk, missing capability, stale state, public release risk, or consequential claims, route to the relevant reference and continue there.

## How To Use A Card

1. Pick exactly one primary card for the current task.
2. Add one secondary card only if the work genuinely spans two task types.
3. Run the checks proportionally; skip cards for trivial self-contained work.
4. If a check reveals drift, blocker, or risk, fix it or route to the deeper reference.
5. Close with the smallest durable state update that future continuation needs.

## Coding Fix Card

- Identify the repo, branch, changed files, and user-visible behavior before editing.
- Read the smallest relevant code path plus existing tests or local patterns.
- Preserve unrelated user changes; do not revert dirty work you did not create.
- Make the narrowest fix that matches the repo style.
- Run the most relevant test, typecheck, lint, build, or smoke command available.
- Report what changed, what passed, and any verification you could not run.
- Update memory only if project state, blockers, decisions, or next steps changed.

## Research Output Card

- State the question, audience, deliverable shape, and confidence standard.
- Identify source lanes: user-provided, local corpus, repo data, external sources, or assumptions.
- Separate verified findings from working assumptions and speculation.
- Preserve provenance for important claims, data, methods, and caveats.
- Attack consequential claims before promoting them into project truth.
- Produce the requested artifact in the canonical project location.
- Close with remaining uncertainties, next research step, and artifact status.

## Public Artifact Card

- Identify who will read it and what decision or action it should support.
- Inspect any named URL, screenshot, repo, brand, document, or reference before finalizing.
- Keep public claims honest; do not invent adoption, metrics, credentials, or proof.
- Check privacy boundaries and avoid private memory leakage.
- Verify the exact local artifact, render, preview, or deployed surface when feasible.
- Distinguish local latest from production/deployed state.
- Close with the artifact path, verification, and any real release/deploy decision needed.

## Adoption Audit Card

- Preserve the existing project before reshaping it; observe first.
- Identify repo/workspace purpose, current status, tech/data stack, and sensitive boundaries.
- Separate observed facts from agent inferences.
- Create the smallest useful Specialist Layer: current state, task board, charter/audit, and work orders only if needed.
- Record baseline commands, tests, artifacts, and known risks.
- Choose Light Mode, Minimal Specialist Layer, or Full Specialist Layer from actual complexity.
- End with exact next work order, blocker, or decision needed.

## Fresh Continuation Card

- Read the active project index/current-state first, then the latest active handoff.
- Confirm active task, blockers, version/git state, and next action against tool reality when cheap.
- Supersede older active handoffs if a new one becomes canonical.
- Keep the new handoff short: objective, completed work, active state, exact next steps, and options.
- Link the handoff from the project index/current state when it becomes the active continuation.
- Do not copy the whole history; route to canonical notes instead.
- Run a closeout/state check if the handoff changes active task or blocker state.

## Workflow Patch Card

- Name the friction, evidence, and rule gap before patching.
- Decide whether this is private-only, installed-skill, public-template, template, or eval work.
- Patch the canonical installed skill first when standing behavior changes.
- Mirror public sanitized changes only when the behavior belongs in the reusable template.
- Update version/changelog/README when public behavior changes.
- Verify installed/public reachability with text search and run public leak/diff checks.
- Close state: work order, task board, current state, project memory, handoff, and public commit if applicable.

## Status Or Closeout Card

- Run the stale dashboard or equivalent state check when drift risk is non-trivial.
- Confirm current-state, task board, active work order, handoff, and blockers agree.
- If version/git changed, confirm README/CHANGELOG/VERSION and latest commit/status.
- If artifacts changed, verify exact paths and label canonical, diagnostic, temporary, or superseded.
- Do not report old blockers or old active tasks as current truth.
- Include state-aware options when meaningful.
- If the next task is obvious and approved, create or start it instead of ending with vague advice.
