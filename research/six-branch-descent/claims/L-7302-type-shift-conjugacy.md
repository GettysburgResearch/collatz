# L-7302 — Geometric type-shift conjugacy and the zero-type gate

**Claim ID:** `L-7302`  
**Title:** Vertical shifts of the six branch types are exact `9/8` conjugacies  
**Status:** `PROPOSED / EXACT ALGEBRAIC THEOREM`  
**Authoring agent:** `gpt56-cycle-01`  
**Created:** 2026-07-26  
**Dependencies:** PR #64 `D-7401`; the phase-free valuation identity from PR #45  
**Scope:** type-confined ordinary tails in the fixed six-branch chart  
**Related counterexample candidates:** none

## 1. Geometric alphabet

The six digits satisfy

\[
\boxed{a_{i+1}={9\over8}a_i.}
\tag{1}
\]

Let a positive ordinary orbit have type code

\[
i_0,i_1,\ldots
\]

and satisfy

\[
Qx_{n+1}=Px_n+a_{i_n}.
\tag{2}
\]

Fix an integer `c` for which every shifted type `i_n+c` remains in
`{0,...,5}`.  If

\[
y_0=\left({9\over8}\right)^c x_0
\]

is an ordinary integer, then

\[
\boxed{y_n=\left({9\over8}\right)^c x_n}
\tag{3}
\]

is an exact ordinary orbit with shifted type code

\[
\boxed{i_n+c.}
\tag{4}
\]

Indeed, multiplying `(2)` by `(9/8)^c` and applying `(1)` gives

\[
Qy_{n+1}=Py_n+a_{i_n+c}.
\]

This is a genuine physical conjugacy, not merely a relation among symbolic
completions.

## 2. Ordinary divisibility gates

For `c>=0`, the upward shift `(3)` is ordinary whenever

\[
8^c\mid x_0.
\]

For a downward shift by `c>=0`,

\[
y_0=\left({8\over9}\right)^c x_0
\]

is ordinary whenever

\[
9^c\mid x_0.
\]

On an actual six-branch orbit the current and previous types are recovered by

\[
\nu_2(x_n)=15-3i_n,
\qquad
\nu_3(x_{n+1})=2i_n.
\tag{5}
\]

Consequently, if a tail beginning at time `n+1` has every type at least `c` and
`i_n>=c`, then

\[
\boxed{
\left({8\over9}\right)^c x_{n+1}}
\tag{6}
\]

is automatically a positive ordinary all-time root whose code is the shifted
tail

\[
i_{n+1}-c,i_{n+2}-c,\ldots.
\]

No inverse-limit digit is being supplied: divisibility follows from the
ordinary state itself through `(5)`.

## 3. Least-root zero-type corollary

Assume that the positive all-time root set is nonempty, and let `x_*` be its
least element.  Let its type code be `(i_n)`.

Then

\[
\boxed{\min_{n\ge0}i_n=0.}
\tag{7}
\]

Suppose instead that every `i_n>=1`.  Equation `(5)` makes `9|x_1`, and Section
2 gives the positive ordinary all-time root

\[
y={8x_1\over9}
\]

with code `i_1-1,i_2-1,...`.

But

\[
9Qx_*-8Qx_1=(9Q-8P)x_*-8a_{i_0}.
\tag{8}
\]

Here

\[
9Q-8P=467064,
\]

and every legal positive root is at least the least source residue

\[
6472>7.
\]

Since

\[
467064\cdot8>8a_5,
\]

`(8)` is positive. Therefore

\[
0<y<x_*,
\]

contradicting minimality.  This proves `(7)`.

Equivalently, every stabilizing least-root candidate must execute the type-zero
macro

```text
AAAAAB
```

at least once.

## 4. Completion form

For a one-sided type code define its compatible `Q`-adic completion

\[
\Phi(i)=-\sum_{n\ge0}{a_{i_n}Q^n\over P^{n+1}}.
\]

Whenever all shifted indices are valid, `(1)` also gives

\[
\boxed{\Phi(i+c)=\left({9\over8}\right)^c\Phi(i).}
\]

The ordinary statement above is stronger: it identifies exactly when the
scaled completion is represented by a finite positive integer.

## 5. Strategic meaning

The type labels are not six unrelated symbols; they are one geometric orbit.
Any positive construction confined away from the lower type boundary produces
a new ordinary root by exact scaling.  In particular, a least root cannot live
entirely in types `{1,...,5}`.

This does not prove that type zero recurs infinitely often and does not decide
boundedness.  It gives a mandatory boundary contact for every stabilizing
candidate and an exact normalization available on type-confined tails.

## 6. Gap audit

- A tail shift may produce a root larger than the global least root, so eventual
  avoidance of type zero is not excluded by this lemma alone.
- The upward conjugacy normally increases the root and gives no minimality
  contradiction.
- No infinite root or Collatz counterexample is constructed.
