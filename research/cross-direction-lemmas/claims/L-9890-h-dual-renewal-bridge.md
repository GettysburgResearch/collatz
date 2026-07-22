# L-9890 -- Dual H renewal valuations and integral capital dynamics

Claim ID: `L-9890`
Title: Consecutive nonzero H letters share one dual-valuation core and an exact integral renewal-height law
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-a`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR19/D-9501`, `PR19/L-9516`, `PR19/T-9502`, `PR19/T-9505`; post-Yu part also uses `PR19/T-9509`
Scope: nonzero renewal times on a hypothetical positive nonperiodic exact H orbit
Related counterexample candidates: none

## Setup

Use the exact H block coordinates of `PR19/D-9501`:

\[
p_i=2^{3r_i+2}u_i,
\qquad
u_i\equiv1\pmod4,
\qquad
p_i\equiv1\pmod3.
\tag{1}
\]

Let

\[
t_0<t_1<t_2<\cdots
\tag{2}
\]

be the indices with `r_(t_k)>0`, and put

\[
R_k=r_{t_k},
\qquad
L_k=t_{k+1}-t_k,
\qquad
U_k=u_{t_k}.
\tag{3}
\]

Thus the letters strictly between `t_k` and `t_(k+1)` are zero.

## Statement 1 -- rooms are high-valuation entrance sections

Let `P!=4` be a positive ordinary survivor in centered room `q` of
`PR19/L-9516`. Then

\[
P=4+4^{q+1}z,
\qquad
z>0\text{ odd},
\qquad
3\mid z.
\tag{4}
\]

After its `q` initial zero letters, the first nonzero-section state is

\[
Y=T_0^q(P)=4(1+3^qz)=2^{3R+2}U,
\qquad R\ge1,
\tag{5}
\]

and

\[
\boxed{
2^{3R}U-1=3^qz,
\qquad
v_3(2^{3R}U-1)\ge q+1.
}
\tag{6}
\]

Conversely, any positive nonzero-section survivor

\[
Y=2^{3R+2}U
\tag{7}
\]

with

\[
v_3(2^{3R}U-1)\ge q+1
\tag{8}
\]

has the unique `q`-zero ordinary predecessor

\[
\boxed{
P
=4+\left({4\over3}\right)^q(Y-4)
=4+4^{q+1}{2^{3R}U-1\over3^q},
}
\tag{9}
\]

and this predecessor lies in exactly room `q`.

### Proof

The room formula in `PR19/L-9516` gives the first two assertions of (4).
The ordinary state condition `P=1 mod3` then forces `3|z`. Its exact zero-run
formula gives (5), and division by four proves (6).

Conversely, (8) makes (9) an integer. The quotient in (9) is positive, odd,
and divisible by `3`, so

\[
v_2(P-4)=2q+2
\tag{10}
\]

and `P=1 mod3`. Forward application of the zero branch recovers `Y`, proving
existence and exact room membership. Injectivity of the zero branch proves
uniqueness. **QED**

## Statement 2 -- dual centered-renewal bridge

Take consecutive nonzero indices `i=t_k<j=t_(k+1)`. Write

\[
R=r_i,
\qquad
S=r_j,
\qquad
L=j-i,
\qquad
U=u_i,
\qquad
V=u_j.
\tag{11}
\]

There is a positive integer

\[
W\equiv5\pmod6
\tag{12}
\]

such that

\[
\boxed{
9^RU-1=4^LW,
\qquad
2^{3S}V-1=3^LW.
}
\tag{13}
\]

Equivalently,

\[
\boxed{
4^L(2^{3S}V-1)=3^L(9^RU-1).
}
\tag{14}
\]

The two endpoint residuals therefore have exact dual valuations

\[
\boxed{
v_2(9^RU-1)=2L,
\qquad
v_3(2^{3S}V-1)=L.
}
\tag{15}
\]

Every intermediate state is explicit:

