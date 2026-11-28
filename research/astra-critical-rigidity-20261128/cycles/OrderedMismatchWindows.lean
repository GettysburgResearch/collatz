import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace Collatz.OrderedMismatchWindows

open scoped BigOperators

private theorem sumAdjacent (f : ℕ → ℝ) (k n : ℕ) :
    (∑ i ∈ Finset.range n, (f (k+(i+1)) - f (k+i))) =
    f (k+n) - f k := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    ring

/-- The sum of all windows spanning k successive marked gaps is k whole laps,
    even if the endpoints wrap through the same physical mark several times. -/
theorem totalWindows (date : ℕ → ℝ) (s k : ℕ) (P : ℝ)
    (wrap : ∀ i, date (i+s) = date i + P) :
    (∑ i ∈ Finset.range s, (date (i+k) - date i)) = (k : ℝ) * P := by
  induction k with
  | zero => simp
  | succ k ih =>
    calc
      (∑ i ∈ Finset.range s, (date (i+(k+1)) - date i)) =
          ∑ i ∈ Finset.range s,
            ((date (i+k) - date i) + (date (k+(i+1)) - date (k+i))) := by
              apply Finset.sum_congr rfl
              intro i hi
              have h : i+(k+1)=k+(i+1) := by omega
              rw [h, Nat.add_comm i k]
              ring
      _ = (k : ℝ) * P + (date (k+s) - date k) := by
              rw [Finset.sum_add_distrib, ih, sumAdjacent]
      _ = ((k+1 : ℕ) : ℝ) * P := by rw [wrap]; push_cast; ring

theorem shiftedCosts (cost : ℕ → ℝ) (s k : ℕ)
    (wrap : ∀ i, cost (i+s) = cost i) :
    (∑ i ∈ Finset.range s, cost (i+k)) = ∑ i ∈ Finset.range s, cost i := by
  have h := totalWindows cost s k 0 (fun i => by simpa using wrap i)
  rw [Finset.sum_sub_distrib] at h
  linarith

/-- Sum open endpoint inequalities at the k-th next post-mismatch mark. -/
theorem clusteredWindowCosts (date high low : ℕ → ℝ) (s k : ℕ)
    (P rate penalty : ℝ)
    (dateWrap : ∀ i, date (i+s) = date i + P)
    (lowWrap : ∀ i, low (i+s) = low i)
    (bound : ∀ i < s, rate * (date (i+k) - date i) ≤ high i + low (i+k) + penalty) :
    rate * ((k : ℝ) * P) ≤
      (∑ i ∈ Finset.range s, (high i + low i)) + (s : ℝ) * penalty := by
  have h := Finset.sum_le_sum
    (s := Finset.range s) (fun i hi => bound i (Finset.mem_range.mp hi))
  rw [← Finset.mul_sum, totalWindows date s k P dateWrap] at h
  simp only [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul] at h
  rw [shiftedCosts low s k lowWrap] at h
  simpa only [Finset.sum_add_distrib] using h

#print axioms totalWindows
#print axioms shiftedCosts
#print axioms clusteredWindowCosts

end Collatz.OrderedMismatchWindows
