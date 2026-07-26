# Session report — all-repetition three-pulse exclusion

**Agent:** `gpt56-sol-04`  
**Issue:** #52  
**Branch:** `cursor/three-pulse-exclusion-8f0f`  
**Date:** 2026-07-26

## Result

`T-8260` and `X-8260` extend the exact two-pulse framework to exactly three
distinct positive pulse locations with arbitrary heights, over every
repetition and rotation of both known ordinary negative cycles.

The all-repetition conclusion is explicitly `PROPOSED / SOURCE-DEPENDENT`
because the primary Matveev theorem was not independently reconstructed.  The
remaining finite computation is proved by an independently replayable exact
certificate and does not depend on Matveev.

## Reduction

Rotating a largest cyclic support gap to the end gives

```text
p3 <= floor(2kr/3).
```

The reduced distributed-pulse correction has exact chain form

```text
R = -w1 + (w1-w2)X1 + (w2-w3)X1X2 + w3X1X2X3,
w1>w2>w3>0.
```

For a divisor hit this yields

```text
0 < Lambda
  < 2 c_* 3^floor(2kr/3) / 2^(Ar).
```

Conditional Matveev cutoffs, exact transition inequalities, Legendre's
criterion, and certified continued fractions reduce the finite computation to

```text
P3:  r=2,3
P11: r=1
```

with `P3,r=1` structurally impossible for three distinct locations.

The continued-fraction reduction rejects 17 ordinary upper families.  The
exceptional P3 row `1/5` has `(r,t)=(5m,m)`; three pulses force `m>=3`, and
the exact first-case exclusion margin is

```text
75388584689551 / 281474976710656.
```

## Arbitrary-height computation

For every normalized finite packet, the computation reconstructs the reduced
L-8201 resultants, exact `2`-adic valuations, Bézout identities, norm bounds,
and all three coordinate caps.  It then checks every power-of-two height tuple
inside the cap boxes, including `C-zD=G R`, divisibility, and physical replay.

Exact totals:

```text
raw rotation/support configurations:      293
normalized packets:                        45
finite tuples:                         53,808
resultant identities:                 161,424
continued-fraction rows:                   38
primitive upper families rejected:         18
transition repetitions rejected:            7
nontrivial hits:                             0
trivial hits:                                1
```

The sole hit is

```text
P3, r=3, rotation=0,
support=(0,2,4), heights=(1,1,1),
(1,2)^3 -> (2,2,2,2,2,2),
D=R=3367, n=1.
```

It replays exactly and is the trivial Collatz cycle.

## Invalid scout premise

PR #51 `X-8002` does not close arbitrary pulse heights.  It scans only the
least total pulse crossing `D>0` and the next three total-pulse levels.
Therefore its absence of nontrivial hits cannot by itself imply an
arbitrary-height exclusion.  `X-8260` closes that gap with nonzero coordinate
caps and complete cap-box enumeration.  `X-8002` remains useful corroboration
and saw the same trivial `r=3` hit.

## New files

```text
experiments/X-8260-three-pulse-repetitions/README.md
experiments/X-8260-three-pulse-repetitions/run.py
experiments/X-8260-three-pulse-repetitions/verify.py
experiments/X-8260-three-pulse-repetitions/test_run.py
experiments/X-8260-three-pulse-repetitions/results/canonical.json
experiments/X-8260-three-pulse-repetitions/results/finite-tuples.jsonl.gz
research/outlier-bridges/claims/T-8260-all-repetition-three-pulse-exclusion.md
reports/gpt56-sol-04/2026-07-26-52-three-pulse-repetitions.md
```

The independent verifier imports no author-side module.  It reconstructs all
analytic records, support coverage, primitive rotations, packet caps, 53,808
tuple rows, transcript digests, and the sole replay.

Master transcript:

```text
3ecc48c9b33c99f9395cb61e28fed61ad9cd8f5ed48b3eac246a97cc1f7655cc
```

## Status boundary

- exact finite arbitrary-height computation: independently replayable;
- elementary all-repetition reductions after the logarithmic-form lower
  bound: exact rational certificates;
- Matveev theorem statement and normalization: external source dependency;
- final all-repetition theorem: `PROPOSED / SOURCE-DEPENDENT`;
- no nontrivial cycle, divergent orbit, or Collatz counterexample claimed.
