import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Rat.Cast.Order

/-! Finite weighted subset counts. The prime-pivot and asymptotic
applications are written in HEIGHT_WEIGHTED_RANK.md. -/
set_option autoImplicit false
set_option warningAsError true

namespace WeightedMasks
open scoped BigOperators

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem count_subsets {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (masks : Finset (Finset ι)) (w : ι → R) (H : R)
    (inside : masks ⊆ s.powerset) (hH : 0 ≤ H)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (charge : ∀ t ∈ masks, 1 ≤ H * ∏ i ∈ t, w i) :
    (masks.card : R) ≤ H * ∏ i ∈ s, (1 + w i) := by
  have lower : (masks.card : R) ≤ ∑ t ∈ masks, H * ∏ i ∈ t, w i := by
    calc
      (masks.card : R) = ∑ _t ∈ masks, (1 : R) := by simp
      _ ≤ _ := Finset.sum_le_sum charge
  have upper : (∑ t ∈ masks, H * ∏ i ∈ t, w i) ≤
      ∑ t ∈ s.powerset, H * ∏ i ∈ t, w i := by
    apply Finset.sum_le_sum_of_subset_of_nonneg inside
    intro t ht _
    apply mul_nonneg hH
    apply Finset.prod_nonneg
    intro i hi
    exact hw i ((Finset.mem_powerset.mp ht) hi)
  calc
    (masks.card : R) ≤ ∑ t ∈ s.powerset, H * ∏ i ∈ t, w i := lower.trans upper
    _ = H * ∑ t ∈ s.powerset, ∏ i ∈ t, w i := (Finset.mul_sum _ _ _).symm
    _ = H * ∏ i ∈ s, (1 + w i) := by rw [Finset.prod_one_add]

theorem count_encoded {α ι : Type*} [DecidableEq α] [DecidableEq ι]
    (a : Finset α) (s : Finset ι) (code : α → Finset ι)
    (w : ι → R) (H : R)
    (injective : Set.InjOn code a)
    (inside : ∀ x ∈ a, code x ⊆ s)
    (hH : 0 ≤ H) (hw : ∀ i ∈ s, 0 ≤ w i)
    (charge : ∀ x ∈ a, 1 ≤ H * ∏ i ∈ code x, w i) :
    (a.card : R) ≤ H * ∏ i ∈ s, (1 + w i) := by
  have bound := count_subsets s (a.image code) w H
    (by
      intro t ht
      obtain ⟨x,hx,rfl⟩ := Finset.mem_image.mp ht
      exact Finset.mem_powerset.mpr (inside x hx)) hH hw
    (by
      intro t ht
      obtain ⟨x,hx,rfl⟩ := Finset.mem_image.mp ht
      exact charge x hx)
  simpa only [Finset.card_image_of_injOn injective] using bound

#print axioms count_subsets
#print axioms count_encoded
end WeightedMasks
