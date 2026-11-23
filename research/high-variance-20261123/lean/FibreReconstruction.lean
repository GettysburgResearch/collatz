import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
The finite algebra behind the coherent actual-orbit chart and its size-biased
real fibre. No existence of an infinite orbit or canonical measure is assumed.
The infinite boundary, support dimension, and entropy applications remain
written mathematics in ANALYTIC_GLUING.md.
-/

namespace CollatzHighVariance.FibreReconstruction

open scoped BigOperators

/-- An actual edge and its homogeneous multiplier give the exact change in
the coherent real coordinate. The common scale can be any nonzero real;
for an odd Collatz edge it is the corresponding power of two. -/
theorem coherent_edge_increment
    (q q' a a' p : ℝ) (ha : a ≠ 0) (hp : p ≠ 0)
    (hq : p * q' = 3 * q + 1) (hc : p * a' = 3 * a) :
    q' / a' - q / a = 1 / (3 * a) := by
  have hratio : q' / a' = (3 * q + 1) / (3 * a) := by
    rw [← hq, ← hc]
    exact (mul_div_mul_left q' a' hp).symm
  rw [hratio]
  field_simp
  ring

private theorem weighted_variance
    {ι : Type*} (s : Finset ι) (w z : ι → ℝ) (m : ℝ)
    (hw : ∑ i ∈ s, w i = 1) (hm : ∑ i ∈ s, w i * z i = m) :
    (∑ i ∈ s, w i * (z i - m) ^ 2) =
      (∑ i ∈ s, w i * z i ^ 2) - m ^ 2 := by
  calc
    (∑ i ∈ s, w i * (z i - m) ^ 2) =
        ∑ i ∈ s, (w i * z i ^ 2 - 2 * m * (w i * z i) + m ^ 2 * w i) := by
      apply Finset.sum_congr rfl
      intro i hi
      ring
    _ = (∑ i ∈ s, w i * z i ^ 2) - m ^ 2 := by
      rw [Finset.sum_add_distrib, Finset.sum_sub_distrib,
        ← Finset.mul_sum, ← Finset.mul_sum, hm, hw]
      ring

/-- Exact finite algebraic reconstruction. The tilt w*z/m has total weight
one; its reciprocal fibre moment recovers b/m, and the charge-minus-first-moment
gap is exactly the centered second moment divided by b*m. All sums retain the
supplied weights. The probability interpretation additionally requires
nonnegative w and positive z,m; those assumptions are not needed for these
algebraic identities and are not asserted by this theorem.
-/
theorem finite_fibre_reconstruction
    {ι : Type*} (s : Finset ι) (w z : ι → ℝ) (m b : ℝ)
    (hw : ∑ i ∈ s, w i = 1) (hm : ∑ i ∈ s, w i * z i = m)
    (hm0 : m ≠ 0) (hb : b ≠ 0)
    (hz : ∀ i ∈ s, z i ≠ 0) :
    (∑ i ∈ s, w i * z i / m) = 1 ∧
    (∑ i ∈ s, (w i * z i / m) / (1 - (1 - z i / b))) = b / m ∧
    (1 - m / b) - (∑ i ∈ s, (w i * z i / m) * (1 - z i / b)) =
      (∑ i ∈ s, w i * (z i - m) ^ 2) / (b * m) := by
  have hn : (∑ i ∈ s, w i * z i / m) = 1 := by
    rw [← Finset.sum_div, hm, div_self hm0]
  refine ⟨hn, ?_, ?_⟩
  · calc
      (∑ i ∈ s, (w i * z i / m) / (1 - (1 - z i / b))) =
          ∑ i ∈ s, (b / m) * w i := by
        apply Finset.sum_congr rfl
        intro i hi
        have hzi := hz i hi
        have ht : 1 - (1 - z i / b) = z i / b := by ring
        rw [ht]
        field_simp
      _ = b / m := by rw [← Finset.mul_sum, hw, mul_one]
  · have ht : (∑ i ∈ s, (w i * z i / m) * (1 - z i / b)) =
        1 - (∑ i ∈ s, w i * z i ^ 2) / (b * m) := by
      calc
        (∑ i ∈ s, (w i * z i / m) * (1 - z i / b)) =
            ∑ i ∈ s, (w i * z i / m - w i * z i ^ 2 / (b * m)) := by
          apply Finset.sum_congr rfl
          intro i hi
          field_simp
        _ = 1 - (∑ i ∈ s, w i * z i ^ 2) / (b * m) := by
          rw [Finset.sum_sub_distrib, hn, ← Finset.sum_div]
    rw [ht, weighted_variance s w z m hw hm]
    field_simp
    ring

end CollatzHighVariance.FibreReconstruction
