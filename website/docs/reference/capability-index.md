---
title: Capability Index
description: A compact map of what JARVIS OS can do and where each capability lives.
---

# Capability Index

This page is a map, not a new workflow. Use it when you want to know what JARVIS OS can do and where to look next.

JarvisOS agents should apply these capabilities by relevance. The user should not need to name every internal feature; the agent chooses the smallest useful set for the task.

| Capability | Use it when | Primary trigger | Where to read |
| --- | --- | --- | --- |
| Relevance-First Auto-Routing | JARVIS OS is invoked and the agent must choose which features apply. | `Jarvis, use JARVIS OS` | this page, [Reference Router](../operations/reference-router.md) |
| Bare JARVIS OS Mode Choice Gate | JARVIS OS is invoked without a task, mode, project, or target. | `Jarvis, use JARVIS OS` alone | [Light Mode](../modes/light-mode.md), [Specialist Mode](../modes/specialist-mode.md) |
| Feature Adoption Check | Existing JarvisOS features were named or naturally triggered and should not be silently skipped. | JARVIS R&D, workflow feedback, public template change | [Checklists](checklists.md) |
| Light Mode | The task is small, local, or self-contained. | `Jarvis, use JARVIS OS` | [Light Mode](../modes/light-mode.md) |
| Specialist Mode | The project needs roles, work orders, durable state, review, or release discipline. | `Jarvis, use JARVIS OS Specialist Mode` | [Specialist Mode](../modes/specialist-mode.md) |
| Specialist Mode Target Gate | A bare Specialist Mode request could apply to the wrong project. | `go for Specialist Mode` without target | [Specialist Mode](../modes/specialist-mode.md) |
| Mode Exit Ramp | Specialist Mode work is closed and the next task can be lighter. | closeout after serious work | [Light Mode](../modes/light-mode.md), [Specialist Mode](../modes/specialist-mode.md) |
| Closeout Stack Order | Several closeout pieces apply and the final report could become bloated. | closeout with example, verification, rollback, options | [Checklists](checklists.md) |
| Command Deck | You want short invocation phrases instead of long prompts. | `status`, `continue`, `new idea` | [Prompt Library](prompt-library.md) |
| Clarifying Follow-Up Gate | A short/vague request would change implementation depending on interpretation. | `change this`, `fix it`, `make it better` | [Checklists](checklists.md) |
| Referent Snapshot | The request says `this`, `that`, `it`, `here`, or similar and the target must be identified. | vague target words | [Checklists](checklists.md) |
| Clarification Receipt | The user answers a follow-up with a terse reply that must bind back to the pending question. | `yes`, `go`, `second`, `that one` | [Checklists](checklists.md) |
| Accidental Message Guard | A prior message was wrong, accidental, or cancelled. | `ignore previous`, `cancel that` | [Prompt Library](prompt-library.md) |
| Fresh-Chat Handoff | A chat is getting long or another session needs to continue. | `fresh-chat handoff` | [Fresh Chat](../getting-started/fresh-chat.md), [Handoffs](../concepts/handoffs.md) |
| One-Screen Handoff Seed | Continuation is likely, but a full handoff file would be too much. | long thread, likely fresh chat | [Checklists](checklists.md) |
| Usage Example Closeout | A JARVIS R&D idea or workflow feature was implemented and the user needs to understand how it works in practice. | implemented idea closeout | [Checklists](checklists.md) |
| Artifact Hygiene | Files, docs, images, data, PDFs, or generated outputs need trust labels and verification. | any meaningful artifact | [Artifact Hygiene](../concepts/artifact-hygiene.md) |
| Context Freshness Badge | A task relies on memory, state files, git status, public versions, blockers, dates, or mutable external facts. | stale-risk context | [Checklists](checklists.md) |
| Verification Breadcrumb | A result, artifact, version, build, test, dashboard, or public claim was verified and future agents may need to trust or rerun it. | `verified`, `tests passed`, `ready` | [Checklists](checklists.md) |
| Rollback Handle | A public template change, installed skill change, workflow rule, or consequential R&D feature may need a future safe undo path. | release closeout, workflow patch | [Checklists](checklists.md) |
| Scratchpad Expiry | Temporary notes, assumptions, QA outputs, screenshots, drafts, Work Packs, or diagnostics may become memory noise. | closeout after scratch work | [Checklists](checklists.md) |
| Reference Router | Several workflow references could apply and the agent should not over-read. | complex routing | [Reference Router](../operations/reference-router.md) |
| Skill Dictionary | A specialized task may match a standalone/domain skill and the agent should not load every skill file. | research/math/tool/domain work | [Skill Dictionary](../operations/skill-dictionary.md) |
| Project Skill Index Routing | A Specialist Mode project already has local project skills and the agent must decide whether one applies. | `company/project-skills/index.md` exists | [Project Skill Incubator](../operations/project-skill-incubator.md) |
| Project Skill Incubator | A Specialist Mode project has repeated local workflow that may deserve a local project skill. | repeated project-local procedure | [Project Skill Incubator](../operations/project-skill-incubator.md) |
| Agent Work Pack | A meaningful task has scattered context, tools, constraints, and done criteria. | `create a Work Pack` | [Agent Work Pack](../operations/agent-work-pack.md) |
| Done Shape | A deliverable needs a clear target before implementation. | meaningful deliverable Work Pack | [Agent Work Pack](../operations/agent-work-pack.md) |
| Assumption Ledger | A Work Pack needs to carry consequential assumptions without blocking execution. | meaningful Work Pack with uncertainty | [Agent Work Pack](../operations/agent-work-pack.md) |
| Skill Composition | Multiple skills apply and the lead/support boundary is unclear. | named or overlapping skills | [Skill Composition](../operations/skill-composition.md) |
| Task Lifecycle | A Specialist Mode work order needs state, risk, evidence, blockers, or closeout. | work order change | [Task Lifecycle](../operations/task-lifecycle.md) |
| Quality Gates | Output needs critique, verification, or closeout integrity. | QA/review/readiness | [Quality Gates](../operations/quality-gates.md) |
| Public Artifact Framing | A README, public page, bio, landing page, email, or simple site will be judged externally. | public-facing artifact | [Public Artifacts](../operations/public-artifacts.md) |
| R&D Idea Loop | A team is improving a product, workflow, or JarvisOS itself idea by idea. | `new idea` | [R&D Loop](../modes/rd-loop.md) |
| Dogfood Return Check | A new R&D loop starts and the last feature may have produced evidence. | start of `new idea` loop | [R&D Loop](../modes/rd-loop.md) |
| Feature Saturation Check | Several consecutive R&D additions land in the same workflow area and the next idea may add bloat. | repeated nearby workflow features | [Checklists](checklists.md) |
| Cross-Project Contribution | Another JarvisOS chat finds a reusable workflow or skill candidate. | `JarvisOS Skill Ticket` | [Cross-Project Contributions](../operations/cross-project-contributions.md) |
| Skill Quality Standard | A JarvisOS skill or skillset needs to be detailed, reusable, and verifiable. | skill creation/review | [Skill Quality Standard](../operations/skill-quality-standard.md) |
| Self-Improvement | A repeated friction pattern should become a candidate, not a silent rule. | learning/reflex signal | [Self-Improvement](../concepts/self-improvement.md) |
| Jarvis Doctor | Public template changes need structural validation before commit/push. | `python3 tools/jarvis-doctor.py` | [Jarvis Doctor](../operations/jarvis-doctor.md) |
| Release Readiness | A public repo, version, changelog, or deployment is being prepared. | `release readiness` | [Release and GitHub Pages](../operations/release-and-github-pages.md) |

## Choosing Quickly

- Apply features by relevance; do not wait for the user to name every feature.
- If JARVIS OS is invoked with no task, mode, project, or target, explain Core and Specialist Mode briefly and ask which mode to use.
- Use Feature Adoption Check when Melih names a feature or a task naturally triggers one.
- Start with Light Mode unless the task earns Specialist Mode.
- Use Specialist Mode when state, roles, review, release risk, or long-running continuity matter.
- Resolve the Specialist Mode target before creating files, memory, or work orders.
- Use the Command Deck for short invocations.
- Use the Reference Router when several docs could apply.
- Use the Skill Dictionary when a specialized task may match a standalone/domain skill.
- Scan `company/project-skills/index.md` when it exists before choosing a Specialist Mode project workflow.
- Use Project Skill Incubator before creating local project skills.
- Use a Work Pack when execution context is scattered.
- Use Jarvis Doctor before public template commits.

## What This Is Not

The Capability Index is not an automation layer, hidden command parser, or replacement for judgment. It is a map of the existing JarvisOS surfaces.
