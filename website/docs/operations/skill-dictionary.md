---
title: Skill Dictionary
description: A compact routing index for choosing standalone and domain skills without loading every skill file.
---

# Skill Dictionary

The Skill Dictionary helps an agent choose the right standalone/domain skill when the user does not name one explicitly.

It is separate from the Capability Index:

- Capability Index: internal JARVIS OS features, such as Feature Adoption Check or Jarvis Doctor.
- Skill Dictionary: standalone/domain skills, plugin skill families, and lead/support ownership.

## Use It When

- The request sounds like specialized research, math, document, data, browser, GitHub, image, skill, or plugin work.
- Several skills might apply and loading every `SKILL.md` would create context bloat.
- A new skill was added, removed, renamed, or materially rerouted.

## Routing Shape

1. Scan the compact dictionary.
2. Pick one lead skill for the main deliverable.
3. Add supporting skills only when they uniquely improve a subtask.
4. Read only the selected skill files.
5. Stop reading once the lead/support boundary is clear enough to act.

## Maintenance

When a workflow change creates, installs, removes, renames, or materially changes a skill, update the Skill Dictionary in the same work order.

Run the dictionary check when available:

```bash
python3 tools/skill-dictionary-check.py
```

For local deployments with custom installed skills:

```bash
python3 tools/skill-dictionary-check.py --skills-root "$HOME/.codex/skills"
```

## Failure Mode

If the dictionary becomes a giant duplicate of every skill file, it has failed. It should stay a routing index: short triggers, non-triggers, ownership, and path.
