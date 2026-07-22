# X-9605 — Exact seven-defect positive-cycle exclusion

**Experiment ID:** `X-9605`  
**Status:** exact finite computation supporting proposed `T-9601`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22

## Purpose

This packet verifies the complete finite remainder of `T-9601` after its all-parameter contraction and largest-gap arguments.

A valuation `2` is neutral after centering at the trivial accelerated fixed point `1`. The experiment considers words with exactly seven valuations different from `2`, rotates a largest neutral gap to the terminal position, classifies the surviving exceptional-letter multisets, and tests every remaining exact divisor condition.

It is a cycle-exclusion computation. It does not search ordinary divergent trajectories and it does not produce a Collatz counterexample.

## Exact coverage

The theorem reduces all seven-defect words to five residual exceptional types:

```text
1^7
1^6,3
1^6,4
1^6,5
1^5,3,3
```

The infinite neutral-gap ranges are terminated by proved Archimedean inequalities. The remaining packet has:

```text
finite (type,R) rows                  27
largest-gap-normalized candidates     49,471
height survivors                       1,290
formal divisor hits                        0
nontrivial cycle hits                       0
```

Tied largest gaps may duplicate a cyclic word but cannot omit one.

## Two independent programs

`run.py` uses a recursive weak-composition generator and computes every centered numerator both as `C-D` and through the sparse centered sum.

`verify.py` uses a separate separator-position stars-and-bars generator, independently constructs each core word, independently recomputes `C`, `D`, and the sparse numerator, and refuses any unexpected divisor hit.

Both programs use Python integers only. There is no floating-point arithmetic and no solver dependency.

## Replay

```bash
python3 -B experiments/X-9605-seven-defect-cycle/run.py \
  --check-results \
  experiments/X-9605-seven-defect-cycle/results/canonical.json

python3 -B experiments/X-9605-seven-defect-cycle/verify.py \
  experiments/X-9605-seven-defect-cycle/results/canonical.json
```

## Frozen digests

```text
run.py SHA-256
b19bfb9815390e3fab2b63394fb9792a2f311f4da5d85844e0ef7b0658204c3c

verify.py SHA-256
0535fe43a150c55f11464ba0f12cad281fcbd7631776f8a1ea28323fefc3f56c

canonical.json SHA-256
6c77350c160bd6017781e83ee041882787d881ccf4fff23cd8b56f83fb5a5b7e

semantic audit SHA-256
9545aa4c7677d13f1ff47374f93bb3fc6dd3e01b9ca89312521466d556beebba

canonical results payload SHA-256
db9fdf0647d5111ee1dd2fb83fdcb41dbd03a29d9a4bd013493e9c803cdfc607
```

The source-file hashes above were computed in the authoring environment. Repository or CI replay is still required for independent confirmation.

## Boundary

- The computation covers exactly seven non-`2` valuations, with arbitrary nonnegative neutral gaps and unbounded original high valuations through the theorem's monotone reductions.
- It assumes the mathematical contraction and cutoff lemmas stated in `T-9601`; the finite programs separately verify their frozen arithmetic tables.
- Eight or more non-`2` valuations are outside this packet.
- No finite prefix, residue, near-divisibility, or failed search row is interpreted as evidence for an unconditional counterexample.
