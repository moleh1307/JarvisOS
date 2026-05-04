---
title: Specialist Mode
description: Role-based JARVIS OS workflow for serious projects.
---

# Specialist Mode

Specialist Mode is the serious-project layer of JARVIS OS.

It is the successor name for the older Company Mode. Company Mode remains a compatibility alias.

## Target Gate

Specialist Mode must govern a specific target: a project, repo, folder, research problem, product, or workflow.

If the user only says something like `go for Specialist Mode` without naming a target in the message, the agent should ask:

```text
Specialist Mode for which project or folder?
```

Do not default to JARVIS R&D just because the current workspace is a JARVIS vault, because `company/` exists, or because the user also says `JARVIS OS`. Existing Specialist Mode files are evidence of a possible target, not consent to bind to that target. Route to JARVIS R&D only when the user explicitly asks for JARVIS OS/R&D improvement, `new idea`, public template work, workflow bug fixing, or a specific JRD/work-order continuation.

When the target is clear, state it once before acting:

```text
Specialist Mode target: /path/to/project
```

## What It Adds

Specialist Mode can add:

- Founder / project-shape inference;
- Chief of Staff routing;
- functional specialist roles;
- `company/current-state.md`;
- `company/task-board.md`;
- work orders;
- role memories;
- capability surface declaration;
- review gates;
- operating mode;
- task lifecycle;
- internal critique;
- closeout integrity checks.

## The Team Model

In Specialist Mode, "team" usually means one Codex agent changing hats across file-backed roles.

It does not automatically mean multiple runtime agents.

Runtime subagents are optional helpers for explicit or clearly valuable parallel work, but they are not durable team members.

## Functional Role Headers

User-facing Specialist Mode replies should start with a functional role header:

```text
[Role: Chief of Staff]
```

Examples:

- `[Role: Founder]`;
- `[Role: Documentation Engineer]`;
- `[Role: QA Engineer]`;
- `[Role: Product Designer]`;
- `[Role: Memory & Retrieval Engineer]`.

Avoid named persona headers in active routing.

## Operating Modes

`company/current-state.md` should declare what the project is doing now:

- discovery;
- build;
- audit;
- polish;
- release;
- dogfood;
- research attack;
- recovery;
- maintenance.

Operating mode helps the Chief of Staff choose the right next action.

## Minimal Specialist Layer

For small-but-real projects, use only what is needed:

- `company/current-state.md`;
- `company/task-board.md`;
- one charter or adoption audit;
- `company/work-orders/`.

Add richer artifacts only when complexity earns them.

## Full Specialist Layer

Use the full layer for complex projects:

- team roster;
- role memories;
- integration log;
- strategy map;
- evidence ledger;
- adversarial review;
- claim review;
- design QA;
- release readiness.

The goal is not bureaucracy. The goal is fewer missed obligations.

## Mode Exit Ramp

After meaningful closeout, check whether Specialist Mode is still needed.

Downshift the next turn to Light Mode when:

- the active work order is done;
- blockers are clear;
- current state and memory are updated;
- no release, deployment, credential, destructive, or public/private boundary remains open;
- the next likely request is a small question, narrow edit, status check, or ordinary artifact task.

Do not downshift when active work remains, review is still needed, state is inconsistent, or the user asks the team to keep running.
