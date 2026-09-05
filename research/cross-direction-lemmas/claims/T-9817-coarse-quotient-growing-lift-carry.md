# T-9817 -- Coarse cap quotients require an exponentially growing inverse-lift carry

Claim ID: `T-9817`
Title: The natural scale-doubling law is an exact 2-adic isometry, but its projection to the six-bit cap quotient loses `2849*2^(m-8)-1` new bits per scale
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave17-cap-carry`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9806` and `T-9813`; frozen corrected phase-34 schedule and core table at `PR3` head `c37e96efd0dcc9dd610d59041234dc57e74090fd`; elementary LTE and Newton lifting for odd 2-adic units
Scope: the inverse-power lane controlling `delta_(m,c)` and `A_m(a,b,c)` for every stabilized scale `m>=12`
Related counterexample candidates: none

## Setup

Put

\[
 d_m=2^{m-8},
 \qquad
 (t_0,t_1,t_2,t_3)=(256,257,258,259)d_m.
\tag{1}
\]

The odd unit inverted in `T-9806/(7)` and the width of its dyadic modulus are

\[
 \mathcal U_m=N_0N_1N_2=3^{E_m},
 \qquad
 E_m=5397d_m+21,
\tag{2}
\]

\[
 64T_3=2^{L_m},
 \qquad
 L_m=2849d_m+17.
\tag{3}
\]

Write

\[
 u_m=\left[\mathcal U_m^{-1}\right]_{2^{L_m}}.
\tag{4}
\]

For the corrected core vector

\[
 (b_0,b_1,b_2,b_3)=(9,54,36,24),
\tag{5}
\]

the third-symbol offsets are

\[
 \delta_{m,c}
 =\left[-(b_c-b_0)u_m\right]_{2^{L_m}}.
\tag{6}
\]

For every fixed first-symbol pair `(a,b)`, the coarse quotient of `T-9813`
is defined by

\[
 \boxed{
 [J_m(a,b)+\delta_{m,c}]_{2^{L_m}}
 =2^{L_m-6}A_m(a,b,c)+\ell_m(a,b,c),
 }
\tag{7}
\]

with

\[
 0\le A_m(a,b,c)<64,
 \qquad
 0\le\ell_m(a,b,c)<2^{L_m-6}.
\tag{8}
\]

The room-survivor test in `T-9813` is

\[
 A_m(a,b,c)\in\{0,61,11,63\}.
\tag{9}
\]

## Theorem 1 -- exact normalized squaring law

The exponent and precision widths obey

\[
 \boxed{
 E_{m+1}=2E_m-21,
 \qquad
 L_{m+1}=2L_m-17.
 }
\tag{10}
\]

Let

\[
 \mathbf u_m=3^{-E_m}\in\mathbf Z_2^\times
\tag{11}
\]

be the full 2-adic inverse whose reduction is (4), and normalize away the
fixed exponent by

\[
 \mathbf g_m=3^{21}\mathbf u_m=3^{-5397d_m}.
\tag{12}
\]

Then

\[
 \boxed{\mathbf g_{m+1}=\mathbf g_m^2.}
\tag{13}
\]

Moreover,

\[
 \boxed{
 \nu_2(\mathbf g_m-1)=m-6.
 }
\tag{14}
\]

Consequently there is a unique odd 2-adic integer `q_m` such that

\[
 \boxed{
 \mathbf g_m=1+2^{m-6}q_m,
 \qquad
 q_m\in\mathbf Z_2^\times.
 }
\tag{15}
\]

It satisfies the exact nonautonomous polynomial recurrence

\[
 \boxed{
 q_{m+1}=q_m+2^{m-7}q_m^2.
 }
\tag{16}
\]

The update map

\[
 f_m(x)=x+2^{m-7}x^2
\tag{17}
\]

is a 2-adic isometry:

\[
 \boxed{
 \nu_2(f_m(x)-f_m(y))=\nu_2(x-y)
 \qquad(x\ne y).
 }
\tag{18}
\]

Finally, the sequence `q_m` has a 2-adic limit `q_infinity`, but it gains only
one stable low bit per scale:

\[
 \boxed{
 \nu_2(q_\infty-q_m)=m-7.
 }
\tag{19}
\]

### Proof

The four heights in (1) give

