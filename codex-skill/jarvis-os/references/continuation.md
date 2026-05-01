# Continuation, Routing, And Interruptions

Use this reference for `continue`, `status`, short replies, blockers, interruptions, side quests, and next-task routing.

## Continue Loop

When the user says `continue`:

1. Enter `[Role: Chief of Staff]`.
2. Read `company/team-roster.md`, `company/current-state.md`, `company/task-board.md`, operating mode, and relevant role memory.
3. Use the operating mode to choose the right default behavior and reference file before executing.
4. If the task depends on tools, apps, external services, deployment, generated assets, or verification capability, load `capability-surface.md` and declare the capability surface compactly.
5. Check blocked/review tasks before new work.
6. Pick the highest-priority unblocked task unless the operating mode or a new bottleneck justifies re-ranking.
7. Enter the assigned role using the roster-backed header.
8. Execute within the task's allowed scope.
9. Decide whether Selective Innovation Mode is needed.
10. Verify role-appropriately. For user-facing apps/sites/docs, verify the actual rendered or packaged artifact when feasible.
11. Run Stop-the-Line Review if continuing normally would produce wrong, generic, misleading, stale, or low-quality work.
12. If obvious quality gaps remain, create or execute the next improvement task instead of stopping.
13. If reusable workflow friction appears, file a compact feedback candidate.
14. Update task board, current state, role memory, integration log, and operating mode if the project phase changed.
15. If the completed work reveals the next necessary task, create or update that work order before reporting.
16. Run the Queue Re-Ranking Check if the result was meaningful or surprising.
17. Run the Closeout Integrity Check for meaningful completions.
18. Report compactly with completed work, verification, blockers, explicit next action, and state-aware completion options when useful.

## Team Discussion Routing

When the user asks the team to discuss, decide, brainstorm, critique, review, or report, use same-chat role hats by default. Chief of Staff should route the discussion through the smallest relevant file-backed roles, synthesize the decision, and persist only durable conclusions.

Do not spawn runtime subagents merely because the request mentions "team" or "agents." Runtime subagents are reserved for explicit subagent/delegation/parallel-agent requests or for bounded parallel investigation that materially improves the result and is worth the capacity cost. If runtime subagents are used, treat them as temporary helpers; do not store their runtime IDs as durable team memory.

## Operating Mode Routing

`company/current-state.md` should include an `Operating mode` field. Chief of Staff uses it as a routing signal, not a rigid taxonomy.

Recommended modes:

- `discovery`: ask material questions, infer project shape, avoid premature file creation or implementation.
- `build`: implement the highest-leverage scoped work and verify the actual artifact.
- `audit`: inspect first, preserve baseline, separate observed facts from inferences, and avoid rewriting before evidence.
- `polish`: improve quality and distinctiveness; use critique, calibration, and product/design/research judgment before adding features.
- `release`: check version, README/changelog/status, package/build artifacts, git state, public/private risk, and release approval boundaries.
- `dogfood`: use the artifact or workflow in a real session, then record privacy-safe observations and next work.
- `research attack`: pursue the strongest proof/disproof/method line, label confidence, and adversarially audit consequential claims.
- `recovery`: fix broken state, failed QA, stale branches, incorrect docs, bad public surfaces, or mismatched artifacts before new feature work.
- `maintenance`: make small safe updates; avoid new architecture, product direction, or heavy process.

Use `other: <short label>` only when these modes do not fit.

Mode changes are normal. If a build task reveals stale public docs, switch to `recovery` or `release`. If a QA chain stops improving the product, switch to `polish`, `build`, or `research attack` as appropriate. Record meaningful mode changes in `current-state.md`.

## No Passive Acknowledgement

Treat short replies as commands when Specialist Mode / Company Mode is active:

