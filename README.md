# JARVIS OS

**A local-first operating system for Codex continuity.**

This public template was previously named JARVIS Light. The repository path may keep that name during the migration, but the workflow now uses JARVIS OS as the umbrella name.

Current version: `0.0.40`

Latest update: JARVIS OS now includes a Reference Router so agents choose the smallest relevant workflow references before deep Specialist Mode work.

JARVIS OS turns a folder of markdown files into durable assistant memory.
It helps Codex work across long chats, fresh chats, projects, research, codebases, and handoffs without pretending the chat history itself is the source of truth.

It is inspired by the same continuity problem that Chronicle-style memory tries to solve, but it is intentionally different:

- no background screen capture
- no automatic background screenshots
- no always-on memory agent
- no hidden database requirement
- no transcript dumping
- no expensive automatic capture loop

JARVIS OS is **not a Chronicle replacement**.
It is the lightweight/manual mode: local markdown, explicit retrieval, compact memory, and agent discipline.

## The One-Sentence Version

JARVIS OS makes Codex behave less like a fresh chat and more like an organized teammate that can read the project state, do the work, and leave the next session in a better position.

## Copy-Paste Starts

Use these prompts as starting points. Replace the project details and paths.

### 1. Normal Continuity Work

```text
Jarvis, use JARVIS OS.

Read the relevant project memory first, then help me with:
...
```

### 2. Fresh-Chat Handoff

```text
Jarvis, use JARVIS OS.

This chat is getting long. Create a fresh-chat handoff for this project.
Include current objective, completed work, blockers, exact next steps,
and files the next chat should read first.
```

### 3. Refresh An Older Active Chat

Use this when JARVIS or Specialist Mode / Company Mode has been updated while an older project chat is still active.

```text
Jarvis, workflow refresh.

Use JARVIS OS Specialist Mode.

Read the latest installed JARVIS OS skill:
- ~/.codex/skills/jarvis-os/SKILL.md
- ~/.codex/skills/jarvis-os/references/workflow-refresh.md if it exists

Then read the live project state:
- company/team-roster.md if it exists
- company/current-state.md
- company/task-board.md
- company/integration-log.md if it exists

If this project is missing newer Specialist Mode / Company Mode fields,
create a small workflow refresh task and update the company state.

Continue from the next unblocked task using the latest workflow rules.
Do not ask me for routine review or approval unless escalation rules require it.
```

The installed skills are the source of truth. This prompt intentionally does not copy every rule into the README, because the detailed rules change over time.

A successful refresh should usually reconcile:

- roster-backed role headers
- `company/current-state.md` operating mode
- no-passive-acknowledgement continuation
- internal review and autonomous next-task routing
- README, changelog, version, QA, GitHub, and release-safety surfaces

For long or messy threads, use a fresh-chat handoff instead of trying to keep the old chat alive.

```text
Jarvis, create a fresh-chat handoff for this project using the latest JARVIS workflow.
```

### 4. New App Or Product

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a new project in Specialist Mode.
Project idea:
...

Your first role is Founder.
Ask all material questions needed to understand the project.
Then choose the right workspace, decide the team, and create the first high-leverage work orders.
```

### 5. Existing Repo Adoption

```text
Jarvis, use JARVIS OS Specialist Mode.

Adopt this existing project into Specialist Mode:
/path/to/project

Your first role is Founder / Organizational Auditor.
Audit first, then create the company layer around the existing structure.
Do not reorganize or rewrite anything before the audit.
```

### 6. Research Project

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a research team for:
...

Your first role is Principal Investigator / Founder.
Ask all material questions needed to understand the research question,
data, method, risks, and success criteria.
Then decide the research team and create the first work orders.
```

### 7. Data / Quant Project

```text
Jarvis, use JARVIS OS Specialist Mode.

Start a data/quant project for:
...

Your first role is Founder.
Ask all material questions needed to understand the data, objective,
constraints, validation needs, and delivery target.
Then decide the required team and first work orders.
Do not let anyone call results ready without verification and artifact hygiene.
```

### 8. Website Or Launch Page

