import Std

namespace Collatz.ParentCertificate

/-- First-hitting words ending at 4, with the unreduced numerator obtained
    by companion backward substitution over the denominator 3^h. -/
inductive ToFour : Nat → Nat → Nat → Prop where
  | root : ToFour 0 4 4
  | even {h y b} : ToFour h y b → ToFour (h+1) (2*y) (2*b)
  | odd {h x y b} : ToFour h y b → 3*x+1=2*y →
      ToFour (h+1) x (3^(h+1)+4*b)

theorem numerator_unit {h x a} (w : ToFour h x a) : a % 3 ≠ 0 := by
  induction w with
  | root => decide
  | even _ ih => omega
  | @odd h x y b _ _ ih =>
    rw [Nat.pow_succ]
    omega

/-- Decode numerators of the entire positive first-hit level simultaneously.
    The last guard enforces ordinary integrality of an odd physical preimage. -/
def recover : Nat → Nat → Option Nat
  | 0, a => if a = 4 then some 4 else none
  | h+1, a =>
    if a%2=0 then (recover h (a/2)).map (fun y => 2*y)
    else
      let t := 3^(h+1)
      let b := (a-t)/4
      if a=t+4*b then do
        let y ← recover h b
        let x := (2*y-1)/3
        if 3*x+1=2*y then some x else none
      else none

theorem recover_complete {h x a} (w : ToFour h x a) : recover h a = some x := by
  induction w with
  | root => decide
  | @even h y b _ ih => simp [recover, ih]
  | @odd h x y b _ edge ih =>
    have hp : 3^(h+1)%2=1 := by simp [Nat.pow_mod]
    have hz : (3^(h+1)+4*b)%2 ≠ 0 := by omega
    have hdiv : (2*y-1)/3=x := by omega
    simp [recover, hz, ih, hdiv, edge]

theorem recover_sound {h x a} (ha : recover h a = some x) : ToFour h x a := by
  induction h generalizing a x with
  | zero =>
    simp only [recover] at ha
    split at ha
    next he => cases he; cases ha; exact .root
    next => contradiction
  | succ h ih =>
    simp only [recover] at ha
    by_cases he : a%2=0
    · simp only [he, ite_true] at ha
      cases hr : recover h (a/2) with
      | none => simp [hr] at ha
      | some y =>
        simp [hr] at ha
        have hdouble : 2*(a/2)=a := by omega
        simpa only [hdouble, ha] using ToFour.even (ih hr)
    · simp only [he, ite_false] at ha
      split at ha
      next hs =>
        cases hr : recover h ((a-3^(h+1))/4) with
        | none => simp [hr] at ha
        | some y =>
          simp only [hr, bind, Option.bind] at ha
          split at ha
          next hedge =>
            cases ha
            exact hs.symm ▸ ToFour.odd (ih hr) hedge
          next => contradiction
      next => contradiction

def step (x : Nat) : Nat := if x%2=0 then x/2 else (3*x+1)/2
def run (x : Nat) : Nat → Nat
  | 0 => x
  | h+1 => run (step x) h

theorem run_even (t k : Nat) :
    run (9*4^k*t+1) (2*k)=9*3^k*t+1 := by
  induction k generalizing t with
  | zero => simp [run]
  | succ k ih =>
    have h₀ : 9*4^(k+1)*t+1 = 4*(9*4^k*t)+1 := by rw [Nat.pow_succ]; grind
    have h₁ (z : Nat) : step (4*z+1)=6*z+2 := by unfold step; split <;> omega
    have h₂ (z : Nat) : step (6*z+2)=3*z+1 := by unfold step; split <;> omega
    have h₃ : 2*(k+1)=2*k+1+1 := by omega
    rw [h₀, h₃, run, h₁, run, h₂]
    have h₄ : 3*(9*4^k*t)+1 = 9*4^k*(3*t)+1 := by grind
    rw [h₄, ih, Nat.pow_succ]
    grind

/-- At the very clock where the power-of-two ordinary parent reaches 1,
    its residual child is the indicated exponential integer. -/
theorem terminal_powers (t : Nat) :
    run (9*2^(6*t+1)+2) (6*t+1) = 3^(3*t+2)+1 := by
  have hp : 2^(6*t)=4^(3*t) := by
    rw [show 6*t=2*(3*t) by omega, Nat.pow_mul]
  have he : step (9*2^(6*t+1)+2)=9*4^(3*t)+1 := by
    rw [Nat.pow_succ, hp]
    unfold step
    split <;> omega
  rw [run, he, show 6*t=2*(3*t) by omega]
  have h := run_even 1 (3*t)
  simpa [Nat.pow_add, Nat.mul_comm] using h

def odds (x : Nat) : Nat → Nat
  | 0 => 0
  | h+1 => x%2 + odds (step x) h

theorem step_pos {x : Nat} (hx : 0 < x) : 0 < step x := by
  unfold step
  split <;> omega

theorem step_law (x : Nat) : 2*step x = 3^(x%2)*x + x%2 := by
  by_cases hz : x%2 = 0
  · simp [step, hz]; omega
  · have ho : x%2=1 := by omega
    simp [step, ho]; omega

/-- The two-clock normalized contraction is sharp on the 1,2 cycle. -/
theorem two_clock (x : Nat) (hx : 0 < x) :
    3 * step (step x) ≤ 3^(x%2) * 3^((step x)%2) * x := by
  have h₁ := step_law x
  have h₂ := step_law (step x)
  generalize he : x%2 = e at *
  generalize hf : step x%2 = f at *
  have ee : e=0 ∨ e=1 := by omega
  have ff : f=0 ∨ f=1 := by omega
  rcases ee with rfl|rfl <;> rcases ff with rfl|rfl <;>
    simp only [Nat.pow_zero, Nat.pow_one, Nat.one_mul, Nat.mul_one] at * <;> omega

theorem paired_clock_budget (x j : Nat) (hx : 0 < x) :
    3^j * run x (2*j) ≤ 3^(odds x (2*j)) * x := by
  induction j generalizing x with
  | zero => simp [run, odds]
  | succ j ih =>
    rw [show 2*(j+1)=2*j+1+1 by omega, run, run, odds, odds]
    have h₁ := Nat.mul_le_mul_left 3 (ih (step (step x)) (step_pos (step_pos hx)))
    have h₂ := Nat.mul_le_mul_left (3^(odds (step (step x)) (2*j))) (two_clock x hx)
    rw [Nat.pow_succ, Nat.pow_add, Nat.pow_add]
    grind

end Collatz.ParentCertificate

#print axioms Collatz.ParentCertificate.numerator_unit
#print axioms Collatz.ParentCertificate.recover_complete
#print axioms Collatz.ParentCertificate.recover_sound
#print axioms Collatz.ParentCertificate.terminal_powers
#print axioms Collatz.ParentCertificate.two_clock
#print axioms Collatz.ParentCertificate.paired_clock_budget
