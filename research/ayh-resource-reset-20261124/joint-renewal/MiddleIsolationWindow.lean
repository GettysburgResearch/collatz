import TripleGradeProduct

/-! Deterministic physical-window and overlap bounds in the finite-mean proof. -/
namespace CollatzTripleGrades

open scoped BigOperators

def mixedCount (W : Finset ℕ) (a b : ℕ → ℤ) : ℤ :=
  ∑ t ∈ W, if a t ≠ b t then 1 else 0

def isolatedCount (W : Finset ℕ) (a b c : ℕ → ℤ) : ℤ :=
  ∑ t ∈ W, if a t = c t ∧ a t ≠ b t then 1 else 0

/-- Actual bits from all three arms share one physical observation window.
The pair counts need only lie between 2/5 and 3/5 of its length. -/
theorem middle_window_lower (W : Finset ℕ) (a b c : ℕ → ℤ)
    (ha : ∀ t ∈ W, a t = 0 ∨ a t = 1)
    (hb : ∀ t ∈ W, b t = 0 ∨ b t = 1)
    (hc : ∀ t ∈ W, c t = 0 ∨ c t = 1)
    (ab : 2*(W.card:ℤ) ≤ 5*mixedCount W a b)
    (bc : 2*(W.card:ℤ) ≤ 5*mixedCount W b c)
    (ac : 5*mixedCount W a c ≤ 3*(W.card:ℤ)) :
    (W.card:ℤ) ≤ 10*isolatedCount W a b c := by
  have id : 2*isolatedCount W a b c =
      mixedCount W a b + mixedCount W b c - mixedCount W a c := by
    unfold isolatedCount mixedCount
    rw [Finset.mul_sum, ←Finset.sum_add_distrib, ←Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun t ht =>
      mixed_middle_identity (ha t ht) (hb t ht) (hc t ht)
  omega

/-- Summing sliding physical windows on one dyadic shell costs at most their
length times the isolation mass on the enlarged shell. -/
theorem sliding_shell_occupation (H B : ℕ) (p : ℕ → ℝ) (nonneg : ∀ t, 0 ≤ p t) :
    ∑ t ∈ Finset.Ico H (2*H), ∑ i ∈ Finset.range B, p (t+i) ≤
      (B:ℝ) * ∑ t ∈ Finset.Ico H (2*H+B), p t := by
  classical
  have bound (i : ℕ) (hi : i∈Finset.range B) :
      ∑ t ∈ Finset.Ico H (2*H), p (t+i) ≤ ∑ t ∈ Finset.Ico H (2*H+B), p t := by
    have inj : Set.InjOn (fun t : ℕ => t+i) ↑(Finset.Ico H (2*H)) :=
      fun _ _ _ _ eq => by simpa using eq
    have sub : (Finset.Ico H (2*H)).image (fun t : ℕ => t+i) ⊆ Finset.Ico H (2*H+B) := by
      intro v hv
      obtain ⟨t,ht,rfl⟩ := Finset.mem_image.mp hv
      simp only [Finset.mem_Ico] at ht ⊢
      have := Finset.mem_range.mp hi
      omega
    rw [← Finset.sum_image inj]
    exact Finset.sum_le_sum_of_subset_of_nonneg sub (fun t _ _ => nonneg t)
  rw [Finset.sum_comm]
  calc
    _ ≤ ∑ _i ∈ Finset.range B, ∑ t ∈ Finset.Ico H (2*H+B), p t :=
      Finset.sum_le_sum bound
    _ = _ := by simp

#print axioms middle_window_lower
#print axioms sliding_shell_occupation

end CollatzTripleGrades
