module

public import Mathlib.Algebra.Polynomial.Expand
import Lean.Elab.Tactic.Omega

/-! Finite algebra for the reducible binary-substitution argument. -/
@[expose] public section

namespace BinaryDigitMahler

open Polynomial

/-- If a rational series equals a digit polynomial times its base-`a`
substitution, the reduced fraction has a constant numerator and linear denominator. -/
theorem rational_digit_degrees {K : Type*} [Field K] {a : ℕ} (ha : 2 ≤ a)
    {A B P : K[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hP : P ≠ 0)
    (hcop : IsCoprime A B) (hdeg : P.natDegree + 1 = a)
    (heq : A * expand K a B = P * B * expand K a A) :
    A.natDegree = 0 ∧ B.natDegree = 1 := by
  have ha_pos : 0 < a := by omega
  have hcop' : IsCoprime (expand K a A) (expand K a B) :=
    (isCoprime_expand ha_pos.ne').2 hcop
  have hdiv : expand K a A ∣ A * expand K a B := by
    rw [heq]
    exact dvd_mul_left _ _
  have hle := natDegree_le_of_dvd (hcop'.dvd_of_dvd_mul_right hdiv) hA
  rw [natDegree_expand] at hle
  have hAdeg : A.natDegree = 0 := by
    by_contra hn
    have hlt := Nat.mul_lt_mul_of_pos_left (show 1 < a by omega) (Nat.pos_of_ne_zero hn)
    exact (not_lt_of_ge hle) (by simpa using hlt)
  have hEA : expand K a A ≠ 0 := (expand_ne_zero ha_pos).2 hA
  have hEB : expand K a B ≠ 0 := (expand_ne_zero ha_pos).2 hB
  have hbalance := congrArg natDegree heq
  rw [natDegree_mul hA hEB, natDegree_mul (mul_ne_zero hP hB) hEA,
      natDegree_mul hP hB] at hbalance
  simp only [natDegree_expand, hAdeg, zero_add, zero_mul, add_zero] at hbalance
  rw [← hdeg, Nat.mul_add, Nat.mul_one] at hbalance
  have hmul : B.natDegree * P.natDegree = 1 * P.natDegree := by
    simpa only [one_mul] using Nat.add_right_cancel hbalance
  exact ⟨hAdeg, Nat.eq_of_mul_eq_mul_right (by omega) hmul⟩

#print axioms rational_digit_degrees

end BinaryDigitMahler
