---
title: Checklists
description: Compact execution checklists for common JARVIS OS work.
---

# Checklists

## Light Mode Task

- Identify the project or domain.
- If the request is short or vague, ask one sharp follow-up before editing when interpretation matters.
- If the user answers a follow-up tersely, bind the answer to the pending question before asking again.
- Read only directly relevant memory.
- Badge mutable context internally as fresh, verified, stale-risk, or working-assumption.
- Make the change or answer the question.
- Verify meaningful output.
- Leave a compact verification breadcrumb when verification matters.
- Expire temporary scratch: promote, archive diagnostic, or discard.
- Update memory only if future continuation benefits.

## Clarifying Follow-Up

- Run a quick Referent Snapshot for words like `this`, `that`, `it`, `there`, `here`, `the file`, `the page`, or `the project`.
- Identify the most likely target from current browser/app context, selected path, recent message, active project state, or latest artifact.
- Identify the unclear reference, target, or desired outcome.
- Ask one to three direct questions only when there is no clear target, multiple plausible targets, or consequential ambiguity.
- Name the candidate targets when asking.
- Offer a likely default when it helps the user answer quickly.
- Keep a Clarification Receipt after asking: remember the exact question, options, and default.
- Interpret terse replies like `yes`, `go`, `second`, `that one`, `do it`, or `no` against the pending question first.
- State the resolved instruction once before acting when the answer could otherwise be misread.
- Ask again only when the reply does not choose an option, contradicts the original request, or expands into consequential/destructive work.
- Proceed with a stated assumption only when the missing detail is low-risk.
- Stop and ask before code edits, deletion, public changes, memory writes, project-direction changes, cost, credentials, or irreversible work.

## Specialist Mode Continuation

- Resolve the Specialist Mode target first: project, repo, folder, research problem, product, or workflow.
- If the user only says `go for Specialist Mode` or similar and the target is unclear, ask which project/folder instead of defaulting to JARVIS R&D.
- Route to JARVIS R&D only when the user explicitly asks for JarvisOS/R&D improvement, `new idea`, public template work, workflow bug fixing, or the live R&D state is clearly active.
- Read `company/current-state.md`.
- Check `company/task-board.md`.
- Identify operating mode.
- If continuation is likely but a full handoff is too much, maintain a one-screen handoff seed.
- Run Feature Adoption Check for JARVIS R&D, workflow feedback, public template work, or named JarvisOS features.
- Pick the next unblocked task.
- Load only the references needed.
- Execute and verify.
- After implementing an R&D idea or workflow feature, include a short usage example in the closeout.
- Use Closeout Stack Order when several closeout pieces apply.
- Update state and closeout.

## Feature Adoption Check

- Use it for meaningful JARVIS R&D, Specialist Mode workflow changes, public template changes, or when Melih names an existing JarvisOS feature.
- Identify named features from the prompt or recent feedback, such as Jarvis Doctor, Usage Example Closeout, Dogfood Return Check, or Closeout Stack Order.
- Identify naturally triggered features from the task type: R&D Loop, public validation, memory routing, capability surface, closeout, skill quality, or release readiness.
- Identify the last meaningful feature in the active workflow area when dogfooding is relevant.
- For each applicable feature, use it or mark `skipped` with a short reason.
- Do not silently ignore named features, public validation tools, or closeout rules that clearly apply.
- In the user-facing report, mention only the features that materially shaped the work or were deliberately skipped.
- For public template/repo changes, run Jarvis Doctor unless unavailable or genuinely irrelevant.
- Keep it lightweight; this is an adoption guard, not a new long form.

## Skill Dictionary Routing

- Use it when a specialized task may match a standalone/domain skill but the user did not name the skill.
- Scan the dictionary before reading full skill files.
- Choose one lead skill for the main deliverable.
- Add supporting skills only when they uniquely improve a subtask.
- Read only the selected skill files and triggered references.
- Update the dictionary when a skill is created, installed, removed, renamed, or materially rerouted.
- Run the skill dictionary check when skill coverage changed.

## Project Skill Incubator

- At the start of meaningful Specialist Mode work, scan `company/project-skills/index.md` when it exists.
- Use a local project skill only when its trigger matches and it adds local context, constraints, or verification.
- Do not claim a project skill was used unless the index and triggered skill file were actually read.
- Use it when repeated Specialist Mode project-local workflow may deserve a local skill.
- Try a project note, checklist, or playbook before creating a project skill.
- Create a project skill only when triggers, non-triggers, workflow, outputs, verification, and sunset trigger are clear.
- Store local skills under `company/project-skills/`.
- Maintain `company/project-skills/index.md` when skills exist or future agents may miss them.
- Run the project-skill checker when creating, changing, promoting, retiring, or relying on project skills.
- Keep project skills local unless dogfood or cross-project evidence justifies a JarvisOS Skill Ticket.

