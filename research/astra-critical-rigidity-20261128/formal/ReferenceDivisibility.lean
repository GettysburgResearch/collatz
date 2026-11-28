import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact integer denominator costs for physical reference arcs.
These are finite arithmetic kernels, not the Subspace Theorem. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.ReferenceDivisibility

theorem two_three_coprime : IsCoprime (2 : ℤ) 3 := by
  exact ⟨-1, 1, by norm_num⟩

theorem complete_dyadic_divisor (d g : ℕ) (u v : ℤ)
    (h : (2 : ℤ)^d * v = 3^g * u) : (2 : ℤ)^d ∣ u := by
  apply (two_three_coprime.pow (m := d) (n := g)).dvd_of_dvd_mul_left
  exact ⟨v, h.symm⟩

theorem nonzero_residual_height (d g : ℕ) (u v : ℤ)
    (h : (2 : ℤ)^d * v = 3^g * u) (hu : u ≠ 0) :
    (2 : ℤ)^d ≤ |u| :=
  Int.le_abs_of_dvd hu (complete_dyadic_divisor d g u v h)

/-- Both rational reference endpoints have already been cleared by a common
integer denominator h. The actual affine carry cancels exactly. -/
theorem reference_integer_law (d g : ℕ) (A B q h a b C : ℤ)
    (physical : (2 : ℤ)^d * B = 3^g * A + q*C)
    (reference : (2 : ℤ)^d * b = 3^g * a + h*C) :
    (2 : ℤ)^d * (h*B-q*b) = 3^g * (h*A-q*a) := by
  calc
    2^d * (h*B-q*b) = h*(2^d*B)-q*(2^d*b) := by ring
    _ = h*(3^g*A+q*C)-q*(3^g*a+h*C) := by rw [physical, reference]
    _ = 3^g*(h*A-q*a) := by ring

theorem reference_source_divisor (d g : ℕ) (A B q h a b C : ℤ)
    (physical : (2 : ℤ)^d * B = 3^g * A + q*C)
    (reference : (2 : ℤ)^d * b = 3^g * a + h*C) :
    (2 : ℤ)^d ∣ h*A-q*a :=
  complete_dyadic_divisor d g (h*A-q*a) (h*B-q*b)
    (reference_integer_law d g A B q h a b C physical reference)

theorem reference_source_height (d g : ℕ) (A B q h a b C : ℤ)
    (physical : (2 : ℤ)^d * B = 3^g * A + q*C)
    (reference : (2 : ℤ)^d * b = 3^g * a + h*C)
    (separated : h*A-q*a ≠ 0) :
    (2 : ℤ)^d ≤ |h| * |A| + |q| * |a| := by
  have lower := nonzero_residual_height d g (h*A-q*a) (h*B-q*b)
    (reference_integer_law d g A B q h a b C physical reference) separated
  calc
    2^d ≤ |h*A-q*a| := lower
    _ ≤ |h*A| + |q*a| := abs_sub _ _
    _ = |h| * |A| + |q| * |a| := by rw [abs_mul, abs_mul]

end Collatz.ReferenceDivisibility