\[
 \begin{aligned}
 E_m
 &=7(t_0+t_1+t_2+3)
 =7(771d_m+3),\\
 L_m
 &=6+11(t_3+1)
 =6+11(259d_m+1),
 \end{aligned}
\tag{20}
\]

which proves (2)--(3).  Since `d_(m+1)=2d_m`, equation (10) follows.
Equations (11)--(13) are then direct.

For the odd integer 5397, LTE gives

\[
 \begin{aligned}
 \nu_2(3^{5397d_m}-1)
 &=\nu_2(3-1)+\nu_2(3+1)+\nu_2(5397d_m)-1\\
 &=1+2+(m-8)-1=m-6.
 \end{aligned}
\tag{21}
\]

Taking the inverse of an odd unit does not change the valuation of its
difference from one, so (14)--(15) follow.  Squaring (15) and comparing it
with the same formula at scale `m+1` gives

\[
 1+2^{m-5}q_{m+1}
 =1+2^{m-5}q_m+2^{2m-12}q_m^2,
\tag{22}
\]

which is (16).

For arbitrary `x,y in Z_2`,

\[
 f_m(x)-f_m(y)
 =(x-y)\left[1+2^{m-7}(x+y)\right].
\tag{23}
\]

The bracket is odd, proving (18).  Since `q_m` is odd, (16) also gives

\[
 \nu_2(q_{m+1}-q_m)=m-7.
\tag{24}
\]

The successive valuations strictly increase, so the sequence is Cauchy.
In its tail beginning at `m`, the first difference in (24) has valuation
`m-7` and every later difference has larger valuation; it cannot cancel.
This proves (19). **QED**

## Theorem 2 -- exact Newton carry and its width

Define the canonical inverse defect

\[
 \varepsilon_m
 ={\mathcal U_m u_m-1\over2^{L_m}}\in\mathbf Z_{\ge0}
\tag{25}
\]

and the retained carry

\[
 \boxed{
 c_m=[\varepsilon_m]_{2^{\Delta_m}},
 \qquad
 \Delta_m=L_m-18=2849d_m-1.
 }
\tag{26}
\]

Then the next canonical inverse is given exactly by

\[
 \boxed{
 u_{m+1}
 =\left[
 3^{21}u_m^2
 \left(1-2^{L_m+1}c_m\right)
 \right]_{2^{L_{m+1}}}.
 }
\tag{27}
\]

Thus the natural inverse update is exact, and its quotient carry has precisely
`Delta_m=2849*2^(m-8)-1` bits.  For the distinguished source unit
`mathcal U_m`, this carry is of course computable from the displayed quotient
in (25).  The point is that it is not part of `u_m` viewed merely as an
abstract inverse residue; a bounded projected-state rule must either retain
this growing quotient block or exploit the special source formula anew.

### Proof

Put

\[
 v_m=u_m(2-\mathcal U_m u_m)
 =u_m(1-2^{L_m}\varepsilon_m).
\tag{28}
\]

Newton's identity gives

\[
 \mathcal U_m v_m
 =1-2^{2L_m}\varepsilon_m^2.
\tag{29}
\]

Because `L_(m+1)=2L_m-17<2L_m`, the integer `v_m` is an inverse of
`mathcal U_m` modulo `2^(L_(m+1))`.  Also

\[
 \mathcal U_{m+1}={\mathcal U_m^2\over3^{21}},
\tag{30}
\]

so `3^21*v_m^2` is its inverse at the required precision.  Squaring (28)
and reducing modulo `2^(L_(m+1))` gives

\[
 v_m^2
 \equiv
 u_m^2(1-2^{L_m+1}\varepsilon_m)
 \pmod {2^{L_{m+1}}},
\tag{31}
\]

because the omitted term is divisible by `2^(2L_m)`.  The coefficient of
`epsilon_m` begins at bit `L_m+1`; therefore only

\[
 L_{m+1}-(L_m+1)=L_m-18=\Delta_m
\tag{32}
\]

bits of that defect survive.  Replacing `epsilon_m` by `c_m` in (31) proves
(27). **QED**

## Theorem 3 -- why the six-bit quotient is not a closed state

The current inverse residue `u_m modulo 2^(L_m)` is equivalent to exactly

\[
 \boxed{
 K_m=L_m-(m-6)=2849d_m+23-m
 }
\tag{33}
\]

