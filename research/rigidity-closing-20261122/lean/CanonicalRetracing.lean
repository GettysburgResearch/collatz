import OriginalSourceEntropy
import Mathlib.Algebra.BigOperators.Field

/-!
Finite scalar bounds for the exact retracing probability of an inverse
harmonic flow along one forward orbit. The inputs are a positive monotone
capacity sequence and its upper bound. No Collatz or analytic statement is
assumed as an axiom. The path-law interpretation and limiting consequences
are in MOVING_INVERSE_WINDOW.md, not asserted to be formalized here.
-/

open scoped BigOperators

namespace CollatzCanonicalRetracing

theorem sum_increments (v : ℕ → ℝ) (k r : ℕ) :
    (∑ j ∈ Finset.range r, (v (k+j+1) - v (k+j))) = v (k+r) - v k := by
  induction r with
  | zero => simp
  | succ r ih =>
      rw [Finset.sum_range_succ, ih]
      simp only [Nat.add_succ]
      ring

theorem capacity_ratio_failure_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) (k r : ℕ) :
    1 - v k / v (k+r) ≤ (v (k+r) - v k) / v 0 := by
  have hbase : v 0 ≤ v (k+r) := hv (Nat.zero_le _)
  have hden : 0 < v (k+r) := lt_of_lt_of_le hpos hbase
  have hinc : 0 ≤ v (k+r) - v k := sub_nonneg.mpr (hv (Nat.le_add_right k r))
  calc
    1 - v k / v (k+r) = (v (k+r) - v k) / v (k+r) := by
      field_simp
    _ ≤ (v (k+r) - v k) / v 0 := by
      apply (div_le_div_iff₀ hden hpos).2
      nlinarith [mul_nonneg hinc (sub_nonneg.mpr hbase)]

theorem window_capacity_sum_le (v : ℕ → ℝ) (hv : Monotone v)
    {r N : ℕ} (hr : r ≤ N) :
    (∑ k ∈ Finset.range (N-r+1), (v (k+r) - v k))
      ≤ (r : ℝ) * (v N - v 0) := by
  have h := CollatzOriginalEntropy.sliding_window_cost_le
    (fun i => v (i+1) - v i)
    (fun i => sub_nonneg.mpr (hv (Nat.le_succ i))) hr
  simp_rw [sum_increments] at h
  have hN := sum_increments v 0 N
  simp only [Nat.zero_add] at hN
  rw [hN] at h
  exact h

theorem retracing_failure_sum_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) {C : ℝ} {r N : ℕ} (hbound : v N ≤ C)
    (hr : r ≤ N) :
    (∑ k ∈ Finset.range (N-r+1), (1 - v k / v (k+r)))
      ≤ (r : ℝ) * (C - v 0) / v 0 := by
  have hcost := window_capacity_sum_le v hv hr
  have hbound' : (r : ℝ) * (v N - v 0) ≤ (r : ℝ) * (C - v 0) :=
    mul_le_mul_of_nonneg_left (sub_le_sub_right hbound (v 0)) (Nat.cast_nonneg r)
  calc
    (∑ k ∈ Finset.range (N-r+1), (1 - v k / v (k+r)))
        ≤ ∑ k ∈ Finset.range (N-r+1), (v (k+r) - v k) / v 0 := by
      exact Finset.sum_le_sum (fun k _ => capacity_ratio_failure_le v hv hpos k r)
    _ = (∑ k ∈ Finset.range (N-r+1), (v (k+r) - v k)) / v 0 := by
      rw [Finset.sum_div]
    _ ≤ (r : ℝ) * (C - v 0) / v 0 :=
      div_le_div_of_nonneg_right (hcost.trans hbound') hpos.le

theorem retracing_failure_mean_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) {C : ℝ} {r N : ℕ} (hbound : v N ≤ C)
    (hr : r ≤ N) :
    (∑ k ∈ Finset.range (N-r+1), (1 - v k / v (k+r))) / (N-r+1 : ℕ)
      ≤ (r : ℝ) * (C - v 0) / (v 0 * (N-r+1 : ℕ)) := by
  have h := div_le_div_of_nonneg_right
    (retracing_failure_sum_le v hv hpos hbound hr)
    (show (0 : ℝ) ≤ (N-r+1 : ℕ) by positivity)
  simpa only [div_div] using h

/-- A path starting after clock L retains at least v L / C of its mass. -/
theorem tail_retracing_failure_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) {C : ℝ} {L k i : ℕ}
    (hLk : L ≤ k) (hbound : v i ≤ C) :
    1 - v k / v i ≤ 1 - v L / C := by
  have hvi : 0 < v i := lt_of_lt_of_le hpos (hv (Nat.zero_le i))
  have hC : 0 < C := lt_of_lt_of_le hvi hbound
  have hvL : 0 ≤ v L := (lt_of_lt_of_le hpos (hv (Nat.zero_le L))).le
  have hLk' : v L ≤ v k := hv hLk
  have hratio : v L / C ≤ v k / v i := by
    apply (div_le_div_iff₀ hC hvi).2
    calc
      v L * v i ≤ v L * C := mul_le_mul_of_nonneg_left hbound hvL
      _ ≤ v k * C := mul_le_mul_of_nonneg_right hLk' hC.le
  linarith

/-- Uniformly for roots N+j and a depth r with L+r ≤ N. -/
theorem linear_window_failure_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) {C : ℝ} (hbound : ∀ i, v i ≤ C)
    {L r N : ℕ} (hclock : L+r ≤ N) (j : ℕ) :
    1 - v (N+j-r) / v (N+j) ≤ 1 - v L / C := by
  apply tail_retracing_failure_le v hv hpos
  · omega
  · exact hbound _

/-- Averaged retracing over a shifted window, uniformly in the shift r. -/
theorem uniform_shift_failure_mean_le (v : ℕ → ℝ) (hv : Monotone v)
    (hpos : 0 < v 0) {C : ℝ} (hbound : ∀ i, v i ≤ C) (r M : ℕ) :
    (∑ j ∈ Finset.range (M+1), (1 - v j / v (r+j))) / (M+1 : ℕ)
      ≤ 1 - (∑ j ∈ Finset.range (M+1), v j) / ((M+1 : ℕ) * C) := by
  have hC : 0 < C := lt_of_lt_of_le hpos (hbound 0)
  have hn : (0 : ℝ) < (M+1 : ℕ) := by positivity
  have hsum : (∑ j ∈ Finset.range (M+1), (1 - v j / v (r+j)))
      ≤ ∑ j ∈ Finset.range (M+1), (1 - v j / C) := by
    apply Finset.sum_le_sum
    intro j _
    exact tail_retracing_failure_le v hv hpos (le_refl j) (hbound (r+j))
  calc
    _ ≤ (∑ j ∈ Finset.range (M+1), (1 - v j / C)) / (M+1 : ℕ) :=
      div_le_div_of_nonneg_right hsum hn.le
    _ = 1 - (∑ j ∈ Finset.range (M+1), v j) / ((M+1 : ℕ) * C) := by
      rw [Finset.sum_sub_distrib, ← Finset.sum_div]
      simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
      field_simp [ne_of_gt hC, ne_of_gt hn]

#print axioms sum_increments
#print axioms capacity_ratio_failure_le
#print axioms window_capacity_sum_le
#print axioms retracing_failure_sum_le
#print axioms retracing_failure_mean_le
#print axioms tail_retracing_failure_le
#print axioms linear_window_failure_le
#print axioms uniform_shift_failure_mean_le

end CollatzCanonicalRetracing
