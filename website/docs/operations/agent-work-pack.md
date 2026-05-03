---
sidebar_position: 4
---

# Agent Work Pack

An Agent Work Pack is a temporary task-local mission packet for meaningful JarvisOS work.

It gives the current agent one compact brief:

- what the task is;
- which mode and role apply;
- what to read first;
- what not to read unless needed;
- which tools and permissions matter;
- what output is expected;
- what verification proves done;
- where durable memory should be updated.

It is designed to reduce agent cognitive load. It is not a second task board, not a new permanent state file, and not required for tiny Light Mode work.

## When To Use It

Use a Work Pack when:

- starting a serious Specialist Mode task;
- resuming after a fresh chat, compaction, or interruption;
- onboarding a new agent to a complex project;
- context is scattered across current state, task board, work order, references, skills, and tools;
- a task has meaningful verification or privacy boundaries.

Skip it for:

- one-command answers;
- tiny edits;
- simple Light Mode questions;
- tasks where the work order already contains everything needed.

## Lifecycle

Default lifecycle: temporary.

At closeout, the Work Pack should expire. Promote only durable facts into:

- a work order;
- current state;
- handoff;
- project memory;
- decision log;
- artifact note.

## Compact Template

```markdown
# Agent Work Pack

- Status: temporary
- Created:
- Expires:

## Mission

- Task:
- User intent:
- Success definition:
- Non-goals:

## Mode And Role

- Operating mode:
- Role:
- Risk lane:
- Lifecycle state:
- Work order:

## Read Set

- Read first:
- Read only if needed:
- Do not read:

## Constraints

- Scope boundaries:
- Privacy boundary:
- Do-not-touch:
- User preferences:
- Stop/ask triggers:

## Capability Surface

- Available tools:
- Required tools:
- Missing or risky tools:
- Allowed autonomous actions:
- Approval needed:

## Execution

- Steps:
- Expected outputs:
- Canonical artifact:
- Temporary artifacts:

## Verification

- Required checks:
- Evidence to record:
- Known verification gaps:

## Memory And Closeout

- Update targets:
- Done criteria:
- Closeout options:
```

## Good Work Pack

A good Work Pack fits on one screen when possible, names exact files, prevents over-reading, states stop/ask triggers, and makes done criteria observable.

## Bad Work Pack

A bad Work Pack duplicates the whole work order, lists every JarvisOS rule, becomes another current-state file, or is created for every tiny task.

