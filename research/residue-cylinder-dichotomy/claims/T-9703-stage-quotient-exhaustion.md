# T-9703 — The corrected 256-stage ordinary quotient is eventually exhausted

**Claim ID:** `T-9703`  
**Title:** Next-scale completion height forces every ordinary 256-stage trajectory onto the cap-correction tail  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `L-9702`; frozen PR #3 interface `T-0027`  
**Scope:** every infinite directive of corrected phase-`-34` 256-transition stage words  
**Related counterexample candidates:** none

## Statement

Freeze the exact stage interface of PR #3 `T-0027`. At every scale `m >= 8`,
an arbitrary admissible tower-type word `w_m` determines one complete stage map

\[
z_{m+1}
=
\frac{3^{A_m}z_m+C_m(w_m)}{2^{D_m}},
\tag{1}
\]

where

\[
A_m=\frac{5369}{2}2^m+1792,
\qquad
D_m=\frac{1085579}{256}2^m+2816.
\tag{2}
\]

Write

\[
N_m=3^{A_m},
\qquad
q_m=2^{D_m}.
\tag{3}
\]

Let `R_m=R_m(w_m)` and `S_m=S_m(w_m)` be the canonical stage correction and
cap. Thus every nonnegative integral stage input has the unique form

\[
z_m=R_m+q_mY_m,
\qquad Y_m\in\mathbb Z_{\ge0},
\tag{4}
\]

and its exact output is

\[
z_{m+1}=S_m+N_mY_m.
\tag{5}
\]

Then the following statements hold uniformly over **every** infinite sequence
of admissible stage words.

### 1. Canonical cap bound

\[
\boxed{0\le R_m<q_m,
\qquad
0\le S_m<N_m.}
\tag{6}
\]

### 2. Exact next-scale precision drain

Put

\[
\varepsilon_m=\frac{N_m}{q_{m+1}}.
\tag{7}
\]

Then

\[
\boxed{
\log_2\varepsilon_m
<
-\frac{22173699}{5248}2^m
+\frac{1024}{41}
<-2.}
\tag{8}
\]

In particular,

\[
\boxed{\varepsilon_m<\frac14}
\tag{9}
\]

for every `m >= 8`.

### 3. Eventual quotient exhaustion

Let `(z_m)_(m>=m_0)` be any ordinary nonnegative trajectory satisfying every
chosen stage exactly. Then there is a finite scale `M >= m_0` such that, for
every `m >= M`,

\[
\boxed{z_m=R_m,
\qquad
Y_m=0,
\qquad
S_m=R_{m+1}.}
\tag{10}
\]

Thus the apparently unbounded ordinary quotient channel of the composed stage
cannot remain active forever. Every ordinary infinite trajectory eventually
runs on the unique zero-quotient cap-correction tail.

### 4. Tiny-target consequence

Every such late correction satisfies

\[
\boxed{
0\le R_{m+1}=S_m<N_m<\frac{q_{m+1}}4.}
\tag{11}
\]

More precisely, whenever `R_(m+1)>0`,

\[
\boxed{
\log_2\frac{R_{m+1}}{q_{m+1}}
<
-\frac{22173699}{5248}2^m
+\frac{1024}{41}.}
\tag{12}
\]

### 5. Exact tail equivalence

For a fixed directive and a fixed scale `M`, the sequence

\[
z_m=R_m
\qquad(m\ge M)
\tag{13}
\]

is an exact nonnegative residual trajectory if and only if

\[
\boxed{S_m=R_{m+1}
\quad\text{for every }m\ge M.}
\tag{14}
\]

Consequently the residue-cylinder dichotomy for the genuinely supercritical
stage class has been reduced from an arbitrary self-feeding quotient to one
sharp question: exclude every infinite cap-correction chain, or construct one
with a finite symbolic rule and then complete the separate marked-initialization
and growth proof.

## Definitions

- `R_m` is the least nonnegative representative of the complete stage domain.
- `S_m` is the output of `R_m` under the complete stage.
- `Y_m` is the ordinary free quotient in (4), not a 2-adic digit or an entropy
  count.
- A **cap-correction chain** is a directive satisfying (14).

## Motivation

PR #3 correctly observes that the within-stage multiplier `N_m/q_m` is
supercritical. That prevents the fixed finite-trap argument of `T-9702`.
However, an infinite trajectory must land not merely somewhere after the
current stage but inside the **next stage's complete cylinder**. The next radix
`q_(m+1)` almost squares `q_m`; it is much larger than the current odd
multiplier `N_m`. Paying this full next-scale completion height restores a
strong contraction in the normalized variable `z_m/q_m`.

This is the scale-level analogue of the two-connector correction that replaced
the invalid 128-step budget in PR #3: every future cylinder consumed by the
claimed regenerated state must be paid.

## Proof

### Step 1: cap bounds

For one local residual transition, PR #3 has

\[
C_j=\theta_j-\eta_{j+1},
\qquad
N_j=3^{G_j},
\qquad
q_j=2^{K_{j+2}},
\]

with

\[
0\le\theta_j<N_j,
\qquad
0\le\eta_{j+1}<q_j.
\]

Let `rho_j` be its least dyadic correction and put

\[
\psi_j=\frac{C_j+N_j\rho_j}{q_j}.
\]

Because `-q_j<C_j<N_j`, `0<=rho_j<q_j`, and the numerator is divisible by
`q_j`,

