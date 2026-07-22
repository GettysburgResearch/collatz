# L-9702 — Canonical caps remain below the composite odd multiplier

**Claim ID:** `L-9702`  
**Title:** Finite chains of canonical odd-affine tiles have one canonical cap in the full odd-radix interval  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** elementary odd-affine arithmetic; compatible with `L-9701`  
**Scope:** every finite chain of nonnegative canonical Montgomery tiles  
**Related counterexample candidates:** none

## Statement

For `0 <= j < s`, let

\[
\mathcal M_j(x)=\frac{N_jx+C_j}{q_j},
\]

where each `N_j` is a positive odd integer and each `q_j` is a positive power
of two. Suppose the local tile has canonical nonnegative digits

\[
0\le \rho_j<q_j,
\qquad
0\le \psi_j<N_j,
\]

satisfying

\[
C_j+N_j\rho_j=q_j\psi_j.
\tag{1}
\]

Equivalently, for every `y >= 0`,

\[
\boxed{
\rho_j+q_jy\longmapsto \psi_j+N_jy.}
\tag{2}
\]

Put

\[
P=\prod_{j=0}^{s-1}N_j,
\qquad
Q=\prod_{j=0}^{s-1}q_j.
\tag{3}
\]

Then the complete chronological chain has one canonical input correction `R`
and one canonical output cap `S` such that

\[
\boxed{0\le R<Q,\qquad 0\le S<P,}
\tag{4}
\]

and, for every ordinary integer `y >= 0`,

\[
\boxed{
R+Qy\longmapsto S+Py.}
\tag{5}
\]

Moreover the cylinder `R mod Q` is exactly the set of nonnegative inputs for
which every intermediate quotient in the chain is integral. Thus the upper
bound `S<P` does not hide or relax any local divisibility condition.

## Definitions

The word **canonical** means that the binary correction is the least
nonnegative representative modulo its binary radix and the output cap lies in
the least nonnegative odd-radix interval. No infinite digit string is involved.

## Motivation

PR #3 compresses 256 local residual transitions into one stage tile. Its
stage-to-stage height argument needs the apparently innocuous but load-bearing
fact that the stage cap is strictly below the complete odd multiplier. This
lemma proves that bound once for every finite chain of canonical local tiles.

## Proof

The unique composite correction `R mod Q` follows from oddness of every `N_j`
and the usual composition recurrence; this is also the algebra of `L-9701`.
We prove simultaneously that its complete output has the form (5) and that the
least output cap satisfies (4).

Proceed by induction on the chain length `s`.

### Base case

For `s=1`, take

\[
R=\rho_0,
\qquad
S=\psi_0.
\]

Equations (4)--(5) are exactly the hypotheses (1)--(2).

### Induction step

Write the chain as the first tile followed by a suffix of length `s-1`. By the
induction hypothesis, the suffix has canonical data

\[
R',\ Q',\ S',\ P'
\]

with

\[
0\le R'<Q',
\qquad
0\le S'<P',
\]

and acts by

\[
R'+Q'v\longmapsto S'+P'v
\qquad(v\ge0).
\tag{6}
\]

The full composite modulus is `Q=q_0Q'`. Let `R` be its least nonnegative
correction. Since `R` must satisfy the first local cylinder, write

\[
R=\rho_0+q_0u.
\tag{7}
\]

Because `0 <= R < q_0Q'` and `0 <= rho_0 < q_0`, the integer `u` satisfies

\[
0\le u<Q'.
\tag{8}
\]

After the first tile, the state is

\[
x_1=\psi_0+N_0u.
\tag{9}
\]

The full correction was chosen to satisfy the suffix, so

\[
x_1=R'+Q'v
\tag{10}
\]

for one integer `v`. Equation (9), nonnegativity, and `R'<Q'` force `v>=0`.
Also, from (8) and `psi_0<N_0`,

\[
0\le x_1
< N_0+N_0(Q'-1)
=N_0Q'.
\]

Together with (10), this gives

\[
0\le v<N_0.
\tag{11}
\]

The suffix output from the least full correction is therefore

\[
S=S'+P'v.
\]

Using `0 <= S' < P'` and (11),

\[
0\le S<P'+P'(N_0-1)=N_0P'=P.
\]

This proves the cap bound.

Finally, adding the full modulus `Qy=q_0Q'y` to the input in (7) adds `Q'y` to
the first quotient `u`, hence adds `N_0y` to the suffix quotient `v`. Equation
(6) then adds `P'N_0y=Py` to the complete output. This proves (5).

The same induction shows the exact domain equivalence: the composite
congruence first forces the first local quotient to be integral, then the
remaining quotient lies in the suffix cylinder, and conversely every sequence
of local integral divisions composes to the full congruence. ∎

## Dependency audit

- Oddness of `N_j` gives uniqueness of every dyadic correction.
- The bounds on `rho_j` and `psi_j` are used at (8) and (11).
- No asymptotic estimate, compactness argument, or external theorem is used.
- `L-9701` contains compatible cumulative-cylinder algebra but is not needed as
  a black box for the cap inequality.

## Gap audit

- The hypothesis `0 <= psi_j < N_j` is essential. A merely integral local
  quotient with an arbitrary signed cap need not satisfy `0 <= S < P`.
- The lemma is finite. It proves no infinite path and no ordinary initialization.
- A small cap is a height bound, not membership in a later dyadic cylinder.

## Adversarial tests

`X-9702` exhaustively composes 160,434 small canonical chains using the formula
above. Its independent checker uses a different parameter set and directly
enumerates every residue modulo the composite radix for 178,808 chains. Both
confirm uniqueness, all intermediate divisions, and `0 <= S < P`.

## Remaining uncertainty

The argument is elementary and complete-looking. Independent review should pay
special attention to the nonnegativity of the suffix quotient `v` and to the
claim that one composite congruence implies every intermediate divisibility
condition.

## Suggested next attack

Apply the cap bound to a scale-dependent family in which the next binary radix
grows faster than the current odd multiplier. This is done for PR #3's
corrected 256-transition stage in `T-9703`.
