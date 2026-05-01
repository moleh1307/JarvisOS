# Adaptive Operating Patterns

Use this reference when Specialist Mode / Company Mode must decide how to shape a project, which operating mode it is in, how much structure to create, when to run Excellence Calibration, how to label confidence, whether to run adversarial review, how to run the Claim Review Loop, and when to re-rank the queue.

These are general operating patterns, not project-type recipes. Do not hardcode "math projects need X" or "apps need Y." Infer the project's needs from the user's goal, the observed project, the risk profile, and the success bar.

## Project-Shape Inference

Before Founder creates the company layer for a serious project, write a compact Project-Shape Inference. This can live in `project-charter.md` for greenfield work or `adoption-audit.md` for existing projects.

Answer proportionally:

- What kind of work is this?
- What makes success hard?
- What would failure look like?
- What evidence, artifacts, or outputs matter?
- What roles or disciplines are needed?
- Is the work excellence-critical, and what calibration is needed before execution?
- What should not be overbuilt?
- What confidence lanes are needed?
- What verification or adversarial review gates are justified?
- Is a task board enough, or does the project need a strategy map, evidence ledger, attack tree, calibration pack, or similar artifact?

For simple projects, this may be five bullets. For complex research, product, data, writing, strategy, or architecture projects, it can be fuller.

## Operating Mode Declaration

Project-shape inference describes the work. Operating mode describes what the company should do now.

Record the current mode in `company/current-state.md`:

```text
Operating mode: discovery / build / audit / polish / release / dogfood / research attack / recovery / maintenance
```

Use `other: <short label>` if none fit.

Mode meanings:

- `discovery`: ask material questions, infer project shape, and avoid premature implementation.
- `build`: execute scoped work that advances the artifact, repo, research, or deliverable.
- `audit`: inspect existing reality, preserve baseline, and separate observed facts from inferences before changing things.
- `polish`: improve quality, distinctiveness, clarity, ergonomics, or craft before adding more surface area.
- `release`: verify version/docs/git/package/public-risk surfaces and respect release escalation boundaries.
- `dogfood`: use the artifact or workflow in a real session and record privacy-safe observations.
- `research attack`: pursue the strongest proof/disproof/method line and attack consequential claims before stabilizing them.
- `recovery`: fix broken state, failed QA, stale docs, branch drift, or artifact mismatch before new work.
- `maintenance`: make small safe updates without changing strategy, architecture, or project direction.

Chief of Staff should use operating mode during `continue` to choose the right reference files, role, next task type, and queue re-ranking behavior. Update the mode when the project phase changes; do not preserve a stale mode just because the previous work order used it.

## Excellence Calibration Gate

Use Excellence Calibration when the quality bar materially affects success and a weak target would cap the project before execution starts.

Examples:

- user-facing products, websites, apps, decks, documents, or demos;
- professor/client/public-facing deliverables;
- research notes, proof attempts, or literature maps where rigor and provenance matter;
- data, statistical, or visualization outputs that others may trust;
- architecture, strategy, or workflow decisions that shape later work;
- redesigns, rebuilds, or recovery work after rejection;
- any artifact the user asks to be best-in-field, AAA, world-class, not generic, or unusually strong.

Skip for tiny bug fixes, mechanical docs updates, routine QA, small refactors, or urgent recovery work where the target is already obvious.

Answer compactly before major execution or revision:

1. Reference class: what field, artifact type, or standard are we competing with?
2. Excellence bar: what would make this top-tier for that class?
3. Benchmarks/references: what strong examples, papers, products, artifacts, or standards calibrate us?
4. Missing capability: what would a real team hire or consult for this?
5. Rejection tests: what would make this generic, weak, misleading, unsafe, or not worth shipping?
6. Decision: proceed, add/activate a role, run reference research, reshape the work order, or lower scope honestly.

The gate does not require a new file by default. Put the answers in the work order, project charter, art direction brief, research plan, or a dedicated calibration artifact only when the project size justifies it.

## Confidence Lanes

Use confidence lanes when a project has claims, hypotheses, results, designs, data outputs, architecture decisions, or public statements that can vary in certainty.

Recommended lanes:

- `verified`: checked by tool, source, proof, test, or review.
- `working-assumption`: currently useful but not fully proven.
- `speculative`: useful for exploration, not stable project truth.
- `needs-audit`: important enough that another role should attack it.
- `rejected`: considered and ruled out; keep only if the reason matters.

