# T-9820 -- The base cell and third-symbol offset share one Newton carry

Claim ID: `T-9820`
Title: The joint coarse cell factors as one inverse unit times one connector coefficient, and at least one symbol lane retains the full growing lift ambiguity
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave18-cap-joint-carry`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave16-completion-cold-review`; `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9806`, `T-9813`, and `T-9817`; frozen corrected PR #3 connector algebra at `c37e96efd0dcc9dd610d59041234dc57e74090fd`
Scope: the stabilized two-transition head at every scale `m>=12`
Related counterexample candidates: none

## Setup

Use

\[
 N_j=3^{7(t_j+1)},
 \qquad
 T_j=2^{11(t_j+1)}
 \qquad(0\le j\le3),
\tag{1}
\]

and put

\[
 P=N_0N_1,
 \qquad
 Q=T_2T_3,
 \qquad
 \mathcal W={T_2\over64},
 \qquad
 M=64T_3=2^{L_m}.
\tag{2}
\]

Fix the first two symbols `(a,b)`.  For the base last-symbol pair `(c,k)=(0,0)`,
let `X_0,Y_0` be the connector from `a@t_0` to `b@t_1`, and let `X_2`
be the connector from `0@t_2` to `0@t_3`.  The telescoped head constant is

\[
 \boxed{
 64F=N_1Y_0+b_b-T_2X_2.
 }
\tag{3}
\]

Write its canonical correction as in `T-9806`:

\[
 r_{0,0}=[-FP^{-1}]_Q=\mathcal WJ+V,
\tag{4}
\]

\[
 0\le J<M,
 \qquad
 0\le V<\mathcal W.
\tag{5}
\]

The common inverse and third-symbol translations are

\[
 u_m=[(PN_2)^{-1}]_M,
 \qquad
 \delta_{m,c}=[-u_m(b_c-b_0)]_M,
\tag{6}
\]

where

\[
 (p_0,b_0)=(5,9),
 \qquad
 (b_0,b_1,b_2,b_3)=(9,54,36,24).
\tag{7}
\]

Finally define the realized joint cell

\[
 s_{m,c}(a,b)=[J_m(a,b)+\delta_{m,c}]_M.
\tag{8}
\]

Its top-six quotient is exactly the room-filter datum

\[
 A_m(a,b,c)=\left\lfloor{s_{m,c}(a,b)\over T_3}\right\rfloor.
\tag{9}
\]

## Theorem 1 -- exact connector factorization

Define

\[
 G_m(a,b)={PV+F\over\mathcal W}.
\tag{10}
\]

Then `G_m(a,b)` is an integer, and so is

\[
 \boxed{
 Z_m(a,b)=G_m(a,b)+X_2
 ={64PV+N_1Y_0+b_b\over T_2}.
 }
\tag{11}
\]

The base cell itself is

\[
 \boxed{
 J_m(a,b)=[(X_2-Z_m(a,b))P^{-1}]_M.
 }
\tag{12}
\]

For every third symbol, put

\[
 \boxed{
 H_{m,c}(a,b)=T_3p_0-b_c-N_2Z_m(a,b).
 }
\tag{13}
\]

Then the apparent sum of a base-cell carry and an inverse-power translation
collapses to one product:

\[
 \boxed{
 s_{m,c}(a,b)=[u_mH_{m,c}(a,b)]_M.
 }
\tag{14}
\]

Thus `J_m` and `delta_(m,c)` do not carry independent copies of the inverse
defect.  Their inverse parts are perfectly correlated through the single unit
`u_m`; the remaining connector information is exactly `H_(m,c)`.

### Proof

Since `r_(0,0)` is the correction modulo `Q`, equation (4) gives

\[
 P(\mathcal WJ+V)+F\equiv0
 \pmod {64T_3\mathcal W}.
\tag{15}
\]

Reduction modulo `mathcal W` proves that `PV+F` is divisible by
`mathcal W`, so (10) is integral.  Dividing (15) by `mathcal W` gives

\[
 PJ+G_m(a,b)\equiv0\pmod M.
\tag{16}
\]

Multiplying (10) by 64 and using (3) and `64mathcal W=T_2` yields

\[
 T_2G_m
 =64PV+N_1Y_0+b_b-T_2X_2.
\tag{17}
\]

