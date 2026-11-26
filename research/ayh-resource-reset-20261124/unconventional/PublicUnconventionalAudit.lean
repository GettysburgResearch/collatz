import AdelicSwitch
import AdelicParent
import InverseBudget
import InversePhase
import InverseMultiplicity
import DyadicPowerPrecision
import LogTowerData
import LogTowerCore
import LogTower
import PerfectPowerParents
import SegmentTrace
import NegativeProfile
import NegativeExponentAddress
import WallRefinement
import WallGate
import WallShadow
import WallWheel
import WallPeriodic
import WallRun
import WallBank
import WallRuns81
import WallRational
import WallAffine
import WallOrbit
import WallGeneral
import WallUniform
import WallWords
import WallExamples
import WallTernary
import WallDichotomy
import WallDensity
import WallEscape
import WallShifted
import WallLinear
import WallDelay
import RecordPrecision
import FreshAscentShadow
import UnconventionalProposal

/-! Exhaustive audit of every explicitly declared public theorem in this packet. -/
#print axioms AdelicSwitch.prepare
#print axioms AdelicSwitch.power_precision
#print axioms AdelicSwitch.cylinder
#print axioms AdelicParent.cylinder_excluded
#print axioms InverseBudget.equation
#print axioms InverseBudget.one_class
#print axioms InverseBudget.quadratic
#print axioms InverseBudget.root_bound
#print axioms InversePhase.all_phase_gate
#print axioms InverseMultiplicity.legal_iff
#print axioms InverseMultiplicity.numerator_unique
#print axioms DyadicPowerPrecision.precision
#print axioms LogTowerData.finite_unit
#print axioms LogTowerData.anchors
#print axioms LogTowerData.terminal
#print axioms LogTower.rotation_multiple
#print axioms LogTower.normalized
#print axioms LogTower.normalized_at
#print axioms LogTower.anchor_lift
#print axioms LogTower.laps
#print axioms LogTower.terminal_lift
#print axioms LogTower.ordinary_gate
#print axioms LogTower.band_peaks
#print axioms LogTower.six_peaks
#print axioms PerfectPowerParents.excluded
#print axioms SegmentTrace.correct
#print axioms NegativeProfile.ordinary
#print axioms NegativeExponentAddress.minus_one_grade
#print axioms NegativeExponentAddress.separated_endpoint
#print axioms NegativeExponentAddress.all_earlier
#print axioms NegativeExponentAddress.representative_form
#print axioms NegativeExponentAddress.progression
#print axioms NegativeExponentAddress.not_perfect_power
#print axioms NegativeExponentAddress.all_smaller
#print axioms NegativeExponentAddress.pointwise
#print axioms NegativeExponentAddress.full_clock
#print axioms NegativeExponentAddress.full_margin
#print axioms NegativeExponentAddress.prepeak_clock
#print axioms WallRefinement.child_eq
#print axioms WallRefinement.index_eq
#print axioms WallRefinement.index_mixed
#print axioms WallRefinement.triple_four_edge
#print axioms WallRefinement.ones
#print axioms WallRefinement.even_pair
#print axioms WallRefinement.run_fusion
#print axioms WallRefinement.forbidden_even_run
#print axioms WallRefinement.split_difference
#print axioms WallRefinement.propagated
#print axioms WallRefinement.propagated_run
#print axioms WallRefinement.fused_zero
#print axioms WallRefinement.exact_sparseSum
#print axioms WallRefinement.source_difference
#print axioms WallRefinement.twelve_bit_cut
#print axioms WallRefinement.thirteen_bit_cut
#print axioms WallRefinement.fixed_source
#print axioms WallShadow.block_eq
#print axioms WallShadow.paired_charts
#print axioms WallWheel.wheel
#print axioms WallWheel.bank_spec
#print axioms WallWheel.bank_merge
#print axioms WallPeriodic.cross_clock_merge
#print axioms WallPeriodic.breaks_by
#print axioms WallPeriodic.split_twos
#print axioms WallPeriodic.no_infinite_period
#print axioms WallPeriodic.index_add
#print axioms WallPeriodic.from_copies
#print axioms WallPeriodic.reset_bound
#print axioms WallPeriodic.eventually_from_reset
#print axioms WallPeriodic.eventually_no_copies
#print axioms WallBank.sound
#print axioms WallBank.forbids
#print axioms WallBank.reset_81
#print axioms WallBank.eventually_no_81
#print axioms WallRational.runD_add
#print axioms WallRational.grade_add
#print axioms WallRational.lift
#print axioms WallRational.lap
#print axioms WallAffine.solve_unit
#print axioms WallAffine.cell_pull
#print axioms WallAffine.absorb
#print axioms WallAffine.signed_lift
#print axioms WallAffine.two_slopes
#print axioms WallAffine.in_class
#print axioms WallOrbit.odd_power
#print axioms WallOrbit.bit
#print axioms WallOrbit.cover
#print axioms WallOrbit.cancel
#print axioms WallOrbit.exponential_merger
#print axioms WallOrbit.exp_unit
#print axioms WallOrbit.paired
#print axioms WallGeneral.address_eq
#print axioms WallGeneral.phase_at
#print axioms WallGeneral.chart_arm
#print axioms WallGeneral.signed_nat
#print axioms WallGeneral.cross_clock
#print axioms WallGeneral.breaks
#print axioms WallUniform.finite_bound
#print axioms WallUniform.exponential_bound
#print axioms WallUniform.paired_bound
#print axioms WallUniform.after_mismatch
#print axioms WallWords.range
#print axioms WallWords.read_blocks
#print axioms WallWords.eventual_cap
#print axioms WallExamples.period4
#print axioms WallExamples.period8
#print axioms WallExamples.period12
#print axioms WallExamples.period18
#print axioms WallTernary.excludes_power_three
#print axioms WallTernary.finite_floor
#print axioms WallTernary.ternary_bound
#print axioms WallTernary.rejects_ternary_word
#print axioms WallDichotomy.ternary_or_breaks
#print axioms WallDichotomy.alternating_or_eventual_cap
#print axioms WallDensity.time_pos
#print axioms WallDensity.chart_from_residue
#print axioms WallDensity.same_rate
#print axioms WallDensity.universal_cap
#print axioms WallDensity.period18_uniform
#print axioms WallEscape.positive_escape
#print axioms WallEscape.forces_escape
#print axioms WallShifted.sampled
#print axioms WallShifted.rotation_cap
#print axioms WallLinear.linear_depth
#print axioms WallDelay.merger_needs_clock
#print axioms WallDelay.period18_separated
#print axioms WallDelay.other_separations
#print axioms WallDelay.missing_bit
#print axioms WallDelay.period18_unbounded_clocks
#print axioms Collatz.RecordPrecision.ordinary_row
#print axioms Collatz.RecordPrecision.grade_le_clock
#print axioms Collatz.RecordPrecision.carry_le
#print axioms Collatz.RecordPrecision.carry_plus_clock_le
#print axioms Collatz.RecordPrecision.shifted_row
#print axioms Collatz.RecordPrecision.zero_shift_parameter
#print axioms Collatz.RecordPrecision.closing_matches
#print axioms Collatz.RecordPrecision.disjoint_powers
#print axioms Collatz.RecordPrecision.clock_difference_coprime
#print axioms Collatz.RecordPrecision.one_zero_denominator_dvd
#print axioms Collatz.RecordPrecision.fixed_plane_late
#print axioms Collatz.RecordPrecision.fixed_plane_unique_late
#print axioms Collatz.FreshAscentShadow.endpoint_unique
#print axioms Collatz.FreshAscentShadow.shift_path
#print axioms Collatz.FreshAscentShadow.at_signed_fixed_point
#print axioms Collatz.FreshAscentShadow.signed_parent_gt_one
#print axioms Collatz.FreshAscentShadow.first_fresh_parent
#print axioms UnconventionalProposal.small_query_excluded
#print axioms UnconventionalProposal.failure_has_wall
#print axioms UnconventionalProposal.survivor_extends
#print axioms UnconventionalProposal.collatz_from_remaining
#print axioms UnconventionalProposal.collatz_iff_remaining
