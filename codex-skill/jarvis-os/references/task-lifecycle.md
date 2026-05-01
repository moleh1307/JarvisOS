# Task Lifecycle

Use this reference when creating, routing, reviewing, or closing Specialist Mode work orders. The goal is safer task management without a heavy task-management system.

Task Lifecycle v1 gives every meaningful task three things:

- a small lifecycle state;
- a risk lane;
- enough proof to know why `done` is safe.

Do not use this for trivial JARVIS Core work where no durable task exists.

## Lifecycle States

Use these states for the real state of the work:

- `Intake`: captured but not yet shaped enough to work.
- `Ready`: shaped, scoped, unblocked, and ready to start.
- `Active`: currently being worked.
- `Review/Verify`: output exists and needs verification, review, or acceptance evidence.
- `Done`: accepted into project state with verification evidence or a clear reason verification was not possible.
- `Blocked`: cannot move because a specific file, access, credential, dependency, artifact, or fact is missing.
- `Decision Needed`: cannot move because the user or another real owner must choose.
- `Superseded`: replaced by a newer task, decision, or artifact.
- `Emergency`: urgent recovery where speed matters; record evidence and cleanup after the immediate fix.

## Risk Lanes

Pick the lightest lane that honestly fits:

- `standard`: small, known, reversible, low-risk, and pre-authorized by existing workflow.
- `normal`: meaningful work that needs explicit verification before done.
- `high-risk`: public release, private data, credentials, security, destructive actions, protected branches, cost, or strategy changes.
- `emergency`: urgent recovery where delay is riskier than the usual process.

Risk lane controls process weight:

- `standard`: use task cards and normal verification; no extra gate.
- `normal`: require acceptance criteria and verification evidence.
- `high-risk`: require capability surface, escalation boundary, and closeout integrity.
- `emergency`: fix the immediate problem, then write retrospective evidence and cleanup tasks.

## Board Status Mapping

Existing task-board statuses map to lifecycle states:

| Task board status | Lifecycle state |
| --- | --- |
| `todo` | `Intake` or `Ready` |
| `active` | `Active` |
| `review` | `Review/Verify` |
| `internally-accepted` | `Review/Verify` or `Done` depending on closeout |
| `blocked` | `Blocked` |
| `waiting-user-decision` | `Decision Needed` |
| `done` | `Done` |
| `superseded` | `Superseded` |

Do not rebuild the task board only to use lifecycle. Add lifecycle state to the work order; keep the board compact.

## Core Work-Order Fields

For lifecycle-aware work orders, these fields matter most:

- `Owner role`: who owns execution.
- `Status`: board-facing state.
- `Lifecycle state`: real task lifecycle state.
- `Risk lane`: standard, normal, high-risk, or emergency.
- `Scope`: what is inside the task.
- `Acceptance criteria`: what must be true for completion.
- `Verification evidence`: what proved it.
- `Canonical artifact`: output path, commit, PR, report, release, or `none`.
- `Blocker / decision needed`: exact missing item or choice.
- `Closeout state`: done, blocked, superseded, or paused with reason.

## Done Rule

A task is not safely `Done` until:

1. The work is completed or explicitly superseded.
2. Acceptance criteria are met or revised with reason.
3. Verification evidence is recorded.
4. Canonical artifacts are linked or marked `none`.
5. Blockers and decision-needed fields are empty or historical.
6. Current state, task board, and work order agree.

If verification could not run, record why and keep the confidence lane honest.

If a resume, compaction, interruption, or fresh-chat handoff reveals that a task crossed the implementation boundary but did not finish closeout, treat the task as not yet fully done for routing purposes. Finish the missing closeout surfaces first or open a recovery task before starting unrelated work.

## Blocked And Decision Needed

Use `Blocked` only for missing facts, files, credentials, access, dependencies, artifacts, or tool capability.

Use `Decision Needed` only for a real owner choice: strategy, cost, credentials, destructive action, public release, protected branch, private-data boundary, or unavoidable taste/judgment.

Do not use either state as a vague pause.

## Emergency Lane

Emergency tasks may skip normal sequencing only to reduce immediate harm. After the fix:

- record what happened;
- run the skipped verification if still meaningful;
- create cleanup work orders for residue;
- update state so emergency context does not linger as normal truth.

## Anti-Patterns

- One task with many unrelated outcomes.
- `done` without proof.
- `blocked` without a concrete missing item.
- `waiting-user-decision` for something the team can decide internally.
- Multiple canonical task homes for the same fact.
- Keeping old active tasks in current state after a newer handoff supersedes them.

## Closeout

For meaningful lifecycle-aware tasks, closeout should say:

- lifecycle state;
- risk lane;
- verification evidence;
- canonical artifact;
- blocker or decision status;
- next task or reason to pause.

After context transitions, apply the Closeout Resume Sweep from `continuation.md` before accepting stale `done` claims at face value.
