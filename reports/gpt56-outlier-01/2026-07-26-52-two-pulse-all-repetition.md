# Session report — global target audit and all-repetition two-pulse closure

**Agent:** `gpt56-outlier-01`  
**Issue:** #52; reviewed in the global-blocker context of #55  
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`  
**Date:** 2026-07-26

## Starting target

Attack the smallest honest ordinary-extraction decision: boundedness versus escape of the fixed six-branch least-root sequence. Do not add another finite prefix or conditional-growth lemma.

## Direct six-branch finding

The exact chart is the minimal rational-base orbit for

```text
P/Q=3^12/2^19
```

with six allowed minimal digits. A tempting p-adic periodicity theorem does not apply: Frougny--Klouda treat positive-power AFS/GMD representations with the p-adically contracting numerator orientation, whereas the six-branch completion is the opposite minimal-word extension orientation. The April 2026 rational-base normality paper still presents normality, digit richness, and the relevant equidistribution as conjectural.

Therefore no honest digit-escape theorem was obtained for the six-branch sequence. Claiming otherwise would silently solve a recognized open rational-base frontier.

## Pivot criterion

The user requested a genuine global result or an exhaustive class elimination. The nearest tractable infinite axis was the remaining repetition parameter in the two-pulse negative-cycle program.

## New result

`T-8255` proposes, source-conditionally, that every two-pulse lift of every repetition and rotation of either known negative accelerated cycle is nonintegral except the trivial `(2,2)^2`, `n=1` cycle.

The central new inequality is uniform in gap and pulse split:

```text
0<Lambda
 <2 c_* 3^floor(k r/2)/U^r.
```

It follows from the exact two-pulse correction and the shorter-gap normalization. Matveev gives finite repetition cutoffs; Legendre and certified continued fractions reduce all remaining repetitions to eighteen primitive upper families; seventeen vanish by one exact size inequality and the exceptional `1/5` family vanishes separately because two pulses force multiplier `m>=2`.

The remaining small repetitions are exhaustively closed by the nonzero two-pulse eliminants. The sole hit is `n=1`.

## New files

```text
research/outlier-bridges/claims/T-8255-all-repetition-two-pulse-exclusion.md
experiments/X-8255-two-pulse-all-repetition/README.md
experiments/X-8255-two-pulse-all-repetition/run.py
experiments/X-8255-two-pulse-all-repetition/verify.py
experiments/X-8255-two-pulse-all-repetition/results/canonical.json
reports/gpt56-outlier-01/2026-07-26-52-two-pulse-all-repetition.md
```

## Exact validation

Both local programs passed:

```text
continued-fraction rows:             38
primitive upper families rejected:   18
small positive-denominator pairs:    898
nontrivial hits:                       0
trivial hits:                          1
master transcript:
b60b6c1e4564ac52a52749af8e19f854fb0f3de0c0a6269037e3f452b91278a8
```

The verifier imports no author module.

## Mathematical status

- native two-pulse algebra and finite certificates: exact and locally replayed;
- theorem: `PROPOSED / SOURCE-DEPENDENT`;
- concentrated external uncertainty: exact primary Matveev theorem normalization inherited from `T-8202`;
- no counterexample claimed.

## Genuine relationship to Collatz

The result eliminates an exhaustively specified infinite construction class and is therefore genuinely weaker than Collatz. It does not merely extend a search cutoff. It says that any positive cycle derived from the two known negative baselines by coordinatewise upward pulsing must use at least three pulse locations in a support architecture not covered by the theorem.

## Recommended next action

1. independent primary-source reconstruction of the Matveev constant and substitutions for `T-8202/T-8255`;
2. do not revisit one- or two-pulse scans after review;
3. attack growing multi-pulse support uniformly, or return to the six-branch least-root sequence only with an architecture-specific Archimedean theorem.
