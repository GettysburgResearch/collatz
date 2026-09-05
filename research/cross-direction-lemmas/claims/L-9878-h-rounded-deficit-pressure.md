# L-9878 -- Rounded-critical contraction and exact H deficit pressure

Claim ID: `L-9878`  
Title: Positive exact H chains pay a sharp linear rounded-deficit toll, with sparse deficits forcing large odd cores  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `PR19/D-9501`  
Scope: every genuine positive exact H block chain; no critical-regime assumption  
Related counterexample candidates: none

## Statement

Let

\[
2^{3r_{n+1}+2}u_{n+1}-3^{2r_n+1}u_n=1
\tag{1}
\]

be a positive exact H chain.  Thus `r_n>=0`, `u_n>0`, `u_n=1 mod 4`,
and the corresponding genuine block states have `p_n>=16`.  Put

\[
c_*={\log9\over\log8},
\qquad
s_n=\lceil c_*r_n\rceil-r_{n+1},
\tag{2}
\]

and split the signed rounded deficit as

\[
d_n=(s_n)^+,
\qquad
o_n=(-s_n)^+,
\qquad
s_n=d_n-o_n.
\tag{3}
\]

Define also

\[
\theta_n=\lceil c_*r_n\rceil-c_*r_n,
\qquad
H_n=u_n-1,
\qquad
X_n=3^{2r_n+1}u_n,
\tag{4}
\]

and

\[
\omega_n
=
\log{4\over3}-\log\left(1+{1\over X_n}\right)
=
\log{4X_n\over3(X_n+1)}.
\tag{5}
\]

### 1. Rounded-critical contraction

If

\[
r_{n+1}\ge\lceil c_*r_n\rceil,
\tag{6}
\]

then

\[
\boxed{H_{n+1}\le{3\over4}H_n.}
\tag{7}
\]

Consequently, a run of rounded-critical steps starting at a positive height
`H_a` reaches `H=0` after more than `log_(4/3)(H_a)` steps.  Every infinite
chain that stays in genuine states must therefore contain infinitely many
below-rounded-critical steps `d_n>=1`.

### 2. Exact one-step pressure identity and sharp toll

For every positive exact transition,

\[
\boxed{
{H_{n+1}+1\over H_n+1}
=
{u_{n+1}\over u_n}
=
8^{s_n-\theta_n}e^{-\omega_n}.
}
\tag{8}
\]

If `H_n>0`, then equivalently

\[
\boxed{
{H_{n+1}\over H_n}
=
\rho_n+{\rho_n-1\over H_n},
\qquad
\rho_n=8^{s_n-\theta_n}e^{-\omega_n}.
}
\tag{9}
\]

Every positive exact transition obeys the sharp lower bound

\[
\boxed{X_n\ge147,}
\tag{10}
\]

attained by the adjacent transition `(r,u)=(0,49) -> (0,37)`.  Hence

\[
\boxed{
\log{49\over37}\le\omega_n<\log{4\over3},
\qquad
{3\over4}<e^{-\omega_n}\le{37\over49}.
}
\tag{11}
\]

### 3. Exact cumulative deficit balance

For a block `a<=n<b`, set

\[
L=b-a,
\quad
D=\sum_{n=a}^{b-1}d_n,
\quad
O=\sum_{n=a}^{b-1}o_n,
\quad
\Theta=\sum_{n=a}^{b-1}\theta_n,
\quad
\Omega=\sum_{n=a}^{b-1}\omega_n.
\tag{12}
\]

Then

\[
\boxed{
{u_b\over u_a}
=
8^{D-O-\Theta}e^{-\Omega}
}
\tag{13}
\]

and therefore

\[
\boxed{
8^{D-O-\Theta}\left({3\over4}\right)^L
<
{u_b\over u_a}
\le
8^{D-O-\Theta}\left({37\over49}\right)^L.
}
\tag{14}
\]

Put

\[
\delta_H=\log_8{49\over37}
=0.135085492828753\ldots .
\tag{15}
\]

Since `u_b>=1`, every block satisfies

\[
\boxed{
D\ge O+\Theta+\delta_HL-\log_8u_a.
}
\tag{16}
\]

In particular, on every infinite positive exact chain,

\[
\boxed{
\liminf_{N\to\infty}{1\over N}\sum_{n<N}d_n
\ge\delta_H.
}
\tag{17}
\]

More sharply,

\[
\liminf_{N\to\infty}
{D_N-O_N-\Theta_N\over N}
\ge\delta_H.
\tag{18}
\]

