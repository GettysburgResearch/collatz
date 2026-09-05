# Contributing

The repository supports free exploration and a narrow integration layer.

## Join and start

Read the [research map](docs/RESEARCH_MAP.md), choose a question, and check overlapping issues and PRs. A new research direction does not need a registry entry or formal proposal.

For direct repository access, [request contributor access](https://github.com/GettysburgResearch/collatz/issues/new?template=contributor-access.md) with your GitHub username and the project you want to work on. While the repository is private, contact the maintainer who invited you if you cannot open it. An owner or authorized maintainer handles team membership; accept any GitHub invitation. No private email address, biography or research proposal is required. Once public, a fork and PR provide a contribution route without joining the organization.

Use your own branch and open a PR. Leave `main`, other contributors' branches and frozen research records to the integration process. Follow the [phone tutorial](docs/PHONE.md), [agent guidance](AGENTS.md), and [shared review guide](docs/REVIEWING.md).

Commit public-safe material: no credentials, private chat transcripts, personal contact details or secret local configuration. Credit contributors by their chosen public name or GitHub username; ordinary scholarly citations are welcome.

## Explore freely

Research notes, experiments, counterexamples and useful failed attempts are contributions. Make the exact map and normalization, claim status, finite/all-depth and ordinary/2-adic boundaries, evidence level and first unresolved step visible. Computation that matters needs a frozen artifact, a replay command and an honest account of what was independently checked.

## Request review

Give the reviewer the exact commit, load-bearing claims and dependencies, known doubts, and the artifact/checker state. A verdict applies only to that SHA and scope. A mixed branch can contain passing, refuted, conditional and unreviewed claims simultaneously.

## Request integration

Supply the statement and exact scope; `(PR, full SHA, path, claim ID)`; dependencies and normalization; review report and verdict; proof/artifact residency and replay state; and refutation, repair or supersession relations. The full path is required because different files in the same PR can reuse an ID. Repository aliases do not silently rename source claims.

An integrator may extract a coherent subset rather than merge the whole PR. A repair receives a distinct identity; it never retroactively verifies the original. Use [integration practice](docs/INTEGRATION_PRACTICE.md) for extraction, dependency handling, preservation and source-PR closure. This contract is not a prerequisite for exploration.

## Validate a contribution

Use `python -X utf8 -B tools/validate.py` in a clean complete checkout, with `--regressions` when bounded arithmetic replay is appropriate. See [replay policy](docs/REPLAY_POLICY.md) for receipt output and individual commands. The validator intentionally refuses dirty or incomplete checkouts; preserve your working changes and use another clean checkout rather than discarding work.

Preserve byte-exact frozen evidence. Do not regenerate a canonical report in place or renormalize an archive to make an integrity test pass. A changed artifact or checker needs its own provenance and review boundary. Historical checks remain historically scoped.

## Repository changes

Use branches and reviewable PRs. Changes to checkers, automation, access rules, licensing or visibility need explicit authority and review appropriate to their consequences. The integrity workflow is read-only and is not permission to run privileged contributed code. Never expose repository secrets to an untrusted research program. A new research contribution does not authorize settings, membership or public-release changes.
