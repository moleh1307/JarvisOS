# JARVIS Light

**A local-first operating system for Codex continuity.**

JARVIS Light turns a folder of markdown files into durable assistant memory.  
It helps Codex work across long chats, fresh chats, projects, research, codebases, and handoffs without pretending the chat history itself is the source of truth.

It is inspired by the same continuity problem that Chronicle-style memory tries to solve, but it is intentionally different:

- no background screen capture
- no screenshots
- no always-on memory agent
- no hidden database requirement
- no transcript dumping
- no expensive automatic capture loop

JARVIS Light is **not a Chronicle replacement**.  
It is the lightweight/manual mode: local markdown, explicit retrieval, compact memory, and agent discipline.

## The One-Sentence Version

JARVIS Light makes Codex behave less like a fresh chat and more like an organized teammate that can read the project state, do the work, and leave the next session in a better position.

## What Is Inside

JARVIS Light has two layers.

### 1. JARVIS Memory

The base layer:

- project memory
- personal preferences
- decision logs
- session notes
- handoffs
- artifact hygiene
- source-aware facts
- governed self-improvement

This is for continuity.

### 2. JARVIS Company Mode

The optional serious-project layer:

- Founder / Project Architect
- Chief of Staff
- specialist roles
- task board
- work orders
- role memories
- review gates
- internal critique
- out-of-box thinking
- GitHub / PR workflow guidance
- adoption mode for existing projects

This is for projects where one undifferentiated agent would likely mix design, backend, frontend, QA, research, writing, and release work into one blurry pile.

## Why This Exists

Long Codex chats eventually become awkward:

- too much old context
- compaction noise
- repeated explanations
- lost project state
- unclear latest artifact
- agents saying “done” without enough durable trace

JARVIS Light changes the center of gravity:

```text
Chat = temporary working surface
Markdown vault = durable continuity layer
```

When the chat gets too long, you create a handoff and start fresh.

## What It Is

JARVIS Light is:

- a local markdown vault
- a Codex skill
- a set of templates and operating rules
- a low-token continuity workflow
- readable, editable, inspectable, private by default
- useful for coding, research, writing, planning, and long-running projects

JARVIS Light is not:

- a new chat app
- a model replacement
- an automatic memory recorder
- a screenshot/screen-observation tool
- a database-first knowledge system
- a place to dump full transcripts

## Core Ideas

### Markdown Is The Source Of Truth

Important state lives in `.md` files:

- what the project is
- what was decided
- what is blocked
- what was generated
- what is canonical
- what should happen next

Indexes or databases can be added later, but markdown remains canonical.

### Memory Should Preserve The Next Useful Action

Good memory is not a diary.

Save:

- decisions
- constraints
- current state
- exact next steps
- blockers
- artifact paths and validation
- durable preferences
- handoff context

Avoid:

- transcript dumps
- filler
- repeated summaries
- vague progress notes
- speculative thoughts that were not adopted

### Source-Aware Notes Reduce Fake Certainty

When provenance matters, label facts:

- `User-stated`
- `Observed in repo`
- `Tool result`
- `Agent inference`
- `External source`

Use labels only where they help. Do not turn every note into citation theater.

### Fresh-Chat Handoffs Are A Feature

Long chats are disposable. Project state is not.

When a thread gets long, create:

```text
handoffs/YYYY-MM-DD-project-handoff.md
```

Then start a new chat with a short starter prompt that points to the right project note and handoff.

### Generated Artifacts Need Hygiene

Every meaningful output should answer:

- What is this?
- How was it made?
- Is it canonical, delivery, diagnostic, temporary, or superseded?
- How was it verified?
- What caveats remain?

The goal is not pretty documentation. The goal is not losing track of reality.

## Company Mode

Company Mode is optional. Use it when the project is big enough that specialist roles would help.

Examples:

- building an app
- adopting an existing codebase
- running a research project
- writing a book
- doing quant/data work
- preparing a serious website or product

### Greenfield Mode

Use this when starting from an idea.

The Founder asks only setup-level questions, then creates:

- project charter
- current state
- task board
- role charters
- role memories
- first work orders

Then you can mostly say:

```text
continue
status
show blockers
```

### Adoption Mode

Use this when the project already exists.

The Founder becomes **Founder / Organizational Auditor**:

1. Inspect the repo/folder first.
2. Create `company/adoption-audit.md`.
3. Separate observed facts from inferences and unknowns.
4. Infer roles from the actual project structure.
5. Add the Company Mode layer around the existing project.