Thus rounded valuation overshoots must be repaid one-for-one, in addition to
the universal baseline toll and the accumulated irrational rounding phase.

If a block recovers or grows its core by a factor `R>=1`, so `u_b>=Ru_a`,
then

\[
\boxed{
D\ge O+\Theta+\delta_HL+\log_8R.
}
\tag{19}
\]

### 4. Finite-core trap and the `u=1` escape

For any `B>=1`, the condition

\[
D-O-\Theta-\delta_HL
\le\log_8{B\over u_a}
\tag{20}
\]

forces `u_b<=B`.  If the corresponding absolute upper bound

\[
u_a8^{D-O-\Theta}\left({37\over49}\right)^L<5,
\tag{20a}
\]

then exact residue legality forces

\[
\boxed{u_b=1.}
\tag{21}
\]

This is a finite **core** trap, not a finite full-state trap, because `r_b`
can remain unbounded.  At the edge `u=1`, elementary LTE gives

\[
\nu_2(3^{2r+1}+1)=2,
\tag{22}
\]

so the next index is `r'=0`.  If `r=0`, this is the formal fixed state
`p=4`.  If `r>0`, the next step pays the large deficit

\[
d=\lceil c_*r\rceil
\tag{23}
\]

and escapes to

\[
u'={3^{2r+1}+1\over4}.
\tag{24}
\]

### 5. Frequency--height dichotomy

On a positive-deficit step `d_n>=1`,

\[
\boxed{
{3\over4}8^{d_n-1}
<
{u_{n+1}\over u_n}
\le
{37\over49}8^{d_n}.
}
\tag{25}
\]

In particular, `d_n>=2` forces

\[
\boxed{{u_{n+1}\over u_n}>6.}
\tag{26}
\]

For a block as above, let

\[
M=\#\{a\le n<b:d_n>0\},
\qquad
U=\max_{a\le n\le b}u_n.
\tag{27}
\]

Whenever its numerator is positive,

\[
\boxed{
M>
{\delta_HL-\log_8u_a
\over
1+\log_8(4U/3)}.
}
\tag{28}
\]

Equivalently, sparse deficit events force a large core:

\[
\boxed{
U>{3\over4}
8^{(\delta_HL-\log_8u_a)/M-1}.
}
\tag{29}
\]

Thus a polynomial core bound `U<=CL^A` forces

\[
M=\Omega(L/\log L),
\tag{30}
\]

while a uniformly bounded core forces positive lower density of deficit
indices.

## Definitions

The block coordinates are those of `PR19/D-9501`.  A step is
**rounded-critical** when (6) holds, equivalently `s_n<=0`; it is
**below-rounded-critical** when `s_n=d_n>=1`.  The shift `H=u-1` is essential:
the affine `+1` in (1) prevents an exact multiplicative recurrence for `H`
itself.

The word **positive** excludes the formal `p=4` state.  All estimates remain
valid up to the first visit to that boundary; (22)--(24) describe the `u=1`
edge separately.

## Motivation

The critical recurrence in PR #19 identifies the near-Pillai scale
`r_(n+1) about c_*r_n`, but it did not quantify how often or how strongly an
ordinary infinite chain must fall below that scale.  Equation (13) supplies
an exact balance law.  It turns the affine toll in every H block into a sharp
linear demand for positive rounded deficit, and separates three costs:
valuation overshoot, irrational rounding phase, and actual core recovery.

This is useful in two directions.  Any construction must budget at least
`delta_H` positive-deficit mass per step.  Conversely, any argument that
bounds core height converts that mass into a quantitative frequency of
below-critical events through (28).

## Proof

### Rounded-critical contraction

If (6) holds, then

\[
2^{3r_{n+1}+2}\ge4\,3^{2r_n}.
\tag{31}
\]

Using (1), `u_n=H_n+1`, and `3^(-2r_n)<=1` gives

\[
H_{n+1}
\le
{3u_n\over4}+{1\over4\,3^{2r_n}}-1
\le{3\over4}H_n,
\tag{32}
\]

which proves (7).  Iteration proves the run-length assertion because `H` is
a nonnegative integer.

### Exact pressure and the toll gap

From

\[
r_{n+1}=c_*r_n+\theta_n-s_n
\tag{33}
\]

and `2^(3c_*r_n)=3^(2r_n)`, division of (1) by
`2^(3r_(n+1)+2)u_n` gives

