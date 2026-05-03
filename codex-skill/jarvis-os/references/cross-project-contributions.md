# Cross-Project Contributions

Use this reference when a JarvisOS-powered project or chat discovers an improvement that may belong in JarvisOS itself.

The bridge lets real projects contribute learning through explicit skill tickets without letting every project directly mutate core workflow rules.

## Primary Command

Use this command in any JarvisOS-powered chat:

```text
JarvisOS Skill Ticket
```

or:

```text
Jarvis, create a JarvisOS Skill Ticket from this chat.
```

The agent should review the available chat/project context, create a detailed ticket, and return the ticket number. The user can then bring that ticket number to the JarvisOS R&D chat for triage or implementation.

## Contribution Contract

Other JarvisOS chats may create skill tickets or contribution candidates. They must not directly promote project-local discoveries into standing JarvisOS behavior unless the user explicitly asks for that patch in the JarvisOS R&D workspace.

A contribution candidate may propose:

- a new or revised skill;
- a skillset made from repeated project patterns;
- a workflow rule or reference patch;
- a template field or template;
- an eval seed;
- documentation or prompt-library update;
- a project-local pattern that should stay project-local.

## Trigger Phrases

Route here when the user says:

- "JarvisOS Skill Ticket";
- "create a JarvisOS Skill Ticket";
- "make a ticket for JarvisOS R&D";
- "this should become a JarvisOS feature";
- "make this reusable in JarvisOS";
- "capture this for JarvisOS R&D";
- "turn what we learned here into a skill";
- "review this chat and propose a JarvisOS skill/skillset";
- "contribute this project back to JarvisOS".

## Skill Ticket Rules

When the user wants R&D to implement later, create a ticket instead of a loose candidate.

Use ticket IDs:

```text
JST-YYYYMMDD-short-slug
```

If the central JARVIS vault is available, save tickets under:

```text
company/skill-tickets/
```

If the central vault is not available, output the ticket in the final answer with ID `JST-PENDING-short-slug`.

The source chat should close with:

- ticket ID;
- ticket path, if saved;
- one-line summary;
- exact R&D handoff command.

## Intake Rules

When a contribution is requested:

1. Identify the source project/chat and the useful pattern.
2. Review only the available chat context and relevant project artifacts. If full history is compacted or unavailable, say what is missing and use durable handoffs/session notes when present.
3. Separate project-specific details from reusable behavior.
4. Mark the privacy lane: `private`, `needs-sanitization`, or `public-safe`.
5. State evidence strength: `one-off`, `repeated-in-project`, `repeated-across-projects`, `high-impact`, or `user-approved`.
6. Decide candidate type: `skill`, `skillset`, `workflow-rule`, `template`, `docs`, `eval-seed`, `project-local-only`, or `reject`.
7. Save the ticket/candidate in the smallest correct home.

## Canonical Homes

Prefer this order:

- If the request is for later R&D implementation, save a ticket under `company/skill-tickets/`.
- If inside a Specialist Mode project, save a project-local candidate under `company/contributions/`.
- If the central JARVIS vault is available and the user explicitly wants R&D routing, save or summarize into `company/contribution-inbox/`.
- If neither exists, create a compact candidate in the current project memory or final answer and ask the user to paste it into a JARVIS R&D chat.

Do not save private project details into the public JarvisOS template.

## Candidate Shape

A good candidate answers:

- What happened?
- What project/chat revealed it?
- What is the reusable pattern?
- What should become a skill, skillset, rule, template, docs patch, or eval?
- What should stay project-local?
- What private details must be removed before public use?
- What is the expected benefit?
- What could this make worse?
- How should JARVIS R&D verify it?

## Skill Or Skillset Review

When asked to create a skill or skillset from a chat:

1. Extract recurring tasks, tools, decisions, artifacts, quality checks, prompts, and failure modes.
2. Cluster them into candidate skills only when they are reusable outside the source project.
3. Reject clusters that are merely project memory, one-off taste, private facts, or ordinary instructions.
4. For each candidate skill, draft:
   - name;
   - purpose;
   - trigger conditions;
   - required context/files/tools;
   - workflow steps;
   - output artifacts;
   - verification checks;
   - privacy boundary;
   - examples.
5. Recommend `create-skill`, `merge-into-existing-skill`, `keep-as-project-memory`, `make-template`, or `reject`.

Skills must be detailed and long enough to explain the workflow clearly. Do not create shallow skill stubs. A future agent should be able to use the skill without reconstructing the original chat.

Do not install or publish a new skill unless the user explicitly approves that implementation step.

## R&D Review

JARVIS R&D triages contribution candidates as:

- `reject`: not reusable, unsafe, or too project-specific;
- `project-local`: useful, but should stay in the source project;
- `document-only`: add docs/prompt guidance, no behavior patch;
- `template-update`: update a reusable template;
- `skill-patch`: update installed JarvisOS behavior;
- `new-skill-candidate`: draft a separate skill with `skill-creator`;
- `eval-seed`: preserve as a future regression scenario;
- `public-release`: sanitize and mirror into the public template.

Promotion still requires evidence, user approval, high-impact prevention, or successful dogfood.

## Anti-Bloat Rules

- Do not convert every good project habit into a JarvisOS rule.
- Do not create skills that only encode one project's private context.
- Do not add a new named mechanism if Reflexes, Friction Inbox, or R&D Idea Loop can already handle it.
- Do not publicize private file paths, names, datasets, clients, credentials, or unpublished plans.
- Do not create background automation claims. This is manual cross-project intake unless a real automation exists.

## Output Commands

Use these in other chats.

### Contribution Candidate

```text
Jarvis, use JARVIS OS.

This project/chat revealed something that may improve JarvisOS itself.
Use the Cross-Project Contribution Bridge.
Review the available chat history and relevant project memory/artifacts.
Create a contribution candidate with:
- reusable pattern;
- evidence strength;
- privacy lane;
- proposed JarvisOS change;
- what should stay project-local;
- verification path;
- recommended R&D triage outcome.

Do not patch JarvisOS directly. If the central JARVIS vault is available, save it under company/contribution-inbox/; otherwise give me a compact candidate I can paste into the JarvisOS R&D chat.
```

### Skill Ticket

```text
JarvisOS Skill Ticket
```

Expanded form:

```text
Jarvis, use JARVIS OS.

Create a JarvisOS Skill Ticket from this chat.
Review the available chat history, project memory, decisions, artifacts,
repeated workflows, prompts, tools, and failure modes.

Create a detailed skill ticket with:
- ticket ID;
- source evidence;
- reusable pattern;
- proposed skill or skillset;
- detailed skill draft;
- privacy lane;
- what stays project-local;
- anti-bloat review;
- suggested implementation path;
- verification plan;
- R&D handoff prompt.

Save it under company/skill-tickets/ if that vault is available.
Otherwise print the full ticket in chat.
Do not implement it here.
```

### Skillset Extraction

```text
Jarvis, use JARVIS OS.

Review this chat's available history, project memory, decisions, artifacts, repeated workflows, prompts, tools, and failure modes.
Use the Cross-Project Contribution Bridge to propose a JarvisOS skill or skillset based on what became reusable here.

For each proposed skill, include:
- name;
- trigger conditions;
- reusable workflow;
- required inputs/tools;
- output artifacts;
- verification checks;
- privacy boundary;
- examples;
- recommendation: create-skill, merge-into-existing-skill, keep-as-project-memory, make-template, or reject.

Do not install or publish anything yet. Package the result as a contribution candidate for JarvisOS R&D.
```
