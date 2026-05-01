# Changelog

## 0.0.54 - 2026-05-01

- Added a Closeout Resume Sweep for compaction, fresh-chat continuation, interruption, and restart recovery.
- Continuation now checks whether the previous task was implemented but not fully closed before starting new work.
- Task lifecycle and task cards now route interrupted closeouts back through state repair instead of treating public commits as enough.

## 0.0.53 - 2026-05-01

- Added a Sunset Clause for meaningful R&D loop workflow features.
- Idea cards and work orders can now declare a review trigger and keep/simplify/merge/retire/extend-trial outcomes.
- Clarified that sunset review creates a decision point, not permission for silent rule removal.

## 0.0.52 - 2026-05-01

- Added a Friction Inbox template for lightweight workflow-friction capture.
- Updated the R&D Idea Loop so future ideas can be grounded in captured friction before becoming rules or work orders.
- Added a Friction Inbox task card for tiny evidence capture and triage.

## 0.0.51 - 2026-05-01

- Added a Subtraction Gate to the R&D Idea Loop.
- Accepted ideas now state what they simplify, remove, replace, or make less necessary.
- Updated idea-card templates and task cards so added complexity must be explicitly justified.

## 0.0.50 - 2026-05-01

- Added `references/rd-idea-loop.md` for continuous improvement, product R&D, workflow R&D, and idea-by-idea loops.
- Added `templates/company-mode/idea-card.md` to capture proposed ideas, team discussion, decisions, task conversion, verification, and dogfood evidence.
- Routed R&D idea loops from the skill, Reference Router, Continuation, and Task Cards.

## 0.0.49 - 2026-05-01

- Added `references/task-lifecycle.md` with Task Lifecycle v1.
- Added lifecycle states, risk lanes, board-status mapping, and done-evidence rules.
- Updated work-order and task-board templates with lifecycle fields.
- Routed lifecycle checks from the skill, Reference Router, Continuation, and Task Cards.

## 0.0.48 - 2026-05-01

- Added `references/task-cards.md` with compact execution checklists for common task types.
- Routed task cards from the skill entry point and Reference Router.
- Updated README reference guidance so agents can reduce cognitive load without loading the whole workflow stack.

## 0.0.47 - 2026-05-01

- Standardized Specialist Mode on functional role headers.
- Removed persistent role/persona names from active role guidance and templates.
- Updated examples so agents use `[Role: <Role Title>]` instead of `[Name: ...]` headers.

## 0.0.46 - 2026-05-01

- Added explicit JARVIS Core / Light Mode guidance for small work.
- Added Minimal Specialist Layer guidance for small-but-real projects and focused adoptions.
- Clarified that Specialist Mode should scale to the project instead of always creating full role/memory/integration machinery.
- Corrected the README visible version line.

## 0.0.45 - 2026-05-01

- Added the Vague Improvement Loop Gate as a focused Stop-the-Line extension.
- Repeated vague dissatisfaction such as "improve more," "still not good," or repeated rejection of the same direction now triggers diagnosis instead of another incremental patch.
- Added an anti-ceremony guard: skip the gate when one clear local fix, clarification, or existing gate can resolve the issue.

## 0.0.44 - 2026-05-01

- Clarified Specialist Mode team semantics: the team is the current Codex agent sequentially inhabiting file-backed roles, not automatic runtime subagents.
- Added guidance for "discuss with your team" prompts to use same-chat role hats by default.
- Runtime subagents are now explicitly temporary helpers for explicit/valuable parallel work, and their IDs should not become canonical team memory.

## 0.0.43 - 2026-04-30

- Tightened Closeout Integrity Check so state-aware completion options are explicitly checked before meaningful Specialist Mode reports.
- Missing useful completion options now count as a closeout mismatch, not a harmless formatting omission.
- This reinforces the existing `0.0.35` Completion Options Menu behavior by making it part of final report integrity.

## 0.0.42 - 2026-04-30

