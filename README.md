# JARVIS Light

**A local-first operating system for Codex continuity.**

Current version: `0.0.25`

Latest update: Company Mode v0.8.1 adds Operating Mode Declaration so `continue` routes differently for discovery, build, audit, polish, release, dogfood, research attack, recovery, and maintenance.

JARVIS Light turns a folder of markdown files into durable assistant memory.  
It helps Codex work across long chats, fresh chats, projects, research, codebases, and handoffs without pretending the chat history itself is the source of truth.

It is inspired by the same continuity problem that Chronicle-style memory tries to solve, but it is intentionally different:

- no background screen capture
- no screenshots
- no always-on memory agent
- no hidden database requirement
- no transcript dumping
- no expensive automatic capture loop

JARVIS Light is **not a Chronicle replacement**.  
It is the lightweight/manual mode: local markdown, explicit retrieval, compact memory, and agent discipline.

## The One-Sentence Version

JARVIS Light makes Codex behave less like a fresh chat and more like an organized teammate that can read the project state, do the work, and leave the next session in a better position.

## Copy-Paste Starts

Use these prompts as starting points. Replace the project details and paths.

### 1. Normal Continuity Work

```text
Jarvis, use JARVIS.

Read the relevant project memory first, then help me with:
...
```

### 2. Fresh-Chat Handoff

```text
Jarvis, use JARVIS.

This chat is getting long. Create a fresh-chat handoff for this project.
Include current objective, completed work, blockers, exact next steps, and files the next chat should read first.
```

### 3. Refresh An Older Active Chat

Use this when JARVIS or Company Mode has been updated while an older project chat is still active.

```text
Jarvis, workflow refresh.

Read the latest installed JARVIS and JARVIS Company Mode skills before continuing:
- ~/.codex/skills/jarvis/SKILL.md
- ~/.codex/skills/jarvis-company-mode/SKILL.md

Then read:
- company/team-roster.md if it exists
- company/current-state.md
- company/task-board.md

If company/team-roster.md does not exist, create or propose a small workflow refresh task to add it.

Follow the latest workflow rules from now on, especially:
- every Company Mode reply starts with a roster-backed role header
- before every user-facing reply, run Response Preflight; if Company Mode is active or the topic is Company Mode/workflow R&D, the first line must be the roster-backed role header
- if unsure which role owns the reply, use Chief of Staff for routing/status, Workflow Architect for workflow diagnosis/design, and Skill Engineer for skill/rule/template changes
- role names are optional and must come from company/team-roster.md
- if no role name exists, use only [Role: Role Title]
- no passive acknowledgement; ok/yes/go/next/? should continue when unblocked
- Founder can evolve the team when needed
- roles should critique weak orders and propose better paths
- version changes must update visible docs
- reusable workflow friction should become a feedback candidate
- internal role review is the default; do not ask me for routine comments/review/approval when the team can decide
- internally accept milestones after role review and QA, then continue to the next useful task
- craft-critical user-facing work must classify craft criticality, activate design leadership, run reference intelligence, write an art direction brief, compare divergent concepts, and pass screenshot-based Design QA before major implementation
- if UI/visual work is rejected as generic, ugly, AI-looking, template-like, or not best-in-field, re-enter Creative Preproduction instead of restyling incrementally or asking me for taste by default
- before creating or reshaping a serious project, Founder runs Project-Shape Inference: infer what kind of work this is, what makes success hard, what evidence matters, what roles/artifacts are needed, and which verification/adversarial gates are justified
- company/current-state.md should declare an Operating mode, and Chief of Staff should use it to route `continue` rather than treating every phase like generic task execution
- do not use fixed project-type recipes; choose roles/artifacts from the actual project shape
- use confidence lanes for consequential claims/results: verified, working-assumption, speculative, needs-audit, rejected
- trigger adversarial review for major proof claims, design directions, method choices, architecture decisions, data results, release candidates, or public claims
- after meaningful discoveries, Chief of Staff should check whether the bottleneck changed and re-rank the queue instead of blindly following old work orders
- after adoption audit and baseline preservation, takeover means the company owns the project outcome
- if a role identifies necessary follow-up work, it must create/assign/start the work order unless blocked
- if I approve a listed set of safe actions, execute the whole approved set instead of asking again item by item
- project-scoped free dev/test dependencies, official stack plugins, and normal test assets can be installed when required by the accepted stack or QA plan unless they require sudo/global install, credentials, paid services, telemetry/cloud enablement, destructive changes, or unusual system-level impact
- approval for a dependency/tooling class carries through the current task chain; do not ask again for exact package-manager commands after I approve the class or say not to ask again
- clean isolated agent-created QA/demo data without asking when needed for review/release; ask only before touching real user data
- report single-role work as the executing role, and multi-role aggregate work as Chief of Staff
- after several QA/infrastructure tasks, Founder or Chief of Staff should check whether the next task improves product/research value rather than only adding more tests
- verified role/task branch pushes and PR updates can proceed without asking when the remote exists and no sensitive/release risk is present
- when I provide a GitHub repo URL for a coding project, configure it and push a verified README-backed baseline unless there is a concrete blocker
- after internal acceptance, merge safe role/task branches and push main when project policy allows
- ask before protected/default branch changes when policy is unknown, publishing releases/tags/packages, changing remotes/settings, force-pushing, deleting branches, or risking secrets/private memory
- every completion should state verification, blockers, and one explicit next-action label:
  - Next task:
  - Blocked:
  - Decision needed:
  - User review requested:
```

