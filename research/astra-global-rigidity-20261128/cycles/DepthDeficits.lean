import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Lean.Elab.Tactic.Omega

/-!
Finite loss bounds for the exact valuation-depth model. These statements
do not formalize a pressure limit, irrational rotation, or a count-rate
asymptotic. The positive-block entry has a stronger cost than later sites.
-/
namespace Collatz.DepthDeficits

open scoped BigOperators

def loss (a : ℚ) (j : ℕ) : ℚ := a * (1 - (1 / 2 : ℚ) ^ j)

theorem zero_loss (a : ℚ) : loss a 0 = 0 := by
  simp [loss]

theorem half_power_bound (j : ℕ) (hj : 0 < j) :
    (1 / 2 : ℚ) ^ j ≤ 1 / 2 := by
  obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hj)
  rw [hk, pow_succ]
  have h : (1 / 2 : ℚ) ^ k ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  linarith

theorem positive_site_loss (a : ℚ) (j : ℕ)
    (ha : 1 / 2 ≤ a) (hj : 0 < j) : 1 / 4 ≤ loss a j := by
  have hp := half_power_bound j hj
  unfold loss
  nlinarith

theorem positive_entry (j g : ℕ) (hg : g ≤ 2)
    (hstep : j + 1 ≤ g) (hj : 0 < j) : g = 2 ∧ j = 1 := by
  omega

theorem entry_loss (aBefore aAfter : ℚ)
    (ha : 1 / 2 ≤ aBefore) (hstep : 3 * aAfter = 4 * aBefore) :
    1 / 3 ≤ loss aAfter 1 := by
  norm_num [loss]
  linarith

theorem block_loss (n : ℕ) (cost : Fin (n + 1) → ℚ)
    (first : 1 / 3 ≤ cost 0)
    (later : ∀ i : Fin n, 1 / 4 ≤ cost i.succ) :
    3 * ((n : ℚ) + 1) + 1 ≤ 12 * ∑ i, cost i := by
  have hsum : (n : ℚ) / 4 ≤ ∑ i : Fin n, cost i.succ := by
    have h := Finset.sum_le_sum (s := Finset.univ) (fun i _ => later i)
    simpa [div_eq_mul_inv] using h
  rw [Fin.sum_univ_succ]
  linarith

end Collatz.DepthDeficits