Adoption Mode should not rewrite or reorganize the project before it understands it.

### Quality Bar

Company Mode should not stop at “it works.”

Roles should:

- aim for top-tier output for the project stage
- think out of the box
- challenge conventional assumptions
- identify weak parts before the user has to
- create improvement work orders when obvious gaps exist
- visually/materially verify user-facing artifacts
- wait for user approval before final acceptance

For coding projects, the workflow also supports:

- role/task branches
- role-authored commits
- PR handoffs
- version changes after reliable milestones

Example commit author:

```bash
git commit --author="JARVIS Frontend Engineer <your-verified-email@example.com>" -m "Polish task filtering UI"
```

## Folder Structure

```text
.
├── AGENTS.md
├── codex-skill/
│   ├── jarvis/
│   │   └── SKILL.md
│   └── jarvis-company-mode/
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
│   ├── failure-patterns.md
│   ├── learning-log.md
│   ├── proposals/
│   ├── upgrade-roadmap.md
│   └── vault-map.md
└── templates/
    ├── company-mode/
    │   ├── adoption-audit.md
    │   ├── current-state.md
    │   ├── integration-log.md
    │   ├── project-charter.md
    │   ├── role-charter.md
    │   ├── role-memory.md
    │   ├── task-board.md
    │   └── work-order.md
    ├── decision-entry.md
    ├── handoff.md
    ├── project-memory.md
    └── session-note.md
```

## Quick Start

1. Copy this repository to a local folder:

   ```bash
   git clone https://github.com/<you>/jarvis-light.git ~/JARVIS
   cd ~/JARVIS
   ```

2. Install the base JARVIS skill:

   ```bash
   mkdir -p ~/.codex/skills/jarvis
   cp codex-skill/jarvis/SKILL.md ~/.codex/skills/jarvis/SKILL.md
   ```

3. Optional: install Company Mode:

   ```bash
   mkdir -p ~/.codex/skills/jarvis-company-mode
   cp codex-skill/jarvis-company-mode/SKILL.md ~/.codex/skills/jarvis-company-mode/SKILL.md
   ```

4. Start Codex from the vault folder.

5. For normal continuity work:

   ```text
   Jarvis, use JARVIS. Read the relevant project memory first.
   ```

6. For a new serious project:

   ```text
   Jarvis, use JARVIS and JARVIS Company Mode.

   Start a new project in Company Mode.
   Project idea:
   ...

   Your first role is Founder.
   Ask only setup questions that materially affect the project.
   ```

7. For an existing project:

   ```text
   Jarvis, use JARVIS and JARVIS Company Mode.

   Adopt this existing project into Company Mode:
   /path/to/project

   Your first role is Founder / Organizational Auditor.
   Audit first, then create the company layer around the existing structure.
   Do not reorganize or rewrite anything before the audit.
   ```

## Operating Loop

For meaningful work, the agent should:

1. understand the request,
2. identify the project/domain,
3. read the relevant memory,
4. execute the task,
5. verify the result,
6. update the smallest durable note,
7. create a handoff only when continuation would otherwise be lossy.

In Company Mode:

1. Chief of Staff reads current state and task board.
2. It picks the next unblocked task.
3. The assigned role executes.
4. The role runs verification and an out-of-box pass.
5. The company updates task board, role memory, and integration log.
6. Work continues until user approval, a real blocker, or a deliberate pause.

## End-of-Task Memory Check

Before finishing meaningful work:

- Did project state change?
- Was a durable decision made?
- Did a stable preference appear?
- Is there unfinished work or a blocker?
- Is a fresh-chat handoff needed?
- Was a generated artifact verified?
- Did this reveal a reusable lesson or failure pattern?

If not, do not write memory just to write memory.

## Suggested First Setup

1. Edit `memory/personal/preferences.md`.
2. Edit `memory/projects/index.md`.
3. Create one project note from `templates/project-memory.md`.
4. Keep `AGENTS.md` as the root operating rule file.
5. Install only the skills you actually want to use.

## Publishing Your Own Fork

Do not publish your private working vault directly unless you have reviewed it for secrets and personal information.

Recommended pattern:

- private live vault for real memory
- public sanitized template repo for reusable workflow
- copy improvements from private to public only after removing personal context

## License

No license is included in this template by default. Add the license you want before publishing for broad reuse.
