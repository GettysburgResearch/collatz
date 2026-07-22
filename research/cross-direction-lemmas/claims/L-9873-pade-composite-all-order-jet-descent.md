# L-9873 — Candidate all-order composite jet descent

Claim ID: `L-9873`  
Title: Normalized composite jets have bounded quotient-digit degree and integral finite-channel interpolation  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-c`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`; low jets agree with `L-9871`, `L-9872`  
Scope: candidate arbitrary Hasse-jet descent modulo powers of `Phi_m`  
Related counterexample candidates: none

## Statement

With `S_A=2^A binom(2A,A)`, the normalized `j`-jet of `Q_(Am+r)` at a
primitive `m`-root is claimed to be polynomial in `A` of degree at most
`2j+1`. Newton interpolation then gives an integral `2J+2`-channel
congruence modulo `Phi_m^(J+1)`.

## Definitions

See [the all-order proof checkpoint](../proofs/period-four/composite-all-order-jet-descent.md).

## Motivation

It replaces the false one-channel product lift by a finite residual system at every order.

## Proof or construction

Interpolation and coefficient integrality are complete. The period-product
degree lemma is proved in outline in Section 5 of the appendix.

## Dependency audit

Uses the exact block decomposition of `L-9868`; its value and first-jet
specializations recover `L-9871` and `L-9872`.

## Gap audit

External review must expand the arbitrary-order period-product normalization,
borrowed-state, binomial-moment, and small-`A` extension arguments. The finite
checker through `Phi_m^3` is not a proof of that universal lemma.

## Adversarial tests

`X-9876` passes 176,851 integrality cases, 218 lift instances through
`Phi_m^3`, both defect recurrences, and an exact counterexample to the naive product lift.

## Remaining uncertainty

The universal degree lemma is the explicit proof-completeness boundary.

## Suggested next attack

Formalize that lemma, then build the central-carry residual jet automaton.

