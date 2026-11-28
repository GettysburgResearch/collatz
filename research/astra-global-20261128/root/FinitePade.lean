import PadeArithmetic
import Mathlib.Tactic.FieldSimp

/-! Finite Padé cancellation, with an actual finite remainder for every coefficient.
There are no infinite series or assumed interpolation identities in this module. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FinitePade
open Collatz.PadeArithmetic
open scoped BigOperators

def term (q z : ℚ) (l : ℕ) : ℚ := z^l/q^(tri l)

noncomputable def rawCoeff (n m : ℕ) (q z : ℚ) (k : ℕ) : ℚ :=
  (padePoly n q).coeff k*q^(tri k+k*m)/z^k

noncomputable def headCoeff (n m : ℕ) (q z : ℚ) : ℚ :=
  ∑ k ∈ Finset.range (n+1), rawCoeff n m q z k

noncomputable def constantCoeff (n m : ℕ) (q z : ℚ) : ℚ :=
  ∑ k ∈ Finset.range (n+1),
    rawCoeff n m q z k*(∑ l ∈ Finset.range (k+m+1), term q z l)

def partialSum (q z : ℚ) (j : ℕ) : ℚ :=
  ∑ l ∈ Finset.range j, term q z l

noncomputable def leading (n m : ℕ) (q z : ℚ) : ℚ :=
  term q z (n+m+1)*(padePoly n q).eval ((q^(n+1))⁻¹)

theorem polynomial_root (n t : ℕ) (q : ℚ) (hq : q≠0)
    (ht : 0<t) (htn : t≤n) :
    (padePoly n q).eval ((q^t)⁻¹)=0 := by
  simp only [padePoly,Polynomial.eval_prod,Polynomial.eval_sub,
    Polynomial.eval_one,Polynomial.eval_mul,Polynomial.eval_C,Polynomial.eval_X]
  apply Finset.prod_eq_zero (Finset.mem_range.mpr (show t-1<n by omega))
  rw [show t-1+1=t by omega,mul_inv_cancel₀ (pow_ne_zero t hq)]
  ring

theorem coefficient_term_shift (n m k t : ℕ) (q z : ℚ)
    (hq : q≠0) (hz : z≠0) :
    rawCoeff n m q z k*term q z (k+(m+t)) =
      (padePoly n q).coeff k*((q^t)⁻¹)^k*term q z (m+t) := by
  simp only [rawCoeff,term,tri_add,Nat.mul_add,pow_add,inv_pow,←pow_mul]
  rw [Nat.mul_comm t k]
  field_simp

theorem grouped_shift (n m t : ℕ) (q z : ℚ)
    (hq : q≠0) (hz : z≠0) :
    (∑ k ∈ Finset.range (n+1), rawCoeff n m q z k*term q z (k+(m+t))) =
      term q z (m+t)*(padePoly n q).eval ((q^t)⁻¹) := by
  rw [Polynomial.eval_eq_sum_range' (Nat.lt_succ_of_le (padePoly_degree n q)),
    Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  rw [coefficient_term_shift n m k t q z hq hz]
  ring

/-- The interpolation polynomial kills all but the last term of this finite window. -/
theorem finite_window (n m : ℕ) (q z : ℚ) (hq : q≠0) (hz : z≠0) :
    (∑ k ∈ Finset.range (n+1), rawCoeff n m q z k*
      (∑ t ∈ Finset.range (n+1), term q z (k+m+1+t))) = leading n m q z := by
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  have hg (t : ℕ) :
      (∑ k ∈ Finset.range (n+1), rawCoeff n m q z k*term q z (k+m+1+t)) =
        term q z (m+(t+1))*(padePoly n q).eval ((q^(t+1))⁻¹) := by
    calc
      _ = ∑ k ∈ Finset.range (n+1),
          rawCoeff n m q z k*term q z (k+(m+(t+1))) := by
            apply Finset.sum_congr rfl
            intro k hk
            rw [show k+m+1+t=k+(m+(t+1)) by omega]
      _ = _ := grouped_shift n m (t+1) q z hq hz
  simp_rw [hg]
  rw [Finset.sum_range_succ]
  have hzsum : (∑ t ∈ Finset.range n,
      term q z (m+(t+1))*(padePoly n q).eval ((q^(t+1))⁻¹))=0 := by
    apply Finset.sum_eq_zero
    intro t ht
    rw [polynomial_root n (t+1) q hq (by omega)
      (by have := Finset.mem_range.mp ht; omega),mul_zero]
  rw [hzsum,zero_add]
  unfold leading
  congr 2
  omega

theorem partial_window (n m k : ℕ) (q z : ℚ) :
    partialSum q z (n+m+k+2) = partialSum q z (k+m+1)+
      ∑ t ∈ Finset.range (n+1), term q z (k+m+1+t) := by
  unfold partialSum
  rw [show n+m+k+2=(k+m+1)+(n+1) by omega,Finset.sum_range_add]

/-- Exact finite identity before any height or valuation bound is applied. -/
theorem finite_identity (n m : ℕ) (q z y : ℚ) (hq : q≠0) (hz : z≠0) :
    headCoeff n m q z*y-constantCoeff n m q z =
      leading n m q z+
      ∑ k ∈ Finset.range (n+1),
        rawCoeff n m q z k*(y-partialSum q z (n+m+k+2)) := by
  have hs :
      (∑ k ∈ Finset.range (n+1),
        rawCoeff n m q z k*partialSum q z (n+m+k+2)) =
      constantCoeff n m q z+leading n m q z := by
    simp_rw [partial_window, mul_add]
    rw [Finset.sum_add_distrib, finite_window n m q z hq hz]
    rfl
  simp only [mul_sub,Finset.sum_sub_distrib,←Finset.sum_mul]
  rw [hs]
  unfold headCoeff
  ring

theorem scaled_finite_identity (n m : ℕ) (q z y D : ℚ) (hq : q≠0) (hz : z≠0) :
    (D*headCoeff n m q z)*y-D*constantCoeff n m q z =
      D*leading n m q z+
      ∑ k ∈ Finset.range (n+1),
        (D*rawCoeff n m q z k)*(y-partialSum q z (n+m+k+2)) := by
  have h := congrArg (fun v : ℚ => D*v) (finite_identity n m q z y hq hz)
  simpa only [mul_sub,mul_add,Finset.mul_sum,mul_assoc] using h

end Collatz.FinitePade
