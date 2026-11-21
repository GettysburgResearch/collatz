import CollatzGlobal

/-! Complete public-theorem axiom inspection for this checkpoint.
No open residual closure is assumed by this audit. -/

-- AdaptiveDescent.lean
#print axioms CollatzGlobal.hits_iff_orbit
#print axioms CollatzGlobal.oddCount_add
#print axioms CollatzGlobal.balanced_five_zero
#print axioms CollatzGlobal.balanced_five_append
#print axioms CollatzGlobal.lastReturn_le
#print axioms CollatzGlobal.lastReturn_balanced
#print axioms CollatzGlobal.lastReturn_maximal
#print axioms CollatzGlobal.residual_hits
#print axioms CollatzGlobal.residual_is_finite
#print axioms CollatzGlobal.finite_residual_last_zero
#print axioms CollatzGlobal.normalization_idempotent
#print axioms CollatzGlobal.even_balanced_one
#print axioms CollatzGlobal.finite_residual_odd
#print axioms CollatzGlobal.residual_five_basin
#print axioms CollatzGlobal.compile_residual_clock
#print axioms CollatzGlobal.return_decreases_certificate_clock
#print axioms CollatzGlobal.five_closure_iff_finite_residual
#print axioms CollatzGlobal.expanding_return_example
#print axioms CollatzGlobal.expanding_source_certificate
#print axioms CollatzGlobal.expanding_normal_form
#print axioms CollatzGlobal.rank_one_finite_residual
#print axioms CollatzGlobal.asynchronous_numerical_return

-- CommonRank.lean
#print axioms CollatzGlobal.rank_denominator_positive
#print axioms CollatzGlobal.rank_bernoulli
#print axioms CollatzGlobal.rank_sublevel_bounds
#print axioms CollatzGlobal.rank_sublevel_preserved
#print axioms CollatzGlobal.scaledRank_strict
#print axioms CollatzGlobal.scoreLT_accessible_on_sublevel
#print axioms CollatzGlobal.scoreLT_wellFounded
#print axioms CollatzGlobal.common_rank_induction

-- Coverage.lean
#print axioms CollatzGlobal.binary_source_first_hits
#print axioms CollatzGlobal.psi_source_first_hits
#print axioms CollatzGlobal.source_order_not_potential_order
#print axioms CollatzGlobal.rank_five_parameter_mod_four
#print axioms CollatzGlobal.rank_five_parameter_misses_negative_guard

-- Expansion.lean
#print axioms CollatzGlobal.orbit_zero
#print axioms CollatzGlobal.orbit_linear_lower
#print axioms CollatzGlobal.canonical_endpoint_bound
#print axioms CollatzGlobal.expanding_endpoint_not_one_mod

-- Forcing.lean
#print axioms CollatzGlobal.small_orbit_bound
#print axioms CollatzGlobal.basin_orbit_bounded
#print axioms CollatzGlobal.finite_basin_orbits_bounded
#print axioms CollatzGlobal.no_inverse_descent_cover
#print axioms CollatzGlobal.arbitrarily_large_inverse_minimal
#print axioms CollatzGlobal.basin_four_succ
#print axioms CollatzGlobal.certified_lift
#print axioms CollatzGlobal.certified_units_unbounded
#print axioms CollatzGlobal.certified_units_inverse_minimal
#print axioms CollatzGlobal.expansion_depth_for_endpoint_lift
#print axioms CollatzGlobal.bounded_expansion_misses_lift

-- OrbitLift.lean
#print axioms CollatzGlobal.orbit_basin
#print axioms CollatzGlobal.orbit_add
#print axioms CollatzGlobal.shortcut_add_even
#print axioms CollatzGlobal.high_bit_lift
#print axioms CollatzGlobal.basin_high_bit_lift
#print axioms CollatzGlobal.balanced_five_lift
#print axioms CollatzGlobal.five_failure_return
#print axioms CollatzGlobal.five_failure_cylinder

-- PsiCoverage.lean
#print axioms CollatzGlobal.ordinary_odd_rise
#print axioms CollatzGlobal.ordinary_power_two_orbit
#print axioms CollatzGlobal.ordinary_odd_rise_partial
#print axioms CollatzGlobal.singular_psi_prefixes
#print axioms CollatzGlobal.singular_psi_residual
#print axioms CollatzGlobal.rank_five_psi_residual
#print axioms CollatzGlobal.hard_parameter_equation
#print axioms CollatzGlobal.hard_parameter_large
#print axioms CollatzGlobal.hard_psi_family

