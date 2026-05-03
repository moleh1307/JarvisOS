---
title: Skill Quality Standard
description: How JarvisOS keeps reusable skills detailed, executable, and safe.
---

# Skill Quality Standard

JarvisOS skills should be detailed enough that a future agent can execute the workflow without reconstructing the original chat.

The standard is not "make every skill long." The standard is operational clarity.

## Use It For

- new JarvisOS skills or skillsets;
- JarvisOS Skill Tickets that propose a reusable workflow;
- reviews of existing skills;
- R&D decisions about whether a project method should become a skill, template, reference, eval seed, or project-local note.

## Serious Skill Checklist

A serious skill should define:

- trigger and non-trigger conditions;
- ownership boundary;
- delegation boundary;
- hard boundaries against fake completion;
- default workflow;
- visible progress when the workflow is long-running;
- repair or fallback workflow;
- outputs and artifact provenance;
- observable verification and acceptance criteria;
- privacy boundary;
- examples and failure modes.

## Acceptance Rule

Do not accept a skill proposal just because it sounds useful.

Accept it only when the reusable pattern is clear, the workflow is executable, the public/private boundary is safe, and the completion checks are observable.

If the pattern is weak, keep it as project memory, a template idea, a docs note, or an eval seed instead of promoting it into JarvisOS behavior.

