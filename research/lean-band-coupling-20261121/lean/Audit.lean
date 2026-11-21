module

public import Examples
public import LowerMarkedMerger
public import RisingReturns

@[expose] public section

/-! Kernel dependency audit. No theorem below asserts the open global cover. -/

#print axioms CollatzShell.ForwardSection.bounded_visit
#print axioms CollatzShell.ForwardSection.marked_count_bound
#print axioms CollatzShell.ForwardSection.collatz_iff_return_descent
#print axioms CollatzShell.ForwardSection.arbitrarily_large_first_return
#print axioms CollatzShell.ForwardSection.steer_window
#print axioms CollatzShell.ForwardSection.steer_non_descending
#print axioms CollatzShell.ForwardSection.no_descent_forces_height_gain
#print axioms CollatzShell.OffsetDescent.binary_lift
#print axioms CollatzShell.OffsetDescent.offset_descent_transports
#print axioms CollatzShell.OffsetDescent.rebase_hits
#print axioms CollatzShell.OffsetDescent.reservedRebase_hits
#print axioms CollatzShell.OffsetDescent.reservedRebase_cheaper_iff
#print axioms CollatzShell.OffsetDescent.basin_of_cheaper_reservedRebase
#print axioms CollatzShell.OffsetDescent.horizonSeed_marked
#print axioms CollatzShell.OffsetDescent.horizonSeed_no_descent
#print axioms CollatzShell.rising_smaller_partner
#print axioms CollatzShell.horizon_family_smaller_partner
#print axioms CollatzShell.horizon_family_basin_of_smaller
#print axioms CollatzShell.ForwardSection.marked_return_clock_bound
#print axioms CollatzShell.ForwardSection.eventually_long_return
#print axioms CollatzShell.ForwardSection.collatz_iff_source_bounded_section_merge
#print axioms CollatzShell.BandExamples.reserve_283_merge
#print axioms CollatzShell.BandExamples.seed_319_no_native_descent
#print axioms CollatzShell.BandExamples.seed_319_smaller_merger

#print axioms CollatzShell.ForwardSection.lower_marked_from_small_merger
#print axioms CollatzShell.ForwardSection.collatz_iff_marked_merger_descent
#print axioms CollatzShell.ForwardSection.collatz_iff_small_marked_merger_cover
