module

public import ClockAbsorption
public import SectionDynamics

@[expose] public section

namespace CollatzShell.ForwardSection

open CollatzHarmonic

theorem returns_eq_iterate (n k : ℕ) : returns n k = (next^[k]) n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => simpa only [returns, Function.iterate_succ_apply] using ih (next n)

theorem return_iterate_hit (n k : ℕ) : Hits n ((next^[k]) n) := by
  induction k generalizing n with
  | zero => exact ⟨0,rfl⟩
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    exact Hits.trans (y:=next n) ⟨returnTime n,rfl⟩ (ih _)

/-- Composition with the actual proved forced-section theorem.  Only marked
initial atoms require positive weight; the irrelevant zero state is excluded. -/
theorem collatz_of_marked_linear_columns
    {w : (ℕ × ℕ) → ℝ} {W C : ℝ} (hw : FiniteMass w W)
    (hC : 0 < C) (positive : ∀ n, Marked n → 0 < w (n,0))
    (columns : ∀ k, ColumnBound (clockLift next) w k (C*((k : ℝ)+1))) :
    Universal := by
  apply collatz_iff_marked.mpr
  intro n hn
  obtain ⟨k,hk⟩ := absorption_of_linear_columns next hw hC n (positive n hn) columns
  obtain ⟨t,ht⟩ := return_iterate_hit n k
  exact ⟨t,ht.trans hk⟩

theorem collatz_of_marked_reciprocal_columns
    {w : (ℕ × ℕ) → ℝ} {W : ℝ} (hw : FiniteMass w W)
    (positive : ∀ n, Marked n → 0 < w (n,0)) (M : ℕ → ℝ)
    (hp : ∀ k, 0 < M k)
    (hunbounded : ∀ B : ℝ, ∃ N, B < ∑ k ∈ Finset.range N, 1 / M k)
    (columns : ∀ k, ColumnBound (clockLift next) w k (M k)) :
    Universal := by
  apply collatz_iff_marked.mpr
  intro n hn
  obtain ⟨k,hk⟩ := absorption_of_reciprocal_columns next hw n (positive n hn)
    M hp hunbounded columns
  obtain ⟨t,ht⟩ := return_iterate_hit n k
  exact ⟨t,ht.trans hk⟩

end CollatzShell.ForwardSection
