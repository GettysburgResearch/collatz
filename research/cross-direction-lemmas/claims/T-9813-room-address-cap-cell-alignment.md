# T-9813 -- Three-symbol room addresses are exact quotients of cap-head cells

Claim ID: `T-9813`
Title: The room decoder collapses exactly the fourth-symbol cap direction, and eventual rooms inject into a computable head-survivor set
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave16-cap-room-alignment`
Reviewing agents: `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9806`, `T-9809`, and `L-9821`; branch-qualified `PR3/L-0031` at `c37e96efd0dcc9dd610d59041234dc57e74090fd`; branch-qualified `PR33/L-9702` at `2cfe2506e2a5e86157c8ac970bd9466ce86a6891`
Scope: the common stabilized corrected phase-34 head and positive scaled-tail coordinates, at every scale `m>=12`
Related counterexample candidates: none

## Setup

Put

\[
 T_j=2^{11(t_j+1)},
 \qquad
 N_j=3^{7(t_j+1)}
 \qquad
 \left(0\le j\le256\text{ for }T_j,
 \quad0\le j\le255\text{ for }N_j\right),
\tag{1}
\]

where `t_j=2^m+j2^(m-8)`.  The three-symbol incoming modulus, the two-step
head modulus, its coarse cell width, and the second-level width are

\[
 \mathcal M_m=T_1T_2T_3=2^{U_{m,3}},
 \qquad
 Q_m^H=T_2T_3,
\tag{2}
\]

\[
 \mathcal C_m={Q_m^H\over64},
 \qquad
 \mathcal W_m={T_2\over64}.
\tag{3}
\]

Thus

\[
 \mathcal M_m=T_1Q_m^H,
 \qquad
 \mathcal C_m=T_3\mathcal W_m.
\tag{4}
\]

For the first connector of a head beginning with `(a,b)`, write

\[
 X_0(a,b)
 =\left[(T_1p_b-b_a)N_0^{-1}\right]_{64T_1},
 \qquad
 0\le X_0(a,b)<64T_1.
\tag{5}
\]

The stabilized tolls are

\[
 (b_0,b_1,b_2,b_3)=(9,54,36,24).
\tag{6}
\]

For a four-symbol head `(a,b,c,k)`, abbreviate its canonical correction by

\[
 r_{a,b,c,k}=r_m^H(a,b,c,k),
 \qquad
 0\le r_{a,b,c,k}<Q_m^H.
\tag{7}
\]

## Theorem 1 -- the room address is the exact coarse-cell remainder

Define the local three-transition toll

\[
 \tau_m(a,b,c)
 =N_1N_2b_a+T_1N_2b_b+T_1T_2b_c.
\tag{8}
\]

Then the address of `T-9809` has the equivalent local form

\[
 \boxed{
 \rho_m^{[3]}(a,b,c)
 =\left[-(N_0N_1N_2)^{-1}\tau_m(a,b,c)\right]_{\mathcal M_m}.
 }
\tag{9}
\]

The fourth symbol changes `r_(a,b,c,k)` only by multiples of
`mathcal C_m`.  Hence

\[
 \upsilon_m(a,b,c)
 =\left[r_{a,b,c,k}\right]_{\mathcal C_m}
 \qquad(0\le\upsilon_m(a,b,c)<\mathcal C_m)
\tag{10}
\]

is independent of `k`.  The two coordinate systems are related by the exact
integer identity

\[
 \boxed{
 \rho_m^{[3]}(a,b,c)
 =X_0(a,b)+64T_1\upsilon_m(a,b,c).
 }
\tag{11}
\]

There is no wrap on the right side of (11).  In particular,

\[
 \boxed{
 \upsilon_m(a,b,c)
 ={\rho_m^{[3]}(a,b,c)-X_0(a,b)\over64T_1}.
 }
\tag{12}
\]

Thus the three-symbol incoming address does not supply an independent
partition transverse to the cap-head cells.  It reads exactly the head
correction modulo its coarse width `mathcal C_m`, after the fixed connector
prefix is removed.

### Proof

Let a canonical head input `z_0=r_(a,b,c,k)` pass through its first two
residual transitions, producing the integral values `z_1,z_2`.  In the scaled
coordinate of `PR3/L-0031`, put

\[
 \begin{aligned}
 W_0&=X_0+64T_1z_0,\\
 W_1&=Y_0+64N_0z_0=X_1+64T_2z_1,\\
 W_2&=Y_1+64N_1z_1=X_2+64T_3z_2,\\
 W_3&=Y_2+64N_2z_2.
 \end{aligned}
\tag{13}
\]

Only `z_1` and `z_2` require the two residual divisions in the head
composite.  The definition of `W_3` uses the output side of the connector
from `c` to `k`; it does not assume that a third residual quotient is
integral.

The exact connector identity gives

\[
 T_1W_1=N_0W_0+b_a,
 \quad
 T_2W_2=N_1W_1+b_b,
 \quad
 T_3W_3=N_2W_2+b_c.
\tag{14}
\]

Composing the three equations yields

\[
 \mathcal M_mW_3
 =N_0N_1N_2W_0+\tau_m(a,b,c).
\tag{15}
\]

Reduction modulo `mathcal M_m` proves that `W_0` has the residue in (9).
To check that this is exactly the address as defined in `T-9809`, let

\[
 \Sigma_m=\prod_{j=3}^{255}N_j.
\tag{16}
\]

The full odd stage multiplier is
`N_0*N_1*N_2*Sigma_m`, while the first three terms of the full positive toll
are exactly `Sigma_m*tau_m(a,b,c)`.  The odd unit `Sigma_m` cancels modulo
`mathcal M_m`, proving (9) from the original room-address definition.

Equation (13) now gives, for every `k`,

\[
 \rho_m^{[3]}(a,b,c)
 =\left[X_0(a,b)+64T_1r_{a,b,c,k}\right]_{\mathcal M_m}.
\tag{17}
\]

Since `mathcal M_m=64*T_1*mathcal C_m`, reduction of the head correction modulo
`mathcal C_m` turns (17) into (11).  Finally,

\[
 0\le X_0+64T_1\upsilon_m
 \le(64T_1-1)+64T_1(\mathcal C_m-1)
 <\mathcal M_m,
\tag{18}
\]

so the representative in (11) never wraps.  Division proves (12). **QED**

## Theorem 2 -- exact projection of the sixteen cap cells

Fix `(a,b)`, and use the `T-9806` decomposition

\[
 r_{a,b,c,k}
 =\mathcal W_m
 \left[J+\delta_c+T_3\kappa_k\right]_{64T_3}+V,
\tag{19}
\]

where

\[
 0\le V<\mathcal W_m,
 \qquad
 (\kappa_0,\kappa_1,\kappa_2,\kappa_3)=(0,3,53,1),
\tag{20}
\]

\[
 \delta_c
 =\left[-u_m(b_c-b_0)\right]_{64T_3},
 \qquad
 u_m=\left[(N_0N_1N_2)^{-1}\right]_{64T_3}.
\tag{21}
\]

Define

\[
 \ell_c=[J+\delta_c]_{T_3}.
\tag{22}
\]

Then

\[
 \boxed{
 \upsilon_m(a,b,c)=\mathcal W_m\ell_c+V,
 }
\tag{23}
\]

and therefore

\[
 \boxed{
 \rho_m^{[3]}(a,b,c)
 =X_0(a,b)+64T_1V+T_1T_2\ell_c.
 }
\tag{24}
\]

The ambient cell projection is exactly

\[
 \boxed{
 \begin{array}{ccc}
 \mathbf Z/(64T_3)\mathbf Z&\longrightarrow&\mathbf Z/T_3\mathbf Z,\\
 [J+\delta_c+T_3\kappa_k]_{64T_3}
 &\longmapsto&[J+\delta_c]_{T_3}.
 \end{array}}
\tag{25}
\]

The ambient homomorphism in (25) has fibers of size 64.  Its restriction to
the sixteen cap-cell indices for fixed `(a,b)` is instead four-to-one onto
the four distinct values `ell_c`; its four restricted fibers are exactly the
final-symbol quartets

\[
 \{(c,0),(c,1),(c,2),(c,3)\}
 \qquad(c=0,1,2,3).
\tag{26}
\]

Consequently the compatible symbolic combination of the 64 three-symbol
addresses and the 16 last-two-symbol cells is the overlap fiber product

\[
 \boxed{
 4^3\mathbin{\times}_{4}4^2=4^4=256,
 }
\tag{27}
\]

not the independent product `64*16=1024`.

### Proof

Reducing (19) modulo
`mathcal C_m=T_3*mathcal W_m` kills the term
`T_3*kappa_k` and gives (23).  Equation (24) follows from (11) and
`64*T_1*mathcal W_m=T_1*T_2`.

The four values `ell_c` are distinct.  Indeed, equality for `c` and `c'`
would imply

