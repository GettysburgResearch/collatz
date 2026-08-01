# L-6816 — Every displaced odd position pays a uniform mechanical-remainder loss

**Claim ID:** `L-6816`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-08-01  
**Dependencies:** the upper-mechanical extremizer; elementary affine-numerator algebra  
**Scope:** equal-length, equal-weight coefficient-first-crossing words  
**Counterexample status:** none

## 1. Setup

Fix a valid coefficient-first-crossing length `j` and its unique weight `q`.
Put

\[
P=2^j,
\qquad
Q=3^q,
\qquad
C={Q\over P},
\qquad
D=P-Q>0.
\tag{1}
\]

Let

\[
u=w^{\rm mech}_{j,q}
\]

be the upper-mechanical first-crossing word and let `v` be any other
first-crossing word of the same length and weight.  Write their odd positions,
indexed from zero, as

\[
e_1<\cdots<e_q,
\qquad
d_1<\cdots<d_q.
\tag{2}
\]

Prefix dominance gives

\[
d_i\le e_i.
\]

Put

\[
h_i=e_i-d_i\ge0
\tag{3}
\]

and define the displaced support

\[
\boxed{
R(v)=\#\{i:h_i>0\}.}
\tag{4}
\]

Let

\[
E_z={A_z\over P}
\]

be the normalized affine remainder of a word `z`.

## 2. Exact loss identity

The odd-position formula gives

\[
E_u
=C\sum_{i=1}^{q}{2^{e_i}\over3^i},
\qquad
E_v
=C\sum_{i=1}^{q}{2^{d_i}\over3^i}.
\tag{5}
\]

Since `d_i=e_i-h_i`, subtraction gives the exact identity

\[
\boxed{
E_u-E_v
=C\sum_{i=1}^{q}
{2^{e_i}\over3^i}
\left(1-2^{-h_i}\right).}
\tag{6}
\]

This is the complete Archimedean loss caused by moving the odd positions to
the left of their upper-mechanical locations.

## 3. Every mechanical odd contribution lies in one fixed corridor

Let

\[
\alpha={\log2\over\log3}.
\]

For the `i`th odd position of the upper-mechanical word,

\[
\lceil\alpha e_i\rceil=i-1,
\qquad
\lceil\alpha(e_i+1)\rceil=i.
\tag{7}
\]

Consequently

\[
i-1-\alpha<\alpha e_i\le i-1.
\tag{8}
\]

Using `2^x=3^(alpha*x)`, equation `(8)` gives

\[
\boxed{
{1\over6}
<
{2^{e_i}\over3^i}
\le
{1\over3}.}
\tag{9}
\]

The lower endpoint is `3^(-1-alpha)=1/6`; the upper endpoint is attained by
the first odd position `e_1=0`.

## 4. Uniform support loss

Whenever `h_i>0`,

\[
1-2^{-h_i}\ge{1\over2}.
\]

Keeping only the `R(v)` displaced indices in `(6)` and using `(9)`,

\[
\boxed{
E_u-E_v
>
{C\over12}R(v).}
\tag{10}
\]

At a first crossing,

\[
3^q\ge2^{j-1},
\]

and equality is impossible between positive powers of three and two. Hence
`C>1/2`, so the source-free numerical consequence is

\[
\boxed{
E_u-E_v>{R(v)\over24}.}
\tag{11}
\]

Unlike the earlier total-swap estimates, `(10)` does not deteriorate when a
large displacement is distributed among many positions or concentrated into
long moves.  Every distinct displaced odd position pays one fixed amount.

In integer numerator coordinates, put

\[
\Delta A=A_u-A_v.
\]

Then `(10)` is exactly

\[
\boxed{
\Delta A>{Q\over12}R(v).}
\tag{12}
\]

This is the form that couples directly to the complete denominator.

## 5. Pointwise support-corrected source envelope

Assume the canonical source `r_v` of `v` does not descend and write

\[
T_v^j(r_v)=r_v+d,
\qquad d\ge0.
\]

The exact affine equation gives

\[
E_v=(1-C)r_v+d
\tag{13}
\]

or, equivalently,

\[
\boxed{A_v=Dr_v+Pd.}
\tag{14}
\]

Therefore

\[
r_v\le {E_v\over1-C}.
\]

Put

\[
F_j={E_u\over1-C}
={A_u\over D}.
\tag{15}
\]

Combining `(10)--(15)`,

\[
\boxed{
 r_v
 <
 F_j
 -
 {C\,R(v)\over12(1-C)}.}
\tag{16}
\]

Thus a nonmechanical failure never reaches the full mechanical envelope.  Its
ordinary source loses an amount amplified by the same small coefficient gap
`1-C` that makes `F_j` large near lower convergents.

The exact complete-denominator face of the same statement is

\[
\boxed{
A_u-Dr_v
=Pd+\Delta A,}
\tag{17}
\]

with

\[
\boxed{
Pd+\Delta A>{Q\over12}R(v).}
\tag{18}
\]

At every prime-power factor `Q_s|D`, the common displacement equation

\[
A_v\equiv Qd\pmod {Q_s}
\]

is therefore equivalent to

\[
\boxed{
\Delta A
\equiv
A_u-Qd
\pmod {Q_s},}
\tag{19}
\]

while the same ordinary integer `Delta A` must satisfy `(12)`.  Hence the
complete prime-power compiler must reconstruct not only one common `d`, but a
mechanical loss numerator of support-forced Archimedean size.  No proper
factor alone supplies `(17)`.

Using only the one-third upper bound `E_u<q/3` from `L-6812`, `(16)` also gives
the explicit scalar estimate

\[
\boxed{
 r_v
 <
 {q/3-C R(v)/12\over1-C}.}
\tag{20}
\]

Equations `(16)--(20)` preserve source/endpoint notation: `r_v` is the
source; the endpoint is `r_v+d`.  No quotient involving `A_v-Qd` is
substituted for the source.

## 6. Strategic consequence

Any independent lower bound

\[
R(v)\ge R_0(j)
\]

for a complete obstruction class immediately weakens the source-coordinate
closure target from

\[
m_{j-1}^{\rm sup}>F_j
\]

to

\[
m_{j-1}^{\rm sup}
\ge
F_j-{C R_0(j)\over12(1-C)}.
\]

`T-6812` supplies the exact return-forced choice of `R_0(j)` and proves that
the weakened cofinal inequality still closes both coefficient lanes.

## 7. Gap audit

- The support loss is strict and elementary; it uses no distribution or
  logarithmic-form theorem.
- It does not by itself lower-bound the displaced support of a candidate.
- Equations `(17)--(19)` couple the support loss to the complete denominator,
  but do not prove the required residue avoidance.
- The correction is of order `R/(1-C)`; the unresolved source lower bound may
  still fail to dominate it.
- No proof of SC*, FC*, CST, or Collatz is claimed.
