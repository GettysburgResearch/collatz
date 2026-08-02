# Contributing

The repository supports free exploration and a narrow integration layer.

## Explore freely

Broad research PRs, informal notes, experiments, countermodels, and changes of direction are welcome. Before publishing, make four things visible:

1. the exact map and normalization;
2. the status of each load-bearing claim;
3. the finite-versus-all-depth and 2-adic-versus-ordinary boundary;
4. the unresolved step.

Computation that matters should have a frozen artifact, a replay command, and an honest statement of whether it was independently replayed.

## Request review

Give the reviewer:

- the exact commit to freeze;
- the load-bearing claims and files;
- dependencies and source-qualified inputs;
- artifact/checker state;
- known doubts, repairs, and supersessions.

A review verdict applies only to that SHA. A branch-level verdict may contain passing and failing claims.

## Request integration

Integration is a lightweight additional contract, not a prerequisite for exploration. Supply:

```text
statement and exact scope
source PR, SHA, claim IDs, and paths
dependencies and normalization
review report and verdict
proof/artifact residency and replay state
refutation, repair, alias, or supersession relations
```

An integrator may extract a coherent subset rather than merge the whole PR. A repaired theorem never changes the status of the original.

## Identifiers and evidence

Use branch-qualified source IDs such as `PR61:T-7401` when collisions exist. Repository IDs are aliases, not silent renames.

Keep these evidence states distinct: proof inspected, independently reconstructed, artifact inspected, artifact regenerated, checker run, large computation independently replayed, computation not replayed, and artifact missing.

## Repository changes

Use branches and reviewable PRs. Do not change visibility, permissions, branch protection, or public-release status from a research contribution. Do not add GitHub Actions without an explicit infrastructure decision.
