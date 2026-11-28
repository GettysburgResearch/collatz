import ShiftedRampCores

namespace Collatz.ShiftedSiblingCarries

open Collatz.MersenneCrests (State next run run_add)
open Collatz.ShiftedRampCores (halving_run)

def multiplier (z : State) : Nat := if z.1 % 2 = 0 then 1 else 3

def sibling (x : Nat) : Nat := 64*x+21

def siblingOffset (z : State) : Nat := if z.1 % 2 = 0 then 21 else 43

theorem small_shift_step (z : State) :
    2*(2*(next z).1+1) = multiplier z * (2*z.1+1)+1 := by
  by_cases h : z.1 % 2 = 0
  · simp only [next, multiplier, ite_eq_left h, Nat.one_mul]
    omega
  · simp only [next, multiplier, ite_eq_right h]
    omega

theorem sibling_shift_step (z : State) :
    2*sibling (next z).1 = multiplier z * sibling z.1+siblingOffset z := by
  by_cases h : z.1 % 2 = 0
  · simp only [sibling, next, multiplier, siblingOffset, ite_eq_left h, Nat.one_mul]
    omega
  · simp only [sibling, next, multiplier, siblingOffset, ite_eq_right h]
    omega

def slope (z : State) : Nat → Nat
  | 0 => 1
  | n+1 => multiplier (run z n) * slope z n

def carry (delta : State → Nat) (z : State) : Nat → Nat
  | 0 => 0
  | n+1 => multiplier (run z n) * carry delta z n + 2^n * delta (run z n)

/-- Exact positive-state composition for either physical shift. -/
theorem carry_identity (W : Nat → Nat) (delta : State → Nat)
    (one : ∀ z, 2*W (next z).1 = multiplier z * W z.1 + delta z)
    (z : State) (n : Nat) :
    2^n * W (run z n).1 = slope z n * W z.1 + carry delta z n := by
  induction n with
  | zero => simp [run, slope, carry]
  | succ n ih =>
    let m := multiplier (run z n)
    calc
      _ = 2^n*(2*W (next (run z n)).1) := by rw [Nat.pow_succ]; ac_rfl
      _ = m*(2^n*W (run z n).1)+2^n*delta (run z n) := by
        rw [one, Nat.mul_add]
        dsimp only [m]
        ac_rfl
      _ = _ := by
        rw [ih, Nat.mul_add]
        dsimp only [m, slope, carry]
        ac_rfl

theorem positive_carry (delta : State → Nat) (positive : ∀ z, 0 < delta z)
    (z : State) (n : Nat) : 0 < carry delta z (n+1) := by
  have hp := Nat.mul_pos (Nat.pow_pos (by decide : 0 < 2) : 0 < 2^n) (positive (run z n))
  unfold carry
  omega

/-- The upper bound written without truncated subtraction. -/
theorem carry_bound (delta : State → Nat) (C : Nat) (bound : ∀ z, delta z ≤ C)
    (z : State) (n : Nat) : carry delta z n + C * 2^n ≤ C * 3^n := by
  induction n with
  | zero => simp [carry]
  | succ n ih =>
    have hm : multiplier (run z n) ≤ 3 := by
      unfold multiplier
      split <;> decide
    have ha := Nat.mul_le_mul_right (carry delta z n) hm
    have hb := Nat.mul_le_mul_left (2^n) (bound (run z n))
    have h2 : C * 2^(n+1) = 2*(2^n*C) := by rw [Nat.pow_succ]; ac_rfl
    have h3 : C * 3^(n+1) = 3*(C*3^n) := by rw [Nat.pow_succ]; ac_rfl
    rw [carry, h2, h3]
    rw [Nat.mul_comm C (2^n)] at ih
    omega

theorem gcd_divides_carry (W : Nat → Nat) (delta : State → Nat)
    (one : ∀ z, 2*W (next z).1 = multiplier z * W z.1 + delta z)
    (z : State) (n : Nat) :
    Nat.gcd (W z.1) (W (run z n).1) ∣ carry delta z n := by
  have hd := Nat.dvd_mul_left_of_dvd (Nat.gcd_dvd_right (W z.1) (W (run z n).1)) (2^n)
  rw [carry_identity W delta one z n] at hd
  exact (Nat.dvd_add_iff_right (Nat.dvd_mul_left_of_dvd (Nat.gcd_dvd_left _ _) _)).mpr hd

theorem sibling_unit (x : Nat) : sibling x % 3 = x % 3 := by
  unfold sibling
  omega

/-- The ordinary sibling itself reaches the exact next shortcut state with
the same augmented odd count, using six additional even divisions. -/
theorem sibling_merge (x q : Nat) (odd : x % 2 = 1) :
    run (sibling x,q) 7 = next (x,q) := by
  have ho : sibling x % 2 = 1 := by unfold sibling; omega
  have hs : next (sibling x,q) = (64*((3*x+1)/2),q+1) := by
    simp only [next, ho, Nat.one_ne_zero, ite_false]
    unfold sibling
    congr 1
    omega
  calc
    _ = run (next (sibling x,q)) 6 := by
      rw [show (7 : Nat) = 1+6 by decide, run_add]
      rfl
    _ = ((3*x+1)/2,q+1) := by
      rw [hs]
      exact halving_run 6 ((3*x+1)/2) (q+1)
    _ = _ := by simp [next, odd]

end Collatz.ShiftedSiblingCarries
