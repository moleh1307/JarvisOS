# Reference Router

Use this reference before loading deeper JARVIS OS references when a task could match several workflows. Its job is routing, not execution.

The router keeps `SKILL.md` short while making reference selection explicit. It should reduce prompt bloat, stale refresh prompts, and missed workflow gates.

## Routing Principles

- Route by the user's intent, the project operating mode, artifact risk, and escalation boundaries.
- Load the smallest reference bundle that can guide the next action correctly.
- Combine references only when the work genuinely spans them.
- Prefer the highest-consequence route first: safety, public release, private data, destructive action, and major claims outrank normal continuation.
- Stop reading once the selected route is enough to act. Do not load every reference for confidence theater.
- If the selected route exposes a wrong frame, generic output, skipped evidence, or stale state, run Stop-the-Line Review from `continuation.md`.

## Fast Router

| Trigger | Load first | Add when needed |
| --- | --- | --- |
| Older active chat needs latest workflow | `workflow-refresh.md` | `continuation.md`, `roles-and-roster.md` |
| Durable memory write, stale memory conflict, long project note, handoff, project-note split, memory cleanup | `memory-discipline.md` | `continuation.md` for closeout or handoff |
| `continue`, `go`, `next`, short approval, status, blocker, interruption | `continuation.md` | `adaptive-operating-patterns.md` for queue re-ranking or claim review |
| New serious project or unclear project shape | `greenfield.md` | `adaptive-operating-patterns.md`, `roles-and-roster.md`, domain-specific quality references |
| Existing repo/project takeover | `adoption-takeover.md` | `github-release-versioning.md`, `quality-qa-and-critique.md` |
| Tool-dependent work, plugin/tool use, local app/browser/imagegen/GitHub/deploy/email capability, or verification boundary | `capability-surface.md` | `quality-qa-and-critique.md`, `github-release-versioning.md`, domain reference |
| Role headers, role names, team changes, roster drift | `roles-and-roster.md` | `continuation.md` for response preflight |
| Research, data, proof, architecture, strategy, or consequential claims | `adaptive-operating-patterns.md` | `quality-qa-and-critique.md` |
| Excellence-critical non-visual output | `adaptive-operating-patterns.md` | `quality-qa-and-critique.md`, `innovation-feedback.md` |
| User-facing app/site/product with visual quality risk | `creative-preproduction.md` | `visual-concept-pipeline.md`, `quality-qa-and-critique.md` |
| Concrete UI concept, screenshot, mockup, or generated design target | `visual-concept-pipeline.md` | `creative-preproduction.md` for art direction |
| Small public-facing artifact: personal site, public email, README, bio, one-pager, deployed static site | `public-artifacts.md` | `creative-preproduction.md` or `visual-concept-pipeline.md` if craft-critical |
| QA, rendered checks, package smoke, internal critique, artifact readiness | `quality-qa-and-critique.md` | `continuation.md` for closeout integrity |
| GitHub, PR, branch, first push, release, version, changelog, public repo readiness | `github-release-versioning.md` | `continuation.md` for closeout integrity |
| Workflow feedback, new rule proposal, deep brainstorm, R&D improvement | `innovation-feedback.md` | `continuation.md` for off-roadmap proposal gate |
| Generic, stale, wrong, misleading, repeated-failure, or low-quality momentum | `continuation.md` | the domain reference that should own the correction |

## Core-Only Cases

Stay in the main `SKILL.md` without deeper Specialist Mode references when the task is ordinary JARVIS Core work:

- answer a simple question from current context;
- inspect or update one memory note;
- create a small handoff from already-known state;
- make a narrow code or docs edit in a normal project;
- run a simple command or explain a local artifact.

If the task becomes consequential, public-facing, long-running, or role-governed, route again.

## Routing Procedure

1. Identify the active mode: JARVIS Core or Specialist Mode.
2. Identify the request class: continue, initialize, adopt, build, research, public artifact, visual craft, release, QA, workflow feedback, or recovery.
3. Select the smallest reference bundle from the table.
4. Read only the selected references and the live project state needed for the next action.
5. Execute or propose according to the selected route.
6. If the route was wrong, run Stop-the-Line Review and switch route.

## Conflict Rules

- If a task is both public-facing and visual, start with `public-artifacts.md` for audience/trust/privacy, then use `creative-preproduction.md` or `visual-concept-pipeline.md` for craft.
- If a task is tool-dependent or verification-heavy, load `capability-surface.md` early enough to declare available tools, approval lane, and verification path before execution or closeout.
- If a task changes durable memory and also executes project work, do the project work first, then use `memory-discipline.md` for the smallest correct continuity update.
- If a task is both release-related and implementation-related, start with the implementation reference, then run `github-release-versioning.md` before reporting readiness.
- If a task is both research/proof and public-facing, use `adaptive-operating-patterns.md` for confidence lanes before public wording.
- If the user asks for a workflow change while a project is active, use `innovation-feedback.md` and `continuation.md` so the side quest is proposed or tracked without losing the active task.
- If a named external resource, URL, screenshot, repo, skill, or PDF is part of the request, inspect it or state why it is inaccessible before calling the route complete.

## Closeout

For meaningful Specialist Mode work, the selected route should still end through `continuation.md` closeout checks:

- state files agree with the report;
- docs/version/git/artifacts match reality;
- blockers and options reflect actual autonomy boundaries;
- the next task is concrete, created, assigned, or started unless truly blocked.
