# Claim and provenance layer

The scientific front door is [`../CURRENT_KNOWLEDGE.md`](../CURRENT_KNOWLEDGE.md). Readable proofs live under [`../research/integrated/`](../research/integrated/README.md). This directory retains the structured claim, alias, and provenance layer used by integrators and tooling.

## Files

- [`CANONICAL.md`](CANONICAL.md) — concise human index of accepted reference and roadmap records.
- [`registry.json`](registry.json) — machine-readable registry index and vocabulary.
- [`registry/canonical-1.json`](registry/canonical-1.json) and [`registry/canonical-2.json`](registry/canonical-2.json) — full integrated-reference metadata.
- [`registry/roadmap.json`](registry/roadmap.json) — open and proposed roadmap records.
- [`aliases.json`](aliases.json) — branch-qualified aliases, collisions, repairs, refutations, and supersessions.

The registry complements proof packets; it does not replace them.

## Four orthogonal fields

### `mathematical_status`

What is known about the statement itself:

```text
verified
source-qualified
empirical
proposed
open
refuted
superseded
```

### `integration_status`

The intended repository role:

```text
canonical
roadmap
reference-only
deferred
quarantined
```

### `promotion_state`

Whether the repository has accepted that role:

- `candidate_in_draft_pr` — selected by an unmerged integration draft;
- `accepted_reference_record` — accepted on `main` as the repository reference statement;
- `accepted_with_local_proof` — accepted on `main` with a readable local proof or proof extract;
- `roadmap_candidate_in_draft_pr` — selected roadmap record in an unmerged draft;
- `roadmap_accepted` — accepted roadmap or obligation on `main`, whether or not it is solved;
- `retired` — no longer active, with a durable migration or supersession record.

Merged PR #84 accepted the initial eight `IC-*` reference records and three `RD-*` roadmap records. Round 1 adds local proof packets and advances proof residency where appropriate. `IC-PERIODIC-001` remains an accepted reference whose exact integrated synthesis is pending narrow review.

### `proof_residency`

Where the proof or obligation lives:

- `frozen_source_reference` — proof body remains only at exact source commits;
- `local_proof_packet` — readable proof or exact proof extract resides on this branch or `main`;
- `open_obligation` — no proof exists because the mathematical target is open;
- `historical_record` — retained for provenance rather than active use.

Proof residency does not change the mathematical verdict. Copying a proof locally is an information-architecture action, not a new independent review.

## Minimum integrated record

An integrated reference should state:

- the exact theorem and scope;
- exclusions and common misreadings;
- source PR, SHA, claim IDs, and files;
- review report and exact review SHA;
- dependencies and source-qualified inputs;
- proof and computation evidence;
- repair, refutation, alias, and supersession relations;
- repository acceptance and proof residency;
- the next missing lemma.

The corresponding readable packet should contain the proof or proof extract itself.

## Identifier rule

Never cite a bare colliding ID such as `T-7401`. Use either:

```text
PR61:T-7401
```

or the repository-owned integrated ID. Source files are not silently renamed.

## Repairs

A corrected theorem is a new statement with a new source identity or reviewed source SHA. Preserve the false original and the exact first invalid inference. A later repair cannot retroactively change the original verdict.

## Roadmap rule

An accepted roadmap record can remain mathematically `open` or `proposed`. In particular:

- `RD-SC-001` is open;
- `RD-FC-001` is open;
- `RD-BRIDGE-001` is proposed and pending narrow review.

See [`../FRONTIERS.md`](../FRONTIERS.md). Do not call `SC* + FC*` an established exhaustive reduction until the exact bridge crosswalk receives independent review.

## Historical integration evidence

The dated proof-import plans, promotion audits, lifecycle ledgers, and old candidate-state language are indexed under [`../archive/integration/`](../archive/integration/README.md). Their original paths remain stable for provenance.
