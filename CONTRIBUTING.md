# Contributing

The repository supports free exploration and a narrow integration layer.

## Join and start

1. [Request contributor access](https://github.com/GettysburgResearch/collatz/issues/new?template=contributor-access.md) with just your GitHub username.
2. Accept the invitation to GettysburgResearch; a maintainer adds you to `polymath-contributors`.
3. Connect your agent using the [phone tutorial](docs/PHONE.md), or work through your preferred GitHub tools.
4. Read [README.md](README.md) and [AGENTS.md](AGENTS.md), choose your question, check overlapping work, and open a PR from your own branch.

Public contributors can also use a fork and PR without joining the organization. New directions and unfinished exploratory work are welcome; see the [review guide](docs/REVIEWING.md) for giving or requesting feedback.

Keep contributions public-safe: omit credentials and private personal information, and credit others by their chosen public name or GitHub username.

## Roles and responsibilities

Our intended division of access and responsibility is:

| Group | Access and responsibility |
|---|---|
| Contributors | Write access for research branches and PRs; review one another's work. Public fork contributions are also welcome. |
| Integrators | Write access plus permission to merge reviewed PRs into main; preserve claim status, dependencies and review scope. Repository Admin access is not needed. |
| Owners | Manage membership, settings and exceptional interventions; keep this group small. |

Owners configure GitHub permissions and branch protections separately; this table describes the working policy.

Interested in helping integrate? After contributing research, reviews or a small integration PR, [request integrator access](https://github.com/GettysburgResearch/collatz/issues/new?template=integrator-access.md) with your GitHub username. A maintainer reviews your contribution history and grants access when you are ready.

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

## Contribution license

By submitting a contribution, you agree to license your original contribution under the [MIT License](LICENSE). Only include material you have the right to contribute; preserve third-party licenses, notices, and attribution.
