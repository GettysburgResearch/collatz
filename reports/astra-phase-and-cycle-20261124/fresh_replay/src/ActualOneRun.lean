module

public import OneRun
public import PhaseBounds
import all ActualScalar

public section

namespace Collatz.PhaseRepulsion

open Collatz.CarryTowerRoundTen.ActualScalar
open Collatz.ActualThreeRun

/-- Run obstruction for the actual discounted-gap scalar at the given shift
of the given positive odd source. No input about future carries is required. -/
theorem actual_one_run (q j L : ℕ) (hq : 0 < q) (ho : Odd q)
    (run : ∀ i, j ≤ i → i < j+L → digit (orbit q i) = 1) :
    2^(L+1) ≤ orbit q j+1 := by
  apply one_run_length (orbit q) (fun i => carry (orbit q i)) j L
  constructor
  · intro i _ _
    exact orbit_pos q i hq
  · intro i _ _
    have hh := Nat.odd_iff.mp (orbit_odd q i ho)
    omega
  · intro i _ _
    exact actual_floor _ (orbit_pos q i hq) (orbit_odd q i ho)
  · intro i hji hil
    refine ⟨gap (orbit q i), gap_pos _ (orbit_odd q i ho), complete_step _, ?_⟩
    exact actual_clock _ (orbit_pos q i hq) 1 (by simpa using run i hji hil)

#print axioms actual_one_run
end Collatz.PhaseRepulsion
