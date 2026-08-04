# L-9703 — Normalized offset bound for the corrected 256-stage map

**Claim ID:** `L-9703`  
**Title:** Every corrected stage has affine offset smaller than 256 copies of its full multiplier  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** frozen PR #3 local residual interface and exponent schedule; elementary integer inequalities  
**Scope:** every admissible tower-type word in one corrected phase-`-34` 256-transition stage  
**Related counterexample candidates:** none

## Statement

Fix one corrected stage at scale `m >= 8`. Put

\[
B=2^m,
\qquad
d=B/256,
\]

and use the PR #3 heights

\[
t_j=B+jd
\qquad(0\le j\le256),
\]

with

\[
t_{257}=2B+2d.
\]

For `0 <= j < 256`, write the exact local residual map as

\[
z_{j+1}=\lambda_j z_j+c_j
=
\frac{N_jz_j+C_j}{q_j},
\tag{1}
\]

where

\[
N_j=3^{7(t_j+1)},
\qquad
q_j=2^{11(t_{j+2}+1)},
\qquad
C_j=\theta_j-\eta_{j+1}.
\tag{2}
\]

Let the complete stage be

\[
z_{256}=\Lambda_m z_0+\beta_m
=
\frac{N_mz_0+C_m}{q_m},
\tag{3}
\]

where

\[
\Lambda_m=\prod_{j=0}^{255}\lambda_j,
\qquad
N_m=\prod_{j=0}^{255}N_j,
\qquad
q_m=\prod_{j=0}^{255}q_j.
\tag{4}
\]

Then, uniformly in every stage type word:

### 1. Every local slope is strictly expanding

\[
\boxed{\lambda_j>1
\qquad(0\le j<256).}
\tag{5}
\]

More precisely, for `0 <= j <=254`,

\[
\boxed{
\log_2\lambda_j
>
\frac{57}{6784}B+rac5{53},}
\tag{6}
\]

and for `j=255`,

\[
\boxed{
\log_2\lambda_{255}
>
\frac{403}{6784}B+rac5{53}.}
\tag{7}
\]

### 2. Every normalized local offset is smaller than its local slope

\[
\boxed{|c_j|<\lambda_j.}
\tag{8}
\]

### 3. Complete normalized offset bound

\[
\boxed{|\beta_m|<256\Lambda_m.}
\tag{9}
\]

Equivalently, in the exact integer presentation of the complete stage,

\[
\boxed{|C_m|<256N_m.}
\tag{10}
\]

The bound is independent of the selected tower-type word.

## Definitions

The connector digits are canonical:

\[
0\le\theta_j<N_j,
\qquad
0\le\eta_{j+1}<q_j.
\]

The complete normalized affine offset is

\[
\beta_m=C_m/q_m.
\]

No sign is asserted for `C_m` or `beta_m`.

## Motivation

`T-9703` shows that every hypothetical ordinary 256-stage trajectory eventually
has zero free quotient. The resulting cap-correction recurrence is

\[
R_{m+1}=\Lambda_mR_m+\beta_m.
\]

A useful global-height theorem therefore needs a type-word-uniform bound on the
inhomogeneous term. Equation (9) supplies exactly that bound and exposes the
stage surplus `Lambda_m` as the only asymptotically significant archimedean
scale.

## Proof

Put

\[
\sigma=7\log_2 3-11.
\]

The exact integer inequality

\[
3^{53}>2^{84}
\]

gives

\[
\sigma>\frac5{53}.
\tag{11}
\]

For every local step,

\[
\begin{aligned}
\log_2\lambda_j
&=7(t_j+1)\log_2 3-11(t_{j+2}+1)\\
&=\sigma(t_j+1)-11(t_{j+2}-t_j).
\end{aligned}
\tag{12}
\]

For `0 <= j <=254`,

\[
t_{j+2}-t_j=2d,
\qquad
t_j\ge B.
\]

Hence

\[
\begin{aligned}
\log_2\lambda_j
&>\frac5{53}(B+1)-22\frac B{256}\\
&=\frac{57}{6784}B+\frac5{53}>0.
\end{aligned}
\]

For the last step,

\[
t_{255}=\frac{511}{256}B,
\qquad
t_{257}-t_{255}=3d.
\]

Therefore

\[
\begin{aligned}
\log_2\lambda_{255}
&>\frac5{53}\left(\frac{511}{256}B+1\right)
 -33\frac B{256}\\
&=\frac{403}{6784}B+\frac5{53}>0.
\end{aligned}
\]

This proves (5)--(7).

For the offset bound, canonical connector digits give

\[
-q_j<C_j<N_j.
\tag{13}
\]

If `C_j>=0`, then

\[
|c_j|=C_j/q_j<N_j/q_j=\lambda_j.
\]

If `C_j<0`, then

\[
|c_j|<1<\lambda_j.
\]

Thus (8) holds.

Composition of the affine maps (1) gives

\[
\beta_m
=
\sum_{j=0}^{255}
 c_j\prod_{k=j+1}^{255}\lambda_k.
\tag{14}
\]

By (8), the absolute value of the `j`-th summand is strictly less than

\[
\prod_{k=j}^{255}\lambda_k.
\]

Every omitted earlier factor is greater than one by (5), so every suffix product
is at most the full product `Lambda_m`. There are 256 summands. Hence

\[
|\beta_m|<256\Lambda_m,
\]

proving (9). Multiplying by `q_m` and using

\[
\Lambda_m=N_m/q_m
\]

gives (10). ∎

## Dependency audit

- The PR #3 local zipper supplies (1)--(2) and the canonical bounds on `theta`
  and `eta`; its native status remains `PROPOSED`.
- The two exact integer comparisons `3^53>2^84` and the dyadic height arithmetic
  supply all real inequalities.
- No stage-cap theorem, entropy result, p-adic logarithm, or experiment is used.

## Gap audit

- The lemma bounds the inhomogeneous term but does not decide its sign.
- It does not prove a cap-correction chain exists.
- The condition `lambda_j>1` uses the corrected fixed 256-cell lane. An arbitrary
  adaptive height lane needs its own gap audit.
- A small normalized offset is not an exact cylinder-membership theorem.

## Adversarial tests

`X-9703` checks the coefficient inequalities at 25 scales and exhaustively
composes 82,082 small expanding canonical chains satisfying the same local
bounds. Its independently written checker uses different odd bases, radices,
and direct compositions.

## Remaining uncertainty

The complete-looking proof should be reviewed for the exceptional last height
`t_257` and for the strict local offset interval (13).

## Suggested next attack

Combine (9) with the exact stage-multiplier growth to obtain a global ordinary
height bound for every cap-correction chain. This is `T-9704`.
