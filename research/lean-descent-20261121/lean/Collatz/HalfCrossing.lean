/-
A direct fixed-source closure route. The affine accounting and descent proof
are unconditional. HalfBudget is the remaining universal arithmetic claim.
No random-parity, measure, GRH, or cycle-exclusion assumption is used.
-/
import Collatz.Closure

open CollatzReverseBasin CollatzClosure

namespace CollatzHalfCrossing

/-- Exact integer accounting for one ordinary trajectory. -/
structure Account where
  value : Nat
  mul : Nat
  den : Nat
  debt : Nat
  odds : Nat
  deriving Repr, DecidableEq

def start (n : Nat) : Account := ⟨n, 1, 1, 0, 0⟩

def advance (s : Account) : Account :=
  if s.value % 2 = 0 then
    ⟨shortcut s.value, s.mul, 2*s.den, s.debt, s.odds⟩
  else
    ⟨shortcut s.value, 3*s.mul, 2*s.den, 3*s.debt+s.den, s.odds+1⟩

def run (n : Nat) : Nat → Account
  | 0 => start n
  | t+1 => advance (run n t)

theorem advance_value (s : Account) : (advance s).value = shortcut s.value := by
  unfold advance
  split <;> rfl

theorem advance_identity (n : Nat) (s : Account)
    (h : s.den*s.value = s.mul*n+s.debt) :
    (advance s).den*(advance s).value = (advance s).mul*n+(advance s).debt := by
  unfold advance
  split <;> rename_i hp
  · have he : 2*shortcut s.value = s.value := by unfold shortcut; split <;> omega
    change 2*s.den*shortcut s.value = s.mul*n+s.debt
    calc
      2*s.den*shortcut s.value = s.den*(2*shortcut s.value) := by grind
      _ = s.den*s.value := by rw [he]
      _ = _ := h
  · have ho : 2*shortcut s.value = 3*s.value+1 := by unfold shortcut; split <;> omega
    change 2*s.den*shortcut s.value = 3*s.mul*n+(3*s.debt+s.den)
    calc
      2*s.den*shortcut s.value = s.den*(2*shortcut s.value) := by grind
      _ = s.den*(3*s.value+1) := by rw [ho]
      _ = 3*(s.den*s.value)+s.den := by grind
      _ = 3*(s.mul*n+s.debt)+s.den := by rw [h]
      _ = _ := by grind

theorem run_identity (n t : Nat) :
    (run n t).den*(run n t).value = (run n t).mul*n+(run n t).debt := by
  induction t with
  | zero => simp [run, start]
  | succ t ih => exact advance_identity n (run n t) ih

theorem run_mul_pos (n t : Nat) : 0 < (run n t).mul := by
  induction t with
  | zero => change 0<1; decide
  | succ t ih =>
    change 0 < (advance (run n t)).mul
    unfold advance
    split <;> simp_all

theorem run_value_pos (n t : Nat) (hn : 0<n) : 0 < (run n t).value := by
  induction t with
  | zero => exact hn
  | succ t ih =>
    change 0 < (advance (run n t)).value
    rw [advance_value]
    unfold shortcut
    split <;> omega

theorem run_den (n t : Nat) : (run n t).den = 2^t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change (advance (run n t)).den = 2^(t+1)
    unfold advance
    split <;> simp_all [Nat.pow_succ, Nat.mul_comm]

theorem run_mul (n t : Nat) : (run n t).mul = 3^((run n t).odds) := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change (advance (run n t)).mul = 3^((advance (run n t)).odds)
    unfold advance
    split <;> simp_all [Nat.pow_succ, Nat.mul_comm]

/-- Before the coefficient falls below one half, each odd step adds at
most 2/3 to the debt divided by the multiplier. This is an integer proof. -/
theorem advance_debt (s : Account)
    (hdebt : 3*s.debt ≤ 2*s.odds*s.mul)
    (hcoef : s.den ≤ 2*s.mul) :
    3*(advance s).debt ≤ 2*(advance s).odds*(advance s).mul := by
  unfold advance
  split
  · exact hdebt
  · change 3*(3*s.debt+s.den) ≤ 2*(s.odds+1)*(3*s.mul)
    have h1 := Nat.mul_le_mul_left 3 hdebt
    have h2 := Nat.mul_le_mul_left 3 hcoef
    have e1 : 3*(2*s.odds*s.mul) = 6*s.odds*s.mul := by grind
    have e2 : 2*(s.odds+1)*(3*s.mul) = 6*s.odds*s.mul+6*s.mul := by grind
    rw [e1] at h1
    rw [e2]
    omega

def BeforeHalf (n t : Nat) : Prop :=
  ∀ j, j<t → (run n j).den ≤ 2*(run n j).mul

theorem run_debt (n t : Nat) (h : BeforeHalf n t) :
    3*(run n t).debt ≤ 2*(run n t).odds*(run n t).mul := by
  induction t with
  | zero => simp [run, start]
  | succ t ih =>
    apply advance_debt (run n t)
    · apply ih
      intro j hj
      exact h j (by omega)
    · exact h t (by omega)

/-- A first half-crossing within 3n/2 odd steps is an actual strict descent. -/
theorem half_crossing_descent (n t : Nat) (hn : 0<n)
    (hprefix : BeforeHalf n t)
    (hcross : 2*(run n t).mul < (run n t).den)
    (hbudget : 2*(run n t).odds ≤ 3*n) :
    (run n t).value < n := by
  have hdebt := run_debt n t hprefix
  have hid := run_identity n t
  have hbudget' := Nat.mul_le_mul_right (run n t).mul hbudget
  have e : 3*n*(run n t).mul = 3*((run n t).mul*n) := by grind
  rw [e] at hbudget'
  have hb : (run n t).debt ≤ (run n t).mul*n := by omega
  have not_ge : ¬ n ≤ (run n t).value := by
    intro hv
    have hc := Nat.mul_lt_mul_of_pos_right hcross hn
    have hv' := Nat.mul_le_mul_left (run n t).den hv
    have e2 : 2*(run n t).mul*n = 2*((run n t).mul*n) := by grind
    rw [e2] at hc
    omega
  omega

theorem basin_run (n t : Nat) : Basin (run n t).value ↔ Basin n := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change Basin (advance (run n t)).value ↔ Basin n
    rw [advance_value]
    exact (basin_step _).trans ih

/-- The missing global claim. It concerns each fixed ordinary integer;
all quantifiers are explicit and the terminal odd count is bounded. -/
def HalfBudget : Prop :=
  ∀ n, 1<n → ∃ t, BeforeHalf n t ∧
    2*(run n t).mul < (run n t).den ∧ 2*(run n t).odds ≤ 3*n

/-- A proof of HalfBudget would prove full Collatz, including exclusion
of both divergent trajectories and nontrivial cycles. -/
theorem collatz_of_half_budget (H : HalfBudget) : ∀ n, 0<n → Basin n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases h1 : n=1
    · subst n; exact ⟨0, rfl⟩
    obtain ⟨t, hp, hc, hb⟩ := H n (by omega)
    have smaller := half_crossing_descent n t hn hp hc hb
    exact (basin_run n t).mp (ih _ smaller (run_value_pos n t hn))

end CollatzHalfCrossing
