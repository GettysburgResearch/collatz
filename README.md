# Gettysburg Research: Collatz

> **Project status: UNSOLVED.** This repository does not contain a proof or disproof of the Collatz conjecture, an accepted divergent positive orbit, or an accepted nontrivial positive cycle.

This is an open, agentic research repository for developing, testing, refuting, and integrating approaches to Collatz. Broad exploration is welcome. Canonical status is deliberately narrower: a result enters the integrated layer only with an exact source commit, a stated scope, dependencies, review provenance, an honest computation/replay record, and an explicit repository-promotion state.

## Start here

- [`STATE.md`](STATE.md) — current operational pointer.
- [`docs/integration/CURRENT.md`](docs/integration/CURRENT.md) — frozen snapshot and lifecycle continuation.
- [`docs/integration/2026-08-02-lifecycle/PR_LIFECYCLE.md`](docs/integration/2026-08-02-lifecycle/PR_LIFECYCLE.md) — advisory disposition for every source PR in the first snapshot.
- [`claims/README.md`](claims/README.md) — status and promotion semantics.
- [`claims/CANONICAL.md`](claims/CANONICAL.md) — candidate-canonical and roadmap records selected by draft PR #84.
- [`docs/INTEGRATION_PRACTICE.md`](docs/INTEGRATION_PRACTICE.md) — reusable integration and lifecycle practice.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — lightweight contributor guidance.

The README is intentionally stable. Live PR heads, review coverage, short-term blockers, lifecycle decisions, and current priorities belong in dated integration records.

## Three boundaries that must not be collapsed

1. **Finite compatibility:** every finite word or depth has one or more positive integer representatives.
2. **A 2-adic completion:** compatible finite residues determine a point of `Z_2`, which may be negative or nonintegral in the ordinary sense.
3. **One ordinary all-time trajectory:** a single positive integer realizes every depth and the required dynamics indefinitely.

An argument that proves only the first or second item has not produced the third.

## Review, integration, and acceptance are different

A review verdict answers whether a statement passed at one exact SHA. It is not a merge, extraction, closure, or lifecycle instruction.

The registry uses four separate dimensions:

```text
mathematical status
integration role
repository promotion state
proof residency
```

While PR #84 remains an unmerged draft, its eight `IC-*` records are **candidate canonical reference records**, not accepted repository canon. Their source mathematics retains the exact reviewed status recorded at the frozen commits. See [`claims/README.md`](claims/README.md).

## Current strategic spine

The first integration pass uses the following as a **proposed roadmap bridge**, not as an accepted theorem:

```text
SC*  +  FC*  =>  no least positive counterexample
```

- **SC\*** is the fixed-source coefficient-stopping / all-supercritical source-escape obligation.
- **FC\*** is the complete first-crossing and full-denominator exclusion, including every nontrivial positive cycle.
- **RD-BRIDGE-001** is the missing clean crosswalk showing that the repository definitions of SC* and FC* cover every least-counterexample case.

The reviewed ingredients and the remaining bridge review are recorded in [`SC_FC_BRIDGE.md`](docs/integration/2026-08-02-lifecycle/SC_FC_BRIDGE.md). Until that bridge receives narrow independent review, describe this as the principal proposed organizational spine, not as a logically established exhaustive theorem.

## Research freedom and lifecycle discipline

Exploratory PRs may be broad, informal, unconventional, computational, or deliberately speculative. Contributors do **not** need a registry entry before exploring.

The additional contract begins only when material seeks review, canonical integration, or eventual closure. A source PR is not closed merely because its headline is rejected or duplicated: accepted claims, refutations, artifacts, open questions, and provenance must first have durable destinations. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the lifecycle ledger.

Be imaginative in discovery, precise in status, and uncompromising about the finite-to-infinite and 2-adic-to-ordinary boundaries.
