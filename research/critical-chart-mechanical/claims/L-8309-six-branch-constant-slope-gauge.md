# L-8309 — The six-branch intrinsic core has a constant-slope six-digit gauge

Claim ID: `L-8309`  
Status: `PROPOSED / EXACT AFFINE CONJUGACY`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `T-8305`  
Scope: every exact ordinary transition of the six-branch intrinsic-core system  
Related counterexample candidates: none

## 1. Starting recurrence

Retain the type/core recurrence

\[
2^{19+3(i_n-i_{n+1})}u_{n+1}
=3^{12+2(i_{n-1}-i_n)}u_n+7,
\tag{1}
\]

with

\[
i_n\in\{0,1,2,3,4,5\}.
\tag{2}
\]

Define the rational gauge

\[
\boxed{
y_n
=3^{2i_{n-1}}2^{-3i_n}u_n.}
\tag{3}
\]

The pair `(i_(n-1),i_n)` determines the lattice containing `y_n`; no information is discarded.

## 2. Constant-slope recurrence

### Theorem

Equation `(1)` is equivalent to

\[
\boxed{
y_{n+1}
=\lambda y_n+d_{i_n},}
\tag{4}
\]

where

\[
\boxed{
\lambda={3^{12}\over2^{19}}>1,}
\tag{5}
\]

and the six positive digits are

\[
\boxed{
d_i
={7\over2^{19}}\left({9\over8}\right)^i,
\qquad0\le i\le5.}
\tag{6}
\]

### Proof

Solving `(1)` for `u_(n+1)` and multiplying by the next gauge gives

\[
\begin{aligned}
y_{n+1}
&=3^{2i_n}2^{-3i_{n+1}}
 {3^{12+2(i_{n-1}-i_n)}u_n+7
  \over
  2^{19+3(i_n-i_{n+1})}}\\
&={3^{12}\over2^{19}}
  3^{2i_{n-1}}2^{-3i_n}u_n
 +{7\,3^{2i_n}\over2^{19+3i_n}}.
\end{aligned}
\]

The first term is `lambda y_n`; the second is `(6)`. **QED**

## 3. Explicit finite evolution

For every `m>=1`, iteration gives

\[
\boxed{
y_m
=\lambda^m y_0
+\sum_{t=0}^{m-1}\lambda^{m-1-t}d_{i_t}.}
\tag{7}
\]

Equivalently,

\[
\boxed{
\lambda^{-m}y_m
=y_0+
\sum_{t=0}^{m-1}\lambda^{-t-1}d_{i_t}.}
\tag{8}
\]

The digit sum is positive in the real embedding. The exact ordinary path condition is not merely `(7)`: each `y_n` must lie in the moving rational lattice

\[
\boxed{
y_n\in
3^{2i_{n-1}}2^{-3i_n}\mathbf Z_{>0}}
\tag{9}
\]

and must reconstruct the exact shortcut-Collatz block.

## 4. Physical meaning

The six-branch quotient chart and the negative-three run highway are therefore one rational-base affine system with:

```text
constant slope: 3^12 / 2^19,
digits:         (7/2^19)(9/8)^i,  i=0,...,5,
lattice phase:  (i_(n-1),i_n).
```

All drift is in the single constant `(5)`. The types carry only the digit and lattice phase.

This separates the full counterexample problem into two exact obligations:

1. construct one positive ordinary orbit of `(4)` satisfying every lattice condition `(9)`;
2. invoke `T-8305` to obtain automatic unbounded physical Collatz growth.

## 5. Gap audit

- A real orbit of `(4)` need not satisfy `(9)`.
- A compatible 2-adic digit sequence need not have an ordinary positive initial point.
- The gauge is rational and phase-dependent; dropping the phase loses integrality information.
- No positive infinite path or cycle is asserted.

## 6. Suggested next attack

Treat `(4)` as a six-digit rational-base expansion with a 36-phase lattice automaton. Search for a finite-support/top-boundary invariant rather than a low-residue lasso. The constant slope makes interval propagation and exact backward cylinders substantially simpler than in the ungauged recurrence.
