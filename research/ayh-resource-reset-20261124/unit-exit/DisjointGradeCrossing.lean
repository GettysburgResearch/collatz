import Mathlib

/-! Two unordered pairs of live symbolic classes, one from each head.
The grade is the actual integer exponent of the affine slope. -/

namespace Collatz.DisjointGradeCrossing

/-- If both head pairs occupy the same two different classes, an ordered
choice of different classes realizes a nonnegative terminal grade difference. -/
theorem opposite_classes {α : Type*} (grade : α → ℤ) (a b : Bool → α)
    (ha : a false ≠ a true)
    (hmatches : (b false = a false ∧ b true = a true) ∨
               (b false = a true ∧ b true = a false)) :
    ∃ i j : Bool, a i ≠ b j ∧ grade (b j) ≤ grade (a i) := by
  rcases le_total (grade (a false)) (grade (a true)) with h | h
  · rcases hmatches with ⟨hb, _⟩ | ⟨_, hb⟩
    · exact ⟨true, false, by simpa [hb] using ha.symm, by simpa [hb] using h⟩
    · exact ⟨true, true, by simpa [hb] using ha.symm, by simpa [hb] using h⟩
  · rcases hmatches with ⟨_, hb⟩ | ⟨hb, _⟩
    · exact ⟨false, true, by simpa [hb] using ha, by simpa [hb] using h⟩
    · exact ⟨false, false, by simpa [hb] using ha, by simpa [hb] using h⟩

/-- A cross-grade difference starts strictly negative and gains at most
one per clock.  Inverting its order therefore requires a physical tie. -/
theorem tie_before_inversion (g : ℕ → ℤ) (H : ℕ) (start : g 0 < 0)
    (finish : 0 ≤ g H) (step : ∀ t < H, g (t+1) ≤ g t + 1) :
    ∃ t ≤ H, g t = 0 := by
  induction H with
  | zero => omega
  | succ H ih =>
    by_cases h : 0 ≤ g H
    · obtain ⟨t, ht, he⟩ := ih h (fun t ht => step t (by omega))
      exact ⟨t, by omega, he⟩
    · have hs := step H (by omega)
      exact ⟨H+1, le_rfl, by omega⟩

end Collatz.DisjointGradeCrossing

#print axioms Collatz.DisjointGradeCrossing.opposite_classes
#print axioms Collatz.DisjointGradeCrossing.tie_before_inversion
