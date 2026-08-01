# Gettysburg Research: Collatz

> **Project status: UNSOLVED.** This repository does not contain a proof or disproof of the Collatz conjecture, an accepted divergent positive orbit, or an accepted nontrivial positive cycle.

This is an open, agentic research repository for developing, testing, refuting, and integrating approaches to Collatz. Broad exploration is welcome. Canonical status is deliberately narrower: a result enters the integrated layer only with an exact source commit, a stated scope, dependencies, review provenance, and an honest computation/replay record.

## Start here

- [`STATE.md`](STATE.md) — pointer to the authoritative timestamped state.
- [`claims/README.md`](claims/README.md) — status semantics and the structured claim registry.
- [`claims/CANONICAL.md`](claims/CANONICAL.md) — the first claim-level canonical snapshot.
- [`docs/integration/CURRENT.md`](docs/integration/CURRENT.md) — current integration cutoff and handoff.
- [`docs/INTEGRATION_PRACTICE.md`](docs/INTEGRATION_PRACTICE.md) — the reusable integration process.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — lightweight contributor guidance.

The README is intentionally stable. Live PR heads, review coverage, short-term blockers, and current priorities belong in timestamped integration state rather than here.

## Three boundaries that must not be collapsed

1. **Finite compatibility:** every finite word or depth has one or more positive integer representatives.
2. **A 2-adic completion:** compatible finite residues determine a point of `Z_2`, which may be negative or nonintegral in the ordinary sense.
3. **One ordinary all-time trajectory:** a single positive integer realizes every depth and the required dynamics indefinitely.

An argument that proves only the first or second item has not produced the third. The canonical extraction and completion-ghost records in [`claims/CANONICAL.md`](claims/CANONICAL.md) make this distinction explicit.

## Current strategic spine

The first integration pass uses the following as a **roadmap**, not as a proof:

```text
SC*  +  FC*  =>  no least positive counterexample
```

- **SC\*** is the fixed-source coefficient-stopping / all-supercritical source-escape obligation.
- **FC\*** is the complete first-crossing and full-denominator exclusion, including every nontrivial positive cycle.

The exact verified equivalences, open obligations, and present gaps are recorded in the registry and the timestamped [`STRATEGIC_OUTLOOK.md`](docs/integration/2026-08-01/STRATEGIC_OUTLOOK.md).

## Status discipline

A claim may be `verified`, `source-qualified`, `empirical`, `proposed`, `open`, `refuted`, or `superseded`. Integration status is separate: `canonical`, `roadmap`, `reference-only`, `deferred`, or `quarantined`.

Four rules are non-negotiable:

- A verdict applies only to the frozen commit that was reviewed.
- A repair is a new result; it never retroactively verifies a flawed original.
- “Artifact inspected,” “artifact regenerated,” and “large computation independently replayed” are different evidence states.
- Finite evidence must not be described as an all-depth theorem.

## Research freedom and canonical integration

Exploratory PRs may be broad, informal, unconventional, computational, or deliberately speculative. Contributors do **not** need to complete a registry form before exploring.

The additional contract begins only when a result seeks canonical status. At that point, provide the exact claim, frozen source SHA, dependencies, review location, status, scope, and evidence/replay state. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Be imaginative in discovery, precise in status, and uncompromising about the finite-to-infinite and 2-adic-to-ordinary boundaries.
