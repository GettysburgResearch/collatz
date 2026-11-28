import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Ring.Rat
import Mathlib.Tactic.Linarith

/-! Exact accounting for a stored block with a strictly better choice on
one fine source cell above every coarse state. -/

namespace Collatz.AdaptiveBlockSaving

open scoped BigOperators

/-- One unit of pointwise savings on a named cell survives summation
against uniform fine-cell probabilities. -/
theorem strict_row {ι : Type*} [Fintype ι] [DecidableEq ι]
    (base pick : ι → ℚ) (cell : ι) (better : ∀ i, pick i ≤ base i)
    (strict : pick cell + 1 ≤ base cell) :
    (∑ i, pick i) + 1 ≤ ∑ i, base i := by
  have bound : ∀ i, pick i + (if i = cell then 1 else 0) ≤ base i := by
    intro i
    by_cases hi : i = cell
    · simpa [hi] using strict
    · simpa [hi] using better i
  simpa [Finset.sum_add_distrib] using
    (Finset.sum_le_sum (s := Finset.univ) (fun i _ => bound i))

/-- Terminal potentials cancel at a stationary coarse boundary, leaving
the same uniform saving in the true mean cost. `weight` is the number
of fine lifts per coarse state. -/
theorem stationary_bound {σ ι : Type*} [Fintype σ] [Fintype ι] [DecidableEq ι]
    (π V : σ → ℚ) (baseline cost : σ → ι → ℚ) (dst : σ → ι → σ)
    (w c : ℚ) (gate : σ → ι)
    (prob : ∑ s, π s = 1) (nonneg : ∀ s, 0 ≤ π s)
    (rows : ∀ s, (∑ i, baseline s i) ≤ w*(c+V s))
    (improve : ∀ s i, cost s i + V (dst s i) ≤ baseline s i)
    (strict : ∀ s, cost s (gate s) + V (dst s (gate s)) + 1 ≤ baseline s (gate s))
    (closed : (∑ s, π s * (∑ i, V (dst s i))) = ∑ s, π s * (w * V s)) :
    (∑ s, π s * (∑ i, cost s i)) + 1 ≤ w*c := by
  have row (s : σ) := (strict_row (baseline s) (fun i => cost s i + V (dst s i))
    (gate s) (improve s) (strict s)).trans (rows s)
  have aggregate := Finset.sum_le_sum (s := Finset.univ)
    (fun s _ => mul_le_mul_of_nonneg_left (row s) (nonneg s))
  simp only [Finset.sum_add_distrib, mul_add, mul_one, ← mul_assoc] at aggregate
  have hconst : (∑ s, π s * w * c) = w*c := by
    rw [← Finset.sum_mul, ← Finset.sum_mul, prob, one_mul]
  simp only [← mul_assoc] at closed
  linarith

end Collatz.AdaptiveBlockSaving