\[
-q_j<C_j+N_j\rho_j<N_jq_j.
\]

Hence the integral quotient satisfies

\[
0\le\psi_j<N_j.
\]

Every local transition is therefore a canonical nonnegative tile in the exact
sense of `L-9702`. Applying that lemma to the 256 chronological transitions
gives (6), including the strict stage-cap bound `S_m<N_m`.

### Step 2: compare the current multiplier with the next radix

The elementary exact inequality

\[
3^{41}=36472996377170786403
<36893488147419103232=2^{65}
\]

gives

\[
\log_2 3<\frac{65}{41}.
\tag{15}
\]

Using (2),

\[
\begin{aligned}
\log_2\varepsilon_m
&=A_m\log_2 3-D_{m+1}\\
&<A_m\frac{65}{41}-D_{m+1}\\
&=
-\frac{22173699}{5248}2^m
+\frac{1024}{41}.
\end{aligned}
\tag{16}
\]

The right side is already less than `-2` when `2^m >= 1`, because

\[
22173699\cdot2^m>141568.
\]

This proves (8)--(9).

### Step 3: normalized height recurrence

Define

\[
r_m=\frac{z_m}{q_m}\ge0.
\tag{17}
\]

From (4), `R_m>=0` gives

\[
0\le Y_m\le r_m.
\tag{18}
\]

From (5), (6), and (18),

\[
\begin{aligned}
r_{m+1}
&=\frac{S_m+N_mY_m}{q_{m+1}}\\
&<\frac{N_m(1+Y_m)}{q_{m+1}}\\
&\le\varepsilon_m(1+r_m).
\end{aligned}
\tag{19}
\]

If `r_m>=1`, then `1+r_m<=2r_m`; by (9),

\[
r_{m+1}<\frac12r_m.
\tag{20}
\]

A finite real number cannot be halved indefinitely while remaining at least
one. Hence there is a finite `M` with

\[
r_M<1.
\tag{21}
\]

If `r_m<1`, equation (19) gives

\[
r_{m+1}<2\varepsilon_m<\frac12,
\tag{22}
\]

so the condition persists forever.

### Step 4: a subradix ordinary member is the canonical correction

For every `m>=M`, equation (21)--(22) says

\[
0\le z_m<q_m.
\]

But exact stage integrality also says

\[
z_m\equiv R_m\pmod{q_m},
\qquad
0\le R_m<q_m.
\]

Therefore

\[
z_m=R_m,
\qquad
Y_m=0.
\tag{23}
\]

Equation (5) now gives `z_(m+1)=S_m`. Applying the same subradix argument at
the next scale gives `z_(m+1)=R_(m+1)`. Hence

\[
S_m=R_{m+1}
\]

for every `m>=M`. This proves (10).

The cap bound `S_m<N_m` and (8)--(9) give (11)--(12).

Finally, (13) and the stage identity imply

\[
R_m\longmapsto S_m.
\]

Thus (13) is a trajectory exactly when `S_m=R_(m+1)` at each step, proving the
tail equivalence (14). ∎

## Dependency audit

- PR #3 `T-0027` supplies the exact 256-stage map, exponent formulas, canonical
  correction, and stage quotient decomposition. Its native status remains
  `PROPOSED`.
- `L-9702` supplies `0 <= S_m < N_m`; no hidden positivity of a composite cap is
  assumed.
- The only analytic estimate is replaced by the displayed exact integer
  inequality `3^41<2^65`.
- No entropy theorem, random model, p-adic logarithm, Padé theorem, or finite
  experiment is a proof dependency.

## Gap audit

- This theorem is conditional on the exact PR #3 stage interface being correct;
  it does not independently reconstruct all 256 physical tower blocks.
- Eventual `Y_m=0` is not yet a negative theorem. The cap-correction equality
  might conceivably hold along a specially chosen directive.
- The theorem produces no finite initial marked Collatz integer and therefore no
  `K-####` candidate.
- A cap-correction tail beginning at a late scale is not by itself a proof that
  an earlier prescribed finite seed reaches it.
- Positive within-stage slope and eventual zero free quotient are compatible:
  the next-scale modulus grows far faster than the current stage output
  multiplier.
- The ordinary bulk `V_m` of PR #3 `T-0030` is not identified with `R_m` or
  `S_m` here.

## Adversarial tests

`X-9702` checks the exact exponent identity at 17 scales, exhaustively verifies
the canonical-cap lemma on 160,434 small composite chains, and runs 64 exact
sample zippers. A separately written checker directly enumerates the complete
residue domain for 178,808 different chains and rebuilds 25 independent zipper
paths. Finite checks validate the algebra only; the universal conclusion is the
proof above.

## Remaining uncertainty

The most important review points are:

1. the use of the next denominator `q_(m+1)`, rather than the current stage
   denominator `q_m`;
2. the strict cap bound `S_m<N_m`;
3. the implication from `z_m<q_m` and stage integrality to `Y_m=0`;
4. the distinction between a residual tail and one initialized marked Collatz
   orbit.

## Suggested next attack

Prove that every admissible sequence has infinitely many scales with

\[
S_m(w_m)\ne R_{m+1}(w_{m+1}),
\]

or construct a finite-rule sequence satisfying equality forever. The exact
remaining interface is recorded as `Q-9702`.
