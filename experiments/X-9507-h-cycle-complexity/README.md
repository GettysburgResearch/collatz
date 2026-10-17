# X-9507 — cycle-period compression and structured-candidate barrier

**Status:** `INTERNAL EXACT COMPUTATION`; finite certificate only.

This experiment supports `L-9521` and `T-9515` in
`research/h-frontier/claims/ITERATION_08.md`. It combines the exact ordinary
sweep from `X-9506` with a rational continued-fraction certificate for

\[
\kappa={\log(4/3)\over\log(9/8)}.
\]

## Mathematical interface

For a positive exact block cycle of length `L` and total letter sum `R`, the
period multiplier is

```text
M=(3/4)^L (9/8)^R < 1.
```

`L-9521` proves that some cycle state is at most

```text
L/(1-M).
```

If this quantity could exceed the exact ordinary sweep bound

```text
B0=3*2^65,
```

for a cycle with `L<=2,479,700,524`, then `R/L` would approximate `kappa`
within `1/(2L^2)`. Legendre's theorem forces the reduced fraction to be a
continued-fraction convergent of `kappa`.

The script uses only exact rational arithmetic. It bounds

```text
log(4/3)=2*atanh(1/7),
log(9/8)=2*atanh(1/17)
```

with positive rational series tails, reconstructs the relevant continued
fraction, and certifies every lower convergent and all of its multiples in the
period range.

## Result

The certified continued-fraction prefix is

```text
[2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9].
```

The last lower convergent in the range is

```text
2733776749 / 1119265172,
```

and the next convergent is the upper approximation

```text
27172759629 / 11125094063.
```

For every lower convergent and every multiple with denominator at most

```text
2,479,700,524,
```

the exact certificate proves

```text
L/(1-M) < 3*2^65.
```

Together with `X-9506`, this excludes every positive exact H block cycle with
period at most `2,479,700,524`.

## Reproduction

```bash
python3 -B cycle_period_bound.py \
  --output results/canonical.json
```

No third-party package is used.

Semantic payload digest:

```text
b3459e07b363633422db9224bd1758abee922dbd0b2cc3b482db2a6efbb37eba
```

## Scope boundary

The computation does not exclude cycles of larger period and does not produce
or exclude a nonperiodic infinite orbit. The factor-entropy result in
`L-9522` is a proof and has no computational dependency on this experiment.