\[
 u_m(b_c-b_{c'})\equiv0\pmod {T_3}.
\tag{28}
\]

The multiplier `u_m` is odd, hence a unit, and the four values in (6) are
distinct with pairwise differences smaller than `T_3`.  Thus `c=c'`.  On the
sixteen-point cap-cell set, the term `T_3*kappa_k` shows that every fixed `c`
has the four-element restricted fiber in (26).  The room prefix `(a,b,c)` and
cap suffix `(c,k)` share the symbol `c`, so their compatible union is one
four-symbol word.  This proves (25)--(27). **QED**

## Theorem 3 -- every eventual room enters the zero coarse cell

Let `mathscr C` be the eventual fixed-room set of `T-9809`.  For a fixed
`C in mathscr C`, every sufficiently late stage has

\[
 W_m=\lfloor C H_m\rfloor<\mathcal M_m.
\tag{29}
\]

If its decoded first four symbols are `(a,b,c,k)`, then

\[
 \boxed{
 W_m=\rho_m^{[3]}(a,b,c)
 =X_0(a,b)+64T_1r_{a,b,c,k},
 \qquad
 r_{a,b,c,k}<\mathcal C_m.
 }
\tag{30}
\]

This conclusion uses the fixed-room scale, not the wider cap-height estimate
of `L-9821`.

To make the resulting finite filter explicit, write

\[
 [J+\delta_c]_{64T_3}=T_3A_m(a,b,c)+\ell_c,
 \qquad
 0\le A_m(a,b,c)<64.
\tag{31}
\]

Then

\[
 \boxed{
 r_{a,b,c,k}
 =\mathcal C_m[A_m(a,b,c)+\kappa_k]_{64}
 +\upsilon_m(a,b,c).
 }
\tag{32}
\]

Hence a three-symbol address can support an eventual room at scale `m` only
if

\[
 \boxed{
 A_m(a,b,c)\in\{0,61,11,63\}.
 }
\tag{33}
\]

When (33) holds, it forces respectively

\[
 \boxed{
 A_m=0,61,11,63
 \quad\Longrightarrow\quad
 k=0,1,2,3.
 }
\tag{34}
\]

Define the computable prefix-survivor set and its size by

\[
 \mathfrak P_m
 =\{(a,b,c):A_m(a,b,c)\in\{0,61,11,63\}\},
 \qquad
 \mathfrak n_m=\#\mathfrak P_m.
\tag{35}
\]

Then

\[
 \boxed{
 0\le\mathfrak n_m\le64,
 \qquad
 \#\mathscr C\le\liminf_{m\to\infty}\mathfrak n_m.
 }
\tag{36}
\]

In particular, `mathfrak n_m=0` at arbitrarily large scales excludes every
eventual room.  Any all-late or cofinal improvement on `mathfrak n_m<=64`
immediately improves the global room bound by the same amount.

### Proof

For a valid head, the exact finite-chain cylinder theorem gives

\[
 z_{m,0}=r_{a,b,c,k}+Q_m^Hy_m,
 \qquad
 y_m\ge0.
\tag{37}
\]

The scaled-coordinate definition is

\[
 W_m=X_0(a,b)+64T_1z_{m,0}.
\tag{38}
\]

For a fixed room, `T-9809/(14)` makes (29) hold eventually.  If `y_m>=1`,
then (4), (37), and (38) would give

\[
 W_m\ge64T_1Q_m^H=64\mathcal M_m,
\tag{39}
\]

contrary to (29).  Thus `y_m=0`.  Substitution back into (38) gives

\[
 X_0+64T_1r_{a,b,c,k}<T_1Q_m^H,
\tag{40}
\]

and nonnegativity of `X_0` implies `r_(a,b,c,k)<Q_m^H/64=mathcal C_m`.
The incoming congruence of `T-9809` and the bounds
`0<=W_m,rho_m^[3]<mathcal M_m` then make the congruence an equality, proving
(30).

Equations (19), (22), and (31) give

\[
 [J+\delta_c+T_3\kappa_k]_{64T_3}
 =T_3[A_m(a,b,c)+\kappa_k]_{64}+\ell_c.
\tag{41}
\]

Together with (23), this is (32).  Since
`0<=upsilon_m<mathcal C_m`, inequality (30) holds exactly when the coarse
index in (32) is zero.  The four `kappa_k` are distinct, and their negatives
modulo 64 are `(0,61,11,63)`.  This proves (33)--(35), including uniqueness
of the fourth symbol and `mathfrak n_m<=64`.

It remains to prove the liminf bound.  Theorem 3 of `T-9809` first gives
`#mathscr C<=64`, so all rooms have a common sufficiently late regime.  If
there are at least two rooms, let `d>0` be their minimum pairwise separation;
for zero or one room the conclusion is immediate.  At every sufficiently
late scale, `H_m^(-1)<d`, so distinct rooms give distinct integers
`floor(C H_m)`.  By (30), these distinct integers are distinct three-symbol
addresses belonging to `mathfrak P_m`.  Therefore

\[
 \#\mathscr C\le\mathfrak n_m
\tag{42}
\]

at every sufficiently late scale.  Taking the lower limit proves (36).
**QED**

## What this advances

- It answers the address-map question exactly: the maps are aligned by the
  affine quotient (11), not transverse and not merely controlled by the safe
  product bound 1024.
- It identifies what each coordinate sees.  The room prefix retains the
  third-symbol residue `ell_c` and collapses precisely the fourth-symbol
  coarse translation `T_3*kappa_k`.
- A fixed room eventually forces the head quotient to zero and the head
  correction below `Q_m^H/64` without invoking the PR #33 completion-height
  estimate.
- It turns the cap hierarchy into the 64-test filter `mathfrak P_m`; each
  surviving room prefix forces one exact fourth symbol.
- The variable bound in (36) is potentially stronger than 64 and supplies an
  all-late target whose success would immediately prune or eliminate rooms.

## Dependency and source-head audit

- Local `T-9806` supplies (19)--(21), including the exact cell group
  `Z/(64T_3)Z`, the common remainder `V`, and the corrected offset vector
  `(0,3,53,1)`.  Its audited blob is
  `c2c03ff398fdf80dc0ac13a4d995eab8680e829a`.
- Local `T-9809` supplies the three-symbol addresses, their injectivity, the
  eventual domination `C H_m<2^(U_(m,3))`, and the finite 64-room theorem.
  Its audited blob is `b993b72c16db77ec27e71857784c84ba120d5c59`.
- `PR3/L-0031` supplies the scaled coordinate (38), the local recurrences
  (14), and the positive stage toll.  The live PR #3 head was independently
  checked as `c37e96efd0dcc9dd610d59041234dc57e74090fd`; the audited `L-0031`
  blob is `dd916b4ee19a2e685956571acb247559122745db`.
- The exact head-cylinder domain (37) is the finite canonical-composite
  theorem `PR33/L-9702`.  The physical PR #3 head consists of the first two
  canonical nonnegative residual tiles, as audited by `L-9821` through its
  `PR33/T-9703` dependency, so `L-9702`'s exact-domain clause applies locally
  without any cap-chain height hypothesis.  The audited `L-9821` blob is
  `5e0769eb0b79345dd6686d161f46da59a42a4962`.  The live PR #33 head was
  checked as `2cfe2506e2a5e86157c8ac970bd9466ce86a6891`; the audited `L-9702`
  blob is `c4a3c87defe870307d905671722194a6ba2630ed`.
- No seam enumeration, S-unit theorem, Ridout theorem, or completion-height
  estimate is used in the proof.

## Gap and scope audit

- The sequence `mathfrak n_m` is not controlled asymptotically here.  The
  higher quotient `A_m(a,b,c)` contains the same truncated inverse-power data
  left unresolved by `T-9806`.
- The uniform theorem is `mathfrak n_m<=64`; no smaller constant is claimed.
  Several or all four values of `c` for one fixed `(a,b)` are not excluded by
  the symbolic argument.
- A small value of `mathfrak n_m` at one bounded scale does not constrain a
  room whose unknown eventual onset is later.  Equation (36) requires a
  cofinal or all-late bound.
- Passing the head filter does not verify the other 254 transitions, any of
  the 84 triple seams, the terminal collar, or stage-to-stage continuation.
- All conclusions remain conditional on the proposed corrected stage and
  fixed-room interfaces.  No room, path, marked initialization, or Collatz
  counterexample is constructed or excluded.

## Adversarial and bounded exact checks

- The factor 64 in (11) is essential.  The scaled tail is
  `X_0+64T_1z_0`, not `X_0+T_1z_0`.
- The room modulus is `T_1T_2T_3`, while the head modulus is `T_2T_3`.
  This one-radix shift is exactly what turns reduction modulo
  `mathcal C_m=(T_2T_3)/64` into the room address.
- The three-symbol toll ends with `b_c`; it does not contain `b_k`.  The cap
  correction still depends on `k`, but only through a multiple of
  `mathcal C_m`, which (11) kills.
- The compatible-state count shares `c`.  Treating `(a,b,c)` and `(c,k)` as
  independent is the precise source of the spurious factor four in 1024.
- Exact integer replay recovered (11) for all 256 heads at `m=12`.  The
  filter (35) had five heads there,
  `0311, 1330, 2013, 2111, 2303`, and three at `m=13`,
  `0203, 2202, 2300`.  These bounded counts audit the formulas only; both
  scales are below an unknown eventual onset and no extrapolation is made.

## Suggested next attack

Study the 64 coarse quotients

\[
 A_m(a,b,c)
 ={[J_m(a,b)+\delta_{m,c}]_{64T_3}-\ell_{m,c}\over T_3}
 \in\{0,1,\ldots,63\}.
\tag{43}
\]

It is now enough to prove that these quotients avoid
`{0,61,11,63}` on a cofinal sequence of scales, or that at most `R<64` hit
that set eventually.  The first result eliminates every fixed room; the
second improves the global room bound to `R` by (36).
