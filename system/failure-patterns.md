# Failure Patterns

## Purpose

Track recurring ways work can go wrong, plus the prevention rule already encoded or proposed.

Use this file for stable patterns, not every one-off mistake.

## Pattern Template

```md
## Pattern: Name

- Symptom:
- Risk:
- Prevention:
- Where encoded:
- Example notes:
```

## Pattern: Memory Bloat

- Symptom: Agents create too many session notes, duplicate facts, or narrative summaries.
- Risk: The vault becomes another messy transcript system and retrieval gets worse.
- Prevention: Memory should preserve the next useful action, not the whole story; update the smallest canonical note.
- Where encoded: `AGENTS.md`, `codex-skill/jarvis-os/SKILL.md`
- Example notes:

## Pattern: Methodological Drift

- Symptom: An agent silently swaps an exact/full/research method for a faster approximate method.
- Risk: Research validity and important outputs become hard to trust.
- Prevention: Ask before replacing explicitly requested exact, exhaustive, or full methods.
- Where encoded: `AGENTS.md`, `codex-skill/jarvis-os/SKILL.md`
- Example notes:

## Pattern: Artifact Confusion

- Symptom: Similar files exist across project outputs, `Downloads`, Desktop, diagnostics, and superseded versions.
- Risk: Future agents or users may treat the wrong file as canonical.
- Prevention: Label artifacts as canonical, delivery, diagnostic, temporary, or superseded; keep canonical artifacts in project workspaces; verify exact artifacts before saying ready.
- Where encoded: `AGENTS.md`, `codex-skill/jarvis-os/SKILL.md`, templates
- Example notes:

## Pattern: Stale Project Memory

- Symptom: A project note claims a current state that no longer matches repo/files/tool results.
- Risk: Agents become overconfident from stale memory.
- Prevention: Use source labels, verify against files/tools when stakes matter, and update the current-state capsule after meaningful changes.
- Where encoded: `AGENTS.md`, `codex-skill/jarvis-os/SKILL.md`, templates
- Example notes:
