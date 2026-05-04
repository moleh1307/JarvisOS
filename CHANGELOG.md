# Changelog

## 0.0.104 - 2026-05-04

- Added a Specialist Mode Target Gate so bare requests like `go for Specialist Mode` ask for the project/folder instead of defaulting to JARVIS R&D.
- Updated Specialist Mode docs, checklists, capability index, prompt library, and quick-start prompts to require or state the Specialist Mode target.

## 0.0.103 - 2026-05-04

- Added Project Skill Index Routing so Specialist Mode agents scan `company/project-skills/index.md` when local project skills already exist.
- Clarified that local project skills should be used only when their trigger matches and they add local context, constraints, or verification.
- Updated Project Skill Incubator docs, Capability Index, and checklists with the project-skill adoption rule.

## 0.0.102 - 2026-05-04

- Added Project Skill Incubator so Specialist Mode projects can grow local project-specific skills from repeated workflow evidence.
- Added a project skill template and project-skill checker for local skill structure.
- Updated routing, Skill Dictionary, Skill Quality Standard, R&D loop guidance, Capability Index, checklists, and public docs.

## 0.0.101 - 2026-05-04

- Added Skill Dictionary routing so agents can choose standalone/domain skills without loading every skill file.
- Added a Skill Dictionary maintenance rule and verifier for skill additions, removals, renames, and material reroutes.
- Updated public docs, Capability Index, checklists, and R&D loop guidance with the Skill Dictionary flow.

## 0.0.100 - 2026-05-04

- Added Feature Adoption Check so agents must use or explicitly skip named/naturally triggered JarvisOS features.
- Routed the check into R&D loops, Specialist Mode continuation, closeout, public template validation, and the Capability Index.
- Clarified that Jarvis Doctor should run for public template/repo changes unless unavailable or genuinely irrelevant.

## 0.0.99 - 2026-05-03

- Added Feature Saturation Check so R&D loops pause before adding another adjacent feature after several consecutive additions in the same workflow area.
- Updated public checklists and Capability Index with continue, consolidate, simplify/remove, switch-domain, and ask-user outcomes.
- Clarified that the check stays lightweight and should not block one-off high-value ideas.

## 0.0.98 - 2026-05-03

- Added Closeout Stack Order so agents keep final reports compact when outcome, usage example, verification breadcrumbs, rollback handle, and options all apply.
- Updated public checklists and Capability Index with ordered closeout guidance.
- Clarified that agents should omit irrelevant closeout sections and avoid repeating the same fact across sections.

## 0.0.97 - 2026-05-03

- Added Rollback Handle so public/template/workflow changes leave a compact future repair pointer.
- Updated public checklists and Capability Index with rollback guidance for commit, version, branch, touched section, safest undo route, and required revalidation.
- Clarified that rollback handles are not rollback requests; they are short repair pointers for future agents.

## 0.0.96 - 2026-05-03

- Added Usage Example Closeout so agents include a short practical example after implementing a JARVIS R&D idea or workflow feature.
- Updated public checklists and Capability Index with usage-example guidance.
- Clarified that examples should be concrete and small, and can be skipped for purely internal cleanup with no user-observable behavior.

## 0.0.95 - 2026-05-03

- Added One-Screen Handoff Seed so agents can preserve compact continuation context when a full handoff file would be too much.
- Updated public checklists and Capability Index with seed guidance for current objective, live facts, next action, risks, read-first files, and fresh-chat starter text.
- Clarified that agents should not create a new handoff file only to store a seed; promote to full handoff only when continuation risk earns it.

## 0.0.94 - 2026-05-03

- Added Scratchpad Expiry so agents choose whether temporary notes, assumptions, QA files, screenshots, drafts, Work Packs, diagnostics, and one-off analysis should be promoted, archived as diagnostic, or discarded.
- Updated public checklists and Capability Index with closeout guidance for scratch artifacts.
- Clarified that scratch work should not become durable memory unless its reusable result is promoted to the canonical home.

## 0.0.93 - 2026-05-03

