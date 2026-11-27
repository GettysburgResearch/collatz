import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum

namespace Collatz.ReciprocalOperator

/-- The unaccelerated positive Collatz map used by the audited source. -/
def ordinary (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else 3*n+1

private theorem positive {n : ℕ} (hn : 0 < n) : 0 < ordinary n := by
  unfold ordinary
  split_ifs with h
  · omega
  · omega

/-- Every three consecutive ordinary positive states have product at least eight. -/
theorem triple_product {n : ℕ} (hn : 0 < n) :
    8 ≤ n * ordinary n * ordinary (ordinary n) := by
  by_cases h : n < 8
  · interval_cases n <;> norm_num [ordinary] at *
  · have hp := positive hn
    have hpp := positive hp
    calc
      8 ≤ n := by omega
      _ ≤ n * ordinary n := Nat.le_mul_of_pos_right n hp
      _ ≤ n * ordinary n * ordinary (ordinary n) :=
        Nat.le_mul_of_pos_right _ hpp

/-- The three-step point-mass multiplier in the harmonic weighted norm.
The operator being audited puts a factor `1/n` on each departure. -/
theorem harmonic_three_step {n : ℕ} (hn : 0 < n) :
    (1 : ℚ) /
      ((ordinary n : ℚ) * ordinary (ordinary n) * ordinary (ordinary (ordinary n)))
      ≤ 1/8 := by
  have h : (8 : ℚ) ≤
      (ordinary n : ℚ) * ordinary (ordinary n) * ordinary (ordinary (ordinary n)) := by
    exact_mod_cast triple_product (positive hn)
  exact (one_div_le_one_div_of_le (by norm_num : (0 : ℚ) < 8) h)

/-- The ordinary cycle has reciprocal departure product exactly one eighth. -/
theorem cycle_product :
    ordinary 1 = 4 ∧ ordinary 4 = 2 ∧ ordinary 2 = 1 ∧
    (1 : ℚ) / (1*4*2) = 1/8 := by
  norm_num [ordinary]

/-- At the point mass at one, logarithmic mass falls from one to one quarter.
This distinguishes a change-of-weight identity from invariance of one functional. -/
theorem logarithmic_mass_changes : (1 : ℚ) / ordinary 1 ≠ 1 := by
  norm_num [ordinary]

#print axioms triple_product
#print axioms harmonic_three_step
#print axioms cycle_product
#print axioms logarithmic_mass_changes

end Collatz.ReciprocalOperator
