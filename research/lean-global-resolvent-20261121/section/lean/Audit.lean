import BandCriterion
import SectionTransport

/-! Axiom audit of every public theorem in the new section modules. -/

-- BandSteering
#print axioms CollatzShell.ForwardSection.Band.goodScale_cofinal
#print axioms CollatzShell.ForwardSection.Band.inverse_grid
#print axioms CollatzShell.ForwardSection.Band.log_error
#print axioms CollatzShell.ForwardSection.Band.lift_ge
#print axioms CollatzShell.ForwardSection.Band.lift_upper
#print axioms CollatzShell.ForwardSection.Band.lift_phase
#print axioms CollatzShell.ForwardSection.Band.scale_error
#print axioms CollatzShell.ForwardSection.Band.steered_root_with_clock
#print axioms CollatzShell.ForwardSection.Band.steered_root

-- CountCriterion
#print axioms CollatzShell.ForwardSection.Band.HitBy.mono
#print axioms CollatzShell.ForwardSection.Band.hitBy_step
#print axioms CollatzShell.ForwardSection.Band.hitBy_at_hit
#print axioms CollatzShell.ForwardSection.Band.nohit_iff_not_hitBy
#print axioms CollatzShell.ForwardSection.Band.mem_sectionSurvivors
#print axioms CollatzShell.ForwardSection.Band.sectionSurvivors_mono
#print axioms CollatzShell.ForwardSection.Band.recover_unit_from_section_count
#print axioms CollatzShell.ForwardSection.Band.recover_unit_finite
#print axioms CollatzShell.ForwardSection.Band.section_count_certifies_small_units
#print axioms CollatzShell.ForwardSection.Band.counterexample_section_population
#print axioms CollatzShell.ForwardSection.Band.empty_section_survivors
#print axioms CollatzShell.ForwardSection.Band.collatz_iff_unbounded_section_counts

-- PopulationTransfer
#print axioms CollatzShell.ForwardSection.Band.BoundedSectionFan.toSectionFan
#print axioms CollatzShell.ForwardSection.Band.mem_markedProperty
#print axioms CollatzShell.ForwardSection.Band.component_population_transfer
#print axioms CollatzShell.ForwardSection.Band.survivor_population_transfer
#print axioms CollatzShell.ForwardSection.Band.finite_survivor_population_transfer
#print axioms CollatzShell.ForwardSection.Band.mem_smallUnitSurvivors
#print axioms CollatzShell.ForwardSection.Band.finite_survivor_population_bound

-- BandCriterion
#print axioms CollatzShell.ForwardSection.Band.marked_ancestors_with_clocks
#print axioms CollatzShell.ForwardSection.Band.marked_ancestors
#print axioms CollatzShell.ForwardSection.Band.band_count_finite_certificate
#print axioms CollatzShell.ForwardSection.Band.collatz_iff_band_survivor_count
#print axioms CollatzShell.ForwardSection.Band.band_component_population
#print axioms CollatzShell.ForwardSection.Band.band_survivor_population
#print axioms CollatzShell.ForwardSection.Band.band_finite_survivor_population

-- FanGeometry
#print axioms CollatzShell.ForwardSection.bareChild_spec
#print axioms CollatzShell.ForwardSection.oddFan_spec
#print axioms CollatzShell.ForwardSection.oddFan_clock
#print axioms CollatzShell.ForwardSection.oddFan_hit
#print axioms CollatzShell.ForwardSection.fan_strict_octave
#print axioms CollatzShell.ForwardSection.oddFan_injective
#print axioms CollatzShell.ForwardSection.oddFan_le_raw
#print axioms CollatzShell.ForwardSection.oddFan_upper
#print axioms CollatzShell.ForwardSection.fan_lower
#print axioms CollatzShell.ForwardSection.oddFan_lower
#print axioms CollatzShell.ForwardSection.oddFan_phase
#print axioms CollatzShell.ForwardSection.sixteen_mul_le_pow_two
#print axioms CollatzShell.ForwardSection.oddFan_marked_of_phase
#print axioms CollatzShell.ForwardSection.marked_fan_of_phase

-- SectionTransport
#print axioms CollatzShell.ForwardSection.Transport.weight_nonneg
#print axioms CollatzShell.ForwardSection.Transport.weight_summable
#print axioms CollatzShell.ForwardSection.Transport.sectionWeight_nonneg
#print axioms CollatzShell.ForwardSection.Transport.sectionWeight_le
#print axioms CollatzShell.ForwardSection.Transport.sectionWeight_summable
#print axioms CollatzShell.ForwardSection.Transport.source_atom_le
#print axioms CollatzShell.ForwardSection.Transport.returnMass_total
#print axioms CollatzShell.ForwardSection.Transport.weight_lt_of_growth
#print axioms CollatzShell.ForwardSection.Transport.no_uniform_endpoint_bound
#print axioms CollatzShell.ForwardSection.Transport.entryMass_total
#print axioms CollatzShell.ForwardSection.Transport.entry_atom_le
#print axioms CollatzShell.ForwardSection.Transport.no_uniform_entry_bound
