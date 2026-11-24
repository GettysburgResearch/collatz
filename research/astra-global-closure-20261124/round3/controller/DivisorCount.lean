import Mathlib.NumberTheory.Divisors
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! Finite source counting for an exact affine word.  The parameters may
depend on a word and on a chosen row.  The asymptotic divisor bound is not
an assumption or conclusion of these finite declarations. -/
set_option autoImplicit false
namespace Collatz.FixedWordCount

/-- On one fixed affine word, an endpoint divisor determines at most one
original source.  No random or independently resampled endpoint is used. -/
theorem source_divisor_bound (S : Finset Nat) (q : Nat → Nat)
    (D B C P : Nat) (hB : 0 < B) (hP : P ≠ 0)
    (edge : ∀ x ∈ S, D * q x = B * x + C)
    (divisor : ∀ x ∈ S, q x ∣ P) :
    S.card ≤ P.divisors.card := by
  apply Finset.card_le_card_of_injOn q
  · intro x hx
    exact Nat.mem_divisors.mpr ⟨divisor x hx, hP⟩
  · intro x hx y hy hxy
    have eq : B * x + C = B * y + C := by
      rw [← edge x hx, ← edge y hy, hxy]
    exact Nat.eq_of_mul_eq_mul_left hB (Nat.add_right_cancel eq)

/-- Word/row choices may depend on the original source.  Taking their
finite union charges every such choice with its actual divisor count. -/
theorem source_divisor_cover {ι : Type*} [DecidableEq ι]
    (I : Finset ι) (S : Finset Nat) (q : ι → Nat → Nat)
    (D B C P : ι → Nat)
    (positive : ∀ i ∈ I, 0 < B i ∧ P i ≠ 0)
    (cover : ∀ x ∈ S, ∃ i ∈ I,
      D i * q i x = B i * x + C i ∧ q i x ∣ P i) :
    S.card ≤ ∑ i ∈ I, (P i).divisors.card := by
  classical
  let F : ι → Finset Nat := fun i =>
    S.filter (fun x => D i * q i x = B i * x + C i ∧ q i x ∣ P i)
  have subset : S ⊆ I.biUnion F := by
    intro x hx
    obtain ⟨i, hi, hedge, hdiv⟩ := cover x hx
    exact Finset.mem_biUnion.mpr ⟨i, hi, Finset.mem_filter.mpr ⟨hx, hedge, hdiv⟩⟩
  calc
    S.card ≤ (I.biUnion F).card := Finset.card_le_card subset
    _ ≤ ∑ i ∈ I, (F i).card := Finset.card_biUnion_le
    _ ≤ ∑ i ∈ I, (P i).divisors.card := by
      apply Finset.sum_le_sum
      intro i hi
      apply source_divisor_bound (F i) (q i) (D i) (B i) (C i) (P i)
        (positive i hi).1 (positive i hi).2
      · intro x hx
        exact (Finset.mem_filter.mp hx).2.1
      · intro x hx
        exact (Finset.mem_filter.mp hx).2.2

#print axioms source_divisor_bound
#print axioms source_divisor_cover
end Collatz.FixedWordCount
