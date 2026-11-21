module

public import ClockSteering
public import OffsetDescent
public import OffsetHorizon
public import ReturnClock
public import RisingMerge
public import SourceBoundedMerge

@[expose] public section

namespace CollatzShell.BandExamples

open OffsetDescent

/-- A reserve of two ternary factors repairs the native splice for 283. -/
theorem reserve_283_source : reservedSource 139 4 2 1 = 283 := by decide

theorem reserve_283_partner : reservedRebase 139 4 2 1 123 7 = 251 := by decide

theorem reserve_283_merge : orbit 7 251 = orbit 4 283 := by
  have merge : orbit 7 123 = orbit 4 139 := by decide
  have count : oddCount 7 123 ≤ oddCount 4 139 + 2 := by decide
  have result := reservedRebase_hits (s:=2) (v:=1) merge count
  simpa only [reserve_283_source,reserve_283_partner] using result

theorem reserve_283_smaller : 0 < 251 ∧ 251 < 283 := by decide

/-- The explicit 319 example needs a merger rather than native-horizon
forward descent: its first eight clocks all remain at least 319. -/
theorem seed_319_no_native_descent : ∀ t≤8, 319≤orbit t 319 := by
  intro t ht
  exact horizonSeed_no_descent (m:=2) (by decide) ht

theorem seed_319_smaller_merger : 0<239 ∧ 239<319 ∧ orbit 6 239=orbit 8 319 := by
  exact rising_smaller_partner 6 5 (by decide) (by decide) (by decide)

#print axioms reserve_283_merge
#print axioms seed_319_no_native_descent
#print axioms seed_319_smaller_merger

end CollatzShell.BandExamples
