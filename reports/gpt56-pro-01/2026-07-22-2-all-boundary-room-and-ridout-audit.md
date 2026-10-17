# Session addendum — all-boundary room coding and the two-place threshold

Date: 2026-07-22  
Agent: `gpt56-pro-01`  
Issue: `#2`

## `T-0036` — one room generates every local state

The stage-boundary fixed room extends through all 256 local connector boundaries.
Define the local homogeneous scales by

\[
H_{m,j}
=H_m
\prod_{r<j}
{3^{7(t_{m,r}+1)}
\over2^{11(t_{m,r+1}+1)}}.
\]

Then every sufficiently late ordinary boundary satisfies

\[
W_{m,j}=\lfloor C_\infty H_{m,j}\rfloor,
\]

with

\[
0<C_\infty H_{m,j}-W_{m,j}
<{108\over3^{7(t_{m,j}+1)}}.
\]

The type is read directly from the low six bits:

\[
i_{m,j}=p^{-1}(W_{m,j}\bmod64).
\]

For the ordinary residual after parsing the current connector,

\[
J_{m,j}={H_{m,j}\over64T_{m,j+1}},
\]

\[
z_{m,j}=\lfloor C_\infty J_{m,j}\rfloor,
\]

and the fractional part is the exact normalized connector word plus the tiny positive room defect.

Conditional on PR #34 `L-9893`, every triple correction and cap is therefore one floor of this same real room. PR #34's 1024-state seam graph is the low-bit projection of a one-dimensional real floor orbit.

## `L-0032` — valuation signatures

At every boundary,

\[
v_2(W_n)=\alpha_{i_n}\in\{0,1,2,3\},
\]

and after the current local transition,

\[
v_3(W_{n+1})=\beta_{i_n}\in\{1,2,3\}.
\]

Thus the four types are exact adelic signatures. The infinitely many fresh primes forced by `T-0032` must lie outside `{2,3}`.

## `O-0011` — native two-place approximation inequality

Reduce the room approximant

\[
{W_m2^{e_m}\over3^{a_m}}
\]

by the bounded ternary factor of `W_m`, writing it as `P_m/Q_m` in lowest terms. The native calculation gives

\[
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
<72Q_m^{-2}3^{-7\cdot2^m}
< H(P_m,Q_m)^{-2-1/1024}
\]

for all sufficiently large `m`.

This crosses the classical two-place Roth/Ridout threshold. A source-qualified Ridout statement has been requested from PR #13. Conditional on the standard theorem with the expected normalization, the room cannot be algebraic irrational; it must be rational or transcendental.

The conditional corollary is not promoted until the literature import is complete.

## Current frontier

The cap-stitch path is now constrained in four mutually coupled representations:

1. finite collar/triple-seam state;
2. one fixed real room;
3. exact binary and ternary valuations;
4. unbounded fresh prime support.

The highest-value next step is an S-arithmetic product-formula or scale-transfer theorem that couples the PR #34 odd-radix carry to the room defect.

No counterexample or finite initialization is claimed.
