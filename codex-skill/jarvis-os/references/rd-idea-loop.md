# R&D Idea Loop

Use this reference when a Specialist Mode team is explicitly running a continuous improvement, product R&D, workflow R&D, or idea-by-idea loop.

The loop exists to turn creative ideas into tested workflow changes without letting brainstorming become theater.

## Loop Contract

Run one idea at a time:

1. Run Dogfood Return Check for the last meaningful R&D feature when useful.
2. Ideation role proposes one out-of-box idea.
3. Relevant team roles discuss the idea.
4. If rejected, record the rejection reason and return to ideation.
5. If accepted, Chief of Staff or project manager converts it into a short task list.
6. The team implements the task list.
7. The project or skill is refreshed.
8. The closeout explains the implemented idea compactly.
9. The team defines where the new feature should be dogfooded next.
10. Return to one new idea.

Do not batch many unrelated ideas unless the user explicitly asks for a broad brainstorm. A loop is strongest when every idea must survive discussion, implementation planning, and dogfood evidence.

## Dogfood Return Check

At the start of a new R&D loop, briefly check the last meaningful R&D feature before proposing a fresh idea, unless the user explicitly wants to skip review or the previous feature is clearly not relevant yet.

Answer only what helps the next decision:

- What was the last feature expected to improve?
- Did this cycle use it, avoid it, or reveal that it is too early to judge?
- Did it reduce friction, add overhead, expose a gap, or need a future sunset review?
- Should today's idea use that evidence, ignore it, or record a follow-up candidate?

Keep this check tiny. It is a return signal, not a retrospective. If it shows no useful evidence, say `too early` and move on.

## Idea Quality Bar

A strong idea should be:

- non-obvious enough to improve the system, not just restate an existing rule;
- practical enough to implement in the current tool and memory environment;
- small enough to become one to five tasks;
- useful enough that the team will actually dogfood it;
- sharp enough to simplify, replace, remove, or make something less necessary, unless added complexity is explicitly justified;
- safe for public/private boundaries if it affects reusable templates.

Reject or revise ideas that require pretending background work happens without an automation, leaking private memory, adding ceremony without payoff, or depending on tools that are unavailable.

## Subtraction Gate

Before accepting an idea, answer:

- What does this simplify?
- What does this remove?
- What does this replace?
- What does this make less necessary?

If the honest answer is "nothing," the team may still accept the idea, but the idea card must explain why the added complexity is worth it.

The goal is net workflow sharpness. Continuous R&D should make the system more capable without only making it larger.

## Stack Compression Check

After several workflow features in a row, or when a proposed idea mostly adds another named rule, card, template, or gate, run a compact compression check before acceptance:

- Can this be merged into an existing reference, card, template, or closeout check?
- Can an older rule be simplified, downgraded, or made less prominent?
- Can this be a note, eval seed, or acceptance criterion instead of standing behavior?
- Does accepting this idea reduce future work more than it increases cognitive load?

Prefer `merge`, `simplify`, `downgrade`, or `reject` over adding a new surface when the benefit is mostly organizational. Do not silently retire or weaken standing behavior; create a sunset/review decision when removal is consequential.

## Friction Inbox

Use a Friction Inbox when real usage reveals a small but potentially reusable problem:

- the agent hesitated or asked again because the workflow was unclear;
- the agent repeated itself or added ceremony;
- current state, blocker, version, or handoff drift appeared;
- the user corrected the workflow, not just the task output;
- a quality miss, routing miss, or tool gap appeared;
- the same class of friction has happened before.

Capture the smallest useful item first. Inbox items are candidates, not rules. They should not become standing behavior until triaged through the idea loop, a work order, eval, template update, or explicit user approval.

Before pure ideation, check whether the Friction Inbox, Reflex candidates, cross-project contribution candidates, or a recent Learning Pulse contains a stronger evidence-backed candidate. Prefer real friction, project contribution, or learning signal over novelty when the signal is repeated, high-impact, or blocking compounding improvement.

Use Learning Pulse Cadence when evidence is thin or stale: if three R&D idea loops completed since the last pulse, or if there is no fresh unpromoted Friction/Reflex signal before ideation, run a compact Learning Pulse first. Skip it when a recent pulse is still current or a strong unpromoted candidate is already obvious.

