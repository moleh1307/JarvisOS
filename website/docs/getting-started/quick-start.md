---
title: Quick Start
description: Start using JARVIS OS in a Codex workspace.
---

# Quick Start

Clone the template:

```bash
git clone https://github.com/moleh1307/JarvisOS.git
cd JarvisOS
```

Install the Codex skill:

```bash
mkdir -p ~/.codex/skills
cp -R codex-skill/jarvis-os ~/.codex/skills/jarvis-os
```

Then start a new Codex chat:

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

## First Good Use

Use JARVIS OS on a real project where continuity matters:

- a codebase you revisit often;
- a research project with sources and outputs;
- a writing project with decisions and drafts;
- a product or website build;
- a long troubleshooting thread.

For a tiny self-contained request, JARVIS OS should stay in Light Mode and avoid extra files.

## Minimal Project Memory

Create or update a project note under `memory/projects/` when a project needs durable continuity.

Good project memory answers:

- what the project is;
- where it lives;
- what matters right now;
- what is blocked;
- what should happen next;
- which artifacts are canonical.

Do not write a transcript. Preserve the next useful action.

## Normal Prompt

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

## Fresh-Chat Prompt

```text
Jarvis, use JARVIS OS.

This chat is getting long. Create a fresh-chat handoff for this project.
Include current objective, completed work, blockers, exact next steps,
and files the next chat should read first.
```

## Serious Project Prompt

```text
Jarvis, use JARVIS OS Specialist Mode.

Specialist Mode target:
/path/to/project

Start a serious project for:
...

Ask the material questions, choose the right team, and create the first work orders.
```
