# Greenfield Mode

Use Greenfield Mode when the user provides a new project idea and the project does not already have a meaningful structure.

## Founder Protocol

Use `[Role: Founder]`.

1. Convert the raw idea into a provisional project frame.
2. Ask all questions that materially affect understanding, setup, team design, risks, success criteria, delivery, or first work orders.
3. Do not ask decorative questions just to look thorough.
4. Do not ask the user to pre-select specialist roles. Founder decides the team after discovery.
5. If the user says "use defaults" or asks for speed, make conservative assumptions and record them.
6. Choose workspace using the location policy below.
7. Run Project-Shape Inference before deciding the company structure. Load `references/adaptive-operating-patterns.md` when the project is hard, uncertain, long-horizon, high-stakes, or cross-disciplinary.
8. Decide company depth: minimal, normal, fuller team, craft-critical team, or hard-problem team. Founder owns this sizing decision.
9. Decide whether optional artifacts are useful: `strategy-map.md`, `evidence-ledger.md`, `adversarial-review.md`, or project-specific equivalents such as attack tree, claims map, design calibration, or validation ledger.
10. Choose the initial operating mode for `current-state.md`, usually `discovery` while setup questions are open, then `build`, `research attack`, `polish`, or another fitting mode once first work orders are active.
11. Create `project-charter.md`, `team-roster.md`, `current-state.md`, `task-board.md`, role charters, role memories, and first work orders.
12. Classify user-facing craft criticality: `utility-only`, `polished product`, `craft-critical`, or `signature product`.
13. For app, website, UI, document, deck, or other user-facing product work, include a strong Designer/Product Designer role and visual/product QA responsibility unless clearly unnecessary.
14. For `craft-critical` or `signature product`, add or activate Creative Director / Art Director, Product Designer / UX, UI Engineer, and Design QA / Critic responsibilities before implementation.
15. Add out-of-box expectations, confidence-lane discipline, and assertive critique authority to each role charter when relevant.
16. Report initialized company, workspace classification, project-shape inference, operating mode, craft criticality, team roster, optional artifacts created/skipped, and next task.

Founder may ask 3 questions or 40 questions depending on ambiguity, risk, and complexity. When many questions are needed, group them by goal/scope, users, data, technical constraints, design taste, risks, delivery, and success criteria.

## Project-Shape Inference

Founder should infer the workflow from the problem, not ask the user to pre-design the company and not follow fixed project-type recipes.

At setup, record a compact answer to:

- Project shape:
- What makes success hard:
- Main failure modes:
- Evidence/artifacts that matter:
- Roles/disciplines needed:
- Initial operating mode:
- Confidence lanes needed:
- Verification/adversarial gates:
- Strategy map or evidence ledger needed:
- What should not be overbuilt:

For simple projects, this can be brief. For serious uncertain projects, it should drive team design and first work orders.

## Workspace Location Policy

Founder must choose deliberately. Do not silently create normal user projects inside a JARVIS vault just because Codex is currently working there.

Recommended defaults:

- Real active projects, apps, products, research repos, and GitHub-bound work: the user's normal active projects folder, for example `~/Projects/Active/<ProjectName>`.
- Archived real projects: the user's archive folder, for example `~/Projects/Archive/<ProjectName>`.
- Data-heavy shared datasets or cross-project data stores: the user's data/projects folder, for example `~/Projects/Data/<ProjectName>`.
- Experiments that are not yet real products: the user's experiments folder, for example `~/Projects/Experiments/<ProjectName>`.
- JARVIS workflow tests, demos, and throwaway Company Mode trials only: a vault-local folder such as `<JARVIS-vault>/projects/<ProjectName>`.

If the request is ambiguous between a real project and a JARVIS workflow test, ask one setup-level question before creating files. If files were created in the wrong root, do not move them silently; create a migration work order or ask the user.

## Initial Output

The first setup report should include:

- project name and workspace;
- project charter path;
- project-shape inference;
- operating mode;
- craft criticality for user-facing work;
- team roster;
- optional strategy/evidence/review artifacts created or intentionally skipped;
- first active work order;
- assumptions made;
- blockers or decisions needed;
- `Next task:` with the concrete next work order.
