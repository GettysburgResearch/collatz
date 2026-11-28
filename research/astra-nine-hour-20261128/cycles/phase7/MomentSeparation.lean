import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Fintype.BigOperators

/-! Sign separation for the leading terms of genuine Syracuse path moments. -/

namespace Collatz.MomentSeparation

/-- If both a strictly contracting and strictly expanding multiplier are
available at each date, a linear combination of adjacent homogeneous moment
increments cannot be nonnegative on every word unless every coefficient
vanishes. The preceding positive weight can depend on the entire word. -/
theorem all_words_nonnegative {I : Type*} [Fintype I] (c : I → ℝ)
    (weight : (I → Bool) → I → ℝ) (positive : ∀ w i, 0 < weight w i)
    {lo hi : ℝ} (contract : lo < 1) (expand : 1 < hi)
    (h : ∀ w : I → Bool, 0 ≤ ∑ i, c i * weight w i * ((if w i then hi else lo)-1)) :
    ∀ i, c i = 0 := by
  classical
  let w : I → Bool := fun i => decide (c i < 0)
  let f : I → ℝ := fun i => c i * weight w i * ((if w i then hi else lo) - 1)
  have nonpositive (i : I) : f i ≤ 0 := by
    by_cases hc : c i < 0
    · simp only [f, w, hc, decide_true, ite_true]
      exact mul_nonpos_of_nonpos_of_nonneg
        (mul_nonpos_of_nonpos_of_nonneg hc.le (positive _ _).le) (sub_nonneg.mpr expand.le)
    · simp only [f, w, hc, decide_false, Bool.false_eq_true, ite_false]
      exact mul_nonpos_of_nonneg_of_nonpos
        (mul_nonneg (le_of_not_gt hc) (positive _ _).le) (sub_nonpos.mpr contract.le)
  have hz : ∑ i, f i = 0 := le_antisymm
    (Finset.sum_nonpos fun i _ => nonpositive i) (h w)
  have every (i : I) : f i = 0 :=
    (Finset.sum_eq_zero_iff_of_nonpos (fun j _ => nonpositive j)).mp hz i (Finset.mem_univ i)
  intro i
  rcases mul_eq_zero.mp (every i) with left | right
  · exact (mul_eq_zero.mp left).resolve_right (ne_of_gt (positive _ _))
  · by_cases hw : w i = true
    · simp [hw] at right
      exact ((ne_of_gt expand) (sub_eq_zero.mp right)).elim
    · simp [hw] at right
      exact ((ne_of_lt contract) (sub_eq_zero.mp right)).elim

/-- Positive transports on a strongly connected finite-type graph cannot
support a nonzero signed leading coefficient when a strictly expanding loop
and a strictly contracting loop both satisfy the dual inequalities. -/
theorem type_graph_zero {S : Type*} (R : S → S → Prop) (C : S → ℝ)
    (connected : ∀ s t, Relation.ReflTransGen R s t)
    (edge : ∀ {s t}, R s t → ∃ k : ℝ, 0 < k ∧ C s ≤ k * C t)
    (sHi sLo : S) {kHi kLo : ℝ}
    (hi : 1 < kHi) (lo : kLo < 1)
    (loopHi : C sHi ≤ kHi * C sHi) (loopLo : C sLo ≤ kLo * C sLo) :
    ∀ s, C s = 0 := by
  have nonnegative {s t : S} (path : Relation.ReflTransGen R s t)
      (hs : 0 ≤ C s) : 0 ≤ C t := by
    induction path with
    | refl => exact hs
    | tail _ h ih =>
      obtain ⟨k, hk, bound⟩ := edge h
      by_contra! hn
      exact (not_lt_of_ge (ih.trans bound)) (mul_neg_of_pos_of_neg hk hn)
  have positive {s t : S} (path : Relation.ReflTransGen R s t)
      (hs : 0 < C s) : 0 < C t := by
    induction path with
    | refl => exact hs
    | tail _ h ih =>
      obtain ⟨k, hk, bound⟩ := edge h
      by_contra! hn
      exact (not_le_of_gt (ih.trans_le bound)) (mul_nonpos_of_nonneg_of_nonpos hk.le hn)
  have start : 0 ≤ C sHi := by
    by_contra! hn
    have bad := mul_lt_mul_of_neg_right hi hn
    rw [one_mul] at bad
    exact (not_lt_of_ge loopHi) bad
  have stop : C sLo ≤ 0 := by
    by_contra! hp
    have bad := mul_lt_mul_of_pos_right lo hp
    rw [one_mul] at bad
    exact (not_lt_of_ge loopLo) bad
  intro s
  exact le_antisymm (le_of_not_gt fun h => (not_lt_of_ge stop) (positive (connected s sLo) h))
    (nonnegative (connected sHi s) start)

end Collatz.MomentSeparation
