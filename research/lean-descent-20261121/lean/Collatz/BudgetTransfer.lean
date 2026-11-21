/- General compositional rules for the fixed-source half budget. -/
import Collatz.HalfCrossing

open CollatzReverseBasin CollatzHalfCrossing

namespace CollatzBudgetTransfer

theorem advance_odds (s : Account) :
    (advance s).odds = s.odds + if s.value % 2 = 0 then 0 else 1 := by
  unfold advance
  split <;> simp_all

theorem run_add_value_odds (n t u : Nat) :
    (run n (t+u)).value = (run (run n t).value u).value ∧
    (run n (t+u)).odds = (run n t).odds + (run (run n t).value u).odds := by
  induction u with
  | zero => simp [run, start]
  | succ u ih =>
    change (advance (run n (t+u))).value =
        (advance (run (run n t).value u)).value ∧
      (advance (run n (t+u))).odds =
        (run n t).odds + (advance (run (run n t).value u)).odds
    obtain ⟨hv, ho⟩ := ih
    constructor
    · rw [advance_value, advance_value, hv]
    · rw [advance_odds, advance_odds, hv, ho]
      omega

theorem run_add_mul (n t u : Nat) :
    (run n (t+u)).mul = (run n t).mul * (run (run n t).value u).mul := by
  simp only [run_mul, (run_add_value_odds n t u).2, Nat.pow_add]

theorem run_add_den (n t u : Nat) :
    (run n (t+u)).den = (run n t).den * (run (run n t).value u).den := by
  simp only [run_den, Nat.pow_add]

theorem odds_mono (n j k : Nat) (h : j ≤ k) : (run n j).odds ≤ (run n k).odds := by
  have hp := (run_add_value_odds n j (k-j)).2
  rw [Nat.add_sub_of_le h] at hp
  omega

/-- One source has a first half-crossing within the stated odd budget. -/
def BudgetAt (n : Nat) : Prop :=
  ∃ t, BeforeHalf n t ∧ 2*(run n t).mul < (run n t).den ∧
    2*(run n t).odds ≤ 3*n

/-- Any crossing within budget contains a first crossing within budget. -/
theorem budget_of_crossing (n t : Nat)
    (hc : 2*(run n t).mul < (run n t).den)
    (hb : 2*(run n t).odds ≤ 3*n) : BudgetAt n := by
  classical
  induction t using Nat.strong_induction_on with
  | h t ih =>
    by_cases he : ∃ j, j<t ∧ 2*(run n j).mul < (run n j).den
    · obtain ⟨j, hj, hcj⟩ := he
      have hm := odds_mono n j t (by omega)
      exact ih j hj hcj (by omega)
    · refine ⟨t, ?_, hc, hb⟩
      intro j hj
      by_cases hgood : (run n j).den ≤ 2*(run n j).mul
      · exact hgood
      · exact False.elim (he ⟨j, hj, by omega⟩)

/-- Reading a noncontracting ordinary prefix backwards transfers the budget,
provided the source first crossing lies after that prefix. All hypotheses
concern actual ordinary integers and exact integer coefficients. -/
theorem budget_inverse (x q t : Nat)
    (he : (run x t).value = q)
    (hp : BeforeHalf x t)
    (ha : (run x t).den ≤ (run x t).mul)
    (hr : 3*x ≤ 3*q+2*(run x t).odds)
    (hx : BudgetAt x) : BudgetAt q := by
  obtain ⟨h, hbefore, hcross, hbudget⟩ := hx
  have hlate : t<h := by
    by_cases hnot : t<h
    · exact hnot
    have hle : h≤t := by omega
    rcases Nat.lt_or_eq_of_le hle with hlt | heq
    · have hn := hp h hlt
      omega
    · subst h
      omega
  let u := h-t
  have ht : t+u=h := Nat.add_sub_of_le (by omega)
  have hm := run_add_mul x t u
  have hd := run_add_den x t u
  have ho := (run_add_value_odds x t u).2
  rw [ht, he] at hm hd ho
  have hu : 2*(run q u).mul < (run q u).den := by
    rw [hm, hd] at hcross
    have hden := Nat.mul_le_mul_right (run q u).den ha
    have heq : 2*((run x t).mul*(run q u).mul) =
        (run x t).mul*(2*(run q u).mul) := by grind
    rw [heq] at hcross
    apply Nat.lt_of_mul_lt_mul_left (a := (run x t).mul)
    omega
  apply budget_of_crossing q u hu
  omega

