# T-9811 -- Every fixed corrected-stage room is transcendental

Claim ID: `T-9811`
Title: Ridout's exact three-place theorem excludes every algebraic fixed room
Status: `PROPOSED / SOURCE-QUALIFIED CONDITIONAL CONSEQUENCE`
Authoring agent: `gpt56-synthesis-01-wave15-ridout-audit`
Reviewing agents: `gpt56-synthesis-01-wave15-ridout-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR3/O-0011`, `L-0032`, and `T-0033` at `c37e96efd0dcc9dd610d59041234dc57e74090fd`; Ridout's theorem in the exact projective normalization stated below
Scope: each real room attached to an assumed infinite positive ordinary path in the corrected phase-`34` stage architecture
Related counterexample candidates: none

## Source-qualified Ridout theorem

Normalize the finite-place absolute values by

\[
 |p|_p=p^{-1},
 \qquad
 |x|_\infty=|x|.
\tag{1}
\]

For a reduced rational `xi=y/x`, with `gcd(x,y)=1`, use the projective
height

\[
 H(\xi)=\max\{|x|,|y|\}.
\tag{2}
\]

The form of Ridout's theorem used here is the following.  Let `S` be a finite
set of places of `Q` containing the infinite place, and choose algebraic
targets

\[
 \zeta_v\in\mathbf P^1(\overline{\mathbf Q})
 \qquad(v\in S).
\tag{3}
\]

For every `epsilon>0`, only finitely many `xi in Q` satisfy

\[
 \boxed{
 \prod_{v\in S}
 \min\{1,|\zeta_v-\xi|_v\}
 <H(\xi)^{-2-\epsilon}.
 }
\tag{4}
\]

For an infinite target, the standard projective convention is

\[
 |\infty-\xi|_v=|\xi|_v^{-1}.
\tag{5}
\]

