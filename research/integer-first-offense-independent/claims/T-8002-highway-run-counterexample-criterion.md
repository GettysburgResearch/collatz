# T-8002 — A forever-defined run-five highway is a full Collatz counterexample

**Claim ID:** `T-8002`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `O-8001`, `L-8002`  
**Scope:** positive ordinary paths in the negative-three-cycle pulse chart

## Statement

Let

\[
 z_j=2^{3r_j}u_j,
 \qquad r_j\ge0,
 \qquad u_j\text{ odd},
\tag{1}
\]

be successive maximal-run section states of the exact chart in `L-8002`. Thus

\[
 \boxed{
 z_{j+1}=\frac{9^{r_j+1}u_j+7}{16}.}
\tag{2}
\]

Then:

1. if `r_j=0`, one has `z_(j+1)<=z_j`, with equality only at `z_j=1`;
2. if `1<=r_j<=4`, one has `z_(j+1)<z_j`;
3. if `r_j>=5`, one has `z_(j+1)>z_j`.

Consequently, if one explicit positive ordinary section state has a forward
macro orbit defined for every `j>=0`, avoids `z=1`, and satisfies

\[
 \boxed{r_j\ge5\quad\text{for every }j,}
\tag{3}
\]

then

\[
 n_0=6z_0-5
\tag{4}
\]

is an unconditional shortcut-Collatz counterexample. Its exact physical orbit
is positive and unbounded.

Equivalently, in the quotient coordinates of `L-8002`, it is enough to find
one finite ordinary state `(r_0,r_1,k_0)` whose deterministic partial quotient
map is defined forever and whose emitted run labels all lie in
`{5,6,7,...}`. No additional drift, integrality, or physical-replay theorem is
then required.

## Proof

From (1)–(2),

\[
 \begin{aligned}
 16(z_{j+1}-z_j)
 &=9^{r_j+1}u_j+7-16\,2^{3r_j}u_j\\
 &=\bigl(9^{r_j+1}-2^{4+3r_j}\bigr)u_j+7.
 \end{aligned}
\tag{5}
\]

For `r=0`, equation (5) is

\[
 16(z^+-z)=7(1-u),
\]

which is nonpositive for positive odd `u`, and vanishes only at `u=1`, i.e.
`z=1`.

For `r=1,2,3,4`, the coefficient in (5) is negative. Its absolute value is
already

\[
 2^7-9^2=47>7
\]

at `r=1`, and multiplying the dyadic term by `8` and the ternary term by `9`
keeps the gap positive through `r=4`. Since `u>=1`, equation (5) is strictly
negative.

At `r=5`,

\[
 9^6=531441>524288=2^{19}.
\tag{6}
\]

Increasing `r` multiplies the left term by `9` and the right term by `8`, so

\[
 9^{r+1}>2^{4+3r}
 \qquad(r\ge5).
\tag{7}
\]

Equation (5) is then strictly positive.

Now assume (3). Every macro is one exact finite sequence `A^(r_j)B` of the
integer chart, and local `O-8001` translates each chart edge to an exact finite
shortcut-Collatz block under `n=6z-5`. By (7),

\[
 z_0<z_1<z_2<\cdots.
\]

Thus all physical boundary states `n_j=6z_j-5` are positive and unbounded.
The complete shortcut trajectory cannot reach `1`: reaching `1` would put the
chart at its fixed state `z=1`, contrary to strict increase. Hence `n_0` is a
Collatz counterexample. ∎

## Quantitative benchmark

For a run sequence with asymptotic average `r_bar`, the homogeneous logarithmic
macro gain is

\[
 (r_{\rm bar}+1)\log 9-(4+3r_{\rm bar})\log2.
\]

Its zero is

\[
 \boxed{
 r_*=\frac{\log(16/9)}{\log(9/8)}
 =4.884949192\ldots.}
\tag{8}
\]

The pointwise hypothesis `r_j>=5` is deliberately stronger than a positive
average; it avoids every cancellation and bounded-excursion issue.

## Gap audit

- The theorem is a complete implication, not an existence theorem. No state
  satisfying infinite definedness and (3) is currently known.
- A long sequence of runs at least five is finite evidence only.
- A modular lasso does not suffice; the same finite integer must carry the
  canonical most-significant boundary forever.
- The physical conclusion uses the exact block conjugacy of `O-8001`; it does
  not infer a Collatz orbit from an abstract rational-base completion.

## Suggested next attack

Use `L-8002` to freeze a small high-run alphabet and retain the exact quotient,
not merely its low residues. Seek either:

1. an inductive inequality/congruence class on the ordinary quotient that makes
   the deterministic map total and keeps every run at least five; or
2. an exact return to a previous full ordinary quotient state, which would give
   a finite nontrivial cycle immediately.