\[
\boxed{
p_{i+m}=4+3^m4^{L-m+1}W,
\qquad1\le m\le L.
}
\tag{16}
\]

### Proof

The departure transition gives

\[
p_{i+1}-4=3(9^RU-1).
\tag{17}
\]

Each of the next `L-1` zero letters multiplies the centered difference by
`3/4`, while at arrival

\[
p_j-4=4(2^{3S}V-1).
\tag{18}
\]

Equating the two expressions and clearing `4^(L-1)` gives (14). Coprimality
of `3^L` and `4^L` gives the common integer `W` in (13). The arrival residual
is odd, while the departure residual is `-1 mod3`; hence `W` is odd and
`W=-1 mod3`, proving (12) and the exact valuations. Propagating the centered
difference through the zero run gives (16). **QED**

## Exact local universality

The bridge alone cannot bound the gap `L` through finite local legality. For
every prescribed `R,S,L>=1`, infinitely many exact local segments exist.
Choose `W` in the unique Chinese-remainder class

\[
1+4^LW
\equiv
(-1)^R3^{2R}
\pmod {3^{2R+1}},
\tag{19}
\]

\[
1+3^LW
\equiv
2^{3S}
\pmod {2^{3S+2}}.
\tag{20}
\]

Then

\[
U={1+4^LW\over9^R},
\qquad
V={1+3^LW\over2^{3S}}
\tag{21}
\]

have all exact legality congruences, and (16) supplies the intervening zero
letters. Adding multiples of the coprime product modulus gives infinitely many
positive examples.

For instance,

\[
(R,S,L,W,U,V)=(1,1,2,239,425,269)
\tag{22}
\]

gives

\[
13600\longmapsto11476\longmapsto8608.
\tag{23}
\]

## Statement 3 -- integral renewal height and exact sign law

Define the positive integer renewal height

\[
\boxed{
Z_k={p_{t_k}-4\over4}=2^{3R_k}U_k-1.
}
\tag{24}
\]

Put

\[
\kappa={\log(4/3)\over\log(9/8)},
\qquad
C_k=R_k-\kappa L_k,
\tag{25}
\]

and

\[
A_k=\left({9\over8}\right)^{C_k},
\qquad
c_k=\left({3\over4}\right)^{L_k}.
\tag{26}
\]

Then

\[
\boxed{
Z_{k+1}
=
\left({9\over8}\right)^{R_k}
\left({3\over4}\right)^{L_k}(Z_k+1)
-\left({3\over4}\right)^{L_k}
=A_kZ_k+(A_k-c_k).
}
\tag{27}
\]

The order change obeys

\[
\boxed{
C_k>0\Longrightarrow Z_{k+1}>Z_k,
}
\tag{28}
\]

and

\[
\boxed{
C_k<0\Longrightarrow Z_{k+1}\le Z_k.
}
\tag{29}
\]

On a nonperiodic orbit the inequality in (29) is strict. Since `kappa` is
irrational, `C_k=0` never occurs. Thus

\[
\boxed{
\operatorname{sgn}(Z_{k+1}-Z_k)
=
\operatorname{sgn}(R_k-\kappa L_k)
}
\tag{30}
\]

on every nonperiodic orbit. In particular, a consecutive run of negative
renewal capital strictly decreases the positive integer `Z` and has length at
most its initial value.

### Proof

Equation (13) gives `Z_(k+1)=3^(L_k)W_k`. Eliminating `W_k` and substituting
`U_k=(Z_k+1)/8^(R_k)` gives the first expression in (27). The definition of
`kappa` makes

\[
\left({9\over8}\right)^{R_k}
\left({3\over4}\right)^{L_k}
=\left({9\over8}\right)^{C_k},
\tag{31}
\]

proving the second.

Always `A_k-c_k>0`, because `R_k>=1`. If `C_k>0`, both terms in

\[
Z_{k+1}-Z_k=(A_k-1)Z_k+(A_k-c_k)
\tag{32}
\]

