import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite critical side-branch flux for the ordinary odd Collatz map.
A single source weight at its prescribed clock can enter a side branch
on at most one date. The inequality holds with arbitrary finite sources. -/

namespace Collatz.Diagonal.CriticalSibling

def oddStep (x : ℕ) : ℕ := ordCompl[2] (3*x+1)
def sibling (x : ℕ) : ℕ := if x % 3 = 2 then 16*x+5 else 4*x+1

theorem sibling_unit (x : ℕ) : sibling x % 3 ≠ 0 := by
  unfold sibling
  split <;> omega

theorem sibling_gt (x : ℕ) : x < sibling x := by
  unfold sibling
  split <;> omega

theorem sibling_step (x : ℕ) : oddStep (sibling x) = oddStep x := by
  unfold oddStep sibling
  split
  · rw [show 3*(16*x+5)+1 = 2^4*(3*x+1) by ring]
    exact Nat.ordCompl_self_pow_mul _ _ Nat.prime_two
  · rw [show 3*(4*x+1)+1 = 2^2*(3*x+1) by ring]
    exact Nat.ordCompl_self_pow_mul _ _ Nat.prime_two

def row (V : Finset ℕ) (w : ℕ → ℚ) (j y : ℕ) : ℚ :=
  ∑ x ∈ V, if oddStep^[j] x = y then w x else 0

/-- Two true parents give disjoint terms in the next physical row. -/
theorem row_side_step (V : Finset ℕ) (w : ℕ → ℚ) (hw : ∀ x ∈ V, 0 ≤ w x)
    (j y : ℕ) :
    row V w j y + row V w j (sibling y) ≤ row V w (j+1) (oddStep y) := by
  unfold row
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro x hx
  by_cases h₁ : oddStep^[j] x = y
  · have h₂ : oddStep^[j] x ≠ sibling y := by rw [h₁]; exact (sibling_gt y).ne
    simp [Function.iterate_succ_apply', h₁, (sibling_gt y).ne]
  · by_cases h₂ : oddStep^[j] x = sibling y
    · simp [Function.iterate_succ_apply', h₂, sibling_step, (sibling_gt y).ne']
    · simp only [ite_eq_right_iff.mpr (fun h => (h₁ h).elim), ite_eq_right_iff.mpr (fun h => (h₂ h).elim), zero_add]
      split <;> simp [hw x hx]

/-- The cumulative side mass is spent from one original finite measure. -/
theorem side_budget (V : Finset ℕ) (w : ℕ → ℚ) (hw : ∀ x ∈ V, 0 ≤ w x)
    (a N : ℕ) :
    row V w 0 a + ∑ j ∈ Finset.range N, row V w j (sibling (oddStep^[j] a))
      ≤ row V w N (oddStep^[N] a) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Finset.sum_range_succ, ← add_assoc, Function.iterate_succ_apply']
    exact (add_le_add_left ih _).trans (row_side_step V w hw N (oddStep^[N] a))

theorem side_budget_total (V : Finset ℕ) (w : ℕ → ℚ) (hw : ∀ x ∈ V, 0 ≤ w x)
    (a N : ℕ) :
    row V w 0 a + ∑ j ∈ Finset.range N, row V w j (sibling (oddStep^[j] a))
      ≤ ∑ x ∈ V, w x := by
  apply (side_budget V w hw a N).trans
  unfold row
  apply Finset.sum_le_sum
  intro x hx
  split
  · exact le_rfl
  · exact hw x hx

end Collatz.Diagonal.CriticalSibling
