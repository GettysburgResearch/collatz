import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic

/-!
Weighted finite collision transport with every decoding label retained.
The exact joint injection is an explicit premise. The infinite stationary
law, carry-moment estimates, and any universal Collatz conclusion are not
asserted here.
-/

namespace CollatzClosing.WeightedCollision

open scoped BigOperators

/-- Weighted Cauchy--Schwarz without square-root choices. -/
theorem weighted_sum_cauchy {I : Type*} (s : Finset I)
    (w L : I → ℝ) (hL : ∀ i ∈ s, 0 < L i) :
    (∑ i ∈ s, w i) ^ 2 ≤
      (∑ i ∈ s, (L i)⁻¹) * ∑ i ∈ s, L i * (w i) ^ 2 := by
  apply Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul s
  · intro i hi
    exact inv_nonneg.mpr (hL i hi).le
  · intro i hi
    exact mul_nonneg (hL i hi).le (sq_nonneg _)
  · intro i hi
    have hn : L i ≠ 0 := ne_of_gt (hL i hi)
    exact le_of_eq (by field_simp)

/-- If a label and a residue jointly determine every original object, then
the residue collision is bounded by a weighted square sum over all original
objects. Cross-label collisions are included in the left side. -/
theorem labelled_collision_bound
    {I B R : Type*} [Fintype I] [Fintype B] [Fintype R] [DecidableEq R]
    (box : I → B) (residue : I → R) (w : I → ℝ) (L : B → ℝ)
    (hL : ∀ b, 0 < L b)
    (hinj : Function.Injective (fun i => (box i, residue i))) :
    (∑ r, (∑ i ∈ Finset.univ.filter (fun i => residue i = r), w i) ^ 2) ≤
      (∑ b, (L b)⁻¹) * ∑ i, L (box i) * (w i) ^ 2 := by
  classical
  have hrow (r : R) :
      (∑ i ∈ Finset.univ.filter (fun i => residue i = r), w i) ^ 2 ≤
        (∑ b, (L b)⁻¹) *
          ∑ i ∈ Finset.univ.filter (fun i => residue i = r),
            L (box i) * (w i) ^ 2 := by
    let s := Finset.univ.filter (fun i => residue i = r)
    have hbox : ∀ i ∈ s, ∀ j ∈ s, box i = box j → i = j := by
      intro i hi j hj hij
      apply hinj
      apply Prod.ext hij
      exact (Finset.mem_filter.mp hi).2.trans (Finset.mem_filter.mp hj).2.symm
    have hinv : (∑ i ∈ s, (L (box i))⁻¹) ≤ ∑ b, (L b)⁻¹ := by
      calc
        (∑ i ∈ s, (L (box i))⁻¹) = ∑ b ∈ s.image box, (L b)⁻¹ := by
          symm
          apply Finset.sum_image
          exact hbox
        _ ≤ ∑ b, (L b)⁻¹ := by
          apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _)
          intro b _ _
          exact inv_nonneg.mpr (hL b).le
    exact (weighted_sum_cauchy s w (fun i => L (box i))
      (fun i _ => hL (box i))).trans
      (mul_le_mul_of_nonneg_right hinv
        (Finset.sum_nonneg (fun i _ => mul_nonneg (hL (box i)).le (sq_nonneg _))))
  calc
    _ ≤ ∑ r, (∑ b, (L b)⁻¹) *
        ∑ i ∈ Finset.univ.filter (fun i => residue i = r),
          L (box i) * (w i) ^ 2 := Finset.sum_le_sum (fun r _ => hrow r)
    _ = (∑ b, (L b)⁻¹) * ∑ i, L (box i) * (w i) ^ 2 := by
      rw [← Finset.mul_sum]
      congr 1
      simp only [Finset.sum_filter]
      rw [Finset.sum_comm]
      simp

/-- The complete quotient and endpoint residue recover the complete
nonnegative carry when the accumulated binary clock is retained. -/
theorem complete_carry_recovery (M A z C D : ℕ)
    (hquot : C / M = D / M)
    (hC : C % M = (2 ^ A * z) % M)
    (hD : D % M = (2 ^ A * z) % M) : C = D := by
  have hmod : C % M = D % M := hC.trans hD.symm
  have hc := Nat.mod_add_div C M
  have hd := Nat.mod_add_div D M
  rw [hmod, hquot] at hc
  exact hc.symm.trans hd

end CollatzClosing.WeightedCollision
