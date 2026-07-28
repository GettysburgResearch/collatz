# Publication Readiness

Last audited: 2026-07-29

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

- comprehensive Agentic Polymath #1 README using the original protocol as its
  structural base;
- `PROJECT STATUS: UNSOLVED` and a proof-or-disproof mission;
- original `Do not fear confabulation` note with visible epistemic labels;
- compact human quick start with access, app setup placeholders, phone workflow,
  and starter prompts;
- agent-selected persistent IDs;
- Issues as broad agent-readable research workspaces;
- expected Issue creation and claims of work;
- active commenting, correction, and review across other Issues and PRs;
- long-lived multi-pass research PRs and exact-SHA review semantics;
- open-problem continuation rule;
- human circular-loop steering guidance;
- original `D/Q/O/C/K/L/T/X/R/M` claim prefixes and established status
  vocabulary;
- ordinary-integer and full-denominator warnings;
- selective formalization guidance;
- CI/CD policy: bounded validation, not distributed mathematical compute;
- external data and artifact provenance policy;
- repository-specific `collatz-contributors` / `collatz-integrators` access
  model;
- initial two-sweep GPT-5.6 Pro integration practice;
- state and roadmap scaffolds;
- Issue and PR templates, including a concise access-request form;
- security, conduct, data, compute, and integration policies;
- preliminary dependency-aware PR backlog.

## Owner actions still required before public announcement

1. Review and merge PR #74 without promoting any mathematical claim.
2. Confirm a tested mirror/bundle backup and permanent pre-public tag.
3. Complete a secrets, privacy, copyright, branch, Actions-log, release,
   attachment, and commit-email audit.
4. Choose and add a project license and `CITATION.cff`.
5. Create and verify organization teams:

   ```text
   collatz-contributors  -> Write on this repository only
   collatz-integrators   -> Maintain on this repository
   organization base     -> None
   ```

6. Keep broad contributor Write access disabled until `main` has server-side
   protection.
7. Require two-factor authentication for organization members and keep only the
   founder plus a trusted backup as owners.
8. Verify installed App scopes for ChatGPT, Claude, Cursor, Codex, and any other
   GitHub Apps.
9. Rename `.github/CODEOWNERS.example` to `.github/CODEOWNERS` after the team
   slugs exist and verify review routing.
10. Keep Actions disabled or configure only selected bounded workflows with
    read-only tokens, explicit timeouts, no PR approval, no secrets exposed to
    untrusted code, and no self-hosted public runner.
11. Configure `main` protection:

    ```text
    Restrict updates
    Restrict deletion
    Require pull request
    Block force pushes
    Bypass only collatz-integrators and organization owners
    ```

12. If the private organization repository cannot use rulesets or protected
    branches on the current plan, do not grant broad Write access while private.
    Complete the integration pass, change visibility in a controlled unpublished
    setup window, immediately activate free public branch protection, test it,
    and only then add contributors and announce the repository.
13. Run the first mathematical integration pass and populate `STATE.md` from
    exact source SHAs.
14. Create the actual labels listed in `LABELS.md`.
15. Seed open expeditions, focused tasks, verification requests, literature
    tasks, formalization tasks, and organization tasks.
16. Change visibility to public only after the integration and owner-controlled
    setup are complete.
17. Recheck rulesets, Actions, Apps, logs, branches, releases, Issues, access
    requests, fork PR flow, and direct contributor branch flow from an external
    account before posting publicly.

## Not yet verified through the connector

- organization plan and billing tier;
- team existence, membership, and base permissions;
- two-factor-authentication enforcement;
- repository rulesets or branch protection;
- Actions organization- and repository-level settings beyond the owner's report
  that Actions are disabled;
- existence of a tested external backup or pre-public tag;
- publication audit completion;
- license selection;
- exact App permissions for Claude and Cursor;
- whether Claude and Cursor can consume GitHub Discussions.

## Discussions portability warning

The GitHub connector available to the current ChatGPT session exposes
repositories, Issues, pull requests, comments, files, and writes, but not GitHub
Discussions. Discussions may remain available for humans; actionable outcomes
must be mirrored into Issues, PRs, reports, or repository documents.
