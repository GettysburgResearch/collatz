import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic

/-!
Finite algebra for the residual-unit cycle argument. The general
irreducibility of the reduced principal binomial and the complex-root
classification are proved in the accompanying written note, not assumed as
axioms here. The preservation theorem states its irreducibility premise.
-/
namespace CollatzResidualWord

noncomputable section

open Polynomial Finset

set_option maxHeartbeats 1200000

def numerator (p : ℕ) (d : ℕ → ℕ) : ℚ[X] :=
  ∑ i ∈ range p, C ((2 : ℚ) ^ d i) * X ^ (p - 1 - i)

def alternatingQuotient (p : ℕ) : ℚ[X] :=
  ∑ i ∈ range p, C ((4 : ℚ) ^ i) * X ^ (p - 1 - i)

theorem numerator_coefficient (p i : ℕ) (d : ℕ → ℕ) (hi : i < p) :
    (numerator p d).coeff (p - 1 - i) = (2 : ℚ) ^ d i := by
  classical
  unfold numerator
  rw [finsetSum_coeff]
  rw [Finset.sum_eq_single i]
  · rw [coeff_C_mul, coeff_X_pow_self, mul_one]
  · intro j hj hji
    have hj' : j < p := mem_range.mp hj
    have hne : p - 1 - j ≠ p - 1 - i := by omega
    rw [coeff_C_mul, coeff_X_pow]
    rw [ite_eq_right (Ne.symm hne), mul_zero]
  · intro h
    exact (h (mem_range.mpr hi)).elim

theorem alternating_coefficient (p i : ℕ) (hi : i < p) :
    (alternatingQuotient p).coeff (p - 1 - i) = (4 : ℚ) ^ i := by
  classical
  unfold alternatingQuotient
  rw [finsetSum_coeff]
  rw [Finset.sum_eq_single i]
  · rw [coeff_C_mul, coeff_X_pow_self, mul_one]
  · intro j hj hji
    have hj' : j < p := mem_range.mp hj
    have hne : p - 1 - j ≠ p - 1 - i := by omega
    rw [coeff_C_mul, coeff_X_pow]
    rw [ite_eq_right (Ne.symm hne), mul_zero]
  · intro h
    exact (h (mem_range.mpr hi)).elim

theorem alternating_factorization (p : ℕ) :
    alternatingQuotient p * (X - C (4 : ℚ)) = X ^ p - C ((4 : ℚ) ^ p) := by
  have h := geom_sum₂_mul (C (4 : ℚ)) (X : ℚ[X]) p
  simp only [← C_pow] at h
  unfold alternatingQuotient
  calc
    _ = -(∑ i ∈ range p, C ((4 : ℚ)^i) * X^(p-1-i)) *
        (C (4 : ℚ) - X) := by ring
    _ = -(C ((4 : ℚ)^p) - X^p) := by rw [neg_mul, h]
    _ = _ := by ring

private theorem numerator_ne_zero (p : ℕ) (d : ℕ → ℕ) (hp : 0 < p) :
    numerator p d ≠ 0 := by
  intro h
  have hc := numerator_coefficient p 0 d hp
  rw [h, coeff_zero] at hc
  exact (pow_ne_zero (d 0) (by norm_num : (2 : ℚ) ≠ 0)) hc.symm

private theorem alternating_ne_zero (p : ℕ) (hp : 0 < p) :
    alternatingQuotient p ≠ 0 := by
  intro h
  have hc := alternating_coefficient p 0 hp
  rw [h, coeff_zero] at hc
  norm_num at hc

private theorem numerator_degree (p : ℕ) (d : ℕ → ℕ) (hp : 0 < p) :
    (numerator p d).natDegree = p - 1 := by
  apply natDegree_eq_of_le_of_coeff_ne_zero
  · unfold numerator
    apply natDegree_sum_le_of_forall_le
    intro i _
    exact (natDegree_C_mul_X_pow_le _ _).trans (Nat.sub_le _ _)
  · have hc := numerator_coefficient p 0 d hp
    simp only [Nat.sub_zero] at hc
    rw [hc]
    positivity

