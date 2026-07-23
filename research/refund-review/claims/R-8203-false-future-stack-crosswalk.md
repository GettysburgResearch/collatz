# R-8203 — Plain mixed-radix digits are not the future legality stack

**Claim ID:** `R-8203`  
**Type:** refutation / scope boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Target:** PR #49 `T-8512` at head `210b1e204aa82947bab086b020bf2bd53805d84e`  
**Dependencies:** `L-8203`; frozen PR #49 `L-8507`  
**Scope:** the interpretation of the mixed-radix depth in `T-8512`  
**Related counterexample candidates:** none

## Refuted inference

`T-8512` defines the ordinary Euclidean expansion

\[
m_n=a_0+H_n(a_1+H_{n+1}(\cdots))
\]

and then states that its digits are the finite top-boundary data consumed by later connectors.

That crosswalk is false. The quantitative size comparison in `T-8512` may be retained as an ordinary **radix-capacity depth**, but the second and later Euclidean digits are not the later legality residues.

## Exact reason

One complete transition has

\[
\boxed{
m_n=\rho_n+H_n\ell_n,}
\tag{1}
\]

\[
\boxed{
m_{n+1}=\sigma_n+A_n\ell_n,}
\tag{2}
\]

where `A_n` is an odd multiplier and `sigma_n>=0`.

The first Euclidean digit in the expansion of `m_n` is indeed

\[
a_0=\rho_n,
\]

and its first quotient is

\[
a_1+H_{n+1}(\cdots)=\ell_n.
\]

Therefore

\[
\boxed{a_1\equiv\ell_n\pmod {H_{n+1}}.}
\tag{3}
\]

But the next exact cylinder condition is imposed on `m_(n+1)`, not on `ell_n`:

\[
\boxed{
\rho_{n+1}\equiv
\sigma_n+A_n\ell_n
\pmod {H_{n+1}}.}
\tag{4}
\]

Equations `(3)` and `(4)` agree only under the additional congruence

\[
(A_n-1)\ell_n+\sigma_n\equiv0\pmod {H_{n+1}},
\]

which is neither automatic nor generally true.

Thus ordinary Euclidean division of the current quotient does not commute with the intervening odd affine transport.

## Concrete intrinsic-core counterexample

Independently reconstruct the PR #49 two-block law at

```text
finite state:       (t,gamma,i)=(3744,1,0)
current block:      (j,nu)=(0,1)
next target:        k=0
chosen next lift:   1
following target:   0
```

Let `theta` be the residue of the current free lift `ell_n` that makes the following cylinder legal, and let `rho_next` be the actual next cylinder residue. Exact integer arithmetic gives

```text
theta mod64    = 45,
rho_next mod64 = 16.
```

Hence

\[
\boxed{
theta\ne\rho_{\rm next}.}
\tag{5}
\]

The second mixed-radix digit of `m_n` is `45 mod64`, while the actual next legality digit is `16 mod64`.

This is a concrete counterexample inside the claimed physical system, not an abstract toy model.

## Correct surviving theorem

The size calculation of `T-8512` proves:

```text
late top quotients exceed products of many future radix sizes.
```

Equivalently, the ordinary integer has large **radix capacity** when expanded in the chosen numerical radix sequence.

It does **not** prove:

```text
the expansion digits equal the future legal cylinder residues,
```

or that the current integer contains a causally readable legal stack without applying the intervening affine maps.

A corrected claim should therefore:

1. rename the quantity `radix-capacity depth`;
2. preserve the exact `1/288` and `1/233` size bounds;
3. remove the statement that the digits are exactly future legality data;
4. require a separate transducer/cocycle theorem to transport each digit through `m -> sigma+A ell`.

## Verdict

- `T-8512` numerical growth comparison: **PASSED**.
- `T-8512` future-stack interpretation: **REFUTED** by `(5)`.
- Overall claim: **SCOPE NARROWING REQUIRED**.

The original claim and proof history should be preserved. Any repaired physical-stack theorem should receive a fresh claim ID.

## Verification

`X-8203` independently reconstructs the displayed intrinsic transition and freezes the unequal residues `45` and `16 modulo 64`.
