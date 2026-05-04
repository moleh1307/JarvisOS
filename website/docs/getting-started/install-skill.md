---
title: Install The Skill
description: Install the JARVIS OS Codex skill from the template.
---

# Install The Skill

The installable skill lives in:

```text
codex-skill/jarvis-os/
```

Copy it into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R codex-skill/jarvis-os ~/.codex/skills/jarvis-os
```

Restart or open a fresh Codex chat, then invoke it:

```text
Jarvis, use JARVIS OS.
```

## What The Skill Contains

The skill includes:

- Core continuity rules;
- Light Mode guidance;
- Specialist Mode routing;
- reference router;
- task cards;
- memory discipline;
- adoption and greenfield setup;
- quality and QA gates;
- R&D idea loop;
- self-improvement reflexes.

The skill is the executable protocol. The docs explain it, but the skill is what agents should follow.

## Updating The Skill

When the skill changes, update the installed copy:

```bash
rm -rf ~/.codex/skills/jarvis-os
cp -R codex-skill/jarvis-os ~/.codex/skills/jarvis-os
```

If an old chat is still active, use a workflow refresh prompt:

```text
Jarvis, workflow refresh.

Use JARVIS OS Specialist Mode.

Specialist Mode target:
/path/to/project
Read the latest installed JARVIS OS skill and the live project state.
Continue from the next unblocked task using the latest workflow rules.
```