This proves the integrality and the second formula in (11).  Equations
(16) and `G_m=Z_m-X_2` prove (12).

The canonical connector formula gives

\[
 N_2X_2\equiv T_3p_0-b_0\pmod M.
\tag{18}
\]

Using `P^(-1)=N_2u_m` modulo `M`, equations (6), (8), and (12) now give

\[
\begin{aligned}
J+\delta_{m,c}
&\equiv
u_m\{N_2(X_2-Z_m)-(b_c-b_0)\}\\
&\equiv
u_m(T_3p_0-b_c-N_2Z_m)
\pmod M.
\end{aligned}
\tag{19}
\]

Taking the canonical residue proves (14). **QED**

### Scaled-coordinate interpretation

If

\[
 W_1^{(V)}=Y_0+64N_0V,
\tag{20}
\]

then (11) is equivalently

\[
 \boxed{
 Z_m(a,b)={N_1W_1^{(V)}+b_b\over T_2}.
 }
\tag{21}
\]

Thus `Z_m` is the exact scaled word after two toll transitions begun from the
common within-cell remainder `V`.  It is not an ad hoc correction variable.

## Theorem 2 -- joint Newton law and exact cancellation depth

Use the widths and carry of `T-9817`:

\[
 L_{m+1}=2L_m-17,
 \qquad
 \Delta_m=L_m-18,
\tag{22}
\]

\[
 c_m=\left[
 {\mathcal U_m u_m-1\over2^{L_m}}
 \right]_{2^{\Delta_m}},
 \qquad
 \mathcal U_m=PN_2.
\tag{23}
\]

For a fixed next-scale coefficient `H_(m+1,c)`, define the zero-carry
baseline

\[
 B_{m+1,c}
 =3^{21}u_m^2H_{m+1,c}.
\tag{24}
\]

Then the exact next joint cell is

\[
 \boxed{
 s_{m+1,c}
 =\left[
 B_{m+1,c}(1-2^{L_m+1}c_m)
 \right]_{2^{L_{m+1}}}.
 }
\tag{25}
\]

Let

\[
 h_{m+1,c}=\nu_2(H_{m+1,c}),
\tag{26}
\]

with `h_(m+1,c)=infinity` if the coefficient is zero.  Relative to (24), the
carry in (25) depends on exactly

\[
 \boxed{
 \max\{0,\Delta_m-h_{m+1,c}\}
 }
\tag{27}
\]

potential bits of `c_m`.  When `h_(m+1,c)<Delta_m`, distinct residues of
`c_m modulo 2^(Delta_m-h_(m+1,c))` give distinct joint-cell corrections.
In particular, an odd `H_(m+1,c)` makes multiplication by it a 2-adic
isometry and retains the full `Delta_m`-bit inverse-lift ambiguity.

### Proof

The exact inverse update of `T-9817/(27)` is

\[
 u_{m+1}
 =\left[
 3^{21}u_m^2(1-2^{L_m+1}c_m)
 \right]_{2^{L_{m+1}}}.
\tag{28}
\]

Multiplying by `H_(m+1,c)` and applying (14) at scale `m+1` proves (25).
If `H=2^hh^*` with `h^*` odd, the carry term begins at bit
`L_m+1+h`.  It vanishes modulo `2^(L_(m+1))` once `h>=Delta_m`, and otherwise
only the lowest

\[
 L_{m+1}-(L_m+1+h)=\Delta_m-h
\tag{29}
\]

bits of `c_m` survive.  Multiplication by the remaining odd factor is
invertible, proving injectivity and (27). **QED**

## Theorem 3 -- full cancellation is impossible on all four lanes

At every stabilized scale and for every fixed `(a,b)`, either

\[
 \boxed{
 Z_m(a,b)\equiv0\pmod2
 \quad\Longrightarrow\quad
 H_{m,0}\text{ is odd and }H_{m,1},H_{m,2},H_{m,3}\text{ are even},
 }
\tag{30}
\]

or

\[
 \boxed{
 Z_m(a,b)\equiv1\pmod2
 \quad\Longrightarrow\quad
 H_{m,0}\text{ is even and }H_{m,1},H_{m,2},H_{m,3}\text{ are odd}.
 }
\tag{31}
\]

