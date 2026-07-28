# Agentic Polymath #1 Public Launch Checklist

## Ownership and backup

- [x] Organization and repository transfer completed
- [ ] Trusted backup human owner added
- [ ] Two-factor authentication required for members
- [ ] Repository mirror backup stored
- [ ] Portable Git bundle tested
- [ ] Frozen pre-public tag verified
- [ ] Issue and PR registries exported

## Publication audit

- [ ] All branch history inspected
- [ ] Secrets and credentials scanned and removed from history
- [ ] Actions logs and artifacts inspected
- [ ] Releases and attachments inspected
- [ ] Commit author emails reviewed
- [ ] Copyright and redistribution rights reviewed
- [ ] Personal, employer, and proprietary material reviewed
- [ ] Installed Apps, deploy keys, webhooks, and tokens reviewed
- [ ] Audit report committed

## Public operating baseline

- [ ] PR #74 reviewed and merged without mathematical claim promotion
- [ ] Comprehensive Agentic Polymath README
- [ ] Historical original README preserved
- [ ] `STATE.md`
- [ ] `ROADMAP.md`
- [ ] `CONTRIBUTING.md`
- [ ] `AGENTS.md`
- [ ] `GOVERNANCE.md`
- [ ] Research and integrator protocols
- [ ] Human steering guide
- [ ] Data and compute policies
- [ ] Claim registry and examples
- [ ] Pull-request template
- [ ] Exploration, task, verification, and access-request Issue templates
- [ ] Security policy
- [ ] Code of conduct
- [ ] License
- [ ] `CITATION.cff`

## Access and teams

- [ ] Organization base permission set to `None`
- [ ] `collatz-contributors` created with Write on this repository only
- [ ] `collatz-integrators` created with Maintain on this repository
- [ ] Only founder initially in `collatz-integrators`
- [ ] Broad contributor Write access withheld until `main` is protected
- [ ] CODEOWNERS team slugs verified and file activated
- [ ] Access-request workflow tested

## Backlog and first integration

- [x] Pre-existing open PRs frozen by exact SHA
- [x] Explicit dependency stacks mapped
- [ ] Giant umbrella PRs classified
- [ ] Independent reviews identified
- [ ] First synthesis sweep completed
- [ ] First adversarial sweep completed
- [ ] Canonical `STATE.md` populated
- [ ] No mathematical status silently promoted
- [ ] Stable packets selected or extracted

## Actions and compute

- [x] Actions temporarily disabled by owner
- [ ] Decision made to remain disabled or enable only reviewed bounded workflows
- [ ] Default workflow token read-only
- [ ] Actions cannot approve pull requests
- [ ] Selected actions only
- [ ] Explicit short timeouts
- [ ] No secrets exposed to untrusted code
- [ ] No public self-hosted runner
- [ ] No scheduled or distributed mathematical search

## Protecting `main`

Desired configuration:

- [ ] Restrict updates
- [ ] Restrict deletion
- [ ] Require pull request
- [ ] Block force pushes
- [ ] Bypass limited to `collatz-integrators` and organization owners
- [ ] `integration/**` protected where practical

When private protection is unavailable on the current plan:

- [ ] Keep broad Write access disabled while private
- [ ] Finish baseline, audit, and first integration pass
- [ ] Change visibility during an unpublished controlled setup window
- [ ] Immediately activate public branch protection or a ruleset
- [ ] Test that a contributor cannot update `main`
- [ ] Only then grant contributor Write access and announce the project

## Contributor experience

- [ ] Actual labels created from `LABELS.md`
- [ ] Open-expedition Issues seeded
- [ ] Focused starter tasks seeded
- [ ] Verification tasks seeded
- [ ] Literature tasks seeded
- [ ] Formalization tasks seeded
- [ ] Cartography and organization tasks seeded
- [ ] Worked example contribution
- [ ] Outside-account Issue test
- [ ] Outside-account fork PR test
- [ ] Direct contributor branch test
- [ ] Phone workflow test
- [ ] Connected-agent README and Issue test
- [ ] Visible `UNSOLVED` notice

## Controlled public launch

- [ ] Repository made public only after all pre-public work above
- [ ] Ruleset or branch protection immediately activated and rechecked
- [ ] Actions, Apps, logs, branches, releases, and attachments rechecked publicly
- [ ] ChatGPT, Claude, Cursor, and Codex repository access rechecked
- [ ] Public Issue, fork PR, and access-request flows tested
- [ ] First integration practice documented
- [ ] Reddit post published
- [ ] X thread published
