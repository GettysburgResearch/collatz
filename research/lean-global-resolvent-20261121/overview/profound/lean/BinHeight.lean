import Mathlib.Data.Nat.Log
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
An unconditional height budget for the ternary occupation bins.  The map is
the ordinary shortcut map on natural numbers.  No convergence, predecessor
density, or harmonic-reference hypothesis occurs in this module.
-/

set_option autoImplicit false

namespace CollatzBinHeight

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit (p : ℕ) : ℕ → ℕ
  | 0 => p
  | k + 1 => step (orbit p k)

def oddCount (p : ℕ) : ℕ → ℕ
  | 0 => 0
  | k + 1 => oddCount p k + if orbit p k % 2 = 0 then 0 else 1

theorem step_positive {n : ℕ} (hn : 0 < n) : 0 < step n := by
  unfold step
  split <;> omega

theorem orbit_positive {p : ℕ} (hp : 0 < p) (k : ℕ) : 0 < orbit p k := by
  induction k with
  | zero => exact hp
  | succ k ih => exact step_positive ih

theorem even_square_budget {n : ℕ} (h : n % 2 = 0) :
    (step n + 1)^2 ≤ (n + 1)^2 := by
  simp only [step, h, ite_true]
  have : n / 2 ≤ n := Nat.div_le_self n 2
  exact Nat.pow_le_pow_left (Nat.add_le_add_right this 1) 2

theorem odd_square_budget {n : ℕ} (h : n % 2 ≠ 0) :
    (step n + 1)^2 ≤ 3 * (n + 1)^2 := by
  have hn : n % 2 = 1 := by omega
  have heq : 2 * step n = 3 * n + 1 := by
    simp only [step, h, ite_false]
    omega
  nlinarith

/-- Each actual odd decision costs a factor three in this squared-height
budget; even decisions cost no factor. -/
theorem orbit_square_budget (p k : ℕ) :
    (orbit p k + 1)^2 ≤ 3^(oddCount p k) * (p + 1)^2 := by
  induction k with
  | zero => simp [orbit, oddCount]
  | succ k ih =>
    by_cases h : orbit p k % 2 = 0
    · simpa [orbit, oddCount, h] using
        (even_square_budget h).trans ih
    · have stepBudget := odd_square_budget h
      have scaled := Nat.mul_le_mul_left 3 ih
      simpa [orbit, oddCount, h, pow_succ, Nat.mul_assoc,
        Nat.mul_comm, Nat.mul_left_comm] using stepBudget.trans scaled

/-- The least power of three above a positive centre is strictly below
three times that centre, including the centre one. -/
theorem ceiling_power_lt {c : ℕ} (hc : 0 < c) :
    3^(Nat.clog 3 c) < 3 * c := by
  by_cases h : c = 1
  · simp [h]
  · have h1 : 1 < c := by omega
    have positive := Nat.clog_pos (by omega : 1 < 3) h1
    have low := Nat.pow_pred_clog_lt_self (by omega : 1 < 3) h1
    have eq : Nat.clog 3 c = (Nat.clog 3 c - 1) + 1 := by omega
    rw [eq, pow_succ]
    simpa [Nat.mul_comm, Nat.pred_eq_sub_one] using
      (Nat.mul_lt_mul_of_pos_right low (by decide : 0 < 3))

/-- Finite algebraic core: a centre in bin t has height at most an
exponential in t times a fixed power of its unchanged original source. -/
theorem centre_bound_of_budget {p c n t : ℕ}
    (hc : 0 < c)
    (budget : (c + 1)^2 ≤ 3^n * (p + 1)^2)
    (bin : n = t + Nat.clog 3 c) :
    c + 1 ≤ 3^(t + 1) * (p + 1)^2 := by
  have ceiling := ceiling_power_lt hc
  rw [bin, pow_add] at budget
  have coarse : 3^t * 3^(Nat.clog 3 c) * (p+1)^2 ≤
      3^t * (3*c) * (p+1)^2 := by
    gcongr
  have combined := budget.trans coarse
  rw [pow_succ]
  nlinarith

/-- The height bound applies to every actual visit in a positive ternary
bin, including visits on cycles.  It does not discard the original source. -/
theorem actual_bin_centre_bound {p k t : ℕ}
    (hp : 0 < p)
    (bin : oddCount p k = t + Nat.clog 3 (orbit p k)) :
    orbit p k + 1 ≤ 3^(t + 1) * (p + 1)^2 :=
  centre_bound_of_budget (orbit_positive hp k) (orbit_square_budget p k) bin

end CollatzBinHeight