- Added Verification Breadcrumb so agents record the exact command, tool, source, artifact path, commit, or dashboard behind meaningful verification claims.
- Updated public checklists and Capability Index with compact rerunnable evidence guidance.
- Clarified that verification summaries should include meaningful results without dumping giant logs, and should name gaps when checks were not possible.

## 0.0.92 - 2026-05-03

- Added Context Freshness Badge so agents internally mark mutable context as `fresh`, `verified`, `stale-risk`, or `working-assumption` before relying on it.
- Updated public checklists and Capability Index with freshness guidance for memory, repo, public-version, blocker, date, and external-fact claims.
- Clarified that live tool state should win over stale memory during execution, with canonical memory updated during closeout.

## 0.0.91 - 2026-05-03

- Added Clarification Receipt so agents bind terse replies like `yes`, `go`, `second`, or `that one` back to the follow-up question they asked.
- Updated public checklists and Capability Index with follow-up answer binding guidance.
- Clarified that agents should restate the resolved instruction once before acting when a compact answer could otherwise be misread.

## 0.0.90 - 2026-05-03

- Added Referent Snapshot inside Clarifying Follow-Up Gate so agents identify what `this`, `that`, `it`, `here`, or similar words likely point to before acting or asking.
- Updated public checklists and Capability Index with target-resolution guidance.
- Clarified that agents may proceed with a stated target assumption only when there is one plausible low-risk target.

## 0.0.89 - 2026-05-03

- Added Clarifying Follow-Up Gate so agents ask compact follow-up questions before acting on short or vague requests that would change implementation.
- Updated public intro, README, Capability Index, and checklists with same-page follow-up guidance.
- Clarified that low-risk gaps can still proceed with stated assumptions, while consequential ambiguity should stop for a question.

## 0.0.88 - 2026-05-03

- Added Relevance-First Auto-Routing so agents use JarvisOS features by task relevance instead of requiring users to name each mechanism.
- Updated public intro, README, and Capability Index with the auto-routing principle.
- Clarified that auto-routing means optimal feature selection, not running every JarvisOS feature on every task.

## 0.0.87 - 2026-05-03

- Added Assumption Ledger to Agent Work Pack so meaningful tasks can expose consequential assumptions without stopping execution.
- Updated installed/public Work Pack templates and public docs with confidence and revisit-trigger fields.
- Added Assumption Ledger to the Capability Index as part of Agent Work Pack.

## 0.0.86 - 2026-05-03

- Added Dogfood Return Check to the R&D Loop so each new idea can briefly learn from the previous implemented feature.
- Updated the R&D Loop docs and Capability Index with the new return signal.
- Kept it tiny and optional when evidence is too early, avoiding a full retrospective ceremony.

## 0.0.85 - 2026-05-03

- Added Sunset Review Ledger guidance so R&D features with sunset clauses can be tracked without scanning scattered work orders.
- Added public docs for reviewing keep/simplify/merge/retire/extend-trial outcomes.
- Kept the ledger optional and lightweight; it is an inventory for review, not another mandatory gate.

## 0.0.84 - 2026-05-03

- Added a public Capability Index under Reference so users and agents can see what JarvisOS can do without scanning the changelog.
- Linked the Capability Index from the docs intro, sidebar, and README.
- Kept the index as a documentation map only; it does not add a new workflow rule or automation layer.

## 0.0.83 - 2026-05-03

- Added Accidental Message Guard guidance so cancelled, accidental, or ignored prior user messages are treated as discarded instructions.
- Added `ignore previous` / `cancel that` to the Command Deck and prompt library.
- Clarified that cancelled instructions should not create artifacts or memory unless a separate durable preference or safety-relevant fact is still affirmed.

## 0.0.82 - 2026-05-03

- Added Mode Exit Ramp guidance so agents downshift from Specialist Mode to Light Mode after meaningful closeout when the next work no longer needs project machinery.
- Updated Light Mode and Specialist Mode docs with downshift criteria and exceptions.
- Clarified that active work, review, release risk, inconsistent state, and explicit team-running requests should keep Specialist Mode active.

## 0.0.81 - 2026-05-03

