import Mathlib.Tactic

/-!
Exact algebra and ordinary arithmetic used to test proposed closing arguments.
This file does not prove Collatz or a universal decreasing rank.  In particular,
the infinite weighted-charge and Subspace Theorem arguments are not formalized.
-/

namespace CentralClosure

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def inverseValley (a b : ℕ) (z : ℚ) : ℚ :=
  2 ^ a * (2 ^ b * z + 1) / 3 ^ a - 1

theorem inverse_difference (a b : ℕ) (z r : ℚ) :
    inverseValley a b z - inverseValley a b r =
      2 ^ (a + b) * (z - r) / 3 ^ a := by
  unfold inverseValley
  rw [pow_add]
  ring

theorem fixed_type_debit (P Q C y z : ℤ) (h : Q * z = P * y + C) :
    Q * ((P - Q) * z + C) = P * ((P - Q) * y + C) := by
  linear_combination (P - Q) * h

/-- A fully ordinary switch from run type (2,1) to run type (3,1). -/
theorem refill_family (t : ℕ) :
    step (512 * t + 91) = 768 * t + 137 ∧
    step (768 * t + 137) = 1152 * t + 206 ∧
    step (1152 * t + 206) = 576 * t + 103 ∧
    step (576 * t + 103) = 864 * t + 155 ∧
    step (864 * t + 155) = 1296 * t + 233 ∧
    step (1296 * t + 233) = 1944 * t + 350 ∧
    step (1944 * t + 350) = 972 * t + 175 := by
  simp only [step]
  split_ifs <;> omega

theorem refill_run_parities (t : ℕ) :
    (512 * t + 91) % 2 = 1 ∧ (768 * t + 137) % 2 = 1 ∧
    (1152 * t + 206) % 2 = 0 ∧ (576 * t + 103) % 2 = 1 ∧
    (864 * t + 155) % 2 = 1 ∧ (1296 * t + 233) % 2 = 1 ∧
    (1944 * t + 350) % 2 = 0 ∧ (972 * t + 175) % 2 = 1 := by
  omega

/-- Exact power of two, stated by divisibility rather than a valuation API. -/
def exactTwoExponent (n k : ℕ) : Prop :=
  n % 2 ^ k = 0 ∧ n % 2 ^ (k + 1) ≠ 0

theorem source_reservoir_five (t : ℕ) :
    exactTwoExponent ((512 * t + 91) + 5) 5 := by
  simp only [exactTwoExponent]
  norm_num
  omega

theorem destination_reservoir_factor (t : ℕ) :
    11 * (576 * t + 103) + 19 = 2 ^ 6 * 9 * (11 * t + 2) := by
  ring

theorem increasing_refill (t : ℕ) :
    0 < 512 * t + 91 ∧ 512 * t + 91 < 576 * t + 103 := by
  omega

/-- A concrete switch has current-type reservoir 5 at 1115 and 9 at 1255. -/
theorem concrete_refill :
    exactTwoExponent (1115 + 5) 5 ∧
    exactTwoExponent (11 * 1255 + 19) 9 ∧
    1115 * 2 ^ 5 < 1255 * 2 ^ 9 := by
  norm_num [exactTwoExponent]

/-- Thus every positive weighting of this reservoir, with nonnegative height
weight, increases on this switch.  The height coordinate here is arbitrary;
in the written rank it is log₂(n), which increases from 1115 to 1255. -/
theorem positive_weights_increase (h₀ h₁ c w : ℝ)
    (hh : h₀ < h₁) (hc : 0 ≤ c) (hw : 0 < w) :
    c * h₀ + w * 5 < c * h₁ + w * 9 := by
  nlinarith [mul_nonneg hc (le_of_lt (sub_pos.mpr hh))]

/-- The unreduced numerator-height comparison at a=16, b=1, r=-5.
The written argument identifies gcd=9 and normalizes by root height 5. -/
theorem restricted_tree_transfer_counterexample :
    Nat.gcd 43636545 43046721 = 9 ∧
    45 * 131072 < 43636545 := by
  decide

#print axioms inverse_difference
#print axioms fixed_type_debit
#print axioms refill_family
#print axioms refill_run_parities
#print axioms source_reservoir_five
#print axioms destination_reservoir_factor
#print axioms increasing_refill
#print axioms concrete_refill
#print axioms positive_weights_increase
#print axioms restricted_tree_transfer_counterexample

end CentralClosure
