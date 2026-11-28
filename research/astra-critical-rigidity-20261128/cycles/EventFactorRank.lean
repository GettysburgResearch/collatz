import Mathlib.Basic.Real.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Weighted prime-valuation vectors and the local rank obstruction at a common
point of the marked backward intervals. -/
set_option autoImplicit false
open scoped BigOperators
open Finset Module
namespace Collatz.EventFactorRank

private theorem capSum {ι : Type*} (s : Finset ι) (v : ι → ℝ) (a : ℝ)
    (ha : 0 ≤ a) (hv : ∀ i ∈ s, 0 ≤ v i) (h : a ≤ ∑ i ∈ s, v i) :
    a ≤ ∑ i ∈ s, min a (v i) := by
  classical
  by_cases hit : ∃ i ∈ s, a ≤ v i
  · obtain ⟨i, hi, hlarge⟩ := hit
    have one := single_le_sum (f := fun j => min a (v j))
      (fun j hj => le_min ha (hv j hj)) hi
    simpa only [min_eq_left hlarge] using one
  · have unchanged (i : ι) (hi : i ∈ s) : min a (v i) = v i := by
      exact min_eq_right (le_of_not_ge (fun he => hit ⟨i, hi, he⟩))
    rw [sum_congr rfl unchanged]
    exact h

/-- A family of nonnegative finite weighted valuation vectors is independent
when each row mass strictly dominates the sum of its pairwise overlaps. -/
theorem independent_of_overlap {ι κ : Type*} [Fintype ι] [Fintype κ]
    [DecidableEq ι] (v : ι → κ → ℝ) (hv : ∀ i k, 0 ≤ v i k)
    (dominates : ∀ i, (∑ j ∈ univ.erase i, ∑ k, min (v i k) (v j k)) < ∑ k, v i k) :
    LinearIndependent ℝ v := by
  classical
  apply Fintype.linearIndependent_iff.mpr
  intro coeff hzero i
  by_contra hbad
  obtain ⟨j, _, hmax⟩ := univ.exists_max_image (fun t => |coeff t|) ⟨i, mem_univ i⟩
  have hpos : 0 < |coeff j| := lt_of_lt_of_le (abs_pos.mpr hbad) (hmax i (mem_univ i))
  have remaining (k : κ) : v j k ≤ ∑ t ∈ univ.erase j, v t k := by
    have zero : (∑ t, coeff t * v t k) = 0 := by
      simpa only [sum_apply, Pi.smul_apply, smul_eq_mul, Pi.zero_apply] using congrFun hzero k
    have split := sum_erase_add (s := univ) (fun t => coeff t * v t k) (mem_univ j)
    have term : coeff j * v j k = -(∑ t ∈ univ.erase j, coeff t * v t k) := by
      linarith
    have mulBound : |coeff j| * v j k ≤ |coeff j| * ∑ t ∈ univ.erase j, v t k := by
      calc
        |coeff j| * v j k = |coeff j * v j k| := by rw [abs_mul, abs_of_nonneg (hv j k)]
        _ = |∑ t ∈ univ.erase j, coeff t * v t k| := by rw [term, abs_neg]
        _ ≤ ∑ t ∈ univ.erase j, |coeff t * v t k| := abs_sum_le_sum_abs _ _
        _ ≤ ∑ t ∈ univ.erase j, |coeff j| * v t k := by
          apply sum_le_sum
          intro t _
          rw [abs_mul, abs_of_nonneg (hv t k)]
          exact mul_le_mul_of_nonneg_right (hmax t (mem_univ t)) (hv t k)
        _ = _ := (mul_sum _ _ _).symm
    exact (mul_le_mul_iff_right₀ hpos).mp mulBound
  have mass : (∑ k, v j k) ≤ ∑ k, ∑ t ∈ univ.erase j, min (v j k) (v t k) := by
    apply sum_le_sum
    intro k _
    exact capSum _ _ _ (hv j k) (fun t _ => hv t k) (remaining k)
  rw [sum_comm] at mass
  exact (not_le_of_gt (dominates j)) mass

