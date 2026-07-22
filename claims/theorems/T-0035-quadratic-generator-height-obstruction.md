# T-0035 — Height obstruction for fixed polynomial quadratic-generator schemas

Claim ID: `T-0035`  
Title: No finite library of fixed polynomials in shifted quadratic bulk words can generate the canonical stage correction infinitely often  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0025`, `T-0030`, `T-0034`  
Scope: the positive ordinary quadratic bulk sequence and eventual canonical corrections of the corrected phase-34 stage  
Related counterexample candidates: none

## Setup

Recall the positive ordinary quadratic generator

\[
\boxed{
V_m={3^{7\cdot2^m}-1\over2^{m+2}},}
\tag{1}
\]

which satisfies

\[
V_{m+1}=V_m+2^{m+1}V_m^2.
\tag{2}
\]

`T-0034` proves that every assumed infinite ordinary corrected-stage path has
canonical corrections `R_m` satisfying

\[
\boxed{
\log_2R_m
=\Gamma2^m+O(m),}
\tag{3}
\]

where

\[
\boxed{
\Gamma
={687232\log_2 3-1085579\over256}.}
\tag{4}
\]

## Statement

Fix integers

\[
c_1,\ldots,c_s
\]

and a nonzero polynomial

\[
P\in\mathbb Q[X_1,\ldots,X_s].
\]

Then the equality

\[
\boxed{
R_m=P(V_{m+c_1},\ldots,V_{m+c_s})}
}
\tag{5}
\]

can hold for only finitely many sufficiently large scales `m` for which all
shifted indices are nonnegative.

The same conclusion holds for a finite library of fixed rational polynomials:
no rule selecting one polynomial from a finite set at each scale can represent
`R_m` at every sufficiently large scale.

In particular, the following candidate classes are impossible:

1. fixed affine transforms
   \[
   R_m=aV_m+b;
   \]
2. fixed-degree univariate polynomial transforms of `V_m`;
3. fixed rational polynomials in finitely many shifts
   \[
   V_{m-c},\ldots,V_m,\ldots,V_{m+c};
   \]
4. any finite-control selection among finitely many such formulas.

## Proof

Put

\[
B=2^m.
\]

For one shifted generator,

\[
V_{m+c}
=
2^{-m-c-2}
\left(3^{7\cdot2^cB}-1\right).
\tag{6}
\]

Expand every monomial of `P` using (6). Because `P` is fixed, the resulting
expression is a finite sum of terms of the form

\[
\boxed{
q\,2^{-dm}\,3^{7rB},}
\tag{7}
\]

where

\[
q\in\mathbb Q^*,
\qquad d\in\mathbb Z_{\ge0},
\qquad r\in\mathbb Z[1/2]_{\ge0}.
\tag{8}
\]

The dyadic rational `r` is a finite sum of shifted weights `2^c`, with
nonnegative integer coefficients, after choosing either the power-of-three or
the `-1` term from every factor.

Combine identical pairs `(r,d)`. Since `P` is nonzero, the resulting finite
exponential polynomial is not identically zero. Choose the lexicographically
largest pair `(r_*, -d_*)` with nonzero combined coefficient: first maximize
`r`, and among those terms minimize `d`.

Then, along every sufficiently large scale at which the polynomial value is
nonzero,

\[
\boxed{
\log_2
\left|
P(V_{m+c_1},\ldots,V_{m+c_s})
\right|
=
7r_*\log_2(3)\,2^m+O(m).}
\tag{9}
\]

Indeed, every term with smaller `r` is exponentially smaller in `2^m`; among
terms with the same `r`, every larger `d` is smaller by a power of `2^m`.

Suppose (5) held for infinitely many `m`. Comparing (3) and (9) would give

\[
\Gamma=7r_*\log_2 3.
\tag{10}
\]

Substitution of (4) yields

\[
\left(687232-1792r_*\right)\log_2 3
=1085579.
\tag{11}
\]

If the coefficient on the left vanished, (11) would read `0=1085579`. If it
did not vanish, (11) would make `log_2 3` rational because `r_*` is rational.
But rationality of `log_2 3` would imply

\[
2^a=3^b
\]

for some positive integers `a,b`, contradicting unique prime factorization.
Thus (10) is impossible, proving the first statement.

For a finite library, one polynomial occurs infinitely often; apply the proved
case to that subsequence. ∎

## Quantitative affine mismatch

The fixed affine ansatz is not merely nonresonant. Its bit length is too small.
Using `log_2 3>84/53` from `L-0025`,

\[
\begin{aligned}
\Gamma-7\log_2 3
&=
{685440\log_2 3-1085579\over256}\\
&>
\boxed{{41273\over13568}>3.}
\end{aligned}
\tag{12}
\]

Hence

\[
\log_2R_m-\log_2V_m
>3\cdot2^m-O(m).
\tag{13}
\]

Any affine multiplier capable of turning `V_m` into `R_m` must itself contain
more than `3*2^m-O(m)` bits. It cannot be a bounded coefficient or a finite
control label.

## Strategic consequence

The quadratic bulk remains valuable as a forward finite-word generator, but it
cannot be the entire ordinary correction track. A viable construction must add
an explicit binary renormalization channel of exponential size or use a more
substantial nonlinear combination whose scale includes both powers of `2` and
powers of `3`.

This closes the most literal version of the ansatz proposed after `T-0030`:

\[
z_m=\alpha V_m+\beta
\]

with fixed or finitely selected coefficients.

## Gap audit

- The theorem does not exclude coefficients whose bit length is itself
  `Theta(2^m)`.
- It does not exclude scale-dependent recurrences combining `V_m` with the
  canonical connector word.
- A polynomial identity with coefficients containing explicit powers such as
  `2^(c 2^m)` lies outside the fixed-polynomial class.
- No cap-stitch tail or counterexample is constructed.

## Adversarial tests

`X-0016` checks the exact exponent coefficient `Gamma`, the growth coefficient
of `V_(m+c)`, and the nonresonance identity for representative dyadic weights.
The universal proof is the finite exponential-polynomial expansion above.