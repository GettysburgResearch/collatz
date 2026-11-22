module

public import RetainedTransport
public import Mathlib.Analysis.SpecificLimits.Basic

@[expose] public section

/-!
# Scalar kernels for an actual asynchronous common tail

The ordinary-source decomposition and its infinite pair limit are written
in ASYNCHRONOUS_RESIDUE.md. This file checks the geometric coefficient
with independent clocks, the finite overlap window, and the entire
one-path geometric series bound. No global Collatz estimate is assumed
or asserted here.
-/

namespace CollatzShell.AsynchronousKernel

open Finset

theorem independent_clock_weight (r : ℝ) (p q j : ℕ) :
    r ^ (p + j) * r ^ (q + j) = r ^ (p + q) * (r ^ 2) ^ j := by
  rw [pow_add, pow_add, pow_add, ← pow_mul]
  ring_nf

theorem overlap_clock_iff (p q j J : ℕ) :
    p + j < J ∧ q + j < J ↔ j < J - max p q := by
  omega

theorem overlap_clock_finset (p q J : ℕ) :
    (range J).filter (fun j => p + j < J ∧ q + j < J) =
      range (J - max p q) := by
  ext j
  simp only [mem_filter, mem_range]
  rw [overlap_clock_iff]
  omega

theorem finite_common_tail_geometric (r : ℝ) (p q J : ℕ) :
    (1 - r ^ 2) *
        (∑ j ∈ range J, r ^ (p + j) * r ^ (q + j)) =
      r ^ (p + q) * (1 - (r ^ 2) ^ J) := by
  simp_rw [independent_clock_weight]
  rw [← mul_sum]
  have h := mul_geom_sum (r ^ 2) J
  calc
    (1 - r ^ 2) * (r ^ (p + q) * ∑ i ∈ range J, (r ^ 2) ^ i) =
        -(r ^ (p + q) * ((r ^ 2 - 1) * ∑ i ∈ range J, (r ^ 2) ^ i)) := by ring
    _ = r ^ (p + q) * (1 - (r ^ 2) ^ J) := by rw [h]; ring

theorem atom_series_summable {t v : ℝ} (ht0 : 0 ≤ t) (ht1 : t < 1)
    (hv : 0 < v) (w : ℕ → ℝ) (hw : ∀ j, v ≤ w j) :
    Summable (fun j : ℕ => t ^ j / w j) := by
  have hgeo : Summable (fun j : ℕ => t ^ j / v) :=
    (summable_geometric_of_lt_one ht0 ht1).div_const v
  apply Summable.of_nonneg_of_le
    (fun j => div_nonneg (pow_nonneg ht0 j) (hv.le.trans (hw j)))
    (fun j => div_le_div_of_nonneg_left (pow_nonneg ht0 j) hv (hw j)) hgeo

theorem normalized_atom_series_bound {t v : ℝ}
    (ht0 : 0 ≤ t) (ht1 : t < 1) (hv : 0 < v)
    (w : ℕ → ℝ) (hw : ∀ j, v ≤ w j) :
    (1 - t) * (∑' j : ℕ, t ^ j / w j) ≤ 1 / v := by
  have hseries := atom_series_summable ht0 ht1 hv w hw
  have hgeo : Summable (fun j : ℕ => t ^ j / v) :=
    (summable_geometric_of_lt_one ht0 ht1).div_const v
  have bound : (∑' j : ℕ, t ^ j / w j) ≤ ∑' j : ℕ, t ^ j / v :=
    Summable.tsum_le_tsum
      (fun j => div_le_div_of_nonneg_left (pow_nonneg ht0 j) hv (hw j))
      hseries hgeo
  have ht : 0 < 1 - t := by linarith
  calc
    (1 - t) * (∑' j : ℕ, t ^ j / w j)
        ≤ (1 - t) * (∑' j : ℕ, t ^ j / v) :=
      mul_le_mul_of_nonneg_left bound ht.le
    _ = 1 / v := by
      rw [tsum_div_const, tsum_geometric_of_lt_one ht0 ht1]
      field_simp

theorem normalized_resolvent_atom_bound {r v : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) (hv : 0 < v)
    (w : ℕ → ℝ) (hw : ∀ j, v ≤ w j) :
    (1 - r ^ 2) * (∑' j : ℕ, (r ^ 2) ^ j / w j) ≤ 1 / v := by
  apply normalized_atom_series_bound (sq_nonneg r) (by nlinarith) hv w hw

theorem finite_cesaro_atom_bound {v : ℝ} (hv : 0 < v)
    (w : ℕ → ℝ) (hw : ∀ j, v ≤ w j) (J : ℕ) :
    (∑ j ∈ range J, 1 / w j) ≤ (J : ℝ) / v := by
  calc
    (∑ j ∈ range J, 1 / w j) ≤ ∑ j ∈ range J, 1 / v := by
      apply sum_le_sum
      intro j hj
      exact one_div_le_one_div_of_le hv (hw j)
    _ = (J : ℝ) / v := by simp [div_eq_mul_inv]

end CollatzShell.AsynchronousKernel