- Added Memory Router and Lifecycle Lanes for JARVIS OS memory discipline.
- Agents now have a focused reference for routing durable facts to the right canonical note, marking active/stable/candidate/archived/superseded memory when freshness matters, and splitting long project notes before retrieval degrades.
- Updated memory templates with lifecycle, routing, freshness, and split-trigger fields while keeping markdown as the canonical memory layer.

## 0.0.41 - 2026-04-30

- Added Capability Surface Declaration for tool-dependent Specialist Mode work.
- Teams now have a compact way to declare available capabilities, required capabilities, missing/risky tools, approval lane, and verification path before execution or closeout.
- Updated templates so work orders and current state can record capability surfaces without turning every task into a runtime inventory.

## 0.0.40 - 2026-04-30

- Added the Reference Router for JARVIS OS.
- Agents now have a compact trigger-to-reference map for choosing the smallest useful reference bundle before deeper Specialist Mode work.
- Clarified that routing should happen before loading large workflow stacks, with Stop-the-Line or operating-mode changes causing re-routing when needed.

## 0.0.39 - 2026-04-30

- Added the Visual Concept Pipeline for craft-critical UI and visual product work.
- Teams can now generate or choose a concrete visual target, freeze it as the spec, implement against it, and compare rendered screenshots back to the concept.
- Clarified that generated UI concepts are design inputs, not product truth; real data, accessibility, responsiveness, and domain correctness can justify intentional deviations.

## 0.0.38 - 2026-04-30

- Added Stop-the-Line Review for Specialist Mode.
- Teams should interrupt normal execution when continuing would produce wrong, generic, misleading, stale, or low-quality work.
- Stop-the-Line can fix now, create a corrective work order, switch operating mode, run claim review, or escalate only when a real boundary requires it.

## 0.0.37 - 2026-04-30

- Added Lightweight Public Artifact Framing for small public-facing artifacts.
- Agents should now frame audience, decision/job, tone/trust, avoid-list, missing material facts, and public-data boundaries before building personal sites, small public pages, public emails, bios, one-pagers, READMEs, and similar artifacts.
- Named external references should be read or explicitly marked inaccessible instead of silently skipped.
- Deployed artifacts should distinguish local latest files from production and report local-only changes with a clear Deploy/Pause path.

## 0.0.36 - 2026-04-30

- Added the Closeout Integrity Check for Specialist Mode completion reports.
- Meaningful completions should now verify that current state, task board, work order status, docs/version surfaces, git/GitHub claims, artifacts, blockers, and completion options agree before reporting.
- Clarified that mismatches should be fixed before reporting when safe, or surfaced as `Blocked:` / recovery work when not immediately fixable.

## 0.0.35 - 2026-04-29

- Added state-aware completion options for Specialist Mode reports.
- Meaningful task completions can now end with a compact `Options:` menu such as Continue, Status, Inspect, Resolve blocker, Review, Release, Pause, or Handoff, depending on live project state.
- Clarified that options should not be a fixed footer and must not contradict autonomy, release, credential, cost, destructive-action, protected-branch, or private-data boundaries.

## 0.0.34 - 2026-04-29

- Added the Off-Roadmap Request Proposal Gate.
- Substantial requests outside the current team roadmap should first receive a compact internal intake and proposal.
- After user approval, the team executes the approved scope, verifies, updates state, and pushes when safe.

## 0.0.33 - 2026-04-29

- Added progressive Founder discovery for new project initialization.
- Founder should start with a small, direct first question batch instead of a long survey.
- Follow-up questions are allowed when answers are insufficient, but long questionnaires should be split into rounds and reserved for genuinely complex or high-risk projects.

## 0.0.32 - 2026-04-29

- Merged the public `jarvis` and `jarvis-company-mode` skill packages into one `jarvis-os` package.
- Kept the skill set split internally through progressive `codex-skill/jarvis-os/references/` files.
- Removed the separate public `codex-skill/jarvis` and `codex-skill/jarvis-company-mode` folders.
- Updated README install and start prompts so users install one skill and let JARVIS OS choose Core or Specialist Mode from the task shape.

