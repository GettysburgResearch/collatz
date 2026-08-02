# Contributing

Start with [`START_HERE.md`](START_HERE.md) and [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md). Agents should also read [`AGENTS.md`](AGENTS.md).

This repository supports free exploration, exact review, and selective integration. The process becomes more structured only when a result seeks review or promotion.

## Explore freely

You may open a broad research PR, pursue an unconventional model, write informal notes, run a bounded experiment, connect distant programs, refute an earlier claim, or change direction. No registry entry or canonical packet is required before exploration.

Free-form work can live in an existing `research/`, `experiments/`, `literature/`, or `reports/` area, or in a focused new directory.

Minimal discipline:

- state the map, normalization, and quantifiers;
- label the work `PROPOSED`, `EMPIRICAL`, `SOURCE-QUALIFIED`, `OPEN`, or `REFUTED` as appropriate;
- separate finite evidence from all-depth conclusions;
- keep exact code, artifacts, and replay instructions when computation matters;
- identify external-theorem dependencies and exact normalizations;
- preserve useful failures and say what remains missing.

These are defaults, not a submission bureaucracy. Depart from them when research benefits, and explain the departure.

## Request review

A review request should identify:

- the exact commit to freeze;
- the load-bearing claims and files;
- dependencies and source-qualified inputs;
- computational artifacts and whether a full replay is expected;
- the finite, ordinary, 2-adic, or all-depth conclusion;
- known doubts, repairs, refutations, or superseded statements.

Reviewers record a verdict at the frozen SHA:

```text
VERIFIED
VERIFIED WITH FIXES
GAP/BLOCKED
REJECTED
```

A branch-level verdict may contain passing and failing claims. Record the exceptions. Later theorem-bearing commits require a delta review.

## Request integrated promotion

Integration is claim-level and normally uses clean extraction rather than merging a long exploratory history. Supply a short note containing:

```text
precise statement:
source PR and exact SHA:
claim IDs and files:
scope and exclusions:
dependencies:
review report and exact review SHA:
proof/computation evidence:
repair, refutation, alias, or supersession relations:
next missing lemma:
```

A promoted result should become a readable packet under [`research/integrated/`](research/integrated/README.md), not only a registry row. The integrator may extract a coherent subset while leaving blocked or speculative material in the source branch.

## Status and evidence are separate

Mathematical status:

- `VERIFIED`
- `SOURCE-QUALIFIED`
- `EMPIRICAL`
- `PROPOSED`
- `OPEN`
- `REFUTED`
- `SUPERSEDED`

Evidence state:

- proof inspected;
- proof independently reconstructed;
- proof extracted locally;
- artifact inspected;
- artifact regenerated;
- checker run;
- large computation independently replayed;
- computation not replayed;
- artifact missing.

Do not compress these into one “verified” flag.

## Repairs and identifiers

A repaired theorem receives a separate source claim or reviewed source SHA. The original verdict remains in history. Branch-local identifiers are written as `PR<number>:<claim-id>` because collisions exist; repository-owned integrated IDs are recorded in [`claims/aliases.json`](claims/aliases.json).

A refuted original should remain readable beside its repair whenever practical.

## Repository safety

- Never push research directly to `main`.
- Use a branch and a draft PR for unfinished work.
- Do not change repository visibility, permissions, branch protection, or workflow settings from a research PR.
- Do not enable or add GitHub Actions without explicit owner approval.
- Do not run expensive searches merely for activity; explain cost, pilot scale, and proof role first.
- Do not merge or close another contributor’s PR without explicit integration authority.

## What makes a contribution valuable

A full proof is valuable. So is a precise counterexample to a proposed lemma, an exact method boundary, a well-scoped finite artifact, a corrected source normalization, or a clear first unsupported inference. The goal is durable research that later humans and systems can trust and extend.
