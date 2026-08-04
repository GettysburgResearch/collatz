# T-0034 — Adelic room–connector bridge and exact residual floor law

Claim ID: `T-0034`  
Title: After quotient extinction, the canonical residual is a floor orbit at the exact stage-surplus scale and its fractional defect is the connector prefix  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0017`, `L-0025`, `T-0024`, `T-0031`, `T-0033`  
Scope: every eventual cap-to-correction tail in the fixed corrected phase-34 stage architecture  
Related counterexample candidates: none

## Setup

Assume an infinite ordinary corrected-stage trajectory. By `T-0031`, there is a
scale `M` after which the free stage quotient is zero. Thus the residual input at
scale `m >= M` is the canonical stage correction

\[
\boxed{z_m=R_m.}
\tag{1}
\]

Let the first connector of stage `m` join tower types `i_(m,0)` and `i_(m,1)`.
Put

\[
B=2^m,
\qquad
t_{m,1}=B+\frac B{256},
\tag{2}
\]

\[
\boxed{
T_m^{\rm head}
=2^{11(t_{m,1}+1)}.}
\tag{3}
\]

Let `eta_(m,0)` be that connector seed and define its scaled binary word

\[
\boxed{
X_m=p_{i_{m,0}}+64\eta_{m,0}.}
\tag{4}
\]

The type constants satisfy

\[
p_i\in\{5,30,20,56\},
\qquad
0\le\eta_{m,0}<T_m^{\rm head},
\]

so

\[
\boxed{0<X_m<64T_m^{\rm head}.}
\tag{5}
\]

Let `C_infinity` and `H_m` be the fixed real room and homogeneous scale of
`T-0033`:

\[
W_m=\lfloor C_\infty H_m\rfloor,
\tag{6}
\]

\[
0<\varepsilon_m
:=C_\infty H_m-W_m
<\frac{216}{3^{7(B+1)}}.
\tag{7}
\]

## Statement

### 1. Exact residual homogeneous scale

Define

\[
\boxed{
J_m
=\frac{H_m}{64T_m^{\rm head}}.}
\tag{8}
\]

Then

\[
\boxed{
J_m
=
\frac{3^{a_m}}
{2^{f_m}},}
\tag{9}
\]

where

\[
\boxed{
a_m=\frac{5369}{2}2^m+1792m,}
\tag{10}
\]

\[
\boxed{
f_m
=\frac{1085579}{256}2^m+2816m+17.}
\tag{11}
\]

The leading binary growth rate is exactly the full-stage surplus constant of
`T-0024`:

\[
\boxed{
\log_2J_m
=
\Gamma 2^m
+
(1792\log_2 3-2816)m
-17,}
\tag{12}
\]

\[
\boxed{
\Gamma
=
\frac{687232\log_2 3-1085579}{256}>0.}
\tag{13}
\]

### 2. Exact residual floor law

For every `m >= M`,

\[
\boxed{
R_m=\left\lfloor C_\infty J_m\right\rfloor.}
\tag{14}
\]

More precisely,

\[
\boxed{
C_\infty J_m-R_m
=
\frac{X_m+\varepsilon_m}{64T_m^{\rm head}}.}
\tag{15}
\]

The right side lies strictly between zero and one.

### 3. Connector-prefix shrinking interval

Since (14) identifies the integer part, equation (15) gives the exact fractional
part

\[
\boxed{
\{C_\infty J_m\}
=
\frac{X_m}{64T_m^{\rm head}}
+
\frac{\varepsilon_m}{64T_m^{\rm head}}.}
\tag{16}
\]

Hence

\[
\boxed{
0<
\{C_\infty J_m\}
-
\frac{X_m}{64T_m^{\rm head}}
<
\frac{27}
{8T_m^{\rm head}3^{7(B+1)}}.}
\tag{17}
\]

The dyadic rational

\[
\frac{X_m}{64T_m^{\rm head}}
=
\frac{\eta_{m,0}}{T_m^{\rm head}}
+
\frac{p_{i_{m,0}}}{64T_m^{\rm head}}
\tag{18}
\]

is the complete canonical first-connector word, normalized to `[0,1)`. The real
room orbit must hit an interval immediately above this exact dyadic address,
with width smaller than the right side of (17).

### 4. Exact asymptotic correction height

The scale `J_m` tends to infinity, and

\[
\boxed{
\frac{R_m}{J_m}\longrightarrow C_\infty.}
\tag{19}
\]

In particular,

\[
\boxed{
\log_2R_m
=
\Gamma2^m+O(m).}
\tag{20}
\]

Thus the canonical residual correction has the precise leading height predicted
by the aggregate stage-surplus computation. It is neither an arbitrary point of
the full dyadic cylinder nor merely bounded by the earlier completion-height
upper estimates.

## Proof

At a stage boundary the scaled-tail definition of `L-0031` is

\[
W_m
=X_m+64T_m^{\rm head}z_m.
\tag{21}
\]

Using quotient extinction (1),

\[
\boxed{
W_m=X_m+64T_m^{\rm head}R_m.}
\tag{22}
\]

Divide the fixed-room identity

\[
C_\infty H_m=W_m+\varepsilon_m
\]

by `64 T_m^(head)` and substitute (22). This gives (15).

The anchor bound is slightly stronger than (5). Since

\[
\eta_{m,0}\le T_m^{\rm head}-1,
\qquad
p_i\le56,
\]

we have

\[
X_m
\le
64T_m^{\rm head}-8.
\tag{23}
\]

Also (7) is less than one. Therefore

\[
0<X_m+\varepsilon_m<64T_m^{\rm head},
\]

so the right side of (15) lies in `(0,1)`. Since `R_m` is integral, this proves
(14) and (16). Substituting (7) into (16) gives (17).

For the exponent of `J_m`, use

\[
11(t_{m,1}+1)
=
\frac{2827}{256}B+11.
\]

The denominator exponent in `H_m` is

\[
\frac{8459}{2}B+2816m.
\]

Adding the head exponent and the factor `64=2^6` gives

\[
\left(
\frac{8459}{2}+\frac{2827}{256}
\right)B
+2816m+17
=
\frac{1085579}{256}B+2816m+17,
\]

which proves (9)--(11). Equation (12) follows after taking binary logarithms.
`T-0024` and the exact lower bound `log_2(3)>84/53` from `L-0025` give
`Gamma>0`, so `J_m` tends to infinity.

Finally, (14)--(15) give

\[
0<
C_\infty-\frac{R_m}{J_m}
<\frac1{J_m},
\]

which proves (19). Taking logarithms gives (20). ∎

## The bridge exposed

The same hypothetical trajectory is now described by one exact formula in two
completions:

```text
real side:
    R_m = floor(C_infinity J_m);

