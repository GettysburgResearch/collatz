# Session addendum — adelic room–connector bridge and generator height obstruction

Date: 2026-07-22  
Agent: `gpt56-pro-01`  
Issue: `#2`

## Exact room–connector bridge

The fixed-room theorem `T-0033` combines with quotient extinction from `T-0031` in a particularly direct way.

After the free quotient reaches zero, the stage-boundary scaled tail is

\[
W_m=X_m+64T_m^{\rm head}R_m,
\]

where `X_m` is the complete scaled first-connector word and `R_m` is the canonical residual correction.

Dividing the fixed-room identity

\[
C_\infty H_m=W_m+\varepsilon_m
\]

by `64 T_m^(head)` gives `T-0034`:

\[
R_m=\lfloor C_\infty J_m\rfloor,
\]

\[
\{C_\infty J_m\}
=
{X_m\over64T_m^{\rm head}}
+
{\varepsilon_m\over64T_m^{\rm head}}.
\]

The second term is positive and doubly-exponentially small. Thus the real room orbit must land immediately above the exact normalized binary connector word.

The residual homogeneous scale is

\[
J_m={3^{a_m}\over2^{f_m}},
\]

\[
f_m={1085579\over256}2^m+2816m+17.
\]

Its leading logarithmic coefficient is exactly

\[
\Gamma={687232\log_2 3-1085579\over256},
\]

the same coefficient first found as full-stage information surplus. Consequently

\[
\log_2R_m=\Gamma2^m+O(m).
\]

The bit-surplus calculation now has an exact ordinary interpretation: it is the asymptotic height of the canonical residual itself.

## Quadratic-generator obstruction

The positive quadratic generator

\[
V_m={3^{7\cdot2^m}-1\over2^{m+2}}
\]

was the most natural source of forward-generated bits and fresh primes. Its height, however, is not resonant with the canonical correction.

`T-0035` proves that no fixed rational polynomial in finitely many shifts

\[
V_{m+c_1},\ldots,V_{m+c_s}
\]

can equal `R_m` infinitely often. After expansion, every such polynomial has leading logarithmic coefficient

\[
7r\log_2 3
\]

for one dyadic rational `r`, while the correction coefficient is `Gamma`. Equality would force `log_2 3` rational.

For the affine ansatz the mismatch is quantitative:

\[
\Gamma-7\log_2 3
>{41273\over13568}>3.
\]

Hence a multiplier converting `V_m` into `R_m` requires more than

\[
3\cdot2^m-O(m)
\]

bits. Fixed coefficients or finite control labels cannot supply it.

## Updated frontier

A hypothetical corrected-stage path must now satisfy four simultaneous demands:

1. cap-to-correction stitching and PR #34's collar/triple-seam constraints;
2. infinitely many fresh endpoint primes by `T-0032`;
3. the real fixed-room shrinking targets of `T-0033`;
4. the exact dyadic room–connector approximation of `T-0034`.

The literal fixed-polynomial quadratic-generator ansatz is closed by `T-0035`. A constructive use of `V_m` would need an additional exponentially large binary renormalization channel tied directly to the connector address.

No counterexample or finite initialization is claimed.
