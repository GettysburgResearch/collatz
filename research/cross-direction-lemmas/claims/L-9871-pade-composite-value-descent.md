# L-9871 — Exact composite value descent

Claim ID: `L-9871`  
Title: Composite root values descend to one or two residual channels  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-c`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`; `L-9870` for the carry-gap application  
Scope: value jet modulo `Phi_m`, for every quotient index  
Related counterexample candidates: none

## Statement

For `u=Am+r`, the upper residual value is `Q_A(1)Q_r(zeta)`; the lower
residual value is an explicit two-channel combination of `Q_r(zeta)` and
`Q_(m+r)(zeta)`. These are full `Phi_m` congruences and therefore exact
full-factor criteria modulo every odd `p` not dividing `m`.

## Definitions

See [the value-descent proof](../proofs/period-four/composite-value-descent.md).

## Motivation

This is the first exact quotient-digit descent for genuinely composite order.

## Proof or construction

The proof classifies every zero-order two-level block and sums the remaining
q-Lucas channels.

## Dependency audit

Imports the decomposition of `L-9868`; all channel sums are derived locally.

## Gap audit

This is a value theorem, not a higher-multiplicity theorem.

## Adversarial tests

`X-9876` passes 216 congruences, 704 finite-field reductions, and the carry audit.

## Remaining uncertainty

Positive value multiplicity can still be strictly below the required threshold.

## Suggested next attack

Use the derivative descent in `L-9872`.