bits of `q_m`.  Explicitly,

\[
 \boxed{
 [q_m]_{2^{K_m}}
 ={[3^{21}u_m]_{2^{L_m}}-1\over2^{m-6}}.
 }
\tag{34}
\]

The next inverse requires `K_(m+1)` bits, and

\[
 \boxed{
 K_{m+1}-K_m
 =2849d_m-1
 =\Delta_m.
 }
\tag{35}
\]

Fix one residue `q_* modulo 2^(K_m)`.  Its possible lifts to the next required
precision are

\[
 q_*+2^{K_m}h
 \pmod {2^{K_{m+1}}},
 \qquad
 0\le h<2^{\Delta_m}.
\tag{36}
\]

Under the exact update `f_m`, these `2^(Delta_m)` lifts remain pairwise
distinct and fill one complete residue class modulo `2^(K_m)`.  Equivalently,
the compatible next inverse residues fill the complete coset

\[
 \boxed{
 \mathcal C_{m+1}(u_*')
 =\left\{
 [u_*'+2^{L_m+1}h]_{2^{L_{m+1}}}:
 0\le h<2^{\Delta_m}
 \right\}.
 }
\tag{37}
\]

For every `c in {1,2,3}`, the multiplier `b_c-b_0` in (6) is odd.  Therefore
the same statement holds for the compatible next offsets
`delta_(m+1,c)`: they fill a full coset modulo `2^(L_m+1)`.

Even if the next base cell `J_(m+1)(a,b)` is supplied for free and held fixed,
the six-bit quotient

\[
 \left\lfloor
 {[J_{m+1}(a,b)+\delta_{m+1,c}]_{2^{L_{m+1}}}
  \over2^{L_{m+1}-6}}
 \right\rfloor
\tag{38}
\]

takes every value in `{0,1,...,63}` across that lift fiber, each exactly

\[
 \boxed{2^{\Delta_m-6}}
\tag{39}
\]

times.  In particular, there is no universal next-scale transition on the
abstract projected state `A_m`, or even on an inverse residue of an otherwise
unspecified full odd unit, that is compatible with every lift in (36).  The
distinguished base-3 source does have the exact transition (27); evaluating it
requires its growing quotient carry (26) or equivalent source information.

### Proof

Multiplication by the fixed odd unit `3^21`, subtraction of one, and division
by `2^(m-6)` give the bijection (34), proving (33).  Direct substitution of
(10) into the definition of `K_(m+1)` gives (35).

By the isometry (18), distinct lifts in (36) have distinct images modulo
`2^(K_(m+1))`; every image is congruent to `f_m(q_*)` modulo `2^(K_m)`.
The source and target cosets have the same finite cardinality, so the image is
the complete target coset.

At the next scale,

\[
 \mathbf u_{m+1}
 =3^{-21}\left(1+2^{m-5}q_{m+1}\right).
\tag{40}
\]

Thus a change by a multiple of `2^(K_m)` in `q_(m+1)` becomes a change by a
multiple of

\[
 2^{m-5+K_m}=2^{L_m+1}
\tag{41}
\]

in the next inverse.  This proves (37).  Multiplication by any of
`45,27,15` is a permutation of that coset, and addition of fixed `J_(m+1)`
again gives a complete coset modulo `2^(L_m+1)`.

Finally,

\[
 L_{m+1}-(L_m+1)=\Delta_m\ge6
 \qquad(m\ge12).
\tag{42}
\]

Every one of the 64 intervals selected by the top six bits contains exactly
`2^(Delta_m-6)` elements of a fixed coset modulo `2^(L_m+1)`.  This proves
(38)--(39). **QED**

## What this advances

- It replaces the heuristic that the inverse "roughly squares" by the exact
  normalized recurrence (16) and the exact Newton transition (27).
- It quantifies the obstruction to a 64-state cap recurrence: scale doubling
  requires a quotient block of `2849*2^(m-8)-1` bits beyond the abstract
  truncated-inverse state.  For the actual source this block is the computable
  defect (25), but its width is unbounded.
- It proves that the natural projected lift fiber has all 64 possible next
  coarse blocks on every nonzero third-symbol lane.  A successful bounded
  recurrence must therefore transport or recompute the distinguished carry
  `c_m`, or prove a special correlation with the independently defined base
  cell `J_(m+1)(a,b)`.
- The convergent normalization `q_m -> q_infinity` identifies a fixed 2-adic
  object behind the scale sequence, while (19) shows that its directly stable
  prefix grows only linearly in `m`, far below the exponential moving window
  sampled by `A_m`.

## Dependency, novelty, and source-head audit

- `T-9806` supplies the inverse (4), the offset formula (6), and the exact
  modulus `64T_3`; its audited blob is
  `c2c03ff398fdf80dc0ac13a4d995eab8680e829a`.
- `T-9813` supplies the coarse quotient (7) and the survivor set (9); its
  audited blob is `5230750e23bec39a744ca9561465a32dd474d544`.
- The coefficients 5397 and 2849 are exact sums from the frozen corrected
  PR #3 heights and are derived again in (20).  The live PR #3 head was
  refreshed as `c37e96efd0dcc9dd610d59041234dc57e74090fd`.
- The live PR #33 head was refreshed as
  `2cfe2506e2a5e86157c8ac970bd9466ce86a6891`, but no PR #33 height or cap
  theorem is used here.
- Equations (16), (19), (27), and the exact lift-fiber count (39) are new.
  They use only elementary arithmetic of odd units in `Z_2`; no external
  equidistribution, transcendence, or automatic-sequence theorem is invoked.

## Gap and scope audit

- This theorem explains why the direct 64-state route collapses; it does not
  prove that the actual distinguished lift hits or avoids
  `{0,61,11,63}` cofinally.
- The actual `q_m` is fixed by `3^(-5397d_m)`, so it selects one element of
  the lift fiber in (36).  The all-64 ambiguity is an information-loss theorem
  for the truncated state, not a claim that the one source sequence branches.
- Given the scale and the exact source integer `mathcal U_m`, formula (25)
  computes `c_m` from `u_m`; the theorem does not deny this source-specific
  transition.  It proves that the quotient block grows exponentially and is
  invisible to a bounded projection such as `A_m`.
- The base cell `J_m(a,b)` has its own connector carries.  A cancellation or
  correlation between those carries and `c_m` is not excluded.  Proving such
  a correlation is now necessary for a smaller state closure.
- Formula (19) is 2-adic convergence, not a real estimate and not a source of
  high moving digits at precision `L_m`.
- The lane `c=0` has `delta_(m,0)=0`; the inverse ambiguity does not control
  its quotient, which is entirely the base-cell problem.
- No bounded computation is extrapolated, and no room, cap chain, marked
  initialization, or Collatz conclusion is proved or refuted.

## Adversarial and bounded exact checks

- At `m=12`,

  \[
  (E_{12},L_{12},K_{12})=(86373,45601,45595),
  \tag{43}
  \]

  while

  \[
  (E_{13},L_{13},K_{13})=(172725,91185,91178),
  \qquad
  \Delta_{12}=45583.
  \tag{44}
  \]

  Exact integer replay verified (16), (27), and (34) at these full widths.
- A separate exact replay of the actual 64 prefix quotients found, for
  example,

  \[
  A_{12}(0,0,1)=A_{12}(2,1,0)=19,
  \tag{45}
  \]

  but

  \[
  A_{13}(0,0,1)=36,
  \qquad
  A_{13}(2,1,0)=27.
  \tag{46}
  \]

  Thus even the most naive label-free rule `A_(m+1)=F(A_m)` already fails at
  one exact transition.  This bounded counterexample is only an audit; the
  theorem-level obstruction is the lift-fiber proof above.
- The fixed factor in (27) is `3^21`, not `3^(-21)`: the next odd unit is
  `mathcal U_m^2/3^21`, so its inverse acquires `3^21`.
- The precision deficit is `L_m-18`, not `L_m-17`.  One bit is saved because
  squaring the Newton lift shifts the defect term by `L_m+1`.
- Holding `J_(m+1)` fixed in Theorem 3 strengthens the insufficiency test.  It
  does not assert that arbitrary inverse lifts occur in the actual connector
  system.

## Suggested next attack

Derive the connector analogue of (27) for `J_m(a,b)` and compare its retained
Newton defect with `c_m`.  A useful theorem must show that their top-six
carries cancel, correlate, or jointly close in a state whose width is bounded
independently of `m`.  Without such a relation, (37)--(39) prove that the
inverse lane alone cannot improve the room-survivor bound.
