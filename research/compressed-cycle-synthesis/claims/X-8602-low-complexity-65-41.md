# X-8602 — Low-complexity census at the `65/41` cycle shape

**Experiment ID:** `X-8602`  
**Status:** `EMPIRICAL` exact finite computation  
**Agent:** `gpt56-cycle-01`  
**Date:** 2026-07-22  
**Associated claims:** cycle equation `L-9905`; cycle program issue #9

## Question

At the first nontrivial upper continued-fraction shape

\[
(m,K)=(41,65),
\qquad
D=2^{65}-3^{41}=420491770248316829,
\]

do any low-complexity positive valuation words satisfy

\[
C(a)\equiv0\pmod D?
\]

## Exhausted families

The exact meet-in-the-middle programs cover:

1. every word in `{1,2}^41` with total exponent `65`, equivalently exactly 24 letters equal to `2`;
2. every word of length `41` and total exponent `65` having exactly one exponent at least `3`, with every other exponent equal to `1` or `2`.

The conceptual search sizes are

\[
\binom{41}{24}=151,584,480,450
\]

and

\[
\sum_{e=3}^{25}41\binom{40}{24-(e-1)}
=35,397,011,688,418.
\]

Together this is

\[
\boxed{35,548,596,168,868}
\]

valuation words.

## Result

Both searches returned

```text
modular_matches=0
```

so no word in either family can be a positive cycle.

## Exactness boundary

This is not an exhaustive search over all positive compositions of `65` into `41` parts. Words with two or more exponents at least `3` remain outside the computation. The full composition count is

\[
\binom{64}{40}=250,649,105,469,666,120.
\]

No probabilistic inference from the zero count is made.
