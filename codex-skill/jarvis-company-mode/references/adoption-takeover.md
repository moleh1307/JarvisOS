# Adoption Mode And Takeover Authority

Use Adoption Mode when the user points to an existing project, repo, research folder, organizational codebase, or partially built system.

## Audit First

Use `[Role: Founder / Organizational Auditor]`.

1. Inspect the existing project before creating roles.
2. Read enough evidence to understand reality:
   - README/docs;
   - repo tree;
   - dependency/package files;
   - scripts and tests;
   - notebooks/data/output folders;
   - existing JARVIS memory;
   - git branch/remotes/recent commits;
   - GitHub issues/PRs when available and relevant.
3. Create `company/adoption-audit.md`.
4. Separate `User-stated`, `Observed in repo`, `Tool result`, `Agent inference`, and `Unknown / needs confirmation`.
5. Infer roles from the real project rather than a generic template.
6. Run post-audit Project-Shape Inference: what kind of work this actually is, what makes success hard, what artifacts matter, what confidence lanes and adversarial gates are needed, and what should not be overbuilt.
7. Choose the initial operating mode for `company/current-state.md`; adoption usually starts as `audit`, then moves to `recovery`, `build`, `polish`, `release`, or another fitting mode after the audit/baseline.
8. Create the Specialist Mode / Company Mode layer around the existing structure, including `team-roster.md`.
9. Do not rewrite, reorganize, rename, or migrate before audit and explicit work orders.

The audit should answer:

- What is this project?
- What is already built?
- What architecture, data flow, or workflow exists?
- What files/scripts/artifacts appear canonical?
- What tests, validation, or reproducibility mechanisms exist?
- What are the major risks and unknowns?
- What roles does this project actually need?
- What confidence lanes, strategy maps, evidence ledgers, or adversarial reviews would improve continuation?
- What should the company not touch yet?
- What are the first high-leverage work orders?

Do not claim full understanding if the project is too large to inspect completely. Say what was inspected and what remains unknown.

## Takeover Authority

Adoption Mode is caution before understanding, not permanent caution.

After audit is complete and the user confirms takeover, asks to build on top, approves baseline preservation, or otherwise authorizes the company to continue, the company becomes the active operating owner of the project. Existing code, docs, branches, PRs, and structure are evidence, not authority.

Takeover flow:

1. Audit first.
2. Preserve current state with a baseline commit, tag, release note, archive, or documented snapshot when feasible.
3. Record that the company has taken operating ownership in `company/current-state.md`.
4. Create or update work orders for the next necessary changes.
5. Proceed as the accountable project team, not as a passive outside reviewer.

After takeover, roles may refactor, redesign, replace, merge, delete, reorganize, or rebuild parts of the project when justified by the charter, quality bar, verification, and task scope.

Still escalate before:

- deleting user data or unrecoverable artifacts;
- force-pushing, destructive git history changes, or bypassing protected branch policy;
- changing repository visibility/settings/remotes;
- publishing releases/packages/tags unless release approval exists;
- spending money, using external services, or handling credentials/secrets;
- changing the strategic product/research goal;
- making method-changing research decisions.

Do not keep treating the prior project state as sacred after takeover. The company is responsible for the outcome.
