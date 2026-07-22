# L-9807 — Exact first-crossing reduction for H cylinders

Claim ID: `L-9807`  
Title: A first expanding-to-contracting H crossing is one sharp carry inequality  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `PR19/L-9511`; the exact H concatenation identities restated below  
Scope: the unresolved first-crossing case of `PR19/C-9501`  
Related counterexample candidates: none

## Definitions

For an exact word `w`, write its normalized affine map and canonical endpoint as

\[
f_w(x)=\frac{V_wx+B_w}{U_w},
\qquad Y_w=f_w(A_w),
\]

where `0<=A_w<U_w` is the canonical input residue. Its multiplier gap and
signed displacement are

\[
D_w=U_w-V_w,
\qquad \Delta_w=A_w-Y_w.
\]

For a concatenation, `h,j` denote the unique interface carries in their
canonical ranges.

## Statement

Let `u` be an exact H word whose canonical normalized affine data are

\[
U=2^{E_u},\qquad V=3^{S_u},\qquad
0\le A<U,\qquad 0\le Y<V.
\]

Assume `u` is expanding and already lies on the conjectured side of its fixed
point. Equivalently, write

\[
V=U+e,\qquad Y=A+c,
\qquad 0<c<e.
\tag{1}
\]

Append one contracting H letter `r in {0,1,2}` and put

\[
P=2^{3r+2},\qquad Q=3^{2r+1},\qquad
d=P-Q>0,
\qquad
\delta=\frac{d-1}{4}.
\tag{2}
\]

Let `h,j` be the canonical carries at the interface:

\[
Y+hV=\frac P4+jP,
\qquad 0\le h<P,\quad 0\le j<V.
\tag{3}
\]

Then the displacement and multiplier gap of the concatenated word `ur` are

\[
\boxed{D_{ur}=dU-Qe,}
\tag{4}
\]

\[
\boxed{\Delta_{ur}=\delta+jd-c-he.}
\tag{5}
\]

Consequently, whenever `ur` is the first contracting prefix, so that
`D_(ur)>0`, the unresolved half of `PR19/C-9501` is exactly

\[
\boxed{c+he\le\delta+jd.}
\tag{6}
\]

This is the nonnegative-displacement assertion. Since a word with an expanding
prefix is not the all-zero word, the equality clause of `PR19/C-9501` would
require the strict strengthening

\[
c+he<\delta+jd.
\tag{6a}
\]

Equivalently, with

\[
x=A+hU,
\qquad T=Y+hV,
\]

condition (6) is the strict rational comparison

\[
\boxed{Px>QT.}
\tag{7}
\]

Thus the nonnegative-displacement part of the first-crossing problem is reduced
to a word-specific comparison between the two interface carries, with (6a)
recording the additional equality boundary. The canonical carry rectangle
alone does not imply (6); `R-9802` gives an exact abstract countermodel.

## Proof

For an exact word `w`, write

\[
D_w=U_w-V_w,
\qquad \Delta_w=A_w-Y_w.
\]

The one-letter data in (2) have

\[
D_r=d,
\qquad
\Delta_r=\frac P4-\frac{Q+1}{4}
=\frac{d-1}{4}=\delta.
\tag{8}
\]

Exact concatenation gives

\[
D_{ur}=P D_u+V D_r,
\qquad
\Delta_{ur}=\Delta_u+\Delta_r+hD_u+jD_r.
\tag{9}
\]

By (1), `D_u=-e` and `Delta_u=-c`. Substitution in (9) gives

\[
D_{ur}=-Pe+(U+e)d=dU-Qe
\]

and (5). If `D_(ur)>0`, the already-proved canonical endpoint bound gives
`Delta_(ur)<D_(ur)`; the missing sign assertion is precisely
`Delta_(ur)>=0`, which is (6).

It remains to prove the alternate form. Equation (3) and (1) give

\[
T=x+c+he=P\left(j+\frac14\right).
\]

Therefore

\[
Px-QT
=P\left(\delta+jd-c-he+\frac14\right)
=P\left(\Delta_{ur}+\frac14\right).
\tag{10}
\]

Because `Delta_(ur)` is an integer, the right-hand side is positive exactly
when `Delta_(ur)>=0`. This proves (7) and the reduction. ∎

## Motivation

`PR19/L-9512` closes same-sign concatenation. The source therefore singles out
the first expanding prefix followed by a contracting letter as the
highest-leverage mixed-sign lane. This lemma removes all remaining affine
bookkeeping from that lane: only (6), or equivalently (7), still needs
Collatz-specific input, with (6a) needed for the equality clause.

## Dependency audit

- `PR19/L-9511` is used after (9) only for the proved upper bound
  `Delta_(ur)<D_(ur)` when `D_(ur)>0`; the concatenation formulas are restated
  and checked directly.
- No empirical instance of `PR19/C-9501` is used.
- The restriction `r in {0,1,2}` is exactly the range of contracting H
  one-letter multipliers.

## Gap audit

- Inequalities (6) and (6a) are not proved here. They are exact normal forms for
  the remaining sign and equality steps.
- Bounds `0<=h<P` and `0<=j<V`, even together with (1), are insufficient;
  actual H offset structure must be used.
- Random or bounded word searches cannot promote the missing inequality.

## Adversarial tests

- For `r=0`, one has `d=1` and `delta=0`, so (6) becomes the sharp condition
  `c+he<=j`.
- Near the multiplier-one boundary, `dU-Qe` can be positive while very small;
  replacing (6) by a coarse ratio estimate loses the needed integer margin.
- `R-9802` satisfies every displayed coarse range and sign condition but
  reverses (6), showing exactly where a non-word argument fails.

## Remaining uncertainty

Whether actual H offsets always force (6), and force (6a) away from the
all-zero word, is the open content of `PR19/C-9501` in the first-crossing case.

## Suggested next attack

Insert the exact offset sum

\[
B_u=\frac14\sum_k 2^{E_k}3^{S_u-S_k}
\]

into the interface comparison (7), or express the sign of `Px-QT` in the
canonical 2-adic ghost digits. Any proof must exclude the abstract geometry of
`R-9802` by using this word-specific structure.
