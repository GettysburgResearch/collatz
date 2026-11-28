import GateReturnBudget

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeCycleGrade

open Collatz.GateReturnBudget

/-- The affine correction in an actual native path is nonnegative. -/
theorem native_power_lower (y e : Nat → Nat) (q : Nat)
    (step : ∀ i, i < q → 2 ^ e i * y (i + 1) = 3 * y i + 1) :
    3 ^ q * y 0 ≤ 2 ^ clock e q * y q := by
  induction q with
  | zero => simp [clock]
  | succ q ih =>
    have h := ih (fun i hi => step i (by omega))
    have hs := step q (by omega)
    calc
      3 ^ (q + 1) * y 0 = 3 * (3 ^ q * y 0) := by rw [pow_succ]; ring
      _ ≤ 3 * (2 ^ clock e q * y q) := Nat.mul_le_mul_left 3 h
      _ ≤ 2 ^ clock e (q + 1) * y (q + 1) := by
        simp only [clock, pow_add]
        calc
          _ ≤ 3 * (2 ^ clock e q * y q) + 2 ^ clock e q := Nat.le_add_right _ _
          _ = 2 ^ clock e q * (3 * y q + 1) := by ring
          _ = _ := by rw [← hs]; ring

/-- Every nonempty positive native cycle has a strictly positive real
affine correction, hence its binary multiplier exceeds its ternary one. -/
theorem cycle_power_gap (y e : Nat → Nat) (q : Nat)
    (step : ∀ i, i < q → 2 ^ e i * y (i + 1) = 3 * y i + 1)
    (nonempty : 0 < q) (positive : 0 < y 0) (closed : y q = y 0) :
    3 ^ q < 2 ^ clock e q := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt nonempty)
  have h := native_power_lower y e k (fun i hi => step i (by omega))
  have hs := step k (by omega)
  have hp : 0 < (2 : Nat) ^ clock e k := by positivity
  have strict : 3 ^ (k + 1) * y 0 < 2 ^ clock e (k + 1) * y (k + 1) := by
    calc
      _ = 3 * (3 ^ k * y 0) := by rw [pow_succ]; ring
      _ ≤ 3 * (2 ^ clock e k * y k) := Nat.mul_le_mul_left 3 h
      _ < 3 * (2 ^ clock e k * y k) + 2 ^ clock e k := by omega
      _ = 2 ^ clock e k * (3 * y k + 1) := by ring
      _ = _ := by simp only [clock, pow_add]; rw [← hs]; ring
  rw [closed] at strict
  exact (Nat.mul_lt_mul_right positive).mp strict

/-- A positive native cycle with all odd sources at least three has positive
net shortcut grade. This is the integer part of the strict gate-rate gap. -/
theorem cycle_positive_grade (y e : Nat → Nat) (q : Nat)
    (step : ∀ i, i < q → 2 ^ e i * y (i + 1) = 3 * y i + 1)
    (floor : ∀ i, i < q → 3 ≤ y i)
    (nonempty : 0 < q) (closed : y q = y 0) :
    clock e q < 2 * q := by
  have positive : 0 < y 0 := by have := floor 0 nonempty; omega
  have upper := native_height_product y e q step floor
  rw [closed] at upper
  have reduced : 2 ^ clock e q * 3 ^ q ≤ 10 ^ q :=
    Nat.le_of_mul_le_mul_right upper positive
  by_contra bad
  have he : 2 * q ≤ clock e q := by omega
  have hp : (2 : Nat) ^ (2 * q) ≤ 2 ^ clock e q :=
    Nat.pow_le_pow_right (by decide) he
  have h12 : (12 : Nat) ^ q ≤ 10 ^ q := by
    calc
      _ = 2 ^ (2 * q) * 3 ^ q := by
        rw [show 2 * q = q + q by omega, pow_add,
          show (12 : Nat) = 2 * 2 * 3 by rfl, mul_pow, mul_pow]
      _ ≤ 2 ^ clock e q * 3 ^ q := Nat.mul_le_mul_right _ hp
      _ ≤ _ := reduced
  have impossible : (10 : Nat) ^ q < 12 ^ q :=
    Nat.pow_lt_pow_left (by decide) (Nat.ne_of_gt nonempty)
  omega

end Collatz.NativeCycleGrade
