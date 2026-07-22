# Current integrated state

Last updated: 2026-07-22  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Status

There is currently **no positive-integer Collatz counterexample**, no regular
sanctuary, and no closed infinite corrected-stage grammar in this branch.

All complete-looking mathematical claims remain `PROPOSED` pending independent
reconstruction. Exact finite experiments are labeled `EMPIRICAL`; they are not
substituted for proofs.

## Fixed map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The branch contains an exact finite theory of parity cylinders, collision
fibers, mixed-radix rewrites, negative return phases, marked ordinary spines,
and cycle-padded negative towers. `CLAIMS.md` is the detailed index.

# Corrected-stage architecture

For the four phase-34 tower types,

\[
K_t=11(t+1),
\qquad
G_t=7(t+1).
\]

One corrected 256-transition stage is

\[
z^+={3^{A_m}z+C_m\over2^{D_m}},
\]

\[
A_m={5369\over2}2^m+1792,
\qquad
D_m={1085579\over256}2^m+2816.
\]

Writing its canonical correction and cap as `R_m,S_m`, every stage input/output
is

\[
z_m=R_m+2^{D_m}Y_m,
\]

\[
z_m^+=S_m+3^{A_m}Y_m.
\]

`T-0031` proves

\[
0\le Y_{m+1}<\frac{Y_m+3}{512}.
\]

Therefore every ordinary infinite realization eventually reaches `Y_m=0` and
must obey

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1})}
\]

at every sufficiently late scale.

The free quotient is not an infinite memory channel.

# Scaled ordinary-tail coordinate

For the stabilized types, put

```text
p = (5,30,20,56)
b = (9,54,36,24).
```

For an ordinary high tail `h_j`, define

\[
W_j=p_{i_j}+64h_j.
\]

`L-0031` proves the local recurrence

\[
\boxed{
2^{11(t_{j+1}+1)}W_{j+1}
=
3^{7(t_j+1)}W_j+b_{i_j}.}
\]

All connector seeds, caps, and residual offsets telescope. One complete stage
becomes a positive 257-term equation in powers of two and three.

`T-0032`, using the source-qualified finite-rank multiplicative-equation theorem
from PR #13, proves that any infinite ordinary corrected-stage path must
introduce infinitely many fresh prime factors in its boundary words. Fixed-prime
monomial and finite-library multiplicative schemas are excluded.

# One fixed real room

Define

\[
a_m={5369\over2}2^m+1792m,
\qquad
e_m={8459\over2}2^m+2816m,
\]

\[
H_m={3^{a_m}\over2^{e_m}}.
\]

`T-0033` proves that every assumed infinite ordinary path has one real number
`C_infinity` with

\[
\boxed{W_m=\lfloor C_\infty H_m\rfloor}
\]

and

\[
0<\{C_\infty H_m\}
<{216\over3^{7(2^m+1)}}.
\]

`T-0036` extends the same room through every local connector boundary. The tower
word is not independent control data:

\[
\boxed{i_{m,j}=p^{-1}(W_{m,j}\bmod64).}
\]

# Three simultaneous type signatures

`L-0032` gives the ordinary valuation signatures

\[
v_2(W_n)=\alpha_{i_n}\in\{0,1,2,3\},
\]

\[
v_3(W_{n+1})=\beta_{i_n}\in\{1,2,3\}.
\]

`L-0034` adds the exact real defect digit. If

\[
\varepsilon_n=C_\infty H_n-W_n,
\qquad
Z_n=3^{7(t_n+1)}\varepsilon_n,
\]

then

\[
Z_n=b_{i_n}
+\left({2048\over2187}\right)^{t_{n+1}+1}Z_{n+1},
\]

and, throughout the stabilized region,

\[
\boxed{b_{i_n}<Z_n<b_{i_n}+{1\over16}.}
\]

Thus every type is forced simultaneously by:

```text
one binary valuation,
one ternary valuation,
one leading real defect digit.
```