Consequently at least one, and in fact either one or three, of the four
third-symbol lanes retains the complete growing inverse carry in Theorem 2.

In the universal lift-fiber information model of `T-9817/Theorem 3`, fix the
entire current inverse residue and grant the next coefficient `H_(m+1,c)`
for free.  On every odd-coefficient lane, the compatible next joint cells form
a complete coset modulo `2^(L_m+1)`.  Their top-six quotients therefore attain
all 64 values, each exactly

\[
 \boxed{2^{\Delta_m-6}}
\tag{32}
\]

times.  Hence adjoining `J_m` to the six-bit state does not produce a
universal bounded-state transition: at least one lane still requires the
distinguished growing carry or equivalent source information.

### Proof

Since `T_3` is even and `N_2` is odd, (13) gives

\[
 H_{m,c}\equiv b_c+Z_m(a,b)\pmod2.
\tag{33}
\]

The value `b_0=9` is odd, while `54,36,24` are even.  This proves
(30)--(31).  On an odd lane, multiplication by `H` permutes the complete
next-inverse coset from `T-9817/(37)`.  Addition has already been absorbed by
the exact product (14).  Since

\[
 L_{m+1}-(L_m+1)=\Delta_m\ge6,
\tag{34}
\]

each top-six interval contains `2^(Delta_m-6)` elements of that coset.  This
proves (32) and the stated bounded-projection obstruction. **QED**

## What this advances

- It answers the correlation question exactly: the base cell and
  third-symbol translation share the same inverse unit and factor as (14).
  There are not two independent Newton defects to track.
- It isolates the only remaining connector datum as the scaled two-step word
  `Z_m(a,b)`, equivalently the coefficient `H_(m,c)`.
- It measures cancellation rather than merely allowing it: valuation `h`
  removes exactly `h` possible carry bits, up to the full width `Delta_m`.
- The parity dichotomy proves that this cancellation cannot occur on every
  third-symbol lane simultaneously.
- At each stabilized scale, the low six bits of `Z_m(a,b)` and `J_m(a,b)`
  are affinely and bijectively equivalent, so retaining both adds no
  same-scale bounded information.

## Dependency, novelty, and source audit

- `T-9806` supplies (3)--(6), including the telescoped connector identity and
  the two-level decomposition.  Its audited blob is
  `c2c03ff398fdf80dc0ac13a4d995eab8680e829a`.
- `T-9813` identifies (9) as the exact room-filter quotient; its audited blob
  is `5230750e23bec39a744ca9561465a32dd474d544`.
- `T-9817` supplies (22)--(23), (28), and the precise universal lift-fiber
  model used in Theorem 3.
- The frozen connector formula (18) and corrected core values (7) were
  refreshed against live PR #3 head
  `c37e96efd0dcc9dd610d59041234dc57e74090fd`.  Live PR #33 head
  `2cfe2506e2a5e86157c8ac970bd9466ce86a6891` is contextual only.
- A later read-only comparison through live `PR3` head
  `537e1cab2e8dacc444e973e730daa463273bab6f` found the frozen source files
  unchanged.  New `PR3/L-0033` and `T-0039` admit the exact crosswalk
  `h_(L0033)=A_m+25 mod64`,
  `q_(T0039)=floor(64ell_m/T_3)`, and
  `64A_m+q_(T0039)=floor(s_(m,c)/(T_3/64))`.  Thus their two-block room
  filter is one affine labeling of the top twelve bits of the joint cell,
  not a second inverse coordinate.
- Live `PR33/T-9705` at
  `c9d62bce3e93f5785f72e4520bc576863d9379eb` proposes a globally stronger
  ordinary exclusion through a connector-free Evertse argument.  It is
  comparison only and is not imported or independently source-audited here.
- Notation must remain fenced: this claim's integral connector word `Z_m` is
  not the real defect digit `Z_n` of live `PR3/L-0034` or the physical scaled
  boundary `Z_j` of live `PR33/L-9704`; likewise `h_(L0033)` is an output digit,
  not the valuation `h_(m,c)` in (26).
- The factorization (14), scaled interpretation (21), cancellation-depth law
  (27), parity no-go (30)--(32), and low-six-bit equivalence (36)--(38) are
  new.

## Gap and scope audit

