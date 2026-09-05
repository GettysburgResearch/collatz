# L-9874 — Dyadic boundary nonvanishing

Claim ID: `L-9874`  
Title: The two dyadic Newton-boundary families are nonzero at every order  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-d`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`, `L-9839`, `L-9848`  
Scope: `u=d-2,d-1` for dyadic `d`  
Related counterexample candidates: none

## Statement

At a primitive `2d`-th root with `d` a power of two,
`Q_(d-1)^(5)` and `Q_(d-2)^(5)` are nonzero.

## Definitions

See [the boundary proof](../proofs/period-four/dyadic-boundary-nonvanishing.md).

## Motivation

These are exactly the indices where the Newton target can meet the largest binary cluster.

## Proof or construction

The two cases reduce respectively to a folded quadratic mass and a signed
negacyclic coefficient equal to `+/-2d`.

## Dependency audit

Only the quotient definition and elementary root-of-unity pairing are used.

## Gap audit

No nonboundary dyadic index is covered.

## Adversarial tests

`X-9876` independently checks the identities through `d=64`.

## Remaining uncertainty

None within the two stated families; external review is pending.

## Suggested next attack

Prove the uniform transfer valuation of `L-9875`.