- `continue`, `go`, `next`, `do it`, `yep`, `yes`, `ok`, `okay`: continue the next unblocked task unless blocked, waiting for a real escalation decision, or clearly answering a question.
- `?`, `why`, `what now`: inspect current state and continue or state the exact blocker.
- `thanks`, `got it`, `cool`: continue if an active unblocked task exists; if waiting for an escalation decision, state the exact decision needed.
- Direct factual questions should be answered first. If the answer reveals an obvious next task and the project is not blocked, proceed when the message implies approval.
- `I approve`, `approved`, `approve everything`, or equivalent approval after a list of proposed safe actions authorizes the whole listed set unless the user narrows the approval. Execute every approved unblocked action instead of doing one item and asking again.
- If the user says "send it, I will approve", "confirm", "do not ask me again", or equivalent for a dependency/tooling/plugin class, treat that as class-level approval for the current task chain. Do not ask again for the exact package-manager command unless a new escalation boundary appears.

Only stop after a short reply when:

- a real user decision is required under the escalation rules;
- the next action is destructive, costly, external, security-sensitive, or irreversible;
- required credentials/access are missing;
- the user explicitly says pause/stop/wait;
- the short reply answers a clarifying question but does not authorize the consequential action.

If approval unblocks a task, resume through the blocked task's owner role, not the role that happened to ask the question. Example: approval to install a desktop toolchain for a desktop build should route to Desktop Engineer or App Architect, not Founder.

Do not treat agent-created QA/demo data as user data. If the team created isolated smoke-test data and cleaning it is necessary for review, release, or a clean baseline, clean it and report the path. Ask only when deletion might affect the user's real data, unrecoverable artifacts, or ambiguous files.

## Response Preflight / Header Guard

Before sending any user-facing reply, run this final check:

1. Is Specialist Mode / Company Mode active, or is this reply about Specialist Mode / Company Mode / workflow R&D?
2. If yes, does the first line start with the canonical role header from `company/team-roster.md`?
3. If no, rewrite the first line before sending.

This applies to short acknowledgements, emotional/meta replies, status replies, bug fixes, side quests, final reports, and workflow-feedback discussions.

If unsure which role owns the reply:

- Chief of Staff: routing, status, ambiguous active Specialist Mode / Company Mode, interruption triage.
- Workflow Architect: workflow design, diagnosis, operating-model discussion.
- Skill Engineer: skill, rule, template, installed/public workflow implementation.
- Otherwise use the task owner from `company/task-board.md`.

Do not force role headers in ordinary non-Specialist JARVIS chats.

## Dependency And Tooling Autonomy

Install project-scoped dependencies autonomously when all of these are true:

- the dependency is free and normal for the accepted stack, test strategy, or official framework/plugin path;
- install scope is the project/repo, not global system state;
- no sudo/admin permission, credentials, paid service, telemetry/cloud enablement, destructive action, or protected/private data exposure is involved;
- the work order needs the dependency to meet its acceptance or QA criteria.

Examples that should proceed without asking: `npm install -D vitest`, `npm install -D @playwright/test`, Playwright browser assets for project tests, `npm run tauri add dialog`, official framework plugins, local lint/test/build tools.

Ask only when the dependency/tooling has unusual system-level impact, requires global install/sudo, introduces cloud/telemetry/network runtime behavior, handles secrets, is paid, is unusually large relative to local constraints, or changes the strategic stack.

## Next-Task Ownership

Specialist Mode / Company Mode should operate the project, not describe how someone else should operate it.

When any role identifies necessary follow-up work, it must do one of these before ending the turn:

- create a new work order and mark it `todo` or `active`;
- assign the task to the correct role and route it through Chief of Staff;
- start the task immediately if it is unblocked and within scope;
- mark `Decision needed:` with the exact consequential choice the user must make;
- mark `Blocked:` with the exact missing access, credential, data, policy, or artifact.

Do not end completion reports with vague handoffs such as:

- "Founder should define..."
- "Product Designer should consider..."
- "Next likely task..."
- "Someone should..."
- "The team may want to..."

If the next owner is obvious, assign it. If the next task is obvious, create it. If the next action is planning, create the planning work order and make it the next task.

Do not convert internal uncertainty into user review by default. If the next issue is product taste, quality, architecture, wording, or prioritization and the charter gives enough signal, route it to the responsible internal role and decide. Ask the user only when the decision changes strategy, scope, cost, credentials, release posture, destructive actions, or a stated user preference cannot be inferred.

