# Contributing

This repository supports two complementary modes.

## Exploratory research

You may open a broad research PR, pursue an unconventional model, write informal notes, run an experiment, refute an earlier claim, or change direction. Use clear status labels and preserve failed approaches. No registry entry is required before exploration.

Useful defaults:

- identify the source issue or question;
- state which map, normalization, and quantifiers are in force;
- separate finite computation from all-depth conclusions;
- keep an exact artifact and replay command when computation matters;
- mark external-theorem dependencies and exact normalizations;
- say plainly what remains open.

These are defaults, not a bureaucracy. Deviate when the research benefits, and explain the deviation.

## Requesting review

A review request should identify:

- the exact commit to freeze;
- the load-bearing claims and files;
- dependencies and source-qualified inputs;
- computational artifacts and whether a full replay is expected;
- the finite-versus-all-depth conclusion;
- known doubts, repairs, or superseded statements.

Reviewers should record a verdict at the frozen SHA. Later commits require a delta review.

## Requesting canonical integration

Canonical integration adds a lightweight contract. Include a short canonicalization note containing:

```text
claim:
source PR and exact SHA:
claim IDs and files:
mathematical status sought:
scope and exclusions:
dependencies:
review report and reviewer:
artifact state:
repair/refutation/supersession relations:
```

The integrator may extract a coherent subpacket rather than merge the entire PR. A mixed PR can therefore preserve verified claims while blocked claims remain deferred.

## Status and evidence

Mathematical status:

- `VERIFIED`
- `SOURCE-QUALIFIED`
- `EMPIRICAL`
- `PROPOSED`
- `OPEN`
- `REFUTED`
- `SUPERSEDED`

Evidence must say which of the following occurred:

- proof inspected;
- proof independently reconstructed;
- artifact inspected;
- artifact regenerated;
- checker run;
- large computation independently replayed;
- computation not replayed;
- artifact missing.

Do not compress these into a single “verified” flag.

## Repairs and identifiers

A repaired theorem receives a new source claim or new source SHA. The original verdict remains in history. Branch-local identifiers are written as `PR<number>:<claim-id>`; canonical IDs are allocated by integrators and recorded in [`claims/aliases.json`](claims/aliases.json).

## Repository changes

Never push research directly to `main`. Use a branch and a reviewable PR. Do not change repository visibility, announce public readiness, or assume licensing/security settings are settled from a research PR.
