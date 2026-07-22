# L-9314 — Exact nearest-integer cylinder block

**Claim ID:** L-9314  
**Title:** Every itinerary extension appends one explicitly computable base-`M` block to its nearest-integer cylinder  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `L-9313`; elementary affine iteration  
**Scope:** every coprime binary expanding chart; the exact block-tail target for `64 -> 81`  
**Related counterexample candidates:** none

## 1. Finite nearest-integer cylinder

Fix coprime integers

\[
2\le M<N
\]

and binary digits

\[
e_0,\ldots,e_K.
\]

Put

\[
\boxed{d_i=e_i-e_{i+1}\in\{-1,0,1\}.}
\tag{1}
\]

The nearest-integer recurrence is

\[
\boxed{M B_{i+1}=N B_i+d_i.}
\tag{2}
\]

For every `K>=1`, let

\[
0\le R_K<M^K
\]

be the unique initial residue for which `(2)` is integral through the first `K` transitions `i=0,...,K-1`.

Equivalently,

\[
\boxed{
R_K
\equiv
-
\sum_{i=0}^{K-1}
d_i M^i N^{-(i+1)}
\pmod{M^K}.
}
\tag{3}
\]

Let `C_K` be the resulting ordinary terminal nearest integer. Then

\[
\boxed{
M^K C_K
=
N^K R_K
+
\sum_{i=0}^{K-1}
N^{K-1-i}M^i d_i.
}
\tag{4}
\]

## 2. The appended block digit

Nestedness gives a unique digit

\[
\boxed{
q_K
=
\frac{R_{K+1}-R_K}{M^K}
\in\{0,1,\ldots,M-1\}.
}
\tag{5}
\]

It is determined exactly by

\[
\boxed{
q_K
\equiv
-N^{-(K+1)}(NC_K+d_K)
\pmod M.
}
\tag{6}
\]

The residue on the right is read in `0,...,M-1`, so `(6)` specifies the ordinary integer `q_K` uniquely.

The new terminal value is

\[
\boxed{
C_{K+1}
=
\frac{N(C_K+q_KN^K)+d_K}{M}.
}
\tag{7}
\]

## 3. Proof

Changing the initial representative from `R_K` to

\[
R_K+qM^K
\]

changes the state after `K` transitions by exactly

\[
qN^K.
\tag{8}
\]

Indeed, the homogeneous multiplier across `K` steps is `(N/M)^K`, and the factor `M^K` cancels its denominator.

Thus the candidate terminal state before the new transition is

\[
C_K+qN^K.
\]

The transition at time `K` is integral exactly when

\[
N(C_K+qN^K)+d_K
\equiv0\pmod M.
\tag{9}
\]

Since `N` is a unit modulo `M`, equation `(9)` has one solution `q mod M`. Solving gives `(6)`, and division of the numerator gives `(7)`.

Formula `(3)` follows from `(4)` modulo `M^K`. QED.

## 4. Zero-block criterion

The cylinder does not move at extension `K` exactly when

\[
\boxed{
q_K=0
\iff
NC_K+d_K\equiv0\pmod M.
}
\tag{10}
\]

Thus a run

\[
q_K=q_{K+1}=\cdots=q_{K+L-1}=0
\]

means that the same ordinary representative `R_K` realizes `L` additional nearest-integer transitions.

An infinite itinerary selects an ordinary nonnegative nearest integer exactly when `q_K=0` eventually.

## 5. The `64 -> 81` specialization

Set

\[
M=64,
\qquad
N=81.
\]

Then

\[
\boxed{
q_K
\equiv
-81^{-(K+1)}
(81C_K+e_K-e_{K+1})
\pmod{64}.
}
\tag{11}
\]

Since

\[
81\equiv17\pmod{64},
\qquad
17^{-1}\equiv49\pmod{64},
\]

the zero-block cases are

\[
\boxed{
\begin{array}{c|c|c}
(e_K,e_{K+1})&d_K&C_K\pmod{64}\text{ required for }q_K=0\\
\hline
(0,0),(1,1)&0&0\\
(1,0)&1&15\\
(0,1)&-1&49.
\end{array}
}
\tag{12}
\]

This is the same three-state table appearing in `L-9312`, now attached to the terminal state of the finite nearest-integer cylinder.

## 6. One-step uniqueness of an unchanged cylinder

For a fixed prefix through `e_K`, the two choices of `e_(K+1)` change `d_K` by one. Their block digits therefore satisfy

\[
\boxed{
q_K^{(1)}-q_K^{(0)}
\equiv81^{-(K+1)}\pmod{64}.
}
\tag{13}
\]

The right side is a unit. Consequently,

\[
\boxed{
\text{at most one of the two one-digit extensions can have }q_K=0.
}
\tag{14}
\]

A hypothetically stabilizing itinerary is therefore uniquely forced at every stage after stabilization begins.

This does not imply periodicity: the forcing rule still depends on the unbounded terminal integer `C_K`.

## 7. Completion interpretation

The digits `(q_K)` are the base-`M` digits of the inverse-limit nearest integer selected by the itinerary. For `M=64`, this is the `2`-adic point of `L-9313`.

Eventual zero of `(q_K)` is exactly ordinary stabilization.

## 8. Cross-program relationship

`L-9314` is the direct full-binary analogue of the block-tail variable in PR #20's active-cylinder theorem:

- a finite directive fixes one initial cylinder;
- extending the directive appends one radix block;
- the unused quotient is transported by an odd affine map;
- ordinary closure is eventual zero of the appended blocks.

Here the centered errors provide a bounded real coordinate, and `(6)` gives the appended block without backward search.

## 9. Dependency audit

- Finite-cylinder uniqueness and stabilization are from `L-9313`.
- Equations `(4)`--`(9)` are direct affine iteration.
- No Fourier theorem, computation, external Diophantine theorem, PR #20 claim, or issue-#4 unmerged theorem is used.

## 10. Gap audit

- Formula `(6)` does not prove infinitely many nonzero blocks.
- The terminal values `C_K` are unbounded state; the three residue cases do not close at a finite level.
- One uniquely forced stabilizing continuation could in principle remain aperiodic.
- A long zero-block run is merely a long ordinary finite survivor, which is abundant at finite depth.
- Translation to all possible Collatz counterexamples remains separate.

## 11. Correct next attack

Assume `q_K=0` from some point onward. Then `(12)` forces the future digit from `C_K mod64`, while `(7)` reduces to one ordinary expanding recurrence.

Seek an invariant of that forced orbit—return-word repetition, a reduced shifted-value determinant, or a phase-crossing law—that contradicts indefinite zero blocks.