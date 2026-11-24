import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# The canonical source seed and its complete Green potential

The analytic application uses `h_k = L^k h`, `d_k = L^k d`, and
`a_k = L^k a₀` at one fixed ordinary target. The actual operator,
harmonicization, and source-qualified analytic inputs are in the
companion note. These finite and series theorems install none of them
as axioms. Time zero is retained explicitly.
-/

namespace CollatzShell.HarmonicCapture

open Finset Filter
open scoped BigOperators Topology

/-- The canonical seed is exactly between three and four times the
immigration seed, with its ordinary source height retained. -/
theorem canonical_seed_identity {n h : ℝ} (hn : 1 ≤ n) :
    h / n = (3 + 1 / n) * (h / (3 * n + 1)) := by
  have hn0 : n ≠ 0 := ne_of_gt (by linarith : 0 < n)
  have hd0 : 3 * n + 1 ≠ 0 := ne_of_gt (by linarith : 0 < 3 * n + 1)
  field_simp

theorem canonical_seed_bounds {n h : ℝ} (hn : 1 ≤ n) (hh : 0 ≤ h) :
    3 * (h / (3 * n + 1)) ≤ h / n ∧
    h / n ≤ 4 * (h / (3 * n + 1)) := by
  have hn0 : 0 < n := by linarith
  have hd0 : 0 < 3 * n + 1 := by linarith
  have lower : (3 * h) / (3 * n + 1) ≤ h / n := by
    apply (div_le_div_iff₀ hd0 hn0).2
    nlinarith
  have upper : h / n ≤ (4 * h) / (3 * n + 1) := by
    apply (div_le_div_iff₀ hn0 hd0).2
    nlinarith [mul_nonneg hh (sub_nonneg.mpr hn)]
  constructor
  · convert lower using 1
    ring
  · convert upper using 1
    ring

/-- The time-one-and-later immigration sum telescopes exactly. -/
theorem green_telescope (h d : ℕ → ℝ)
    (step : ∀ k, h (k + 1) = h k + d (k + 1)) (N : ℕ) :
    (∑ k ∈ range N, d (k + 1)) = h N - h 0 := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [sum_range_succ, ih, step N]
      ring

/-- Keeping time zero gives the harmonic correction `d 0 + h N - h 0`. -/
theorem green_with_time_zero (h d : ℕ → ℝ)
    (step : ∀ k, h (k + 1) = h k + d (k + 1)) (N : ℕ) :
    (∑ k ∈ range (N + 1), d k) = d 0 + h N - h 0 := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [sum_range_succ, ih, step N]
      ring

/-- Positive transport preserves the seed comparison; this is the exact
finite targetwise Green bound after that pointwise comparison is supplied. -/
theorem finite_seed_green_bounds (h d a : ℕ → ℝ)
    (step : ∀ k, h (k + 1) = h k + d (k + 1))
    (lower : ∀ k, 3 * d k ≤ a k) (upper : ∀ k, a k ≤ 4 * d k)
    (N : ℕ) :
    3 * (d 0 + h N - h 0) ≤ ∑ k ∈ range (N + 1), a k ∧
    (∑ k ∈ range (N + 1), a k) ≤ 4 * (d 0 + h N - h 0) := by
  have lo := sum_le_sum (fun k (_ : k ∈ range (N + 1)) => lower k)
  have hi := sum_le_sum (fun k (_ : k ∈ range (N + 1)) => upper k)
  rw [← mul_sum, green_with_time_zero h d step N] at lo
  rw [← mul_sum, green_with_time_zero h d step N] at hi
  exact ⟨lo, hi⟩

