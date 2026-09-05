# Contributing

The repository supports free exploration and a narrow integration layer.

## Explore freely

Broad research PRs, informal notes, experiments, countermodels and changes of direction are welcome. Before publishing, make visible the exact map and normalization, each load-bearing claim's status, the finite/all-depth and ordinary/2-adic boundary, and the unresolved step. No registry form is required to explore.

Computation that matters needs a frozen artifact, replay command and an honest statement of whether it was independently replayed. Use the [replay policy](docs/REPLAY_POLICY.md); historical generators may overwrite reports, and optimized Python is not automatically supported.

## Request review

Supply the exact commit, load-bearing claims/files, dependencies and source-qualified inputs, checker/artifact state, and known doubts/repairs. A verdict applies only to that SHA and exact statement; a branch may contain passing, failed, conditional and unreplayed items.

## Request integration

Integration is an additional contract, not a prerequisite for exploration. Supply statement and scope; source identity; dependencies and normalization; exact review and verdict; proof/artifact residency and replay state; and refutation, repair, alias or supersession relations.

An integrator may extract a coherent subset rather than merge a whole branch. A repaired theorem never changes the status of its false original. Follow [integration practice](docs/INTEGRATION_PRACTICE.md) for extraction, dependency repair, supersession, preservation and later closure.

## Identifiers and evidence

Use **(PR, full SHA, full repository path, claim ID)**. PR-only qualification is insufficient for the new same-branch collisions. [aliases.json](claims/aliases.json) supplies stable display namespaces; historical short aliases remain valid only when a canonical record resolves them uniquely. Repository IDs are aliases, not silent renames.

Keep proof inspection, independent reconstruction, artifact inspection, regeneration, checker execution, complete encoded-corpus replay, large external replay, not-replayed and missing-artifact states distinct. New wrappers, amended normalization and proposed replacements have separate receipts.

## Repository changes

Use branches and reviewable PRs. Do not change visibility, permissions, branch protection or public-release status from a research contribution. Do not add GitHub Actions without an explicit infrastructure decision. [Public-launch gates](docs/PUBLIC_RELEASE_GATES.md) are owner decisions, not claims implicitly cleared by research integration.
