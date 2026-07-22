# Session report — outlier bridge audit

**Agent:** `gpt56-outlier-01`
**Issue:** #52
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`
**Date:** 2026-07-23

## Starting hypothesis

A remote discipline might recognize the repository's ordinary-integer boundary or full-denominator equations in a form not visible from a standard Collatz literature search. The search was therefore directed away from parity vectors, generic p-adic dynamics, automata, `S`-units, and other topics already covered by issue #7.

## Repository sweep

Read and indexed:

- the complete project README;
- the open issue/PR registry through #51;
- cartography PR #38 pass 4;
- literature PR #13 wave 7 and its file inventory;
- the exact pulse equations in PR #47 and PR #51;
- the run-core and reset-highway equations in PR #51;
- PR #49's complement-counter target;
- the regular-sanctuary and H-map summaries relevant to finite-memory certificates.

The main branch is deliberately sparse; active mathematical state is branch-local. All status labels below preserve that fact.

## Approaches attempted

### 1. Sparse/toric elimination

Rewrote the arbitrary-support pulse correction as a chain Laurent polynomial and eliminated each pulse variable with a degree-one Sylvester determinant.

**Outcome:** new proposed theorem `L-8201`.

### 2. Non-Archimedean tropical noncancellation

Compared the 2-adic valuations of every monomial in the reduced resultant.

**Outcome:** one Collatz coefficient is the unique minimum, so every resultant is nonzero with an exact valuation. This supplies the uniform pulse caps.

### 3. Catastrophic convolutional coding

Translated “infinite directive produces finite-support ordinary boundary” into coding-theoretic catastrophicity.

**Outcome:** retained as a concrete format-level audit for bounded-memory linearized certificate classes. It does not directly cover the current nonlinear changing-modulus maps.

### 4. Primitive divisors in arithmetic dynamics

Tested whether a dynamical Zsigmondy theorem could supply PR #49's required stream of fresh odd primes.

**Outcome:** direct import rejected. Standard theorems require a fixed degree-at-least-two rational map; PR #49 is presently nonautonomous and affine. An autonomization lemma is the exact missing bridge.

### 5. 2-adic T-functions

Tested single-cycle residue criteria against the active deterministic partial maps.

**Outcome:** direct import rejected because the maps are partial and expanding, not global 1-Lipschitz self-maps. Possible future use is confined to an inverse address generator.

### 6. Homoclinic algebraic dynamics

Compared summable/decaying symbolic points with the ordinary-integer boundary.

**Outcome:** retained as a firewall. Homoclinic decay is not eventual zero support.

## New results

### `L-8201` — PROPOSED

For every fixed ordinary negative accelerated cycle word and every fixed nonempty pulse support:

- each pulse coordinate has an exact one-variable resultant;
- divisibility by the full cycle denominator is equivalent to divisibility by that resultant;
- its 2-adic valuation is exactly a baseline prefix valuation;
- it never vanishes;
- each pulse power `X_i=2^{d_i}` has an explicit support-dependent upper bound.

Corollary: the complete upward pulse cone over a fixed negative-cycle word is finite and exactly enumerable.

This extends PR #51's two-pulse all-size theorem to arbitrary finite support. It does not bound repetition length.

### `X-8201` — EMPIRICAL

Two independent standard-library implementations agree on:

```text
8,842 fixed-support packets
875,356 pulse instances
3,651,452 resultants
3,651,452 exact valuation certificates
5,856 PR #51 K/J specialization matches
```

The only five formal divisor hits are trivial `n=1` all-`2` words.

## Candidate counterexamples

None.

## Failed approaches and nonapplications

1. Primitive-divisor theorems do not apply to the current PR #49 map without autonomization and degree growth.
2. T-function ergodicity does not apply to the partial expanding forward charts.
3. Homoclinic or summable symbolic points do not meet the finite-support ordinary-integer criterion.
4. Convolutional-code tests cover linear bounded-memory certificate formats only; they cannot silently be applied to nonlinear quotient maps.

## Potential errors to review

1. The indexing in the right-hand chain form `H_i^+`.
2. The use of evenness of every left-chain coefficient in the unique-minimum valuation proof.
3. The support-wise cap's replacement of `R_i` by its lower bound `2^(e-1)`.
4. Reliance on the branch-qualified PR #47 pulse correction before independent repository review.
5. Whether another active branch has an equivalent arbitrary-support eliminant under different vocabulary; repository search found none, but no global novelty claim is made.

## Files changed

```text
research/outlier-bridges/README.md
research/outlier-bridges/OUTLIER_BRIDGE_AUDIT.md
research/outlier-bridges/SOURCE_LEDGER.md
research/outlier-bridges/claims/L-8201-fixed-pulse-cone-resultant-caps.md
experiments/X-8201-pulse-resultant-caps/README.md
experiments/X-8201-pulse-resultant-caps/run.py
experiments/X-8201-pulse-resultant-caps/verify.py
experiments/X-8201-pulse-resultant-caps/results/canonical.json
reports/gpt56-outlier-01/2026-07-23-52-outlier-bridge-audit.md
```

## Claims affected

- Adds `L-8201` (`PROPOSED`).
- Adds `X-8201` (`EMPIRICAL`).
- Strictly generalizes the algebraic cap interface of PR #51 `L-8001` from two pulses to arbitrary fixed support.
- Uses the arbitrary pulse correction of PR #47 `L-9602` as its branch-qualified input.

## Recommended next actions

1. Assign an independent agent to reconstruct `L-8201` without reading the experiment implementation first.
2. Integrate the bounds into one proof-producing all-support enumerator for each fixed repetition.
3. Attack the remaining repetition parameter using PR #47's macro-block commutator, `S`-unit finiteness, or an autonomized primitive-divisor sequence.
4. Apply the catastrophic-encoder test to the next bounded-memory linear boundary compiler proposed by PR #12 or a fixed macro family.

## Organizational improvement idea

Add an **outlier bridge rubric** to future literature work:

```text
REMOTE SOURCE OBJECT:
EXACT NATIVE OBJECT:
HYPOTHESES SATISFIED:
HYPOTHESES FAILED:
OUTPUT IF APPLICABLE:
FALSIFICATION TEST:
STATUS: theorem transfer / method / analogy / nonapplication
```

This preserves creativity while preventing distant-field analogies from being mistaken for imported theorems.
