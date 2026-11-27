import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! The normalized two-source affine recurrence, finite center identity,
and good-offset localization estimate for geometric posterior shells.
The exact-cylinder count and infinite sum are written arguments. -/
namespace EscapeGeodesicPosterior

theorem normalized_edge
    (x y b c ref alt rel nextRel theta nextTheta : ℚ)
    (hx : ref * y = 3 * x + 1) (hb : alt * c = 3 * b + 1)
    (hxrel : b = rel * (x + theta)) (hyrel : c = nextRel * (y + nextTheta))
    (hclock : alt * nextRel = rel * ref) :
    rel * (ref * nextTheta - 3 * theta + 1) = 1 := by
  calc
    rel * (ref * nextTheta - 3 * theta + 1) =
        (rel * ref) * (y + nextTheta) - rel * (ref * y) - 3 * rel * theta + rel := by ring
    _ = alt * (nextRel * (y + nextTheta)) - rel * (3 * x + 1) -
        3 * rel * theta + rel := by rw [← hclock, mul_assoc, hx]
    _ = 1 := by rw [← hyrel, hb, hxrel]; ring

theorem center_telescope
    (theta weight ratio inverseRel : ℕ → ℚ)
    (hstart : weight 0 = 1)
    (hweight : ∀ i, 3 * weight (i + 1) = weight i * ratio i)
    (hedge : ∀ i, ratio i * theta (i + 1) = 3 * theta i + inverseRel i - 1)
    (n : ℕ) :
    theta 0 = weight n * theta n +
      ∑ i ∈ Finset.range n, weight i / 3 * (1 - inverseRel i) := by
  induction n with
  | zero => simp [hstart]
  | succ n ih =>
    rw [Finset.sum_range_succ]
    have hstep : weight (n+1) * theta (n+1) =
        weight n * theta n - weight n / 3 * (1 - inverseRel n) := by
      calc
        weight (n+1) * theta (n+1) =
            (3 * weight (n+1)) * theta (n+1) / 3 := by ring
        _ = weight n * (ratio n * theta (n+1)) / 3 := by rw [hweight n]; ring
        _ = _ := by rw [hedge n]; ring
    rw [hstep]
    linarith

theorem exact_center_error
    (theta weight ratio inverseRel : ℕ → ℚ)
    (hstart : weight 0 = 1)
    (hweight : ∀ i, 3 * weight (i + 1) = weight i * ratio i)
    (hedge : ∀ i, ratio i * theta (i + 1) = 3 * theta i + inverseRel i - 1)
    (n : ℕ) (hjoin : theta n = 0) (tail : ℚ) :
    (∑ i ∈ Finset.range n, weight i / 3) + tail - theta 0 =
      (∑ i ∈ Finset.range n, weight i / 3 * inverseRel i) + tail := by
  have ht := center_telescope theta weight ratio inverseRel hstart hweight hedge n
  simp only [hjoin, mul_zero, zero_add, mul_sub, mul_one, Finset.sum_sub_distrib] at ht
  linarith

theorem split_center_error (p q : ℕ → ℚ) (t s : ℕ) (small large : ℚ)
    (hp : ∀ i, 0 ≤ p i)
    (hearly : ∀ i < t, q i ≤ small) (hlate : ∀ i < s, q (t+i) ≤ large) :
    (∑ i ∈ Finset.range (t+s), p i * q i) ≤
      (∑ i ∈ Finset.range t, p i) * small +
      (∑ i ∈ Finset.range s, p (t+i)) * large := by
  rw [Finset.sum_range_add, Finset.sum_mul, Finset.sum_mul]
  apply add_le_add
  · apply Finset.sum_le_sum
    intro i hi
    exact mul_le_mul_of_nonneg_left (hearly i (Finset.mem_range.mp hi)) (hp i)
  · apply Finset.sum_le_sum
    intro i hi
    exact mul_le_mul_of_nonneg_left (hlate i (Finset.mem_range.mp hi)) (hp (t+i))

#print axioms normalized_edge
#print axioms center_telescope
#print axioms exact_center_error
#print axioms split_center_error
end EscapeGeodesicPosterior
