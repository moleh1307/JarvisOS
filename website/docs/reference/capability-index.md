---
title: Capability Index
description: A compact map of what JARVIS OS can do and where each capability lives.
---

# Capability Index

This page is a map, not a new workflow. Use it when you want to know what JARVIS OS can do and where to look next.

| Capability | Use it when | Primary trigger | Where to read |
| --- | --- | --- | --- |
| Light Mode | The task is small, local, or self-contained. | `Jarvis, use JARVIS OS` | [Light Mode](../modes/light-mode.md) |
| Specialist Mode | The project needs roles, work orders, durable state, review, or release discipline. | `Jarvis, use JARVIS OS Specialist Mode` | [Specialist Mode](../modes/specialist-mode.md) |
| Mode Exit Ramp | Specialist Mode work is closed and the next task can be lighter. | closeout after serious work | [Light Mode](../modes/light-mode.md), [Specialist Mode](../modes/specialist-mode.md) |
| Command Deck | You want short invocation phrases instead of long prompts. | `status`, `continue`, `new idea` | [Prompt Library](prompt-library.md) |
| Accidental Message Guard | A prior message was wrong, accidental, or cancelled. | `ignore previous`, `cancel that` | [Prompt Library](prompt-library.md) |
| Fresh-Chat Handoff | A chat is getting long or another session needs to continue. | `fresh-chat handoff` | [Fresh Chat](../getting-started/fresh-chat.md), [Handoffs](../concepts/handoffs.md) |
| Artifact Hygiene | Files, docs, images, data, PDFs, or generated outputs need trust labels and verification. | any meaningful artifact | [Artifact Hygiene](../concepts/artifact-hygiene.md) |
| Reference Router | Several workflow references could apply and the agent should not over-read. | complex routing | [Reference Router](../operations/reference-router.md) |
| Agent Work Pack | A meaningful task has scattered context, tools, constraints, and done criteria. | `create a Work Pack` | [Agent Work Pack](../operations/agent-work-pack.md) |
| Done Shape | A deliverable needs a clear target before implementation. | meaningful deliverable Work Pack | [Agent Work Pack](../operations/agent-work-pack.md) |
| Skill Composition | Multiple skills apply and the lead/support boundary is unclear. | named or overlapping skills | [Skill Composition](../operations/skill-composition.md) |
| Task Lifecycle | A Specialist Mode work order needs state, risk, evidence, blockers, or closeout. | work order change | [Task Lifecycle](../operations/task-lifecycle.md) |
| Quality Gates | Output needs critique, verification, or closeout integrity. | QA/review/readiness | [Quality Gates](../operations/quality-gates.md) |
| Public Artifact Framing | A README, public page, bio, landing page, email, or simple site will be judged externally. | public-facing artifact | [Public Artifacts](../operations/public-artifacts.md) |
| R&D Idea Loop | A team is improving a product, workflow, or JarvisOS itself idea by idea. | `new idea` | [R&D Loop](../modes/rd-loop.md) |
| Cross-Project Contribution | Another JarvisOS chat finds a reusable workflow or skill candidate. | `JarvisOS Skill Ticket` | [Cross-Project Contributions](../operations/cross-project-contributions.md) |
| Skill Quality Standard | A JarvisOS skill or skillset needs to be detailed, reusable, and verifiable. | skill creation/review | [Skill Quality Standard](../operations/skill-quality-standard.md) |
| Self-Improvement | A repeated friction pattern should become a candidate, not a silent rule. | learning/reflex signal | [Self-Improvement](../concepts/self-improvement.md) |
| Jarvis Doctor | Public template changes need structural validation before commit/push. | `python3 tools/jarvis-doctor.py` | [Jarvis Doctor](../operations/jarvis-doctor.md) |
| Release Readiness | A public repo, version, changelog, or deployment is being prepared. | `release readiness` | [Release and GitHub Pages](../operations/release-and-github-pages.md) |

## Choosing Quickly

- Start with Light Mode unless the task earns Specialist Mode.
- Use Specialist Mode when state, roles, review, release risk, or long-running continuity matter.
- Use the Command Deck for short invocations.
- Use the Reference Router when several docs could apply.
- Use a Work Pack when execution context is scattered.
- Use Jarvis Doctor before public template commits.

## What This Is Not

The Capability Index is not an automation layer, hidden command parser, or replacement for judgment. It is a map of the existing JarvisOS surfaces.