- Added a compact Command Deck to `jarvis-os` so common phrases such as `status`, `continue`, `new idea`, `create a Work Pack`, and `JarvisOS Skill Ticket` route consistently.
- Added Command Deck examples to the public prompt library and README.
- Clarified that command phrases are intent shortcuts, not a rigid parser or automation layer.

## 0.0.80 - 2026-05-03

- Added Done Shape to Agent Work Pack so meaningful deliverables define the intended finished output before execution.
- Updated installed/public Work Pack templates and docs with audience, final form, must-be-visible, must-not-become, and quality-feel fields.
- Kept Done Shape inside Work Pack rather than adding a new standalone gate.

## 0.0.79 - 2026-05-03

- Added `references/skill-composition.md` so agents can combine JarvisOS with domain and plugin skills without over-reading.
- Routed multi-skill tasks through the Reference Router and public Operations docs.
- Clarified lead/support ownership: JarvisOS owns continuity and closeout while domain skills own deliverable method, format, quality bar, and domain verification.

## 0.0.78 - 2026-05-03

- Added `tools/jarvis-doctor.py`, a deterministic public-template diagnostic for agents.
- Added docs for Jarvis Doctor under Operations and routed it into workflow patch / closeout task cards.
- Doctor checks version metadata, required files, JarvisOS reference reachability, docs sidebar targets, obvious private-leak patterns, and git state.

## 0.0.77 - 2026-05-03

- Added Agent Work Pack as a temporary task-local execution context for meaningful JarvisOS work.
- Added `references/agent-work-pack.md` and `templates/company-mode/agent-work-pack.md`.
- Routed Work Packs through the Reference Router and Task Cards so agents can reduce over-reading without creating another task board.

## 0.0.76 - 2026-05-03

- Rejected the dense `ARCHIVE_OS` panel layout and rebuilt the docs landing page around a full-bleed retro-futurist archive-room hero.
- Added new generated bitmap assets for the archive-room hero scene and holographic local-memory seal.
- Simplified the page into a cinematic first viewport, command dock, invocation strip, and artifact-style docs links.

## 0.0.75 - 2026-05-02

- Recreated the Docusaurus docs landing page as a retro-futurist `ARCHIVE_OS` memory workstation.
- Added project-bound generated bitmap assets for a JarvisOS memory cartridge and CRT memory texture under `website/static/img/landing/`.
- Built the landing page around archive files, docs routes, boot logs, command rail, and memory-cartridge bay instead of a generic SaaS hero/cards structure.

## 0.0.74 - 2026-05-02

- Removed the custom Docusaurus landing page implementation so the docs landing can be recreated from a clean surface.
- Replaced the root page with a minimal redirect to `/docs/intro` and removed landing-specific CSS while preserving shared docs theme/navbar styling.

## 0.0.73 - 2026-05-02

- Added `references/skill-quality-standard.md` so JarvisOS skill and skill-ticket drafts follow an explicit quality bar.
- Routed skill creation/review through the Reference Router and strengthened skill-ticket templates with ownership, delegation, hard-boundary, repair, provenance, and acceptance-criteria sections.
- Added public docs for the Skill Quality Standard.

## 0.0.72 - 2026-05-02

- Added the `JarvisOS Skill Ticket` command so other JarvisOS chats can create numbered R&D tickets for reusable discoveries, feature ideas, and skill/skillset candidates.
- Added `references/cross-project-contributions.md`, contribution routing in the skill/router/task cards/R&D loop/reflexes, and reusable `contribution-candidate.md` / `skill-ticket.md` templates.
- Added public docs and prompt-library commands for skill tickets and skillset extraction.

## 0.0.71 - 2026-05-01

- Reworked the Docusaurus landing page to echo the original Hermes Agent framed editorial grid while keeping JarvisOS visually distinct.
- Added JarvisOS-specific framed navigation, local install/invoke commands, terminal continuity demo, vault map, and feature matrix.

## 0.0.70 - 2026-05-01

- Redesigned the Docusaurus landing page around a distinctive JarvisOS continuity-console concept.
- Preserved docs navigation and docs content while updating landing-specific styling.
- Verified the production Docusaurus build and rendered desktop/mobile landing states locally.

