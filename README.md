<p align="center">
  <img src="assets/jarvisos-banner.png" alt="JARVIS OS banner" />
</p>

# JARVIS OS

[![Docs](https://img.shields.io/badge/docs-moleh1307.github.io%2FJarvisOS-1f6feb?style=for-the-badge)](https://moleh1307.github.io/JarvisOS/)
[![Built By](https://img.shields.io/badge/built_by-MOLEH-2ea44f?style=for-the-badge)](https://github.com/moleh1307)
[![Version](https://img.shields.io/badge/version-0.0.97-da3633?style=for-the-badge)](VERSION)

**A local-first operating system for Codex continuity.**

JARVIS OS makes Codex feel less like a fresh chat and more like an organized teammate: it remembers through markdown, hands work across sessions, runs serious projects with specialist roles, and improves without hiding state in a black box.

Invoke it once; agents should route the right JarvisOS features by relevance instead of waiting for you to name each internal mechanism.
Short prompts are fine; when intent is unclear, agents should ask a sharp follow-up instead of guessing.

Memory files. Handoffs. Task boards. Specialist Mode. Artifact hygiene. Self-improvement logs. No hidden database. No transcript dumping.

---

## Docs

Full docs live in the Docusaurus site under [website/](website/). Start with the docs [Capability Index](website/docs/reference/capability-index.md) when you want the compact feature map.

After GitHub Pages is enabled, the public docs URL is:

```text
https://moleh1307.github.io/JarvisOS/
```

## Quick Start

```bash
git clone https://github.com/moleh1307/JarvisOS.git
cd JarvisOS
```

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

## Why

Long agent work breaks when the chat becomes the only memory.

JARVIS OS moves durable state into files:

```text
chat = working surface
markdown = continuity layer
```

## How It Works

| Layer | Purpose |
| --- | --- |
| `memory/` | project state, preferences, durable context |
| `sessions/` | meaningful work episodes |
| `handoffs/` | fresh-chat continuation |
| `logs/` | decisions that should survive the chat |
| `company/` | optional Specialist Mode for serious projects |
| `codex-skill/` | installable JARVIS OS skill package |

## Modes

**Light Mode** for small work. Retrieve only what matters, do the task, update memory only when it helps the next session.

**Specialist Mode** for serious work. Add roles, task boards, work orders, review gates, capability checks, and closeout discipline.

## Prompts

Command deck:

| Say | Result |
| --- | --- |
| `status` | compact project state |
| `continue` | next unblocked task |
| `new idea` | one R&D loop idea |
| `create a Work Pack` | task-local execution context |
| `JarvisOS Skill Ticket` | reusable workflow ticket |
| `ignore previous` | discard accidental instruction |

Normal continuity:

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

Fresh handoff:

```text
Jarvis, use JARVIS OS.

Create a fresh-chat handoff for this project.
Include current objective, completed work, blockers, exact next steps,
and files the next chat should read first.
```

Serious project:

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a project for:
...

Ask the material questions, choose the right team, and create the first work orders.
```

Existing repo:

```text
Jarvis, use JARVIS OS Specialist Mode.

Adopt this existing project:
/path/to/project

Audit first. Do not reorganize before understanding the repo.
```

Create a JarvisOS skill ticket:

```text
JarvisOS Skill Ticket
```

## What It Is Not

JARVIS OS is not a new chat app, model, database, screen recorder, or automatic surveillance memory system. It is a local markdown operating discipline for agents.

## Install The Skill

Copy or symlink the skill folder into Codex:

```bash
mkdir -p ~/.codex/skills
cp -R codex-skill/jarvis-os ~/.codex/skills/jarvis-os
```

Then start a new Codex chat and say:

```text
Jarvis, use JARVIS OS.
```

## License

MIT. See [LICENSE](LICENSE) if present in your fork.