Do not turn every trivial note into a confidence table. Use lanes where future agents could otherwise mistake a guess for fact.

## Optional Strategy Artifacts

A task board tracks work. A strategy map tracks why the work matters and how routes relate.

Create optional artifacts only when useful:

- `company/strategy-map.md`: hard, uncertain, multi-route, or long-horizon projects.
- `company/evidence-ledger.md`: projects with sources, claims, data, methodology, legal/financial/medical risk, research claims, or public assertions.
- `company/adversarial-review.md`: consequential results that need a hostile check before acceptance.
- `company/excellence-calibration.md`: excellence-critical projects where the reference class, top-tier bar, benchmarks, missing capability, and rejection tests need to stay visible.

Project-specific names are allowed when clearer, such as `attack-tree.md`, `claims-map.md`, `design-calibration.md`, or `release-risk-review.md`.

## Adversarial Review Trigger

When a role produces a consequential internal result, trigger adversarial review or explicitly record why review is skipped.

Examples:

- proof claim -> proof audit;
- major design direction -> design critique;
- data result -> reproducibility/validation audit;
- architecture choice -> failure-mode review;
- method choice -> methodology review;
- release candidate -> release/QA audit;
- public claim -> source/fact check.

The review should try to break the result, not rubber-stamp it.

Review output should state:

- claim/result under review;
- confidence lane before review;
- strongest attack;
- defects found;
- surviving claim after review;
- new confidence lane;
- next work order if needed.

## Claim Review Loop

Use this loop when downstream work would depend on a consequential claim, assumption, result, direction, or method.

Examples:

- proof lemma or mathematical route;
- product/design direction;
- architecture decision;
- data/statistical result;
- research methodology choice;
- release/readiness claim;
- strategy assumption.

The loop is:

1. State the claim precisely enough to attack.
2. Assign its current confidence lane.
3. Create or run an independent attack/review task before downstream work treats it as stable.
4. Record the strongest attack and what survived.
5. End with exactly one outcome:
   - `promoted`: stable enough to build on;
   - `revised`: usable only in a narrower or corrected form;
   - `rejected`: should not be used downstream;
   - `split`: converted into sharper subclaims or subproblems.
6. Chief of Staff re-ranks the queue from that outcome.

Do not create a review task for every small implementation detail. Use the loop when being wrong would waste substantial work, publish a false claim, lock in weak design, corrupt data conclusions, or send the company down the wrong route.

## Queue Re-Ranking

After meaningful work, Chief of Staff should ask:

- Did the last result change the bottleneck?
- Did a claim become important enough to audit?
- Did an old work order become obsolete or lower priority?
- Is the next task still the highest-leverage task?
- Should the team create a new review, integration, cleanup, or strategy work order before continuing?

If the bottleneck changed, update `task-board.md`, `current-state.md`, and relevant work orders. Do not blindly execute old numbered tasks just because they were already queued.

If continuing the old queue would optimize the wrong thing, create stale state, or build on a weak claim/direction, run Stop-the-Line Review from `references/continuation.md`. Stop-the-Line can route to recovery, polish, release, research attack, discovery, claim review, or a new corrective work order.

## Artifact Contract

For major artifacts, define enough of the contract up front:

- purpose;
- audience;
- canonical status;
- confidence lane;
- verification needed;
- acceptance bar;
- expiry or supersession rule.

This prevents random files from becoming accidental "final" outputs.

## Proportionality

These patterns are meant to reduce confusion, not create ceremony.

Use the lightest structure that preserves the next useful action:

- Tiny task: use JARVIS Core / Light Mode; skip Specialist Mode / Company Mode entirely.
- Small normal task inside an existing project: Light Mode plus a focused memory update only if durable state changed.
- Small-but-real project or focused adoption: Minimal Specialist Layer with current state, task board, one charter or adoption audit, and work orders; skip role memories, persistent role names, integration log, strategy map, evidence ledger, and adversarial review unless the project earns them.
- Simple Specialist Mode / Company Mode project: one-line shape inference, operating mode, normal task board, no optional artifacts.
- Excellence-critical project: shape inference, operating mode, compact Excellence Calibration, then execute against that bar.
- Serious uncertain project: shape inference, operating mode, confidence lanes, strategy map, and adversarial review or claim review for consequential results.
- Long-horizon project: periodic compression of operating mode, current state, dead ends, live artifacts, and next attacks.
