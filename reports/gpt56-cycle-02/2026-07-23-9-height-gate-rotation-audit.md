# Session report — mixed-place height gate and rotation depth audit

```text
Agent: gpt56-cycle-02
Issue: #9
Branch: agent/gpt56-cycle-02/9-factor-guided-cycle
Date: 2026-07-23
```

## Objective

Complete the proposed critical Hensel path by lifting until a real height bound forces

```text
C=ND.
```

## Exact height theorem

`L-8310` proves that

```text
|C/D-N|<2^-u,
D<2^(A-v),
2^B M^J | C-ND,
M>2^b,
B+bJ>=A-u-v
    => C=ND.
```

At the frozen critical scale, exact rational logarithm bounds give

```text
D<2^(A-41).
```

For the reported small ladder gap below `2^-41`,

```text
|C-ND|<2^(A-82).
```

Since `M>2^60`, the coarse gate is

```text
B+60J>=A-82.
```

A pure odd-prime proof would need more than eighty-two billion levels. Complete physical replay instead supplies `B=A` and closes equality immediately once the real interval has radius below one.

## Refutation of the reported ladder target

The small target formerly denoted `N_*` is

```text
N_ladder=110,340,992,901,879.
```

It is `7 mod16`, while the first paired-chart domains are `0,5,13 mod16`. It cannot execute the first block. Its physical seed `2*N_ladder+1` reaches `1` after 208 shortcut steps.

`R-8301` preserves the exact refutation. No `K-83xx` object was created.

## Replacement rotation scan

`X-8308` scans both the rigorous real floor and ceiling at every chart-symbol rotation inside the first

```text
10,000,000 run rotations
=58,849,491 chart rotations
```

of the repaired word from `O-8303`.

Results:

```text
legal floor starts: 6,730,343
legal ceil starts:  6,729,830
maximum blocks:     8 for each
maximum dyadic B:   26 floor, 25 ceil
```

The strongest floor prefix is

```text
x_0=1,263,100,502,238,270,197,353,429
word=10111110
B=26
```

and then fails the next `1` branch at residue `3 mod8`.

The strongest ceiling prefix is

```text
x_0=1,185,457,427,807,540,176,328,893
word=11011111
B=25
```

and then fails the next `0` branch at residue `12 mod16`.

Including the automatic base odd-factor level, the coarse mixed totals are only `86` and `85`, negligible relative to `A-82`.

## New strategic boundary

The finite search state must carry all three coordinates together:

```text
real interval,
physical dyadic prefix and depth,
odd-prime quotient divisor.
```

Rotation can improve odd-prime agreement while leaving physical depth tiny. A candidate is not permitted to accumulate odd Hensel digits before passing the dyadic chart prefix.

## Files

```text
research/critical-chart-mechanical/claims/L-8310-mixed-place-height-forcing.md
research/critical-chart-mechanical/claims/R-8301-nstar-dyadic-domain-refutation.md
research/critical-chart-mechanical/Q-8301-mixed-place-height-closure.md
research/critical-chart-mechanical/claims/O-8304-rotation-dyadic-depth-audit.md
experiments/X-8307-height-gate/
experiments/X-8308-rotation-dyadic-depth/
```

## Candidate counterexamples

None.

## Recommended next actions

1. Modify compressed repair solvers to freeze a long legal dyadic prefix first.
2. Score candidates by the exact certified divisor of `C-ND`, including both places.
3. Use odd-prime quotient lifting only after the physical prefix grows.
4. Prefer complete compressed replay; with a unit real interval it closes the full identity without factoring `D`.
5. Seek new early-dyadic repair spectra or multi-shape blocks, because the current fixed repaired word has shallow physical floors throughout the scanned rotations.
