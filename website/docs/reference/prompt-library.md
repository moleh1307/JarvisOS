---
title: Prompt Library
description: Common prompts for using JARVIS OS.
---

# Prompt Library

## Command Deck

Use these as short intent shortcuts. They are not rigid syntax; agents should still route by context.

| Command | Use it for |
| --- | --- |
| `status` | Compact current state. |
| `continue` / `go` / `next` | Next unblocked task. |
| `new idea` | One R&D Idea Loop cycle. |
| `create a Work Pack` | Task-local execution context before meaningful work. |
| `JarvisOS Skill Ticket` | Package a reusable discovery for JarvisOS R&D. |
| `fresh-chat handoff` | Continuation note for a new chat. |
| `adopt this project` | Existing project audit before Specialist Mode structure. |
| `release readiness` | Verification, version, docs, git, and approval checks. |

## Normal Continuity

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

## Fresh-Chat Handoff

```text
Jarvis, use JARVIS OS.

This chat is getting long. Create a fresh-chat handoff for this project.
Include current objective, completed work, blockers, exact next steps,
and files the next chat should read first.
```

## Workflow Refresh

```text
Jarvis, workflow refresh.

Use JARVIS OS Specialist Mode.
Read the latest installed JARVIS OS skill and the live project state.
Continue from the next unblocked task using the latest workflow rules.
```

## JarvisOS Skill Ticket

Short command:

```text
JarvisOS Skill Ticket
```

Expanded command:

```text
Jarvis, use JARVIS OS.

Create a JarvisOS Skill Ticket from this chat.
Review the available chat history, project memory, decisions, artifacts,
repeated workflows, prompts, tools, and failure modes.

Create a detailed skill ticket with:
- ticket ID;
- source evidence;
- reusable pattern;
- proposed skill or skillset;
- detailed skill draft with ownership boundary, delegation boundary,
  hard boundaries, workflow, repair path, outputs, and verification;
- privacy lane;
- what stays project-local;
- anti-bloat review;
- suggested implementation path;
- verification plan;
- R&D handoff prompt.

Save it under company/skill-tickets/ if that vault is available.
Otherwise print the full ticket in chat.
Do not implement it here.
```

## Skillset Extraction

```text
Jarvis, use JARVIS OS.

Review this chat's available history, project memory, decisions, artifacts,
repeated workflows, prompts, tools, and failure modes.
Use the Cross-Project Contribution Bridge to propose a JarvisOS skill or
skillset based on what became reusable here.

For each proposed skill, include:
- name;
- trigger conditions;
- non-triggers;
- ownership boundary;
- delegation boundary;
- hard boundaries;
- reusable workflow;
- repair or fallback workflow;
- required inputs/tools;
- output artifacts and provenance;
- verification checks and acceptance criteria;
- privacy boundary;
- examples;
- recommendation: create-skill, merge-into-existing-skill,
  keep-as-project-memory, make-template, or reject.

Do not install or publish anything yet. Package the result as a JarvisOS
Skill Ticket for R&D.
```

## New App Or Product

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a new project in Specialist Mode.
Project idea:
...

Your first role is Founder.
Ask the material questions, choose the right workspace, decide the team,
and create the first high-leverage work orders.
```

## Existing Repo Adoption

```text
Jarvis, use JARVIS OS Specialist Mode.

Adopt this existing project into Specialist Mode:
/path/to/project

Audit first, then create the company layer around the existing structure.
Do not reorganize or rewrite anything before the audit.
```

## Research Project

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a research team for:
...

Ask the material questions needed to understand the research question,
data, method, risks, and success criteria.
```

## Side Quest

```text
Jarvis, side quest for the current Specialist Mode project:
...

Classify this as clarification, defect, side quest, or scope change.
Preserve the interrupted task and tell me whether the main flow resumes afterward.
```

## Release Readiness

```text
Jarvis, use JARVIS OS Specialist Mode.

Run release readiness for this project.
Check verification, version metadata, README/changelog visibility,
git status, and whether a PR or tag is needed.
Do not publish a release or stop the company without my approval.
```
