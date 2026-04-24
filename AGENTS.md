# JARVIS Light Instructions

This workspace is a JARVIS Light vault.

JARVIS Light is a local continuity workflow for Codex. It uses markdown files as durable memory so work can continue across chats, projects, and sessions without relying on giant conversation history.

## Core Rules

- Treat markdown as the source of truth.
- Behave like one continuing assistant identity across chats.
- Retrieve relevant vault context before meaningful work.
- Ask when ambiguity affects code, memory, project direction, or irreversible work.
- Write the smallest durable note that preserves future continuity.
- Do not dump transcripts.
- Do not invent memory.
- Do not create noisy notes just because a conversation happened.
- Memory should preserve the next useful action, not the whole story.
- Keep canonical generated artifacts inside the relevant project repo/workspace.
- Treat `Downloads` and Desktop copies as temporary or delivery copies unless explicitly declared canonical.
- Use clickable absolute markdown links when referencing local artifacts.
- Verify exact artifacts before saying they are ready.

## Retrieval Order

For meaningful work:

1. Understand the request.
2. Identify the active project or domain.
3. Read `memory/projects/index.md` if the active project is unclear.
4. Read the relevant project note.
5. Read recent session or handoff notes only if needed.
6. Execute the task.
7. Update the smallest correct note if durable state changed.

## Memory Writing

Write durable memory for:

- decisions
- project constraints
- reusable project context
- stable preferences
- blockers
- next steps
- handoff state
- recurring workflows
- generated artifacts that future agents need, including whether each artifact is canonical, delivery, diagnostic, temporary, or superseded

Avoid storing:

- raw transcripts
- casual chatter
- duplicated facts
- speculative thoughts that were not adopted
- temporary reasoning with no future value

## Source-Aware Memory

When provenance matters, label durable facts with:

- `User-stated`
- `Observed in repo`
- `Tool result`
- `Agent inference`
- `External source`

Use labels only where they improve trust or tell a future agent what to re-check.

## Artifact Hygiene

Every generated artifact should answer:

- What is this?
- How was it made?
- Should it be treated as canonical, delivery, diagnostic, temporary, or superseded?

Before saying an artifact is ready, verify it:

- data outputs: file exists, row count, key columns/header, summary counts, small sample, and caveats;
- plots/images: render or open the file, check title/axes/definition, and confirm the canonical output path;
- documents/decks/PDFs: open or render enough to confirm the file is not corrupt and contains expected content.

When writing memory for generated artifacts, prefer compact operational bullets: input path, script/workflow path, output path, method definition, validation result, caveat, and next step.

## Large Project Notes

Project notes should stay quick to scan. If a project note becomes a long chronological log or retrieval becomes painful, split it into a project folder:

- `memory/projects/<project>/index.md`
- `memory/projects/<project>/methods.md`
- `memory/projects/<project>/outputs.md`
- `memory/projects/<project>/decisions.md` if project-local decisions need a home

Do not split preemptively. Split only when retrieval is getting worse, and leave a clear pointer from the old project note.

## Handoffs

Create a handoff when:

- a chat becomes long, compacted, or token-expensive,
- work is unfinished,
- work is blocked,
- a future chat needs a compact bridge.

Active handoffs live under `handoffs/` and should be linked from the relevant project note.

## End-of-Task Check

Before finishing meaningful work:

- Did project state change?
- Was a durable decision made?
- Did a stable preference or working rule appear?
- Is there unfinished work or a blocker?
- Is a fresh-chat handoff needed?

If not, do not write memory just to write memory.
