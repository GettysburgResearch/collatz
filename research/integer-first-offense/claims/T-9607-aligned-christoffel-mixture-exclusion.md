# T-9607 — Aligned mixtures of Christoffel conjugate blocks cannot form positive cycles

**Claim ID:** `T-9607`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** `L-9606`, `L-9607`, `T-9606`  
**Scope:** repeated aligned choices between the two standard conjugates of one primitive rational mechanical block

## 1. Standard conjugate pair

Let

\[
0<p<q,
\qquad
\gcd(p,q)=1,
\tag{1}
\]

and let the lower mechanical valuation word of slope `p/q` have its standard Farey-parent factorization

\[
\boxed{w=uv.}
\tag{2}
\]

Thus the parent slopes are Farey neighbors and the other standard conjugate is

\[
\widetilde w=vu.
\tag{3}
\]

Both words have

\[
k=q,
\qquad
A=p+q.
\tag{4}
\]

Put

\[
P=3^q,
\qquad
Q=2^{p+q},
\qquad
C=C_w,
\qquad
\widetilde C=C_{\widetilde w}.
\tag{5}
\]

By `L-9606`,

\[
\boxed{
\delta=C-\widetilde C=\pm2^a3^b}
\tag{6}
\]

for explicit nonnegative integers `a,b` determined by the two Farey parents.

## 2. Aligned repeated-block grammar

Fix `R>=1`. At each of `R` aligned block positions, choose either `w` or `w_tilde`. For

\[
\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{R-1})
\in\{0,1\}^R,
\]

write

\[
W_\varepsilon=w_{\varepsilon_0}\cdots w_{\varepsilon_{R-1}},
\qquad
w_0=w,
\quad
w_1=\widetilde w.
\tag{7}
\]

The theorem is

\[
\boxed{
W_\varepsilon\text{ is never a nontrivial positive accelerated cycle certificate.}}
\tag{8}
\]

This holds for every binary pattern and every repetition count.

## 3. Full geometric-factor sieve

Define

\[
G_R={Q^R-P^R\over Q-P}
=\sum_{m=0}^{R-1}P^{R-1-m}Q^m.
\tag{9}
\]

The number `G_R` is coprime to six. Indeed, its first summand is odd and every later summand is even, so `G_R` is odd. Modulo three, every summand containing `P` vanishes and the final term is the unit `Q^(R-1)`.

Consequently `(6)` gives

\[
\boxed{\gcd(\delta,G_R)=1.}
\tag{10}
\]

Apply the equal-summary mixture theorem `L-9607`. If the full cycle denominator divides the numerator of `W_epsilon`, then `(10)` forces the selected geometric subsum to be either zero or all of `G_R`. Hence

\[
\boxed{
\varepsilon=0^R
\quad\hbox{or}\quad
\varepsilon=1^R.}
\tag{11}
\]

Thus every possible cycle hit in the aligned grammar would have to be the pure power

\[
w^R
\qquad\hbox{or}\qquad
\widetilde w^R.
\tag{12}
\]

## 4. Final exclusion

`T-9606` proves that neither primitive rational mechanical word `w` nor its conjugate `w_tilde` is a nontrivial positive cycle certificate. The exact power-collapse identity says a powered word certifies precisely when its primitive root does and has the same reduced fixed point.

Therefore neither word in `(12)` certifies a nontrivial cycle. Combined with `(11)`, this proves `(8)`. ∎

## 5. Constructive boundary

The theorem closes a large and tempting repair grammar:

```text
repeat one primitive mechanical block R times;
independently choose the lower or upper standard conjugate in each copy.
```

Although every local conjugation changes the numerator by one exact `{2,3}`-unit, the aligned contextual weights share the geometric denominator factor `G_R`. That factor enforces an all-or-none orientation.

A viable Christoffel repair circuit must therefore break alignment. The surviving mechanisms are:

1. swaps nested at different Farey scales inside a copy;
2. overlapping or context-dependent standard-factor swaps;
3. at least three block constants whose differences share controlled factors with `G_R`;
4. scale-varying summaries rather than one repeated summary.

This is a positive design constraint, not merely a negative census.

## Gap audit

- Nonaligned hierarchical repairs remain open.
- A three-or-more-block alphabet may evade the binary all-or-none sieve.
- The theorem constructs no full-denominator identity and no Collatz counterexample.

## Verification

`X-9611` checks the geometric-factor identity and all-or-none conclusion on every primitive rational mechanical block of denominator at most `30`, every repetition count through `12`, and every aligned binary orientation pattern.