/-- Two endpoints looking backwards onto the same point have small separation
relative to either height. Distances use the lifted actual chronological cost. -/
theorem shared_point_gap (r : ℕ) (η Hi Hj ti tj : ℝ) (hη : 0 ≤ η)
    (hη1 : η ≤ 1) (ht : 0 ≤ ti) (order : ti ≤ tj)
    (hj : ((r : ℝ) + 2) * tj ≤ η * Hj)
    (lip : Hj - Hi ≤ tj - ti) :
    ((r : ℝ) + 1) * (tj - ti) ≤ η * Hi := by
  have a : 0 ≤ (r : ℝ) + 2 := by positivity
  have b : ((r : ℝ) + 2) * (tj - ti) ≤ ((r : ℝ) + 2) * tj :=
    mul_le_mul_of_nonneg_left (sub_le_self _ ht) a
  have c := mul_le_mul_of_nonneg_left lip hη
  have d := mul_le_mul_of_nonneg_right hη1 (sub_nonneg.mpr order)
  linarith

/-- In a common overlap of r+1 intervals the actual pair estimates require a
span of dimension at least r+1. The row coordinates carry the prime weights. -/
theorem common_overlap_rank {κ : Type*} [Fintype κ] (r : ℕ) (η : ℝ)
    (H t : Fin (r+1) → ℝ) (v : Fin (r+1) → κ → ℝ)
    (hη : 0 < η) (hη1 : η ≤ 1) (hH : ∀ i, 0 < H i)
    (ht : ∀ i, 0 ≤ t i) (radius : ∀ i, ((r : ℝ) + 2)*t i ≤ η*H i)
    (lip : ∀ i j, H j - H i ≤ |t j - t i|)
    (hv : ∀ i k, 0 ≤ v i k) (large : ∀ i, η*H i ≤ ∑ k, v i k)
    (pair : ∀ i j, i ≠ j → (∑ k, min (v i k) (v j k)) ≤ |t j - t i|) :
    r + 1 ≤ finrank ℝ (Submodule.span ℝ (Set.range v)) := by
  classical
  have ind : LinearIndependent ℝ v := by
    apply independent_of_overlap v hv
    intro i
    have den : 0 < (r : ℝ) + 1 := by positivity
    have cap (j : Fin (r+1)) (hji : j ∈ univ.erase i) :
        (∑ k, min (v i k) (v j k)) ≤ η * H i / ((r : ℝ) + 1) := by
      apply le_trans (pair i j (ne_of_mem_erase hji).symm)
      apply (le_div_iff₀ den).mpr
      rw [mul_comm]
      rcases le_total (t i) (t j) with h | h
      · rw [abs_of_nonneg (sub_nonneg.mpr h)]
        apply shared_point_gap r η (H i) (H j) (t i) (t j) hη.le hη1 (ht i) h (radius j)
        simpa only [abs_of_nonneg (sub_nonneg.mpr h)] using lip i j
      · rw [abs_of_nonpos (sub_nonpos.mpr h), neg_sub]
        have b : t i - t j ≤ t i := sub_le_self _ (ht j)
        have b' := mul_le_mul_of_nonneg_left b den.le
        have rad := radius i
        have non := ht i
        linarith
    calc
      (∑ j ∈ univ.erase i, ∑ k, min (v i k) (v j k)) ≤
          ∑ _j ∈ univ.erase i, η * H i / ((r : ℝ) + 1) := sum_le_sum cap
      _ = (r : ℝ) * (η * H i / ((r : ℝ) + 1)) := by
        simp [card_erase_of_mem, nsmul_eq_mul]
      _ < η * H i := by
        rw [← mul_div_assoc, div_lt_iff₀ den]
        nlinarith [mul_pos hη (hH i)]
      _ ≤ ∑ k, v i k := large i
  rw [finrank_span_eq_card ind, Fintype.card_fin]

end Collatz.EventFactorRank

#print axioms Collatz.EventFactorRank.independent_of_overlap
#print axioms Collatz.EventFactorRank.shared_point_gap
#print axioms Collatz.EventFactorRank.common_overlap_rank
