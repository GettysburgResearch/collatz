import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith

namespace Collatz.DefectCover

def evalBits : List Bool → ℚ → ℚ
  | [], x => x
  | false :: w, x => evalBits w (x / 2)
  | true :: w, x => evalBits w ((3*x+1)/2)

/-- Odd steps budget a factor 3/2 for the translated coordinate x+1. -/
theorem translated_bound (w : List Bool) (x : ℚ) (hx : 0 ≤ x) :
    evalBits w x + 1 ≤ (3/2 : ℚ) ^ w.count true * (x+1) := by
  induction w generalizing x with
  | nil => simp [evalBits]
  | cons b w ih =>
    cases b with
    | false =>
      simp [evalBits]
      exact (ih _ (by linarith : 0 ≤ x/2)).trans
        (mul_le_mul_of_nonneg_left (by linarith) (by positivity))
    | true =>
      simp [evalBits, pow_succ]
      have h := ih _ (by linarith : 0 ≤ (3*x+1)/2)
      linarith

/-- Aggregation at a single marked boundary, expressed without division. -/
theorem aggregate (k : ℕ) (b : ℕ → ℚ) (eta q span d unit cost : ℚ)
    (he : 0 ≤ eta) (hd : 0 ≤ d) (hu : 0 ≤ unit)
    (hclose : eta*q = ∑ i ∈ Finset.range k, b i)
    (hterm : ∀ i < k, b i * unit ≤ cost)
    (hspan : span ≤ d*q) :
    eta*span*unit ≤ d*(k*cost) := by
  have hsum : (∑ i ∈ Finset.range k, b i) * unit ≤ k * cost := by
    rw [Finset.sum_mul]
    simpa using Finset.sum_le_sum (s := Finset.range k)
      (fun i hi => hterm i (Finset.mem_range.mp hi))
  rw [← hclose] at hsum
  calc
    eta * span * unit ≤ eta * (d*q) * unit :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hspan he) hu
    _ = d * (eta*q*unit) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left hsum hd

#print axioms translated_bound
#print axioms aggregate
end Collatz.DefectCover
