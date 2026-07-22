# L-9875 — Dyadic Cartier product and scalar kernel

Claim ID: `L-9875`  
Title: The characteristic-two quotient splits into a solved scalar kernel and one type-C transfer state  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-d`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`, `L-9874`  
Scope: characteristic-two identities and scalar valuation; transfer target remains open  
Related counterexample candidates: none

## Statement

The centered numerator has an exact type-C product. Its scalar kernel
`K_(M,a;b)` has `ord_(s=1) K=M` for every even `a` and integer `b`.
Exact one-parameter transfer recurrences, Dickson individual factor orders,
and binary-cluster arithmetic follow.

## Definitions

See [the Cartier/kernel proof](../proofs/period-four/dyadic-cartier-kernel.md).

## Motivation

This reduces the remaining mod-two problem to one explicit transfer valuation.

## Proof or construction

The appendix proves the centered product, elementary/scalar separation,
binary-interaction kernel theorem, transfer recurrences, and cluster formulas.

## Dependency audit

Uses the quotient numerator of `L-9868`; `L-9874` handles the two boundary indices.

## Gap audit

The uniform transfer valuation, monomial-shadow symmetric valuation, and
mod-four lift are explicitly conjectural/open and are not part of this claim.

## Adversarial tests

`X-9876` checks exact Cartier identities through `u=8`, 820 kernel states
through `M=40`, and binary-cluster formulas through 100,000 inputs.

## Remaining uncertainty

The tied transfer case `u=2r`, `r` odd, is the precise obstruction.

## Suggested next attack

Prove the exceptional divided-difference cancellation, then lift one level modulo four.

