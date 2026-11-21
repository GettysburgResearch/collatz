-- Legacy-compatible audit entrypoint: the packet also contains two Std-only files.

import HarmonicTransport
import ClockAbsorption
import BandAbsorption
import FiniteResolvent
import ExplicitSeed
import ActualSurvivorMass
import ExplicitClosure
import PullbackArithmetic
import WildLift
import HalfSourceMerge
import LongDiamondErasure
import MarkedErasure
import NewBandFamily
import RayCertificates
import AL27Certificates
import ResidualPrefixErasure
import ResidualPhaseSelector
import AL27HalfSelector

/- Every public theorem introduced by this packet is audited below.
   Conditional closing estimates remain theorem parameters. -/

-- HarmonicTransport: 6 public theorems
#print axioms CollatzHarmonic.mass_of_distinct
#print axioms CollatzHarmonic.finite_reciprocal_budget
#print axioms CollatzHarmonic.harmonic_dyadic
#print axioms CollatzHarmonic.finite_linear_budget
#print axioms CollatzHarmonic.not_injective_of_linear
#print axioms CollatzHarmonic.not_injective_of_reciprocal

-- ClockAbsorption: 5 public theorems
#print axioms CollatzHarmonic.clockLift_iterate
#print axioms CollatzHarmonic.clockLift_injective_of_avoid
#print axioms CollatzHarmonic.atom_of_column
#print axioms CollatzHarmonic.absorption_of_linear_columns
#print axioms CollatzHarmonic.absorption_of_reciprocal_columns

-- BandAbsorption: 4 public theorems
#print axioms CollatzShell.ForwardSection.returns_eq_iterate
#print axioms CollatzShell.ForwardSection.return_iterate_hit
#print axioms CollatzShell.ForwardSection.collatz_of_marked_linear_columns
#print axioms CollatzShell.ForwardSection.collatz_of_marked_reciprocal_columns

-- FiniteResolvent: 14 public theorems
#print axioms CollatzFiniteResolvent.coefficient_pos
#print axioms CollatzFiniteResolvent.growth_nonneg
#print axioms CollatzFiniteResolvent.coefficient_zero
#print axioms CollatzFiniteResolvent.coefficient_ratio
#print axioms CollatzFiniteResolvent.geometric_growth_sum_exact
#print axioms CollatzFiniteResolvent.geometric_growth_sum_le_eight
#print axioms CollatzFiniteResolvent.budget_le
#print axioms CollatzFiniteResolvent.survivor_atom_bound
#print axioms CollatzFiniteResolvent.survivor_atom_bound_cleared
#print axioms CollatzFiniteResolvent.excludes_transport_of_strict_budget
#print axioms CollatzFiniteResolvent.norm_floor_of_comparable_fibers
#print axioms CollatzFiniteResolvent.coefficient_antitone
#print axioms CollatzFiniteResolvent.coefficient_shift_bound
#print axioms CollatzFiniteResolvent.terminating_shift_fiber_floor

-- ExplicitSeed: 6 public theorems
#print axioms CollatzFiniteResolvent.coefficient_telescope
#print axioms CollatzFiniteResolvent.coefficient_prefix
#print axioms CollatzFiniteResolvent.coefficient_prefix_le_one
#print axioms CollatzFiniteResolvent.coefficient_finiteMass
#print axioms CollatzFiniteResolvent.growth_mul_coefficient
#print axioms CollatzFiniteResolvent.quadratic_baseline

-- ActualSurvivorMass: 9 public theorems
#print axioms CollatzShell.ForwardSection.incomingTerm_bounds
#print axioms CollatzShell.ForwardSection.incoming_finite_bound
#print axioms CollatzShell.ForwardSection.incoming_bdd
#print axioms CollatzShell.ForwardSection.incoming_bounds
#print axioms CollatzShell.ForwardSection.source_atom_le_incoming
#print axioms CollatzShell.ForwardSection.actual_survivor_budget
#print axioms CollatzShell.ForwardSection.survives_of_not_basin
#print axioms CollatzShell.ForwardSection.counterexample_forces_quadratic
#print axioms CollatzShell.ForwardSection.collatz_of_quadratic_slice_saving

