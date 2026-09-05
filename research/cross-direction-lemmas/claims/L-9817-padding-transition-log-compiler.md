# L-9817 — Exact logarithmic transition compiler for padding-counter addresses

Claim ID: `L-9817`  
Title: Exponential counter charts turn the inverse-bulk scale step into an exactly valued finite logarithmic compiler  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9808`, `L-9811`; standard 2-adic LTE and logarithm facts; `PR3/T-0028` for the four padding-chart specializations  
Scope: exponential 2-adic isometries and the inverse-bulk scale transition  
Related counterexample candidates: none

## Definitions

Let

\[
\Omega(s)=\alpha+\beta b^s
\qquad(s\in\mathbb Z_2)
\tag{1}
\]

be a bijective isometry from `Z_2` to itself, where
`alpha,beta in Q_2`, `beta!=0`, and

\[
b\in1+8\mathbb Z_2,
\qquad b\ne1.
\]

Put

\[
\delta=\nu_2(b-1)=\nu_2(\log b),
\qquad
\lambda_0=\frac{\log b}{2^\delta}.
\tag{2}
\]

The isometry condition forces

\[
\nu_2(\beta)=-\delta.
\]

Thus

\[
\beta_0=2^\delta\beta
\tag{3}
\]

and `lambda_0` are odd 2-adic units.

Use the inverse bulk of `L-9808`:

\[
u_{m+1}=u_m+2^{e_m-1}u_m^2,
\qquad
e_m=m+\sigma-1,
\tag{4}
\]

where `u_m` is odd, and define

\[
s_m=\Omega^{-1}(u_m),
\qquad
\Delta s_m=s_{m+1}-s_m.
\tag{5}
\]

Finally, write

\[
N_m=e_m-1+\delta,
\qquad
c_m=\beta_0^{-1}b^{-s_m}u_m^2\in\mathbb Z_2^\times,
\tag{6}
\]

and

\[
\mathcal L(x)=\frac{\log(1+x)}x
=\sum_{j\ge0}\frac{(-1)^jx^j}{j+1}.
\tag{7}
\]

## Statement

### 1. Exact transition formula

The counter increment is

\[
\boxed{
\Delta s_m
=
\frac{
\log\!\left(
1+\dfrac{2^{e_m-1}u_m^2}{u_m-\alpha}
\right)
}{\log b}
=
\log_b\!\left(
1+\frac{2^{e_m-1}u_m^2}{u_m-\alpha}
\right).
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\Delta s_m
=2^{e_m-1}\Gamma_m,
\qquad
\Gamma_m
=\lambda_0^{-1}c_m\mathcal L(2^{N_m}c_m).
}
\tag{9}
\]

### 2. Exact valuation and leading odd unit

One has

\[
\boxed{
\nu_2(\Delta s_m)=e_m-1=m+\sigma-2.
}
\tag{10}
\]

The normalized increment `Gamma_m` is its exact leading odd unit. Moreover,

\[
\boxed{
\Gamma_m
\equiv
\lambda_0^{-1}\beta_0^{-1}b^{-s_m}u_m^2
\pmod{2^{N_m-1}}.
}
\tag{11}
\]

In fact the difference between the two sides of (11) has valuation exactly
`N_m-1`. In particular,

\[
\boxed{
\Delta s_m\equiv2^{e_m-1}\pmod{2^{e_m}}.
}
\tag{12}
\]

Thus the first changing address bit is a universal toggle; higher increment
bits contain the chart-dependent information.

### 3. Finite logarithmic polynomial and certified tail

For a unit `c` and `J>=1`, define

\[
\Phi_{N,J}(c)
=
\sum_{j=0}^{J-1}
\frac{(-1)^j2^{jN}c^{j+1}}{j+1}.
\tag{13}
\]

Every summand is integral. More explicitly, if

\[
\rho_j=\nu_2(j+1),
\qquad
o_j=\frac{j+1}{2^{\rho_j}},
\]

then its unsigned part is

\[
2^{jN-\rho_j}c^{j+1}o_j^{-1},
\tag{14}
\]

so only an odd ordinary denominator is inverted. The convergent limit is

\[
\Phi_N(c)=c\mathcal L(2^Nc),
\]

and the finite tail satisfies

\[
\boxed{
\nu_2\bigl(\Phi_N(c)-\Phi_{N,J}(c)\bigr)
\ge J(N-1).
}
\tag{15}
\]

Hence

\[
J_Q=\left\lceil\frac Q{N_m-1}\right\rceil
\tag{16}
\]

terms suffice for `Q` normalized increment bits. In the large initial range
`Q<=N_m-1`, one has `J_Q=1`, which is precisely congruence (11).

### 4. The normalized chart logarithm is also finitely compiled

Put

\[
d=\frac{b-1}{2^\delta}\in\mathbb Z_2^\times
\]

and, for `K>=1`, define

\[
\Lambda_K
=d\sum_{j=0}^{K-1}
\frac{(-1)^j2^{j\delta}d^j}{j+1}.
\tag{17}
\]

Then `Lambda_K` is odd and

\[
\boxed{
\nu_2(\lambda_0-\Lambda_K)\ge K(\delta-1),
\qquad
\nu_2(\lambda_0^{-1}-\Lambda_K^{-1})
\ge K(\delta-1).
}
\tag{18}
\]

Consequently

\[
K_Q=\left\lceil\frac Q{\delta-1}\right\rceil
\tag{19}
\]

finite terms compile the fixed chart unit `lambda_0^(-1) mod 2^Q`.

### 5. Compiler from ordinary bulk data and finite address bits

Let `P_(m,L)` be the ordinary polynomial in `V_m` from `L-9808`, and suppose
an ordinary integer `S` satisfies

\[
S\equiv s_m\pmod{2^H}.
\tag{20}
\]

Set

\[
U=P_{m,L},
\qquad
\widetilde c=\beta_0^{-1}b^{-S}U^2,
\tag{21}
\]

and define the finite transition compiler

\[
\widetilde\Gamma_{m;L,H,J,K}
=\Lambda_K^{-1}\Phi_{N_m,J}(\widetilde c).
\tag{22}
\]

It has the explicit error certificate

\[
\boxed{
\nu_2\!\left(
\Delta s_m
-2^{e_m-1}\widetilde\Gamma_{m;L,H,J,K}
\right)
\ge e_m-1+T,
}
\tag{23}
\]

where

\[
\boxed{
T=
\min\left\{
Le_m+1,
\delta+H,
J(N_m-1),
K(\delta-1)
\right\}.
}
\tag{24}
\]

Thus, for any requested `Q>=1`, the choices

\[
\boxed{
\begin{aligned}
L&=\max\!\left\{1,
\left\lceil\frac{Q-1}{e_m}\right\rceil\right\},\\
H&=\max\{0,Q-\delta\},\\
J&=\left\lceil\frac Q{N_m-1}\right\rceil,\\
K&=\left\lceil\frac Q{\delta-1}\right\rceil
\end{aligned}
}
\tag{25}
\]

give

\[
\boxed{
\Delta s_m
\equiv
2^{e_m-1}\widetilde\Gamma_{m;L,H,J,K}
\pmod{2^{e_m-1+Q}}.
}
\tag{26}
\]

All divisions in (17) and (22) reduce to powers of two and inversions of odd
residues. When `b`, `beta_0`, and the finite address word `S` are ordinary
chart data, (26) is a finite ordinary-arithmetic compiler.

If only `V_m` is supplied, the required word `S` can itself be obtained by the
finite permutation of `L-9811`:

\[
S
=\Omega_H^{-1}\bigl([P_{m,L}]_{2^H}\bigr),
\tag{27}
\]

because the choice (25) has `Le_m>=H`. This removes every completed 2-adic
input, but it retains a finite inverse-counter routing step.

### 6. Specialization to all four `PR3/T-0028` padding charts

For a fixed finite core of recovery length `r`, `PR3/T-0028` has

\[
P=2^{r-1},
\qquad
\Omega(s)
=\frac{\mu_*+3^{-g_*-7Ps}}{2^{r+1}}.
\tag{28}
\]

Here

\[
\alpha=\frac{\mu_*}{2^{r+1}},
\quad
\beta=\frac{3^{-g_*}}{2^{r+1}},
\quad
b=3^{-7P},
\quad
\delta=r+1,
\quad
\beta_0=3^{-g_*}.
\tag{29}
\]

Writing

\[
\ell_r=\frac{\log(3^{-7P})}{2^{r+1}}
\in\mathbb Z_2^\times,
\]

equations (8)--(9) become

\[
\boxed{
\Delta s_m
=
\frac{
\log\!\left(
1+2^{e_m+r}u_m^2\,3^{g_*+7Ps_m}
\right)
}{\log(3^{-7P})}
}
\tag{30}
\]

and

\[
\boxed{
2^{-(e_m-1)}\Delta s_m
=
\ell_r^{-1}u_m^2\,3^{g_*+7Ps_m}
\mathcal L\!\left(
2^{e_m+r}u_m^2\,3^{g_*+7Ps_m}
\right).
}
\tag{31}
\]

For the `q=3,a=7` bulk of `PR3/T-0030`, `e_m=m+2`. The four chart costs are:

| source mismatch | `r` | `P` | `delta` | `N_m` | address bits `H_Q` | transition terms `J_Q` | chart-log terms `K_Q` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 16 | 6 | `m+7` | `max(0,Q-6)` | `ceil(Q/(m+6))` | `ceil(Q/5)` |
| 6 | 4 | 8 | 5 | `m+6` | `max(0,Q-5)` | `ceil(Q/(m+5))` | `ceil(Q/4)` |
| 7 | 3 | 4 | 4 | `m+5` | `max(0,Q-4)` | `ceil(Q/(m+4))` | `ceil(Q/3)` |
| 8 | 2 | 2 | 3 | `m+4` | `max(0,Q-3)` | `ceil(Q/(m+3))` | `ceil(Q/2)` |

In every row,

\[
\boxed{\nu_2(\Delta s_m)=m+1.}
\tag{32}
\]

The bulk-polynomial cost common to the four rows is

\[
L_Q=\max\left\{1,
\left\lceil\frac{Q-1}{m+2}\right\rceil\right\}.
\tag{33}
\]

The finite-core residue `mu_*` disappears from (31): once the present address
is known, the transition depends only on the exponential chart slope, its
base, and the bulk word.

### 7. What this does and does not make causal

Equations (22)--(26) show that the division by `log b` is not a completed-log
oracle at finite precision: its normalized odd inverse is compiled by (17),
with the explicit cost (19). Given `S mod 2^H`, the increment is a genuine
finite transition law.

It is not, however, a self-starting append law from only the stabilized prefix

\[
s_m\pmod{2^{e_m-1}}.
\]

Indeed, (12) says that passing from `s_m` to `s_(m+1)` toggles the bit in
position `e_m-1`; to learn its new value one must know its old value, which is
not contained in the stabilized prefix. More generally, computing
`s_(m+1) mod 2^(e_m-1+Q)` from

\[
s_{m+1}=s_m+\Delta s_m
\]

requires `s_m` at that output precision, even though the increment itself
needs only `H=max(0,Q-delta)` of its low bits. Equation (27), or an equivalent
physical counter-address lift, still supplies the missing address information.

Thus the logarithmic division has been reduced to finite ordinary arithmetic,
but the causal coupling gap identified in `L-9811` remains a finite
inverse-permutation/address-routing gap.

## Proof

For nonzero ordinary integers `h`, 2-adic LTE gives

\[
\nu_2(b^h-1)=\delta+\nu_2(h).
\]

The same identity holds for every nonzero `h in Z_2`: write
`b^h=exp(h log b)` and use
`nu_2(exp(y)-1)=nu_2(y)` on `4Z_2`.

Therefore

\[
\nu_2(\Omega(s+h)-\Omega(s))
=\nu_2(\beta)+\delta+\nu_2(h).
\]

Since `Omega` is an isometry, `nu_2(beta)=-delta`; (2)--(3) are therefore odd
units as asserted.

Using `Omega(s_m)=u_m` and (4),

\[
\begin{aligned}
b^{\Delta s_m}
&=\frac{u_{m+1}-\alpha}{u_m-\alpha}\\
&=1+\frac{2^{e_m-1}u_m^2}{u_m-\alpha}\\
&=1+2^{e_m-1+\delta}
\beta_0^{-1}b^{-s_m}u_m^2\\
&=1+2^{N_m}c_m.
\end{aligned}
\tag{34}
\]

Taking 2-adic logarithms proves (8). Since

\[
\log b=2^\delta\lambda_0,
\]

factoring `2^(N_m)c_m` out of the numerator proves (9).

Because `N_m>=2` and `c_m` is odd,

\[
\nu_2\bigl(\log(1+2^{N_m}c_m)\bigr)=N_m.
\]

Division by `log b` proves (10). In (7), the first nonconstant term is
`-x/2`, of valuation `N_m-1`, while every later term has strictly larger
valuation. Hence

\[
\nu_2\bigl(\mathcal L(2^{N_m}c_m)-1\bigr)=N_m-1,
\]

which proves (11). Every odd 2-adic unit is `1 mod 2`, giving (12).

For (15), the `j`-th term in (13) has valuation

\[
jN-\nu_2(j+1).
\]

The elementary bound `nu_2(j+1)<=j` makes this at least `j(N-1)`.
Consequently every omitted term for `j>=J` lies in `2^(J(N-1))Z_2`; convergence
then proves (15). Applying the same argument with `N=delta` to

\[
\lambda_0
=d\mathcal L(2^\delta d)
\]

proves the first half of (18). Both units are odd, so subtracting their
reciprocals proves its second half.

It remains to prove the joint error bound. `L-9808` gives

\[
\nu_2(u_m-U)=Le_m.
\]

Both numbers are odd, so

\[
\nu_2(u_m^2-U^2)\ge Le_m+1.
\tag{35}
\]

LTE and (20) give

\[
\nu_2(b^{-s_m}-b^{-S})\ge\delta+H.
\tag{36}
\]

Equations (35)--(36) imply

\[
\nu_2(c_m-\widetilde c)
\ge\min\{Le_m+1,\delta+H\}.
\tag{37}
\]

The function `Phi_N(c)` is 1-Lipschitz on `Z_2`: this follows termwise from
its integral power series, whose leading term is `c`. Combine (15), (18), and
(37), and use that all prefactors are units. The ultrametric inequality gives
(23)--(24). The choices (25) make every entry of the minimum at least `Q`,
proving (26).

For the physical charts, LTE gives

\[
\nu_2(3^{7P}-1)
=1+2+\nu_2(7P)-1
=r+1,
\]

so (29) follows. Substitution in (8)--(9) proves (30)--(31), and the table is
the direct insertion of the four values from `PR3/T-0028`. This proves all
claims. ∎

## Motivation

`L-9811` proves that a padding-counter isometry transports the inverse-bulk
odometer without losing precision, but it leaves the transition itself as an
abstract inverse-image difference. The present lemma exposes that difference:
its valuation, leading unit, logarithmic tail, chart constant, and dependence
on ordinary bulk and address data are all explicit.

The result is useful for a physical router attack because it separates two
very different issues. The analytic-looking logarithm has a short certified
finite compiler, often just one transition-series term at scale `m`. The
remaining obstruction is supplying the moving address word inside the Collatz
state, not evaluating an infinite transcendental object.

## Dependency audit

- `L-9808` supplies the exact polynomial approximation
  `nu_2(u_m-P_(m,L))=Le_m` and the positive ordinary input `V_m`.
- `L-9811` supplies the finite inverse-permutation route (27) and independently
  predicts the exact valuation (10).
- LTE supplies the exponential valuation law and the four values
  `delta=r+1`.
- Only the standard convergent 2-adic logarithm series on `1+8Z_2` is used;
  its two required truncation bounds are proved above.
- `PR3/T-0028` is used only for the four chart parameters in (28).

## Gap audit

- The compiler is finite arithmetic, not yet one bounded local Collatz
  rewrite.
- Formula (27) is a finite permutation lookup/inversion, not a proof that the
  physical residual state emits the required counter word.
- The stabilized prefix of `s_m` alone omits exactly the next old bit needed
  to turn the universal toggle (12) into the next limit-address bit.
- Modular exponentiation, odd inversion, and the short logarithmic polynomial
  still need realization in the residual/counter grammar.
- No single marked ordinary orbit or compatible residual-cylinder evolution
  is produced.

## Adversarial tests

- Omitting the factor `2^delta` hidden in `beta` shifts the predicted
  transition valuation by `delta` and contradicts the isometry law.
- Dividing a modular term in (13) directly by an even `j+1` is invalid. Formula
  (14) first removes its exact power of two and inverts only the odd part.
- Replacing `H=max(0,Q-delta)` by `H=Q` is safe but obscures the `delta` free
  bits supplied by exponentiation; replacing it by a smaller value loses the
  stated uniform certificate.
- The statement `Delta s_m=2^(e_m-1) mod 2^e_m` does not reveal the new address
  bit unless the old bit at that position is already known.
- The finite logarithm compiler removes a completed-log oracle; it does not
  remove the inverse-counter routing in (27).

## Remaining uncertainty

None in the 2-adic transition algebra or precision bounds. The unresolved
question is whether the finite arithmetic and the missing address lift admit
a causal local realization in the physical collision grammar.

## Suggested next attack

Represent one output bit of the finite permutation (27) and the universal
toggle (12) in the same residual/counter cell. The first concrete target is a
one-bit identity that computes the old bit in position `e_m-1` from the
ordinary `V_m` block and then flips it. Only after that succeeds should the
higher-unit compiler (22) be embedded term by term.
