# T-0038 — Every eventual corrected-stage room is transcendental

Claim ID: `T-0038`  
Title: The exact real, binary, and ternary approximation product excludes every algebraic fixed room  
Status: `PROPOSED / SOURCE-QUALIFIED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `O-0011`, `T-0033`; source normalization independently audited in PR #34 `T-9811`  
External source: D. Ridout, *The p-adic generalization of the Thue--Siegel--Roth theorem*, Mathematika 5 (1958), 40--48  
Scope: every real room attached to an assumed infinite positive ordinary corrected-stage path  
Related counterexample candidates: none

## Source theorem used

Normalize finite-place absolute values by

\[
|p|_p=p^{-1}
\]

and use projective height

\[
H(y/x)=\max\{|x|,|y|\}
\]

for a reduced rational `y/x`.

The source-qualified form of Ridout used here states: for a finite set of
places `S` containing the real place, algebraic projective targets `zeta_v`,
and every `epsilon>0`, only finitely many rational numbers `xi` satisfy

\[
\prod_{v\in S}
\min\{1,|\zeta_v-\xi|_v\}
< H(\xi)^{-2-\epsilon}.
\tag{1}
\]

For the projective target infinity, use

\[
|\infty-\xi|_v=|\xi|_v^{-1}.
\]

PR #34 `T-9811` independently audited this precise normalization against
Ridout's theorem and Bilu's Bourbaki exposition, including the independent
targets and the projective infinity convention.

## Statement

If an infinite positive ordinary corrected-stage path exists and `C_infinity`
is its fixed room from `T-0033`, then

\[
\boxed{C_\infty\text{ is transcendental}.}
\tag{2}
\]

In particular, neither a rational room nor an algebraic irrational room can
support such a path.

## Proof

For every sufficiently late scale, `O-0011` gives a reduced positive rational

\[
\xi_m={P_m\over Q_m},
\qquad
\gcd(P_m,Q_m)=1,
\tag{3}
\]

where

\[
P_m=2^{e_m}{W_m\over3^{g_m}},
\qquad
Q_m=3^{a_m-g_m},
\qquad
1\le g_m\le3.
\tag{4}
\]

It proves

\[
\boxed{
|C_\infty-\xi_m|
|P_m|_2
|Q_m|_3
<
\mathcal H_m^{-2-1/1024},}
\qquad
\mathcal H_m=\max\{|P_m|,Q_m\}.
\tag{5}
\]

Assume for contradiction that `C_infinity` is algebraic.  Apply (1) with

\[
S=\{\infty,2,3\},
\qquad
(\zeta_\infty,\zeta_2,\zeta_3)
=(C_\infty,0,\infty),
\qquad
\epsilon={1\over1024}.
\tag{6}
\]

Since `xi_m -> C_infinity`, the real error is eventually below one.  The
reduced denominator is a power of three and `3` does not divide `P_m`; also the
denominator is odd.  Therefore

\[
\min\{1,|C_\infty-\xi_m|\}
=|C_\infty-\xi_m|,
\]

\[
\min\{1,|0-\xi_m|_2\}
=|\xi_m|_2=|P_m|_2,
\]

and

\[
\min\{1,|\infty-\xi_m|_3\}
=|\xi_m|_3^{-1}=|Q_m|_3.
\]

Thus the left side of Ridout's inequality is exactly the left side of (5), and
its projective height is exactly `mathcal H_m`.

The rationals are pairwise distinct.  Indeed,

\[
a_{m+1}-a_m={5369\over2}2^m+1792,
\]

while `g_m` belongs to `{1,2,3}`, so the reduced denominator exponents
`a_m-g_m` strictly increase.  The strict positive defect in `T-0033` also
ensures `xi_m != C_infinity`.

Equation (5) therefore supplies infinitely many distinct rational solutions of
(1), contradicting Ridout's theorem.  Hence `C_infinity` is not algebraic,
which proves (2). ∎

## Combined classification

Together with `T-0037`, the corrected architecture has at most 64 eventual
rooms, and every one of them—if any exists—is transcendental and determines one
unique eventual ordinary trajectory.

Together with `T-0032`, each such trajectory must also introduce infinitely
many fresh ordinary prime factors in its scaled boundaries.

Thus every surviving path belongs to the narrow class

```text
one of at most 64 rooms
+ transcendental real room
+ infinitely many fresh endpoint primes
+ exact moving Hensel filter
+ exact cap-to-correction stitching.
```

## Gap audit

- Transcendence is a classification, not a contradiction.
- The theorem is conditional on the proposed native room and approximation
  interfaces.
- Ridout is ineffective here; no largest exceptional scale is obtained.
- No room, finite marked initialization, or counterexample is constructed.