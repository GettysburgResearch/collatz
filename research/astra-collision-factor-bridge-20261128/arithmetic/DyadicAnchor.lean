import Mathlib.Data.Rat.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.Omega

/-!
# Exact denominator growth for the affine anchor recursion

These finite rational identities support the written obstruction to an
atomic stationary anchor measure. They do not formalize that measure
argument, the ordinary/Haar interchange, or a Collatz convergence result.
-/

namespace Collatz.DyadicAnchor

def affine (e : ℕ) (x : ℚ) : ℚ := (3 * x + 1) / 2 ^ e

theorem dyadic_numerator_odd (p : ℤ) (d : ℕ)
    (hp : Odd p) (hd : 0 < d) : Odd (3 * p + (2 : ℤ) ^ d) := by
  have hthree : Odd (3 : ℤ) := ⟨1, by norm_num⟩
  exact (hthree.mul hp).add_even (even_two.pow_of_ne_zero (Nat.ne_of_gt hd))

theorem dyadic_step_formula (p : ℤ) (d e : ℕ) :
    affine e ((p : ℚ) / (2 : ℚ) ^ d) =
      ((3 * p + (2 : ℤ) ^ d : ℤ) : ℚ) / (2 : ℚ) ^ (d + e) := by
  simp only [affine, Int.cast_add, Int.cast_mul, Int.cast_ofNat, Int.cast_pow,
    pow_add]
  field_simp

private lemma odd_fraction_denominator (p : ℤ) (d : ℕ) (hp : Odd p) :
    ((p : ℚ) / (2 : ℚ) ^ d).den = 2 ^ d := by
  have hc : Nat.Coprime p.natAbs ((2 : ℤ) ^ d).natAbs := by
    simpa [Int.natAbs_pow] using
      Nat.Coprime.pow_right d hp.natAbs.coprime_two_right
  have hh := Rat.den_div_eq_of_coprime
    (a := p) (b := (2 : ℤ) ^ d) (pow_pos (by norm_num) d) hc
  norm_num only [Int.cast_pow, Int.cast_ofNat] at hh
  exact_mod_cast hh

theorem dyadic_step_denominator (p : ℤ) (d e : ℕ)
    (hp : Odd p) (hd : 0 < d) :
    (affine e ((p : ℚ) / (2 : ℚ) ^ d)).den = 2 ^ (d + e) := by
  rw [dyadic_step_formula]
  exact odd_fraction_denominator _ _ (dyadic_numerator_odd p d hp hd)

theorem dyadic_step_denominator_grows (p : ℤ) (d e : ℕ)
    (hp : Odd p) (hd : 0 < d) (he : 0 < e) :
    ((p : ℚ) / (2 : ℚ) ^ d).den <
      (affine e ((p : ℚ) / (2 : ℚ) ^ d)).den := by
  rw [odd_fraction_denominator p d hp, dyadic_step_denominator p d e hp hd]
  exact Nat.pow_lt_pow_right (by norm_num) (Nat.lt_add_of_pos_right he)

theorem integer_anchor_has_nonintegral_branch (z : ℤ) :
    ∃ e : ℕ, 0 < e ∧ (affine e (z : ℚ)).den ≠ 1 := by
  have hn : (3 * z + 1 : ℤ) ≠ 0 := by omega
  let e : ℕ := (3 * z + 1).natAbs
  have he : 0 < e := Int.natAbs_pos.mpr hn
  refine ⟨e, he, ?_⟩
  intro hh
  have hdiv : (2 : ℤ) ^ e ∣ 3 * z + 1 := by
    apply (Rat.den_div_intCast_eq_one_iff (3 * z + 1) ((2 : ℤ) ^ e)
      (pow_ne_zero e (by norm_num))).mp
    simpa only [affine, Int.cast_add, Int.cast_mul, Int.cast_ofNat,
      Int.cast_one, Int.cast_pow] using hh
  have hle := Int.natAbs_le_of_dvd_ne_zero hdiv hn
  have hle' : 2 ^ e ≤ e := by
    simpa [Int.natAbs_pow, e] using hle
  have hlt : e < 2 ^ e := Nat.lt_two_pow_self
  omega

end Collatz.DyadicAnchor
