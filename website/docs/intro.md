---
title: Introduction
description: What JARVIS OS is and when to use it.
slug: /intro
---

# JARVIS OS

JARVIS OS is a local-first operating system for Codex continuity. It turns a normal repository or workspace into a durable memory layer for agent work.

The core idea is simple:

```text
chat = temporary working surface
markdown = durable continuity layer
```

Instead of asking an agent to remember a long conversation forever, JARVIS OS teaches the agent to retrieve the right files, do the work, verify outputs, and leave the smallest useful trace for the next session.

## What JARVIS OS Solves

Long agent projects usually fail in predictable ways:

- the chat becomes too long to reason through cleanly;
- context compaction loses subtle project state;
- a fresh chat starts from zero;
- decisions hide in old transcripts;
- generated artifacts become hard to trust;
- task status drifts across notes;
- agents forget why a workflow rule exists.

JARVIS OS moves those facts into markdown files that both humans and agents can inspect.

## The Two Layers

JARVIS OS has two operating layers.

| Layer | Use it for | What it adds |
| --- | --- | --- |
| JARVIS Core / Light Mode | Normal tasks and small project work | targeted retrieval, memory discipline, handoffs, artifact hygiene |
| JARVIS Specialist Mode | Serious, long-running, public, risky, or multi-discipline work | roles, task boards, work orders, review gates, operating modes, closeout checks |

Light Mode is the default. Specialist Mode is optional and should earn its complexity.

## What Makes It Different

JARVIS OS is not a background surveillance memory system. It does not require screenshots, an always-on recorder, a hidden vector database, or transcript dumping.

It is intentionally inspectable:

- markdown is canonical;
- memory writes are explicit;
- decisions have homes;
- artifacts have status and verification;
- self-improvement is governed by candidate, repeated, promoted, rejected, and superseded lanes.

## The Outcome Contract

A JARVIS OS session succeeds when Codex can:

1. recover the relevant durable context;
2. complete the user's actual task;
3. verify meaningful outputs;
4. update only the memory that future work needs;
5. leave the next session in a clearer state.

The goal is not more ceremony. The goal is continuity without confusion.

## Where To Look Next

Use the [Capability Index](reference/capability-index.md) when you want a compact map of what JARVIS OS can do and which doc explains each capability.
