# Round-three review and execution record

Date: 2026-11-23. Parent checkpoint:
`b78819e95ee7d39f02022de991b42217821e7590`.

The [science entry point](../../research/whole-repo-round3-20261123/README.md)
states the result and its limits. This directory records actual inspections,
independent in-session reviews, fresh executions and source identities.
These are internal research checks, not external peer acceptance or a
proof of Collatz.

## Actual formal execution

`LEAN_RECEIPT.json` records four successful commands in an initially empty
output directory: the unchanged `CycleWordAlgebra` dependency, the new
`CarryFibers` and `OrbitCounting` modules, and `RoundThreeAudit.lean`.
The compiler was Lean 4.34.1 with Mathlib pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`; each build used one thread
and warnings as errors. Every one of the nineteen new public statements
was audited. Only `propext`, `Classical.choice` and `Quot.sound` appear.
Source hashes were checked before and after the fresh build.

The formal proof covers finite carry decoding, source-box injection,
weighted finite fiber inequalities, and finite high-clock compression.
The infinite law, binomial asymptotic, global counting recursion and
integral consequences have the written boundaries in the research notes.

## Actual exact replay

`EXACT_RECEIPT.json` records normal and optimized runs of
`research/whole-repo-round3-20261123/exact_replay.py`. Both exit zero;
their complete outputs are byte-identical and separately retained.

- 8,191 complete shortcut words through length 12, including the empty word.
- 25,265 translated carry fibers and 32,764 ordinary source-box occurrences.
- 7,598 actual overlapping windows from ten finite ordinary trajectories.
- 1,926 exact quotient channels, 7,217 source boxes and 2,695 weighted
  quotient-interval groups.
- 3,160 exact negative-binomial identities, 1,182 high-clock compression
  checks, nine complete finite low-lane counts and ninety finite orbit
  charges with the terminal allowance explicitly paid.
- Controls expose loss of the carry quotient, loss of the source quotient,
  omitted repeated words, omitted cross-box terms, and the invalid use of
  a branching basin as an injective set. The known cycle's four-pair
  conditioning identity is also checked with its full denominator seven.

These counts describe executed finite controls. They do not establish an
infinite injective orbit or turn a finite sample into a universal theorem.
The occurrence weights used by the checker are explicitly finite test
weights, not purported samples from a hypothetical harmonic-flow law.

Reproduce the exact controls with:

```bash
python -X utf8 -B research/whole-repo-round3-20261123/exact_replay.py
python -O -X utf8 -B research/whole-repo-round3-20261123/exact_replay.py
```

For the Lean replay, use the pinned toolchain and Mathlib, add a fresh
output directory to `LEAN_PATH`, and rebuild the unchanged local carry
dependency before the two new modules and the audit. The receipt records
the exact commands and source hashes used in this execution.

## Independent review and inventory

The source and cycle agents independently reconstructed the carry-box
proof in `ESCAPE_CARRY_REVIEW.md` and `CYCLE_CARRY_REVIEW.md`. Three
separate reports reconstruct the global-count argument:
`GLOBAL_COUNT_REVIEW.md`, `GLOBAL_COUNT_ESCAPE_REVIEW.md`, and
`CYCLE_ORBIT_COUNT_REVIEW.md`. The escape agent also reviewed the exact
checker source. Each report binds its reviewed file bytes and separates
semantic review from actual compiler or checker execution.

`ROOT_REVIEW.md` records the principal review and scope corrections.
`REPO_INVENTORY.json` contains all 145 PR metadata records from the
inspection snapshot. `PR182_BEFORE.json` preserves the previous PR body.
The research `SOURCES.json` records selected current heads and the exact
read-scope ledgers. Inventory and source inspection are not whole-branch
mathematical validation.

The clean complete-checkout gate and source binding are recorded in
`CHECKOUT_VALIDATION.json` and `SOURCE_BINDING.json`. The gate checks
repository integrity and frozen contracts; it is not mathematical
verification. Published-head validation is additionally reported in the
PR description after its exact remote commit has been fetched and checked.