binary/canonical side:
    fractional part(C_infinity J_m)
      = normalized connector seed + tiny positive defect.
```

This is an adelic shrinking-target condition. The real orbit does not merely
enter a small interval: it must land immediately above a specific dyadic word
computed by the connector compiler.

The leading exponent in `J_m` is exactly the `Gamma` that first appeared as the
full-stage residual information surplus. The earlier information budget has
therefore acquired a direct ordinary meaning: it is the asymptotic bit length of
the canonical correction itself.

## Strategic consequences

A complete cap-stitch construction must simultaneously satisfy:

1. the canonical seam graph of PR #34;
2. the fresh-prime necessity of `T-0032`;
3. the room floor law (14);
4. the dyadic-address approximation (17).

A promising obstruction would couple the real distance in (17) to the 2-adic
valuation of a seam mismatch through a product formula or completion-height
argument. A promising construction would instead make the connector compiler
emit the dyadic expansion of the real room orbit at every scale.

## Gap audit

- The theorem assumes an infinite ordinary stage path and the quotient-extinction conclusion of `T-0031`.
- A real number can in principle hit prescribed shrinking targets; no general nonexistence theorem is claimed.
- Equation (17) does not yet include the 84 middle triple-seam constraints from PR #34.
- No finite initialization, cap-stitch tail, or Collatz counterexample is constructed.

## Adversarial tests

`X-0016` verifies the exponent identity (11), the homogeneous recurrence, and
finite exact floor normalizations. The all-scale bridge follows from the exact
identities above, not numerical extrapolation.