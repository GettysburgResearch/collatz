import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-! Finite algebra of the folded chronological cuts on a reduced rank clock. -/
namespace Collatz.InfiniteDescent.FoldedCuts
open scoped BigOperators

variable {ι : Type*} [Fintype ι]

/-- A rank displacement has a signed inverse transfer, including any seam weight. -/
theorem weighted_difference (shift : Equiv.Perm ι) (c w seam : ι → ℚ) :
    (∑ r, (2 * c r - seam (shift.symm r) * c (shift.symm r)) * w r) =
      ∑ r, c r * (2 * w r - seam r * w (shift r)) := by
  have reorder :
      (∑ r, seam (shift.symm r) * c (shift.symm r) * w r) =
        ∑ r, seam r * c r * w (shift r) := by
    simpa using (Equiv.sum_comp shift (fun r => seam (shift.symm r) * c (shift.symm r) * w r)).symm
  simp only [sub_mul, mul_sub, Finset.sum_sub_distrib]
  rw [reorder]
  congr 1 <;> apply Finset.sum_congr rfl <;> intro r hr <;> ring

/-- Positive transfer differences at the individual ranks force a positive
chronological lift even if its original signed drift coefficients cancel. -/
theorem positive_cut [Nonempty ι] (shift : Equiv.Perm ι) (c w seam : ι → ℚ)
    (hc : ∀ r, 0 < c r) (hs : ∀ r, seam r * w (shift r) < 2 * w r) :
    0 < ∑ r, (2 * c r - seam (shift.symm r) * c (shift.symm r)) * w r := by
  rw [weighted_difference]
  exact Finset.sum_pos (fun r _ => mul_pos (hc r) (sub_pos.mpr (hs r))) Finset.univ_nonempty

/-- A fixed rank sees every lag exactly once as the chronological cut moves. -/
theorem cut_sum (lags : ι → Equiv.Perm ι) (coeff tilt : ι → ℚ) :
    (∑ j, ∑ r, coeff r * tilt (lags r j)) = (∑ r, coeff r) * ∑ t, tilt t := by
  rw [Finset.sum_comm, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro r _
  rw [← Finset.mul_sum, Equiv.sum_comp (lags r)]

/-- A positive average bounds the number of possibly vanishing individual lifts. -/
theorem average_support_budget [DecidableEq ι] (value : ι → ℚ) (baseline bound : ℚ)
    (average : (Fintype.card ι : ℚ) * baseline ≤ ∑ j, value j)
    (upper : ∀ j, value j ≤ bound) :
    (Fintype.card ι : ℚ) * baseline ≤
      ((Finset.univ.filter fun j => value j ≠ 0).card : ℚ) * bound := by
  let support := Finset.univ.filter fun j => value j ≠ 0
  have keep : (∑ j, value j) = ∑ j ∈ support, value j := by
    symm
    apply Finset.sum_subset (Finset.filter_subset _ _)
    intro j hj h
    by_contra hn
    exact h (Finset.mem_filter.mpr ⟨hj, hn⟩)
  calc
    _ ≤ ∑ j, value j := average
    _ = ∑ j ∈ support, value j := keep
    _ ≤ ∑ _j ∈ support, bound := Finset.sum_le_sum fun j _ => upper j
    _ = _ := by simp [support]

/-- Actual odd recurrences multiplied by compatible dyadic rank weights give
a closed recurrence for the sum over visits; no equality between the visits
or independence of their weights is assumed. -/
theorem physical_sum (before after odds next divisor : ι → ℚ) (mechanical : ℚ)
    (edge : ∀ j, divisor j * next j = 3 * odds j + 1)
    (weights : ∀ j, mechanical * after j = before j * divisor j) :
    mechanical * (∑ j, after j * next j) =
      3 * (∑ j, before j * odds j) + ∑ j, before j := by
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  calc
    mechanical * (after j * next j) = mechanical * after j * next j := by ring
    _ = before j * (divisor j * next j) := by rw [weights]; ring
    _ = 3 * (before j * odds j) + before j := by rw [edge]; ring

#print axioms weighted_difference
#print axioms positive_cut
#print axioms cut_sum
#print axioms average_support_budget
#print axioms physical_sum

end Collatz.InfiniteDescent.FoldedCuts
