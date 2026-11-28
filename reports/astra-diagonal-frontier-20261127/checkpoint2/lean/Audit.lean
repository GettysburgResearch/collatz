import NativeGate
import NativeTransfer
import NativeDecay
import NativeTightness
import NativeCriterion
import NativePersistence
import NativeResidue
import SeedSpread
import ComponentLoss
import FirstEntryRecord
import SelectedBlockBarrier
import PolynomialRank
import HigherDifference
import RotationCuts
import OrdinaryMerge
import ShortProbe
import UnitWindowLift

#print axioms Collatz.NativeGate.step_positive
#print axioms Collatz.NativeGate.orbit_positive
#print axioms Collatz.NativeGate.orbit_add
#print axioms Collatz.NativeGate.reaches_of_orbit
#print axioms Collatz.NativeGate.even_step
#print axioms Collatz.NativeGate.odd_step
#print axioms Collatz.NativeGate.fourth_margin
#print axioms Collatz.NativeGate.protected_bound
#print axioms Collatz.NativeGate.least_source_gate
#print axioms Collatz.NativeGate.atom_le_mass
#print axioms Collatz.NativeGate.extinction_implies_collatz
#print axioms Collatz.NativeGate.finite_certificate
#print axioms Collatz.NativeGate.loss_budget_excludes_atom
#print axioms Collatz.NativeGate.reserve_high
#print axioms Collatz.NativeGate.reserve_low
#print axioms Collatz.NativeGate.orbit_succ_first
#print axioms Collatz.NativeGate.odds_succ_first
#print axioms Collatz.NativeGate.step_lift
#print axioms Collatz.NativeGate.cylinder_lift
#print axioms Collatz.NativeGate.gate_lift
#print axioms Collatz.NativeGate.gate_succ
#print axioms Collatz.NativeGate.candidate_bounds
#print axioms Collatz.NativeGate.candidate_children
#print axioms Collatz.NativeGate.children_disjoint
#print axioms Collatz.NativeGate.sum_children
#print axioms Collatz.NativeGate.mass_identity
#print axioms Collatz.NativeGate.births_le_budget
#print axioms Collatz.NativeGate.debt_nonnegative_iff
#print axioms Collatz.NativeGate.next_gate_iff
#print axioms Collatz.NativeGate.debt_next
#print axioms Collatz.NativeGate.sibling_parity
#print axioms Collatz.NativeGate.reserve_children
#print axioms Collatz.NativeGate.reserve_decreases
#print axioms Collatz.NativeGate.mass_nonnegative
#print axioms Collatz.NativeGate.deaths_nonnegative
#print axioms Collatz.NativeGate.reserve_nonnegative
#print axioms Collatz.NativeGate.envelope_step
#print axioms Collatz.NativeGate.initial_envelope
#print axioms Collatz.NativeGate.envelope_budget
#print axioms Collatz.NativeGate.total_loss_budget
#print axioms Collatz.NativeGate.tail_loss_budget
#print axioms Collatz.NativeGate.native_cutoff
#print axioms Collatz.NativeGate.loss_hazard_implies_collatz
#print axioms Collatz.NativeGate.tilt_positive
#print axioms Collatz.NativeGate.decayRatio_range
#print axioms Collatz.NativeGate.exponentialWeight_positive
#print axioms Collatz.NativeGate.exponentialWeight_lift
#print axioms Collatz.NativeGate.exponentialWeight_next
#print axioms Collatz.NativeGate.exponential_children
#print axioms Collatz.NativeGate.exponentialReserve_step
#print axioms Collatz.NativeGate.exponentialReserve_bound
#print axioms Collatz.NativeGate.linear_le_tilt
#print axioms Collatz.NativeGate.reserveWeight_le_exponential
#print axioms Collatz.NativeGate.reserve_exponential_bound
#print axioms Collatz.NativeGate.highMass_nonnegative
#print axioms Collatz.NativeGate.highMass_step
#print axioms Collatz.NativeGate.highMass_reserve_step
#print axioms Collatz.NativeGate.highMass_initial
#print axioms Collatz.NativeGate.future_highMass_budget
#print axioms Collatz.NativeGate.future_highMass
#print axioms Collatz.NativeGate.gate_mono
#print axioms Collatz.NativeGate.odds_add
#print axioms Collatz.NativeGate.one_even_clock
#print axioms Collatz.NativeGate.reachesOne_fails_gate
#print axioms Collatz.NativeGate.finite_gate_failure
#print axioms Collatz.NativeGate.low_sources_exhausted
#print axioms Collatz.NativeGate.covered_eventual_mass
#print axioms Collatz.NativeGate.universal_eventual_mass
#print axioms Collatz.NativeGate.decayRatio_polynomial_bound
#print axioms Collatz.NativeGate.reserve_small
#print axioms Collatz.NativeGate.covered_finite_certificate
#print axioms Collatz.NativeGate.universal_implies_extinction
#print axioms Collatz.NativeGate.collatz_iff_extinction
#print axioms Collatz.NativeGate.permanent_not_reachesOne
#print axioms Collatz.NativeGate.permanentSources_subset
#print axioms Collatz.NativeGate.permanentMass_nonnegative
#print axioms Collatz.NativeGate.permanentMass_le_mass
#print axioms Collatz.NativeGate.atom_le_permanentMass
#print axioms Collatz.NativeGate.permanentMass_mono
#print axioms Collatz.NativeGate.finite_temporary_exhaustion
#print axioms Collatz.NativeGate.mass_le_permanent_add_high
#print axioms Collatz.NativeGate.eventual_permanent_sandwich
#print axioms Collatz.NativeGate.mass_rational_cauchy
#print axioms Collatz.NativeGate.permanentMass_tail
#print axioms Collatz.NativeGate.permanentMass_bound
#print axioms Collatz.NativeGate.permanentMass_finite_certificate
#print axioms Collatz.NativeGate.universal_iff_permanentMass_zero
#print axioms Collatz.NativeGate.persistentTotal_bdd
#print axioms Collatz.NativeGate.persistentTotal_lower
#print axioms Collatz.NativeGate.persistentTotal_upper
#print axioms Collatz.NativeGate.persistentTotal_nonnegative
#print axioms Collatz.NativeGate.persistentTotal_at_most_nine
#print axioms Collatz.NativeGate.persistentTotal_computable_upper
#print axioms Collatz.NativeGate.permanent_atom_le_persistentTotal
#print axioms Collatz.NativeGate.persistentTotal_cutoff_error
#print axioms Collatz.NativeGate.eventual_mass_residue_bound
#print axioms Collatz.NativeGate.mass_tendsto_persistentTotal
#print axioms Collatz.NativeGate.collatz_iff_persistentTotal_zero
#print axioms SeedSpread.selected_words
#print axioms SeedSpread.rows_first_half
#print axioms SeedSpread.row_at
#print axioms SeedSpread.next_even_terminal_fails
#print axioms SeedSpread.block_pairs
#print axioms SeedSpread.no_wrap
#print axioms ComponentLoss.edge_bound
#print axioms ComponentLoss.path_bound
#print axioms ComponentLoss.uniform_base
#print axioms ComponentLoss.floor_three_strict
#print axioms FirstEntryRecord.safe_iff_record
#print axioms FirstEntryRecord.no_more_records_iff
#print axioms FirstEntryRecord.first_entry_iff
#print axioms SelectedBlockBarrier.extendBlocks
#print axioms SelectedBlockBarrier.prefixDebt
#print axioms SelectedBlockBarrier.bridgePays
#print axioms SelectedBlockBarrier.failedSuffixPrecludesGate
#print axioms Collatz.PolynomialRank.treeBudget
#print axioms Collatz.PolynomialRank.sumCredits
#print axioms Collatz.PolynomialRank.liveStep
#print axioms Collatz.PolynomialRank.tagBudget
#print axioms Collatz.PolynomialRank.signedLinearDominance
#print axioms Collatz.PolynomialRank.differencesUnique
#print axioms Collatz.PolynomialRank.tritRootCredits
#print axioms Collatz.PolynomialRank.childCoefficientOrder
#print axioms Collatz.PolynomialRank.boxSub
#print axioms Collatz.PolynomialRank.boxShift
#print axioms Collatz.PolynomialRank.unitTelescoping
#print axioms Collatz.PolynomialRank.largeStride
#print axioms Collatz.PolynomialRank.strideUpper
#print axioms Collatz.HigherDifference.thirdTable
#print axioms Collatz.HigherDifference.fourthTable
#print axioms Collatz.HigherDifference.nativeEdge
#print axioms Collatz.HigherDifference.closeLast
#print axioms Collatz.HigherDifference.cubicLift
#print axioms Collatz.HigherDifference.quadraticLift
#print axioms Collatz.RotationCuts.noInversion
#print axioms Collatz.RotationCuts.multiTranslate
#print axioms Collatz.RotationCuts.iterateTranslate
#print axioms Collatz.RotationCuts.repeatClock
#print axioms Collatz.RotationCuts.commonClock
#print axioms Collatz.OrdinaryMerge.orderedSiblings
#print axioms Collatz.OrdinaryMerge.noNegativeMeeting
#print axioms CollatzShortProbe.probe_band
#print axioms CollatzShortProbe.finite_edge_band
#print axioms CollatzWindowLift.visits_of_physical
#print axioms CollatzWindowLift.physical_of_row
#print axioms CollatzWindowLift.mobile_info
#print axioms CollatzWindowLift.prescribed_lift
