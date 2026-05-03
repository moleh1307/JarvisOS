---
title: Skill Composition
description: How agents combine JARVIS OS with domain and plugin skills.
---

# Skill Composition

JARVIS OS can work alongside other skills. The useful pattern is not to merge every workflow. The useful pattern is to choose one lead skill, then let the other skills support only where they are strongest.

## Basic Rule

Use the requested outcome to choose the lead skill:

| Outcome | Lead skill | JARVIS OS role |
| --- | --- | --- |
| continuity, memory, project governance, R&D, handoff, adoption | `jarvis-os` | lead |
| paper review or LaTeX reviewer report | academic review skill | context, artifact paths, memory |
| retro-futurist UI or anti-slop design critique | visual/UI skill | work order, state, verification evidence |
| generated bitmap assets | image generation skill | canonical asset path and provenance |
| reusable discovery from another chat | skill-ticket skill | R&D intake and implementation later |
| GitHub, email, calendar, browser, docs, sheets, slides | plugin skill | continuity, approval boundaries, closeout |

## Composition Contract

- Pick one lead skill for the main deliverable.
- Use supporting skills only for the part they uniquely improve.
- Let domain skills own domain method, format, quality bar, and domain verification.
- Let JARVIS OS own continuity, memory, Specialist Mode, work orders, handoffs, and closeout.
- Stop loading references once the lead/support boundary is clear enough to act.

## Examples

### Paper Review

For a manuscript review, the academic review skill leads. JARVIS OS should preserve project context and artifact status, but it should not replace the academic rubric or LaTeX review format.

### Visual UI Work

For a retro-futurist landing page, the UI skill leads art direction and anti-slop checks. JARVIS OS owns project state, verification evidence, and public/private boundaries.

### Skill Ticket

For a reusable discovery from another JarvisOS chat, the ticket skill leads in that chat. The JarvisOS R&D workspace implements later after the ticket is accepted.

## Anti-Patterns

Avoid:

- loading every installed skill just because several are available;
- letting JARVIS OS soften a specialized skill's quality bar;
- creating duplicate task boards or memories for a domain-skill task;
- letting a domain skill bypass artifact hygiene or privacy boundaries;
- reporting a skill as used when its instructions were not actually followed.

## Closeout

For meaningful multi-skill work, report:

- lead skill used;
- supporting skill used;
- verified output or artifact;
- memory update, or why memory was skipped;
- any unresolved skill conflict.

For small tasks, simply deliver the result.
