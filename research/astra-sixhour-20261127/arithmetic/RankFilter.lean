import Mathlib.Data.Rat.Lemmas
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! Finite summation and complete-denominator identities for the physical rank filter. -/

namespace Collatz.RankFilter

set_option autoImplicit false
open scoped BigOperators

/-- Telescope a filter over the native rank recurrence and its backward coefficient recurrence. -/
theorem telescope {a b g u v : ℕ → ℚ} (L : ℕ)
    (edge : ∀ j < L, a j * u (j + 1) = 3 * u j + v j)
    (coefficient : ∀ j < L, 3 * g (j + 1) = a j * (g j - b j)) :
    (∑ j ∈ Finset.range L, b j * u j) + g L * u L =
      g 0 * u 0 + ∑ j ∈ Finset.range L, ((g j - b j) / 3) * v j := by
  induction L with
  | zero => simp
  | succ n ih =>
    have prev := ih (fun j hj => edge j (Nat.lt_succ_of_lt hj))
      (fun j hj => coefficient j (Nat.lt_succ_of_lt hj))
    have step : b n * u n + g (n + 1) * u (n + 1) =
        g n * u n + ((g n - b n) / 3) * v n := by
      linear_combination u (n + 1) / 3 * coefficient n (Nat.lt_succ_self n) +
        ((g n - b n) / 3) * edge n (Nat.lt_succ_self n)
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    linear_combination prev + step

/-- The integer ternary digits clear the full original phase after a dyadic dilation. -/
theorem integral_residual {a b g u : ℕ → ℚ} {t v : ℕ → ℤ} {D L : ℕ}
    (edge : ∀ j < L, a j * u (j + 1) = 3 * u j + v j)
    (coefficient : ∀ j < L, 3 * g (j + 1) = a j * (g j - b j))
    (start : (D : ℚ) * g 0 = 1)
    (digit : ∀ j < L, (D : ℚ) * ((g j - b j) / 3) = t j) :
    (D : ℚ) * ((∑ j ∈ Finset.range L, b j * u j) + g L * u L) =
      u 0 + ((∑ j ∈ Finset.range L, t j * v j : ℤ) : ℚ) := by
  rw [telescope L edge coefficient, mul_add, ← mul_assoc, start, one_mul,
    Finset.mul_sum, Int.cast_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro j hj
  rw [← mul_assoc, digit j (Finset.mem_range.mp hj), Int.cast_mul]

/-- A coprime dilation and an integer translate preserve the complete reduced denominator. -/
theorem complete_denominator {D : ℕ} {w u : ℚ} {z : ℤ}
    (cop : D.Coprime w.den) (residual : (D : ℚ) * w = u + z) : w.den = u.den := by
  have h := congrArg Rat.den residual
  rw [Rat.mul_den, Rat.add_intCast_den] at h
  simpa [Int.natAbs_mul, (cop.mul_left w.reduced).gcd_eq_one] using h

#print axioms telescope
#print axioms integral_residual
#print axioms complete_denominator

end Collatz.RankFilter
