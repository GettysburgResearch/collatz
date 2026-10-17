# R-8202 — Eventually affine run schedules select irrational cores

**Claim ID:** `R-8202`  
**Type:** refutation / source-qualified exclusion  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** frozen PR #51 `L-8004`; Amou–Matala-aho–Väänänen (2007), Theorem 5.1  
**Scope:** divisible-seven `+1` run-core schedules that are eventually affine with positive slope  
**Related counterexample candidates:** none

## Refuted positive target

`Q-8202` proposed the explicit aperiodic schedule

\[
r_n=64+n.
\]

It satisfies the physical-growth and moving-top-refund cones, but it does **not** have an ordinary initial core. More generally, no schedule that is eventually

\[
\boxed{r_n=R+dn,\qquad R\ge0,\ d\ge1}
\tag{1}
\]

has a rational, and hence no positive ordinary, core.

## 1. Exact selected core

For the divisible-seven normalization of PR #51 `L-8004`, an exact run transition is

\[
\boxed{
2^{4+3r_{n+1}}v_{n+1}=9^{r_n+1}v_n+1.}
\tag{2}
\]

Assume `(1)` from time zero. Put

\[
a_n=4+3r_{n+1}=3dn+3R+3d+4,
\]

\[
b_n=r_n+1=dn+R+1,
\]

and

\[
A_j=\sum_{h<j}a_h,
\qquad
B_j=\sum_{h<j}b_h.
\]

Solving `(2)` backwards through `N` transitions gives

\[
\boxed{
 v_0
 =-
 \sum_{j=0}^{N-1}
 {2^{A_j}\over9^{B_{j+1}}}
 +{2^{A_N}\over9^{B_N}}v_N.}
\tag{3}
\]

Every legal `v_N` is odd, while `A_N` tends to infinity. Hence the terminal term tends to zero in `Q_2`, and

\[
\boxed{
 v_0
 =-
 \sum_{j\ge0}{2^{A_j}\over9^{B_{j+1}}}
 \quad\text{in }\mathbf Q_2.}
\tag{4}
\]

Define

\[
q=\left({8\over9}\right)^d,
\qquad
z={2^{3R+3d+4}\over9^{R+d+1}},
\tag{5}
\]

and

\[
F_q(Z)=\sum_{j\ge0}q^{j(j-1)/2}Z^j.
\tag{6}
\]

The first term of `(4)` is `9^(-(R+1))`, and consecutive terms have ratio

\[
{2^{a_j}\over9^{b_{j+1}}}=zq^j.
\]

Therefore

\[
\boxed{
 v_0=-9^{-(R+1)}F_q(z).}
\tag{7}
\]

This is an equality in `Q_2`; no real/finite-place limit identification is used.

## 2. Functional equation and nonrationality

The series `(6)` satisfies

\[
\boxed{F_q(Z)=1+Z F_q(qZ).}
\tag{8}
\]

It is not rational over `Q(Z)`. Indeed, its coefficients

\[
c_n=q^{n(n-1)/2}
\]

would otherwise satisfy a nonzero constant-coefficient linear recurrence for all sufficiently large `n`. Dividing such a recurrence by `c_n` would give one nonzero polynomial vanishing at infinitely many distinct values `q^n`, impossible because `q` is not a root of unity.

Thus `1,F_q(Z)` are linearly independent over `Q(Z)`.

## 3. Primary-source theorem

Apply Theorem 5.1 of:

> M. Amou, T. Matala-aho and K. Väänänen,  
> “On Siegel–Shidlovskii’s theory for q-difference equations,”  
> *Acta Arithmetica* 127 (2007), 309–335,  
> DOI `10.4064/aa127-4-2`.

The source equation is

\[
Z^s f(qZ)=a(Z)Cf(Z)+b(Z).
\]

Equation `(8)` is the case

\[
K=\mathbf Q,\quad v=2,\quad m=s=1,\quad
 a(Z)=1,\quad C=1,\quad b(Z)=-1.
\tag{9}
\]

The evaluation point `z` in `(5)` is nonzero rational and `a(zq^k)=1`, so the evaluation orbit is nonsingular.

For `q=(8/9)^d` in lowest terms,

\[
H(q)=9^d,
\qquad
|q|_2=2^{-3d},
\]

so the source parameter is independent of `d`:

\[
\lambda={\log H(q)\over\log|q|_2}
=-{2\over3}\log_2 3
=-\gamma.
\tag{10}
\]

Take the source choice `delta=1/2`. For `m=s=1`, its formulas give

\[
K_\delta={31\over24},
\]

\[
24\rho_0^2-112\rho_0-217=0,
\]

and

\[
{B(\rho_0)\over A(\rho_0)}
=\beta={2\sqrt{2086}-7\over79}.
\tag{11}
\]

The exact inequalities

\[
\beta>{16\over15}>\gamma>1
\tag{12}
\]

follow from

\[
30^2\cdot2086>1369^2,
\qquad
3^5<2^8,
\qquad
9>8.
\]

Hence

\[
-\beta<\lambda\le-1,
\]

which is exactly the source hypothesis. Theorem 5.1 therefore gives

\[
\boxed{1,F_q(z)\text{ are linearly independent over }\mathbf Q.}
\tag{13}
\]

In particular, `F_q(z)` is irrational. Equation `(7)` makes `v_0` irrational.

## 4. Eventually affine schedules

Suppose the run schedule becomes `(1)` only after a finite prefix. The tail core at that time is irrational by the preceding theorem. Every preceding inverse run step is a nonconstant rational affine transformation

\[
v_n={2^{4+3r_{n+1}}v_{n+1}-1\over9^{r_n+1}}.
\]

A finite composition of such maps sends an irrational number to an irrational number. Therefore the original initial core is also irrational.

Thus:

\[
\boxed{
\text{no eventually affine positive-slope run schedule has an ordinary core.}}
\tag{14}
\]

## Consequences

1. The explicit schedule `r_n=64+n` from `L-8204/Q-8202` is excluded.
2. Merely making the run resource grow linearly cannot close the ordinary section.
3. A successful positive schedule must be genuinely non-eventually-affine.
4. PR #51 `T-8003` remains useful: the positive target may use a nonlinear schedule satisfying the weaker exact resource condition
   \[
   \sum_{h=0}^{8}r_{J+9m+h}\ge44.
   \]

## Gap and source audit

- The source PDF was inspected at printed pages 319–320, including definitions `(5.2)–(5.4)` and Theorem 5.1.
- The theorem is applied at one finite place only; no real limit is substituted for the `2`-adic value.
- Functional independence is proved directly above rather than assumed from a nearby stack claim.
- The result excludes one broad schedule class; it does not exclude nonlinear or adaptive run schedules.
- The source theorem itself is an external black box and should receive another independent source-level review before repository status promotion.

## Verification

`X-8203` reconstructs `(3)–(8)` on exact finite prefixes, checks the source parameter arithmetic, and verifies the canonical-absorption constants from the concurrent PR #49 delta.