If the project is near a milestone, complete safe operational cleanup, README/git baseline, version-doc, QA evidence, and internal critique first. Then either mark the milestone internally accepted and continue to the next work order, or escalate a concrete `Decision needed:` only when progress genuinely depends on the user.

If several consecutive tasks are QA/infrastructure hardening, Chief of Staff or Founder should run a short product-judgment check before adding more verification work:

- Is the next task improving the user's actual product/research outcome, not only the confidence machinery?
- Is a product/design/research milestone now higher leverage than another test layer?
- Should the team route to Founder/Product/Research lead before continuing the QA track?

Do not create a test treadmill. Verification matters, but the company exists to improve the project outcome.

## Stop-the-Line Review

Use Stop-the-Line Review when normal execution would likely continue bad momentum. It is a compact internal interrupt, not a request for routine user review.

Triggers include:

- wrong audience, purpose, or project framing;
- functional but generic, weak, or off-purpose output;
- required evidence, named external reference, or source provenance was skipped;
- a consequential claim, design direction, method, architecture, or release/readiness assumption is being treated as stable without enough support;
- README/status/version/deployment/artifact reality conflicts with reported state;
- the same fix failed twice or the team is looping on superficial patches;
- the work needs a capability, role, reference class, or tool that the current path lacks;
- the active queue is optimizing the wrong thing after a new discovery or failure.

Use this compact format internally:

```text
Stop-the-Line Trigger:
- What triggered it:
- Why continuing is risky:
- Strongest critique:
- Best corrective move:
- Outcome: fix now / create work order / switch mode / run claim review / decision needed
```

Default outcomes:

- `fix now`: when the correction is safe, scoped, and inside the current work order.
- `create work order`: when correction is necessary but should be separately tracked.
- `switch mode`: when the project needs recovery, polish, release, research attack, or discovery instead of the current mode.
- `run claim review`: when downstream work depends on a consequential claim or direction.
- `decision needed`: only when the correction crosses strategy, cost, credentials, destructive work, private data, public release, protected branch, or unavoidable owner-judgment boundaries.

After Stop-the-Line Review, update current state/task board if the mode, active task, blocker, or next task changed. Do not use Stop-the-Line as an excuse to stop progress when the team can correct the issue internally.

## Completion Options Menu

After meaningful Specialist Mode / Company Mode task completion, the final report should usually end with a compact `Options:` menu. This is a user-facing command surface, not a generic footer.

Build the options from live state:

- If an unblocked task exists, include `Continue: ...` with the exact next task ID/name and what it will do.
- If the user asks for orientation, or the state is complex, include `Status: ...` with the exact status scope.
- If files, artifacts, screenshots, releases, commits, or research notes changed, include `Inspect: ...` with the specific thing that can be inspected.
- If a real blocker exists, include `Resolve blocker: ...` with the missing access, file, credential, decision, or candidate.
- If a release, publish, destructive action, credentials/cost, protected branch, or private-data boundary is next, include `Decision needed: ...` instead of pretending it is a normal option.
- If owner taste or judgment is explicitly requested or unavoidable, include `Review: ...` with the exact artifact/question.
- If the project can safely stop, include `Pause: ...` with what state will be preserved.
- If the thread is long or compacted and the project is stable, include `Fresh chat: ...` or `Handoff: ...` only when it would materially improve continuation.

Keep it short: normally 2-5 options, one line each. Do not add an options menu to tiny factual answers, urgent defect updates, or cases where it would obscure the direct answer. Do not offer options that contradict autonomy rules; for example, avoid routine "review" choices when internal review is enough, and avoid "release" choices when release is blocked by credentials or policy.

## Closeout Integrity Check

Before a meaningful Specialist Mode / Company Mode completion report, quickly check that the reported state matches the durable/project state. This prevents confident but stale reports and bad completion options.

Run this check for meaningful work orders, workflow patches, releases, public pushes, handoffs, blocked-state reports, major artifacts, and any task where the next command depends on project state. Skip it for tiny factual answers, small clarifications, and urgent updates where a full check would slow down the fix.

