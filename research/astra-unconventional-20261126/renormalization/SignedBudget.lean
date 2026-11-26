import SourceDeletion
import Mathlib.Tactic.Linarith

/-! A clock inequality on every negative shortcut path avoiding −1.  It
is attained by every complete lap of the cycle through −5. -/
namespace Collatz.SignedBudget
open Collatz.SourceDeletion

def signedStep (x : Int) : Int :=
  if x % 2 = 0 then x / 2 else (3*x+1)/2

def bit (x : Int) : Nat := if x % 2 = 0 then 0 else 1

def travel : Nat → Int → Int
  | 0, x => x
  | h+1, x => travel h (signedStep x)

def digits : Nat → Int → Nat
  | 0, _ => 0
  | h+1, x => digits h (signedStep x) + bit x

private theorem step_eq_nat (x : Nat) : signedStep x = (step x : Nat) := by
  unfold signedStep step
  split <;> split <;> omega

theorem physical (h x : Nat) :
    travel h x = (run h x : Nat) ∧ digits h x = odds h x := by
  induction h generalizing x with
  | zero => simp [travel, digits, run, odds]
  | succ h ih =>
    obtain ⟨a,b⟩ := ih (step x)
    have eb : bit x = x%2 := by unfold bit; split <;> omega
    simp only [travel, digits, run, odds, step_eq_nat, a, b, eb, and_self]

/-- A signed shadow is an exact affine translate, with the same word, including
when the shadow is a negative integer. -/
theorem signed_lift (h : Nat) (x d : Int) :
    travel h (x+2^h*d) = travel h x + 3^(digits h x)*d ∧
    digits h (x+2^h*d) = digits h x := by
  induction h generalizing x d with
  | zero => simp [travel, digits]
  | succ h ih =>
    have db : (2:Int)^(h+1)*d = 2*(2^h*d) := by ring
    by_cases ev : x%2=0
    · have ex : (x+2^(h+1)*d)%2 = 0 := by rw [db]; omega
      have s : signedStep (x+2^(h+1)*d) = signedStep x+2^h*d := by
        simp only [signedStep, ex, ev, ite_true]
        rw [db]
        omega
      obtain ⟨a,b⟩ := ih (signedStep x) d
      simp only [travel, digits, s, a, b, bit, ex, ev, ite_true, Nat.add_zero, and_self]
    · have ex : (x+2^(h+1)*d)%2 ≠ 0 := by rw [db]; omega
      have s : signedStep (x+2^(h+1)*d) = signedStep x+2^h*(3*d) := by
        simp only [signedStep, ex, ev, ite_false]
        rw [db]
        rw [show 3*(x+2*(2^h*d))+1 = (3*x+1)+2*(2^h*(3*d)) by ring]
        omega
      obtain ⟨a,b⟩ := ih (signedStep x) (3*d)
      simp only [travel, digits, s, a, b, bit, ex, ev, ite_false]
      constructor
      · rw [pow_succ]; ring
      · trivial

/-- Squared magnitude with three small corrections. -/
def potential (x : Int) : Int :=
  if x = -2 then 5 else if x = -4 then 18 else if x = -7 then 50 else x^2

theorem potential_lower (x : Int) : x^2 ≤ potential x := by
  unfold potential
  split <;> rename_i e
  · subst x; decide
  split <;> rename_i e
  · subst x; decide
  split <;> rename_i e
  · subst x; decide
  rfl

private theorem above_fixed {x : Int} (hx : -1 ≤ x) : -1 ≤ signedStep x := by
  unfold signedStep
  split <;> omega

private theorem above_travel {x : Int} (h : Nat) (hx : -1 ≤ x) : -1 ≤ travel h x := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih => exact ih (above_fixed hx)

/-- The one-step certificate applies at all negative centers other than −1
whose successor also avoids −1. -/
theorem negative_step {x : Int} (hs : signedStep x ≤ -2) (hx : x ≤ -2) :
    8^(bit x)*potential x ≤ 4*potential (signedStep x) := by
  by_cases small : -8 ≤ x
  · have cases : x = -8 ∨ x = -7 ∨ x = -6 ∨ x = -5 ∨ x = -4 ∨ x = -3 ∨ x = -2 := by omega
    rcases cases with h|h|h|h|h|h|h <;> subst x <;> first | decide | exact False.elim ((by decide : ¬signedStep (-2) ≤ -2) hs)
  · have p : potential x = x^2 := by
      simp only [potential, show x ≠ -2 by omega, show x ≠ -4 by omega, show x ≠ -7 by omega, ite_false]
    rw [p]
    have upper := potential_lower (signedStep x)
    by_cases ev : x%2=0
    · have eqn : 2*signedStep x=x := by simp only [signedStep,ev,ite_true]; omega
      simp only [bit,ev,ite_true,pow_zero,one_mul]
      nlinarith [congrArg (fun a : Int => a^2) eqn]
    · have eqn : 2*signedStep x=3*x+1 := by simp only [signedStep,ev,ite_false]; omega
      simp only [bit,ev,ite_false,pow_one]
      nlinarith [congrArg (fun a : Int => a^2) eqn,
        mul_nonneg (show 0 ≤ -x by omega) (show 0 ≤ -x-6 by omega)]

/-- The terminal test alone excludes a visit to −1 anywhere in the path. -/
theorem negative_budget (h : Nat) (x : Int) (ending : travel h x ≤ -2) :
    8^(digits h x)*potential x ≤ 4^h*potential (travel h x) := by
  induction h generalizing x with
  | zero => simp [travel,digits]
  | succ h ih =>
    change travel h (signedStep x) ≤ -2 at ending
    have sx : signedStep x ≤ -2 := by
      by_contra! fail
      have := above_travel h (show -1 ≤ signedStep x by omega)
      omega
    have xx : x ≤ -2 := by
      by_contra! fail
      have := above_fixed (show -1 ≤ x by omega)
      omega
    have one := negative_step sx xx
    have rest := ih (signedStep x) ending
    simp only [travel,digits,pow_add,pow_succ]
    calc
      _ = 8^(digits h (signedStep x))*(8^(bit x)*potential x) := by ring
      _ ≤ 8^(digits h (signedStep x))*(4*potential (signedStep x)) :=
          Int.mul_le_mul_of_nonneg_left one (by positivity)
      _ = 4*(8^(digits h (signedStep x))*potential (signedStep x)) := by ring
      _ ≤ 4*(4^h*potential (travel h (signedStep x))) :=
          Int.mul_le_mul_of_nonneg_left rest (by decide)
      _ = _ := by ring

/-- No larger uniform exponential per-odd factor can satisfy a multiplicative
potential inequality around a complete lap, regardless of the potential. -/
theorem sharp_lap (v : Int → Int) (base : Int) (pos : 0 < v (-5))
    (bound : base^(digits 3 (-5))*v (-5) ≤ 4^3*v (travel 3 (-5))) :
    base^2 ≤ 64 := by
  change base^2 * v (-5) ≤ 64*v (-5) at bound
  exact (mul_le_mul_iff_left₀ pos).mp bound

#print axioms physical
#print axioms signed_lift
#print axioms negative_step
#print axioms negative_budget
#print axioms sharp_lap
end Collatz.SignedBudget