are positive. If `C_k<0`, then `A_k<1`, and the first expression in (27)
gives

\[
Z_{k+1}=A_k(Z_k+1)-c_k<Z_k+1-c_k<Z_k+1.
\tag{33}
\]

Both endpoints are integers, so `Z_(k+1)<=Z_k`. Equality makes
`p_(t_(k+1))=p_(t_k)`; determinism then gives a periodic return. It is
therefore impossible on a nonperiodic orbit. Finally, equality `C_k=0` would
equate a nontrivial power of `2` with a nontrivial power of `3`. **QED**

## Statement 4 -- exact renewal toll and normalized limit

Let `K_i`, `M_i=(9/8)^(K_i)`, and `Q_i=p_i/M_i` be the capital variables of
`PR19/T-9505`. Then

\[
K_{t_{k+1}}-K_{t_k}=C_k.
\tag{34}
\]

The recurrence factors as

\[
\boxed{
Z_{k+1}
=
\left({9\over8}\right)^{C_k}Z_k
\left(1+{1-(8/9)^{R_k}\over Z_k}\right).
}
\tag{35}
\]

Hence

\[
\log Z_{k+1}-\log Z_k
=C_k\log(9/8)+\varepsilon_k,
\tag{36}
\]

where

\[
0<\varepsilon_k
=
\log\left(1+{1-(8/9)^{R_k}\over Z_k}\right)
<{1\over Z_k}.
\tag{37}
\]

Moreover,

\[
\boxed{
{Z_k\over(9/8)^{K_{t_k}}}
\longrightarrow
{Q_\infty\over4}
\in(0,\infty).
}
\tag{38}
\]

Consequently `sum_k epsilon_k<infinity`. This is the integral renewal-height
normalization sought in `PR19/Q-9505`.

### Proof

Only the letter at `t_k` is nonzero in the half-open interval
`[t_k,t_(k+1))`, so the capital increment is exactly (34). Factoring
`A_k-c_k=A_k[1-(8/9)^(R_k)]` in (27) proves (35)--(37).

Finally,

\[
{Z_k\over M_{t_k}}
={p_{t_k}/4-1\over M_{t_k}}
={Q_{t_k}\over4}-{1\over M_{t_k}}.
\tag{39}
\]

`PR19/T-9502` gives `Q_i->Q_infinity in (0,infinity)` and `K_i->infinity`,
so (38) follows. Telescoping (36) against (34) then proves convergence of the
positive error sum. **QED**

## Statement 5 -- strongest inherited post-Yu consequence

Assume the remaining subcritical alternative of `PR19/T-9509`, including its
external Yu specialization. Put

\[
c_*={\log9\over\log8}.
\tag{40}
\]

Then

\[
R_k=o(c_*^{t_k}),
\qquad
\log U_k=o(c_*^{t_k}),
\tag{41}
\]

and the bridge forces

\[
\boxed{
L_k=o(c_*^{t_k}),
\qquad
\log W_k=o(c_*^{t_k}),
\qquad
\log Z_k=o(c_*^{t_k}).
}
\tag{42}
\]

In particular, both exact renewal valuations are subcritical:

\[
\boxed{
v_2(9^{R_k}U_k-1)=2L_k=o(c_*^{t_k}),
}
\tag{43}
\]

\[
\boxed{
v_3(2^{3R_{k+1}}U_{k+1}-1)=L_k=o(c_*^{t_k}).
}
\tag{44}
\]

If `q_n` is the centered zero-room depth of an ordinary survivor state, then

\[
\boxed{q_n=o(c_*^n).}
\tag{45}
\]

Without using Yu, the discounted excess gaps already satisfy

\[
\boxed{
\sum_k c_*^{-(t_k+1)}
\bigl(L_k\log4-R_k\log9\bigr)^+
<\infty,
}
\tag{46}
\]