## 0.0.69 - 2026-05-01

- Updated README badges: docs now links to the deployed docs site in blue, built-by MOLEH appears in green, and version appears in red.

## 0.0.68 - 2026-05-01

- Fixed the docs navbar logo so the JarvisOS banner renders as a contained wordmark instead of a cropped icon.
- Hid the duplicate navbar title beside the wordmark.

## 0.0.67 - 2026-05-01

- Updated the GitHub Pages docs workflow to use Node 24.
- Kept the deployed Docusaurus docs site and public metadata current after enabling GitHub Pages.

## 0.0.66 - 2026-05-01

- Added a Docusaurus documentation site under `website/`.
- Added a custom JarvisOS docs landing page, structured docs navigation, full workflow documentation pages, and a GitHub Pages deployment workflow.
- Linked the README to the docs site and bumped public metadata.

## 0.0.65 - 2026-05-01

- Compressed the README opening into a shorter, sharper first screen.
- Moved explanation below the quick start and replaced long proof points with a compact capability table.

## 0.0.64 - 2026-05-01

- Redesigned the README opening with a stronger product-style first screen.
- Added a compact badge row, sharper positioning, proof-point style feature summary, and earlier quick-start path.
- Kept the design inspired by strong agent README conventions without copying Hermes Agent content or structure.

## 0.0.63 - 2026-05-01

- Added the JarvisOS banner image to the README.
- Updated the README header status to reflect the current public repository name and version.

## 0.0.62 - 2026-05-01

- Updated the Quick Start clone example for the public repository rename from `jarvis-light` to `JarvisOS`.
- Kept the installed skill package name as `jarvis-os`.

## 0.0.61 - 2026-05-01

- Added R&D Stack Compression Check to the R&D Idea Loop.
- Updated Task Cards so repeated workflow-feature runs check whether new ideas can merge, simplify, downgrade, or become acceptance criteria before adding new workflow surface.
- Clarified that standing behavior should not be silently retired; consequential removals still need sunset/review decisions.

## 0.0.60 - 2026-05-01

- Added Regression Rehearsal for active eval seeds.
- Updated R&D Idea Loop and Task Cards so one relevant eval seed can be manually checked before pure ideation when no stronger evidence candidate is obvious.
- Updated eval-seed templates with rehearsal result fields.

## 0.0.59 - 2026-05-01

- Added Reflex Eval Seeds for consequential promoted learning.
- Added an eval-seed template and Reflex candidate eval-seed fields.
- Updated Self-Improvement Reflexes and Task Cards guidance so promoted standing behavior can carry a tiny future regression check without becoming a full eval harness.

## 0.0.58 - 2026-05-01

- Added Learning Pulse Cadence for R&D idea loops.
- Learning Pulse now runs before pure ideation when three R&D idea loops completed since the last pulse or when no fresh unpromoted Friction/Reflex signal exists.
- Updated R&D Idea Loop and Task Cards guidance while clarifying that cadence is manual, lightweight, and not background automation.

## 0.0.57 - 2026-05-01

- Added Idea Closeout Explanation to the R&D Idea Loop.
- Updated idea-card templates so implemented ideas can explain the problem, concept, mechanics, value, tradeoffs, and dogfood path.
- Updated the R&D Idea Loop task card so closeouts explain the idea after refresh and verification.

## 0.0.56 - 2026-05-01

- Added Learning Pulse reports for compact self-improvement readouts.
- Added a learning-pulse template and routing from the skill, Reference Router, Task Cards, and R&D Idea Loop.
- Clarified that a pulse can recommend promotion but cannot silently change standing rules.

## 0.0.55 - 2026-05-01

- Added Self-Improvement Reflexes for candidate-producing learning after meaningful work.
- Added a reflex candidate template with lanes for observed, candidate, repeated, promoted, rejected, archived, and superseded signals.
- Routed reflexes from the skill, Reference Router, and Task Cards while preserving the rule that standing behavior is not silently rewritten.

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
