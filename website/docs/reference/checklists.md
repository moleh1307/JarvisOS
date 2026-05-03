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

- Read `company/current-state.md`.
- Check `company/task-board.md`.
- Identify operating mode.
- If continuation is likely but a full handoff is too much, maintain a one-screen handoff seed.
- Pick the next unblocked task.
- Load only the references needed.
- Execute and verify.
- Update state and closeout.

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
- Confirm deployment or publish boundary.
- Push only when safe and authorized.

## Verification Breadcrumb

- Name the exact command, tool, script, source, artifact path, or rendered output used.
- Include the meaningful result instead of a giant log dump.
- For public/version/git claims, include commit, branch, version file, build/test command, or dashboard.
- For generated artifacts, include the canonical path and concrete check performed.
- If verification was not possible, state what was not checked and why.
- Skip breadcrumbs for tiny answers where verification is irrelevant.

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