```text
Jarvis, use JARVIS OS Specialist Mode.

Build a serious website for:
...

Founder should ask all material questions needed to understand the audience,
offer, brand, content, visual direction, constraints, and success criteria.
Then decide the team and first work orders.
The team should critique weak design or messaging without waiting for me to say "make it better."
```

### 9. Writing / Thesis / Book

```text
Jarvis, use JARVIS OS Specialist Mode.

Create an editorial team for:
...

Founder should ask all material questions needed to understand audience,
thesis, scope, sources, tone, structure, and delivery format.
Then decide the editorial team and first work orders.
Keep citations, claims, and next writing tasks durable in markdown.
```

### 10. Bug Or Side Quest During Specialist Mode

```text
Jarvis, side quest for the current Specialist Mode project:
...

Classify this as clarification, defect, side quest, or scope change.
Preserve the interrupted task and tell me whether the main flow resumes afterward.
```

### 11. Keep Going Without Micromanaging

```text
ok
```

In an active Specialist Mode / Company Mode project, short acknowledgements such as `ok`, `yes`, `go`, `next`, or `?` should not produce passive replies. They should continue the next unblocked task or explain the exact blocker.

### 12. Force Innovation Mode

```text
Jarvis, use JARVIS OS Specialist Mode.

For the next task, force Innovation Mode.
Generate meaningfully different options.
Critique them for value, risk, cost, originality, and fit.
Then choose the best practical path.
Do not implement a risky or irreversible idea without creating a proposal or asking first.
```

Roles may also self-invoke Innovation Mode when the work is ambiguous, strategically important, creatively underdeveloped, expensive to reverse, or likely to become generic without deeper thinking.

### 13. Report Workflow Feedback

Use this when a real project exposes a reusable JARVIS / Specialist Mode improvement.

```text
Jarvis, use JARVIS OS Specialist Mode.

Feedback for the workflow:
...

Record this as a feedback candidate.
Classify whether it is project-local or should be routed to JARVIS R&D.
Do not turn it into a standing rule until it is triaged.
```

### 14. Release / Version Update

```text
Jarvis, use JARVIS OS Specialist Mode.

Run release readiness for this project.
Check verification, version metadata, README/changelog visibility,
git status, and whether a PR or tag is needed.
Do not publish a release or stop the company without my approval.
```

## What Is Inside

JARVIS OS has two layers.

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

### 2. JARVIS Specialist Mode

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
- agents saying "done" without enough durable trace

JARVIS OS changes the center of gravity:

```text
Chat = temporary working surface
Markdown vault = durable continuity layer
```

When the chat gets too long, you create a handoff and start fresh.

## What It Is

JARVIS OS is:

- a local markdown vault
- a Codex skill
- a set of templates and operating rules
- a low-token continuity workflow
- readable, editable, inspectable, private by default
- useful for coding, research, writing, planning, and long-running projects

JARVIS OS is not:

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

## Specialist Mode

JARVIS Specialist Mode is optional. Use it when the project is big enough that specialist roles would help. Company Mode remains the compatibility alias.

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
- optional strategy/evidence/adversarial-review/claim-review artifacts when useful

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
5. Add the Specialist Mode / Company Mode layer around the existing project.

Adoption Mode should not rewrite or reorganize the project before it understands it.

After audit and baseline preservation, adoption should turn into takeover. The company becomes responsible for the project outcome; existing code is evidence, not authority. Roles may refactor, redesign, replace, merge, delete, reorganize, or rebuild parts of the project when justified by the charter, quality bar, verification, and task scope.

### Quality Bar

Specialist Mode should not stop at "it works."

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

### Reference Router

JARVIS OS uses a Reference Router before deeper Specialist Mode work. The router maps the task shape to the smallest useful reference bundle so agents do not need to paste, load, or remember the whole workflow stack.

Examples:

- older active chat refresh -> `workflow-refresh.md`
- `continue`, blockers, interruptions, completion options -> `continuation.md`
- new serious project -> `greenfield.md`
- existing project takeover -> `adoption-takeover.md`
- public artifacts -> `public-artifacts.md`
- craft-critical UI -> `creative-preproduction.md` and sometimes `visual-concept-pipeline.md`
- GitHub, release, version, changelog -> `github-release-versioning.md`
- consequential claims or research/proof work -> `adaptive-operating-patterns.md`