\[
{u_{n+1}\over u_n}
=
{3\over4}2^{3(s_n-\theta_n)}
\left(1+{1\over X_n}\right),
\tag{34}
\]

which is (8).  Equation (9) follows from
`H_(n+1)=rho_n(H_n+1)-1`.

Exact legality gives

\[
u_n\equiv
\begin{cases}
1\pmod {12},&r_n\text{ even},\\
5\pmod {12},&r_n\text{ odd}.
\end{cases}
\tag{35}
\]

If `r_n>=2`, then `X_n>=3^5=243`.  If `r_n=1` and `X_n<147`, the
only residue-compatible candidate is `u_n=5`; but `3^3*5+1=136` has
2-adic valuation 3, not a value of the required form `3r_(n+1)+2`.  If
`r_n=0`, positivity and `X_n<147` leave `u_n=13,25,37`.  The values
`3u_n+1` are `40,76,112`; their valuations or odd quotients fail exact
next-state legality.  Therefore (10) holds.  The state `(0,49)` maps to
`(0,37)`, proving sharpness, and monotonicity of `X/(X+1)` proves (11).

### Cumulative balance and traps

Multiplying (8) from `a` to `b-1` proves (13).  Inserting (11) gives (14).
The lower bound `u_b>=1` gives (16), and division by `L` gives (17)--(18).
If `u_b/u_a>=R`, the same upper estimate gives (19).  Conditions
(20), (20a), and (21) follow immediately from the upper half of (14) and
(35).
Equation (22) is the odd-exponent case of elementary LTE, proving the edge
dichotomy.

### Deficit concentration

On a deficit step, `s_n=d_n`, `0<=theta_n<1`, and (11) inserted into (8)
gives (25).  The lower bound there proves (26).  Since both endpoints are at
most `U`, each deficit obeys

\[
d_n<1+\log_8{4U\over3}.
\tag{36}
\]

Summing this inequality over the `M` deficit indices and using (16) after
dropping the nonnegative `O+Theta` terms proves (28).  Some deficit is at
least `D/M`; combining this with (25) proves (29).  The two stated growth
consequences are immediate.  QED

## Dependency audit

- `PR19/D-9501` supplies the exact recurrence, state factorization, and
  residue legality.
- The remaining ingredients are elementary inequalities, exact
  telescoping, and the standard two-adic LTE identities displayed above.
- No critical-regime asymptotic, logarithmic-form theorem, ergodic theorem,
  or empirical orbit assertion is used.
- The finite proof of `X>=147` checks only the residue-compatible candidates
  forced below that threshold.

## Gap audit

- Linear total deficit does not imply positive density of deficit **indices**
  without a height bound; the mass may be concentrated in rare large jumps.
- A unit deficit can contract or expand because its rounding phase is not
  controlled.
- The finite trap bounds the odd core, not the full state; `r` remains
  unbounded.
- Reaching `u=1` at `r>0` causes a large escape rather than termination.
- Large core jumps may later be erased by long rounded-critical runs.
- The theorem does not show that below-critical behavior forces the critical
  alternative `Z_infinity>0`, nor does it exclude that alternative.
- The constant `49/37` is sharp among adjacent positive exact transitions,
  although the extremizing transition is not asserted to have an infinite
  exact future.

## Adversarial tests

- The multiplicative law is for `H+1=u`, not for `H`; omitting the affine
  correction in (9) is false.
- The rounding phase has sign `-theta_n` in (8).  Reversing it destroys the
  exact cancellation `2^(3c_*r)=3^(2r)`.
- Overshoot is `o_n=(-s_n)^+` and therefore enters (13) with a minus sign.
- The lower toll endpoint is attained at `X=147`; replacing `37/49` by a
  smaller universal factor would be false.
- In (28), `M` counts positive-deficit indices while `D` counts their total
  mass.  They coincide only when every deficit is one.
- At `H=0`, formula (9) is undefined; equations (8) and (22)--(24) cover that
  boundary.

## Remaining uncertainty

Can the critical asymptotic and its discounted core budget coexist with the
linear pressure (16) once deficit concentration and repeated-core repulsion
are imposed simultaneously?  A contradiction would require a new upper
bound on either deficit mass or the size of the compensating core spikes.

## Suggested next attack

Combine (16), the repeated-core capacity theorem `L-9879`, and the critical
discounted core budget from `PR19/T-9508`.  Either force too many large core
spikes for that budget, or construct an explicit abstract sequence showing
why the present one-dimensional estimates still leave room.
