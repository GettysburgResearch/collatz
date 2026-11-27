import Mathlib.Tactic.NormNum

/-! Exact global predecessor minima at the good ordinary control 353.
Finite certificates reach one while avoiding the fixed target 199. -/
namespace Collatz.OrdinaryBasinControl
set_option autoImplicit false

def step (n : ℕ) : ℕ := if n % 2 = 0 then n/2 else (3*n+1)/2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | t+1, n => run t (step n)

def avoids : ℕ → ℕ → Bool
  | 0, n => n == 1
  | t+1, n => if n = 1 then true else if n = 199 then false else avoids t (step n)

private theorem oneTwo (t n : ℕ) (h : n=1 ∨ n=2) : run t n = 1 ∨ run t n = 2 := by
  induction t generalizing n with
  | zero => exact h
  | succ t ih =>
    apply ih (step n)
    rcases h with rfl | rfl <;> decide

/-- A certificate is valid at every future shortcut time. -/
theorem avoidsForever (fuel n : ℕ) (ok : avoids fuel n = true) (t : ℕ) :
    run t n ≠ 199 := by
  by_cases h : n = 1
  · have hsmall := oneTwo t n (Or.inl h)
    omega
  · induction fuel generalizing n t with
    | zero => simp [avoids, h] at ok
    | succ fuel ih =>
      by_cases hbad : n = 199
      · simp [avoids, hbad] at ok
      · have rest : avoids fuel (step n) = true := by simpa [avoids, h, hbad] using ok
        cases t with
        | zero => exact hbad
        | succ t =>
          by_cases hs : step n = 1
          · have hs' := oneTwo t (step n) (Or.inl hs)
            change run t (step n) ≠ 199
            omega
          · exact ih (step n) rest t hs

def belowCut (n : ℕ) : Prop :=
  n % 2 = 1 ∧ (n < 199 ∨ (n % 3 = 0 ∧ n < 417) ∨ (n % 48 = 17 ∧ n < 353))

instance (n : ℕ) : Decidable (belowCut n) := by unfold belowCut; infer_instance

def checkEntry (n : ℕ) : Bool := if belowCut n then avoids 100 n else true

set_option maxRecDepth 100000 in
set_option maxHeartbeats 1000000 in
private theorem checkedTable : (List.range 417).all checkEntry = true := by decide

/-- No smaller odd source in any of the three claimed classes reaches the target. -/
theorem predecessorFloors (n : ℕ) (hn : belowCut n) (t : ℕ) : run t n ≠ 199 := by
  have bound : n < 417 := by unfold belowCut at hn; omega
  have H := List.all_eq_true.mp checkedTable n (List.mem_range.mpr bound)
  exact avoidsForever 100 n (by simpa [checkEntry, hn] using H) t

set_option maxRecDepth 100000 in
/-- The minima 199, 417 and 353 are each attained, and both original arms are good. -/
theorem attainingSources :
    run 0 199 = 199 ∧ run 9 417 = 199 ∧ run 4 353 = 199 ∧
    run 80 353 = 1 ∧ run 23 1059 = 1 := by decide

#print axioms avoidsForever
#print axioms predecessorFloors
#print axioms attainingSources
end Collatz.OrdinaryBasinControl
