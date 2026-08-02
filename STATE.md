# Current repository state

> **Collatz remains unsolved.** No accepted proof, disproof, divergent positive seed, or nontrivial positive cycle is present.

This file is the single current pointer for the repository.

## Current refinement

Round 1 of the front-door and proof-residency pass is in draft PR [#85](https://github.com/GettysburgResearch/collatz/pull/85):

```text
branch: agent/integration-front-door-round1
base:   7ed553faea8350050ca4c7d742c049f90211a8bd
status: draft; not ready for merge pending Round 2 inspection
```

The pass does not change mathematical verdicts, merge or close source PRs, run expensive computations, or alter repository settings. It reorganizes navigation, imports readable proof packets, and repairs stale post-merge semantics.

## Start here

- [`README.md`](README.md) — two-minute project overview.
- [`START_HERE.md`](START_HERE.md) — human onboarding and basic notation.
- [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md) — curated scientific synthesis.
- [`FRONTIERS.md`](FRONTIERS.md) — exact open obligations and smallest missing lemmas.
- [`AGENTS.md`](AGENTS.md) — concise operating guide for research and coding agents.
- [`research/integrated/`](research/integrated/README.md) — readable integrated proof packets.

## Accepted reference layer

Merged PR #84 accepted eight `IC-*` reference records and three `RD-*` roadmap records onto `main` at merge commit

```text
7ed553faea8350050ca4c7d742c049f90211a8bd.
```

Round 1 distinguishes repository acceptance from proof residency:

- `IC-EXTRACT-001`, `IC-GHOST-001`, `IC-SC-001`, `IC-AUT-001`, and `IC-RIG-001` now have local proof packets;
- `IC-REF-001` and `IC-REP-001` share a local refutation/repair packet, with PR #16 dependencies still source-pinned;
- `IC-PERIODIC-001` has a local proof packet, but its exact integrated synthesis remains pending narrow independent review;
- `RD-SC-001` and `RD-FC-001` remain open;
- `RD-BRIDGE-001` remains proposed and pending narrow review.

The active human index is [`claims/CANONICAL.md`](claims/CANONICAL.md); machine metadata is under [`claims/registry/`](claims/registry/).

## Current scientific gaps

The load-bearing gaps are:

1. a fixed-source valuation theorem proving `SC*`;
2. a complete all-word first-crossing obstruction proving `FC*`;
3. independent review of the exact `SC* + FC*` bridge;
4. independent review of the integrated periodic-tail synthesis;
5. boundedness or escape of a concrete aperiodic least-root sequence;
6. local proof residency for reviewed results outside the initial integrated layer.

See [`FRONTIERS.md`](FRONTIERS.md) for precise formulations.

## Backstage evidence

Frozen snapshots, review-wave detail, PR lifecycle recommendations, machine inventories, and old handoffs are indexed under [`archive/`](archive/README.md).

The first immutable cutoff remains:

```text
cutoff UTC: 2026-08-01T21:16:40Z
frozen main: 0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84
source PRs at cutoff: 45
exact-SHA review coverage: 42/45
unreviewed in that wave: #67, #68, #69
```

Files under `docs/integration/2026-08-01/` remain historical and are not rewritten. The `2026-08-02-lifecycle` directory records the pre-merge lifecycle continuation and may contain language that was accurate while #84 was still a draft; the archive index explains that boundary.

## Current safety boundary

- No source PR has been merged or closed by this refinement.
- No GitHub Actions workflow has been added or run.
- No broad Collatz computation, census, proof search, or expensive replay has been performed.
- The conjecture remains open.
