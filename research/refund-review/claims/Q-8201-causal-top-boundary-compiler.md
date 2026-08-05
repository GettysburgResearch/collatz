# Q-8201 — Causal top-boundary compiler

**Claim ID:** `Q-8201`  
**Status:** `IDEA / PRIMARY CONSTRUCTIVE TARGET`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-22

## Question

Construct one explicit finite positive quotient at a stage base `B_0>=955024` and a causal rule which, from the current finite ordinary state only,

1. emits the next 256 tower types;
2. proves every local connector integral;
3. proves canonical most-significant carry flush;
4. keeps the lift parameter `k_n>=1`; and
5. returns a new state to the same invariant class.

By `L-8201`, items 1--5 automatically force unbounded quotient and physical boundary growth.

## Required certificate state

A viable proof object should carry at least

```text
stage base B,
physical tower type,
current ordinary quotient,
current residue address,
bounded local carry state,
most-significant boundary/length,
proof hash for the emitted stage word.
```

## Newly closed subarchitecture

Live PR #34 `L-9915` proves that finite control plus one **additively updated** counter, observed only through zero and finitely many fixed residues, emits an ultimately periodic word even when the counter has positive drift. Combined with the centered lasso firewall, that restricted architecture cannot close this target.

Therefore a viable `Q-8201` machine must use at least one genuinely unbounded operation or observation outside that theorem, such as:

- exact quotient magnitude or most-significant digit;
- a modulus changing with the stage base;
- multiplication/division with exact unbounded remainder;
- a nonlinear arithmetic update;
- or more than one independent unbounded register.

This is not permission to preload future digits: the top-boundary operation must remain causal.

## Promising coupling

PR #3 contains an ordinary quadratic/formal-group bulk generator capable of producing new low bits causally. The exact next experiment should not merely count its bit surplus. It should express the word-pair residue `y_0(v)` as a certified affine or polynomial functional of that bulk and prove the same finite integer supplies the subsequent top boundary.

## Acceptance gate

A positive result requires:

- one written integer `Y_0` and corresponding physical initialization;
- an all-time inductive invariant;
- exact local replay rather than stage-only congruence;
- positivity and `k_n>=1`;
- independent verification.

A `Z_2` limit, modular cycle, finite prefix, ultimately periodic additive-counter output, or arbitrary future-digit oracle is not a solution.