# Finite and transcendental room classification

`T-0037` proves

\[
\boxed{\#\mathscr C\le64,}
\]

where `mathscr C` is the set of eventual fixed rooms. One room determines at
most one eventual ordinary trajectory.

`T-0038` applies Ridout's theorem in the exact projective normalization audited
independently in PR #34. Every eventual room would have to be transcendental:

\[
\boxed{C_\infty\text{ is transcendental}.}
\]

Together with `T-0032`, the surviving class is therefore:

```text
at most 64 room constants,
each transcendental,
each determining one trajectory,
each forcing infinitely many fresh endpoint primes.
```

This is a classification, not an existence or nonexistence theorem.

# Three-symbol Hensel filter

At scale `m>=12`, put

\[
d=2^{m-8},
\qquad
t_j=(256+j)d
\quad(0\le j\le3).
\]

For a three-symbol prefix `(a,b,c)`, define

\[
M_m=2^{11(t_1+t_2+t_3+3)},
\]

\[
N_m=3^{7(t_0+t_1+t_2+3)},
\]

\[
\tau_m=N_1N_2b_a+T_1N_2b_b+T_1T_2b_c.
\]

`L-0033` defines the canonical address

\[
\boxed{
\rho_m(a,b,c)
=[-\tau_mN_m^{-1}]_{M_m}.}
\]

Lift it by six bits:

\[
[-\tau_mN_m^{-1}]_{64M_m}
=ho_m+M_mh_m,
\qquad0\le h_m<64.
\]

The canonical three-step output satisfies

\[
\boxed{\sigma_m\equiv-N_mh_m\pmod{64}.}
\]

Hence the fourth tower type exists exactly when this output belongs to

\[
\{5,30,20,56\}.
\]

When it exists, it is unique.

# The atomic twelve-bit frontier

Define the adjacent lower six-bit block

\[
q_m(a,b,c)
=\left\lfloor{64\rho_m(a,b,c)\over M_m}\right\rfloor.
\]

Because the room scale is exponentially smaller than `M_m/64`, every actual
room eventually requires

\[
\boxed{q_m=0}
\]

while simultaneously requiring the allowed output-lift condition above.

`T-0039` therefore reduces room existence to one adjacent twelve-bit pattern:

```text
upper six bits: an allowed output Hensel block;
lower six bits: the zero input-cell block.
```

Let `mathfrak Z_m` be the set of three-symbol prefixes satisfying both
conditions. Either of the following would exclude every room:

1. `mathfrak Z_m` is empty on a cofinal sequence of scales;
2. the exact overlap graph between `mathfrak Z_m` and `mathfrak Z_(m+1)` is empty
   cofinally.

This is now the smallest load-bearing arithmetic object in the branch.

# Exact finite audit

The portable standard-library experiment `X-0017` reproduces the exact
three-symbol filter at scales 12 and 13 and the real defect recurrence.

An independent GMP authoring audit extended the same lifted-inverse formulas
through scale 20. The allowed-output counts were

```text
m : 12 13 14 15 16 17 18 19 20
n :  5  3  4  6  3  4  5  2  5
```

and

\[
\boxed{\mathfrak Z_m=\varnothing}
\qquad(12\le m\le20).
\]

This finite emptiness is evidence only. It is not extrapolated to all scales.

# Current load-bearing frontier

The full 256-symbol search has collapsed to:

> Prove that the source-specific Newton lift cannot place an allowed six-bit
> output block immediately above a zero six-bit input-cell block at every
> sufficiently late scale—or construct one coherent transcendental room that
> does so and replay it from one finite positive integer.

The growing inverse-lift quotient contains `Theta(2^m)` new bits per scale. A
bounded finite-state argument cannot control it. The next theorem must use its
source-specific arithmetic, a completion-height/product-formula lower bound, or
an exact scale-doubling relation coupling the two adjacent blocks.