The rule is: route first, load only the selected references, execute, and re-route if Stop-the-Line Review or a changed bottleneck shows the initial route was wrong.

Founder and Chief of Staff can evolve the team as the project changes: hire new roles, merge redundant roles, retire completed roles, or add temporary specialists. Each role may also keep a short name alongside its title, such as:

```text
[Role: Product Designer | Name: Iris]
```

Role names are optional and file-backed. `company/team-roster.md` is the canonical source for role title, role name, status, scope, and header format. If a role has no name in the roster, the agent should use only `[Role: <Role Title>]` and must not invent a name from chat context.

Response Preflight is the guardrail for this. Before every user-facing reply, the agent should ask: is Specialist Mode / Company Mode active, or is this reply about Specialist Mode / Company Mode / workflow R&D itself? If yes, the first line must be the roster-backed role header. If the header is missing, rewrite the first line before sending. This applies even to short, meta, emotional, status, bug-fix, side-quest, completion, and workflow-feedback replies. It does not apply to ordinary non-Specialist JARVIS chats.

Roles can also use Selective Innovation Mode. This is deeper than the normal out-of-box pass. It can be forced by the user or self-invoked by a role when a task deserves serious ideation. The role must state why it invoked the mode, compare meaningfully different options, critique them, and choose the best practical path.

Specialist Mode also supports a feedback loop for improving the workflow itself. When a project exposes reusable friction, a behavior defect, a missing rule, or a useful emergent pattern, the team can file a compact feedback candidate. A JARVIS R&D / maintainer team can then triage it as `reject`, `document-only`, `patch-skill`, `update-template`, `add-eval-scenario`, or `public-release`. Feedback candidates are not rules until promoted.

For coding projects, the workflow also supports:

- role/task branches
- role-authored commits
- PR handoffs
- version changes after reliable milestones

If the remote already exists, verification passed, and the current branch is a role/task branch, agents may push the branch and open/update a PR without asking first. If the user provides a GitHub repo URL for a new coding project, that is authorization to configure the remote and push a clean README-backed baseline after verification unless the user explicitly says local-only or there is a concrete sensitive-data/protected-branch blocker. After internal acceptance, the reviewer role should merge the role/task branch and push `main` when project policy allows. They should still ask before protected/default branch changes when policy is unknown, publishing releases/tags/packages, changing remotes/settings, force-pushing, deleting branches, or pushing anything that may contain private data.

For normal autonomous Specialist Mode / Company Mode projects, PRs are internal review artifacts. If a role opens a PR, the reviewer role should review it, request fixes if needed, then merge it after internal acceptance. Do not leave a draft PR waiting for the user unless there is a real product, release, secret, cost, or strategic decision.

Before a GitHub repo is treated as shipped or handoff-ready, it needs a `README.md`. For coding projects, README should explain what the project is, current status, setup/run/build/test instructions, known limitations, and where Specialist Mode / Company Mode state lives if relevant.

For user-facing work, the company should use available tools for internal QA and internal role review before escalating to the user. Use Computer Use, browser testing, screenshots, renderers, test scripts, package launch commands, or file inspection where relevant. User review is not a routine milestone gate; it is for explicitly requested review or unavoidable owner-level judgment after internal QA.

Project-scoped dev/test dependencies and official stack plugins are normal autonomous work when they are needed for the accepted stack or QA plan. Examples include Vitest, Playwright test packages and browser assets, Tauri dialog/plugin additions, local lint/build tools, and official framework plugins. Ask only for sudo/global installs, credentials, paid services, telemetry/cloud runtime behavior, destructive changes, unusual system-level impact, or strategic stack changes.

Reports should preserve role boundaries. A single-role task reports as that role. Cross-functional implementation/QA/product summaries should report as Chief of Staff after reading the relevant work orders and role memories. If several consecutive tasks only add QA or infrastructure, Founder or Chief of Staff should run a product-judgment check before creating another verification task.

For serious projects, use confidence lanes proportionally:

- `verified`
- `working-assumption`
- `speculative`
- `needs-audit`
- `rejected`