For long or messy threads, use a fresh-chat handoff instead of trying to keep the old chat alive.

```text
Jarvis, create a fresh-chat handoff for this project using the latest JARVIS workflow.
```

### 4. New App Or Product

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Start a new project in Company Mode.
Project idea:
...

Your first role is Founder.
Ask all material questions needed to understand the project.
Then choose the right workspace, decide the team, and create the first high-leverage work orders.
```

### 5. Existing Repo Adoption

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Adopt this existing project into Company Mode:
/path/to/project

Your first role is Founder / Organizational Auditor.
Audit first, then create the company layer around the existing structure.
Do not reorganize or rewrite anything before the audit.
```

### 6. Research Project

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Start a research team for:
...

Your first role is Principal Investigator / Founder.
Ask all material questions needed to understand the research question, data, method, risks, and success criteria.
Then decide the research team and create the first work orders.
```

### 7. Data / Quant Project

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Start a data/quant project for:
...

Your first role is Founder.
Ask all material questions needed to understand the data, objective, constraints, validation needs, and delivery target.
Then decide the required team and first work orders.
Do not let anyone call results ready without verification and artifact hygiene.
```

### 8. Website Or Launch Page

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Build a serious website for:
...

Founder should ask all material questions needed to understand the audience, offer, brand, content, visual direction, constraints, and success criteria.
Then decide the team and first work orders.
The team should critique weak design or messaging without waiting for me to say "make it better."
```

### 9. Writing / Thesis / Book

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Create an editorial team for:
...

Founder should ask all material questions needed to understand audience, thesis, scope, sources, tone, structure, and delivery format.
Then decide the editorial team and first work orders.
Keep citations, claims, and next writing tasks durable in markdown.
```

### 10. Bug Or Side Quest During Company Mode

```text
Jarvis, side quest for the current Company Mode project:
...

Classify this as clarification, defect, side quest, or scope change.
Preserve the interrupted task and tell me whether the main flow resumes afterward.
```

### 11. Keep Going Without Micromanaging

```text
ok
```

In an active Company Mode project, short acknowledgements such as `ok`, `yes`, `go`, `next`, or `?` should not produce passive replies. They should continue the next unblocked task or explain the exact blocker.

### 12. Force Innovation Mode

```text
Jarvis, use JARVIS and JARVIS Company Mode.

For the next task, force Innovation Mode.
Generate meaningfully different options, critique them for value/risk/cost/originality/fit, then choose the best practical path.
Do not implement a risky or irreversible idea without creating a proposal or asking first.
```

Roles may also self-invoke Innovation Mode when the work is ambiguous, strategically important, creatively underdeveloped, expensive to reverse, or likely to become generic without deeper thinking.

### 13. Report Workflow Feedback

