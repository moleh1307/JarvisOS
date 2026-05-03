# Agent Work Pack

Use this reference when an agent needs a compact task-local execution context before starting meaningful work.

An Agent Work Pack is a short temporary mission packet. It gives the current agent the smallest useful set of instructions for this task: what to read, what mode to use, what to avoid, what tools are available, what output is expected, and what proves done.

## Purpose

JarvisOS has strong continuity, but serious tasks can make agents synthesize too many surfaces at once: current state, task board, work order, skills, routing references, role headers, memory rules, capability surface, verification, and closeout.

The Work Pack reduces that load by turning the relevant pieces into one task-local brief.

It is not a second task board. It is not canonical project history. It is not required for small Light Mode work.

## When To Use

Create or mentally assemble a Work Pack when:

- starting a serious Specialist Mode task;
- resuming after a fresh chat, compaction, or interruption;
- onboarding a new agent to a complex project;
- the task spans multiple references, tools, or artifacts;
- the agent might otherwise over-read the vault;
- a work order exists but the execution context is scattered;
- the user asks for a plan before implementation and the plan needs operational clarity.

Use a compact inline Work Pack in the chat when writing a file would be ceremony.

Create a file-backed Work Pack when:

- another chat/agent will likely pick it up;
- the task is high-risk, long-running, or multi-step;
- the task has a real work order and needs reusable execution context;
- tool, privacy, or verification boundaries are easy to lose.

Skip Work Packs for:

- trivial questions;
- one-command answers;
- tiny file edits;
- ordinary Light Mode work where the relevant context is already in the prompt;
- tasks where the work order already contains everything needed and the agent can proceed.

## Lifecycle

Default lifecycle: `temporary`.

Work Packs should expire when the task finishes. Do not keep updating them as living project state. If the content becomes durable, promote the relevant facts to:

- work order;
- current-state capsule;
- handoff;
- project memory;
- decision log;
- capability surface;
- artifact README.

At closeout, either delete/ignore the temporary pack, mark it superseded, or record that it became a handoff/work-order update.

## Required Fields

Keep Work Packs compact. A useful Work Pack answers:

- Task: what needs to be done now.
- Operating mode: Light Mode, Minimal Specialist Layer, or Full Specialist Mode.
- Role: the functional role currently executing.
- Risk lane: standard, normal, high-risk, or emergency.
- Read first: exact files or references to load.
- Do not read unless needed: surfaces that would create noise.
- Active constraints: user preferences, privacy, scope, no-go areas.
- Required tools: capabilities needed for execution.
- Allowed autonomous actions: what can proceed without asking.
- Stop/ask triggers: exact boundaries that require Melih or another real owner.
- Expected outputs: artifact paths or report shape.
- Done Shape: who the finished output is for, what form it takes, what must be visible, and what would make it feel wrong.
- Verification: commands, checks, renders, tests, source checks, or review gates.
- Memory update target: where durable state goes if changed.
- Done criteria: observable conditions.

Optional fields:

- Public/private boundary.
- Dependency/install boundary.
- Role handoff notes.
- Dogfood/eval evidence.
- Expiration condition.

## Template

```markdown
# Agent Work Pack

- Status: temporary / active / superseded / promoted-to-handoff / promoted-to-work-order
- Created:
- Expires:

## Mission

- Task:
- User intent:
- Success definition:
- Non-goals:

## Mode And Role

- Operating mode:
- Role:
- Risk lane:
- Lifecycle state:
- Work order:

## Read Set

- Read first:
- Read only if needed:
- Do not read:

## Constraints

- Scope boundaries:
- Privacy boundary:
- Do-not-touch:
- User preferences:
- Stop/ask triggers:

## Capability Surface

- Available tools:
- Required tools:
- Missing or risky tools:
- Allowed autonomous actions:
- Approval needed:

## Execution

- Steps:
- Expected outputs:
- Canonical artifact:
- Temporary artifacts:

## Done Shape

- Audience/user:
- Final form:
- Must be visible:
- Must not become:
- Quality feel:

## Verification

- Required checks:
- Evidence to record:
- Known verification gaps:

## Memory And Closeout

- Update targets:
- Done criteria:
- Closeout options:
```

## Generation Procedure

1. Identify the task and active project.
2. Choose Light Mode, Minimal Specialist Layer, or Full Specialist Mode.
3. Read only the current-state/work-order/context needed to fill the pack.
4. Route references with `reference-router.md` or `task-cards.md`.
5. For meaningful deliverables, define Done Shape before implementation.
6. Declare capability and verification boundaries if tool-dependent.
7. Mark what is temporary and what would become durable.
8. Execute the task.
9. At closeout, promote only durable facts and let the pack expire.

## Quality Bar

Good Work Pack:

- fits on one screen when possible;
- names exact files/references;
- prevents over-reading;
- states the finished output shape before execution when the deliverable is meaningful;
- makes done criteria obvious;
- separates temporary execution context from durable memory;
- reduces repeated questions.

Bad Work Pack:

- duplicates the full work order;
- lists every JarvisOS rule;
- becomes another current-state file;
- is mandatory for tiny tasks;
- contains vague instructions like "do research well";
- uses Done Shape as decorative prose instead of a concrete output target;
- survives after the task without a reason.

## Interaction With Other Surfaces

- Work order: canonical task record. The Work Pack can summarize it, not replace it.
- Current state: canonical live project status. The Work Pack should not duplicate long history.
- Handoff: durable continuation artifact. Promote a Work Pack to a handoff only when another session needs it.
- Task cards: compact checklists. The Work Pack may name one primary card.
- Capability surface: tool/approval boundary. The Work Pack may contain the compact declaration.
- Memory discipline: decides what survives after closeout.

## Examples

### Light Mode Example

```markdown
# Agent Work Pack

- Status: temporary

## Mission

- Task: Explain how to use a named installed skill with a file path.
- Success definition: User gets a copyable command.
- Non-goals: Do not create files or update memory.

## Mode And Role

- Operating mode: Light Mode
- Role: Chief of Staff
- Risk lane: standard

## Read Set

- Read first: current user request.
- Do not read: company work orders, public repo, old sessions.

## Verification

- Required checks: command uses absolute path placeholder and names expected output.

## Memory And Closeout

- Update targets: none.
- Done criteria: concise usable command provided.
```

### Specialist Mode Example

```markdown
# Agent Work Pack

- Status: temporary
- Expires: after JRD-084 closeout

## Mission

- Task: Add Agent Work Pack to JarvisOS.
- Success definition: installed/public routing can discover the reference; template exists; state closes cleanly.
- Non-goals: Do not add a new task board or mandatory ceremony.

## Mode And Role

- Operating mode: continuous R&D / maintenance
- Role: Skill Engineer
- Risk lane: normal
- Work order: JRD-084

## Read Set

- Read first: jarvis-os/SKILL.md, reference-router.md, task-cards.md, templates/company-mode/.
- Read only if needed: continuation.md, memory-discipline.md.
- Do not read: old unrelated work orders.

## Verification

- Required checks: rg discoverability, diff check, stale dashboard.

## Memory And Closeout

- Update targets: work order, task board, current state, project memory.
- Done criteria: reference/template/routing exist and validation passes.
```

## Anti-Patterns

- Creating Work Packs for every user reply.
- Saving Work Packs as permanent memory by default.
- Hiding consequential ambiguity inside the pack instead of asking.
- Using a Work Pack as permission to skip source inspection or verification.
- Letting Work Packs become stale after task scope changes.
