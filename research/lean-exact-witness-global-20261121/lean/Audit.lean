import Collatz

#check CollatzWitness.e_iff_odd_basin
#check CollatzWitness.original_iff_collatz
#print axioms CollatzWitness.certificate_witness
#print axioms CollatzWitness.witness_certificate
#print axioms CollatzWitness.schedule_exists
#print axioms CollatzWitness.e_iff_odd_basin
#print axioms CollatzWitness.original_iff_collatz
#check CollatzPsiCompletion.normalize_adjacent_below
#check CollatzPsiCompletion.initial_basin_even_tail
#print axioms CollatzPsiCompletion.normalize_adjacent_below
#print axioms CollatzPsiCompletion.adjacent_even_tail
#print axioms CollatzPsiCompletion.adjacent_odd_tail
#print axioms CollatzPsiCompletion.initial_basin_even_tail
#print axioms CollatzPsiCompletion.least_missing_adjacent
#check CollatzResetFamily.reset_family
#print axioms CollatzResetFamily.reset_family
#print axioms CollatzResetFamily.reset_amplification

-- Keep the actual remaining universal statement visible in audit output.
#print CollatzClosure.OpenLemma

#check CollatzDirected.collatz_of_complete_deep
#print axioms CollatzDirected.oddCore_upper_bound
#print axioms CollatzDirected.certificate_sound
#print axioms CollatzDirected.collatz_of_complete_deep
#check CollatzWitnessEnergy.prefixEnergy_dominated_lt
#print axioms CollatzWitnessEnergy.prefixEnergy_replacement_lt_with_suffix
#print axioms CollatzWitnessEnergy.prefixEnergy_cancelled_replacement_lt
#check CollatzSourceWitness.clock_replacement
#check CollatzSourceWitness.energy_replacement
#print axioms CollatzSourceWitness.trace_peel
#print axioms CollatzSourceWitness.clock_replacement
#print axioms CollatzSourceWitness.energy_replacement
#print axioms CollatzSourceWitness.collatz_of_clock_complete
#print axioms CollatzSourceWitness.collatz_of_energy_complete
-- These coverage obligations remain unproved in the current search packet.
#print CollatzDirected.Complete
#print CollatzSourceWitness.ClockComplete
#print CollatzSourceWitness.EnergyComplete

-- Unrestricted source-gap multisets and complete-certificate rewrites.
#print axioms CollatzGapMultiset.less_wellFounded
#print axioms CollatzGapMultiset.cancelled_replacement
#print axioms CollatzGapMultiset.unbounded_high_gap_replacement
#print axioms CollatzGapMultiset.ordinary_step
#print axioms CollatzGapMultiset.collatz_of_complete
#print axioms CollatzHighGapPump.prefix_basin
#print axioms CollatzHighGapPump.whole_witness_rewrite
#print axioms CollatzHighGapPump.rewritten_sizes
#print axioms CollatzHighGapPump.exponential_expansion
#print axioms CollatzHighGapPump.fixed_base_prefix_failure
#print axioms CollatzLowGapLoops.whole_witness_rewrite
#print axioms CollatzLowGapLoops.apply_reverse_rule
#print axioms CollatzUnboundedGapReset.compiled_certificate_reset
#print axioms CollatzUnboundedGapReset.low_depth_zero_reset
#print axioms CollatzGapComparison.close
#print axioms CollatzGapComparison.collatz_of_complete_psi
#print axioms CollatzGapComparison.collatz_of_complete_deep
#print axioms CollatzGapComparison.high_gap_rule
#print axioms CollatzGapComparison.low_gap_rule
#print axioms CollatzGapComparison.ordinary_source
#print axioms CollatzGapComparison.compiled_reset_rule
-- These are hypotheses of the closing theorems, not established selectors.
#print CollatzGapMultiset.Complete
#print CollatzGapComparison.Complete
