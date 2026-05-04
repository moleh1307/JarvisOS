---
title: Runtime Anchor
description: One-screen refresh note for keeping JARVIS OS behavior alive in long chats.
---

# Runtime Anchor

The Runtime Anchor is the small note agents should reload when a long chat risks forgetting JARVIS OS.

It exists because rereading the full skill creates context bloat, but continuing from chat momentum causes feature drift.

## When To Refresh

Reload the anchor when:

- context is long, compacted, resumed, or interrupted;
- the user says `continue`, `status`, `what now`, or `go` in a long-running project;
- the user says the agent forgot JarvisOS;
- Specialist Mode is starting or continuing;
- meaningful file edits are about to happen in a JarvisOS project;
- final closeout is about to claim something is done, ready, verified, or released.

## Anchor Questions

The agent should quickly check:

- Which mode is active: Core / Light Mode or Specialist Mode?
- What is the target project, folder, work order, artifact, or memory note?
- What current state, project memory, handoff, or task board must be read?
- Which JarvisOS feature naturally triggers: Work Pack, Skill Dictionary, project skill, Task Lifecycle, Artifact Hygiene, Quality Gate, handoff, or verifier?
- Is there consequential ambiguity that needs one sharp question?
- Has the exact artifact or state been checked before saying `ready`?
- Did anything change that deserves a small memory update?

## Rule

Never continue a long JarvisOS thread purely from chat momentum.

Refresh the anchor, route to the smallest needed feature, then keep moving.