Consequential internal results should trigger adversarial review or an explicit decision not to review. The review should try to break the result before it becomes stable project truth.

When downstream work depends on a consequential claim, use the Claim Review Loop:

1. State the claim.
2. Assign its confidence lane.
3. Attack it independently.
4. Record the strongest attack and surviving claim.
5. Mark the outcome as `promoted`, `revised`, `rejected`, or `split`.
6. Re-rank the queue from that outcome.

After meaningful discoveries, Chief of Staff should ask whether the bottleneck changed and re-rank the queue if needed.

### Excellence Calibration Gate

For excellence-critical work, Specialist Mode should define the quality target before execution. This is not only for UI. It can apply to apps, research notes, data outputs, decks, architecture, public docs, strategy, papers, demos, and any deliverable where quality, rigor, trust, or originality defines success.

Use Excellence Calibration when the team is about to set the quality ceiling for important work:

1. Reference class: what field or artifact type are we competing with?
2. Excellence bar: what would make this top-tier for that class?
3. Benchmarks/references: what strong examples, papers, products, artifacts, or standards calibrate us?
4. Missing capability: what would a real team hire or consult for this?
5. Rejection tests: what would make this generic, weak, misleading, unsafe, or not worth shipping?
6. Decision: proceed, add/activate a role, run reference research, reshape the work order, or lower scope honestly.

Skip the gate for tiny bug fixes, mechanical docs updates, routine QA, small refactors, and urgent recovery work where the target is already obvious.

### Stop-the-Line Review

Use Stop-the-Line Review when normal Specialist Mode execution would likely continue bad momentum. It is an internal interrupt, not a routine user-review request.

Common triggers:

- wrong audience, purpose, or project framing;
- functional but generic, weak, or off-purpose output;
- skipped evidence, named references, or source provenance;
- consequential claims, design directions, methods, architecture, or readiness assumptions treated as stable too early;
- README, status, version, deployment, or artifact reality conflicting with reported state;
- repeated superficial fixes after the same failure;
- missing role, capability, reference class, or tool for the work;
- an old queue optimizing the wrong thing after a discovery or failure.

Default outcomes are: fix now, create a corrective work order, switch operating mode, run claim review, or escalate only when a real boundary requires it.

### Creative Preproduction And Taste Gate

For craft-critical user-facing artifacts, Specialist Mode should not build first and judge later. Founder classifies the work as `utility-only`, `polished product`, `craft-critical`, or `signature product`. Craft-critical and signature work should activate Creative Director / Art Director, Product Designer / UX, UI Engineer, and Design QA responsibilities before major implementation.

Before implementation, the team should gather best-in-class references and anti-references, write an art direction brief, compare divergent concepts, and choose a direction internally. Design QA should reject screenshots that look generic, template-like, card-heavy without product reason, decorative-gradient-driven, default component-library shaped, or disconnected from the product metaphor.

If the user rejects visual quality as generic, ugly, AI-looking, template-like, or not best-in-field, the team should not simply tweak CSS or ask for taste. It should re-enter Creative Preproduction, strengthen the art direction, generate divergent concepts, and run screenshot-based Design QA again.

### Visual Concept Pipeline

For craft-critical UI or visual product work, JARVIS can create or choose a concrete visual target before implementation. This can be a generated UI concept, user-provided screenshot, hand sketch, reference app screenshot, existing style frame, or high-fidelity mockup.

The pipeline is:

1. define the audience, job, product truth, craft criticality, rejection tests, and required states;
2. create or gather one or more visual concepts;
3. freeze the selected concept as the implementation target;
4. implement from the target as a visual spec, not vague inspiration;
5. render the actual app/site/artifact and compare screenshots back to the concept;
6. record intentional deviations for real data, accessibility, responsiveness, domain correctness, privacy, or platform conventions;
7. trigger Stop-the-Line Review if the implementation drifts into generic UI or loses the concept's intent.

Generated concepts are design inputs, not product truth. Do not trust generated text, data, logos, maps, charts, personal facts, or domain claims without verification.

### Small Public-Facing Artifacts