## 0.0.31 - 2026-04-29

- Introduced JARVIS Specialist Mode as the future-facing name for the role-based project workflow.
- Preserved Company Mode as a compatibility alias for existing prompts, folders, chats, and the legacy `jarvis-company-mode` package path at that version.
- Shifted public README framing toward JARVIS OS while noting that the repository path may keep the older JARVIS Light name during migration.
- Updated the public README, AGENTS instructions, JARVIS skill, Specialist Mode skill, and key references so both old and new invocation phrases remain clear.

## 0.0.30 - 2026-04-29

- Added Company Mode v0.8.5 GPT-5.5-aligned outcome contracts to the JARVIS and Company Mode skills.
- Added retrieval budgets and stop rules so agents read enough context to act correctly without over-reading the vault or project state.
- Preserved Company Mode compatibility, role headers, QA, escalation, confidence lanes, and public/private safety rules.

## 0.0.29 - 2026-04-29

- Added Company Mode v0.8.4 Excellence Calibration Gate.
- Excellence-critical work should define the reference class, top-tier bar, benchmarks/references, missing capabilities, and rejection tests before major execution or revision.
- Clarified that calibration is domain-general: apps, research, data, writing, architecture, public docs, strategy, and other trust/quality-sensitive deliverables can all need it.
- Updated installed/public adaptive operating, quality, creative preproduction, template, README, AGENTS, and version surfaces.

## 0.0.28 - 2026-04-29

- Added Company Mode v0.8.3 Claim Review Loop.
- Consequential claims that downstream work depends on should be stated, confidence-labeled, attacked independently, and marked as `promoted`, `revised`, `rejected`, or `split`.
- Updated installed/public adaptive operating references, skill index, README, AGENTS, and version surfaces.

## 0.0.27 - 2026-04-29

- Added Company Mode v0.8.2 Workflow Refresh Playbook.
- Added `references/workflow-refresh.md` to installed/public Company Mode skills.
- Updated the public refresh prompt to point older active chats at the dedicated refresh reference instead of embedding detailed rules.

## 0.0.26 - 2026-04-29

- Replaced the oversized README workflow refresh prompt with a compact, stable prompt.
- Clarified that installed JARVIS skills are the source of truth for detailed refresh behavior.
- Added a short refresh reconciliation checklist instead of copying the full evolving rule set into GitHub README.

## 0.0.25 - 2026-04-29

- Added Company Mode v0.8.1 Operating Mode Declaration.
- `company/current-state.md` now includes an `Operating mode` field.
- Chief of Staff should use operating mode during `continue` to route work differently for discovery, build, audit, polish, release, dogfood, research attack, recovery, and maintenance.
- Updated greenfield/adoption guidance so setup chooses the initial operating mode.
- Updated Company Mode continuation and adaptive operating references with mode-aware routing.

## 0.0.24 - 2026-04-29

- Added Company Mode v0.8 Adaptive Project-Shape Inference.
- Founder now infers project shape before workflow design: what makes success hard, what evidence matters, what roles/artifacts are needed, and which verification gates are justified.
- Added confidence lanes for consequential claims/results: `verified`, `working-assumption`, `speculative`, `needs-audit`, and `rejected`.
- Added adversarial review trigger for proof claims, major design directions, method choices, architecture decisions, data results, release candidates, and public claims.
- Added queue re-ranking guidance so Chief of Staff updates the next work when discoveries change the bottleneck.
- Added optional templates for `strategy-map.md`, `evidence-ledger.md`, and `adversarial-review.md`.

## 0.0.23 - 2026-04-29

- Added Company Mode v0.7.1 Response Preflight / Header Guard.
- Agents now have an explicit final check before every user-facing reply: if Company Mode is active, or the topic is Company Mode / workflow R&D itself, the first line must be the roster-backed role header.
- Added fallback routing for ambiguous headers: Chief of Staff for routing/status, Workflow Architect for workflow diagnosis/design, and Skill Engineer for skill/rule/template changes.
- Clarified that the guard applies to short, meta, emotional, status, bug-fix, side-quest, completion, and workflow-feedback replies, but not ordinary non-Company JARVIS chats.

