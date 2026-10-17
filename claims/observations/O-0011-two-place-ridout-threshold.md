# O-0011 — The fixed-room approximants cross the two-place Ridout threshold

Claim ID: `O-0011`  
Title: Exact real, 2-adic, and 3-adic approximation product for the corrected-stage room  
Status: `PROPOSED NATIVE INEQUALITY / CONDITIONAL COROLLARY`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0032`, `T-0033`  
External source needed: an imported exact statement of Ridout's extension of Roth's theorem  
Scope: the fixed real room attached to any assumed infinite ordinary corrected-stage path  
Related counterexample candidates: none

## Setup

Let

\[
C_\infty>0
\]

be the fixed real room of `T-0033`. At scale `m`, write

\[
H_m={3^{a_m}\over2^{e_m}},
\tag{1}
\]

where

\[
a_m={5369\over2}2^m+1792m,
\tag{2}
\]

\[
e_m={8459\over2}2^m+2816m.
\tag{3}
\]

The stage-boundary integer satisfies

\[
W_m=\lfloor C_\infty H_m\rfloor
\tag{4}
\]

and

\[
\boxed{
0<C_\infty-{W_m2^{e_m}\over3^{a_m}}
<
{216\,2^{e_m}
\over3^{a_m+7\cdot2^m+7}}.}
\tag{5}
\]

Put

\[
g_m=v_3(W_m).
\tag{6}
\]

By `L-0032`,

\[
1\le g_m\le3
\tag{7}
\]

at every sufficiently late boundary. Define the reduced rational approximant

\[
\boxed{
{P_m\over Q_m}
=
{2^{e_m}(W_m/3^{g_m})
\over
3^{a_m-g_m}}.}
\tag{8}
\]

Then `gcd(P_m,Q_m)=1`.

## Native theorem

### 1. Exact local factors

Let

\[
\alpha_m=v_2(W_m)\in\{0,1,2,3\}.
\tag{9}
\]

Then

\[
\boxed{|P_m|_2=2^{-e_m-\alpha_m},}
\tag{10}
\]

\[
\boxed{|Q_m|_3=3^{-a_m+g_m}.}
\tag{11}
\]

### 2. Two-place approximation product

The real approximation and the two local factors satisfy

\[
\boxed{
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
<
72\,Q_m^{-2}\,3^{-7\cdot2^m}.}
\tag{12}
\]

### 3. Uniform exponent above two

For every `m >= 12`,

\[
\boxed{
3^{-7\cdot2^m}<Q_m^{-1/512}.}
\tag{13}
\]

Consequently

\[
\boxed{
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
<
72\,Q_m^{-2-1/512}.}
\tag{14}
\]

Let

\[
\mathcal H_m=\max(|P_m|,Q_m).
\tag{15}
\]

Because `P_m/Q_m` converges to the fixed positive number `C_infinity`, there is
one constant `K` with

\[
Q_m\le\mathcal H_m\le KQ_m
\tag{16}
\]

for every sufficiently large `m`. Hence, after absorbing the fixed constants,

\[
\boxed{
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
<
\mathcal H_m^{-2-1/1024}}
\tag{17}
\]

for all sufficiently large scales.

## Proof

Since only a power of three is removed from `W_m`, its binary valuation is
unchanged. Equation (10) follows from the factor `2^(e_m)` in `P_m` and
`L-0032`. Equation (11) is immediate from the definition of `Q_m`.

Multiply the real estimate (5) by (10)--(11):

\[
\begin{aligned}
&\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3\\
&<
216\,2^{-\alpha_m}
3^{-2a_m+g_m-7\cdot2^m-7}.
\end{aligned}
\tag{18}
\]

Because

\[
Q_m^{-2}=3^{-2a_m+2g_m}
\]

and `g_m>=1`, the right side of (18) is at most

\[
72Q_m^{-2}3^{-7\cdot2^m},
\]

proving (12).

For (13), it is enough to show

\[
7\cdot2^m>{a_m-g_m\over512}.
\]

After multiplication by `512`, this follows from

\[
{1799\over2}2^m
>
1792m-g_m,
\]

which is already true at `m=12` and becomes stronger under `m -> m+1`.
This proves (13)--(14).

Finally, convergence of `P_m/Q_m` to `C_infinity>0` gives (16). Since the gap
between exponents `1/512` and `1/1024` is positive, the fixed factors `72` and
`K` are absorbed for all sufficiently large `m`, proving (17). ∎

## Conditional Ridout corollary

A standard form of Ridout's theorem says, roughly, that for an algebraic
irrational `alpha`, a finite set of places `S`, and any `epsilon>0`, there are
only finitely many reduced rationals `P/Q` satisfying

\[
\left|\alpha-{P\over Q}\right|
\prod_{p\in S}|P|_p|Q|_p
<
H(P,Q)^{-2-\epsilon}.
\tag{19}
\]

Once an exact source-qualified statement of this theorem is imported and its
normalization checked, (17) with `S={2,3}` would imply:

\[
\boxed{
C_\infty
\text{ is not algebraic irrational}.}
\tag{20}
\]

Thus the room would have to be rational or transcendental.

This corollary is **not yet promoted as an unconditional repository theorem**,
because the exact Ridout source and convention have not been added to the
literature branch. The native inequality (17) is independent of that missing
import.

## Why both places matter

The direct real approximation exponent is only slightly above one relative to
the denominator `3^(a_m)`. It does not approach the Roth threshold by itself.

The enormous power `2^(e_m)` in the numerator and the enormous power
`3^(a_m-g_m)` in the denominator contribute the two local factors in (10)--(11).
Their product raises the effective S-arithmetic exponent above two.

This is the first point in the packet where the fixed room, the binary stack,
and the ternary tower multiplier participate in one quantitative inequality.

## Gap audit

- The Ridout corollary awaits a verified imported theorem statement.
- Rational rooms are not excluded by this observation.
- Transcendental rooms are not excluded.
- The theorem does not produce a cap-stitch tail or a finite initialization.

## Adversarial tests

`X-0016` verifies the valuation bounds, reduced numerator/denominator formulas,
and the exact exponent inequality (13) over representative scales. The
conditional corollary is not treated as computational.