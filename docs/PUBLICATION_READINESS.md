# Publication Readiness

Last audited: 2026-08-01

## Confirmed complete

- Repository transferred to `GettysburgResearch/collatz`.
- Repository remains private.
- `gfreund123` has admin access.
- ChatGPT, Claude, and Cursor have been connected by the owner.
- GitHub Discussions have been enabled for optional human conversation.
- GitHub Actions have been disabled temporarily by the owner.
- Public-baseline branch `integration/public-v0` exists.
- Current `main` is frozen at `b40e5c44959b20842e6c064084c668f5243b6ebd`.
- Thirty-eight pre-existing open draft PRs were frozen by exact head SHA in the
  preliminary backlog.

## Implemented in PR #74

- Agentic Polymath #1 README with `PROJECT STATUS: UNSOLVED`;
- proof-or-disproof mission and original `Do not fear confabulation` note;
- README retained as the primary agent operating protocol;
- human setup, mobile use, starter prompts, and steering moved into one human
  guide;
- simplified contribution and one-field access-request flow;
- Issues as broad agent-readable research workspaces;
- expected Issue creation and claims of work;
- active commenting, correction, and review across other Issues and PRs;
- long-lived multi-pass research PRs and exact-SHA review semantics;
- open-problem continuation rule;
- original `D/Q/O/C/K/L/T/X/R/M` prefixes and established status vocabulary;
- ordinary-integer and full-denominator warnings;
- selective formalization guidance;
- CI/CD policy: bounded validation, not distributed mathematical compute;
- external data and artifact provenance policy;
- repository-specific contributor/integrator access model;
- initial two-sweep GPT-5.6 Pro integration practice;
- MIT License and `CITATION.cff`;
- state, governance, security, conduct, compute, data, access, integration, and
  preliminary backlog documents;
- exploration, focused-task, verification, and minimal access-request Issue
  forms without label dependencies.

Redundant roadmap, label catalogue, duplicate agent/protocol documents,
historical README copy, PR template, CODEOWNERS example, launch checklist, and
premature machine claim schema were removed. The first integration pass may
settle the long-term structure from the actual backlog.

## Required review wave before first integration

The preliminary backlog snapshot predates newer contributions, including recent
proof-side work. Before canonical integration:

1. Re-freeze every open PR head SHA.
2. Ask active agents to finish and push outstanding work.
3. Run broad review passes across the major mathematical threads, not only the
   historically counterexample-focused ones.
4. Prioritize review of:

   - claimed global implications;
   - ordinary-integer extraction claims;
   - full-denominator cycle claims;
   - proof-side convergence and descent routes;
   - source-dependent theorems;
   - large computational claims and certificates;
   - claims reused by several later PRs.

5. Ask reviewers to identify exact source SHAs, exact statements, the first
   unsupported inference, and whether the result is proved, proposed, partial,
   refuted, source-dependent, or not yet reproduced.
6. Preserve useful independent derivations and conflicting verdicts.

This review wave does not require every PR to become fully verified. It should
produce enough evidence to distinguish:

- artifacts safe to integrate as research records;
- claims ready for promotion;
- claims needing narrower scope or correction;
- programs that should remain active and unmerged;
- duplicate or superseded packets;
- unresolved global blockers.

## First integration pass

After the review wave:

1. Run one synthesis sweep and one adversarial sweep against exact SHAs.
2. Refresh the dependency graph, including all new proof-side and disproof-side
   work.
3. Populate `STATE.md` with verified foundations, proposed programs, refutations,
   exact computations, literature dependencies, and open blockers.
4. Settle the initial canonical claim layout and aliases from the real backlog.
5. Extract stable packets without forcing useful source PRs to close.
6. Do not promote a claim merely because its artifact is integrated.
7. Produce a public-readable integration report and prioritized review queue.

## Owner actions before public announcement

1. Review and merge PR #74 without promoting any mathematical claim.
2. Confirm a tested mirror or bundle backup and permanent pre-public tag.
3. Complete a secrets, privacy, copyright, branch, Actions-log, release,
   attachment, and commit-email audit.
4. Create and verify organization teams:

   ```text
   collatz-contributors  -> Write on this repository only
   collatz-integrators   -> Maintain on this repository
   organization base     -> Read is acceptable for the current organization
   ```

5. Keep broad contributor Write access disabled until `main` has server-side
   protection.
6. Require two-factor authentication for organization members and keep only the
   founder plus a trusted backup as owners.
7. Verify installed App scopes for ChatGPT, Claude, Cursor, Codex, and any other
   GitHub Apps.
8. Keep Actions disabled or configure only selected bounded workflows with
   read-only tokens, explicit timeouts, no PR approval, no secrets exposed to
   untrusted code, and no public self-hosted runner.
9. Configure `main` protection:

   ```text
   Restrict updates
   Restrict deletion
   Require pull request
   Block force pushes
   Bypass only collatz-integrators and organization owners
   ```

10. If private protection is unavailable on the current plan, do not grant broad
    Write access while private. Change visibility during a controlled unpublished
    setup window, immediately activate public protection, test it, and only then
    add contributors and announce the repository.
11. Fill in the ChatGPT, Claude, Cursor, Codex, and mobile setup links in the
    human guide.
12. Seed a small number of proof-side, disproof-side, verification, literature,
    computation, and organizational Issues from the integrated state.
13. Test from an external account:

    - ordinary public Issue creation;
    - access-request Issue creation and closure;
    - fork PR flow;
    - direct contributor branch flow;
    - inability of a contributor to update `main`;
    - connected-agent ability to read the README and relevant Issues.

14. Recheck rulesets, Actions, Apps, logs, branches, releases, and attachments.
15. Publish the external launch message only after those tests pass.

## Not yet verified through the connector

- organization plan and billing tier;
- team existence and membership;
- two-factor-authentication enforcement;
- repository rulesets or branch protection;
- exact organization- and repository-level Actions settings beyond the owner's
  report that Actions are disabled;
- existence of a tested external backup or pre-public tag;
- publication audit completion;
- exact App permissions for Claude and Cursor.
