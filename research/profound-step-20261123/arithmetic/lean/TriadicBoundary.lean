import Mathlib.Tactic

/-!
Finite algebra for the boundary-corrected triadic construction attempt.
No universal candidate, algebraicity, or Subspace-Theorem hypothesis is
asserted. The written note supplies the interpretation along an actual orbit.
-/

set_option autoImplicit false

namespace CollatzTriadicBoundary

def originalMultiplier (e : Bool) : ℤ := if e then 3 else 1
def dualMultiplier (e : Bool) : ℤ := if e then 1 else 3
def originalTerminal (e : Bool) : ℤ := if e then 1 else 2
def dualTerminal (e : Bool) : ℤ := if e then 2 else 1
def defect (e f : Bool) : ℤ :=
  (if e then 1 else 0) + (if f then 1 else 0) - 1

def originalCarryNext (k : ℕ) (e : Bool) (c : ℤ) : ℤ :=
  originalMultiplier e * c + (if e then 1 else 0) * 2 ^ k

def dualCarryNext (k : ℕ) (e : Bool) (d : ℤ) : ℤ :=
  dualMultiplier e * d + (if e then 0 else 1) * 2 ^ k

def originalBoundary (k : ℕ) (e : Bool) (c : ℤ) : ℤ :=
  2 ^ k * originalTerminal e - c

def dualBoundary (k : ℕ) (e : Bool) (d : ℤ) : ℤ :=
  2 ^ k * dualTerminal e - d

theorem original_boundary_recurrence (k : ℕ) (e f : Bool) (c : ℤ) :
    originalBoundary (k + 1) f (originalCarryNext k e c) =
      originalMultiplier e * originalBoundary k e c -
        2 ^ (k + 1) * defect e f := by
  cases e <;> cases f <;>
    simp [originalBoundary, originalCarryNext, originalMultiplier,
      originalTerminal, defect, pow_succ] <;> ring

theorem dual_boundary_recurrence (k : ℕ) (e f : Bool) (d : ℤ) :
    dualBoundary (k + 1) f (dualCarryNext k e d) =
      dualMultiplier e * dualBoundary k e d +
        2 ^ (k + 1) * defect e f := by
  cases e <;> cases f <;>
    simp [dualBoundary, dualCarryNext, dualMultiplier,
      dualTerminal, defect, pow_succ] <;> ring

theorem defect_zero_iff (e f : Bool) : defect e f = 0 ↔ e ≠ f := by
  cases e <;> cases f <;> decide

theorem defect_square (e f : Bool) (h : e = f) : defect e f ^ 2 = 1 := by
  subst f
  cases e <;> decide

theorem not_three_dvd_twice (p : ℤ) (hp : ¬ (3 : ℤ) ∣ p) :
    ¬ (3 : ℤ) ∣ 2 * p := by
  intro h
  have h3 : (3 : ℤ) ∣ 3 * p := dvd_mul_right 3 p
  have hsub := dvd_sub h3 h
  have heq : 3 * p - 2 * p = p := by ring
  rw [heq] at hsub
  exact hp hsub

theorem not_three_dvd_backward_odd (p : ℤ) (r : ℕ)
    (hr : 0 < r) (hp : ¬ (3 : ℤ) ∣ p) :
    ¬ (3 : ℤ) ∣ 2 * p - 3 ^ r := by
  intro h
  have hpow : (3 : ℤ) ∣ (3 : ℤ) ^ r := by
    obtain ⟨s, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hr)
    refine ⟨3 ^ s, ?_⟩
    rw [pow_succ]
    ring
  have hsum := dvd_add h hpow
  have heq : (2 * p - (3 : ℤ) ^ r) + 3 ^ r = 2 * p := by ring
  rw [heq] at hsum
  exact not_three_dvd_twice p hp hsum

theorem backward_even_fraction (p : ℤ) (r : ℕ) :
    2 * ((p : ℚ) / (3 : ℚ) ^ r) =
      ((2 * p : ℤ) : ℚ) / (3 : ℚ) ^ r := by
  push_cast
  ring

theorem backward_odd_fraction (p : ℤ) (r : ℕ) :
    (2 * ((p : ℚ) / (3 : ℚ) ^ r) - 1) / 3 =
      ((2 * p - 3 ^ r : ℤ) : ℚ) / (3 : ℚ) ^ (r + 1) := by
  push_cast
  rw [pow_succ]
  field_simp

def alternatingCarry : ℕ → ℤ
  | 0 => 0
  | m + 1 => 3 * alternatingCarry m + 2 * 4 ^ m

theorem alternating_carry_closed (m : ℕ) :
    alternatingCarry m = 2 * ((4 : ℤ) ^ m - 3 ^ m) := by
  induction m with
  | zero => simp [alternatingCarry]
  | succ m ih =>
      simp only [alternatingCarry, ih, pow_succ]
      ring

theorem alternating_residual (m : ℕ) :
    alternatingCarry m + 2 * (3 : ℤ) ^ m = 2 * 4 ^ m := by
  rw [alternating_carry_closed]
  ring

end CollatzTriadicBoundary
