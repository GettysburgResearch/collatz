# Access and Permission Model

## Goal

The Collatz repository is intended to be unusually open to direct human–AI
research contribution while keeping `main`, canonical state, security settings,
and project-level resolution status under integrator control.

Use repository-specific teams for elevated access.

An organization base permission of `Read` is acceptable when all organization
members may see every current repository. Change the base permission to `None`
only if future private repositories should be isolated from ordinary Collatz
contributors.

## Public participation

Once the repository is public and Issues remain enabled, any GitHub user may:

- read and clone the repository;
- open and comment on Issues;
- comment on and review pull requests;
- participate in Discussions;
- fork the repository;
- push to their own fork;
- and open a pull request from a branch they control.

Public visibility alone does not grant direct push access to
`GettysburgResearch/collatz`.

## Requesting direct contributor access

Open the access-request Issue and provide only your GitHub username. An
organization owner may invite you to Gettysburg Research and add you to
`collatz-contributors`.

Access Issues use the `[Access]` title prefix. Close them after handling so they
do not remain mixed into the mathematical backlog. Agents searching for research
work should ignore `[Access]` Issues.

The one-field form is intentionally easy to automate later. At launch, invitations
remain owner-controlled. Do not place a high-privilege organization token in an
Issue-triggered workflow merely to automate membership. If request volume grows,
prefer a narrowly scoped GitHub App or an external form plus owner approval.

## `collatz-contributors` — Write

Members receive `Write` access to this repository only. They may:

- push agent branches;
- open and comment on Issues and PRs;
- apply labels and assign work;
- review and correct other contributions;
- continue long-running research PRs across multiple passes;
- and open new research programs without waiting for a predefined task.

GitHub's standard `Write` role also grants broad Issue and PR controls. Project
policy therefore requires contributors not to:

- update or merge into `main`;
- close or supersede another contributor's active PR;
- rewrite `STATE.md` or the canonical project status outside integration;
- delete or hide another contributor's durable research record;
- alter security-sensitive settings or workflows without review;
- or use repository CI as distributed mathematical compute.

Contributors may close their own Issues and PRs. Access may be removed for abuse.

## `collatz-integrators` — Maintain

Integrators perform dependency-aware sweeps, extract and merge stable artifacts,
maintain `STATE.md` and canonical claim metadata, reconcile stacks, and close or
supersede completed research PRs.

Only this team and organization owners should be allowed to update `main` or
protected integration branches.

Initially this team may contain only the founder.

## Organization owners — Admin

Owners handle invitations, access removal, installed Apps, secrets, security,
visibility, rulesets, and continuity. Keep this group small and include a trusted
backup owner when possible.

## Claiming work

Agents should normally comment on an Issue:

```text
CLAIMED BY: <agent-id>
STARTING COMMIT: <sha>
BRANCH: <branch>
APPROACH: <short plan>
```

Multiple independent attempts are allowed. Formal GitHub assignment is useful
but not required for the mathematical claim of work.

## Labels, assignments, comments, and reviews

Write contributors can help organize research by labeling and assigning Issues
and PRs. Agents are encouraged to comment across the repository with
corrections, objections, literature, computational checks, partial proofs,
dependency observations, and review findings.

Only integrators should close another contributor's active PR or mark it
superseded in the canonical record.

## Protecting `main`

The intended public configuration is:

```text
Target: main
Restrict updates
Restrict deletion
Require a pull request
Block force pushes
Bypass: collatz-integrators and organization owners only
```

If private-repository branch rules are unavailable on the current GitHub plan,
keep contributor Write access limited while private. Complete the baseline and
first integration pass, change visibility during a controlled unpublished setup
window, immediately activate the free public ruleset or protected branch, test
it, and only then grant broad contributor Write access and announce the project.

## AI applications

A contributor needs a write-capable authenticated environment to push a branch
or open a code PR. Capabilities vary among ChatGPT, Codex, Claude, Cursor, local
Git, and other connected tools. The agent acts with the connected GitHub user's
permissions.

Human setup and tool-specific advice belong in
[HUMAN_GUIDE_TO_AI_RESEARCH.md](HUMAN_GUIDE_TO_AI_RESEARCH.md).

## Actions and secrets

Before broad Write access:

- keep Actions disabled or allow only reviewed bounded workflows;
- keep repository secrets empty unless strictly necessary;
- use no public self-hosted runner;
- use read-only default workflow tokens;
- prevent Actions from approving pull requests;
- require explicit short job timeouts;
- and inspect installed Apps, deploy keys, webhooks, and tokens.

See [COMPUTE_POLICY.md](COMPUTE_POLICY.md) and the repository
[SECURITY.md](../SECURITY.md).
