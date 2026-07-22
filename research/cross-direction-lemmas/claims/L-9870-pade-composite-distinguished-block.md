# L-9870 — Carry-optimal composite distinguished block

Claim ID: `L-9870`  
Title: Every composite residual half has a distinguished block preserving the strict prime-power carry gap  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-c`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`  
Scope: `p` not dividing the residual root order `m`  
Related counterexample candidates: none

## Statement

For `u=mB+r`, choose `b_*=0` in the lower residual half and
`b_*=floor(m/2)` in the upper half. Then its valuation is the same carry-only
deficit as the `m=1` state and satisfies `2V_*+1<phi(p^a)` whenever
`mp^a>2u+1`.

## Definitions

See [the proof appendix](../proofs/period-four/composite-distinguished-block.md).

## Motivation

It supplies the correct valuation budget for composite cyclotomic descent.

## Proof or construction

The appendix proves the floor identities, q-Lucas residual, and strict gap.

## Dependency audit

Uses only `L-9868` carry notation and elementary floor arithmetic.

## Gap audit

Residual nonvanishing is not asserted; two antisymmetric states can cancel.

## Adversarial tests

`X-9876` checks 148,289 exact states.

## Remaining uncertainty

Multiplicity control requires `L-9871`--`L-9873` and further noncancellation.

## Suggested next attack

Classify residual jets at the distinguished state.