private theorem alternating_degree (p : ℕ) (hp : 0 < p) :
    (alternatingQuotient p).natDegree = p - 1 := by
  apply natDegree_eq_of_le_of_coeff_ne_zero
  · unfold alternatingQuotient
    apply natDegree_sum_le_of_forall_le
    intro i _
    exact (natDegree_C_mul_X_pow_le _ _).trans (Nat.sub_le _ _)
  · have hc := alternating_coefficient p 0 hp
    simp only [Nat.sub_zero, pow_zero] at hc
    rw [hc]
    norm_num

theorem numerator_of_quotient_divides (p : ℕ) (d : ℕ → ℕ) (hp : 0 < p)
    (hdiv : alternatingQuotient p ∣ numerator p d) :
    numerator p d = C ((2 : ℚ) ^ d 0) * alternatingQuotient p := by
  obtain ⟨R, hR⟩ := hdiv
  have hR0 : R ≠ 0 := by
    intro hz
    apply numerator_ne_zero p d hp
    rw [hR, hz, mul_zero]
  have hdeg := congrArg Polynomial.natDegree hR
  rw [numerator_degree p d hp, natDegree_mul (alternating_ne_zero p hp) hR0,
    alternating_degree p hp] at hdeg
  have heqR := eq_C_of_natDegree_eq_zero (show R.natDegree = 0 by omega)
  rw [heqR, mul_comm] at hR
  have hc := congrArg (fun f : ℚ[X] => f.coeff (p-1)) hR
  have hn := numerator_coefficient p 0 d hp
  have ha := alternating_coefficient p 0 hp
  simp only [Nat.sub_zero, pow_zero] at hn ha
  rw [hn, coeff_C_mul, ha, mul_one] at hc
  rwa [← hc] at hR

theorem exponents_of_alternating_quotient (p : ℕ) (d : ℕ → ℕ)
    (h : numerator p d = C ((2 : ℚ) ^ d 0) * alternatingQuotient p) :
    ∀ i < p, d i = d 0 + 2 * i := by
  intro i hi
  have hc := congrArg (fun f : ℚ[X] => f.coeff (p-1-i)) h
  rw [numerator_coefficient p i d hi, coeff_C_mul, alternating_coefficient p i hi] at hc
  apply (pow_right_injective₀ (by norm_num : (0 : ℚ) < 2) (by norm_num : (2 : ℚ) ≠ 1))
  calc
    (2 : ℚ)^d i = 2^d 0 * 4^i := hc
    _ = 2^(d 0+2*i) := by rw [pow_add, pow_mul]; norm_num

theorem phase_of_alternating_quotient (p : ℕ) (d : ℕ → ℕ) (hp : 0 < p)
    (hbound : d (p-1) < 2*p)
    (h : numerator p d = C ((2 : ℚ) ^ d 0) * alternatingQuotient p) :
    d 0 ≤ 1 ∧ ∀ i < p, d i = d 0 + 2*i := by
  have he := exponents_of_alternating_quotient p d h
  have ht := he (p-1) (by omega)
  exact ⟨by omega, he⟩

theorem numerator_positive (p : ℕ) (d : ℕ → ℕ) (hp : 0 < p)
    (r : ℝ) (hr : 0 < r) :
    0 < (numerator p d).eval₂ (algebraMap ℚ ℝ) r := by
  classical
  simp only [numerator, eval₂_finsetSum, eval₂_mul, eval₂_pow, eval₂_C, eval₂_X]
  apply Finset.sum_pos'
  · intro i _
    positivity
  · exact ⟨0, mem_range.mpr hp, by positivity⟩

theorem principal_factor_survives (M G F₀ : ℚ[X]) (p : ℕ) (d : ℕ → ℕ)
    (hp : 0 < p) (r : ℝ) (hr : 0 < r)
    (hM : Irreducible M) (hMF : M ∣ G * F₀)
    (hGQ : G ∣ numerator p d)
    (hroot : M.eval₂ (algebraMap ℚ ℝ) r = 0) :
    M ∣ F₀ := by
  rcases hM.prime.dvd_mul.mp hMF with hMG | hMF₀
  · obtain ⟨R, hR⟩ := dvd_trans hMG hGQ
    have hz : (numerator p d).eval₂ (algebraMap ℚ ℝ) r = 0 := by
      rw [hR, eval₂_mul, hroot, zero_mul]
    have hpos := numerator_positive p d hp r hr
    rw [hz] at hpos
    exact (lt_irrefl 0 hpos).elim
  · exact hMF₀