/-- A strictly smaller source automatically meets the resource condition. -/
theorem budget_inverse_smaller (x q t : Nat)
    (he : (run x t).value = q)
    (hp : BeforeHalf x t)
    (ha : (run x t).den ≤ (run x t).mul)
    (hs : x<q) (hx : BudgetAt x) : BudgetAt q := by
  exact budget_inverse x q t he hp ha (by omega) hx

/-- Two unequal ordinary prefixes may be compared. This is the general
mixed forward/inverse rule: the source prefix must not have spent its
half-crossing, while the target coefficient and odd cost are no larger
than the displayed exact allowance. -/
theorem budget_merger (x n tx tn : Nat)
    (he : (run x tx).value = (run n tn).value)
    (hp : BeforeHalf x (tx+1))
    (ha : (run n tn).mul*(run x tx).den ≤
      (run x tx).mul*(run n tn).den)
    (hr : 3*x+2*(run n tn).odds ≤ 3*n+2*(run x tx).odds)
    (hx : BudgetAt x) : BudgetAt n := by
  obtain ⟨h, _, hcross, hbudget⟩ := hx
  have hlate : tx<h := by
    by_cases hl : tx<h
    · exact hl
    · have hn := hp h (by omega)
      omega
  let u := h-tx
  have ht : tx+u=h := Nat.add_sub_of_le (by omega)
  have hmx := run_add_mul x tx u
  have hdx := run_add_den x tx u
  have hox := (run_add_value_odds x tx u).2
  rw [ht, he] at hmx hdx hox
  have hmn := run_add_mul n tn u
  have hdn := run_add_den n tn u
  have hon := (run_add_value_odds n tn u).2
  have hdnpos : 0<(run n tn).den := by
    rw [run_den]
    exact Nat.pow_pos (by decide)
  have hc : 2*(run n (tn+u)).mul < (run n (tn+u)).den := by
    rw [hmx, hdx] at hcross
    rw [hmn, hdn]
    have h1 := Nat.mul_lt_mul_of_pos_right hcross hdnpos
    have h2 := Nat.mul_le_mul_right (2*(run (run n tn).value u).mul) ha
    have e1 : (2*((run x tx).mul*(run (run n tn).value u).mul))*(run n tn).den =
        ((run x tx).mul*(run n tn).den)*(2*(run (run n tn).value u).mul) := by grind
    have e2 : ((run n tn).mul*(run x tx).den)*(2*(run (run n tn).value u).mul) =
        (run x tx).den*(2*((run n tn).mul*(run (run n tn).value u).mul)) := by grind
    have e3 : ((run x tx).den*(run (run n tn).value u).den)*(run n tn).den =
        (run x tx).den*((run n tn).den*(run (run n tn).value u).den) := by grind
    rw [e1, e3] at h1
    rw [e2] at h2
    apply Nat.lt_of_mul_lt_mul_left (a := (run x tx).den)
    omega
  apply budget_of_crossing n (tn+u) hc
  omega

/-- A guarded forward prefix is the special case with an empty source prefix. -/
theorem budget_forward (n x t : Nat)
    (he : (run n t).value = x)
    (ha : (run n t).mul ≤ (run n t).den)
    (hr : 3*x+2*(run n t).odds ≤ 3*n)
    (hx : BudgetAt x) : BudgetAt n := by
  apply budget_merger x n 0 t
  · simpa only [run, start] using he.symm
  · intro j hj
    have hj0 : j=0 := by omega
    subst j
    change 1 ≤ 2*1
    decide
  · simpa only [run, start, Nat.mul_one, Nat.one_mul] using ha
  · simpa only [run, start, Nat.mul_zero, Nat.add_zero] using hr
  · exact hx


end CollatzBudgetTransfer
