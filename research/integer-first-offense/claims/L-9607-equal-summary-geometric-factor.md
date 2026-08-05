# L-9607 — Equal-summary block mixtures inherit a geometric-factor sieve

**Claim ID:** `L-9607`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** elementary affine-block concatenation  
**Scope:** finite words assembled from two accelerated blocks with equal length and total valuation

## 1. Equal-summary block pair

Let `u,v` be nonempty accelerated valuation words satisfying

\[
k_u=k_v=k,
\qquad
A_u=A_v=A.
\tag{1}
\]

Put

\[
P=3^k,
\qquad
Q=2^A,
\qquad
C=C_u,
\qquad
\widetilde C=C_v,
\tag{2}
\]

and

\[
\delta=C-\widetilde C.
\tag{3}
\]

For `R>=1`, let

\[
G_R=\sum_{m=0}^{R-1}P^{R-1-m}Q^m
={Q^R-P^R\over Q-P}.
\tag{4}
\]

Choose a binary pattern

\[
\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{R-1})
\in\{0,1\}^R,
\]

and form the chronological block word

\[
W_\varepsilon=w_0w_1\cdots w_{R-1},
\qquad
w_m=\begin{cases}u,&\varepsilon_m=0,\\v,&\varepsilon_m=1.\end{cases}
\tag{5}
\]

Define the selected geometric subsum

\[
H_\varepsilon
=\sum_{m:\varepsilon_m=1}P^{R-1-m}Q^m.
\tag{6}
\]

## 2. Exact numerator and denominator

The full affine data are

\[
\boxed{
C_{W_\varepsilon}=C G_R-\delta H_\varepsilon,}
\tag{7}
\]

and

\[
\boxed{
D_{W_\varepsilon}=Q^R-P^R=(Q-P)G_R.}
\tag{8}
\]

### Proof

Each block constant is either `C` or `C-delta`. Repeated use of

\[
C_{xy}=3^{k_y}C_x+2^{A_x}C_y
\]

shows that the block at chronological position `m` receives weight

\[
P^{R-1-m}Q^m.
\]

Summing the common contribution gives `C G_R`; subtracting the chosen differences gives `delta H_epsilon`. Equation `(8)` is the difference-of-powers factorization. ∎

## 3. Geometric-factor obstruction

If `W_epsilon` is a positive exact cycle certificate, then

\[
D_{W_\varepsilon}\mid C_{W_\varepsilon}.
\]

In particular, `(8)` forces

\[
G_R\mid C_{W_\varepsilon}.
\]

Using `(7)`, this is equivalent to

\[
\boxed{G_R\mid\delta H_\varepsilon.}
\tag{9}
\]

Therefore, whenever

\[
\boxed{\gcd(\delta,G_R)=1,}
\tag{10}
\]

one must have

\[
G_R\mid H_\varepsilon.
\]

All weights in `(6)` are positive and their complete sum is `G_R`. Hence

\[
0\le H_\varepsilon\le G_R,
\]

with equality at the endpoints only for the constant patterns. Thus `(10)` gives

\[
\boxed{
\varepsilon=0^R
\quad\hbox{or}\quad
\varepsilon=1^R.}
\tag{11}
\]

No genuinely mixed two-block word can satisfy the cycle divisibility condition.

## 4. Strength and limitations

The lemma is an exact **full geometric-factor** sieve. It is stronger than checking selected factors of `Q^R-P^R`: the entire quotient

\[
G_R={Q^R-P^R\over Q-P}
\]

is removed before any primitive denominator test remains.

The coprimality hypothesis is also the sharp boundary. If `delta` shares factors with `G_R`, a mixed pattern may survive this sieve and must be tested against the remaining quotient and the primitive factor `Q-P`.

## Constructive consequence

A repeated-block repair architecture can succeed only if at least one of the following occurs:

1. the available constant differences share nontrivial factors with `G_R`;
2. at least three equal-summary block constants create cancellation not reducible to one subset sum;
3. repairs occur at nonaligned internal scales, so their contextual weights are not the common block weights in `(6)`;
4. the block summaries themselves change with scale.

This precisely separates the dead aligned-conjugate grammar from the live hierarchical Christoffel repair program.

## Gap audit

- The lemma is a necessary sieve, not a cycle construction.
- More than two block constants are not covered by the all-or-none conclusion.
- A shared factor of `delta` and `G_R` is only permission to continue, not a certificate.
- No positive cycle or divergent orbit is claimed.