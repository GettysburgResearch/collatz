import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite core of the density-free deflated-germ criterion. This file checks
the explicit strict two-center strategy and the integer recurrence for
the inverse of 1+4t+t^2. It does not assume or formalize the external
arithmetic rationality theorem, analytic radii, or the existence of the
required actual Collatz germ.
-/

set_option autoImplicit false

namespace CollatzGermCapacity

private theorem logarithmic_margin :
    3 * Real.log (3 / 2 : Real) < 2 * Real.log 2 := by
  have h : Real.log ((3 / 2 : Real) ^ 3) < Real.log ((2 : Real) ^ 2) :=
    Real.log_lt_log (by norm_num) (by norm_num)
  simpa only [Real.log_pow, Nat.cast_ofNat] using h

private theorem first_diagonal :
    Real.log (4 / 9 : Real) = -2 * Real.log (3 / 2 : Real) := by
  have h : (4 / 9 : Real) = ((3 / 2 : Real) ^ 2)⁻¹ := by norm_num
  rw [h, Real.log_inv, Real.log_pow]
  ring

private theorem second_diagonal :
    Real.log (2 / 3 : Real) = -Real.log (3 / 2 : Real) := by
  have h : (2 / 3 : Real) = (3 / 2 : Real)⁻¹ := by norm_num
  rw [h, Real.log_inv]

/-- The explicit strategy has a positive payoff against the first pure column. -/
theorem first_column_positive :
    0 < (2 / 5 : Real) * Real.log (4 / 9 : Real)
        + (3 / 5 : Real) * Real.log 2 := by
  rw [first_diagonal]
  have h := logarithmic_margin
  have h2 : 0 < Real.log (2 : Real) := Real.log_pos (by norm_num)
  linarith

/-- The same strategy also pays strictly against the second pure column. -/
theorem second_column_positive :
    0 < (2 / 5 : Real) * Real.log 2
        + (3 / 5 : Real) * Real.log (2 / 3 : Real) := by
  rw [second_diagonal]
  have h := logarithmic_margin
  linarith

/-- The exact two-center matrix has a strictly positive payoff against
every mixed column. This supplies a finite game certificate only. -/
theorem capacity_strategy_positive (t : Real) (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    0 < t * ((2 / 5 : Real) * Real.log (4 / 9 : Real)
              + (3 / 5 : Real) * Real.log 2)
       + (1 - t) * ((2 / 5 : Real) * Real.log 2
              + (3 / 5 : Real) * Real.log (2 / 3 : Real)) := by
  let a := (2 / 5 : Real) * Real.log (4 / 9 : Real)
              + (3 / 5 : Real) * Real.log 2
  let b := (2 / 5 : Real) * Real.log 2
              + (3 / 5 : Real) * Real.log (2 / 3 : Real)
  have ha : 0 < a := first_column_positive
  have hb : 0 < b := second_column_positive
  have hmin : 0 < min a b := lt_min ha hb
  change 0 < t * a + (1 - t) * b
  calc
    0 < min a b := hmin
    _ = t * min a b + (1 - t) * min a b := by ring
    _ ≤ t * a + (1 - t) * b := by
      exact add_le_add
        (mul_le_mul_of_nonneg_left (min_le_left a b) h0)
        (mul_le_mul_of_nonneg_left (min_le_right a b) (sub_nonneg.mpr h1))

/-- Integer coefficients of the formal inverse of 1+4t+t^2. -/
def inverseCoeff : Nat → Int
  | 0 => 1
  | 1 => -4
  | n + 2 => -4 * inverseCoeff (n + 1) - inverseCoeff n

theorem inverse_constant : inverseCoeff 0 = 1 := rfl

theorem inverse_linear : inverseCoeff 1 + 4 * inverseCoeff 0 = 0 := by
  norm_num [inverseCoeff]

theorem inverse_convolution (n : Nat) :
    inverseCoeff (n + 2) + 4 * inverseCoeff (n + 1) + inverseCoeff n = 0 := by
  rw [inverseCoeff]
  ring

#print axioms first_column_positive
#print axioms second_column_positive
#print axioms capacity_strategy_positive
#print axioms inverse_constant
#print axioms inverse_linear
#print axioms inverse_convolution

end CollatzGermCapacity
