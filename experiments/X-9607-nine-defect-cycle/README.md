# X-9607 — Exact nine-defect positive-cycle exclusion

**Experiment ID:** `X-9607`  
**Status:** exact finite computation supporting proposed `T-9603`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23

## Purpose

This packet verifies the complete finite remainder of `T-9603` after its centered-contraction and largest-neutral-gap reductions.

Centering an accelerated valuation word at the trivial fixed point `1` makes every valuation `2` disappear from the defect numerator. The theorem classifies all words with exactly nine remaining valuations, reduces them to nine residual exceptional-letter languages, proves finite cutoffs for every neutral-gap range, and leaves the exact divisor packet checked here.

It is a positive-cycle exclusion computation. It does not produce a positive cycle, an infinite divergent orbit, or a Collatz counterexample.

## Exact coverage

The residual languages are:

```text
1^9
1^8,3
1^8,4
1^8,5
1^8,6
1^7,3,3
1^7,3,4
one cyclic class of 1^7,3,5
three cyclic classes of 1^6,3,3,3
```

The infinite neutral-gap ranges are removed by proved monotone height bounds. The remaining finite packet contains:

```text
finite (type,R) rows                  125
largest-gap-normalized candidates      98,203,183
height survivors                           36,988
formal divisor hits                              0
nontrivial cycle hits                            0
```

High valuation magnitudes are unbounded in the theorem; monotone lowering reduces them to the displayed finite residual types. A tied largest neutral gap can duplicate a cyclic word but cannot omit one.

## Independent implementations

`run.cpp` evaluates the nine-term sparse centered numerator directly. It records every row internally, emits a compact aggregate payload, and binds the omitted rows through the FNV-1a digest

```text
7582e70da78e92b7
```

computed over canonical row strings

```text
type|R|D|candidate_count|max_E|height_count|min_circular_remainder\n
```

in deterministic order.

`verify.cpp` is separately written. It computes centered numerators by composing nine exceptional-letter-plus-gap blocks, independently regenerates every row, checks per-type totals and minimum remainders, and reproduces the same row digest.

Both programs use exact signed 128-bit integers. The largest values in the frozen packet lie safely inside that range. There is no floating-point arithmetic, solver, randomized step, or heuristic pruning.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9607-nine-defect-cycle/run.cpp \
  -o /tmp/x9607

/tmp/x9607 > /tmp/x9607.json

diff -u \
  experiments/X-9607-nine-defect-cycle/results/canonical.json \
  /tmp/x9607.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9607-nine-defect-cycle/verify.cpp \
  -o /tmp/x9607-verify

/tmp/x9607-verify
```

## Frozen digests

```text
run.cpp SHA-256
4963bcd4de43990b4e6d61c4ad67f8018cb37ca3886c304b004c03419ab7d1c6

verify.cpp SHA-256
c94af8b9b993aaecf4c3f0275a9e34344d0a53f168131db788545e3dcf29f02a

canonical.json SHA-256
b6762eeadd307351340392cdda9feba42e04ddf273f609ea711c9c859bc46354

canonical row FNV-1a-64
7582e70da78e92b7
```

The SHA-256 values were computed in the authoring environment. A repository or CI replay remains the requested independent confirmation.

The authoring run completed in approximately `3.77` seconds with peak RSS `3,584 KB`; the independent verifier completed in approximately `3.97` seconds with peak RSS `3,580 KB`. These measurements are informational only.

## Boundary

- The packet covers exactly nine valuations different from `2`, with arbitrary neutral gaps.
- It depends on the universal contraction and cutoff proof in `T-9603`; all frozen numerical classifications are reproduced from exact integer arithmetic.
- Ten or more non-neutral valuations remain open.
- No finite residue, near-divisibility, long computation, or absence of a hit is interpreted as evidence that a counterexample exists.
