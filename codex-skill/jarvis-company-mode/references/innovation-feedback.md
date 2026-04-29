# Innovation Mode And Workflow Feedback

Use this reference for deep brainstorming, out-of-box thinking, and workflow feedback candidates.

## Selective Innovation Mode

Innovation Mode is deeper thinking for tasks where ordinary execution would likely produce generic, shallow, or locally optimal work.

Triggers:

- User-forced: the user asks for brainstorming, Innovation Mode, deep thinking, unique ideas, out-of-box ideas, or innovation.
- Role-invoked: a role decides the task deserves deeper ideation because of uncertainty, quality risk, strategic importance, creative upside, weak prior direction, or high reversal cost.

Use it when:

- product/design quality is weak, generic, or undifferentiated;
- there are many plausible approaches;
- the current plan feels conventional or low-leverage;
- the user asks for "make it better";
- project direction may be wrong;
- research method may be too narrow;
- implementation architecture will be hard to undo;
- there is a chance for a differentiated feature, method, or workflow.

For craft-critical user-facing work, Creative Preproduction is stronger than normal Innovation Mode. Load `references/creative-preproduction.md` when taste, originality, visual identity, public presentation, or repeated design rejection is central. Use Innovation Mode for concept thinking, but do not skip the required reference intelligence, art direction brief, divergent concepts, and screenshot-based Design QA.

Skip it for simple bug fixes, obvious small implementation, mechanical docs, urgent verification, speed-focused tasks, or blockers that brainstorming cannot resolve.

Required format when invoked:

```text
Innovation Mode: invoked / user-forced / skipped
Reason:
Problem:
Options:
1. Safe path
2. High-quality conventional path
3. Unusual but practical path
4. Bold differentiated path
5. Simplest path
Critique:
- value / risk / cost / originality / fit
Decision:
Action:
```

Implement the chosen path only when within scope and not consequentially risky. If too risky, expensive, irreversible, security-sensitive, method-changing, or release-quality-changing, create a proposal/work order and escalate.

## Compact Out-Of-Box Pass

When full Innovation Mode is not needed, each role still asks:

- What is the non-obvious improvement?
- What hidden risk are we missing?
- What could be simplified?
- What would make this more original, robust, or useful?
- What would a world-class specialist challenge?

Filter ideas through scope, feasibility, current milestone value, and project goals.

## JARVIS R&D Feedback Loop

Create feedback when a project reveals:

- behavior defect, such as passive acknowledgement, missing role identity, poor continuation, or bad routing;
- repeated workflow friction;
- missing role, rule, template field, or review gate;
- quality gap Company Mode should have caught;
- emergent pattern worth reusing;
- candidate eval scenario from real project interaction.

Use feedback sparingly. Do not file feedback for every one-off inconvenience or task-specific bug.

Feedback flow:

1. Project role records a compact feedback report in the project `company/` folder or work order.
2. Chief of Staff labels it `feedback-candidate`, not a new rule.
3. If it affects the JARVIS workflow itself, route to the maintainer/R&D project.
4. Maintainers triage as `reject`, `document-only`, `patch-skill`, `update-template`, `add-eval-scenario`, or `public-release`.
5. Only promoted feedback changes installed skills, public templates, README, or version numbers.

Feedback report should answer:

- What happened?
- Where did it happen?
- Why did workflow fail or succeed?
- Is this one-off, repeated, or high-impact?
- What change is proposed?
- What risk does the change introduce?
- How should it be verified?
