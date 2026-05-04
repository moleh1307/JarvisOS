# Skill Quality Standard

Use this reference when creating, reviewing, accepting, or implementing a JarvisOS skill, skillset, or skill-ticket draft.

The standard is inspired by highly operational Codex skills: strong skills define ownership, delegation boundaries, hard no-fake rules, deterministic helpers, repair loops, QA artifacts, and acceptance criteria. JarvisOS skills should copy that clarity without adding length for its own sake.

## Core Principle

A good JarvisOS skill should be detailed enough that a future agent can execute the workflow without reconstructing the original chat.

Long is acceptable when the length carries operational value. Shallow stubs are not acceptable for serious skills.

## When To Apply

Apply this standard when:

- creating a new JarvisOS skill or skillset;
- drafting a proposed skill inside a JarvisOS Skill Ticket;
- reviewing a skill ticket before R&D acceptance;
- patching an existing skill after field evidence;
- turning a repeated project workflow into reusable JarvisOS behavior;
- deciding whether a behavior belongs in core JarvisOS, a separate skill, a reference file, a template, an eval seed, or project-local memory.

Do not apply the full standard when:

- the request is a one-off project note;
- the proposed behavior is not reusable;
- the user only needs a tiny prompt snippet;
- a small docs clarification is enough;
- the workflow belongs in project memory, not a reusable skill.

## Skill Shape

Every serious JarvisOS skill should answer these questions explicitly.

### Identity

- What is the skill called?
- What problem does it own?
- What user language should trigger it?
- What near-miss language should not trigger it?
- Is this a standalone skill, a JarvisOS reference, a task card, a template, or a skillset?

### Ownership Boundary

State what the skill owns and what it does not own.

Good ownership language:

- "This skill owns source ingestion, claim extraction, evidence routing, and output packaging."
- "This skill delegates chart rendering to the spreadsheets skill and does not hand-build workbook internals."
- "This skill creates the R&D ticket only; it does not implement JarvisOS core changes in the source project chat."

Avoid vague ownership:

- "Help with research."
- "Improve UI."
- "Make workflows better."

### Delegation Boundary

Name every external skill, tool, script, connector, or deterministic helper the skill should use.

For each dependency, say:

- when to use it;
- what inputs it receives;
- what outputs it owns;
- what the current agent must still inspect or verify;
- what fallback is allowed if the dependency is unavailable;
- what fallback is not allowed because it would fake the result.

### Hard Boundaries

Include explicit "never" rules for failure modes that would silently corrupt the output.

Examples:

- never claim unavailable chat history was reviewed;
- never promote a one-off project trick into JarvisOS core without anti-bloat review;
- never publish private project paths, credentials, client details, or unpublished research into public templates;
- never mark an artifact ready before verifying the exact file;
- never replace required visual, data, or source evidence with invented placeholders;
- never mutate JarvisOS core from a non-R&D project chat unless the user explicitly asks for implementation there.

### Default Workflow

Give the normal path as numbered steps.

For each step, include:

- the action;
- the expected inputs;
- the expected output or artifact;
- the decision point, if any;
- the verification that proves the step completed.

Use exact commands, file paths, templates, or script names when they exist. If a step is conceptual, make the decision rule concrete.

### Visible Progress

For long-running or multi-artifact skills, define a small progress checklist.

Good checklist qualities:

- 3-6 steps;
- one active step at a time;
- user-friendly wording;
- only mark complete when the real artifact, decision, or verification exists.

Skip visible checklists for tiny skills where the checklist would be ceremony.

### Repair And Fallback

Every serious skill needs a repair path.

State:

- what can fail;
- how to detect it;
- whether to retry, repair the smallest failing scope, reroute to a reference, ask the user, or reject the candidate;
- which fallback is acceptable;
- which fallback is forbidden because it would fabricate quality.

### Outputs And Provenance

Define all expected outputs.

For each output, state:

- path or canonical home;
- whether it is canonical, diagnostic, temporary, delivery-ready, public-safe, private, or superseded;
- how it was produced;
- what source evidence supports it;
- what future agent should inspect first.

### Acceptance Criteria

Acceptance criteria should be observable.

Prefer:

- exact files exist;
- markdown frontmatter parses;
- reference routing includes the new reference;
- public/private versions agree where intended;
- leak scan is clean;
- examples cover trigger and non-trigger cases;
- validation commands pass;
- ticket status and current-state files agree.

Avoid:

- "looks good";
- "is clear";
- "should help";
- "future agents will understand it" without a concrete check.

## Skill Ticket Draft Standard

A skill ticket that proposes a skill should include enough detail to become an implementation source.

Minimum sections:

- skill or skillset name;
- purpose;
- trigger conditions;
- non-triggers;
- required context;
- ownership boundary;
- delegation boundary;
- hard boundaries;
- default workflow;
- visible progress, if long-running;
- repair or fallback workflow;
- outputs and artifact provenance;
- verification;
- privacy boundary;
- examples;
- failure modes to avoid;
- anti-bloat review.

If the source evidence is weak, still draft the shape, but mark the confidence lane honestly and recommend `document-only`, `project-local`, `eval-seed`, or `reject` when appropriate.

## R&D Acceptance Review

Before accepting a skill proposal, the R&D team should ask:

- Does this solve repeated or high-impact friction?
- Does it belong in a separate skill instead of core JarvisOS?
- Does an existing reference already cover most of it?
- Can it replace or simplify an existing rule?
- Are the trigger and non-trigger boundaries clear?
- Is the workflow executable without hidden chat context?
- Are the hard boundaries strong enough to prevent fake completion?
- Are acceptance criteria observable?
- Is the public/private boundary safe?

Reject, narrow, or keep project-local if the proposal is mostly aesthetic, duplicative, one-off, or too broad to execute.

## Implementation Checklist

When implementing an accepted skill-quality change:

1. Add or update the installed skill/reference first.
2. Mirror public-safe guidance into the public template only when it belongs there.
3. Update the Reference Router if agents need to discover the reference.
4. Update `skill-dictionary.md` when a skill is created, installed, removed, renamed, or materially rerouted.
5. Update the skill ticket template or docs if ticket authors must use the standard.
6. Run targeted validation: parse frontmatter where relevant, check references exist, run the skill dictionary verifier when skills changed, run `rg` for routing terms, run public leak scan for public changes, and run `git diff --check`.
7. Update the work order, task board, and current state only with durable facts.

## Anti-Patterns

- Long prose without executable steps.
- A skill that only says "be thoughtful" or "do quality work."
- Trigger conditions so broad the skill fires for everything.
- No non-triggers.
- No repair path.
- No verification path.
- Public examples containing private paths or project-specific facts.
- Rewriting JarvisOS core for a project-local trick.
- Adding a new skill when a template, task card, or reference patch would be enough.
