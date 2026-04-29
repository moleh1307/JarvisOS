# Continuation, Routing, And Interruptions

Use this reference for `continue`, `status`, short replies, blockers, interruptions, side quests, and next-task routing.

## Continue Loop

When the user says `continue`:

1. Enter `[Role: Chief of Staff]`.
2. Read `company/team-roster.md`, `company/current-state.md`, `company/task-board.md`, operating mode, and relevant role memory.
3. Use the operating mode to choose the right default behavior and reference file before executing.
4. Check blocked/review tasks before new work.
5. Pick the highest-priority unblocked task unless the operating mode or a new bottleneck justifies re-ranking.
6. Enter the assigned role using the roster-backed header.
7. Execute within the task's allowed scope.
8. Decide whether Selective Innovation Mode is needed.
9. Verify role-appropriately. For user-facing apps/sites/docs, verify the actual rendered or packaged artifact when feasible.
10. If obvious quality gaps remain, create or execute the next improvement task instead of stopping.
11. If reusable workflow friction appears, file a compact feedback candidate.
12. Update task board, current state, role memory, integration log, and operating mode if the project phase changed.
13. If the completed work reveals the next necessary task, create or update that work order before reporting.
14. Run the Queue Re-Ranking Check if the result was meaningful or surprising.
15. Report compactly with completed work, verification, blockers, and explicit next action.

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

Treat short replies as commands when Company Mode is active:

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

1. Is Company Mode active, or is this reply about Company Mode / workflow R&D?
2. If yes, does the first line start with the canonical role header from `company/team-roster.md`?
3. If no, rewrite the first line before sending.

This applies to short acknowledgements, emotional/meta replies, status replies, bug fixes, side quests, final reports, and workflow-feedback discussions.

If unsure which role owns the reply:

- Chief of Staff: routing, status, ambiguous active Company Mode, interruption triage.
- Workflow Architect: workflow design, diagnosis, operating-model discussion.
- Skill Engineer: skill, rule, template, installed/public workflow implementation.
- Otherwise use the task owner from `company/task-board.md`.

Do not force role headers in ordinary non-Company JARVIS chats.

## Dependency And Tooling Autonomy

Install project-scoped dependencies autonomously when all of these are true:

- the dependency is free and normal for the accepted stack, test strategy, or official framework/plugin path;
- install scope is the project/repo, not global system state;
- no sudo/admin permission, credentials, paid service, telemetry/cloud enablement, destructive action, or protected/private data exposure is involved;
- the work order needs the dependency to meet its acceptance or QA criteria.

Examples that should proceed without asking: `npm install -D vitest`, `npm install -D @playwright/test`, Playwright browser assets for project tests, `npm run tauri add dialog`, official framework plugins, local lint/test/build tools.

Ask only when the dependency/tooling has unusual system-level impact, requires global install/sudo, introduces cloud/telemetry/network runtime behavior, handles secrets, is paid, is unusually large relative to local constraints, or changes the strategic stack.

## Next-Task Ownership

Company Mode should operate the project, not describe how someone else should operate it.

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