Use this when a real project exposes a reusable JARVIS / Company Mode improvement.

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Feedback for the workflow:
...

Record this as a feedback candidate.
Classify whether it is project-local or should be routed to JARVIS R&D.
Do not turn it into a standing rule until it is triaged.
```

### 14. Release / Version Update

```text
Jarvis, use JARVIS and JARVIS Company Mode.

Run release readiness for this project.
Check verification, version metadata, README/changelog visibility, git status, and whether a PR or tag is needed.
Do not publish a release or stop the company without my approval.
```

## What Is Inside

JARVIS Light has two layers.

### 1. JARVIS Memory

The base layer:

- project memory
- personal preferences
- decision logs
- session notes
- handoffs
- artifact hygiene
- source-aware facts
- governed self-improvement

This is for continuity.

### 2. JARVIS Company Mode

The optional serious-project layer:

- Founder / Project Architect
- Chief of Staff
- specialist roles
- task board
- work orders
- role memories
- review gates
- internal critique
- out-of-box thinking
- adaptive team changes
- assertive role critique
- optional role names
- team roster for canonical role identity
- GitHub autonomy rules for role/task branches
- explicit next-action language
- tool-aware QA before internal acceptance or external escalation
- autonomous internal PR/merge behavior
- repo readiness gate with README requirement
- Adoption Takeover Authority
- Next-Task Ownership
- selective innovation mode
- workflow feedback loop
- GitHub / PR workflow guidance
- adoption mode for existing projects
- modular skill references so agents load only the detailed procedure they need
- operating mode declaration for mode-aware continuation

This is for projects where one undifferentiated agent would likely mix design, backend, frontend, QA, research, writing, and release work into one blurry pile.

## Why This Exists

Long Codex chats eventually become awkward:

- too much old context
- compaction noise
- repeated explanations
- lost project state
- unclear latest artifact
- agents saying “done” without enough durable trace

JARVIS Light changes the center of gravity:

```text
Chat = temporary working surface
Markdown vault = durable continuity layer
```

When the chat gets too long, you create a handoff and start fresh.

## What It Is

JARVIS Light is:

- a local markdown vault
- a Codex skill
- a set of templates and operating rules
- a low-token continuity workflow
- readable, editable, inspectable, private by default
- useful for coding, research, writing, planning, and long-running projects

JARVIS Light is not:

- a new chat app
- a model replacement
- an automatic memory recorder
- a screenshot/screen-observation tool
- a database-first knowledge system
- a place to dump full transcripts

## Core Ideas

### Markdown Is The Source Of Truth

Important state lives in `.md` files:

- what the project is
- what was decided
- what is blocked
- what was generated
- what is canonical
- what should happen next

Indexes or databases can be added later, but markdown remains canonical.

### Memory Should Preserve The Next Useful Action

Good memory is not a diary.

Save:

- decisions
- constraints
- current state
- exact next steps
- blockers
- artifact paths and validation
- durable preferences
- handoff context

Avoid:

- transcript dumps
- filler
- repeated summaries
- vague progress notes
- speculative thoughts that were not adopted

### Source-Aware Notes Reduce Fake Certainty

When provenance matters, label facts:

- `User-stated`
- `Observed in repo`
- `Tool result`
- `Agent inference`
- `External source`

Use labels only where they help. Do not turn every note into citation theater.

### Fresh-Chat Handoffs Are A Feature

Long chats are disposable. Project state is not.

When a thread gets long, create:

```text
handoffs/YYYY-MM-DD-project-handoff.md
```

Then start a new chat with a short starter prompt that points to the right project note and handoff.

### Generated Artifacts Need Hygiene

Every meaningful output should answer:

- What is this?
- How was it made?
- Is it canonical, delivery, diagnostic, temporary, or superseded?
- How was it verified?
- What caveats remain?

The goal is not pretty documentation. The goal is not losing track of reality.

## Company Mode

Company Mode is optional. Use it when the project is big enough that specialist roles would help.

Examples:

- building an app
- adopting an existing codebase
- running a research project
- writing a book
- doing quant/data work
- preparing a serious website or product

### Greenfield Mode

Use this when starting from an idea.

The Founder asks all material questions needed to understand the project, then creates:

- project charter
- project-shape inference
- team roster
- current state
- task board
- role charters
- role memories
- first work orders
- optional strategy/evidence/adversarial-review artifacts when useful

Then you can mostly say:

```text
continue
status
show blockers
```

### Adoption Mode

Use this when the project already exists.

The Founder becomes **Founder / Organizational Auditor**:

1. Inspect the repo/folder first.
2. Create `company/adoption-audit.md`.
3. Separate observed facts from inferences and unknowns.
4. Infer roles from the actual project structure.
5. Add the Company Mode layer around the existing project.

Adoption Mode should not rewrite or reorganize the project before it understands it.

After audit and baseline preservation, adoption should turn into takeover. The company becomes responsible for the project outcome; existing code is evidence, not authority. Roles may refactor, redesign, replace, merge, delete, reorganize, or rebuild parts of the project when justified by the charter, quality bar, verification, and task scope.

### Quality Bar

Company Mode should not stop at “it works.”

Roles should:

- aim for top-tier output for the project stage
- classify craft criticality for user-facing or presentation-sensitive work
- run Creative Preproduction for craft-critical or signature artifacts before major implementation
- use reference intelligence and anti-references for serious design/presentation work
- create divergent concepts and choose internally before building
- think out of the box
- challenge conventional assumptions
- critique weak orders and propose better paths
- identify weak parts before the user has to
- create improvement work orders when obvious gaps exist
- visually/materially verify user-facing artifacts
- internally accept normal milestones and keep moving
- ask the user only for final stop/closure, public release, credentials/cost/destructive actions, strategic direction changes, or explicitly requested user review

### Adaptive Project-Shape Inference

Before designing the team or first work orders, Founder should infer the project's shape:

- what kind of work this is
- what makes success hard
- what failure would look like
- what evidence/artifacts matter
- what roles and disciplines are needed
- what confidence lanes are needed
- what verification or adversarial review gates are justified
- whether a strategy map, evidence ledger, attack tree, claims map, design calibration, or similar artifact would help

This is not a recipe system. A research problem, app, data project, writing project, and strategy project may all get different structures, but only because the specific problem demands it.

### Operating Mode Declaration

Project-shape inference describes what kind of work this is. Operating mode says what the company should do now.

`company/current-state.md` should declare one current operating mode:

- `discovery`
- `build`
- `audit`
- `polish`
- `release`
- `dogfood`
- `research attack`
- `recovery`
- `maintenance`

Chief of Staff uses this during `continue` to choose the right role, reference file, next task type, and queue re-ranking behavior. A project should not handle setup questions, product polishing, release readiness, broken-state recovery, and hard research attacks with the same generic loop.

Founder and Chief of Staff can evolve the team as the project changes: hire new roles, merge redundant roles, retire completed roles, or add temporary specialists. Each role may also keep a short name alongside its title, such as:

```text
[Role: Product Designer | Name: Iris]
```

Role names are optional and file-backed. `company/team-roster.md` is the canonical source for role title, role name, status, scope, and header format. If a role has no name in the roster, the agent should use only `[Role: <Role Title>]` and must not invent a name from chat context.

Response Preflight is the guardrail for this. Before every user-facing reply, the agent should ask: is Company Mode active, or is this reply about Company Mode / workflow R&D itself? If yes, the first line must be the roster-backed role header. If the header is missing, rewrite the first line before sending. This applies even to short, meta, emotional, status, bug-fix, side-quest, completion, and workflow-feedback replies. It does not apply to ordinary non-Company JARVIS chats.

Roles can also use Selective Innovation Mode. This is deeper than the normal out-of-box pass. It can be forced by the user or self-invoked by a role when a task deserves serious ideation. The role must state why it invoked the mode, compare meaningfully different options, critique them, and choose the best practical path.

Company Mode also supports a feedback loop for improving the workflow itself. When a project exposes reusable friction, a behavior defect, a missing rule, or a useful emergent pattern, the team can file a compact feedback candidate. A JARVIS R&D / maintainer team can then triage it as `reject`, `document-only`, `patch-skill`, `update-template`, `add-eval-scenario`, or `public-release`. Feedback candidates are not rules until promoted.

For coding projects, the workflow also supports:

- role/task branches
- role-authored commits
- PR handoffs
- version changes after reliable milestones

If the remote already exists, verification passed, and the current branch is a role/task branch, agents may push the branch and open/update a PR without asking first. If the user provides a GitHub repo URL for a new coding project, that is authorization to configure the remote and push a clean README-backed baseline after verification unless the user explicitly says local-only or there is a concrete sensitive-data/protected-branch blocker. After internal acceptance, the reviewer role should merge the role/task branch and push `main` when project policy allows. They should still ask before protected/default branch changes when policy is unknown, publishing releases/tags/packages, changing remotes/settings, force-pushing, deleting branches, or pushing anything that may contain private data.

For normal autonomous Company Mode projects, PRs are internal review artifacts. If a role opens a PR, the reviewer role should review it, request fixes if needed, then merge it after internal acceptance. Do not leave a draft PR waiting for the user unless there is a real product, release, secret, cost, or strategic decision.

Before a GitHub repo is treated as shipped or handoff-ready, it needs a `README.md`. For coding projects, README should explain what the project is, current status, setup/run/build/test instructions, known limitations, and where Company Mode state lives if relevant.

For user-facing work, the company should use available tools for internal QA and internal role review before escalating to the user. Use Computer Use, browser testing, screenshots, renderers, test scripts, package launch commands, or file inspection where relevant. User review is not a routine milestone gate; it is for explicitly requested review or unavoidable owner-level judgment after internal QA.

Project-scoped dev/test dependencies and official stack plugins are normal autonomous work when they are needed for the accepted stack or QA plan. Examples include Vitest, Playwright test packages and browser assets, Tauri dialog/plugin additions, local lint/build tools, and official framework plugins. Ask only for sudo/global installs, credentials, paid services, telemetry/cloud runtime behavior, destructive changes, unusual system-level impact, or strategic stack changes.

Reports should preserve role boundaries. A single-role task reports as that role. Cross-functional implementation/QA/product summaries should report as Chief of Staff after reading the relevant work orders and role memories. If several consecutive tasks only add QA or infrastructure, Founder or Chief of Staff should run a product-judgment check before creating another verification task.

For serious projects, use confidence lanes proportionally:

- `verified`
- `working-assumption`
- `speculative`
- `needs-audit`
- `rejected`

Consequential internal results should trigger adversarial review or an explicit decision not to review. The review should try to break the result before it becomes stable project truth. After meaningful discoveries, Chief of Staff should ask whether the bottleneck changed and re-rank the queue if needed.

### Creative Preproduction And Taste Gate

For craft-critical user-facing artifacts, Company Mode should not build first and judge later. Founder classifies the work as `utility-only`, `polished product`, `craft-critical`, or `signature product`. Craft-critical and signature work should activate Creative Director / Art Director, Product Designer / UX, UI Engineer, and Design QA responsibilities before major implementation.

Before implementation, the team should gather best-in-class references and anti-references, write an art direction brief, compare divergent concepts, and choose a direction internally. Design QA should reject screenshots that look generic, template-like, card-heavy without product reason, decorative-gradient-driven, default component-library shaped, or disconnected from the product metaphor.

If the user rejects visual quality as generic, ugly, AI-looking, template-like, or not best-in-field, the team should not simply tweak CSS or ask for taste. It should re-enter Creative Preproduction, strengthen the art direction, generate divergent concepts, and run screenshot-based Design QA again.

Completion reports should use explicit next-action language:

- `Next task:` for unblocked continuation
- `Blocked:` for concrete blockers
- `Decision needed:` for consequential user choices
- `User review requested:` only when the user explicitly asked to review or progress genuinely depends on owner judgment

If a role identifies the next necessary task, it should create, assign, or start that work order before ending the turn. Do not finish with vague handoffs such as "Founder should define..." or "Product Designer should consider..." unless the report also creates the actual work order or marks a concrete blocker/decision.

Example commit author:

```bash
git commit --author="JARVIS Frontend Engineer <your-verified-email@example.com>" -m "Polish task filtering UI"
```

## Folder Structure

```text
.
├── AGENTS.md
├── codex-skill/
│   ├── jarvis/
│   │   └── SKILL.md
│   └── jarvis-company-mode/
│       ├── SKILL.md
│       └── references/
│           ├── adoption-takeover.md
│           ├── adaptive-operating-patterns.md
│           ├── continuation.md
│           ├── creative-preproduction.md
│           ├── github-release-versioning.md
│           ├── greenfield.md
│           ├── innovation-feedback.md
│           ├── quality-qa-and-critique.md
│           └── roles-and-roster.md
├── handoffs/
│   └── README.md
├── logs/
│   └── decisions.md
├── memory/
│   ├── personal/
│   │   └── preferences.md
│   └── projects/
│       ├── index.md
│       └── example-project.md
├── sessions/
│   └── README.md
├── system/
│   ├── failure-patterns.md
│   ├── learning-log.md
│   ├── proposals/
│   ├── upgrade-roadmap.md
│   └── vault-map.md
└── templates/
    ├── company-mode/
    │   ├── adoption-audit.md
    │   ├── adversarial-review.md
    │   ├── current-state.md
    │   ├── evidence-ledger.md
    │   ├── feedback-report.md
    │   ├── integration-log.md
    │   ├── project-charter.md
    │   ├── role-charter.md
    │   ├── role-memory.md
    │   ├── strategy-map.md
    │   ├── task-board.md
    │   ├── team-roster.md
    │   └── work-order.md
    ├── decision-entry.md
    ├── handoff.md
    ├── project-memory.md
    └── session-note.md
