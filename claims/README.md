# Claim registry

The registry is a hybrid:

- [`registry.json`](registry.json) is the machine-readable source of integrated claim metadata.
- [`CANONICAL.md`](CANONICAL.md) is the human-readable rendering.
- [`aliases.json`](aliases.json) records branch-qualified aliases, collisions, repairs, refutations, and supersessions.

The registry does not replace proof files. It points to proof-bearing source PRs at exact commits and records what was actually reviewed.

## Two orthogonal statuses

`mathematical_status` answers whether the statement is verified, source-qualified, empirical, proposed, open, refuted, or superseded.

`integration_status` answers whether the record is canonical, roadmap, reference-only, deferred, or quarantined.

A mathematically verified claim may remain deferred because its dependency chain, namespace, source normalization, or current-head delta is not ready. A canonical refutation is still `refuted` mathematically.

## Minimum canonical record

A canonical record states:

- the exact claim and scope;
- exclusions and finite-to-infinite boundary;
- source PR, source SHA, source claim IDs, and source paths;
- review report, reviewer scope, and verdict;
- dependencies;
- proof and artifact evidence;
- aliases and repair/supersession relations.

## Identifier rule

Never cite a bare colliding ID such as `T-7401`. Use the branch-qualified source form, for example `PR61:T-7401`, or the canonical integrated ID. Source files are not silently renamed.
