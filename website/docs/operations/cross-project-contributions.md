---
title: Cross-Project Contributions
description: Let other JarvisOS chats package reusable project discoveries for JarvisOS R&D.
---

# Cross-Project Contributions

JarvisOS can improve from real projects, not only from a dedicated R&D chat.

When another JarvisOS-powered chat discovers a reusable workflow, prompt, quality check, template, or skill idea, package it as a skill ticket. Do not directly mutate JarvisOS core from that project unless the user explicitly asks for that implementation in the JarvisOS R&D workspace.

## Primary Command

```text
JarvisOS Skill Ticket
```

Use it in another JarvisOS chat. That chat should create a ticket number, save the ticket if the central vault is available, and give you the handoff command for JarvisOS R&D.

## Expanded Ticket Prompt

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
- detailed skill draft;
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

## Skillset Extraction Prompt

```text
Jarvis, use JARVIS OS.

Review this chat's available history, project memory, decisions, artifacts, repeated workflows, prompts, tools, and failure modes.
Use the Cross-Project Contribution Bridge to propose a JarvisOS skill or skillset based on what became reusable here.

For each proposed skill, include:
- name;
- trigger conditions;
- reusable workflow;
- required inputs/tools;
- output artifacts;
- verification checks;
- privacy boundary;
- examples;
- recommendation: create-skill, merge-into-existing-skill, keep-as-project-memory, make-template, or reject.

Do not install or publish anything yet. Package the result as a JarvisOS Skill Ticket for R&D.
```

## Skill Detail Rule

JarvisOS skill drafts should follow the Skill Quality Standard. A future agent should understand triggers, non-triggers, ownership boundaries, delegation boundaries, hard no-fake rules, context, steps, repair paths, outputs, verification, privacy boundaries, examples, and failure modes without reconstructing the original chat.

For proposed skills, include:

- ownership boundary;
- delegation boundary;
- hard boundaries;
- default workflow;
- visible progress, if long-running;
- repair or fallback workflow;
- outputs and artifact provenance;
- observable acceptance criteria.

## Triage Outcomes

| Outcome | Meaning |
| --- | --- |
| `reject` | Not reusable, unsafe, or too project-specific |
| `project-local` | Useful, but should stay in the source project |
| `document-only` | Add docs or prompt guidance, no behavior patch |
| `template-update` | Update a reusable template |
| `skill-patch` | Update installed JarvisOS behavior |
| `new-skill-candidate` | Draft a separate skill with the skill creator workflow |
| `eval-seed` | Preserve as a future regression scenario |
| `public-release` | Sanitize and mirror into the public template |

## Privacy Guard

Contribution candidates must separate reusable behavior from private project facts. Public JarvisOS artifacts should not include private file paths, datasets, clients, credentials, unpublished plans, or project-specific details.
