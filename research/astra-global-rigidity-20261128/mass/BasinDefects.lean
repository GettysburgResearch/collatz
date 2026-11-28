import CriticalCountStandalone

/-! Ordinary first-hit colors, their one-site defect, and the actual incomparable
roots 5 and 85. The source-density and Hilbert-space conclusions are written. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CriticalCount

def Visits (x a : Nat) : Prop := ∃ k, orbit x k = a

theorem visits_after_step {x a : Nat} (h : Visits (step x) a) : Visits x a := by
  obtain ⟨k, hk⟩ := h
  refine ⟨1+k, ?_⟩
  rw [orbit_add]
  exact hk

theorem visits_step_iff_of_ne {x a : Nat} (hne : x ≠ a) :
    Visits x a ↔ Visits (step x) a := by
  constructor
  · intro h
    obtain ⟨k, hk⟩ := h
    cases k with
    | zero => exact False.elim (hne hk)
    | succ k =>
      refine ⟨k, ?_⟩
      rw [show k+1 = 1+k by omega, orbit_add] at hk
      exact hk
  · exact visits_after_step

theorem common_source_forces_comparability {x a b : Nat}
    (ha : Visits x a) (hb : Visits x b) : Visits a b ∨ Visits b a := by
  obtain ⟨j, hj⟩ := ha
  obtain ⟨k, hk⟩ := hb
  by_cases order : j ≤ k
  · left
    refine ⟨k-j, ?_⟩
    rw [← hj, ← orbit_add, show j+(k-j) = k by omega, hk]
  · right
    refine ⟨j-k, ?_⟩
    rw [← hk, ← orbit_add, show k+(j-k) = j by omega, hj]

private def smallPowers (x : Nat) : Prop :=
  x=1 ∨ x=2 ∨ x=4 ∨ x=8 ∨ x=16 ∨ x=32 ∨ x=64 ∨ x=128

private theorem smallPowers_step {x : Nat} (h : smallPowers x) : smallPowers (step x) := by
  rcases h with h | h | h | h | h | h | h | h <;> subst x <;>
    simp [step, smallPowers]

private theorem smallPowers_orbit {x : Nat} (h : smallPowers x) (j : Nat) :
    smallPowers (orbit x j) := by
  induction j with
  | zero => exact h
  | succ j ih => exact smallPowers_step ih

private theorem five_outside : ¬smallPowers 5 := by simp [smallPowers]
private theorem eightyFive_outside : ¬smallPowers 85 := by simp [smallPowers]

theorem five_nonreturn : ¬Visits (step 5) 5 := by
  rintro ⟨j, hj⟩
  have h := smallPowers_orbit (x := step 5) (by simp [step, smallPowers]) j
  exact five_outside (hj ▸ h)

theorem five_single_defect (x : Nat) :
    (Visits x 5 ∧ ¬Visits (step x) 5) ↔ x=5 := by
  constructor
  · intro h
    by_contra hn
    exact h.2 ((visits_step_iff_of_ne hn).mp h.1)
  · rintro rfl
    exact ⟨⟨0, rfl⟩, five_nonreturn⟩

theorem five_not_eightyFive : ¬Visits 5 85 := by
  intro h
  obtain ⟨j, hj⟩ := (visits_step_iff_of_ne (by decide : (5 : Nat) ≠ 85)).mp h
  have inside := smallPowers_orbit (x := step 5) (by simp [step, smallPowers]) j
  exact eightyFive_outside (hj ▸ inside)

theorem eightyFive_not_five : ¬Visits 85 5 := by
  intro h
  obtain ⟨j, hj⟩ := (visits_step_iff_of_ne (by decide : (85 : Nat) ≠ 5)).mp h
  have inside := smallPowers_orbit (x := step 85) (by simp [step, smallPowers]) j
  exact five_outside (hj ▸ inside)

theorem five_eightyFive_disjoint (x : Nat) : ¬(Visits x 5 ∧ Visits x 85) := by
  rintro ⟨ha, hb⟩
  rcases common_source_forces_comparability ha hb with h | h
  · exact five_not_eightyFive h
  · exact eightyFive_not_five h

end Collatz.CriticalCount
