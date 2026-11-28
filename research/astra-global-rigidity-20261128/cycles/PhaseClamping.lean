import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

/-!
Finite kernels for the all-phase word comparison. The pressure limit,
Kingman theorem, rotation averaging and asymptotic word count are not
formalized here. In particular these results assert no Collatz convergence.
-/
namespace Collatz.PhaseClamping

open scoped BigOperators

def clamp (K b : ℕ → ℕ) (t : ℕ) : ℕ := min (K t) (b t)

theorem min_strict_step (a b c d : ℕ) (hab : a < b) (hcd : c < d) :
    min a c < min b d := by
  omega

theorem clamp_strict (K b : ℕ → ℕ) (hK : StrictMono K) (hb : StrictMono b) :
    StrictMono (clamp K b) := by
  intro i j hij
  exact min_strict_step _ _ _ _ (hK hij) (hb hij)

theorem clamp_below (K b : ℕ → ℕ) (t : ℕ) : clamp K b t ≤ b t := by
  exact min_le_right _ _

theorem clamp_start (K b : ℕ → ℕ) (hK : K 0 = 0) : clamp K b 0 = 0 := by
  simp [clamp, hK]

theorem clamp_endpoint (K b : ℕ → ℕ) (n : ℕ) (hn : b n ≤ K n) :
    clamp K b n = b n := by
  exact min_eq_right hn

theorem clamp_fibre_bit (x b : ℕ) (hx : x ≤ b + 1) :
    x = min x b ∨ (min x b = b ∧ x = b + 1) := by
  omega

theorem clamp_bit_injective (x y b : ℕ) (hx : x ≤ b + 1) (hy : y ≤ b + 1)
    (hmin : min x b = min y b) (hbit : (b < x) ↔ (b < y)) : x = y := by
  omega

theorem clamp_reward (a : ℚ) (x b : ℕ) (hx : x ≤ b + 1) :
    a * (2 : ℚ) ^ x = a * 2 ^ (min x b) +
        if b < x then a * 2 ^ b else 0 := by
  by_cases h : b < x
  · have heq : x = b + 1 := by omega
    have hmin : min x b = b := by omega
    rw [hmin, ite_eq_left h]
    rw [heq, pow_succ]
    ring
  · have hmin : min x b = x := by omega
    simp only [hmin, ite_eq_right h, add_zero]

theorem clamp_correction_bound (a : ℚ) (b : ℕ)
    (ha : 0 ≤ a) (hmax : a * (2 : ℚ) ^ (b + 1) ≤ 1) :
    0 ≤ a * 2 ^ b ∧ a * 2 ^ b ≤ 1 / 2 := by
  have hp : 0 ≤ (2 : ℚ) ^ b := pow_nonneg (by norm_num) _
  constructor
  · exact mul_nonneg ha hp
  · rw [pow_succ] at hmax
    linarith

theorem corrected_sum_bound (n : ℕ) (cost : Fin n → ℚ)
    (hc : ∀ i, 0 ≤ cost i ∧ cost i ≤ 1 / 2) :
    0 ≤ ∑ i, cost i ∧ ∑ i, cost i ≤ (n : ℚ) / 2 := by
  constructor
  · exact Finset.sum_nonneg (fun i _ => (hc i).1)
  · have h := Finset.sum_le_sum (s := Finset.univ) (fun i _ => (hc i).2)
    simpa [div_eq_mul_inv] using h

end Collatz.PhaseClamping
