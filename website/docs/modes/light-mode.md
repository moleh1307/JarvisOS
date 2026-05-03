---
title: Light Mode
description: The lightweight default mode for normal JARVIS OS work.
---

# Light Mode

Light Mode is the default JARVIS OS behavior.

Use it for ordinary tasks where full Specialist Mode would add more friction than value.

## What Light Mode Does

Light Mode keeps the agent disciplined without creating a project company layer.

The agent should:

- retrieve only directly relevant context;
- skip retrieval for trivial self-contained work;
- execute the task;
- verify meaningful outputs;
- update the smallest useful memory only when future continuation benefits.

## What Light Mode Avoids

Light Mode should not create:

- `company/` layer;
- role roster;
- work orders;
- session notes;
- handoffs;
- options menu;
- learning entries.

Those artifacts are useful only when the task earns them.

## Example

```text
Jarvis, use JARVIS OS.

Check the project memory, then fix the typo in the README.
```

The agent should read only the relevant project memory and README, make the edit, verify it, and avoid heavy ceremony.

## Escalating To Specialist Mode

Escalate when:

- the project has multiple disciplines;
- task state needs durable ownership;
- quality gates matter;
- the work is public-facing;
- release or deployment risk exists;
- repeated continuation would otherwise drift.

## Returning From Specialist Mode

After Specialist Mode work closes, return to Light Mode when:

- the work order is done;
- blockers are clear;
- state and memory are updated;
- the next likely request is a small question, narrow edit, status check, or ordinary artifact task.

Do not stay in Specialist Mode by inertia. Use the heavier layer only while it is earning its weight.
