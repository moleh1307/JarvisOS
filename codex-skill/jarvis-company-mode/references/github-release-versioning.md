# GitHub, Release, And Versioning

Use this reference for coding projects, git, GitHub, PRs, releases, tags, version files, and repo readiness.

## Coding Project Defaults

For coding projects:

- reliable milestones should be committed to git;
- work normally gets pushed to the user's GitHub repository when configured;
- app/package versions should be bumped after reliable meaningful milestones when version metadata exists;
- if no repo exists, create a work order to initialize one or ask when repo naming/remote creation matters;
- in Adoption Mode, inspect existing remotes/branches before changing git configuration;
- role/task branches use `agent/<role-slug>/<task-id-or-short-slug>`;
- commits use role-specific author metadata with the user's verified email when known.

Do not change global git identity for each role. Prefer per-commit `--author` or `GIT_AUTHOR_NAME` / `GIT_AUTHOR_EMAIL`.

## GitHub Autonomy

- If a repo and remote already exist, the current branch is a role/task branch, verification passed, and no sensitive/private data risk exists, the executing role may push the branch and open/update a PR without asking.
- If the user provides a GitHub repo URL for a new coding project, treat that as authorization to configure the remote and push a clean README-backed baseline after verification unless the user explicitly says local-only or there is a concrete sensitive-data/protected-branch blocker.
- PRs are internal review artifacts unless the project explicitly says otherwise.
- If a role opens a PR, the reviewer role should review it, request fixes if needed, and merge after internal acceptance.
- Do not leave a draft PR waiting for the user unless there is a real product, release, secret, cost, or strategic decision.
- After internal acceptance, merge the role/task branch to `main` and push `main` when project policy allows and no protected-branch/destructive/sensitive risk exists.
- Ask before creating/changing a remote, pushing directly to a protected/default branch when policy is unknown, publishing a release/tag/package, changing repo visibility/settings, force-pushing, deleting branches, or pushing secrets/private memory.

If a project is already explicitly waiting for the user because an escalation rule applies, do not use "needs approval" as a generic stop sign. State the exact decision needed: release approval, credential/cost approval, destructive action approval, scope choice, or explicitly requested user review.

Do not confuse public repo baseline with final product acceptance. A verified baseline can be pushed to `main` while the app remains internally active or internally accepted, as long as README/status/limitations are honest and private Specialist Mode / Company Mode memory is not pushed.

Project-scoped GitHub/QA dependencies such as test runners, browser testing packages, and official framework plugins are normal coding-project work. Do not turn them into GitHub/release approval gates unless they introduce external services, secrets, paid usage, telemetry/cloud runtime behavior, protected-branch risk, or unusual system-level impact.

## PR Body

PRs should include:

- role owner;
- reviewer role;
- task ID;
- scope;
- verification performed;
- screenshots or visual evidence for user-facing changes when feasible;
- version change and docs updated, if any.

## Repo Readiness

Before first GitHub push intended as project handoff, the repo must include `README.md`.

For coding projects, README should include:

- what the project is;
- current status;
- setup/run/build/test instructions;
- known limitations;
- where Specialist Mode / Company Mode state lives if relevant.

Include `.gitignore` when the stack produces local dependencies/build output. Do not treat a GitHub repo as shipped or handoff-ready while GitHub shows "Add a README" unless the absence is explicitly justified.

If `company/` is kept private/ignored, the README should say where local Specialist Mode / Company Mode state lives and whether it is intentionally excluded from the public repo.

## Version Visibility

If any role changes internal project version, release version, package version, app version, public template version, or Specialist Mode / Company Mode workflow version, visible project docs must change in the same task or commit.

Default targets:

- `README.md` for visible version/current note when no changelog exists;
- `CHANGELOG.md` when the project has or should have change history;
- `VERSION` or package metadata such as `package.json` / `pyproject.toml` when present;
- `company/current-state.md` and the relevant work order for internal state.

Do not only update memory or mention the version in chat. A future user opening the repo should see the version and understand what changed.

For non-coding projects, use equivalent reproducible artifacts: dated outputs, canonical folders, validation notes, and clear supersession.
