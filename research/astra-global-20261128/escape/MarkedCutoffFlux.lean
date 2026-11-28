import MarkedCutoffArithmetic
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Finite harmonic transport for any admissible nonnegative row norm. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.MarkedCutoffFlux
variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def carry (x : ℕ) (a : K) : K := 3 * a / (3 * (x : K) + 1)
def stopped (x : ℕ) (a : K) : K := a / ((x : K) * (3 * x + 1))

/-- The harmonic incoming weight uses the actual division clock and landing. -/
theorem physical_carry (x : ℕ) (a : K) :
    3 * a / ((2 : K) ^ gap x * landing x) = carry x a := by
  have edge : (2 : K) ^ gap x * landing x = 3 * x + 1 := by
    exact_mod_cast native_edge x
  simp only [edge, carry]

theorem edge_depletion (x : ℕ) (hx : 0 < x) (a : K) :
    carry x a + stopped x a = a / x := by
  have pos : (0 : K) < x := by exact_mod_cast hx
  have denom : (3 * (x : K) + 1) ≠ 0 := by positivity
  unfold carry stopped
  field_simp [ne_of_gt pos, denom]

private theorem carry_nonneg (x : ℕ) (a : K) (ha : 0 ≤ a) : 0 ≤ carry x a := by
  unfold carry
  positivity

/-- Each interior source is charged at most once, also when its landing is
outside the retained set. The supplied exterior contribution is separate. -/
theorem finite_cutoff_flux (inside targets : Finset ℕ) (f g influx : ℕ → K)
    (positive : ∀ x ∈ inside, 0 < x)
    (nonneg : ∀ x ∈ inside, 0 ≤ f x)
    (rows : ∀ z ∈ targets, g z / z ≤
      (∑ x ∈ inside, if z = landing x then carry x (f x) else 0) + influx z) :
    (∑ z ∈ targets, g z / z) + (∑ x ∈ inside, stopped x (f x)) ≤
      (∑ x ∈ inside, f x / x) + ∑ z ∈ targets, influx z := by
  have allRows := Finset.sum_le_sum rows
  rw [Finset.sum_add_distrib] at allRows
  have once :
      (∑ z ∈ targets, ∑ x ∈ inside, if z = landing x then carry x (f x) else 0) ≤
        ∑ x ∈ inside, carry x (f x) := by
    rw [Finset.sum_comm]
    apply Finset.sum_le_sum
    intro x hx
    by_cases h : landing x ∈ targets
    · simp [h]
    · simp [h, carry_nonneg x (f x) (nonneg x hx)]
  have split :
      (∑ x ∈ inside, carry x (f x)) + (∑ x ∈ inside, stopped x (f x)) =
        ∑ x ∈ inside, f x / x := by
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun x hx => edge_depletion x (positive x hx) (f x))
  linarith only [allRows, once, split]

/-- Bounded cumulative stopped variation on every physical grade horizon. -/
theorem telescope_budget (reserve loss influx : ℕ → K)
    (step : ∀ d, reserve (d + 1) + loss d ≤ reserve d + influx d) (H : ℕ) :
    reserve H + (∑ d ∈ Finset.range H, loss d) ≤
      reserve 0 + ∑ d ∈ Finset.range H, influx d := by
  induction H with
  | zero => simp
  | succ H ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    linarith only [ih, step H]

end Collatz.MarkedCutoffFlux
