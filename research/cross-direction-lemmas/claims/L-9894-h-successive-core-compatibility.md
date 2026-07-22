# L-9894 -- Successive H renewal cores obey one two-place compatibility law

Claim ID: `L-9894`
Title: Adjacent H bridge cores satisfy an exact elimination identity, shared-prime firewall, and second integral sign law
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-a`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9890`, `PR19/D-9501`, `PR19/T-9505`; post-Yu part also uses `PR19/T-9509`
Scope: the central algebra of three consecutive nonzero renewal times; discounted conclusions assume a hypothetical positive nonperiodic infinite exact H orbit
Related counterexample candidates: none

## Setup

Use the nonzero renewal times and variables of `L-9890`:

\[
t_0<t_1<t_2<\cdots,
\qquad
R_k=r_{t_k},
\qquad
L_k=t_{k+1}-t_k,
\qquad
U_k=u_{t_k}.
\tag{1}
\]

At one interior renewal index `k>=1`, abbreviate

\[
a=L_{k-1},
\qquad b=L_k,
\qquad R=R_k,
\qquad U=U_k,
\tag{2}
\]

\[
X=W_{k-1},
\qquad Y=W_k.
\tag{3}
\]

Thus `X` arrives at the central nonzero state `t_k`, while `Y` departs from
it. Every core `U,X,Y` is positive and coprime to 6.

## Statement 1 -- the simultaneous two-place star

The two adjacent bridges of `L-9890` share the exact central system

\[
\boxed{
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU.
}
\tag{4}
\]

In particular,

\[
\boxed{
v_3(8^RU-1)=a,
\qquad
v_2(9^RU-1)=2b.
}
\tag{5}
\]

Eliminating the central core gives the exact successive-core compatibility
law

\[
\boxed{
8^R4^bY-9^R3^aX=9^R-8^R.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
Y
={9^R3^a\over8^R4^b}X
+{9^R-8^R\over8^R4^b}.
}
\tag{7}
\]

The central exact-state congruences also give

\[
\boxed{
X\equiv3^{-a}(2^{3R}-1)
\pmod {2^{3R+2}},
}
\tag{8}
\]

\[
\boxed{
Y\equiv4^{-b}((-1)^R3^{2R}-1)
\pmod {3^{2R+1}}.
}
\tag{9}
\]

### Proof

Apply `L-9890/(13)` first to the bridge ending at `t_k`, then to the bridge
starting there. The arrival equation is

\[
2^{3R}U-1=3^aX,
\tag{10}
\]

and the departure equation is

\[
9^RU-1=4^bY.
\tag{11}
\]

These are (4)--(5), and eliminating `U` proves (6)--(7).

The exact H coordinate has `U=1 mod4`, so (10) modulo `2^(3R+2)` proves
(8). The ordinary-state condition

\[
2^{3R+2}U\equiv1\pmod3
\tag{12}
\]

gives `U=(-1)^R mod3`; substituting in (11) modulo `3^(2R+1)` proves (9).
**QED**

## Statement 2 -- the shared-prime firewall

The central core shares no prime with either adjacent renewal core:

\[
\boxed{\gcd(U,XY)=1.}
\tag{13}
\]

The two adjacent cores can share only divisors of the central exponential
difference:

\[
\boxed{\gcd(X,Y)\mid9^R-8^R.}
\tag{14}
\]

Consequently, if

\[
\ell^e\mid\gcd(X,Y),
\tag{15}
\]

then `ell>=5` and

\[
\boxed{
\operatorname{ord}_{\ell^e}(9\cdot8^{-1})\mid R.
}
\tag{16}
\]

A plateau `X=Y=W` is therefore resonant:

\[
\boxed{
W\mid9^R-8^R,
\qquad
W\le9^R-8^R.
}
\tag{17}
\]

### Proof

If a prime divides `U` and `X`, the first equation in (4) is simultaneously
one and zero modulo that prime. The second equation gives the same
contradiction for `U` and `Y`, proving (13).

Every common divisor of `X` and `Y` divides the left side of (6), hence the
right side. Since both cores are coprime to 6, every prime in (15) is at least
5 and `8` is invertible modulo `ell^e`. Dividing

\[
9^R\equiv8^R\pmod {\ell^e}
\tag{18}
\]

by `8^R` proves (16). Equation (17) is the case `X=Y`. **QED**

## Statement 3 -- a second integral sign law

Define

\[
\Lambda_k
=R_k\log(9/8)
+L_{k-1}\log3
-L_k\log4.
\tag{19}
\]

Then (7) factors exactly as

