# T-8201 — Uniform top-lift doubling in the intrinsic phase-34 decoder

**Claim ID:** `T-8201`  
**Title:** From connector height 5632, every coherent positive intrinsic top lift at least doubles  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8203`; frozen PR #49 finite-state bounds  
**Scope:** every coherent PR #49 intrinsic block path at heights divisible by `16`  
**Related counterexample candidates:** none

## Setup

Let the PR #49 intrinsic path have connector heights

\[
t_n=t_0+16n.
\]

At one two-block transition, use `L-8203` to write the current source high tail as

\[
m_n=\rho_n+2^{H_n}\ell_n,
\tag{1}
\]

and its next source high tail as

\[
m_{n+1}=\sigma_n+3^{G_n}\ell_n,
\tag{2}
\]

where

\[
H_n=11(t_n+33),
\tag{3}
\]

\[
G_n=7(t_n+1)+\gamma_n-\beta_{i_n},
\tag{4}
\]

\[
\sigma_n\ge0.
\tag{5}
\]

Coherence with one further block means

\[
m_{n+1}
=
\rho_{n+1}+2^{H_{n+1}}\ell_{n+1},
\tag{6}
\]

where

\[
0\le\rho_{n+1}<2^{H_{n+1}},
\qquad
H_{n+1}=11(t_n+49).
\tag{7}
\]

## Theorem

If

\[
16\mid t_n,
\qquad
t_n\ge5632,
\qquad
\ell_n\ge1,
\]

then

\[
\boxed{\ell_{n+1}\ge2\ell_n.}
\tag{8}
\]

Consequently, once one coherent ordinary path reaches height at least `5632` with positive top lift,

\[
\boxed{\ell_{n+r}\ge2^r\ell_n}
\qquad(r\ge0).
\tag{9}
\]

The threshold `5632` is the first multiple of `16` for which the following bound is uniform over all twelve finite states.

## Exact exponential certificate

The worst finite correction in `(4)` is

\[
\gamma_n-\beta_{i_n}\ge-2,
\]

so

\[
G_n\ge7t_n+5.
\tag{10}
\]

The exact integer inequality

\[
\boxed{3^{665}>2^{1054}}
\tag{11}
\]

gives

\[
3^{7t+5}>2^{11(t+49)+1}
\tag{12}
\]

whenever

\[
1054(7t+5)>665(11(t+49)+1).
\]

The difference is

\[
\boxed{63t-353830.}
\tag{13}
\]

At the adjacent multiples of sixteen,

\[
63\cdot5616-353830=-22,
\]

\[
63\cdot5632-353830=986.
\]

Direct integer comparison also gives

\[
3^{7\cdot5616+5}
<
2^{11(5616+49)+1},
\]

\[
3^{7\cdot5632+5}
>
2^{11(5632+49)+1}.
\]

Since increasing `t` by sixteen multiplies the left-to-right ratio in `(12)` by

\[
\frac{3^{112}}{2^{176}}
=
\left(\frac{3^7}{2^{11}}\right)^{16}
>1,
\]

the uniform bound persists at every later connector height.

Thus, for `t_n>=5632`,

\[
\boxed{3^{G_n}>2^{H_{n+1}+1}.}
\tag{14}
\]

## Proof of doubling

Subtract `(6)` from `(2)`:

\[
2^{H_{n+1}}\ell_{n+1}
=
\sigma_n+3^{G_n}\ell_n-\rho_{n+1}.
\tag{15}
\]

Using `(5)`, `(7)`, `(14)`, and `ell_n>=1`,

\[
\begin{aligned}
2^{H_{n+1}}\ell_{n+1}
&>
2^{H_{n+1}+1}\ell_n
-\left(2^{H_{n+1}}-1\right)\\
&=
(2\ell_n-1)2^{H_{n+1}}+1.
\end{aligned}
\]

The left side is an integral multiple of `2^(H_(n+1))`. Therefore

\[
\ell_{n+1}>2\ell_n-1,
\]

and integrality proves `(8)`.

## Significance

PR #49 already proves:

- every legal primitive core grows by more than 170 bits;
- every physical connector is exact;
- consecutive cores are coprime;
- and one forever-defined core is a Collatz counterexample.

This theorem adds the genuinely missing height statement at the **moving most-significant boundary**. Once the top lift is positive after height 5632, it cannot be exhausted by later cylinders; it doubles independently of every type choice.

The remaining obligation is therefore purely arithmetic:

```text
generate the required low residue at every step
from one finite ordinary core.
```

No separate drift, core-height, complement-counter, or top-capacity theorem remains.

## Gap audit

- The theorem is conditional on coherence; it does not prove the next residue congruence.
- It does not supply an initial core with `ell>=1`.
- A compatible `2`-adic path may satisfy all formal lift equations without being an ordinary integer.
- Uniform top-lift growth does not by itself make the decoder total.

## Verification

`X-8202` checks the exact threshold certificate, all twelve worst-state inequalities, the target-independent modulus in `L-8203`, and 384 independently reconstructed finite two-block laws.
