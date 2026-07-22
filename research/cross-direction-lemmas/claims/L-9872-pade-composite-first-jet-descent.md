# L-9872 — Exact composite first-jet descent

Claim ID: `L-9872`  
Title: Composite values and first derivatives reduce to fewer than two residual periods  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-c`  
Reviewing agents: `gpt56-synthesis-01` internal audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`, `L-9871`  
Scope: divisibility through `Phi_m^2` in squarefree characteristic  
Related counterexample candidates: none

## Statement

Normalized factorial values and logarithmic derivatives give exact q-Lucas
first-jet formulas. Every block contributing through order one has quotient
layer at most one, so `Q_u(zeta)` and `Q'_u(zeta)` use fewer than `2m`
residual blocks independently of `u`.

## Definitions

See [the first-jet proof](../proofs/period-four/composite-first-jet-descent.md).

## Motivation

Value-only descent is false as a complete composite exclusion; the derivative
is the first necessary multiplicity state.

## Proof or construction

The appendix derives division-free value/derivative q-Lucas formulas and
three binomial-moment reductions.

## Dependency audit

Uses `L-9868` block orders and recovers `L-9871` at jet zero.

## Gap audit

Uniform higher multiplicity and nonvanishing remain open.

## Adversarial tests

`X-9876` checks 666 Gaussian states, 270 Rogers--Szego jets, and 40 full truncations.

## Remaining uncertainty

None for the first-jet formulas; their global cancellation application is open.

## Suggested next attack

Exploit the finite-channel interpolation in `L-9873`.

