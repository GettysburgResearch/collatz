import PostminimumLevelBalance
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Small absolute intercepts exclude low native departures. The unit sibling
promotion preserves the immediate odd landing and its exact affine slope. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.NativeMarkedLeaves

open Collatz.MarkedCutoffFlux Collatz.PostminimumLevelBalance

private theorem weight_nonnegative (x : ℕ) : 0 ≤ weight x := by
  unfold weight
  positivity

private theorem weight_le_one (x : ℕ) : weight x ≤ 1 := by
  unfold weight
  apply (div_le_one (by positivity)).2
  linarith

private theorem survive_nonnegative (x n : ℕ) : 0 ≤ survive x n := by
  induction n generalizing x with
  | zero => simp [survive]
  | succ n ih => exact mul_nonneg (weight_nonnegative x) (ih (landing x))

private theorem survive_le_one (x n : ℕ) : survive x n ≤ 1 := by
  induction n generalizing x with
  | zero => simp [survive]
  | succ n ih =>
    calc
      survive x (n + 1) = weight x * survive (landing x) n := rfl
      _ ≤ weight x * 1 := mul_le_mul_of_nonneg_left (ih _) (weight_nonnegative _)
      _ ≤ 1 := by simpa using weight_le_one x

/-- Total survival never exceeds the factor at any one departed native site. -/
theorem survive_le_departure (x n j : ℕ) (hj : j < n) :
    survive x n ≤ weight (atDate x j) := by
  induction n generalizing x j with
  | zero => omega
  | succ n ih =>
    cases j with
    | zero =>
      simpa [survive, atDate] using
        mul_le_mul_of_nonneg_left (survive_le_one (landing x) n) (weight_nonnegative x)
    | succ j =>
      change weight x * survive (landing x) n ≤ weight (atDate (landing x) j)
      calc
        _ ≤ 1 * survive (landing x) n :=
          mul_le_mul_of_nonneg_right (weight_le_one x) (survive_nonnegative _ _)
        _ ≤ _ := by simpa using ih (landing x) j (by omega)

/-- A cap on the true endpoint times its survival loss excludes every departure
at or below the supplied floor, including on paths with repeated vertices. -/
theorem small_intercept_forces_high {x n j M : ℕ} {B : ℝ}
    (hj : j < n) (hB : 0 ≤ B)
    (cap : (atDate x n : ℝ) * (1 - survive x n) ≤ B)
    (margin : B * (3 * (M : ℝ) + 1) < atDate x n) : M < atDate x j := by
  by_contra h
  have hz : (atDate x j : ℝ) ≤ M := by exact_mod_cast Nat.le_of_not_gt h
  have hu := survive_le_departure x n j hj
  unfold weight at hu
  have pos : 0 < 3 * (atDate x j : ℝ) + 1 := by positivity
  have localBound := (le_div_iff₀ pos).mp hu
  have h1 : 1 ≤ (1 - survive x n) * (3 * (atDate x j : ℝ) + 1) := by
    linarith
  have h2 := mul_le_mul_of_nonneg_left h1 (show (0 : ℝ) ≤ atDate x n by positivity)
  have h3 := mul_le_mul_of_nonneg_right cap (le_of_lt pos)
  have h4 := mul_le_mul_of_nonneg_left (show 3 * (atDate x j : ℝ) + 1 ≤ 3 * (M : ℝ) + 1 by linarith) hB
  nlinarith only [h2, h3, h4, margin]

/-- Replacing a source by four times itself plus one changes the first native
valuation by two and gives exactly the same positive odd landing. -/
theorem promotion_landing (x : ℕ) : landing (4*x+1) = landing x := by
  unfold landing
  rw [show 3*(4*x+1)+1 = 2^2*(3*x+1) by omega]
  exact Nat.ordCompl_self_pow_mul _ _ Nat.prime_two

/-- At a nonunit the promoted source is a genuine odd ternary unit. -/
theorem promotion_unit {x : ℕ} (hx : x % 3 = 0) :
    (4*x+1) % 2 = 1 ∧ (4*x+1) % 3 = 1 ∧ x < 4*x+1 := by omega

/-- The two affine descriptions of the same endpoint have the precise
quarter-slope shift in the absolute intercept. -/
theorem promotion_intercept (x y : ℕ) (slope : ℝ) :
    (y : ℝ) - (slope/4) * (4*(x : ℝ)+1) =
      ((y : ℝ) - slope*x) - slope/4 := by ring

end Collatz.NativeMarkedLeaves
