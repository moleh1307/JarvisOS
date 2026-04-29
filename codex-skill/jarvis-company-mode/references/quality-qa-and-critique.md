# Quality, QA, And Internal Critique

Use this reference for user-facing apps/sites/docs, design/product quality, QA, artifact readiness, and milestone review.

## Quality Bar

Company Mode should not optimize for "barely works."

Default expectations:

- Functional correctness is necessary but not sufficient for user-facing products.
- User review is not a substitute for internal QA.
- Design polish, UX clarity, empty states, visual hierarchy, and actual packaged/rendered behavior matter.
- Roles identify weak parts and create improvement work orders without waiting for the user.
- Roles critique the order itself when following it would produce weaker work.
- Founder reshapes plan, scope, team, or approach when evidence says the current path is wrong.
- "Done" means verified and ready for the next internal or external gate, not simply written.
- Milestones are internally accepted by the company when the responsible roles, QA, and Founder/Chief of Staff agree the charter criteria are met.

Founder must not mark the whole project as finally closed or stop the company just because internal checks pass. Internal milestone acceptance is allowed; final stop/closure, public release, or owner-level product acceptance requires user approval or explicit stop/release instruction.

## Tool-Aware QA Gate

If a tool can verify the work, use it before involving the user.

For user-facing apps, websites, documents, decks, images, or packaged artifacts:

- QA tests the actual artifact, not only source files or build scripts.
- Use available tools such as Computer Use, browser testing, screenshots, renderers, test scripts, package launch commands, or file inspection.
- For craft-critical or signature work, load `references/creative-preproduction.md` and run screenshot-based Design QA against the art direction brief, not only functional QA.
- Apps: launch packaged app when feasible, inspect visible UI, exercise core flows, quit/reopen when persistence matters, and record evidence.
- Websites: inspect rendered page, key responsive states, navigation, forms/interactions, and console/build errors when feasible.
- Documents/decks/PDFs: render/open enough pages to confirm artifact is not corrupt and layout/content are credible.
- Do not ask the user to perform basic QA that tools can perform.

User review is not a routine milestone gate. After internal tool-based QA and critique pass, the company should normally mark the milestone internally accepted and continue to the next useful task.

Ask the user for review only when:

- the user explicitly asked to review before continuing;
- the company needs final stop/closure or public release acceptance;
- the choice changes strategic product/research direction;
- credentials, cost, destructive work, or external publication is involved;
- subjective owner preference is truly blocking and cannot be inferred from the charter, prior feedback, or project goals.

Before any external review, release, or handoff, complete safe cleanup and packaging hygiene that the team itself caused or can verify:

- remove isolated agent-created QA/demo records from the review build or database;
- rebuild/repackage after source changes;
- verify the exact app/bundle/export the user will open;
- update README/status/limitations so the repo is understandable;
- push the verified baseline when a GitHub repo is configured and no sensitive/protected/release blocker exists.

Do not ask the user to approve cleanup of the team's own isolated smoke-test records. Ask only if cleanup could delete or overwrite real user data.

## Internal Critique And Acceptance Loop

Before a milestone is internally accepted, run a short critique:

- What is the weakest part?
- What would a top-tier version improve?
- What non-obvious move would make this meaningfully better?
- What are we assuming only because it is conventional?
- What would a world-class specialist challenge?
- What should be fixed before internal acceptance?
- Are there hidden verification gaps?
- Should the next task be polish, QA, packaging, documentation, research validation, or release preparation?

If obvious quality gaps exist, create new work orders and continue. Do not wait for the user to say "improve UI" or "make it better" when the gap is visible.

For craft-critical or signature work, internal critique must include the Creative Preproduction generic UI kill switch. If the artifact looks generic, template-like, gradient/card-heavy without product reason, default component-library shaped, or disconnected from the product metaphor, reject internally and re-enter Creative Preproduction.

If no internal blockers remain, Founder/Chief of Staff may record `internally accepted` and immediately create or start the next milestone/work order.

## Role-Accurate Reporting

Use the role header that matches the work being reported:

- Single-role work: report as the executing role.
- Multi-role or cross-functional completion: report as Chief of Staff after reading the touched work orders and role memories.
- Product direction or milestone acceptance: report as Founder or Chief of Staff.
- QA evidence and release checks: report as QA / Release.
- Native/runtime implementation: report as the relevant engineer role.

If a task changes role midstream, switch headers at the transition. Do not let one specialist claim broad implementation, QA, release, and product decisions outside its scope. The point of Company Mode is role separation; reports should preserve that separation.

## Product Judgment Check

After multiple consecutive QA/infrastructure tasks, Founder or Chief of Staff should check whether the company is improving the project or only adding confidence machinery. Route the next task toward product/design/research value when that is higher leverage than another test layer.

## Acceptance And Stop Rule

Founder may declare:

- `internally accepted`;
- `no internal blockers found`.
- `continuing to next milestone`;

Founder must not declare:

- final user accepted;
- project complete;
- company paused/closed because the milestone is done;

unless the user explicitly approves or asks to stop.
