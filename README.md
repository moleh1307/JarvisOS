# JARVIS Light

JARVIS Light is a local, markdown-first continuity workflow for Codex.

It is inspired by the same problem space as Chronicle-style memory: keeping an assistant useful across chats, projects, and long-running work. It is not a replacement for Chronicle. It is a lighter manual alternative for people who want continuity without background agents, screenshots, automatic screen capture, or high token usage.

## What It Is

JARVIS Light is:

- a local markdown vault for durable assistant memory
- a Codex skill plus a small set of rules/templates
- a way to start fresh chats without losing project state
- a workflow for writing only the memory that matters
- inspectable, editable, and easy to keep private

JARVIS Light is not:

- a new chat app
- a model replacement
- an automatic memory recorder
- a screenshot or screen-observation system
- a database-first knowledge system
- a transcript dump

## Why Use It

Long Codex chats eventually become expensive or awkward because context grows and compaction starts carrying old state forward. JARVIS Light treats chats as temporary working surfaces and markdown as the durable state.

The intended flow is:

1. Start a task.
2. Read the smallest relevant vault note.
3. Do the work.
4. Update only the durable memory that changed.
5. If a chat gets too long, create a compact handoff and continue in a fresh chat.

This keeps continuity without asking the model to carry everything in the conversation forever.

## Chronicle vs JARVIS Light

Chronicle-style systems can observe recent screen context and generate memories automatically. That is powerful, but it can require more tokens, more automation, more privacy review, and more trust in inferred memory.

JARVIS Light takes the opposite approach:

- no background agents
- no screenshots
- no automatic capture
- no hidden memory
- no database requirement
- no memory writing unless the active agent decides it matters

Think of it as a low-token, local-first, human-inspectable memory workflow.

## Core Ideas

### 1. Markdown Is The Source Of Truth

Everything important lives in readable `.md` files. Search or indexing can be added later, but markdown remains canonical.

### 2. Agent-Mediated Memory

The user should not maintain a diary. The active Codex agent writes memory when durable context changes.

Examples worth saving:

- decisions
- project state
- next steps
- blockers
- reusable preferences
- handoff context

Examples usually not worth saving:

- casual comments
- low-value status chatter
- raw transcripts
- speculative thoughts that were not adopted

### 3. Fresh-Chat Handoffs

When a chat becomes long, compacted, or token-expensive, create a short handoff under `handoffs/`. A new chat can resume by reading the handoff and the relevant project note.

### 4. Source-Aware Memory

Use provenance labels only when they help trust or future re-checking:

- `User-stated`
- `Observed in repo`
- `Tool result`
- `Agent inference`
- `External source`

Do not label every bullet. Use labels only where ambiguity matters.

### 5. Artifact Hygiene

Generated artifacts should be easy to audit later. For every meaningful output, record what it is, how it was made, whether it is canonical/delivery/diagnostic/temporary/superseded, and the validation result.

Canonical outputs should live in the project workspace. Delivery copies in `Downloads` or Desktop are useful, but they should not become the source of truth unless explicitly declared canonical.

### 6. No Premature Project Skills

Project-specific skills should be extracted only after a workflow repeats. At the start of a project, use project notes and session notes. Let notes discover the workflow; create skills only after the workflow stabilizes.

### 7. Split Large Project Notes Only When Needed

Keep project notes flat while they remain easy to scan. If a project note becomes a long chronological log, migrate to a project folder with an `index.md` plus focused notes such as `methods.md` and `outputs.md`.

Do not split preemptively. Split when retrieval is getting worse.

## Folder Structure

```text
.
├── AGENTS.md
├── codex-skill/
│   └── jarvis/
│       └── SKILL.md
├── handoffs/
│   └── README.md
├── logs/
│   └── decisions.md
├── memory/
│   ├── personal/
│   │   └── preferences.md
│   └── projects/
│       ├── index.md
│       └── example-project.md
├── sessions/
│   └── README.md
├── system/
│   ├── upgrade-roadmap.md
│   └── vault-map.md
└── templates/
    ├── decision-entry.md
    ├── handoff.md
    ├── project-memory.md
    └── session-note.md
```

## Quick Start

1. Copy this repository to a local folder such as `~/JARVIS`.
2. Copy the skill into your Codex skills directory:

   ```bash
   mkdir -p ~/.codex/skills/jarvis
   cp codex-skill/jarvis/SKILL.md ~/.codex/skills/jarvis/SKILL.md
   ```

3. In Codex, start work from the vault folder.
4. For meaningful tasks, ask Codex to use JARVIS memory.
5. Update project notes and session notes only when durable state changes.

## Suggested First Setup

1. Edit `memory/personal/preferences.md` with your stable working preferences.
2. Edit `memory/projects/index.md` with your active, paused, and completed projects.
3. Create one project note from `templates/project-memory.md`.
4. Keep `AGENTS.md` as the root operating rule file.

## Operating Loop

For meaningful work, the agent should:

1. understand the request,
2. identify the project/domain,
3. read `memory/projects/index.md` if project choice is unclear,
4. read the relevant project note,
5. execute the task,
6. run the end-of-task memory check,
7. update the smallest correct note,
8. create a handoff only when continuation needs it.

## End-of-Task Memory Check

Before finishing meaningful work, ask:

- Did project state change?
- Was a durable decision made?
- Did a stable user preference appear?
- Is there unfinished work, a blocker, or an exact next step?
- Has the chat become long, compacted, or likely to continue elsewhere?
- Was any generated artifact verified and stored in the canonical project workspace?

If none of these matter, leave the vault alone.

## Publishing Your Own Fork

Do not publish your private working vault directly unless you have reviewed it for secrets and personal information.

Recommended pattern:

- keep a private live vault for your real memory,
- keep a separate sanitized template repo for the reusable workflow,
- copy improvements from the private vault into the public template only after removing personal context.

## License

No license is included in this template by default. Add the license you want before publishing for broad reuse.
