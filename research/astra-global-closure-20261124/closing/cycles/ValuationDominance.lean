import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Data.Int.Order.Basic

/-! The valuation argument for a largest coefficient in an integral relation. -/
set_option autoImplicit false
namespace Collatz.ValuationDominance

/-- A relation at a prime forces the valuation of the maximal-coefficient
entry to be covered by the other entries' absolute valuations. -/
theorem relation_cover {ι : Type*} (s : Finset ι) (e v : ι → Int) (j : ι)
    (nonzero : e j ≠ 0) (largest : ∀ i ∈ s, |e i| ≤ |e j|)
    (relation : e j*v j = -(∑ i ∈ s, e i*v i)) :
    |v j| ≤ ∑ i ∈ s, |v i| := by
  have h : |e j| * |v j| ≤ |e j| * ∑ i ∈ s, |v i| := by
    calc
      |e j| * |v j| = |∑ i ∈ s, e i*v i| := by rw [← abs_mul, relation, abs_neg]
      _ ≤ ∑ i ∈ s, |e i*v i| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i ∈ s, |e j| * |v i| := by
        apply Finset.sum_le_sum
        intro i hi
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_right (largest i hi) (abs_nonneg _)
      _ = _ := (Finset.mul_sum ..).symm
  exact (mul_le_mul_iff_right₀ (abs_pos.mpr nonzero)).mp h

/-- Truncating competing valuations at the target exponent preserves a
cover. This is the prime-by-prime transition from absolute values to gcds. -/
theorem truncated_cover {ι : Type*} (s : Finset ι) (u : ι → Int) (w : Int)
    (hw : 0 ≤ w) (hu : ∀ i ∈ s, 0 ≤ u i) (cover : w ≤ ∑ i ∈ s, u i) :
    w ≤ ∑ i ∈ s, min w (u i) := by
  by_cases h : ∃ i ∈ s, w ≤ u i
  · obtain ⟨i, hi, hwi⟩ := h
    calc
      w = min w (u i) := (min_eq_left hwi).symm
      _ ≤ _ := Finset.single_le_sum (f := fun i => min w (u i))
        (fun k hk => le_min hw (hu k hk)) hi
  · apply le_trans cover
    exact Finset.sum_le_sum (fun i hi => le_min (le_of_not_ge (fun hwi => h ⟨i, hi, hwi⟩)) le_rfl)

#print axioms relation_cover
#print axioms truncated_cover
end Collatz.ValuationDominance
