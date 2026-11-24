# Correspondence review of eight inherited Lean modules

**Verdict: VERIFIED for source correspondence.** All 62 public proposition headers preserve their upstream names, binder order, explicit/implicit binder forms, hypotheses and conclusions. The same check passed on all four private theorem headers. All fourteen auxiliary definitions preserve their type and body. This verdict concerns those eight sources at the hashes in [PROVENANCE.md](../../../research/astra-global-closure-20261124/formal/PROVENANCE.md).

## Reconstruction

I resolved each of the eight filenames against the applicable frozen Git tree. Each had exactly one matching full path at its assigned commit. I compared git show COMMIT:PATH byte for byte with the previously staged upstream snapshot, then computed SHA-256 for the upstream and packet files independently. Every upstream pair matched. I stripped comments, normalized whitespace and the notation ℕ versus Nat, and compared ordered declaration headers through their proof delimiter. For definitions I compared the complete textual declaration including its defining equations. I also checked the ordered namespace, section and variable declarations; in particular the implicit commutative-ring parameters in ResidueDefect survive. I separately read the proof diffs so these normalizations could not hide a change in assumptions. Every packet module explicitly disables autoImplicit.

| Module | Public | Private | Definitions | Public theorem bodies changed |
|---|---:|---:|---:|---|
| PhasePacking.lean | 8 | 0 | 0 | normalized_edge, cubic_height |
| RepetitionWindow.lean | 11 | 0 | 5 | None |
| RepeatObstruction.lean | 6 | 2 | 1 | None |
| CarryCocycle.lean | 4 | 2 | 1 | carry_power |
| ResidueDefect.lean | 6 | 0 | 1 | None |
| CarryBudget.lean | 6 | 0 | 1 | None |
| MahlerCore.lean | 8 | 0 | 5 | None |
| TwoSidedPacking.lean | 13 | 0 | 0 | None |

## The two kinds of repair

1. **Positive-factor cancellation in #182.** The upstream proofs of normalized_edge and cubic_height call mul_le_mul_right₀. The pinned Mathlib declares mul_le_mul_iff_left₀ for b·a ≤ c·a if and only if b ≤ c when a is strictly positive. The inherited chains already place that factor on the right. Both original positive-factor facts, hdc and hu, are retained. The two normalized_edge calc lines drop a redundant ring step after field_simp has closed the goal. In cubic_height the proof uses the existing hypothesis 1≤y to derive 0≤y and then 0≤y^2 by pow_nonneg; this discharges the same sign fact originally obtained from sq_nonneg y. No inequality, sign premise or comparison domain changed. Two intermediate spellings also failed: mul_le_mul_right is a monotonicity function, and mul_le_mul_iff_right₀ places the common factor on the left. Neither intermediate run counts as a pass.
2. **Warnings as errors in #188.** The private fourth_bound has one sequence and public carry_power has two sequences where the first tactic leaves only one goal. Replacing all-goals sequencing with direct sequencing removes the unnecessarySeqFocus warnings. The same tactics act on the same resulting mathematical goals.
3. **Import narrowing.** The first narrow environment lacked finite-sum notation, field_simp and the natural-number coprime divisibility lemmas used by PhasePacking and RepetitionWindow. Restoring the relevant imports resolves missing names or syntax in the adaptation; those errors do not demonstrate a flaw in the original mathematical statements. The runs of the byte-identical umbrella-import versions for CarryCocycle and MahlerCore with a 180-second time budget timed out, so they supply no result about elaboration of those untouched upstream files. The successful or failed adapted replays must be attributed to their exact source hashes.

## Printed names and evidence limits

For each packet module the printed names occur exactly once and match all its public theorems in declaration order. The following groups are an independent inventory from the pinned sources.

- PhasePacking.lean — clock_carry_identity, normalized_complete, normalized_edge, cubic_height, canonical_difference, canonical_prefix, returning_bound, past_endpoint_unique.
- RepetitionWindow.lean — wordDen_succ, aligned, difference_dvd, small_shared_word, edge_height, prefix_height, two_start_bounds, early_repeat, edge_deterministic, equal_start_future, four_window_reject.
- RepeatObstruction.lean — eq_zero_of_multiple_small, shared_lp_divisibility, shared_lp_eq_of_small, clock_ge, shared_gap_full_divisibility, shared_gap_eq_of_height.
- CarryCocycle.lean — carry_power, clock_step, clock_amortized, clock_amortized_shift.
- ResidueDefect.lean — geom_mul, balanced_unit, exponent_transport, cycle_term, balanced_numerator_inverse, single_interval_defect.
- CarryBudget.lean — prefixSum_congr, prefixSum_ge_length, carry_telescope, carry_budget, carry_word_determined, no_carry_birth.
- MahlerCore.lean — telescope, weight_append, oneSum_append, weight_substitute, oneSum_substitute, finite_mahler, affine_expand, eliminate_zero.
- TwoSidedPacking.lean — cycle_spread_bound, lattice_step, spaced_span, denominator_packing_core, composed_carry_difference, shadow_L, shadow_P, shadow_smaller_odd, shadow_exists, shifted83_L, shifted83_P, shadow_first_gap, bezout_torus.

The [strict execution receipt](../formal/final-replay.json) and its individual logs establish compiler outcomes. Source comparison alone cannot certify elaboration. An axiom report is conclusive here only with exit code zero, an unchanged source hash, the complete expected name set, and no admissions or unapproved axioms. Earlier failed transcripts may display sorryAx after Lean recovers from an error. Those runs cannot be promoted to successful checks. The eight modules concern finite carry algebra, same-source repeat/height constraints, ring identities, affine words and conditional packing inequalities. They do not implement #190’s transcendence proof, a universal cycle denominator exclusion, or an all-source convergence theorem.

Independent readback of the complete final receipt shows eight successful strict processes and 62 individual public theorem axiom reports. I matched each report name to the upstream inventory above, recomputed all eight source and eight compiler-log hashes, and checked that the source did not change during each invocation. The receipt records only propext, Classical.choice and Quot.sound across those declarations. The SHA-256 of the completed final-replay.json is c81a25e6edd81772f05e2cdd210aeee95840fbf58133f00e8d99f6e56c7af100. This verification inspected the compiler output from the integrating process; it did not rebuild the upstream files or rerun the compiler independently.
