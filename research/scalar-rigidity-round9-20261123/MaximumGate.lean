import Mathlib.Tactic

/-! Finite clock arithmetic. The actual pressure-product input remains
source-qualified written mathematics in MAXIMUM_GATE.md. -/
namespace Collatz.ScalarRigidityRoundNine.MaximumGate

set_option autoImplicit false

theorem coefficient_identity (t ell : ℕ) :
    (2 : ℚ) ^ (1 + 3 * t + 5 * ell) / 3 ^ (1 + 2 * t + 2 * ell) =
      (2 / 3 : ℚ) * (8 / 9 : ℚ) ^ t * (32 / 9 : ℚ) ^ ell := by
  simp only [pow_add, pow_mul, div_pow]
  norm_num
  ring

theorem seven_pair_obstruction :
    (1 : ℚ) < (2 / 3) * (8 / 9 : ℚ) ^ 7 * (32 / 9) := by
  norm_num

theorem rational_return_gate (t ell : ℕ) (hell : 1 ≤ ell)
    (hclock : (2 / 3 : ℚ) * (8 / 9 : ℚ) ^ t * (32 / 9 : ℚ) ^ ell < 1) :
    8 ≤ t := by
  by_contra ht
  have ht7 : t ≤ 7 := by omega
  have hlow : (8 / 9 : ℚ) ^ 7 ≤ (8 / 9 : ℚ) ^ t :=
    pow_le_pow_of_le_one (by norm_num) (by norm_num) ht7
  have hpaid : (32 / 9 : ℚ) ≤ (32 / 9 : ℚ) ^ ell := by
    have hh := pow_le_pow_right₀ (show (1 : ℚ) ≤ 32 / 9 by norm_num) hell
    simpa using hh
  have hlower : (2 / 3 : ℚ) * (8 / 9 : ℚ) ^ 7 * (32 / 9) ≤
      (2 / 3 : ℚ) * (8 / 9 : ℚ) ^ t * (32 / 9 : ℚ) ^ ell := by
    apply mul_le_mul
    · exact mul_le_mul_of_nonneg_left hlow (by norm_num)
    · exact hpaid
    · norm_num
    · positivity
  have hstrict := seven_pair_obstruction
  linarith

/-- Complete actual-clock inequalities imply at least eight initial low pairs. -/
theorem complete_clock_gate (t ell clock : ℕ) (hell : 1 ≤ ell)
    (hcharge : 1 + 3 * t + 5 * ell ≤ clock)
    (hpressure : (2 : ℚ) ^ clock < 3 ^ (1 + 2 * t + 2 * ell)) :
    8 ≤ t := by
  have hp := pow_le_pow_right₀ (show (1 : ℚ) ≤ 2 by norm_num) hcharge
  have hpos : (0 : ℚ) < 3 ^ (1 + 2 * t + 2 * ell) := by positivity
  have hratio : (2 : ℚ) ^ (1 + 3 * t + 5 * ell) /
      3 ^ (1 + 2 * t + 2 * ell) < 1 :=
    (div_lt_one hpos).2 (lt_of_le_of_lt hp hpressure)
  rw [coefficient_identity] at hratio
  exact rational_return_gate t ell hell hratio

theorem shifted_valuation_gate (a t : ℕ) (ha : a = 3 * t + 2) (ht : 8 ≤ t) :
    26 ≤ a ∧ a % 3 = 2 := by omega

end Collatz.ScalarRigidityRoundNine.MaximumGate