## Feature Saturation Check

- Use it when several consecutive R&D additions land in the same workflow area.
- Name the active cluster: closeout, ambiguity, memory, verification, public docs, creative craft, R&D governance, or another specific area.
- Decide the next move before adding another adjacent feature: continue, consolidate, simplify/remove, switch domain, or ask the user if direction changes materially.
- Continue only when the new idea solves a distinct failure mode, compresses existing behavior, or clearly earns its place.
- Prefer consolidation or simplification when the idea mainly adds another label, gate, checklist, or section around the same task moment.
- Keep it lightweight; do not turn every R&D cycle into a formal saturation review.

## Public Artifact

- Identify audience and decision.
- Inspect named references.
- Check privacy/public-data boundaries.
- Build or edit.
- Verify local output.
- Record the exact artifact path and check used.
- Distinguish local, pushed, and deployed state.

## Memory Write

- Choose the canonical home.
- If memory conflicts with live tool state, trust the live source for execution and update the canonical memory during closeout.
- Mark mutable facts as stale-risk or working-assumption until verified.
- Write the smallest durable note.
- Add source labels only when useful.
- Link related notes when it improves retrieval.
- Avoid duplicate truths.

## Context Freshness

- Use `fresh` when the fact was just read from the canonical file or current tool output.
- Use `verified` when it was checked against a repo, artifact, build, dashboard, or source of truth.
- Use `stale-risk` when the fact changes often, the note is old, the repo/tool state is dirty, or sources disagree.
- Use `working-assumption` when the fact is plausible but not directly verified.
- Verify before consequential claims, public/version claims, blockers, deployments, credentials, costs, deletion, or irreversible work.
- Do not print freshness labels mechanically; mention them only when they explain risk or verification.

## Release

- Check git status.
- Check version and changelog.
- Run relevant tests/builds.
- Run leak or public/private boundary scans.
- Record the exact verification commands, version, branch, commit, and dashboard/source used.
- Record a rollback handle for public/template/workflow changes.
- Confirm deployment or publish boundary.
- Push only when safe and authorized.

## Verification Breadcrumb

- Name the exact command, tool, script, source, artifact path, or rendered output used.
- Include the meaningful result instead of a giant log dump.
- For public/version/git claims, include commit, branch, version file, build/test command, or dashboard.
- For generated artifacts, include the canonical path and concrete check performed.
- If verification was not possible, state what was not checked and why.
- Skip breadcrumbs for tiny answers where verification is irrelevant.

## Rollback Handle

- Use it for public template changes, installed skill changes, workflow rules, or consequential JARVIS R&D features.
- Record public commit, version, branch, and touched feature/section.
- Name the safest rollback route: revert commit, remove section, restore previous version, or disable through sunset/merge decision.
- List what must be revalidated after rollback.
- Note if rollback would be risky or needs user approval.
- Keep it short; it is a repair pointer, not a requirement to roll back.

## Scratchpad Expiry

- Identify temporary notes, assumptions, QA files, screenshots, drafts, Work Packs, diagnostics, and one-off analysis.
- Promote only durable facts, decisions, blockers, artifacts, or next steps into canonical memory.
- Archive diagnostic outputs only when they help future verification, repair, audit, or comparison.
- Discard scratch work that has served its purpose.
- Label any remaining temporary artifact as canonical, diagnostic, temporary, superseded, or safe to delete.
- Do not preserve whole working trails when only the reusable result matters.

## One-Screen Handoff Seed

- Use it when a full handoff would be too much but continuation is likely.
- Keep it inside current state, a session note, an existing handoff, or the closeout summary.
- Include current objective, checked live facts, next action, blockers or risks, read-first files, and one fresh-chat starter paragraph.
- Keep it to one screen.
- Do not create a new handoff file only to store a seed.
- Promote it into a full handoff only when work remains open, a blocker exists, the thread is costly, or another session/agent is likely to continue.

## Usage Example Closeout

- Use it after implementing a JARVIS R&D idea or workflow feature.
- Show a realistic trigger phrase, task moment, or agent behavior.
- Show what the agent would do differently because of the new feature.
- Keep it to one short paragraph or two bullets.
- Skip only for purely internal cleanup with no user-observable behavior.

## Closeout Stack Order

- Use it when several closeout pieces apply.
- Order the final report as outcome/version, usage example, verification breadcrumbs, rollback handle, then state-aware options.
- Include only sections that apply.
- Keep verification to meaningful checks/results.
- Include rollback only for public/template/workflow changes or consequential releases.
- Do not repeat the same fact across sections.
