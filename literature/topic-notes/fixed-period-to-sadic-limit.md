# From all fixed periods to the balanced S-adic directive

## Why fixed-period irrationality is not enough

Suppose every periodic increment word `W^infinity` selects an irrational `2`-adic value. A balanced nonperiodic directive is not one fixed period, and qualitative irrationality constants may deteriorate arbitrarily with `|W|`.

The true target is a quantitative estimate uniform along the adjacent standard words of the mechanical `17/18` directive.

## Exact repository interface

PR #20 `L-9408` gives the skew transfer

```text
Theta(m;UV)
 =P_U(T^(9m))
  +T^e(U)T^(9m|U|)Theta(m+S(U);V).
```

Standard words satisfy

```text
W_(k+1)=W_k^(a_(k+1))W_(k-1).
```

Their transfer data can be compiled recursively without expanding the full word.

## Required quantitative theorem

For each standard word `W_k`, construct rational approximants with:

```text
finite-place vanishing >= G_k(n),
global reduced height <= H_k(n),
G_k(n)/log_2 H_k(n) >= 1+delta_k,
```

where the margin and all comparison constants remain effective as `k` grows.

Then compare the periodic value `Theta(m;W_k^infinity)` with the true S-adic tail using the exact common-prefix transfer. The error from replacing the true directive by the periodic approximant must be smaller `2`-adically than the nonzero rational linear form produced at level `k`.

## What the block q-Gaussian program should report

Every fixed-period theorem must expose dependence on:

```text
period r;
height sum S(W);
coefficient polynomial P_W;
Padé order n;
primitive boundary determinant;
finite-prefix comparison length.
```

A theorem with constants hidden separately for every `W` cannot pass to the limit.

## Relation to the original staircase idea

The earlier Liouville/Staircase proposal sought increasingly accurate structured approximants to one unique `2`-adic itinerary point. The present version replaces speculative near-cycle words by exact standard-word transfer matrices and completion-safe Padé estimates. The underlying objective is the same: make structured finite approximants survive a limiting ordinary-height argument.
