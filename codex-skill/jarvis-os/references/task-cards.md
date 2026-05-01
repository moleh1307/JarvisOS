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
- If a durable work order exists, confirm lifecycle state and risk lane before changing files.
- Read the smallest relevant code path plus existing tests or local patterns.
- Preserve unrelated user changes; do not revert dirty work you did not create.
- Make the narrowest fix that matches the repo style.
- Run the most relevant test, typecheck, lint, build, or smoke command available.
- Report what changed, what passed, and any verification you could not run.

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
- Give new work orders a lifecycle state, risk lane, acceptance criteria, and verification expectation.
- Record baseline commands, tests, artifacts, and known risks.
- Choose Light Mode, Minimal Specialist Layer, or Full Specialist Layer from actual complexity.

## Fresh Continuation Card

- Read the active project index/current-state first, then the latest active handoff.
- Confirm active task, blockers, version/git state, and next action against tool reality when cheap.
- If the last task appears implemented but not fully closed, run the Closeout Resume Sweep before new work.
- Supersede older active handoffs if a new one becomes canonical.
- Keep the new handoff short: objective, completed work, active state, exact next steps, and options.
- Link the handoff from the project index/current state when it becomes the active continuation.
- Do not copy the whole history; route to canonical notes instead.
- Run a closeout/state check if the handoff changes active task or blocker state.

## Workflow Patch Card

- Name the friction, evidence, and rule gap before patching.
- Set lifecycle state and risk lane for the workflow patch work order.
- Decide whether this is private-only, installed-skill, public-template, template, or eval work.
- Patch the canonical installed skill first when standing behavior changes.
- Mirror public sanitized changes only when the behavior belongs in the reusable template.
- Update version/changelog/README when public behavior changes.
- Verify installed/public reachability with text search and run public leak/diff checks.
- Close state with verification evidence, canonical artifact, work order, task board, current state, project memory, handoff, and public commit if applicable.

## R&D Idea Loop Card

- Start with exactly one proposed idea unless the user explicitly asked for a broad brainstorm.
- Check the Friction Inbox, Reflex candidates, and recent Learning Pulses first; if evidence is thin or stale, apply Learning Pulse Cadence before pure ideation.
- If active eval seeds exist and no stronger evidence candidate is obvious, run one Regression Rehearsal seed and record pass/fail/skip.
- Record why the idea is non-obvious, useful, feasible, and safe enough to discuss.
- Run compact team discussion through the smallest relevant roles.
- Decide accepted, rejected, or revise; record the reason in an idea card when durable.
- Run the Subtraction Gate: what does this simplify, remove, replace, or make less necessary?
- Run Stack Compression Check after several workflow features in a row or when the idea mostly adds a new named mechanism.
- Convert accepted ideas into one work order or a short one-to-five task list.
- Define verification and dogfood evidence before implementation.
- After implementation, refresh the project or skill, record where the new behavior was used, explain the idea compactly, then return to ideation.

## Friction Inbox Card

- Capture only workflow friction that may matter again.
- Keep the item tiny: what happened, where observed, frequency, impact, and candidate response.
- Mark privacy: private, public-safe, or needs sanitization.
- Do not promote inbox items directly into rules.
- Triage as ignore, watch, idea-loop, work-order, update-template, add-eval, or public-release.
- Prefer one good inbox item over a long list of weak observations.

## Self-Improvement Reflex Card

- Run only after meaningful work or clear reusable behavior signals.
- Identify the trigger: correction, repeated mistake, state drift, useful shortcut, note bloat, rule helped, or rule noise.
- Capture the smallest candidate in the right home: Reflex candidate, Friction Inbox, project memory, preferences, learning log, or JARVIS R&D.
- Mark lane: observed, candidate, repeated, promoted, rejected, archived, or superseded.
- Do not silently promote candidates into standing rules.
- If the signal is strong, route to the R&D Idea Loop, work order, template update, eval, or memory cleanup.
- When a signal is promoted into consequential standing behavior, create or link one tiny eval seed unless acceptance criteria already cover it.
- Compress or archive candidates that do not recur.

## Regression Rehearsal Card

- Use only when active eval seeds exist and the loop is about to ideate without a stronger evidence candidate.
- Select one relevant seed, not the whole seed folder.
- Run the seed manually: compare the current behavior against the pass/fail signals.
- Record result as pass, fail, skip, or needs update.
- If it fails, route the result into the R&D Idea Loop or a corrective work order.
- If it passes, continue ideation without turning the rehearsal into a status report.
- Do not imply background or automated eval execution.

## Learning Pulse Card

- Use only when recent learning should be visible or when choosing between evidence-backed candidates and pure ideation.
- Run before pure R&D ideation when three idea loops completed since the last pulse, or when no fresh unpromoted Friction/Reflex signal exists.
- Read the smallest recent set: Reflex candidates, Friction Inbox items, recent idea cards/work orders, and current state.
- Separate captured, promoted, rejected/archived, watch-next, and net effect.
- Do not invent learning or promote rules from the pulse alone.
- Keep the report compact and private by default.

## Status Or Closeout Card

- Run the stale dashboard or equivalent state check when drift risk is non-trivial.
- Confirm current-state, task board, active work order lifecycle state, handoff, and blockers agree.
- After compaction/resume, check whether the previous task needs closeout repair before reporting or starting new work.
- If version/git changed, confirm README/CHANGELOG/VERSION and latest commit/status.
- If artifacts changed, verify exact paths and label canonical, diagnostic, temporary, or superseded.
- Do not report old blockers or old active tasks as current truth.
- Do not mark lifecycle-aware tasks Done without verification evidence or a recorded reason.
- Include state-aware options when meaningful.
