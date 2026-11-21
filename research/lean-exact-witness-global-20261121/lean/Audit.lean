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