-- ExplicitClosure: 2 public theorems
#print axioms CollatzShell.ForwardSection.actual_quadratic_baseline
#print axioms CollatzShell.ForwardSection.collatz_of_explicit_quadratic_saving

-- PullbackArithmetic: 6 public theorems
#print axioms WildLift.correction_iff
#print axioms WildLift.correction_unique
#print axioms WildLift.pullback_identity
#print axioms WildLift.pullback_congruence
#print axioms WildLift.thirteen_after_one_odd
#print axioms WildLift.thirteen_after_two_odds_impossible

-- WildLift: 1 public theorems
#print axioms WildLift.bridge_eight

-- HalfSourceMerge: 4 public theorems
#print axioms CollatzShell.rising_erase_prefix
#print axioms CollatzShell.rising_half_source_of_diamond
#print axioms CollatzShell.half_source_two_clock_diamond
#print axioms CollatzShell.rising_half_source_partner

-- LongDiamondErasure: 5 public theorems
#print axioms CollatzShell.endpoint_diamond_eight_affine
#print axioms CollatzShell.endpoint_diamond_eight
#print axioms CollatzShell.endpoint_diamond_chain
#print axioms CollatzShell.rising_quarter_source_partner
#print axioms CollatzShell.rising_eighth_source_partner

-- MarkedErasure: 2 public theorems
#print axioms CollatzShell.ForwardSection.marked_of_dyadic_prefix_erasure
#print axioms CollatzShell.ForwardSection.rising_erasure_marked_partner

-- NewBandFamily: 10 public theorems
#print axioms CollatzShell.NewBandFamily.exponent_eq
#print axioms CollatzShell.NewBandFamily.seed_form
#print axioms CollatzShell.NewBandFamily.seed_log2
#print axioms CollatzShell.NewBandFamily.seed_marked
#print axioms CollatzShell.NewBandFamily.no_descent_through_run_plus_gap
#print axioms CollatzShell.NewBandFamily.seed_no_descent
#print axioms CollatzShell.NewBandFamily.seed_quarter_merger
#print axioms CollatzShell.NewBandFamily.merger_inside_native_horizon
#print axioms CollatzShell.NewBandFamily.partner_marked
#print axioms CollatzShell.NewBandFamily.lower_marked_merger

-- RayCertificates: 2 public theorems
#print axioms CollatzShell.RayCertificates.ray_certificate_sound
#print axioms CollatzShell.RayCertificates.basin_of_valid_ray

