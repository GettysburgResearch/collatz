import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Lean.Elab.Tactic.Omega

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.GateReturnBudget

/-- The complete binary clock of a finite native odd path. -/
def clock (e : Nat → Nat) : Nat → Nat
  | 0 => 0
  | q + 1 => clock e q + e q

/-- Every odd source at least three has `3 * (3y+1) ≤ 10y`.
The product bound retains every native division exponent. -/
theorem native_height_product (y e : Nat → Nat) (q : Nat) :
    (∀ i, i < q → 2 ^ e i * y (i + 1) = 3 * y i + 1) →
    (∀ i, i < q → 3 ≤ y i) →
    2 ^ clock e q * 3 ^ q * y q ≤ 10 ^ q * y 0 := by
  induction q with
  | zero =>
    intro _ _
    simp [clock]
  | succ q ih =>
    intro step floor
    have hp := ih (fun i hi => step i (by omega))
      (fun i hi => floor i (by omega))
    have hs : 3 * (2 ^ e q * y (q + 1)) ≤ 10 * y q := by
      rw [step q (by omega)]
      have hq := floor q (by omega)
      omega
    calc
      2 ^ clock e (q + 1) * 3 ^ (q + 1) * y (q + 1) =
          (2 ^ clock e q * 3 ^ q) * (3 * (2 ^ e q * y (q + 1))) := by
            simp only [clock, pow_add, pow_succ]
            ring
      _ ≤ (2 ^ clock e q * 3 ^ q) * (10 * y q) :=
        Nat.mul_le_mul_left _ hs
      _ = 10 * (2 ^ clock e q * 3 ^ q * y q) := by ring
      _ ≤ 10 * (10 ^ q * y 0) := Nat.mul_le_mul_left 10 hp
      _ = 10 ^ (q + 1) * y 0 := by rw [pow_succ]; ring

/-- If the net shortcut grade is `a`, finite positive height bounds the
complete native clock. Completed strict-gate returns have this balance. -/
theorem completed_clock_budget (y e : Nat → Nat) (q a : Nat)
    (step : ∀ i, i < q → 2 ^ e i * y (i + 1) = 3 * y i + 1)
    (floor : ∀ i, i < q → 3 ≤ y i) (endpoint : 1 ≤ y q)
    (balance : clock e q + a = 2 * q) :
    6 ^ q ≤ 2 ^ a * 5 ^ q * y 0 := by
  have h := Nat.mul_le_mul_left (2 ^ a)
    (native_height_product y e q step floor)
  have left : 2 ^ a * (2 ^ clock e q * 3 ^ q * y q) =
      2 ^ q * (6 ^ q * y q) := by
    calc
      _ = 2 ^ (clock e q + a) * 3 ^ q * y q := by rw [pow_add]; ring
      _ = 2 ^ (2 * q) * 3 ^ q * y q := by rw [balance]
      _ = (2 ^ q * 2 ^ q) * 3 ^ q * y q := by
        rw [show 2 * q = q + q by omega, pow_add]
      _ = 2 ^ q * (6 ^ q * y q) := by
        rw [show (6 : Nat) = 2 * 3 by rfl, mul_pow]
        ring
  have right : 2 ^ a * (10 ^ q * y 0) =
      2 ^ q * (2 ^ a * 5 ^ q * y 0) := by
    rw [show (10 : Nat) = 2 * 5 by rfl, mul_pow]
    ring
  rw [left, right] at h
  have hp : 0 < (2 : Nat) ^ q := by positivity
  have hc : 6 ^ q * y q ≤ 2 ^ a * 5 ^ q * y 0 :=
    Nat.le_of_mul_le_mul_left h hp
  have hl : 6 ^ q ≤ 6 ^ q * y q := by
    simpa only [mul_one] using Nat.mul_le_mul_left (6 ^ q) endpoint
  exact le_trans hl hc

end Collatz.GateReturnBudget