## 0.0.22 - 2026-04-29

- Added Company Mode v0.7 Creative Preproduction and Taste Gate.
- Craft-critical user-facing work now requires craft criticality classification, design leadership, reference intelligence, art direction, divergent concepts, and screenshot-based Design QA before major implementation.
- Added generic UI kill switch and rejection protocol for work rejected as generic, ugly, AI-looking, template-like, or not best-in-field.
- Updated Company Mode templates with craft criticality, creative direction, and Creative Preproduction quality fields.
- Added `references/creative-preproduction.md` to installed and public Company Mode skills.

## 0.0.21 - 2026-04-29

- Added Company Mode v0.6.3 dependency/tooling autonomy clarification.
- Project-scoped free dev/test dependencies, official stack plugins, and normal test assets can proceed without user approval when required by the accepted stack or QA plan.
- Approval for a dependency/tooling class now carries forward through the current task chain; agents should not ask again for exact package-manager commands after approval.
- Added role-accurate reporting: single-role work reports as the executing role; cross-functional summaries report as Chief of Staff.
- Added product-judgment checks to avoid a QA/test treadmill after several consecutive infrastructure or verification tasks.

## 0.0.20 - 2026-04-28

- Added Company Mode v0.6.2 internal acceptance model.
- Internal role review is now the default; agents should not ask users for routine comments, review, or approval when the team can decide.
- Normal milestones can be internally accepted after role review, QA, cleanup, and critique, then the company continues to the next useful task.
- User review is reserved for explicitly requested review, final stop/closure, public release, credentials/cost/destructive actions, strategic direction changes, or unavoidable owner-level judgment.
- Updated Company Mode templates to use `internally-accepted` and `waiting-user-decision` instead of routine `ready-for-user-review` states.

## 0.0.19 - 2026-04-28

- Added Company Mode v0.6.1 approval/autonomy tightening.
- Approval after a listed set of safe actions now carries through the whole set instead of requiring repeated approval.
- Agent-created QA/demo data can be cleaned without extra approval when isolated from real user data.
- Standard free project toolchains/dependencies can be installed when required by the chosen stack, unless they need sudo, credentials, paid services, or destructive system changes.
- A provided GitHub repo URL now authorizes a verified README-backed baseline push when no sensitive-data or protected-branch blocker exists.
- Clarified that `Ready for review` comes after safe cleanup, packaging, README/status hygiene, internal QA, and eligible baseline push.

## 0.0.18 - 2026-04-28

- Modularized Company Mode v0.6 skill structure.
- Shrank the executable `SKILL.md` into a concise index/non-negotiable layer.
- Added focused reference files for greenfield setup, adoption/takeover, continuation, roles/roster, quality/QA, GitHub/release/versioning, and innovation/feedback.
- Preserved installed/public structure parity while keeping public wording generic.

## 0.0.17 - 2026-04-28

- Added Company Mode v0.5.5 Adoption Takeover Authority.
- After audit and baseline preservation, adopted projects become owned operating projects; existing code is evidence, not authority.
- Added Next-Task Ownership: roles must create, assign, or start necessary follow-up work instead of ending with vague "should" handoffs.
- Clarified that Chief of Staff routes work and Product/Founder roles define product-quality milestones when gaps are visible.

## 0.0.16 - 2026-04-28

- Added Company Mode v0.5.4 autonomous shipping and tool-aware QA policy.
- User-facing artifacts must be internally tested with available tools before asking for user review.
- PRs are internal review artifacts by default; after internal acceptance, merge/push instead of waiting for user approval.
- Added repo readiness gate: GitHub handoff repos need a `README.md` with setup/run/build/test/status information.

## 0.0.15 - 2026-04-28

