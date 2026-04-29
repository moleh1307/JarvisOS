# Vault Map

## Directory Roles

### `AGENTS.md`

Root operating rules.

### `codex-skill/`

Installable Codex skill package. Copy `codex-skill/jarvis-os/` into `~/.codex/skills/jarvis-os/`.

Specialist Mode / Company Mode references live inside `codex-skill/jarvis-os/references/`; there is no separate Specialist Mode skill package.

### `memory/projects/`

Durable project notes and current-state summaries. Start with `memory/projects/index.md`.

### `memory/personal/`

Stable user preferences and cross-project context.

### `sessions/`

Timestamped notes for meaningful work sessions.

### `handoffs/`

Active continuation notes for unfinished, blocked, or long-chat work.

### `logs/decisions.md`

Durable decisions.

### `templates/`

Reusable note templates.

`templates/company-mode/` contains optional templates for role-based projects: adoption audit, project charter, current state, task board, role charter, role memory, work order, and integration log.

### `system/`

System-level notes for the workflow itself:

- `system/learning-log.md` captures candidate lessons and promotion status.
- `system/failure-patterns.md` tracks stable recurring failure modes and prevention rules.
- `system/proposals/` stores consequential workflow changes that should be reviewed before adoption.

## Canonical Homes

- Stable user preference -> `memory/personal/preferences.md`
- Project state -> `memory/projects/<project>.md`
- Project routing -> `memory/projects/index.md`
- Durable decision -> `logs/decisions.md`
- Meaningful session -> `sessions/`
- Active continuation -> `handoffs/`
- Candidate self-improvement lesson -> `system/learning-log.md`
- Recurring failure pattern -> `system/failure-patterns.md`
- Consequential proposed workflow change -> `system/proposals/`
- Specialist Mode / Company Mode project operation -> project-local `company/` folder, guided by `codex-skill/jarvis-os/SKILL.md` and `templates/company-mode/`