- The actual base-3 source chooses one carry `c_m` and one correlated
  connector word `Z_(m+1)(a,b)`.  The universal lift fiber does not assert
  that this distinguished trajectory branches.
- Parity guarantees an odd lane, not that an actual room decodes to that lane.
  No hit or avoidance result for `{0,61,11,63}` follows.
- No scale recurrence for `Z_m(a,b)` is proved.  A special source correlation
  between `Z_(m+1)` and `c_m` could still select or cancel the realized top
  six bits despite the universal no-go.
- The affine equivalence (36)--(37) is strictly same-scale.  It neither
  relates scale `m` to scale `m+1` nor supplies the missing source recurrence.
- When `H` is even, (27) measures the inverse-carry loss but does not include
  any separate information needed to compute `H` itself.
- No bounded-scale computation is extrapolated, and no room, cap chain,
  marked initialization, or Collatz conclusion is proved or refuted.
- If live `PR33/T-9705` survives independent review, its global Evertse route
  supersedes the need for this local cap recurrence inside the frozen stage
  class.  The scale-law target below remains an independent elementary and
  Evertse-free structural question.

## Exact checks

- Direct integer reconstruction at `m=12,13` verified (10)--(14) for all 16
  first-symbol pairs and all four `c` values.
- At both scales and for every `(a,b)`, the observed odd-lane count was exactly
  one or three as forced by (30)--(31); this check is redundant with parity.
- The sign in (13) was checked from
  `N_2X_2 congruent T_3p_0-b_0`, not inferred from numerical residues.
- The information statement in Theorem 3 is explicitly universal over lifts
  compatible with the truncated inverse.  It does not replace the
  distinguished source transition by a branching process.
- Direct substitution at `m=12,13` verified (36)--(38) for all 16
  first-symbol pairs.  This numerical check is redundant with the modular
  proof.

## Scale-law target

Derive a scale law for the single scaled connector word

\[
 Z_m(a,b)={64P_mV_m(a,b)+N_{m,1}Y_{m,0}(a,b)+b_b\over T_{m,2}}.
\tag{35}
\]

## Corollary 4 -- same-scale low-six-bit equivalence

At every stabilized scale, (12) and `64\mid M_m` give

\[
 \boxed{
 Z_m(a,b)\equiv X_2-P_mJ_m(a,b)
       \equiv5-57J_m(a,b)
       \equiv5+7J_m(a,b)\pmod{64}.
 }
\tag{36}
\]

Equivalently, since `57^(-1) congruent 9 (mod 64)`,

\[
 \boxed{
 J_m(a,b)\equiv9\bigl(5-Z_m(a,b)\bigr)
       \equiv45-9Z_m(a,b)\pmod{64}.
 }
\tag{37}
\]

In particular,

\[
 \boxed{Z_m(a,b)\equiv J_m(a,b)+1\pmod2.}
\tag{38}
\]

### Proof and source audit

Equation (12) is `P_mJ_m congruent X_2-Z_m (mod M_m)`, and (1) makes
`M_m=64T_{m,3}` divisible by 64.  At stabilized scales,
`t_j congruent 0 (mod 16)`, so (1) gives
`N_{m,j} congruent 3^7 congruent 11 (mod 64)`.  Reducing (18) modulo 64
therefore gives `11X_2 congruent -9 congruent 55 (mod 64)`, whence
`X_2 congruent 5 (mod 64)`.  Also
`P_m=N_{m,0}N_{m,1} congruent 11^2 congruent 57 (mod 64)`.  Reducing (12)
therefore proves (36).  Because `57*9 congruent 1 (mod 64)`, solving for
`J_m` gives (37), and reduction modulo 2 gives (38). **QED**

Multiplication by either odd coefficient `7` or `-9` permutes
`Z/64Z`.  Thus `Z_m(a,b) mod 64` and `J_m(a,b) mod 64` are bijectively
equivalent information at one fixed scale.  This statement is same-scale
only: it gives no transition from `m` to `m+1` and no scale recurrence.

## Suggested next attack

Only a correlation between its next-scale residue and the source carry `c_m`
can now defeat the odd-lane obstruction.  Conversely, proving their relevant
top bits independent, or merely showing that the decoded room lane is odd
cofinally, would turn this no-go into a room-pruning theorem.
