import Mathlib.Data.Rat.Lemmas
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-! Exact denominator bookkeeping for the two independent periodic forcings.
The written construction supplies the coprimality and divisibility hypotheses.
This file proves that cancelling the common factor leaves the *entire*
product of the two remaining factors as the reduced rational denominator. -/
namespace CoprimeCancellation

def numerator (C P Q U V : ℤ) : ℤ := C*U*V + P*V + Q*U

theorem numerator_coprime (C P Q U V : ℤ)
    (hUV : IsCoprime U V) (hP : IsCoprime P U) (hQ : IsCoprime Q V) :
    IsCoprime (numerator C P Q U V) (U*V) := by
  have hu : IsCoprime (P*V + (C*V+Q)*U) U :=
    (hP.mul_left hUV.symm).add_mul_right_left (C*V+Q)
  have hv : IsCoprime (Q*U + (C*U+P)*V) V :=
    (hQ.mul_left hUV).add_mul_right_left (C*U+P)
  have heu : numerator C P Q U V = P*V + (C*V+Q)*U := by
    unfold numerator
    ring
  have hev : numerator C P Q U V = Q*U + (C*U+P)*V := by
    unfold numerator
    ring
  rw [← heu] at hu
  rw [← hev] at hv
  exact hu.mul_right hv

theorem quotient_coprime (C P Q D U V K : ℤ)
    (hUV : IsCoprime U V) (hP : IsCoprime P U) (hQ : IsCoprime Q V)
    (hcancel : numerator C P Q U V = D*K) :
    IsCoprime K (U*V) := by
  apply (numerator_coprime C P Q U V hUV hP hQ).of_isCoprime_of_dvd_left
  exact ⟨D, by rw [hcancel]; ring⟩

theorem fraction_after_cancel (C P Q D U V K : ℤ) (hD : D ≠ 0)
    (hcancel : numerator C P Q U V = D*K) :
    (numerator C P Q U V : ℚ) / (D*U*V : ℤ) = (K : ℚ) / (U*V : ℤ) := by
  rw [hcancel]
  push_cast
  rw [mul_assoc (D : ℚ) U V]
  exact mul_div_mul_left _ _ (by exact_mod_cast hD)

theorem exact_reduced_denominator (C P Q D U V K : ℤ) (hD : D ≠ 0)
    (hpositive : 0 < U*V)
    (hUV : IsCoprime U V) (hP : IsCoprime P U) (hQ : IsCoprime Q V)
    (hcancel : numerator C P Q U V = D*K) :
    (((numerator C P Q U V : ℚ) / (D*U*V : ℤ)).den : ℤ) = U*V := by
  rw [fraction_after_cancel C P Q D U V K hD hcancel]
  apply Rat.den_div_eq_of_coprime hpositive
  have hc := Int.isCoprime_iff_gcd_eq_one.mp
    (quotient_coprime C P Q D U V K hUV hP hQ hcancel)
  exact hc

#print axioms numerator_coprime
#print axioms quotient_coprime
#print axioms fraction_after_cancel
#print axioms exact_reduced_denominator

end CoprimeCancellation