-- PsiExpansion.lean
#print axioms CollatzGlobal.psi_expanding_seed
#print axioms CollatzGlobal.psi_expanding_source_certificate
#print axioms CollatzGlobal.psi_expanding_family
#print axioms CollatzGlobal.psi_expanding_family_increases
#print axioms CollatzGlobal.psi_expanding_family_guard
#print axioms CollatzGlobal.psi_expanding_family_unit
#print axioms CollatzGlobal.psi_expanding_family_target
#print axioms CollatzGlobal.psi_expanding_family_source
#print axioms CollatzGlobal.psi_expanding_family_rank
#print axioms CollatzGlobal.psi_expanding_seed_child_certificate
#print axioms CollatzGlobal.psi_expanding_seed_rank

-- PsiNormalization.lean
#print axioms CollatzGlobal.shortcut_positive
#print axioms CollatzGlobal.orbit_positive
#print axioms CollatzGlobal.shortcut_unit
#print axioms CollatzGlobal.orbit_unit
#print axioms CollatzGlobal.psi_return_zero
#print axioms CollatzGlobal.psi_return_append
#print axioms CollatzGlobal.lastPsiReturn_le
#print axioms CollatzGlobal.lastPsiReturn_returns
#print axioms CollatzGlobal.lastPsiReturn_maximal
#print axioms CollatzGlobal.psi_residual_positive
#print axioms CollatzGlobal.psi_residual_hits
#print axioms CollatzGlobal.psi_residual_is_finite
#print axioms CollatzGlobal.psi_residual_basin
#print axioms CollatzGlobal.compile_psi_residual_clock
#print axioms CollatzGlobal.lastPsiReturn_before_hit
#print axioms CollatzGlobal.collatz_iff_finite_psi_residual
#print axioms CollatzGlobal.psi_first_layer_residual
#print axioms CollatzGlobal.jacobsthal_three_power_smaller
#print axioms CollatzGlobal.jacobsthal_closed_under_ordinary_floor

-- PsiTemplateBridge.lean
#print axioms CollatzGlobal.binary_upper_psi_prefix
#print axioms CollatzGlobal.binary_lower_psi_prefix
#print axioms CollatzGlobal.conjugate_binary_source_clock
#print axioms CollatzGlobal.conjugate_binary_target

-- RankMoves.lean
#print axioms CollatzGlobal.scoreLT_forward_guard
#print axioms CollatzGlobal.scoreLT_height_clock_guard
#print axioms CollatzGlobal.expanding_return_rank_guard
#print axioms CollatzGlobal.expanding_return_decreases_common_rank
#print axioms CollatzGlobal.negative_template_clock_guards
#print axioms CollatzGlobal.psi_template_common_rank
#print axioms CollatzGlobal.psi_template_height_guards
#print axioms CollatzGlobal.psi_return_common_rank

-- Retraction.lean
#print axioms CollatzGlobal.balanced_five_suffix_iff
#print axioms CollatzGlobal.lastReturn_of_residual_endpoint
#print axioms CollatzGlobal.normalize_inverse_extension
#print axioms CollatzGlobal.no_rank_decrease_both_ways
#print axioms CollatzGlobal.wellFounded_no_two_cycle
#print axioms CollatzGlobal.no_wellFounded_rank_both_ways

-- UnboundedLadder.lean
#print axioms CollatzGlobal.two_step_four
#print axioms CollatzGlobal.four_ladder
#print axioms CollatzGlobal.four_step_five
#print axioms CollatzGlobal.five_four_ladder
#print axioms CollatzGlobal.ladder_last_four
#print axioms CollatzGlobal.unbounded_ladder_balanced
#print axioms CollatzGlobal.unbounded_ladder_failure
#print axioms CollatzGlobal.ladder_endpoint_smaller
#print axioms CollatzGlobal.ladder_endpoint_positive
#print axioms CollatzGlobal.ladder_guard_parametrized
#print axioms CollatzGlobal.unbounded_ladder_descent
#print axioms CollatzGlobal.one_rung_balanced
#print axioms CollatzGlobal.one_rung_failure

-- Imported global interface and exact remaining hypotheses.
#print axioms CollatzClosure.collatz_of_open_lemma
#check CollatzGlobal.collatz_iff_finite_psi_residual
#print CollatzGlobal.ResidualPsiClosure
#check CollatzGlobal.common_rank_induction
#check CollatzGlobal.hard_psi_family
#check CollatzGlobal.psi_expanding_family_source
#check CollatzGlobal.psi_expanding_family_rank
