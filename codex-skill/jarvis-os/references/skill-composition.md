# Skill Composition Map

Use this reference when more than one skill applies to the same task and the agent needs to decide which skill leads, which skill supports, and how to avoid over-reading.

This map is a routing aid, not a new gate. It should reduce cognitive load by making ownership explicit.

## Composition Contract

When multiple skills apply:

1. Use `skill-dictionary.md` first when the candidate skills are not already obvious from the live skill list or user wording.
2. Pick one lead skill for the main deliverable.
3. Use supporting skills only for the part they uniquely improve.
4. Keep JarvisOS responsible for continuity, memory, Specialist Mode, work orders, handoffs, and closeout.
5. Keep domain skills responsible for domain method, output format, quality bar, and domain-specific verification.
6. Stop loading skill references once the lead/support boundary is clear enough to act.

Do not merge every skill's whole workflow into one mega-process. Compose only the needed pieces.

## Lead Skill Rules

Use the user's requested outcome to choose the lead:

- If the outcome is continuity, memory, project governance, R&D, handoff, status, adoption, or Specialist Mode, `jarvis-os` leads.
- If the outcome is a paper review, referee report, manuscript critique, or LaTeX review package, the relevant academic review skill leads and JarvisOS supports continuity.
- If the outcome is a retro-futurist UI, visual redesign, anti-slop UI critique, or web craft pass, the relevant UI/craft skill leads and JarvisOS supports project governance.
- If the outcome is a JarvisOS skill ticket from another chat, the relevant skill-ticket workflow leads and JarvisOS R&D receives the ticket.
- If the outcome is creating or updating a reusable skill package, `skill-creator` leads for skill mechanics, while `skill-quality-standard.md` defines the JarvisOS quality bar.
- If the outcome is image generation or bitmap asset creation, `imagegen` leads for the bitmap operation, while the domain skill defines art direction and JarvisOS records canonical artifacts when needed.
- If the outcome is email, calendar, document, presentation, spreadsheet, GitHub, or browser work through a plugin skill, the plugin skill leads tool-specific execution and JarvisOS supports memory, project state, and closeout.

If two domain skills seem equally central, state the lead assumption briefly, use the second skill only for its narrow contribution, and proceed unless the ambiguity would change outputs materially.

## JarvisOS Support Duties

When JarvisOS is supporting rather than leading, it still owns:

- reading only the relevant project memory before meaningful work;
- choosing Light Mode versus Specialist Mode;
- preserving durable decisions, blockers, artifacts, and next steps;
- keeping public/private boundaries clear;
- using work orders and role review only when the task complexity earns them;
- closeout integrity for meaningful Specialist Mode work.

JarvisOS should not override the domain skill's technical method unless the domain workflow conflicts with user instructions, safety, privacy, artifact hygiene, or project state.

## Domain Skill Duties

When a domain skill leads, it owns:

- domain-specific intake questions and assumptions;
- method, rubric, style, and quality bar;
- output structure and templates;
- domain-specific verification and repair loops;
- examples and failure modes inside that skill.

The domain skill should not create duplicate project memory, role rosters, or task boards. If durable continuity is needed, route it back through JarvisOS memory discipline.

## Common Recipes

### JarvisOS + Academic Paper Review

Use when the user asks to review a PDF, thesis chapter, preprint, or manuscript with professional critique.

- Lead: the relevant academic review skill.
- Support: JarvisOS for project context, artifact paths, memory, and Specialist Mode only if the review becomes a larger research program.
- Output: the review package defined by the academic skill, usually including LaTeX.
- Avoid: turning a one-paper review into a full JARVIS R&D work order unless the user asks or durable project state changes.

### JarvisOS + Retro-Futurist Web UI

Use when building or critiquing a retro-futurist web UI inside a JarvisOS-governed project.

- Lead: the relevant UI/craft skill for art direction, typography, anti-slop checks, microinteractions, and visual QA.
- Support: JarvisOS for work order state, public artifact framing, verification evidence, and memory.
- Output: implemented UI changes and screenshot/render verification.
- Avoid: letting JarvisOS process language water down the craft-critical design bar.

### JarvisOS + Imagegen

Use when a JarvisOS project needs generated bitmap assets.

- Lead: `imagegen` for the actual generated bitmap.
- Support: the domain skill for prompt/art direction; JarvisOS for canonical asset path, provenance, and artifact status.
- Output: generated image asset plus verified local path if it becomes project material.
- Avoid: using generated images as product truth without checking fit, accessibility, responsiveness, or domain correctness.

### JarvisOS + Skill Ticket / Skill Quality

Use when another JarvisOS chat finds a reusable workflow or skill idea.

- Lead: the relevant skill-ticket workflow when creating the ticket in that chat.
- Lead: `jarvis-os` R&D when implementing the accepted ticket.
- Support: `skill-quality-standard.md` for detailed, long, clear skill expectations.
- Output: ticket first, implementation later only in the JarvisOS R&D workspace.
- Avoid: letting another project mutate JarvisOS core directly.

### JarvisOS + Plugin Skills

Use when a tool/plugin skill is required for the actual work, such as GitHub, Gmail, Calendar, docs, sheets, slides, or browser testing.

- Lead: the plugin skill for tool-specific operations.
- Support: JarvisOS for project context, memory, approval boundaries, and closeout.
- Output: the plugin's natural artifact or action, plus JarvisOS continuity only if durable state changes.
- Avoid: asking the user to perform tool work that the available plugin can do safely.

### JarvisOS + Skill Creator

Use when creating or updating a reusable Codex skill.

- Lead: `skill-creator` for skill package mechanics and structure.
- Support: JarvisOS `skill-quality-standard.md` for detailed JarvisOS skill quality.
- Output: installable skill package or patch.
- Avoid: making a thin skill that depends on hidden chat context to be usable later.

## Conflict Rules

- User instructions outrank all skill defaults when safe and feasible.
- Safety, privacy, destructive action, credentials, paid services, and public/private leak risks outrank speed.
- A domain skill's output format outranks JarvisOS formatting when the requested deliverable belongs to that domain.
- JarvisOS memory discipline outranks domain-skill note-writing when deciding what becomes durable project memory.
- If two skills demand different verification, run the verification tied to the deliverable first, then JarvisOS closeout checks when project state changed.
- If composition becomes heavier than the task, downgrade to Light Mode and use only the lead skill.

## Anti-Patterns

Do not:

- load every referenced skill file just because several skills are installed;
- skip the Skill Dictionary when a specialized task may match an installed standalone skill but the right skill is not obvious;
- create duplicate task boards, session notes, or memories for a domain skill task;
- use JarvisOS as an excuse to soften a specialized skill's quality bar;
- let a domain skill bypass artifact hygiene or public/private boundaries;
- claim a skill was used if its instructions were not read or materially followed;
- preserve temporary composition decisions as standing rules unless real usage proves they generalize.

## Closeout

At closeout, report the composition only when it matters:

- lead skill used;
- supporting skill used;
- output/artifact verified;
- memory updated or intentionally skipped;
- any unresolved skill conflict.

For small tasks, omit the composition report and simply deliver the result.
