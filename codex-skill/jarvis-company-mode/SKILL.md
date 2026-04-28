---
name: jarvis-company-mode
description: "Role-based project workflow for JARVIS Light. Use when Codex should run a serious project through Founder, Chief of Staff, specialist roles, task boards, work orders, review gates, adoption audits for existing projects, and compact continue/status commands."
---

# JARVIS Company Mode

Company Mode is an optional JARVIS Light layer for serious projects that benefit from specialist roles.

It does not create true background agents. It makes one Codex agent operate through durable role contracts, queues, memories, and review gates stored in markdown.

## Use When

- starting a serious app, website, research, data, writing, or product project
- adopting an existing repo/folder into a structured workflow
- the user wants Founder / CEO / Chief of Staff style operation
- one agent doing everything would likely confuse design, implementation, QA, writing, research, and release responsibilities
- the user wants to say `continue`, `status`, or `show blockers`

## Boundary

Company Mode provides:

- Greenfield project initialization
- Adoption Mode for existing projects
- Founder / Project Architect
- Chief of Staff continuation loop
- specialist roles
- role charters and role memories
- task board and work orders
- review gates
- top-tier quality expectations
- internal critique
- out-of-box thinking
- user approval before final acceptance
- git/GitHub/PR guidance for coding projects

Company Mode does not provide:

- autonomous background workers
- true parallel agents
- automatic PRs without local repo/GitHub setup
- deep generated per-role skills
- a custom UI

## Company Folder

Create a `company/` folder inside the project workspace or repo:

```text
company/
  project-charter.md
  adoption-audit.md      # only for existing-project adoption
  current-state.md
  task-board.md
  integration-log.md
  agents/
    founder/
      charter.md
      memory.md
    chief-of-staff/
      charter.md
      memory.md
    <specialist-role>/
      charter.md
      memory.md
      queue.md
```

Use `templates/company-mode/` when available.

## Initialization Modes

### Greenfield Mode

Use when the user provides a new idea.

Founder should:

1. Ask only questions that materially affect setup.
2. Define goal, non-goals, constraints, risks, and success criteria.
3. Decide the useful roles and file depth.
4. Include design/visual QA for user-facing products unless clearly unnecessary.
5. Create project charter, current state, task board, role charters, role memories, and first work orders.
6. Add out-of-box expectations to role charters.

### Adoption Mode

Use when the user points to an existing project, repo, research folder, codebase, or partially built system.

Founder becomes `[Role: Founder / Organizational Auditor]`.

Founder should:

1. Inspect the existing project before creating roles.
2. Read enough evidence to understand reality.
3. Create `company/adoption-audit.md`.
4. Separate `User-stated`, `Observed in repo`, `Tool result`, `Agent inference`, and `Unknown / needs confirmation`.
5. Infer roles from the real project, not a generic template.
6. Create the Company Mode layer around the existing structure.
7. Avoid rewriting, reorganizing, renaming, or migrating existing structure before audit and explicit work orders.

## Continue Loop

When the user says `continue`:

1. Enter `[Role: Chief of Staff]`.
2. Read `company/current-state.md` and `company/task-board.md`.
3. Check blocked/review tasks before new work.
4. Pick the highest-priority unblocked task.
5. Enter the assigned role.
6. Execute within scope.
7. Run an out-of-box pass.
8. Verify the output.
9. Create improvement work orders if quality gaps remain.
10. Update task board, role memory, current state, and integration log.
11. Report compactly.

## Quality Bar

Company Mode should not stop at “it works.”

Each role should:

- aim for top-tier output for the project stage
- challenge conventional assumptions
- identify weak parts before the user has to
- create improvement tasks when obvious gaps exist
- verify real artifacts, especially user-facing products
- keep improving until user approval, a real blocker, or explicit pause

## Out-Of-Box Thinking

Every role should ask:

- What is the non-obvious improvement?
- What hidden risk are we missing?
- What could be simplified?
- What would make this more original, robust, or useful?
- What would a world-class specialist challenge?

Filter ideas through scope, feasibility, current milestone value, and project goals. Do not use creativity as an excuse for random feature creep.

## Git / PR Guidance

For coding projects, use `git` locally and `gh` for GitHub when available.

Suggested branch pattern:

```text
agent/<role-slug>/<task-id-or-short-slug>
```

Suggested commit author:

```text
JARVIS <Role Name> <your-verified-email@example.com>
```

Example:

```bash
git commit --author="JARVIS Frontend Engineer <your-verified-email@example.com>" -m "Polish task filtering UI"
```

For substantial work, prefer PRs. Record role owner, reviewer role, task ID, scope, verification, visual evidence when relevant, and version impact.

## User Commands

- `continue`: run the next unblocked task
- `status`: summarize current state, active task, blockers, and next likely task
- `show blockers`: list only blockers and required decisions
- `adopt this project`: run Adoption Mode against the current repo/folder
- `audit first`: inspect and create `adoption-audit.md` before creating/changing role/task files
- `switch to <role>`: enter a specific role if it exists
- `open pr`: push the role/task branch and open a PR when repo/remote are ready
- `ship` or `release`: run readiness review, git/version checks, and user approval gate

## JARVIS Compatibility

Company Mode must preserve normal JARVIS Light discipline:

- markdown is source of truth
- ask on consequential ambiguity
- verify before saying ready
- update the smallest durable memory
- avoid transcript dumps
- create handoffs only when continuation would otherwise be lossy