The primary source is D. Ridout,
[*The p-adic generalization of the Thue--Siegel--Roth theorem*, Mathematika
5 (1958), 40--48](https://doi.org/10.1112/S0025579300001339).  The exact
normalization (1)--(5), including the height, the minimum factors, independent
algebraic targets, and the infinite-target convention, is stated explicitly
in Yuri Bilu's authoritative Bourbaki exposition,
[*The many faces of the Subspace Theorem*, Ast\'erisque 317 (2008),
Section 2.1, printed page 3](https://www.numdam.org/item/AST_2008__317__1_0.pdf).

## Statement

Assume an infinite positive ordinary corrected-stage path exists in the
branch-qualified PR #3 architecture, and let `C_infinity>0` be its fixed room
from `T-0033`.  Then

\[
 \boxed{C_\infty\text{ is transcendental}.}
\tag{6}
\]

Equivalently, no such fixed room can be a real algebraic number, rational or
irrational.

## Exact application to the branch approximants

For every sufficiently late scale, `O-0011` supplies the reduced positive
rational

\[
 \xi_m={P_m\over Q_m},
 \qquad
 \gcd(P_m,Q_m)=1,
\tag{7}
\]

where

\[
 P_m=2^{e_m}{W_m\over3^{g_m}},
 \qquad
 Q_m=3^{a_m-g_m},
 \qquad
 1\le g_m\le3,
\tag{8}
\]

and proves

\[
 \boxed{
 |C_\infty-\xi_m|\,|P_m|_2\,|Q_m|_3
 <\mathcal H_m^{-2-1/1024},
 \qquad
 \mathcal H_m=\max\{|P_m|,Q_m\}.
 }
\tag{9}
\]

Suppose for contradiction that `C_infinity` is algebraic.  In
(4), choose

\[
 S=\{\infty,2,3\},
 \qquad
 (\zeta_\infty,\zeta_2,\zeta_3)
 =(C_\infty,0,\infty),
 \qquad
 \epsilon={1\over1024}.
\tag{10}
\]

All three targets are algebraic points of the projective line.  Since
`xi_m` converges to `C_infinity`, its real error is eventually below one.
Also `Q_m` is a power of three, while reduction in (7)--(8) gives
`3` not dividing `P_m`; hence

\[
 \min\{1,|C_\infty-\xi_m|\}
 =|C_\infty-\xi_m|,
\tag{11}
\]

\[
 \min\{1,|0-\xi_m|_2\}
 =|\xi_m|_2
 =|P_m|_2,
\tag{12}
\]

and

\[
 \begin{aligned}
 \min\{1,|\infty-\xi_m|_3\}
 &=\min\{1,|\xi_m|_3^{-1}\}\\
 &=|Q_m|_3.
 \end{aligned}
\tag{13}
\]

Thus the left side of Ridout's inequality (4) is **exactly** the left side
of (9), and the height (2) is exactly `mathcal H_m`.  Equation (9) therefore
places every sufficiently late `xi_m` in Ridout's finite exceptional set.

These rationals are nevertheless pairwise distinct and never equal the real
target.  The latter follows from the strict positive error in `T-0033`; for
distinctness, observe that

\[
 a_{m+1}-a_m
 ={5369\over2}2^m+1792,
\tag{14}
\]

while `g_m` always lies in `{1,2,3}`.  Consequently

\[
 (a_{m+1}-g_{m+1})-(a_m-g_m)
 \ge {5369\over2}2^m+1790>0,
\tag{15}
\]

so the reduced denominators `Q_m=3^(a_m-g_m)` strictly increase.  Hence
(9) gives infinitely many distinct solutions of (4), contradicting Ridout's
theorem.  Every algebraic case is impossible, proving (6). **QED**

## What this advances

- It strengthens and promotes the conditional literature corollary left open
  in `O-0011`: the branch's native two-place inequality matches an exact
  sourced Ridout theorem without changing its exponent or height convention.
  Because Ridout permits rational algebraic targets, the conclusion is
  transcendence rather than merely the rational-or-transcendental dichotomy
  anticipated there.
- It identifies the load-bearing projective targets.  The binary numerator
  factor comes from target zero at place two; the ternary denominator factor
  comes from target infinity at place three.
- It proves a classification for every assumed fixed room, not existence of a
  room or of an ordinary path.

## Dependency and source audit

- Branch-qualified `PR3/O-0011` supplies (7)--(9), including reduction,
  positivity, convergence, the local factors, and the exponent `1/1024`.
  Its native calculation is not reproved by the external theorem.
- Branch-qualified `PR3/L-0032` supplies `1<=g_m<=3`; `PR3/T-0033` supplies
  the fixed room and the floor approximants underlying `O-0011`.
- Ridout's relevant primary theorem is the 1958 p-adic Roth extension linked
  above, not merely the different restricted-factor result in his 1957 paper.
- Bilu's linked formulation fixes all conventions needed for the application:
  normalized absolute values, reduced projective height, a finite set of
  places containing infinity, independent algebraic targets, minimum factors,
  exponent `2+epsilon`, and the projective infinity convention.
- Bilu explicitly notes that Ridout's theorem remains nontrivial even when the
  targets are rational.  No irrationality hypothesis is imposed on
  `zeta_infinity=C_infinity` in (4).
- Equation (10) uses a genuinely finite set of three places.  The shorthand
  "`S={2,3}` plus the real error" in `O-0011` is equivalent bookkeeping, but
  the exact sourced theorem uses `S={infinity,2,3}`.

## Gap and scope audit

- The conclusion is conditional on the proposed PR #3 corrected-stage
  interfaces and on the existence of an infinite positive ordinary path.
- The theorem does not construct a transcendental room or an ordinary path;
  it classifies the room of any path whose existence is assumed.
- Ridout's theorem is ineffective here: it gives finiteness, not a usable
  largest exceptional scale.
- The result does not prove a cap stitch, marked initialization, nontrivial
  Collatz orbit, or counterexample.
- If the branch formulas or the reduced local factors change, the exact
  target matching (11)--(13) must be repeated.

## Adversarial checks

- Choosing target zero at place three would give
  `min(1,|xi_m|_3)=1`, not `|Q_m|_3`.  The target at place three must be the
  projective point infinity.
- The numerator and denominator factors are not interchangeable:
  `zeta_2=0` yields `|P_m|_2` because `|Q_m|_2=1`, whereas `zeta_3=infinity`
  yields `|Q_m|_3` because `|P_m|_3=1`.
- Ridout's theorem counts rational numbers, not presentations.  Strict growth
  of the reduced denominators in (15) proves the required infinite
  distinctness.
- The theorem uses `H(P_m,Q_m)=max(|P_m|,Q_m)`, not denominator height alone.
- No restriction that all prime factors of `P_m` lie in `{2,3}` is needed;
  the theorem evaluates only the selected local factors.
- The fixed constant in `O-0011/(14)` has already been absorbed before (9),
  leaving the exact positive margin `epsilon=1/1024` required in (4).
- A rational `C_infinity` is also an allowed algebraic target in Ridout's
  theorem.  The strict positive real defect ensures that no `xi_m` equals that
  target, and the increasing reduced denominators still give infinitely many
  distinct forbidden approximants.

## Suggested next attack

Seek a native arithmetic obstruction forcing the fixed room to be algebraic,
or place the exact room series in a class with an independent algebraicity
criterion.  Either result would now contradict (6) and exclude the assumed
infinite ordinary path.
