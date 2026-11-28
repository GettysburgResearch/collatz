import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Integer certificate for the ordinary orbit phase error.
The bottom H is imposed on the actual departures of this single starting n. -/
namespace Collatz.OrdinaryPhase

def mark (n : Nat) : Nat := if n % 2 = 0 then 0 else 1

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | t+1, n => orbit t (step n)

def count : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, n => mark n + count t (step n)

theorem oneStep (n H : Nat) (hne : H ≤ n) :
    3 ^ mark n * n ≤ 2 * step n ∧
    (3*H) * (2 * step n) ≤ (3*H+1) * (3 ^ mark n * n) := by
  by_cases he : n % 2 = 0
  · have h : 2 * (n/2) = n := by omega
    simp only [step, mark, ite_eq_left he, h, Nat.pow_zero, Nat.one_mul]
    exact ⟨le_rfl, by nlinarith⟩
  · have h : 2 * ((3*n+1)/2) = 3*n+1 := by omega
    simp only [step, mark, ite_eq_right he, h, Nat.pow_one]
    exact ⟨by omega, by nlinarith⟩

theorem ordinaryPhaseBound (n H t : Nat) (floorH : ∀ i < t, H ≤ orbit i n) :
    3 ^ count t n * n ≤ 2 ^ t * orbit t n ∧
    (3*H)^t * (2^t * orbit t n) ≤ (3*H+1)^t * (3 ^ count t n * n) := by
  induction t generalizing n with
  | zero => simp [orbit, count]
  | succ t ih =>
    have h₀ := oneStep n H (floorH 0 (Nat.succ_pos t))
    have h₁ := ih (step n) (fun i hi => floorH (i+1) (Nat.succ_lt_succ hi))
    change 3^(mark n + count t (step n)) * n ≤ 2^(t+1) * orbit t (step n) ∧ _
    constructor
    · calc
        3^(mark n + count t (step n)) * n
            = 3^count t (step n) * (3^mark n * n) := by rw [pow_add]; ring
        _ ≤ 3^count t (step n) * (2 * step n) := Nat.mul_le_mul_left _ h₀.1
        _ = 2 * (3^count t (step n) * step n) := by ring
        _ ≤ 2 * (2^t * orbit t (step n)) := Nat.mul_le_mul_left _ h₁.1
        _ = 2^(t+1) * orbit t (step n) := by ring
    · change (3*H)^(t+1) * (2^(t+1) * orbit t (step n)) ≤
          (3*H+1)^(t+1) * (3^(mark n + count t (step n)) * n)
      calc
        _ = (2*(3*H)) * ((3*H)^t * (2^t * orbit t (step n))) := by ring
        _ ≤ (2*(3*H)) * ((3*H+1)^t * (3^count t (step n) * step n)) :=
          Nat.mul_le_mul_left _ h₁.2
        _ = ((3*H+1)^t * 3^count t (step n)) * ((3*H) * (2 * step n)) := by ring
        _ ≤ ((3*H+1)^t * 3^count t (step n)) *
             ((3*H+1) * (3^mark n * n)) := Nat.mul_le_mul_left _ h₀.2
        _ = _ := by rw [pow_add (3:Nat) (mark n)]; ring

#print axioms ordinaryPhaseBound

end Collatz.OrdinaryPhase
