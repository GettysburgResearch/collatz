# Claim registry

The registry is a hybrid:

- [`registry.json`](registry.json) is the machine-readable index and status vocabulary.
- [`registry/canonical-1.json`](registry/canonical-1.json), [`registry/canonical-2.json`](registry/canonical-2.json), and [`registry/roadmap.json`](registry/roadmap.json) hold the full records.
- [`CANONICAL.md`](CANONICAL.md) is the human-readable rendering.
- [`aliases.json`](aliases.json) records branch-qualified aliases, collisions, repairs, refutations and supersessions.
- [`../docs/integration/2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md`](../docs/integration/2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md) records how frozen source proofs should become durable local packets.

The registry does not replace proof files. It points to proof-bearing source PRs at exact commits and records what was actually reviewed.

## Four orthogonal statuses

`mathematical_status` answers whether the statement is verified, source-qualified, empirical, proposed, open, refuted or superseded.

`integration_status` answers the intended repository role: canonical, roadmap, reference-only, deferred or quarantined.

`promotion_state` answers whether that role is merely selected in a draft or accepted on main.

`proof_residency` answers whether the proof is still only at a frozen source commit or has a durable local proof packet.

These fields must not be collapsed. For example:

```text
mathematical_status = verified
integration_status  = canonical
promotion_state     = candidate_in_draft_pr
proof_residency     = frozen_source_reference
```

means that the underlying statement passed exact-SHA review, an integrator selected it for canonical use, but the integration PR is unmerged and the proof body is not yet local to main.

## Promotion states

- `candidate_in_draft_pr` — selected by an unmerged integration draft.
- `accepted_reference_record` — accepted on main as a registry/reference record.
- `accepted_with_local_proof` — accepted on main with a durable proof packet.
- `roadmap_candidate_in_draft_pr` — selected roadmap record in an unmerged draft.
- `roadmap_accepted` — accepted roadmap/obligation on main; the obligation remains unsolved.
- `retired` — no longer active, with a migration or supersession record.

PR #84 currently uses candidate states. It must not self-certify its own independent review.

## Minimum canonical record

A candidate or accepted canonical record states:

- the exact claim and scope;
- exclusions and finite-to-infinite boundary;
- source PR, source SHA, source claim IDs and source paths;
- review report, reviewer scope and verdict;
- dependencies;
- proof and artifact evidence;
- aliases and repair/supersession relations;
- promotion state and gate;
- proof residency and import plan.

## Identifier rule

Never cite a bare colliding ID such as `T-7401`. Use the branch-qualified source form, for example `PR61:T-7401`, or the canonical integrated ID. Source files are not silently renamed.

## Roadmap bridge

`RD-BRIDGE-001` records `SC* + FC* => Collatz` as a **proposed** normalization/crosswalk theorem. Reviewed lane components exist, but the combined repository-level implication still needs narrow independent review. See [`SC_FC_BRIDGE.md`](../docs/integration/2026-08-02-lifecycle/SC_FC_BRIDGE.md).