\[
\boxed{
Y
=e^{\Lambda_k}X
\left(
1+{1-(8/9)^R\over3^aX}
\right).
}
\tag{20}
\]

The coefficient `e^(Lambda_k)` is never one, and integrality gives

\[
\boxed{
\Lambda_k>0\Longrightarrow Y>X,
}
\tag{21}
\]

\[
\boxed{
\Lambda_k<0\Longrightarrow Y\le X.
}
\tag{22}
\]

Unlike the integral-height law of `L-9890`, equality in (22) need not repeat
the full H state. It does, however, obey the resonance firewall (17).

Let

\[
\kappa={\log(4/3)\over\log(9/8)},
\qquad
C_k=R_k-\kappa L_k
\tag{23}
\]

be the renewal capital of `L-9890`. Then

\[
\boxed{
\Lambda_k
=C_k\log(9/8)
+(L_{k-1}-L_k)\log3.
}
\tag{24}
\]

Hence positive capital together with `L_k<=L_(k-1)` makes both integral
renewal heights grow, while negative capital together with
`L_k>=L_(k-1)` makes `Z` strictly decrease on a nonperiodic chain and makes
`W` weakly decrease.

Finally, the exact small logarithmic form is

\[
\boxed{
0<
\log{Y\over X}-\Lambda_k
=
\log\left(
1+{1-(8/9)^R\over3^aX}
\right)
<{1\over3^aX}.
}
\tag{25}
\]

Since `3^aX=Z_k`, the middle quantity is exactly the renewal toll
`epsilon_k` of `L-9890`; its sum converges along a nonperiodic survivor.

### Proof

Factoring the slope from (7) gives (20). Equality `Lambda_k=0` would give

\[
9^R3^a=8^R4^b,
\tag{26}
\]

which equates a positive power of 3 with a positive power of 2.

If `Lambda_k>0`, both factors multiplying `X` in (20) exceed one, proving
(21). If `Lambda_k<0`, put

\[
\eta={1-(8/9)^R\over3^a},
\qquad0<\eta<{1\over3}.
\tag{27}
\]

Then `Y=e^(Lambda_k)(X+eta)<X+eta<X+1`. Since `X,Y` are integers, (22)
follows. Equation (24) is direct substitution from (23), and
`log(1+x)<x` proves (25). **QED**

## Statement 4 -- the algebraic central system is CRT-universal

For every prescribed `R,a,b>=1`, infinitely many positive algebraic central
tuples satisfy (4) and the central exact-state congruences. Choose `U` in the
unique CRT class

\[
8^RU\equiv1-3^a\pmod {3^{a+1}},
\tag{28}
\]

\[
9^RU\equiv1+4^b\pmod {2^{2b+1}}.
\tag{29}
\]

Then

\[
X={8^RU-1\over3^a},
\qquad
Y={9^RU-1\over4^b}
\tag{30}
\]

are positive for every sufficiently large lift and obey `X=Y=5 mod6` in
the sense that each is congruent to 5 modulo 6. The same congruences force
the required central conditions `U=1 mod4` and `2^(3R+2)U=1 mod3`.

This does not realize a finite three-renewal orbit segment. It does not impose
the two outer bridge equations

\[
1+4^aX=9^{R_{k-1}}U_{k-1},
\qquad
1+3^bY=8^{R_{k+1}}U_{k+1}.
\tag{30a}
\]

For example,

\[
(R,a,b,U,X,Y)=(3,2,1,197,11207,35903)
\tag{31}
\]

satisfies

\[
3^2\cdot11207+1=8^3\cdot197,
\qquad
4\cdot35903+1=9^3\cdot197.
\tag{32}
\]

Here

\[
\gcd(11207,35903)=7,
\qquad
9^3-8^3=217=7\cdot31,
\tag{33}
\]

so the firewall is attained nontrivially. A contracting example is

\[
(R,a,b,U,X,Y)=(2,1,3,241,5141,305),
\tag{34}
\]

for which `Lambda<0` and `Y<X`.

These are central-system examples only. For example, (31) has

\[
v_3(1+4^aX)=1,
\qquad
v_2(1+3^bY)=1,
\tag{34a}
\]

so it cannot satisfy (30a) with positive neighboring renewal letters.

### Proof

The moduli in (28)--(29) are coprime. Equation (28) makes the first numerator
have exact 3-adic valuation `a` and its quotient `-1 mod3`; (29) makes the
second numerator have exact 2-adic valuation `2b` and its quotient odd.
Both quotients are therefore `5 mod6`. Reduction of (29) modulo four gives
`U=1 mod4`, while reduction of (28) modulo three gives the central
ordinary-state congruence. Adding positive multiples of the product modulus
gives infinitely many stars. **QED**

