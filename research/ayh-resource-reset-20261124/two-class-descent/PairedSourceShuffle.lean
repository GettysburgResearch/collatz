import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Max
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic

/-! Finite original-source bounds. The record function may contain the full
ordered pair of Collatz futures. These estimates do not assume a law for it. -/
namespace CollatzShell.PairedSourceShuffle

open Finset

/-- At most k sources have fewer than k strict predecessors in their fiber. -/
theorem lower_fringe (S : Finset Nat) (k : Nat) :
    (S.filter fun x => (S.filter fun y => y < x).card < k).card ≤ k := by
  let U := S.filter fun x => (S.filter fun y => y < x).card < k
  change U.card ≤ k
  by_cases h : U.Nonempty
  · let m := U.max' h
    have hm : m ∈ U := U.max'_mem h
    have hsmall := (mem_filter.mp hm).2
    have hsub : U ⊆ insert m (S.filter fun y => y < m) := by
      intro x hx
      by_cases he : x = m
      · simp [he]
      · exact mem_insert_of_mem (mem_filter.mpr
          ⟨(mem_filter.mp hx).1, lt_of_le_of_ne (U.le_max' x hx) he⟩)
    exact (card_le_card hsub).trans ((card_insert_le _ _).trans hsmall)
  · simp [Finset.not_nonempty_iff_eq_empty.mp h]

/-- At most k sources have fewer than k strict successors in their fiber. -/
theorem upper_fringe (S : Finset Nat) (k : Nat) :
    (S.filter fun x => (S.filter fun y => x < y).card < k).card ≤ k := by
  let U := S.filter fun x => (S.filter fun y => x < y).card < k
  change U.card ≤ k
  by_cases h : U.Nonempty
  · let m := U.min' h
    have hm : m ∈ U := U.min'_mem h
    have hsmall := (mem_filter.mp hm).2
    have hsub : U ⊆ insert m (S.filter fun y => m < y) := by
      intro x hx
      by_cases he : x = m
      · simp [he]
      · exact mem_insert_of_mem (mem_filter.mpr
          ⟨(mem_filter.mp hx).1, lt_of_le_of_ne (U.min'_le x hx) (Ne.symm he)⟩)
    exact (card_le_card hsub).trans ((card_insert_le _ _).trans hsmall)
  · simp [Finset.not_nonempty_iff_eq_empty.mp h]

/-- The number of origins lost by two-sided trimming is at most 2k per
realized good record, independently of its probability. -/
theorem total_fringe {α : Type*} [DecidableEq α] (S : Finset Nat) (record : Nat → α)
    (k : Nat) :
    let fiber := fun a => S.filter fun x => record x = a
    let fringe := fun a =>
      ((fiber a).filter fun x => ((fiber a).filter fun y => y < x).card < k) ∪
      ((fiber a).filter fun x => ((fiber a).filter fun y => x < y).card < k)
    ((S.image record).biUnion fringe).card ≤ (S.image record).card * (2*k) := by
  dsimp only
  refine Finset.card_biUnion_le.trans ?_
  calc
    _ ≤ ∑ _a ∈ S.image record, (2*k) := by
      apply Finset.sum_le_sum
      intro a _
      exact (Finset.card_union_le _ _).trans (by
        have hl := lower_fringe (S.filter fun x => record x = a) k
        have hu := upper_fringe (S.filter fun x => record x = a) k
        omega)
    _ = _ := by simp

private theorem one_residue (S : Finset Nat) (lo D q c : Nat)
    (hspan : ∀ x ∈ S, lo ≤ x ∧ x ≤ lo+D) :
    (S.filter fun x => x%q=c).card ≤ 1+D/q := by
  let V := S.filter fun x => x%q=c
  change V.card ≤ 1+D/q
  by_cases h : V.Nonempty
  · let m := V.min' h
    have hm : m ∈ V := V.min'_mem h
    let index := fun x : Nat => (x-m)/q
    have hrepr (x : Nat) (hx : x ∈ V) : m+q*index x=x := by
      have hmle : m ≤ x := V.min'_le x hx
      have hmod : m ≡ x [MOD q] := (mem_filter.mp hm).2.trans (mem_filter.mp hx).2.symm
      have hd := (Nat.modEq_iff_dvd' hmle).mp hmod
      dsimp [index]
      rw [Nat.mul_div_cancel' hd]
      omega
    have hmap : Set.MapsTo index V (Finset.range (D/q+1)) := by
      intro x hx
      have hl := (hspan m (mem_filter.mp hm).1).1
      have hu := (hspan x (mem_filter.mp hx).1).2
      have hd : x-m ≤ D := by omega
      exact Finset.mem_range.mpr (Nat.lt_succ_of_le (Nat.div_le_div_right hd))
    have hinj : Set.InjOn index V := by
      intro x hx y hy hxy
      rw [← hrepr x hx, ← hrepr y hy, hxy]
    simpa [Nat.add_comm] using Finset.card_le_card_of_injOn index hmap hinj
  · simp [Finset.not_nonempty_iff_eq_empty.mp h]

/-- Conditional sparse-test numerator on a fixed fiber of diameter at most D.
The forbidden residue list E may be selected after seeing the whole fiber. -/
theorem sparse_residue_test (S E : Finset Nat) (lo D q : Nat)
    (hspan : ∀ x ∈ S, lo ≤ x ∧ x ≤ lo+D) :
    (S.filter fun x => x%q ∈ E).card ≤ E.card*(1+D/q) := by
  rw [← Finset.sum_card_fiberwise_eq_card_filter S E (fun x => x%q)]
  calc
    _ ≤ ∑ _c ∈ E, (1+D/q) := by
      exact Finset.sum_le_sum fun c _ => one_residue S lo D q c hspan
    _ = _ := by simp

end CollatzShell.PairedSourceShuffle
