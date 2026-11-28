import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Card
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic

/-!
# Finite sparse sampling with exceptional windows

This module proves the finite double-counting inequality used in the
semiprime sampling argument. All short-interval supply, residue-class
upper bounds and quantitative Collatz fusion estimates remain explicit
external hypotheses in the written argument. No asymptotic theorem is
asserted here.
-/

namespace Collatz.SparseSampling

open Finset

variable {α β : Type*} [DecidableEq β]

def mass (w : α → β → ℕ) (s : Finset α) (t : Finset β) : ℕ :=
  ∑ x ∈ s, ∑ y ∈ t, w x y

/-- All incidences are either on a marked target or charged to the supplied
failure array. This retains the actual sparse-target incidences. -/
theorem mass_le_marked_add_failure
    (w e : α → β → ℕ) (s : Finset α) (t b : Finset β)
    (transfer : ∀ x ∈ s, ∀ y ∈ t, y ∉ b → w x y ≤ e x y) :
    mass w s t ≤ mass w s (t ∩ b) + mass e s t := by
  have hp : ∀ x ∈ s, ∀ y ∈ t,
      w x y ≤ (if y ∈ b then w x y else 0) + e x y := by
    intro x hx y hy
    by_cases h : y ∈ b
    · simp [h]
    · simpa [h] using transfer x hx y hy h
  calc
    mass w s t ≤ ∑ x ∈ s, ∑ y ∈ t,
        ((if y ∈ b then w x y else 0) + e x y) := by
      exact Finset.sum_le_sum (fun x hx => Finset.sum_le_sum (hp x hx))
    _ = mass w s (t ∩ b) + mass e s t := by
      simp only [Finset.sum_add_distrib, mass]
      congr 1
      apply Finset.sum_congr rfl
      intro x hx
      rw [← Finset.sum_filter]
      congr 1

variable [DecidableEq α]

/-- A lower incidence count in every nonexceptional marked source window,
an upper target multiplicity, and a charged failure array imply the finite
sparse sampling lower bound. -/
theorem sparse_sampling_budget
    (w e : α → β → ℕ) (s bad : Finset α) (t b : Finset β)
    (L H : ℕ)
    (row_lower : ∀ x ∈ s, x ∉ bad → L ≤ ∑ y ∈ t, w x y)
    (column_upper : ∀ y ∈ t ∩ b, (∑ x ∈ s, w x y) ≤ H)
    (transfer : ∀ x ∈ s, ∀ y ∈ t, y ∉ b → w x y ≤ e x y) :
    L * s.card ≤ H * (t ∩ b).card + L * (s ∩ bad).card + mass e s t := by
  have row : L * s.card ≤ mass w s t + L * (s ∩ bad).card := by
    have hp : ∀ x ∈ s,
        L ≤ (∑ y ∈ t, w x y) + if x ∈ bad then L else 0 := by
      intro x hx
      by_cases h : x ∈ bad
      · simp [h]
      · simpa [h] using row_lower x hx h
    have hs := Finset.sum_le_sum hp
    have hex : (∑ x ∈ s, if x ∈ bad then L else 0) =
        L * (s ∩ bad).card := by
      rw [← Finset.sum_filter]
      have heq : s.filter (fun x => x ∈ bad) = s ∩ bad := by
        ext x
        simp
      rw [heq]
      simp [Nat.mul_comm]
    simpa only [Finset.sum_add_distrib, Finset.sum_const,
      smul_eq_mul, Nat.mul_comm s.card L, hex, mass] using hs
  have columns : mass w s (t ∩ b) ≤ H * (t ∩ b).card := by
    unfold mass
    rw [Finset.sum_comm]
    calc
      (∑ y ∈ t ∩ b, ∑ x ∈ s, w x y) ≤ ∑ y ∈ t ∩ b, H :=
        Finset.sum_le_sum column_upper
      _ = H * (t ∩ b).card := by simp [Nat.mul_comm]
  have split := mass_le_marked_add_failure w e s t b transfer
  omega

/-- Aggregate exception and failure bounds may be inserted after the exact
finite count. No independence of the labels and sparse set is assumed. -/
theorem sparse_sampling_budget_of_bounds
    (w e : α → β → ℕ) (s bad : Finset α) (t b : Finset β)
    (L H E R : ℕ)
    (row_lower : ∀ x ∈ s, x ∉ bad → L ≤ ∑ y ∈ t, w x y)
    (column_upper : ∀ y ∈ t ∩ b, (∑ x ∈ s, w x y) ≤ H)
    (transfer : ∀ x ∈ s, ∀ y ∈ t, y ∉ b → w x y ≤ e x y)
    (exception_bound : (s ∩ bad).card ≤ E)
    (failure_bound : mass e s t ≤ R) :
    L * s.card ≤ H * (t ∩ b).card + L * E + R := by
  have h := sparse_sampling_budget w e s bad t b L H
    row_lower column_upper transfer
  have he := Nat.mul_le_mul_left L exception_bound
  omega

/-- Once two actual iterates meet, equal remaining dates retain equality. -/
theorem iterate_eq_of_meeting {γ : Type*} (F : γ → γ) (x y : γ)
    (t k : ℕ) (h : F^[t] x = F^[t] y) :
    F^[t + k] x = F^[t + k] y := by
  rw [Nat.add_comm t k, Function.iterate_add_apply, Function.iterate_add_apply, h]

/-- A common merger preserves every target visit by a later common
deadline, provided neither original source hit that target beforehand. -/
theorem visit_iff_after_meeting {γ : Type*} (F : γ → γ) (x y v : γ)
    (t L : ℕ) (h : F^[t] x = F^[t] y)
    (no_x : ∀ i < t, F^[i] x ≠ v)
    (no_y : ∀ i < t, F^[i] y ≠ v) :
    (∃ i ≤ L, F^[i] x = v) ↔ (∃ i ≤ L, F^[i] y = v) := by
  constructor
  · rintro ⟨i, hi, hv⟩
    have ht : t ≤ i := by
      by_contra hn
      exact no_x i (Nat.lt_of_not_ge hn) hv
    refine ⟨i, hi, ?_⟩
    have hm := iterate_eq_of_meeting F x y t (i - t) h
    rw [Nat.add_sub_of_le ht] at hm
    exact hm.symm.trans hv
  · rintro ⟨i, hi, hv⟩
    have ht : t ≤ i := by
      by_contra hn
      exact no_y i (Nat.lt_of_not_ge hn) hv
    refine ⟨i, hi, ?_⟩
    have hm := iterate_eq_of_meeting F x y t (i - t) h
    rw [Nat.add_sub_of_le ht] at hm
    exact hm.trans hv

end Collatz.SparseSampling
