/-
The direct descent route as one explicit, finite integer test at each input.
The theorem linking acceptance to Collatz is proved. Universal acceptance is
an open arithmetic assertion, not an axiom of this development.
-/
import Collatz.HalfCrossing

open CollatzReverseBasin CollatzClosure CollatzHalfCrossing

namespace CollatzBudgetCheck

theorem odds_advance_le (s : Account) : s.odds ≤ (advance s).odds := by
  unfold advance
  split <;> simp_all

/-- Every witness allowed by HalfBudget lies within this explicit clock. -/
theorem witness_clock_bound (n t : Nat) (hp : BeforeHalf n t)
    (hb : 2*(run n t).odds ≤ 3*n) : t ≤ 3*n+2 := by
  cases t with
  | zero => omega
  | succ t =>
    have hc := hp t (by omega)
    rw [run_den, run_mul] at hc
    have hg := Nat.pow_le_pow_left (show 3 ≤ 4 by decide) (run n t).odds
    have hpow : 2*4^((run n t).odds) = 2^(2*(run n t).odds+1) := by
      rw [Nat.pow_add, Nat.pow_mul]
      simp [Nat.mul_comm]
    have hpowle : 2^t ≤ 2^(2*(run n t).odds+1) := by omega
    have ht := (Nat.pow_le_pow_iff_right (show 1 < 2 by decide)).mp hpowle
    have ho := odds_advance_le (run n t)
    change (run n t).odds ≤ (run n (t+1)).odds at ho
    omega

/-- The first successful half-crossing, if its odd budget is legal.
The fuel bounds the number of transitions, not the integer values visited. -/
def search (n : Nat) : Nat → Nat → Option Nat
  | fuel, clock =>
    if 2*(run n clock).mul < (run n clock).den then
      if 2*(run n clock).odds ≤ 3*n then some clock else none
    else
      match fuel with
      | 0 => none
      | fuel+1 => search n fuel (clock+1)

/-- The test asks for no oracle, supplied stopping time, or external certificate. -/
def budgetCheck (n : Nat) : Bool := (search n (3*n+2) 0).isSome

theorem search_sound (n fuel clock t : Nat) (hp : BeforeHalf n clock)
    (hs : search n fuel clock = some t) :
    BeforeHalf n t ∧ 2*(run n t).mul < (run n t).den ∧
      2*(run n t).odds ≤ 3*n ∧ clock ≤ t ∧ t ≤ clock+fuel := by
  induction fuel generalizing clock with
  | zero =>
    simp only [search] at hs
    split at hs
    · rename_i hc
      split at hs
      · rename_i hb
        cases hs
        exact ⟨hp, hc, hb, by omega, by omega⟩
      · contradiction
    · contradiction
  | succ fuel ih =>
    simp only [search] at hs
    split at hs
    · rename_i hc
      split at hs
      · rename_i hb
        cases hs
        exact ⟨hp, hc, hb, by omega, by omega⟩
      · contradiction
    · rename_i hc
      have hp' : BeforeHalf n (clock+1) := by
        intro j hj
        by_cases hj' : j < clock
        · exact hp j hj'
        · have he : j = clock := by omega
          subst j
          omega
      obtain ⟨a,b,c,d,e⟩ := ih (clock+1) hp' hs
      exact ⟨a,b,c,by omega,by omega⟩

theorem search_complete (n fuel clock t : Nat) (hlo : clock ≤ t)
    (hhi : t ≤ clock+fuel) (hp : BeforeHalf n t)
    (hc : 2*(run n t).mul < (run n t).den)
    (hb : 2*(run n t).odds ≤ 3*n) : search n fuel clock = some t := by
  induction fuel generalizing clock with
  | zero =>
    have he : clock = t := by omega
    subst clock
    simp [search, hc, hb]
  | succ fuel ih =>
    by_cases he : clock = t
    · subst clock
      simp [search, hc, hb]
    · have hlt : clock < t := by omega
      have hnot : ¬ 2*(run n clock).mul < (run n clock).den := by
        have hh := hp clock hlt
        omega
      simp only [search, ite_eq_right hnot]
      exact ih (clock+1) (by omega) (by omega)

/-- Acceptance is exactly existence of a first half-crossing with this budget. -/
theorem budgetCheck_iff (n : Nat) : budgetCheck n = true ↔
    ∃ t, BeforeHalf n t ∧ 2*(run n t).mul < (run n t).den ∧
      2*(run n t).odds ≤ 3*n := by
  unfold budgetCheck
  constructor
  · intro h
    cases hs : search n (3*n+2) 0 with
    | none => simp [hs] at h
    | some t =>
      have hp : BeforeHalf n 0 := by intro j hj; omega
      obtain ⟨a,b,c,_,_⟩ := search_sound n (3*n+2) 0 t hp hs
      exact ⟨t,a,b,c⟩
  · rintro ⟨t,hp,hc,hb⟩
    have hs := search_complete n (3*n+2) 0 t (by omega)
      (by have hh := witness_clock_bound n t hp hb; omega) hp hc hb
    simp [hs]

/-- A single explicit universal Boolean inequality would finish the proof. -/
def UniversalBudgetCheck : Prop := ∀ n, 1 < n → budgetCheck n = true

theorem universal_check_iff_half_budget : UniversalBudgetCheck ↔ HalfBudget := by
  unfold UniversalBudgetCheck HalfBudget
  exact ⟨fun h n hn => (budgetCheck_iff n).mp (h n hn),
    fun h n hn => (budgetCheck_iff n).mpr (h n hn)⟩

theorem collatz_of_universal_budget_check (h : UniversalBudgetCheck) :
    ∀ n, 0<n → Basin n :=
  collatz_of_half_budget (universal_check_iff_half_budget.mp h)

end CollatzBudgetCheck