Not every public artifact needs a full Specialist Mode team, but small public-facing work still needs framing before build. For personal pages, application sites, public READMEs, small landing pages, public emails, bios, one-pagers, and deployed static sites, JARVIS should identify:

- audience and decision/job;
- tone and trust signals;
- what would feel generic, misleading, cringe, or off-purpose;
- missing contact, call-to-action, privacy, consent, source, or deployment facts;
- named external references that must be read or explicitly marked inaccessible.

If the artifact is deployed, completion should distinguish local files from production. A local fix that has not been deployed should be reported as local-only with an explicit Deploy/Pause option.

Completion reports should use explicit next-action language:

- `Next task:` for unblocked continuation
- `Blocked:` for concrete blockers
- `Decision needed:` for consequential user choices
- `User review requested:` only when the user explicitly asked to review or progress genuinely depends on owner judgment

If a role identifies the next necessary task, it should create, assign, or start that work order before ending the turn. Do not finish with vague handoffs such as "Founder should define..." or "Product Designer should consider..." unless the report also creates the actual work order or marks a concrete blocker/decision.

Before meaningful Specialist Mode completion reports, run a Closeout Integrity Check so the report does not contradict durable state:

- `company/current-state.md` and `company/task-board.md` agree on active task, blocker, operating mode, and next task
- active work order status matches the report
- README, changelog, version, package, release, or app metadata agree when version changed
- git/GitHub branch, status, remote, commit, PR, tag, or release claims match tool results
- referenced artifacts exist, are labeled correctly, and were verified
- public artifact local files, live URL, deployment target, and privacy boundary agree when deployment is involved
- blockers and options do not contradict autonomy rules or the actual next unblocked work

After meaningful Specialist Mode task completion, reports should also offer a small state-aware `Options:` menu when useful. The menu should be based on live state, not a fixed template:

- `Continue:` start the exact next unblocked task
- `Status:` show the current mode, active task, blockers, version, or repo state
- `Inspect:` summarize changed files, artifacts, screenshots, commits, or notes
- `Resolve blocker:` name the exact missing access, file, credential, decision, or candidate
- `Pause:` preserve the current state without starting new work

Use only the options that actually fit. Do not offer routine review when internal review is enough, and do not hide real release, cost, credential, protected-branch, destructive-action, or private-data boundaries behind a normal option.

Example commit author:

```bash
git commit --author="JARVIS Frontend Engineer <your-verified-email@example.com>" -m "Polish task filtering UI"
```

## Folder Structure

```text
.
├── AGENTS.md
├── codex-skill/
│   └── jarvis-os/
│       ├── agents/
│       │   └── openai.yaml
│       ├── SKILL.md
│       └── references/
│           ├── adoption-takeover.md
│           ├── adaptive-operating-patterns.md
│           ├── continuation.md
│           ├── creative-preproduction.md
│           ├── github-release-versioning.md
│           ├── greenfield.md
│           ├── innovation-feedback.md
│           ├── public-artifacts.md
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

2. Install the single JARVIS OS skill:

   ```bash
   rm -rf ~/.codex/skills/jarvis ~/.codex/skills/jarvis-company-mode ~/.codex/skills/jarvis-os
   mkdir -p ~/.codex/skills
   cp -R codex-skill/jarvis-os ~/.codex/skills/jarvis-os
   ```

3. Start Codex from the vault folder.

4. For normal continuity work:

   ```text
   Jarvis, use JARVIS OS. Read the relevant project memory first.
   ```

5. For Specialist Mode examples, use the copy-paste starts near the top of this README.

## Operating Loop

For meaningful work, the agent should:

1. understand the request,
2. identify the project/domain,
3. read the relevant memory,
4. execute the task,
5. verify the result,
6. update the smallest durable note,
7. create a handoff only when continuation would otherwise be lossy.

In Specialist Mode / Company Mode:

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
5. Install the single `jarvis-os` skill from `codex-skill/jarvis-os`.

## Publishing Your Own Fork

Do not publish your private working vault directly unless you have reviewed it for secrets and personal information.

Recommended pattern:

- private live vault for real memory
- public sanitized template repo for reusable workflow
- copy improvements from private to public only after removing personal context

## License

No license is included in this template by default. Add the license you want before publishing for broad reuse.
