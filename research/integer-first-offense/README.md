# Integer-first counterexample offense

**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`

## Acceptance standard

A positive result must provide one ordinary positive integer and prove, with exact standard-map replay, either:

1. a nontrivial positive cycle; or
2. an infinite orbit that never reaches `1`.

The following are not candidates:

- a long finite prefix;
- a compatible inverse limit in `Z_2`;
- a real shadow;
- approximate divisibility;
- a control-map orbit without an exact `3x+1` embedding.

## Current attack

The first lane is proof-producing compressed cycle synthesis. Known negative Collatz cycles have multipliers just above one before their total dyadic division. A natural perturbative construction is to repeat one negative-cycle valuation block and insert extra division at one location so the full cycle denominator becomes positive.

`L-9601` shows that every such single-pulse candidate reduces to

\[
2^{Ar+\delta}-3^{kr}
\mid
(2^\delta-1)(3z+1),
\]

where `z` is one of the finitely many rotated negative-cycle states. This collapses an apparently huge positional search to a small exact divisibility test.

`X-9601` checks the negative three- and eleven-cycle families through `20,000` repeated blocks and finds only the trivial `n=1` cycle.

## Active successor

The next positive-cycle construction must use distributed pulses or more than one primitive block. The intended next exact interface is a meet-in-the-middle product of upper-triangular affine monoids, with every hit passed to the tiny independent replay boundary used by issue #9.

In parallel, cross-cycle ordinary-spine work is shared with issue #39. A permanent phase-1 tail is explicitly recognized as the shifted original Collatz map, not as an additional amplifier.

## Status

No unconditional Collatz counterexample has been found. Every finite negative packet will be shared with the corresponding collaborator rather than kept private.
