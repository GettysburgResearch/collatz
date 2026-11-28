import Mathlib.LinearAlgebra.Matrix.Adjugate
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic.NormNum

/-!
Integer determinant kernel for EFFECTIVE_WORST_LANDING.md.

The congruence coefficients have no height bound. A columnwise entry bound
controls the determinant by the Leibniz formula; an exact row congruence then
forces the determinant to vanish when its possible scaled size is below the
modulus. Cramer's selection of the actual packet columns, the box count and
the infinite valuation-count induction remain written arguments.
-/

set_option autoImplicit false

namespace Collatz.IntegerMinorConcentration

open scoped BigOperators Matrix
open Finset

variable {I : Type*} [Fintype I] [DecidableEq I]

/-- An integer row congruence forces every coefficient times the determinant
to be divisible by the same modulus. There is no coefficient-height premise. -/
theorem modulus_dvd_det_mul_coefficient
    (A : Matrix I I ℤ) (c : I → ℤ) (q : ℤ)
    (hrow : ∀ i, q ∣ (A.mulVec c) i) (j : I) :
    q ∣ A.det * c j := by
  have hdiv : q ∣ (A.adjugate.mulVec (A.mulVec c)) j := by
    change q ∣ ∑ i, A.adjugate j i * (A.mulVec c) i
    exact Finset.dvd_sum fun i _ => dvd_mul_of_dvd_right (hrow i) _
  simpa only [Matrix.mulVec_mulVec, Matrix.adjugate_mul,
    Matrix.smul_mulVec, Matrix.one_mulVec, Pi.smul_apply, smul_eq_mul] using hdiv

/-- The elementary determinant bound with a separate bound for each column.
In the landing application one column is bounded by `3^N`; the other columns
are bounded by `6^B`. -/
theorem abs_det_le_column_product
    (A : Matrix I I ℤ) (C : I → ℤ)
    (_hC : ∀ j, 0 ≤ C j) (hentry : ∀ i j, |A i j| ≤ C j) :
    |A.det| ≤ (Nat.factorial (Fintype.card I) : ℤ) * ∏ j, C j := by
  let abv : AbsoluteValue ℤ ℤ := AbsoluteValue.abs
  change abv A.det ≤ _
  calc
    abv A.det =
        abv (∑ σ : Equiv.Perm I, Equiv.Perm.sign σ • ∏ i, A (σ i) i) :=
      congrArg abv (Matrix.det_apply A)
    _ ≤ ∑ σ : Equiv.Perm I, abv (Equiv.Perm.sign σ • ∏ i, A (σ i) i) :=
      abv.sum_le _ _
    _ = ∑ σ : Equiv.Perm I, ∏ i, abv (A (σ i) i) := by
      apply Finset.sum_congr rfl
      intro σ _
      rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h
      · simp only [h, one_smul, abv.map_prod]
      · simp [h, Units.smul_def, abv.map_prod]
    _ ≤ ∑ _σ : Equiv.Perm I, ∏ j, C j := by
      apply Finset.sum_le_sum
      intro σ _
      apply Finset.prod_le_prod₀
      · intro i _
        exact abv.nonneg _
      · intro i _
        exact hentry (σ i) i
    _ = (Nat.factorial (Fintype.card I) : ℤ) * ∏ j, C j := by
      simp [Fintype.card_perm]

/-- The exact concentration step: a sufficiently large common row modulus
and one nonzero congruence coefficient force an integer minor to be zero.
All entry and scaling costs occur explicitly in the strict inequality. -/
theorem det_eq_zero_of_large_row_modulus
    (A : Matrix I I ℤ) (c : I → ℤ) (q : ℤ) (C : I → ℤ) (j : I)
    (hrow : ∀ i, q ∣ (A.mulVec c) i)
    (hC : ∀ i, 0 ≤ C i) (hentry : ∀ i k, |A i k| ≤ C k)
    (hc : c j ≠ 0)
    (hsize : |c j| * ((Nat.factorial (Fintype.card I) : ℤ) * ∏ i, C i) < |q|) :
    A.det = 0 := by
  have hdiv := modulus_dvd_det_mul_coefficient A c q hrow j
  have hbound := abs_det_le_column_product A C hC hentry
  have hsmall : |A.det * c j| < |q| := by
    rw [abs_mul, mul_comm]
    exact (mul_le_mul_of_nonneg_left hbound (abs_nonneg (c j))).trans_lt hsize
  have hnat : (A.det * c j).natAbs < q.natAbs := by
    rw [Int.abs_eq_natAbs, Int.abs_eq_natAbs] at hsmall
    exact_mod_cast hsmall
  have hzero : A.det * c j = 0 :=
    Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hdiv hnat
  exact (mul_eq_zero.mp hzero).resolve_right hc

end Collatz.IntegerMinorConcentration
