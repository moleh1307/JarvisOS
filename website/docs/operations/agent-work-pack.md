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
- what the finished output should look and feel like;
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

## Done Shape

- Audience/user:
- Final form:
- Must be visible:
- Must not become:
- Quality feel:

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

For meaningful deliverables, it also names the Done Shape before implementation: who the result is for, what form the final artifact takes, what must be visible, what it must not become, and what quality feel the team is aiming for.

## Bad Work Pack

A bad Work Pack duplicates the whole work order, lists every JarvisOS rule, becomes another current-state file, or is created for every tiny task.

Bad Done Shape is vague decoration like "make it professional." Useful Done Shape is concrete enough to guide implementation and review.
