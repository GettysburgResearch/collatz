# R-8701 — Fixed-modulus PDR lassos are not ordinary witnesses

**Claim ID:** `R-8701`  
**Type:** refutation / method boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Dependencies:** `T-8701`  
**Scope:** every fixed dyadic precision in the centered forced-tail system

## Refuted inference

> A cyclic state in a sufficiently deep fixed-modulus forced-tail graph supplies an ordinary positive infinite orbit.

This inference is false at every depth.

## Exact statement

For each `d>=1`, the recurrent PDR kernel is the full de Bruijn cylinder graph `K_d` from `T-8701`. Every kernel state is the reduction of a periodically controlled `2`-adic completion.

If the periodic control is nonconstant, that completion is not a signed ordinary integer. If the control is constant, the nearest-integer completion is `B=0`, yielding only the two trivial section points.

Therefore

\[
\boxed{
\text{no nontrivial fixed-modulus lasso is an ordinary witness.}}
\tag{1}
\]

## Proof of nonordinariness

Let the control have period `p`. Over one period the recurrence gives

\[
(64^p-81^p)B_0=D,
\]
where

\[
D=
\sum_{j=0}^{p-1}
81^{p-1-j}64^j(e_j-e_{j+1}).
\]

Since `|e_j-e_{j+1}|<=1`,

\[
|D|
\le
\sum_{j=0}^{p-1}81^{p-1-j}64^j
=
\frac{81^p-64^p}{17}
<81^p-64^p.
\]

If `B_0` were an integer, divisibility would force `B_0=0` and `D=0`. But with `B_0=0`, one recurrence step reads

\[
64B_1=e_0-e_1.
\]

The right side has absolute value below `64`, so integrality forces `e_0=e_1`. Repeating around the period makes the control constant. Thus every nonconstant periodic lasso is nonordinary.

For either constant control, all differences vanish and `B=0`; the corresponding original states are the trivial `A=0` and `A=1` section points.

## Consequence for PDR design

A sound counterexample certificate must add an **ordinary top-boundary obligation**. Examples include:

- a finite-support base-64 word invariant under the exact carry transducer;
- a height/carry inductive invariant showing that the moving top boundary closes;
- an explicit seed together with a proof-carrying unbounded run;
- a one-counter or well-structured abstraction whose concretization is ordinary, not merely `2`-adic.

Increasing fixed dyadic precision without such a coordinate only enlarges the de Bruijn ghost presentation; it never crosses the completion-to-integer boundary.
