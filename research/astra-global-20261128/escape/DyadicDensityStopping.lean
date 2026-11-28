import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

/-! Finite stopping budgets for a dyadic probability tree. The normalized
width of the current cell is passed explicitly so that translates and
arbitrary starting levels use the same recursion. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DyadicDensityStopping

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The total mass stopped on its first low-density cell through this depth. -/
def firstLow (mass : List Bool → K) (low : K) :
    ℕ → List Bool → K → K
  | 0, cell, width => if mass cell ≤ low * width then mass cell else 0
  | n + 1, cell, width =>
      if mass cell ≤ low * width then mass cell
      else firstLow mass low n (false :: cell) (width / 2) +
        firstLow mass low n (true :: cell) (width / 2)

/-- An arbitrary finite-horizon low-density stop costs at most cutoff
times initial cell length, allowing zero-mass descendants. -/
theorem firstLow_le (mass : List Bool → K) (low : K) (hLow : 0 ≤ low)
    (n : ℕ) (cell : List Bool) (width : K) (hw : 0 ≤ width) :
    firstLow mass low n cell width ≤ low * width := by
  induction n generalizing cell width with
  | zero =>
    unfold firstLow
    split
    · assumption
    · exact mul_nonneg hLow hw
  | succ n ih =>
    unfold firstLow
    split
    · assumption
    · have hhalf : 0 ≤ width / 2 := div_nonneg hw zero_le_two
      have hsum := add_le_add (ih (false :: cell) (width / 2) hhalf)
        (ih (true :: cell) (width / 2) hhalf)
      simpa only [← mul_add, add_halves] using hsum

/-- Through a common finite horizon, stop on the first high-density cell,
then on its first low-density descendant within the time remaining. -/
def highThenLow (mass : List Bool → K) (high low : K) :
    ℕ → List Bool → K → K
  | 0, cell, width =>
      if high * width ≤ mass cell then firstLow mass low 0 cell width else 0
  | n + 1, cell, width =>
      if high * width ≤ mass cell then firstLow mass low (n + 1) cell width
      else highThenLow mass high low n (false :: cell) (width / 2) +
        highThenLow mass high low n (true :: cell) (width / 2)

/-- The mass that registers a high cell and a subsequent low cell is at
most the threshold ratio times the initial mass. -/
theorem highThenLow_le (mass : List Bool → K)
    (nonneg : ∀ cell, 0 ≤ mass cell)
    (splitMass : ∀ cell, mass (false :: cell) + mass (true :: cell) = mass cell)
    (high low : K) (hHigh : 0 < high) (hLow : 0 ≤ low)
    (n : ℕ) (cell : List Bool) (width : K) (hw : 0 ≤ width) :
    highThenLow mass high low n cell width ≤ (low / high) * mass cell := by
  have ratio : 0 ≤ low / high := div_nonneg hLow (le_of_lt hHigh)
  have stopped (depth : ℕ) (node : List Bool) (w : K) (hw' : 0 ≤ w)
      (hit : high * w ≤ mass node) :
      firstLow mass low depth node w ≤ (low / high) * mass node := by
    have scaled := mul_le_mul_of_nonneg_left hit ratio
    rw [← mul_assoc, div_mul_cancel₀ low (ne_of_gt hHigh)] at scaled
    exact (firstLow_le mass low hLow depth node w hw').trans scaled
  induction n generalizing cell width with
  | zero =>
    unfold highThenLow
    split
    · exact stopped 0 cell width hw (by assumption)
    · exact mul_nonneg ratio (nonneg cell)
  | succ n ih =>
    unfold highThenLow
    split
    · exact stopped (n + 1) cell width hw (by assumption)
    · have hhalf : 0 ≤ width / 2 := div_nonneg hw zero_le_two
      have hsum := add_le_add (ih (false :: cell) (width / 2) hhalf)
        (ih (true :: cell) (width / 2) hhalf)
      simpa only [← mul_add, splitMass] using hsum

end Collatz.DyadicDensityStopping
