# R-9302 — Refutation of the naive complexity--carry comparison

**Claim ID:** R-9302  
**Title:** The matching criticality constants in repetition rigidity and phase-carry rigidity cannot be compared to obtain an ordinary-section contradiction  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9310`, `L-9311`; branch-qualified comparison with PR #20  
**Scope:** methodological closure for the proposed complexity--carry incompatibility theorem  
**Related counterexample candidates:** none

## Refuted proof schema

The following proposed argument is invalid:

1. PR #20 forces output factor-complexity slope at least
   \[
   \kappa=\frac1{\log_{64}81-1};
   \]
2. `L-9310` bounds long zero-carry behavior using the same `kappa`;
3. therefore an ordinary itinerary cannot satisfy both requirements.

The conclusion does not follow.

## Exact reason

`L-9311` proves that an exact repeated factor in an ordinary itinerary is itself an integral zero-carry chain for the difference of two ordinary tail orbits:

\[
64D_{i+1}=81D_i.
\]

The local repetition bound

\[
\ell
<
(\log_{64}81-1)(t-r)+\log_{64}A_r
\]

is therefore another completion-height bound for a zero-carry chain.

`L-9310` applies the same mechanism to the reciprocal-character chain. Its reciprocal constant is

\[
\kappa
=
\frac{\log64}{\log(81/64)}.
\]

The two constants agree because

\[
\frac1{\log_{64}81-1}
=
\frac{\log64}{\log(81/64)}.
\]

They are not opposing budgets. They are the same ratio read in two dual cocycles.

## Compatibility, not contradiction

The two conclusions point in compatible directions:

- repetition rigidity says a nontrivial ordinary itinerary must continually create new factors rather than sustain long zero-difference chains;
- phase-carry rigidity says a large Fourier coefficient would require too few nonzero reciprocal carries, so ordinary numerators accumulate phase energy.

A high-novelty itinerary can have many nonzero carries. Neither theorem supplies an upper bound on the other's novelty or carry count.

Thus no contradiction follows from the criticality constants alone, even though both theorems are individually strong.

## What a valid incompatibility theorem must add

A successful ordinary-section theorem must introduce one invariant coupling the two cocycles through the **same** itinerary. Viable exact candidates are:

1. the fixed-room past/future path of `T-9313`;
2. eventual stabilization of nested active-cylinder representatives from PR #20's `T-9409`;
3. a room-wrap block sequence whose zero tail forces a repeated ordinary orbit segment;
4. a return-word state in which symbolic novelty consumes a quantified amount of ordinary-height or cylinder precision that cannot be replenished.

Without such a coupling, comparing lower bounds is double-counting one completion-height principle.

## Dependency audit

- `L-9311` independently reconstructs the repetition bound as an orbit-difference zero-carry theorem.
- `L-9310` supplies the reciprocal-character zero-carry theorem.
- No PR #20 result is used as a premise of a mathematical conclusion on this branch; its statement is only crosswalk context.

## Gap audit

- This refutation concerns one proof route, not the existence of an ordinary survivor.
- It does not say that symbolic complexity is irrelevant. Complexity may become decisive after it is coupled to fixed-room or cylinder stabilization.
- It does not weaken `L-9310`, `T-9311`, or PR #20's repetition results.

## Process consequence

Future work should not advertise the equality of the two `kappa` constants as a contradiction. It should instead state the new coupling lemma that turns symbolic novelty into a fixed-room, sign, or stabilization obstruction.