- Added Company Mode v0.5.3 Founder-led discovery clarification.
- Founder should ask all material project questions before deciding roles, company depth, and first work orders.
- Examples no longer ask the user to pre-select roles for data, research, website, or writing projects.
- Updated workflow refresh prompt with current v0.5.x roster, feedback, GitHub autonomy, and explicit next-action rules.

## 0.0.14 - 2026-04-28

- Added Company Mode v0.5.2 GitHub autonomy clarification.
- Verified role/task branch pushes and PR creation can proceed without asking when the remote exists and no sensitive/release risk is present.
- Added explicit next-action language: `Next task`, `Blocked`, `Decision needed`, or `Ready for review`.
- Clarified that `next likely task` should only appear when there is genuine uncertainty.

## 0.0.13 - 2026-04-28

- Added Company Mode v0.5.1 canonical role identity registry.
- Added `company/team-roster.md` template as the source of truth for role title, optional role name, status, scope, and canonical header.
- Added rule that agents must not invent role names in user-facing headers.
- Updated Company Mode templates so role charters, role memories, and current state point back to the team roster.

## 0.0.12 - 2026-04-28

- Added Company Mode v0.5 JARVIS R&D Feedback Loop.
- Project teams can record feedback candidates for workflow friction, behavior defects, missing rules, quality gaps, emergent patterns, and eval scenarios.
- Added feedback triage outcomes: `reject`, `document-only`, `patch-skill`, `update-template`, `add-eval-scenario`, and `public-release`.
- Added `feedback-report.md` template and workflow feedback fields to Company Mode templates.
- Updated README with a copy-paste prompt for reporting workflow feedback.

## 0.0.11 - 2026-04-28

- Added Company Mode v0.4 Selective Innovation Mode.
- Users can force deep brainstorming for a role/task.
- Roles can self-invoke Innovation Mode when uncertainty, quality risk, strategic importance, creative upside, or high reversal cost justifies deeper ideation.
- Added work-order fields to record whether Innovation Mode was forced, invoked, or skipped.

## 0.0.10 - 2026-04-28

- Added README workflow refresh prompt for older active chats after JARVIS / Company Mode updates.
- Clarified when to refresh an existing chat versus create a fresh-chat handoff.

## 0.0.9 - 2026-04-28

- Added Company Mode no-passive-acknowledgement rule.
- Short replies such as `ok`, `yes`, `go`, `next`, and `?` now route to continuation or exact blocker handling when an active unblocked task exists.
- Clarified that users should not need to micromanage every step with a perfectly formed `continue` command.

## 0.0.8 - 2026-04-28

- Added Company Mode v0.3 Adaptive Team Mode.
- Founder and Chief of Staff can add, merge, retire, or rename roles as project needs evolve.
- Added assertive role autonomy: roles should challenge weak assumptions, critique orders, and propose better paths within scope.
- Added optional role names alongside role titles for clearer persistent team identity.
- Moved expanded copy-paste usage scenarios near the top of README.

## 0.0.7 - 2026-04-28

- Added Company Mode version visibility rule: if a role changes an internal/project version, the project README/changelog/version surface must be updated in the same task or commit.
- Added `VERSION` as the public template's visible version file.
- Updated README with the current public version.

## 0.0.6 - 2026-04-28

- Added Company Mode workspace defaults.
- Real projects should use the user's normal active projects folder.
- Vault-local `projects/` should be reserved for JARVIS workflow tests, demos, or temporary trials.

## 0.0.5 - 2026-04-28

- Added Company Mode user-facing role identity.
- Added interruption and side-quest handling for active Company Mode task flows.

## 0.0.4 - 2026-04-28

- Added Company Mode public template, Adoption Mode templates, and stronger README guidance.

## 0.0.3 - 2026-04-24

- Added governed self-improvement loop.

## 0.0.2 - 2026-04-24

- Added artifact hygiene and large-project memory scaling guidance.

## 0.0.1 - 2026-04-21

- Initial public JARVIS Light template.