## Statement 5 -- joint discounted two-place pressure

Assume from here that the variables come from a hypothetical positive
nonperiodic infinite exact H orbit satisfying the hypotheses of
`PR19/T-9505`.

Define the central excess

\[
\mathcal P_k
=
(L_{k-1}\log3-R_k\log8)^+
+(L_k\log4-R_k\log9)^+.
\tag{35}
\]

Then (4) gives the pointwise bound

\[
\boxed{\mathcal P_k\le2\log U_k.}
\tag{36}
\]

Consequently the core budget of `PR19/T-9505` implies

\[
\boxed{
\sum_{k\ge1}
c_*^{-(t_k+1)}\mathcal P_k<\infty,
\qquad
c_*={\log9\over\log8}.
}
\tag{37}
\]

No new logarithmic-form theorem is used here.

Under the remaining subcritical alternative of `PR19/T-9509`, including its
external Yu specialization,

\[
\boxed{
L_{k-1},L_k,
\log X,log Y,
\log\gcd(X,Y)
=o(c_*^{t_k}).
}
\tag{38}
\]

### Proof

From (4),

\[
3^{L_{k-1}}W_{k-1}<8^{R_k}U_k,
\qquad
4^{L_k}W_k<9^{R_k}U_k.
\tag{39}
\]

Since both `W` cores are at least one, each positive part in (35) is at most
`log U_k`, proving (36)--(37).

The post-Yu bounds in `L-9890` put both adjacent gaps and core heights on the
stated subcritical scale. Finally, (14) gives

\[
\log\gcd(X,Y)
\le\log(9^{R_k}-8^{R_k})
<R_k\log9
=o(c_*^{t_k}),
\tag{40}
\]

proving (38). **QED**

## What this advances

- `L-9890` attached one dual-valuation core to each renewal interval.
  Equation (6) is the first exact constraint linking two successive cores
  through their shared central state.
- Persistent prime powers are quarantined to exact multiplicative-order
  progressions of the central nonzero letter.
- The new `W` sign law couples the renewal capital to changes in both adjacent
  gap lengths and supplies the same summable toll from a second coordinate.
- Algebraic central CRT universality proves that no fixed triple `(R,a,b)` can
  be excluded by the central compatibility law alone; it does not realize the
  two outer bridges.
- The two-place pressure (37) packages both adjacent valuation excesses into
  one inherited discounted budget.

## Dependency audit

- `L-9890` and `PR19/D-9501` supply the two bridge equations and exact-state
  congruences.
- The elimination law, firewall, order condition, sign law, and local CRT
  realization are elementary.
- `PR19/T-9505` supplies the discounted core budget and convergence of the
  renewal tolls.
- Equation (38) additionally depends on `PR19/T-9509` and inherits its
  external-specialization audit.

## Gap audit

- No infinite H chain is excluded.
- A `W` plateau need not repeat the H state; it is only forced into the
  resonance condition (17).
- The firewall controls reused prime powers but does not yet force enough new
  prime mass.
- Central CRT universality need not complete even one finite two-bridge orbit
  segment and is not compatibility of successive central stars.
- The joint budget is still compatible with sparse large excesses.
- No logarithmic-form estimate beyond the existing PR #19 packet is imported.

## Adversarial checks

- `X=W_(k-1)` arrives at `t_k`, while `Y=W_k` departs; reversing these indices
  changes both exponents in (4).
- The order condition excludes primes 2 and 3 because every bridge core is
  `5 mod6`.
- Negative `Lambda` gives only weak `W` descent. Strictness does not follow
  from nonperiodicity because a plateau need not repeat the full state.
- The two local examples satisfy both equations in (4) exactly.
- Local universality realizes one algebraic central star, not its outer
  bridges or an infinite sequence.
- The post-Yu line is explicitly conditional on `PR19/T-9509`.

## Remaining uncertainty

Can reused prime powers carry most of the size of successive cores without
forcing excessive divisibility of the central letters `R_k`? The exact
firewall reduces that question to multiplicative orders.

## Suggested next attack

Put

\[
G_k=\gcd(W_{k-1},W_k),
\qquad
F_k={W_k\over G_k}.
\tag{41}
\]

Prove a prime-persistence/fresh-mass dichotomy: either the discounted sum of
`log F_k` exceeds the `T-9505` budget, or the order conditions imposed by
`G_k` force a capital/gap profile incompatible with the post-Yu subcritical
alternative. A simultaneous estimate for
`v_3(8^R U-1)` and `v_2(9^R U-1)` would be the other natural route.
