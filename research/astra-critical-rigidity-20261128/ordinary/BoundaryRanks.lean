import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic.Ring

/-! Summation by parts for actual finite-dimensional prefix and suffix spaces.
The initial and terminal pair dimensions are allowed to differ. -/
set_option autoImplicit false
open scoped BigOperators
open Finset Module
namespace Collatz.BoundaryRanks

/-- The two-sided cut identity for integer-valued date and dimension functions. -/
private theorem discrete_parts (dates cuts : ℕ → ℤ) (k : ℕ) :
    (∑ i ∈ range k, dates (i+1) * (cuts (i+1)-cuts i)) =
    dates k * cuts k - dates 0 * cuts 0 -
      ∑ i ∈ range k, (dates (i+1)-dates i) * cuts i := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, sum_range_succ, ih]
    ring

/-- When opposite-end spans generate the whole ambient space, their two signed
rank increments add to the increment of the dimension of their intersection. -/
private theorem rank_increment {K V : Type*} [DivisionRing K] [AddCommGroup V]
    [Module K V] [FiniteDimensional K V]
    (P S P' S' : Submodule K V) (h : P ⊔ S = ⊤) (h' : P' ⊔ S' = ⊤) :
    ((finrank K P' : ℤ) - finrank K P) - (finrank K S - finrank K S' : ℤ) =
      (finrank K ↥(P' ⊓ S') : ℤ) - finrank K ↥(P ⊓ S) := by
  have h₁ := Submodule.finrank_sup_add_finrank_inf_eq P S
  have h₂ := Submodule.finrank_sup_add_finrank_inf_eq P' S'
  rw [h, finrank_top] at h₁
  rw [h', finrank_top] at h₂
  omega

/-- The physical partial directions give a lower bound for an actual
intersection whenever they are independent in the stabilized coefficient field. -/
theorem shared_directions_bound {K V : Type*} [DivisionRing K] [AddCommGroup V]
    [Module K V] [FiniteDimensional K V] (P S : Submodule K V) (d : ℕ)
    (directions : Fin d → V) (ind : LinearIndependent K directions)
    (pre : ∀ i, directions i ∈ P) (post : ∀ i, directions i ∈ S) :
    d ≤ finrank K ↥(P ⊓ S) := by
  have inside : Submodule.span K (Set.range directions) ≤ P ⊓ S := by
    apply Submodule.span_le.mpr
    rintro _ ⟨i,rfl⟩
    exact ⟨pre i, post i⟩
  have size := Submodule.finrank_mono inside
  simpa only [finrank_span_eq_card ind,Fintype.card_fin] using size

/-- The calendar-weighted prefix/suffix selection identity with arbitrary
boundary ranks. With nested greedy spans, the signed increments below are the
differences of their selected-carry indicators. -/
theorem chronological_rank_identity {K V : Type*} [DivisionRing K] [AddCommGroup V]
    [Module K V] [FiniteDimensional K V]
    (P S : ℕ → Submodule K V) (t : ℕ → ℤ) (k : ℕ)
    (ht : t 0=0) (complete : ∀ i≤k, P i ⊔ S i = ⊤) (last : P k=⊤)
    (reference : ℤ) :
    (∑ i ∈ range k, t (i+1) *
      (((finrank K (P (i+1)) : ℤ) - finrank K (P i)) -
       ((finrank K (S i) : ℤ) - finrank K (S (i+1))))) =
      ((finrank K (S k) : ℤ)-reference) * t k +
      ∑ i ∈ range k, (t (i+1)-t i) * (reference-finrank K ↥(P i ⊓ S i)) := by
  let c : ℕ → ℤ := fun i => finrank K ↥(P i ⊓ S i)
  have increments (i : ℕ) (hi:i∈range k) :
      ((finrank K (P (i+1)) : ℤ)-finrank K (P i)) -
      ((finrank K (S i) : ℤ)-finrank K (S (i+1))) = c (i+1)-c i :=
    rank_increment _ _ _ _ (complete i (by have := mem_range.mp hi; omega))
      (complete (i+1) (by have := mem_range.mp hi; omega))
  have repr : (∑ i ∈ range k, t (i+1) *
      (((finrank K (P (i+1)) : ℤ)-finrank K (P i)) -
       ((finrank K (S i) : ℤ)-finrank K (S (i+1))))) =
      ∑ i ∈ range k, t (i+1)*(c (i+1)-c i) :=
    sum_congr rfl (fun i hi => congrArg _ (increments i hi))
  have clock : (∑ i ∈ range k, (t (i+1)-t i)) = t k := by
    have eq := discrete_parts t (fun _ => (1 : ℤ)) k
    simp [ht] at eq
    rw [sum_sub_distrib]
    omega
  have ck : c k = finrank K (S k) := by
    change (finrank K ↥(P k ⊓ S k) : ℤ) = _
    rw [last, top_inf_eq]
  rw [repr, discrete_parts, ht, ck]
  change _ = _ + ∑ i ∈ range k, (t (i+1)-t i)*(reference-c i)
  simp_rw [mul_sub]
  rw [sum_sub_distrib, ←sum_mul, clock]
  ring

end Collatz.BoundaryRanks