theorem quotient_of_linear_residual (p : ℕ) (G : ℚ[X])
    (h : G * (X - C (4 : ℚ)) = X^p - C ((4 : ℚ)^p)) :
    G = alternatingQuotient p := by
  apply mul_right_cancel₀ (X_sub_C_ne_zero (4 : ℚ))
  exact h.trans (alternating_factorization p).symm

theorem alternating_profile_of_linear_residual (p : ℕ) (d : ℕ → ℕ)
    (hp : 0 < p) (hbound : d (p-1) < 2*p) (G : ℚ[X])
    (hF : G * (X - C (4 : ℚ)) = X^p - C ((4 : ℚ)^p))
    (hGQ : G ∣ numerator p d) :
    d 0 ≤ 1 ∧ ∀ i < p, d i = d 0 + 2*i := by
  have hG := quotient_of_linear_residual p G hF
  rw [hG] at hGQ
  exact phase_of_alternating_quotient p d hp hbound
    (numerator_of_quotient_divides p d hp hGQ)

theorem alternating_evaluation (p : ℕ) :
    (alternatingQuotient p).eval 3 = (4 : ℚ)^p - 3^p := by
  have h := congrArg (fun f : ℚ[X] => f.eval 3) (alternating_factorization p)
  simp only [eval_mul, eval_sub, eval_X, eval_C, eval_pow] at h
  linarith

theorem ordinary_realizer_of_linear_residual (p : ℕ) (d : ℕ → ℕ)
    (hp : 0 < p) (hbound : d (p-1) < 2*p) (G : ℚ[X])
    (hF : G * (X - C (4 : ℚ)) = X^p - C ((4 : ℚ)^p))
    (hGQ : G ∣ numerator p d) (n : ℕ)
    (hn : ((4 : ℚ)^p - 3^p) * n = (numerator p d).eval 3) :
    n = 1 ∨ n = 2 := by
  have hG := quotient_of_linear_residual p G hF
  rw [hG] at hGQ
  have hQ := numerator_of_quotient_divides p d hp hGQ
  have hphase := (phase_of_alternating_quotient p d hp hbound hQ).1
  rw [hQ, eval_mul, eval_C, alternating_evaluation] at hn
  have hgap : (3 : ℚ)^p < 4^p := pow_lt_pow_left₀ (by norm_num) (by norm_num) (by omega)
  have heq : (n : ℚ) = (2 : ℚ)^d 0 := by
    apply mul_left_cancel₀ (sub_ne_zero.mpr (ne_of_gt hgap))
    simpa only [mul_comm] using hn
  have heqNat : n = 2^d 0 := by exact_mod_cast heq
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hphase with hzero | hone
  · left
    simpa only [hzero, pow_zero] using heqNat
  · right
    simpa only [hone, pow_one] using heqNat

end
end CollatzResidualWord

#print axioms CollatzResidualWord.numerator_coefficient
#print axioms CollatzResidualWord.alternating_coefficient
#print axioms CollatzResidualWord.alternating_factorization
#print axioms CollatzResidualWord.numerator_of_quotient_divides
#print axioms CollatzResidualWord.exponents_of_alternating_quotient
#print axioms CollatzResidualWord.phase_of_alternating_quotient
#print axioms CollatzResidualWord.numerator_positive
#print axioms CollatzResidualWord.principal_factor_survives
#print axioms CollatzResidualWord.quotient_of_linear_residual
#print axioms CollatzResidualWord.alternating_profile_of_linear_residual
#print axioms CollatzResidualWord.alternating_evaluation
#print axioms CollatzResidualWord.ordinary_realizer_of_linear_residual