/-- Monotone harmonicization supplies the complete immigration series;
convergence of `h` is an explicit input, not an imported Collatz axiom. -/
theorem immigration_hasSum (h d : ℕ → ℝ) (v : ℝ)
    (step : ∀ k, h (k + 1) = h k + d (k + 1))
    (hd : ∀ k, 0 ≤ d k) (hv : Tendsto h atTop (𝓝 v)) :
    HasSum d (d 0 + v - h 0) := by
  apply (hasSum_iff_tendsto_nat_of_nonneg hd _).2
  apply (tendsto_add_atTop_iff_nat 1).1
  have lim : Tendsto (fun N => d 0 + h N - h 0) atTop
      (𝓝 (d 0 + v - h 0)) :=
    (tendsto_const_nhds.add hv).sub tendsto_const_nhds
  convert lim using 1
  ext N
  exact green_with_time_zero h d step N

/-- The full canonical source series is summable, with both bounds. -/
theorem canonical_green_bounds (h d a : ℕ → ℝ) (v : ℝ)
    (step : ∀ k, h (k + 1) = h k + d (k + 1))
    (hd : ∀ k, 0 ≤ d k) (ha : ∀ k, 0 ≤ a k)
    (lower : ∀ k, 3 * d k ≤ a k) (upper : ∀ k, a k ≤ 4 * d k)
    (hv : Tendsto h atTop (𝓝 v)) :
    Summable a ∧
    3 * (d 0 + v - h 0) ≤ ∑' k, a k ∧
    (∑' k, a k) ≤ 4 * (d 0 + v - h 0) := by
  have ds := immigration_hasSum h d v step hd hv
  have as : Summable a :=
    Summable.of_nonneg_of_le ha upper (ds.summable.mul_left 4)
  exact ⟨as, hasSum_le lower (ds.mul_left 3) as.hasSum,
    hasSum_le upper as.hasSum (ds.mul_left 4)⟩

/-- The high-floor comparison gives a bound on normalized source occupation.
The floor must apply to the whole predecessor domain in the analytic use. -/
theorem normalized_green_bound {R v h l delta : ℝ}
    (hv : 0 < v) (hl : 0 ≤ l) (floor : delta * v ≤ h)
    (green : R ≤ 4 * (v - l * h)) :
    R / v ≤ 4 * (1 - l * delta) := by
  apply (div_le_iff₀ hv).2
  have scaled := mul_le_mul_of_nonneg_left floor hl
  nlinarith

/-- All collisions at a fixed target remain in the nonnegative time sums.
The complete square bounds the sum of the timewise collision energies. -/
theorem finite_collision_green_bound (a : ℕ → ℝ) (N : ℕ) {v W : ℝ}
    (ha : ∀ k, 0 ≤ a k) (hv : 0 < v) (hW : 0 ≤ W)
    (green : (∑ k ∈ range N, a k) ≤ 4 * W) :
    (∑ k ∈ range N, (a k)^2 / v) ≤ 16 * W^2 / v := by
  rw [← sum_div]
  apply div_le_div_of_nonneg_right _ (le_of_lt hv)
  have sq := sum_sq_le_sq_sum_of_nonneg (fun k (_ : k ∈ range N) => ha k)
  have positive : 0 ≤ ∑ k ∈ range N, a k := sum_nonneg (fun k _ => ha k)
  nlinarith

/-- A targetwise Green bound supplies summability of its entire collision
energy history, with no independence assumption on the colliding sources. -/
theorem collision_green_summable (a : ℕ → ℝ) {v W : ℝ}
    (ha : ∀ k, 0 ≤ a k) (hv : 0 < v) (hW : 0 ≤ W)
    (green : ∀ N, (∑ k ∈ range N, a k) ≤ 4 * W) :
    Summable (fun k => (a k)^2 / v) ∧
    (∑' k, (a k)^2 / v) ≤ 16 * W^2 / v := by
  have nonneg : ∀ k, 0 ≤ (a k)^2 / v := fun k =>
    div_nonneg (sq_nonneg _) (le_of_lt hv)
  have bound : ∀ N, (∑ k ∈ range N, (a k)^2 / v) ≤ 16 * W^2 / v :=
    fun N => finite_collision_green_bound a N ha hv hW (green N)
  exact ⟨summable_of_sum_range_le nonneg bound,
    Real.tsum_le_of_sum_range_le nonneg bound⟩

end CollatzShell.HarmonicCapture
