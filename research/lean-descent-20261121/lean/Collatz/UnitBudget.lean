/-
The full-convergence route only needs the proposed quantitative assertion on
positive ternary units. No quantitative budget is claimed for other inputs.
-/
import Collatz.BudgetCheck

open CollatzReverseBasin CollatzClosure CollatzHalfCrossing CollatzBudgetCheck

namespace CollatzUnitBudget

theorem shortcut_unit (n : Nat) (hu : n%3 ≠ 0) : shortcut n % 3 ≠ 0 := by
  unfold shortcut
  split <;> omega

theorem run_unit (n t : Nat) (hu : n%3 ≠ 0) : (run n t).value % 3 ≠ 0 := by
  induction t with
  | zero => exact hu
  | succ t ih =>
    change (advance (run n t)).value % 3 ≠ 0
    rw [advance_value]
    exact shortcut_unit _ ih

/-- Only the positive integers coprime to three are queried. -/
def UnitBudgetCheck : Prop :=
  ∀ n, 1<n → n%3 ≠ 0 → budgetCheck n = true

/-- The quantitative induction stays entirely inside the unit domain. -/
theorem units_of_budget (H : UnitBudgetCheck) :
    ∀ n, 0<n → n%3 ≠ 0 → Basin n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn hu
    by_cases h1 : n=1
    · subst n; exact ⟨0,rfl⟩
    obtain ⟨t,hp,hc,hb⟩ := (budgetCheck_iff n).mp (H n (by omega) hu)
    have hlt := half_crossing_descent n t hn hp hc hb
    exact (basin_run n t).mp
      (ih _ hlt (run_value_pos n t hn) (run_unit n t hu))

/-- Ordinary moves extend convergence on units to every positive input. -/
theorem all_of_units (H : ∀ n, 0<n → n%3 ≠ 0 → Basin n) :
    ∀ n, 0<n → Basin n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases he : n%2=0
    · have hs : shortcut n = n/2 := by simp [shortcut,he]
      apply (basin_step n).mp
      rw [hs]
      exact ih _ (by omega) (by omega)
    · exact (basin_odd n (by omega)).mp (H _ (by omega) (by omega))

/-- Full Collatz follows if the finite budget test passes on every unit input. -/
theorem collatz_of_unit_budget (H : UnitBudgetCheck) :
    ∀ n, 0<n → Basin n := all_of_units (units_of_budget H)

end CollatzUnitBudget
