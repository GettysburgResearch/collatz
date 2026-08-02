# Claim registry and status semantics

The registry is provenance infrastructure. Human mathematical exposition lives in [`../research/integrated/`](../research/integrated/README.md) and the wider source-pinned catalog is [`../research/RESULTS_CATALOG.md`](../research/RESULTS_CATALOG.md).

## Files

- [`registry.json`](registry.json) — schema, status vocabulary, and part index;
- [`registry/canonical-1.json`](registry/canonical-1.json) and [`registry/canonical-2.json`](registry/canonical-2.json) — eight durable integrated records;
- [`registry/roadmap.json`](registry/roadmap.json) — SC\*, FC\*, and the proposed bridge;
- [`CANONICAL.md`](CANONICAL.md) — compact human rendering;
- [`aliases.json`](aliases.json) — branch-qualified aliases, collisions, refutations, and repairs.

The registry does not replace proof files and does not upgrade a statement merely because it is resident.

## Independent status dimensions

`mathematical_status` says whether the exact statement is verified, source-qualified, empirical, proposed, open, refuted, or superseded.

`integration_status` says whether the record is a resident canonical reference, roadmap obligation, reference-only item, deferred item, or quarantined item.

`promotion_state` says whether the repository accepts the record as a reference, accepts it with local proof, accepts it as a roadmap, or retires it.

`proof_residency` says whether a readable proof packet is local, remains only at a frozen source, is an open obligation, or is historical.

`dependency_residency` says whether the load-bearing dependencies are local, source-pinned, or mixed.

These fields must not be collapsed. Examples:

```text
mathematical_status = verified
promotion_state     = accepted_with_local_proof
proof_residency     = local_proof_packet
```

means the exact reviewed result is accepted and its proof is readable locally.

```text
mathematical_status           = source-qualified
component_mathematical_status = verified_at_exact_source_shas
integrated_statement_status   = pending_narrow_review
promotion_state               = accepted_reference_record
proof_residency               = local_proof_packet
```

is the durable status of `IC-PERIODIC-001`: its component proofs are reviewed and resident, while the exact combined wording still needs one narrow review.

A refutation may be `accepted_with_local_proof` while its `mathematical_status` is `refuted`; that means the refutation is an accepted result, not that the false theorem became verified.

## Minimum integrated record

A durable record states:

- exact claim and scope;
- exclusions and finite-to-infinite boundary;
- source PR, source SHA, source claim IDs, and source paths;
- exact review report and verdict;
- dependencies and dependency residency;
- proof and artifact evidence;
- aliases and repair/supersession relations;
- local packet when resident.

## Identifier rule

Never cite a colliding bare ID such as `T-7401`. Use `PR<number>:<claim-id>` or the repository record ID. Source files are not silently renamed.

## Roadmap boundary

`RD-SC-001` and `RD-FC-001` are accepted **open obligations**. `RD-BRIDGE-001` is an accepted **PROPOSED** roadmap record whose exact least-counterexample crosswalk remains pending narrow review. None is a proof of Collatz.
