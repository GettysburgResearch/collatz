# Canonical Claim Registry

## Why the registry exists

The repository may contain many branches, reports, drafts, and reviews.

The claim registry records the current integrated status without erasing
history.

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

The prefix identifies the kind of research object. It does not certify truth.
A `T-####` theorem file can be `PROPOSED`, `REFUTED`, or `SUPERSEDED`; an
`X-####` computation must still state its exact finite scope.

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

### Mathematical status

```text
IDEA
DEVELOPING
PROPOSED
INDEPENDENTLY_RECONSTRUCTED
FORMALLY_CHECKED
REFUTED
SUPERSEDED
```

Flags:

```text
EMPIRICAL
FINITE_SCOPE
PARTIAL
CONDITIONAL
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
```

## Promotion rules

- authors may move `IDEA` to `DEVELOPING`;
- a complete-looking proof may enter as `PROPOSED`;
- only an independent review may justify
  `INDEPENDENTLY_RECONSTRUCTED`;
- formal compilation plus statement audit may justify `FORMALLY_CHECKED`;
- a concrete invalid inference or counterexample justifies `REFUTED`;
- a stronger or corrected replacement justifies `SUPERSEDED`.

A merged pull request does not automatically change mathematical status.

## Required fields

See `index.example.yaml`.

## Resolution candidates

A complete claimed proof or counterexample receives:

```text
candidate_class: RESOLUTION_CANDIDATE
```

This does not change the README status from `UNSOLVED` without the full
governance process.
