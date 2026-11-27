import StaircaseAffine
import Mathlib.Algebra.Polynomial.Eval.Degree
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic.FieldSimp

/-! Rational polynomial identity behind the exact binary remainder. The sum
over t is truncated at an arbitrary finite length. Use a = 1/q. -/

namespace StaircasePade

open StaircaseAffine
open Polynomial

def term (a z : ℚ) (j : ℕ) : ℚ := z^j * a^(tri j)

theorem tri_add (n k : ℕ) : tri (n+k) = tri n + tri k + n*k := by
  induction k with
  | zero => simp [tri]
  | succ k ih => rw [Nat.add_succ, tri, ih, tri, Nat.mul_succ]; omega

theorem shifted_term (a z : ℚ) (ha : a ≠ 0) (hz : z ≠ 0) (m t k : ℕ) :
    term a z (m+t+k) / (z^k * a^(tri k+k*m)) = term a z (m+t) * (a^t)^k := by
  have h : tri (m+t+k) = tri (m+t) + (tri k+k*m) + t*k := by
    rw [tri_add (m+t) k]
    ring
  rw [term, term, h, pow_add z (m+t) k, pow_add a (tri (m+t) + (tri k+k*m)) (t*k),
      pow_add a (tri (m+t)) (tri k+k*m), ←pow_mul]
  field_simp

noncomputable def filterPoly (a : ℚ) (n : ℕ) : ℚ[X] :=
  ∏ j ∈ Finset.range n, (1 - C ((a^(j+1))⁻¹) * X)

theorem filter_at_root (a : ℚ) (ha : a ≠ 0) {t n : ℕ} (ht : 0 < t) (htn : t ≤ n) :
    (filterPoly a n).eval (a^t) = 0 := by
  rw [filterPoly, eval_prod]
  apply Finset.prod_eq_zero (i := t-1) (Finset.mem_range.mpr (by omega))
  have ht' : t-1+1 = t := by omega
  simp [ht', ha]

def block (a z : ℚ) (m t : ℕ) (P : ℚ[X]) : ℚ :=
  ∑ k ∈ Finset.range (P.natDegree+1),
    P.coeff k * (term a z (m+t+k) / (z^k * a^(tri k+k*m)))

theorem block_eq (a z : ℚ) (ha : a ≠ 0) (hz : z ≠ 0) (m t : ℕ) (P : ℚ[X]) :
    block a z m t P = P.eval (a^t) * term a z (m+t) := by
  rw [block, eval_eq_sum_range, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro k _
  rw [shifted_term a z ha hz]
  ring

theorem initial_remainder_vanishes (a z : ℚ) (ha : a ≠ 0) (hz : z ≠ 0) (n m : ℕ) :
    ∑ t ∈ Finset.range n, block a z m (t+1) (filterPoly a n) = 0 := by
  apply Finset.sum_eq_zero
  intro t ht
  rw [block_eq a z ha hz, filter_at_root a ha (by omega) (Finset.mem_range.mp ht), zero_mul]

theorem finite_remainder (a z : ℚ) (ha : a ≠ 0) (hz : z ≠ 0) (n m N : ℕ) :
    ∑ t ∈ Finset.range (n+N), block a z m (t+1) (filterPoly a n) =
    ∑ t ∈ Finset.range N, (filterPoly a n).eval (a^(n+t+1)) * term a z (m+(n+t+1)) := by
  rw [Finset.sum_range_add, initial_remainder_vanishes a z ha hz, zero_add]
  apply Finset.sum_congr rfl
  intro t _
  exact block_eq a z ha hz m (n+t+1) (filterPoly a n)

theorem uniform_exponent_gap : (3:ℕ)^80 < 2^127 := by decide
set_option exponentiation.threshold 800 in
set_option maxRecDepth 4000 in
theorem fixed_template_exponent_gap : (3:ℕ)^340 < 2^539 := by decide

end StaircasePade

#print axioms StaircasePade.tri_add
#print axioms StaircasePade.shifted_term
#print axioms StaircasePade.filter_at_root
#print axioms StaircasePade.block_eq
#print axioms StaircasePade.initial_remainder_vanishes
#print axioms StaircasePade.finite_remainder
#print axioms StaircasePade.uniform_exponent_gap
#print axioms StaircasePade.fixed_template_exponent_gap