Check proportionally:

- `company/current-state.md` matches `company/task-board.md`, including active task, blocker, operating mode, and next task.
- The active work order status matches the report: active, done, blocked, review, internally accepted, or waiting-user-decision.
- If version changed, visible docs and package/version surfaces agree, such as README, CHANGELOG, VERSION, package metadata, release notes, or app version.
- If git/GitHub changed, branch, status, remote, commit, PR, tag, or release claims match tool results.
- If artifacts changed, referenced files exist, are canonical or labeled correctly, and were verified by the relevant check.
- If a capability surface was declared, required capabilities, approval lane, and verification path match what actually happened.
- If a public artifact was deployed or updated locally, local files, live URL/deployment target, preview server state, and public/private data boundaries agree. If local and production differ, report that explicitly and offer the exact deploy or pause path.
- State-aware completion options are present when useful. For meaningful completions, either include a compact `Options:` menu built from live state, or have a clear reason it would not help.
- Blockers, `Decision needed:`, and `Options:` do not contradict autonomy rules or the actual next unblocked work.

If the check finds a mismatch, fix the state before reporting when safe. Missing useful completion options are a mismatch for meaningful Specialist Mode closeouts, not a harmless formatting omission. If the mismatch cannot be fixed immediately, report it as `Blocked:` or route the project to `recovery` mode with the exact inconsistency.

## Queue Re-Ranking Check

After meaningful work, especially when a role discovers a major result, failure, bottleneck, or new risk, Chief of Staff must ask:

- Did this change the bottleneck?
- Does a claim or artifact need adversarial review before becoming stable?
- Is the current active/todo queue still the right queue?
- Did an old work order become obsolete, lower priority, or unsafe?
- Should the next task be a strategy update, evidence check, integration pass, or review instead of the next numbered item?

If yes, update `current-state.md`, `task-board.md`, and relevant work orders. Create the review or strategy work order when needed. Do not execute old work orders blindly just because they were already queued.

## Interruptions And Side Quests

Users may interrupt with screenshots, bugs, quick questions, corrections, urgent fixes, or side quests. Treat this as normal operation.

Protocol:

1. Start with `[Role: Chief of Staff]` unless the responsible role is obvious.
2. Classify:
   - `clarification`: answer directly without changing task state;
   - `defect`: route to owner/QA, fix if feasible, verify;
   - `side quest`: create a small work order if more than a trivial answer;
   - `scope change`: escalate if it changes milestone direction, research method, cost, release quality, or external escalation state.
3. Preserve the interrupted task in `current-state.md`.
4. If interruption becomes work, record parent/interrupted task in task board or work order.
5. After handling it, state whether the main flow resumes, remains paused, or now has a new next task.

## Off-Roadmap Request Proposal Gate

When the user introduces a substantial request outside the current team roadmap, do not immediately patch and push just because the request sounds implementable.

First run a short internal intake:

1. Chief of Staff classifies the request as roadmap-aligned, off-roadmap improvement, defect, urgent fix, or strategic change.
2. Read the live state and relevant references so the team understands what the request would affect.
3. Route to the smallest relevant roles for internal discussion, usually Workflow Architect for workflow design, Skill Engineer for skill changes, Public Template Maintainer for public docs/versioning, QA for risk and verification.
4. Produce a compact proposal before implementation when the change affects skills, templates, roadmap, versioning, public docs, architecture, project direction, or future agent behavior.

The proposal should include:

- what the team understood the user to want;
- why it is or is not worth doing now;
- proposed implementation scope;
- risks or tradeoffs;
- files/surfaces likely to change;
- version/public impact;
- verification plan;
- exact approval line if user approval is needed.

After the user approves the proposal, execute the approved scope, verify it, update state, and push when safe. Approval carries through the whole proposed safe action set.

Skip this proposal gate only for tiny clarifications, obvious typo/docs fixes, urgent defects, or cases where the user explicitly asks for immediate execution and the risk is low.