\[
\boxed{
\sum_k c_*^{-(t_{k+1}+1)}
\bigl(L_k\log3-3R_{k+1}\log2\bigr)^+
<\infty.
}
\tag{47}
\]

### Proof

`PR19/T-9509` gives `R_k=o(c_*^(t_k))`, while the discounted core budget in
`PR19/T-9505` gives the second relation in (41). From (13),

\[
4^{L_k}W_k=9^{R_k}U_k-1<9^{R_k}U_k,
\tag{48}
\]

which proves the first two estimates in (42); the definition (24) proves the
third. Equations (43)--(44) are then (15).

Room form (4) gives

\[
3\cdot4^{q_n+1}<p_n
=\left({9\over8}\right)^{K_n}Q_n,
\tag{49}
\]

where `Q_n` is bounded by `PR19/T-9505` and `K_n=o(c_*^n)` by
`PR19/T-9509`. Taking logarithms proves (45).

Finally, (48) implies

\[
(L_k\log4-R_k\log9)^+\le\log U_k.
\tag{50}
\]

The arrival half of (13) similarly gives

\[
(L_k\log3-3R_{k+1}\log2)^+\le\log U_{k+1}.
\tag{51}
\]

The two series are subseries of the discounted core budget in
`PR19/T-9505`, proving (46)--(47). **QED**

## What this advances

- Centered zero rooms are exactly high-`3`-adic entrance sections.
- Every nonzero renewal interval carries one common integer `W_k` with exact
  dual `2`- and `3`-adic valuations.
- Contracting one-renewal words have exact weak descent; nonperiodicity makes
  it strict.
- The transformed height has an explicit sign law and convergent
  normalization, narrowing `PR19/Q-9505` to compatibility of successive
  bridge cores.
- Yu's subcritical conclusion now propagates to zero-run lengths, room depths,
  bridge heights, and both endpoint valuations.

## Dependency audit

- `PR19/D-9501` supplies the exact block transition and legality congruences.
- `PR19/L-9516` supplies centered rooms and zero-branch transport.
- `PR19/T-9502` supplies convergence of `Q_i` and capital divergence used in
  the normalized limit.
- `PR19/T-9505` supplies the discounted odd-core budget and the capital/core
  relations.
- Statements (41)--(45) inherit the unreviewed external Yu specialization in
  `PR19/T-9509`; no new external theorem is imported.
- Local universality uses only the Chinese remainder theorem.

## Gap audit

- No survivor is excluded. Local universality shows every fixed triple
  `(R,S,L)` is arithmetically realizable in isolation.
- Strict descent requires nonperiodicity; equality would be a positive
  periodic return, not an independently excluded case.
- The global obstruction is compatibility of the successive cores `W_k`, not
  existence of one bridge.
- The post-Yu conclusions remain conditional on the specialization audit
  already open in `PR19/T-9509`.
- Discounted excess budgets allow sparse late violations and are not pointwise
  bounds.

## Adversarial checks

- The gap contains `L-1` intervening zero letters but has length `L=j-i`;
  this is why (14) contains `4^L` and `3^L`.
- The weak descent in (29) uses integrality after the strict bound
  `Z_(k+1)<Z_k+1`; the affine slope inequality alone would be insufficient.
- The arrival valuation in (44) uses `R_(k+1),U_(k+1)`, not the departure
  core.
- Local CRT realizability is deliberately not promoted to a compatible
  infinite orbit.

## Remaining uncertainty

Can two consecutive bridge equations force a height or residue incompatibility
between `W_k` and `W_(k+1)`? Such a theorem would use both exact valuations at
once and could turn the finite discounted excess budgets into a contradiction.

## Suggested next attack

Eliminate the shared arrival core between two adjacent bridges and derive a
recurrence directly for `W_(k+1)/W_k`. Test whether the sign law forces too
many strict descents or whether the dual valuations violate a known
two-prime logarithmic-form bound.