-- AL27Certificates: 35 public theorems
#print axioms CollatzShell.AL27Certificates.chunk00_valid
#print axioms CollatzShell.AL27Certificates.chunk01_valid
#print axioms CollatzShell.AL27Certificates.chunk02_valid
#print axioms CollatzShell.AL27Certificates.chunk03_valid
#print axioms CollatzShell.AL27Certificates.chunk04_valid
#print axioms CollatzShell.AL27Certificates.chunk05_valid
#print axioms CollatzShell.AL27Certificates.chunk06_valid
#print axioms CollatzShell.AL27Certificates.chunk07_valid
#print axioms CollatzShell.AL27Certificates.chunk08_valid
#print axioms CollatzShell.AL27Certificates.chunk09_valid
#print axioms CollatzShell.AL27Certificates.chunk10_valid
#print axioms CollatzShell.AL27Certificates.chunk11_valid
#print axioms CollatzShell.AL27Certificates.chunk12_valid
#print axioms CollatzShell.AL27Certificates.chunk13_valid
#print axioms CollatzShell.AL27Certificates.chunk14_valid
#print axioms CollatzShell.AL27Certificates.chunk15_valid
#print axioms CollatzShell.AL27Certificates.chunk16_valid
#print axioms CollatzShell.AL27Certificates.chunk17_valid
#print axioms CollatzShell.AL27Certificates.chunk18_valid
#print axioms CollatzShell.AL27Certificates.chunk19_valid
#print axioms CollatzShell.AL27Certificates.chunk20_valid
#print axioms CollatzShell.AL27Certificates.chunk21_valid
#print axioms CollatzShell.AL27Certificates.chunk22_valid
#print axioms CollatzShell.AL27Certificates.chunk23_valid
#print axioms CollatzShell.AL27Certificates.chunk24_valid
#print axioms CollatzShell.AL27Certificates.chunk25_valid
#print axioms CollatzShell.AL27Certificates.chunk26_valid
#print axioms CollatzShell.AL27Certificates.chunk27_valid
#print axioms CollatzShell.AL27Certificates.rows_valid_list
#print axioms CollatzShell.AL27Certificates.rows_valid
#print axioms CollatzShell.AL27Certificates.rows_count
#print axioms CollatzShell.AL27Certificates.source_residues_distinct
#print axioms CollatzShell.AL27Certificates.source_branch
#print axioms CollatzShell.AL27Certificates.certified_ray
#print axioms CollatzShell.AL27Certificates.certified_induction

-- ResidualPrefixErasure: 8 public theorems
#print axioms CollatzShell.ResidualPrefixErasure.prefix_source_bound
#print axioms CollatzShell.ResidualPrefixErasure.prefix_source_bound_eventually
#print axioms CollatzShell.ResidualPrefixErasure.prefix_diamond_partner
#print axioms CollatzShell.ResidualPrefixErasure.prefix_diamond_partner_eventually
#print axioms CollatzShell.ResidualPrefixErasure.prefix27
#print axioms CollatzShell.ResidualPrefixErasure.prefix27_initial_growth
#print axioms CollatzShell.ResidualPrefixErasure.prefix27_no_descent_through_run
#print axioms CollatzShell.ResidualPrefixErasure.prefix27_eighth_partner

-- ResidualPhaseSelector: 12 public theorems
#print axioms CollatzShell.ResidualPhaseSelector.source_endpoint
#print axioms CollatzShell.ResidualPhaseSelector.parameter_odd
#print axioms CollatzShell.ResidualPhaseSelector.source_progression
#print axioms CollatzShell.ResidualPhaseSelector.source_base_bounds
#print axioms CollatzShell.ResidualPhaseSelector.endpoint_phase
#print axioms CollatzShell.ResidualPhaseSelector.physical_merger
#print axioms CollatzShell.ResidualPhaseSelector.source_residue
#print axioms CollatzShell.ResidualPhaseSelector.no_direct_descent_through_run
#print axioms CollatzShell.ResidualPhaseSelector.no_direct_descent_thirteen
#print axioms CollatzShell.ResidualPhaseSelector.smaller_physical_merger
#print axioms CollatzShell.ResidualPhaseSelector.no_direct_descent_through_merger
#print axioms CollatzShell.ResidualPhaseSelector.basin_by_smaller_induction

-- AL27HalfSelector: 9 public theorems
#print axioms CollatzShell.AL27HalfSelector.source_endpoint
#print axioms CollatzShell.AL27HalfSelector.endpoint_phase
#print axioms CollatzShell.AL27HalfSelector.parameter_odd
#print axioms CollatzShell.AL27HalfSelector.source_residue
#print axioms CollatzShell.AL27HalfSelector.source_progression
#print axioms CollatzShell.AL27HalfSelector.source_base_bounds
#print axioms CollatzShell.AL27HalfSelector.physical_merger
#print axioms CollatzShell.AL27HalfSelector.no_direct_descent_through_merger
#print axioms CollatzShell.AL27HalfSelector.basin_by_smaller_induction
