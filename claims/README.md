# Canonical Claim Registry

## Why the registry exists

The repository may contain many branches, reports, drafts, overlapping
namespaces, and independent reviews. The claim registry records the current
integrated status without erasing research history.

## Claim kinds and prefixes

```text
D-####  Definition
Q-####  Open question
O-####  Observation
C-####  Conjecture
K-####  Candidate counterexample
L-####  Lemma
T-####  Theorem
X-####  Computational experiment
R-####  Refutation or correction
M-####  Methodological or organizational proposal
```

The prefix identifies the kind of research object. It does not certify truth. A
`T-####` theorem file can be `PROPOSED`, `REFUTED`, or `SUPERSEDED`; an `X-####`
computation must still state its exact finite scope.

Claim IDs should not be silently renumbered after publication. When historical
branches collide, the integrator records aliases or assigns a canonical ID while
preserving the original branch-qualified identifier.

## Two separate dimensions

### Record status

```text
DRAFT
INTEGRATED
ARCHIVED
```

### Primary mathematical status

Retain the project's established vocabulary:

```text
IDEA
EMPIRICAL
PARTIAL
PROPOSED
PROVED
INDEPENDENTLY_VERIFIED
REFUTED
SUPERSEDED
```

Meanings:

- `IDEA` — informal possibility without substantial support;
- `EMPIRICAL` — supported computationally, but not proved;
- `PARTIAL` — rigorous within an incomplete scope;
- `PROPOSED` — a complete-looking proof or construction has been submitted but
  not independently verified;
- `PROVED` — passed an initial detailed project review;
- `INDEPENDENTLY_VERIFIED` — independently reconstructed or checked by another
  contributor;
- `REFUTED` — a counterexample, source failure, computation, or logical error is
  known;
- `SUPERSEDED` — replaced by a clearer, corrected, or stronger formulation.

### Orthogonal qualifiers

```text
CONDITIONAL
FINITE_SCOPE
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
COMPUTATION_NOT_REPLAYED
FORMALLY_CHECKED
```

`FORMALLY_CHECKED` is a qualifier rather than a replacement for mathematical
status. It means the encoded statement compiles without admitted placeholders
and has undergone a statement-to-mathematics translation audit.

## Promotion rules

- authors may develop an `IDEA`, but a complete-looking theorem enters no higher
  than `PROPOSED`;
- an initial detailed review may justify `PROVED`;
- only an independent reconstruction or checker may justify
  `INDEPENDENTLY_VERIFIED`;
- a concrete invalid inference, source mismatch, or counterexample may justify
  `REFUTED`;
- a corrected or stronger replacement may justify `SUPERSEDED`;
- `NOT YET REPRODUCED` is a neutral review result, not a mathematical status and
  not a refutation.

A merged pull request does not automatically change mathematical status.
Artifact integration and claim promotion are separate decisions.

## Required fields

See `index.example.yaml`.

## Resolution candidates

A complete claimed proof or counterexample may receive:

```text
candidate_class: RESOLUTION_CANDIDATE
```

This does not change the README status from `UNSOLVED` without the full
verification and governance process.