Use Regression Rehearsal when active eval seeds exist and no stronger evidence candidate is already obvious. Run at most one tiny eval seed before pure ideation, record pass/fail/skip, and use the result as evidence for the next idea only if it reveals a real regression or gap. This is manual review, not an automated eval harness.

## Sunset Clause

For meaningful workflow features, define a future review trigger before implementation begins.

The review should be able to choose one of:

- `keep`: the feature is still useful as written;
- `simplify`: the feature works but can be lighter;
- `merge`: the feature should be folded into another rule, card, or template;
- `retire`: the feature no longer earns its complexity;
- `extend trial`: more dogfood evidence is needed.

Use a Sunset Clause for standing behavior changes, new references, new templates, new gates, and process additions. Skip it for tiny one-off tasks, urgent fixes, and artifacts that are already temporary.

Do not retire, delete, or weaken a standing rule silently. A sunset review creates a decision point; it is not permission for unreviewed removal.

## Sunset Review Ledger

When several meaningful workflow features have active Sunset Clauses, keep a compact Sunset Review Ledger in the project governance layer.

Use a ledger when sunset clauses are becoming scattered across work orders, idea cards, or session notes. Skip it for small projects with only one or two obvious trial features.

The ledger should track only review-useful facts:

- feature or task ID;
- what was added;
- review trigger;
- current evidence;
- likely review outcome;
- next review action;
- owner or role;
- status such as `watch`, `due`, `reviewed`, `retired`, or `merged`.

The ledger is an inventory, not a new approval gate. Agents should consult it during status, R&D continuation, Stack Compression Check, or maintenance review when it is likely to prevent stale process debt.

When a sunset review happens, record one compact decision: `keep`, `simplify`, `merge`, `retire`, or `extend trial`, plus the reason and any follow-up work order. Do not duplicate the full work order history in the ledger.

## Team Discussion

Keep discussion compact. Use only the roles that can materially improve the decision:

- Ideation role: why this idea matters.
- Workflow/Product role: whether it fits the operating model and user value.
- Engineering role: whether it is implementable without bloat.
- QA/Red-team role: what can fail, leak, or become ceremony.
- Chief of Staff: final accept/reject and task-list conversion.

Record the decision in an idea card when the idea is accepted, rejected for a durable reason, or likely to matter later.

## Accepted Idea Handling

For accepted ideas:

- create or update an idea card;
- link any contribution candidate that supplied the evidence;
- complete the Subtraction Gate before final acceptance;
- define a Sunset Clause for meaningful workflow features;
- create one work order when the implementation is single-scope;
- create a short task list when the idea naturally splits into two to five tasks;
- mark lifecycle state and risk lane for meaningful work orders;
- define verification and dogfood evidence before implementation begins.

Dogfood evidence should answer:

- Which new behavior was used?
- Where was it used?
- Did it help, fail, or add overhead?
- What should the next loop learn from it?

## Idea Closeout Explanation

After implementing an accepted idea, include a compact explanation of the idea itself in the closeout.

The explanation should cover:

- problem: what friction, gap, or opportunity triggered the idea;
- concept: the core mechanism in plain language;
- practice: how agents will use it;
- value: why it improves JARVIS OS or the active project;
- tradeoffs: what could become noisy, redundant, unsafe, or heavy;
- dogfood path: where the team will use it next.

Keep this explanation short. It should help the user understand the design, not restate every file changed or duplicate the work order.

## Rejected Idea Handling

For rejected ideas, keep only the useful reason:

- already covered by an existing rule;
- too much ceremony;
- weak user value;
- unsafe public/private boundary;
- needs more field evidence;
- blocked by missing capability;
- better as a later candidate.

Do not preserve long rejection debates. Preserve the insight that should prevent repeating the same weak idea.

## Anti-Ceremony Rules

- Do not create idea cards for tiny one-off suggestions.
- Do not run the full loop for urgent bug fixes or obvious maintenance.
- Do not let the ideation role override evidence, safety, or user direction.
- Do not treat "creative" as permission to ignore verification.
- Do not let Idea Closeout Explanation become generic filler; omit obvious repetition and explain only the useful design logic.
- Do not run every eval seed on every loop; Regression Rehearsal uses one relevant seed or skips when stronger evidence already exists.
- Do not add a new named mechanism when Stack Compression Check shows an existing reference/card/template can carry the behavior.
- Do not return to ideation until the accepted feature is refreshed and dogfooded, unless a real blocker appears.
