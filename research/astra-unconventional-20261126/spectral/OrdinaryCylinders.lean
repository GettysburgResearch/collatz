import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact ordinary cylinders used in the written essential-spectrum argument.
The operator-theoretic compactness and spectral arguments are not asserted by
this file.  Every horizon below is finite; its starting integer may change. -/

namespace OrdinaryCylinders

def step (x : ℤ) : ℤ :=
  if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : ℕ → ℤ → ℤ
  | 0, x => x
  | k+1, x => run k (step x)

theorem step_even (x : ℤ) : step (2*x) = x := by
  simp [step]

theorem step_odd (x : ℤ) : step (2*x-1) = 3*x-1 := by
  have he : (2*x-1) % 2 ≠ 0 := by omega
  simp only [step, he, ite_false]
  omega

theorem run_add (h k : ℕ) (x : ℤ) :
    run (h+k) x = run k (run h x) := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    rw [Nat.succ_add]
    exact ih (step x)

theorem even_cylinder (h : ℕ) (u : ℤ) :
    run h ((2:ℤ)^h*u) = u := by
  induction h generalizing u with
  | zero => simp [run]
  | succ h ih =>
    have he : (2:ℤ)^(h+1)*u = 2*((2:ℤ)^h*u) := by
      rw [pow_succ]
      ring
    rw [he, run, step_even]
    exact ih u

theorem odd_cylinder (h : ℕ) (u : ℤ) :
    run h ((2:ℤ)^h*u-1) = (3:ℤ)^h*u-1 := by
  induction h generalizing u with
  | zero => simp [run]
  | succ h ih =>
    have he : (2:ℤ)^(h+1)*u-1 = 2*((2:ℤ)^h*u)-1 := by
      rw [pow_succ]
      ring
    rw [he, run, step_odd]
    have hr : 3*((2:ℤ)^h*u)-1 = (2:ℤ)^h*(3*u)-1 := by ring
    rw [hr, ih, pow_succ]
    ring

theorem even_prefix (h i : ℕ) (hi : i ≤ h) (u : ℤ) :
    run i ((2:ℤ)^h*u) = (2:ℤ)^(h-i)*u := by
  have he : (2:ℤ)^h*u = (2:ℤ)^i*((2:ℤ)^(h-i)*u) := by
    rw [←mul_assoc, ←pow_add, Nat.add_sub_of_le hi]
  rw [he, even_cylinder]

theorem odd_prefix (h i : ℕ) (hi : i ≤ h) (u : ℤ) :
    run i ((2:ℤ)^h*u-1) = (3:ℤ)^i*(2:ℤ)^(h-i)*u-1 := by
  have he : (2:ℤ)^h*u-1 = (2:ℤ)^i*((2:ℤ)^(h-i)*u)-1 := by
    rw [←mul_assoc, ←pow_add, Nat.add_sub_of_le hi]
  rw [he, odd_cylinder]
  ring

theorem even_above_floor (h i : ℕ) (hi : i ≤ h)
    (M u : ℤ) (hM : 0 ≤ M) (hu : M < u) :
    M < run i ((2:ℤ)^h*u) := by
  rw [even_prefix h i hi u]
  have hp : (1:ℤ) ≤ 2^(h-i) := one_le_pow₀ (by norm_num)
  nlinarith

theorem odd_above_floor (h i : ℕ) (hi : i ≤ h)
    (M u : ℤ) (hM : 0 ≤ M) (hu : M+1 < u) :
    M < run i ((2:ℤ)^h*u-1) := by
  rw [odd_prefix h i hi u]
  have hp : (1:ℤ) ≤ 2^(h-i) := one_le_pow₀ (by norm_num)
  have hq : (1:ℤ) ≤ 3^i := one_le_pow₀ (by norm_num)
  have hc : (1:ℤ) ≤ 3^i*2^(h-i) := by nlinarith
  nlinarith

theorem odd_endpoint_identity (h : ℕ) (u : ℤ) :
    (2:ℤ)^h * (run h ((2:ℤ)^h*u-1)+1) =
      (3:ℤ)^h * (((2:ℤ)^h*u-1)+1) := by
  rw [odd_cylinder]
  ring

theorem merger_pair (t : ℤ) :
    step (12*t+10) = 6*t+5 ∧ step (4*t+3) = 6*t+5 := by
  constructor
  · have h : 12*t+10 = 2*(6*t+5) := by ring
    rw [h, step_even]
  · have h : 4*t+3 = 2*(2*t+2)-1 := by ring
    rw [h, step_odd]
    ring

theorem doubled_pair (j : ℕ) (t : ℤ) :
    run (j+1) ((2:ℤ)^j*(12*t+10)) = 6*t+5 ∧
    run (j+1) ((2:ℤ)^j*(4*t+3)) = 6*t+5 := by
  rw [run_add, even_cylinder, run_add, even_cylinder]
  simpa [run] using merger_pair t

end OrdinaryCylinders

#print axioms OrdinaryCylinders.step_even
#print axioms OrdinaryCylinders.step_odd
#print axioms OrdinaryCylinders.run_add
#print axioms OrdinaryCylinders.even_cylinder
#print axioms OrdinaryCylinders.odd_cylinder
#print axioms OrdinaryCylinders.even_prefix
#print axioms OrdinaryCylinders.odd_prefix
#print axioms OrdinaryCylinders.even_above_floor
#print axioms OrdinaryCylinders.odd_above_floor
#print axioms OrdinaryCylinders.odd_endpoint_identity
#print axioms OrdinaryCylinders.merger_pair
#print axioms OrdinaryCylinders.doubled_pair
