# Memory Router And Lifecycle Lanes

Use this reference when a task changes durable memory, when a project note is becoming hard to scan, or when old memory may conflict with current state.

The goal is simple: make memory easier to retrieve later. Do not turn memory into ceremony.

## Core Rule

Before writing memory, route the fact to the smallest correct home and assign its lifecycle lane when freshness matters.

Memory should answer:

- what changed;
- where the canonical truth lives;
- whether it is active, stable, candidate, archived, or superseded;
- what the next agent should read or do first.

## Memory Write Router

Choose one primary home:

| Memory type | Canonical home | Use for |
| --- | --- | --- |
| Project state | `memory/projects/<project>.md` or `memory/projects/<project>/index.md` | current objective, status, blockers, next action, project constraints |
| Personal preference | `memory/personal/preferences.md` | durable user working preferences, communication preferences, standing constraints |
| Decision | `logs/decisions.md` or project-local `decisions.md` | durable choices with rationale and consequence |
| Session trace | `sessions/...` | meaningful work episode: goal, context, completed work, exact resume point |
| Handoff | `handoffs/...` | unfinished, blocked, long, compacted, or fresh-chat continuation |
| Artifact record | project memory or `outputs.md` | generated files, status, verification, caveats, canonical path |
| Lesson candidate | `system/learning-log.md` | reusable friction, near-miss, better workflow, possible future rule |
| Failure pattern | `system/failure-patterns.md` | stable repeated failure mode, not a one-off |
| Work order state | `company/work-orders/...`, `company/current-state.md`, `company/task-board.md` | Specialist Mode task execution state |

If one fact seems to belong in several places, write it once in the canonical home and link to it elsewhere only when useful.

## Lifecycle Lanes

Use lifecycle lanes when a memory item may age, compete with newer facts, or guide future behavior:

- `active`: needed for current continuation.
- `stable`: durable context or rule that should remain true until explicitly changed.
- `candidate`: possible lesson, pattern, or decision not yet promoted.
- `archived`: historical record; useful for provenance but not current guidance.
- `superseded`: replaced by newer state, decision, artifact, or rule.

Do not label every bullet. Use lanes for sections, important entries, or facts that could otherwise be mistaken for current truth.

## Freshness Check

Before trusting or extending a memory note, ask:

- Is this current state or history?
- Is there a newer work order, session note, decision, commit, or artifact?
- Is the item marked `superseded`, `archived`, or `candidate`?
- Does repo/tool reality contradict the note?
- Is there a fresher `Current State Capsule`, handoff, or task board entry?

If memory conflicts with tool reality, tool reality wins for current facts. Update memory after verifying.

## Current-State Capsule

Important project memory should start with a short capsule:

```text
Current State Capsule
- Objective:
- Latest status:
- Current canonical artifact/output:
- Current active script/workflow:
- Last completed step:
- Known caveats:
- Next action:
- Blockers:
- Canonical workspace/repo:
- Last useful session/handoff:
```

Keep the capsule current and short. Move history elsewhere.

## Project Note Split Trigger

Split a project memory note when it becomes:

- a long chronological ledger;
- several hundred lines and hard to scan;
- full of completed work that competes with current state;
- a mix of outputs, decisions, methods, and status that slows retrieval;
- repeatedly read only to find one small current-state fact.

Recommended split:

```text
memory/projects/<project>/index.md
memory/projects/<project>/history.md
memory/projects/<project>/decisions.md
memory/projects/<project>/outputs.md
memory/projects/<project>/methods.md
```

Use only the files the project needs. Do not split preemptively.

After splitting, leave a clear pointer from the old flat note to the new `index.md`, or preserve the old path as a short index.

## Session Note Compression

Session notes should preserve continuation, not recreate the chat.

Include:

- goal;
- context used;
- work completed;
- decisions;
- blockers;
- exact next steps;
- references to changed files, commits, outputs, or work orders.

Avoid:

- play-by-play tool logs;
- full transcript summaries;
- duplicate project-state facts already captured in project memory;
- speculative reasoning that did not become a decision or next action.

## Memory Debt Review

Run a compact Memory Debt Review when:

- a project becomes important or long-running;
- a project note is hard to scan;
- agents repeatedly over-read or miss the current state;
- stale/superseded facts caused confusion;
- a fresh-chat handoff took too much reconstruction.

Use:

```text
Memory Debt Review:
- Bloated notes:
- Stale or superseded facts:
- Duplicated truths:
- Missing current-state capsule:
- Notes needing split:
- Orphaned handoffs:
- Recommended cleanup:
```

Cleanup is normal when safe and scoped. Ask only before deleting or rewriting real user data, private records, or ambiguous canonical artifacts.

## Stop-The-Line Triggers

Run Stop-the-Line Review when:

- memory says one thing and repo/tool reality says another;
- a completion report would rely on stale memory;
- the agent is about to append more chronology to an already bloated project note;
- a note split is needed before continuation can stay reliable;
- a claimed rule or preference is only a candidate but is being treated as stable.

## Closeout

Before finishing meaningful memory-affecting work, verify:

- only the smallest useful memory changed;
- the current-state capsule remains accurate;
- new decisions are in the decision log or project decisions file;
- handoffs are active only when work is actually unfinished or blocked;
- superseded/archived/candidate items are not presented as current truth.
