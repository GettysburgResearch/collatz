import FloorCounting
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite interfaces for the ordinary comparable-ancestor count. The
orbit-union decomposition, measure bounds, fusion estimate and passage to
growing windows are written or source-qualified arguments. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeComparableAncestors
open CoreBranching PeakRigidity FloorCounting
open scoped BigOperators

/-- Removing the exceptional sites costs at most their number once an
iterate is injective on the retained part. -/
theorem union_image_bound {α β : Type*} [DecidableEq α] [DecidableEq β]
    (I C D : Finset α) (f : α → β) (cover : C ⊆ I) (discard : D ⊆ C)
    (injective : Set.InjOn f ((C \ D : Finset α) : Set α)) :
    C.card ≤ (I.image f).card + D.card := by
  have subset : (C \ D).image f ⊆ I.image f :=
    Finset.image_subset_image (Finset.sdiff_subset.trans cover)
  have bound := Finset.card_le_card subset
  rw [Finset.card_image_of_injOn injective] at bound
  rw [← Finset.card_sdiff_add_card_eq_card discard]
  exact Nat.add_le_add_right bound D.card

/-- The physical terminal progression after a known parity word, with
one additional dyadic source bit to force an odd terminal and J extra
source digits at three. -/
theorem terminal_stride (A J r u : ℕ) :
    run A (r+2^(A+1)*(3^J*u)) =
      run A r + 2*3^(grade A r+J)*u ∧
    grade A (r+2^(A+1)*(3^J*u)) = grade A r := by
  obtain ⟨endpoint, parity⟩ := lift_prefix A 1 r (3^J*u)
  constructor
  · rw [endpoint, pow_add]
    ring
  · exact parity

/-- The exact endpoint-to-source density cancellation in (3). -/
theorem terminal_mass_identity (n A J : ℕ) (X : ℚ) :
    (3:ℚ)^J / (2*3^(n+J)) * (3^n / 2^A * X) = X/(2^(A+1)) := by
  rw [pow_add,pow_succ]
  field_simp

/-- The finite population of early pairs controls the number of marks
with multiplicity at least K. -/
theorem crowded_card {α : Type*} [DecidableEq α] (I : Finset α)
    (hits : α → ℕ) (K : ℕ) :
    (I.filter (fun y => K ≤ hits y)).card*K ≤ ∑ y ∈ I, hits y := by
  let F := I.filter (fun y => K ≤ hits y)
  have small : ∑ y ∈ F, K ≤ ∑ y ∈ F, hits y :=
    Finset.sum_le_sum (fun y h => (Finset.mem_filter.mp h).2)
  have large : ∑ y ∈ F, hits y ≤ ∑ y ∈ I, hits y :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
       (fun _ _ _ => Nat.zero_le _)
  simpa [F] using small.trans large

/-- Comparing a count on a fixed residue set across translations only
charges the labels that differ at that individual shift. -/
theorem shift_disagreement {α : Type*} [DecidableEq α] (S : Finset α)
    (f g : α → ℤ) (bad : Finset α) (hb : bad ⊆ S)
    (matched : ∀ x ∈ S \ bad, f x = g x)
    (cost : ∀ x ∈ bad, f x - g x ≤ 1) :
    (∑ x ∈ S, f x) - (∑ x ∈ S, g x) ≤ bad.card := by
  rw [← Finset.sum_sub_distrib, ← Finset.sum_sdiff hb]
  have hz : (∑ x ∈ S \ bad, (f x-g x))=0 :=
    Finset.sum_eq_zero (fun x hx => by rw [matched x hx]; omega)
  rw [hz, zero_add]
  calc
    ∑ x ∈ bad, (f x-g x) ≤ ∑ _x ∈ bad, (1:ℤ) := Finset.sum_le_sum cost
    _ = bad.card := by simp

theorem unit_anchor_failure :
    2*(3/4:ℚ)^82 + 49/8190 < 1/100 := by norm_num

#print axioms union_image_bound
#print axioms terminal_stride
#print axioms terminal_mass_identity
#print axioms crowded_card
#print axioms shift_disagreement
#print axioms unit_anchor_failure
end EscapeComparableAncestors

