# L-9868 — Two-level period-four quotient blocks and carry states

Claim ID: `L-9868`  
Title: The period-four quotient has an exact two-level block decomposition with finite q-Lucas residuals and a strict prime-power carry gap  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`, with independent algebra/checker lanes  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9816`; finite q-binomial theorem and q-Lucas  
Scope: the positive period-four quotient `Q_u^(5)`  
Related counterexample candidates: none

## Statement

The quotient admits an exact decomposition

\[
Q_u^{(5)}=\sum_{b=0}^uD_{u,b}F_{u-b,b},
\]

with explicit factorial block `D` and Rogers--Szego residual `F`. At a
primitive `m`-th root, `F_(Am+R,b)=2^A F_(R,b)`, while the exact local
`p`-adic order of `D` is a five-term `W_p` carry expression. For the least
`p^k>2u+1`, its distinguished `m=1` value satisfies
`2V_0+1<phi(p^k)`.

## Definitions

All notation and formulas are given in the two proof appendices linked below.

## Motivation

This replaces one global cyclotomic cancellation problem by carry valuations
and finite residual states, and is the common prerequisite for `L-9869`--`L-9875`.

## Proof or construction

See [the block/q-Lucas proof](../proofs/period-four/q5-block-lucas-residual.md)
and [the carry-gap proof](../proofs/period-four/odd-prime-power-carry-gap.md).

## Dependency audit

The quotient definition comes from the Padé sector of `L-9816`; every new
block identity and carry formula is proved in the appendices.

## Gap audit

This claim does not bound cancellation among equal-order blocks and does not
classify every residual zero.

## Adversarial tests

`X-9876` checks the block identity, q-Lucas reductions, residual symmetry,
and 45,688 carry-gap cases.

## Remaining uncertainty

None within the scoped identities; their applications require the later
cancellation claims.

## Suggested next attack

Use the exact states in odd, composite, and dyadic characteristic separately.