```

## Quick Start

1. Copy this repository to a local folder:

   ```bash
   git clone https://github.com/<you>/jarvis-light.git ~/JARVIS
   cd ~/JARVIS
   ```

2. Install the base JARVIS skill:

   ```bash
   mkdir -p ~/.codex/skills/jarvis
   cp codex-skill/jarvis/SKILL.md ~/.codex/skills/jarvis/SKILL.md
   ```

3. Optional: install Company Mode:

   ```bash
   rm -rf ~/.codex/skills/jarvis-company-mode
   mkdir -p ~/.codex/skills
   cp -R codex-skill/jarvis-company-mode ~/.codex/skills/jarvis-company-mode
   ```

4. Start Codex from the vault folder.

5. For normal continuity work:

   ```text
   Jarvis, use JARVIS. Read the relevant project memory first.
   ```

6. For Company Mode examples, use the copy-paste starts near the top of this README.

## Operating Loop

For meaningful work, the agent should:

1. understand the request,
2. identify the project/domain,
3. read the relevant memory,
4. execute the task,
5. verify the result,
6. update the smallest durable note,
7. create a handoff only when continuation would otherwise be lossy.

In Company Mode:

1. Chief of Staff reads current state and task board.
2. It picks the next unblocked task.
3. The assigned role executes.
4. The role runs verification and an out-of-box pass.
5. The company updates task board, role memory, and integration log.
6. Work continues through internal milestone acceptance until a real blocker, escalation decision, public release/final stop gate, or deliberate pause.

## End-of-Task Memory Check

Before finishing meaningful work:

- Did project state change?
- Was a durable decision made?
- Did a stable preference appear?
- Is there unfinished work or a blocker?
- Is a fresh-chat handoff needed?
- Was a generated artifact verified?
- Did this reveal a reusable lesson or failure pattern?

If not, do not write memory just to write memory.

## Suggested First Setup

1. Edit `memory/personal/preferences.md`.
2. Edit `memory/projects/index.md`.
3. Create one project note from `templates/project-memory.md`.
4. Keep `AGENTS.md` as the root operating rule file.
5. Install only the skills you actually want to use.

## Publishing Your Own Fork

Do not publish your private working vault directly unless you have reviewed it for secrets and personal information.

Recommended pattern:

- private live vault for real memory
- public sanitized template repo for reusable workflow
- copy improvements from private to public only after removing personal context

## License

No license is included in this template by default. Add the license you want before publishing for broad reuse.
