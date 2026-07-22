# L-9605 — Normalized centered half-join for accelerated cycle words

**Claim ID:** `L-9605`  
**Status:** `PROPOSED / EXACT SEARCH REDUCTION`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** elementary affine composition; the centered numerator identity used in `T-9601`--`T-9603`  
**Scope:** exact accelerated-cycle divisibility searches  
**Related counterexample candidates:** none

## 1. Centered affine summaries

For a finite accelerated valuation word `w`, let

\[
(k_w,A_w,E_w)
\]

be its centered affine summary, meaning that its branch acts on `y=n-1` by

\[
\boxed{
y\longmapsto {3^{k_w}y+E_w\over2^{A_w}}.}
\tag{1}
\]

For chronological concatenation `w=uv`, direct substitution gives

\[
\boxed{
E_{uv}=3^{k_v}E_u+2^{A_u}E_v,}
\tag{2}
\]

and

\[
k_{uv}=k_u+k_v,
\qquad
A_{uv}=A_u+A_v.
\tag{3}
\]

Put

\[
D_{uv}=2^{A_u+A_v}-3^{k_u+k_v}.
\tag{4}
\]

This denominator is odd and coprime to `3`.

## 2. Normalized half-join theorem

Every power of `2` and `3` is invertible modulo `D_(uv)`. Equation `(2)` therefore yields the exact equivalence

\[
\boxed{
D_{uv}\mid E_{uv}
\iff
E_u2^{-A_u}+E_v3^{-k_v}\equiv0\pmod{D_{uv}}.
}
\tag{5}
\]

Here the negative exponents mean modular inverses modulo `D_(uv)`.

### Proof

Multiply `(2)` by the unit

\[
2^{-A_u}3^{-k_v}
\]

modulo `D_(uv)`. The two terms become respectively

\[
E_u2^{-A_u}
\quad\text{and}\quad
E_v3^{-k_v}.
\]

Multiplication by a unit preserves whether a residue is zero. This proves `(5)`. ∎

## 3. Block summaries

A block consisting of one exceptional valuation `b!=2` followed by `r>=0` neutral valuations `2` has summary

\[
\boxed{
(k,A,E)=
(1+r,\,b+2r,\,3^r(4-2^b)).
}
\tag{6}
\]

Thus a half-word can be evaluated by repeated use of

\[
(k,A,E)\star(k',A',E')
=
(k+k',\,A+A',\,3^{k'}E+2^AE').
\tag{7}
\]

No expanded valuation word is needed.

## 4. Exact meet-in-the-middle architecture

Suppose an `s`-defect word is rotated so that a largest neutral gap `t` is terminal and then removed. Its remaining neutral gaps satisfy

\[
r_i\le t,
\qquad
\sum r_i=R-t.
\tag{8}
\]

Split the `s` exceptional blocks into a left and right part. For every left configuration store

\[
\boxed{
\lambda=E_L2^{-A_L}\pmod D,}
\tag{9}
\]

indexed additionally by:

- the exceptional-letter multiset used on the left;
- the left neutral-gap sum.

For every right configuration compute

\[
\boxed{
\rho=E_R3^{-k_R}\pmod D.}
\tag{10}
\]

The full word is a divisor hit exactly when the complementary multiset and gap-sum keys match and

\[
\boxed{
\lambda+ho\equiv0\pmod D.}
\tag{11}
\]

This covers every largest-gap-normalized word and produces no false positives or false negatives.

## 5. Independence from the split

Equation `(5)` holds at every cut. Consequently a `5+5` join and a `4+6` join test the same full divisibility condition while generating genuinely different half-state collections.

This permits an adversarial verification architecture:

```text
authoring search:     5+5 split, direct block summaries;
independent verifier: 4+6 split, separately generated patterns and gaps.
```

Agreement of their exact full-candidate counts and empty hit sets is stronger than rerunning one implementation with different parameters.

## 6. Candidate-count certificate

For a fixed terminal largest gap `t`, let

\[
L(c,g),\qquad R(c,g)
\]

count left and right half-configurations using exceptional multiset code `c` and neutral-gap sum `g`. If `c^*` is the complementary multiset and the core neutral total is `m=R-t`, then the exact number of full covered candidates is

\[
\boxed{
\sum_{c,g}L(c,g)R(c^*,m-g).
}
\tag{12}
\]

Thus the implementation can certify not merely an empty join but the precise raw family cardinality it represents.

## 7. Boundary

- `L-9605` is an exact finite-search reduction, not an asymptotic no-cycle theorem.
- The number of half states can still grow rapidly with defect count and neutral-gap cutoff.
- A zero normalized join must still be converted into the full integer word and replayed, although the centered divisibility theorem guarantees the relevant fixed-point condition.
- No positive cycle or Collatz counterexample is constructed.

`X-9608` applies this lemma to the complete ten-defect frontier.
