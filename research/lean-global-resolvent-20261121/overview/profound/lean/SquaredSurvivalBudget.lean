import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
The reciprocal killing budget for the actual Collatz survival factor.

For positive integer odd states q_n, use their real coercions below and
f_(n+1) = f_n * (3 q_n)/(3 q_n + 1). The finite and series bounds do not
assume convergence, absence of cycles, or a rate of growth for q_n.
The all-centres inverse-word correspondence remains written mathematics.
-/

namespace CollatzSquaredSurvival

theorem hazard_identity (x : ℝ) (hx : 0 < x) :
    1 - (3 * x / (3 * x + 1)) ^ 2 - 7 / (16 * x) =
      (x - 1) * (33 * x + 7) / (16 * x * (3 * x + 1) ^ 2) := by
  have hd : 3 * x + 1 ≠ 0 := ne_of_gt (by linarith)
  field_simp [ne_of_gt hx, hd]
  ring

theorem hazard_lower (x : ℝ) (hx : 1 ≤ x) :
    7 / (16 * x) ≤ 1 - (3 * x / (3 * x + 1)) ^ 2 := by
  have hp : 0 < x := by linarith
  have hm : 0 ≤ x - 1 := sub_nonneg.mpr hx
  have hn : 0 ≤ (x - 1) * (33 * x + 7) /
      (16 * x * (3 * x + 1) ^ 2) := by positivity
  linarith [hazard_identity x hp]

theorem squared_step (x u : ℝ) (hx : 1 ≤ x) :
    (7 / 16 : ℝ) * (u ^ 2 / x) ≤
      u ^ 2 - (u * (3 * x / (3 * x + 1))) ^ 2 := by
  calc
    (7 / 16 : ℝ) * (u ^ 2 / x) = u ^ 2 * (7 / (16 * x)) := by ring
    _ ≤ u ^ 2 * (1 - (3 * x / (3 * x + 1)) ^ 2) :=
      mul_le_mul_of_nonneg_left (hazard_lower x hx) (sq_nonneg u)
    _ = u ^ 2 - (u * (3 * x / (3 * x + 1))) ^ 2 := by ring

theorem finite_budget_with_remainder
    (q f : ℕ → ℝ) (hq : ∀ n, 1 ≤ q n)
    (hrec : ∀ n, f (n + 1) = f n * (3 * q n / (3 * q n + 1)))
    (N : ℕ) :
    (7 / 16 : ℝ) * (∑ n ∈ Finset.range N, f n ^ 2 / q n) + f N ^ 2
      ≤ f 0 ^ 2 := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Finset.sum_range_succ, mul_add]
    have hs := squared_step (q N) (f N) (hq N)
    rw [← hrec N] at hs
    linarith

theorem finite_budget
    (q f : ℕ → ℝ) (hq : ∀ n, 1 ≤ q n)
    (hrec : ∀ n, f (n + 1) = f n * (3 * q n / (3 * q n + 1)))
    (N : ℕ) :
    (∑ n ∈ Finset.range N, f n ^ 2 / q n) ≤ (16 / 7 : ℝ) * f 0 ^ 2 := by
  have hb := finite_budget_with_remainder q f hq hrec N
  nlinarith [sq_nonneg (f N)]

theorem reciprocal_cost_summable
    (q f : ℕ → ℝ) (hq : ∀ n, 1 ≤ q n)
    (hrec : ∀ n, f (n + 1) = f n * (3 * q n / (3 * q n + 1))) :
    Summable (fun n => f n ^ 2 / q n) := by
  apply summable_of_sum_range_le (c := (16 / 7 : ℝ) * f 0 ^ 2)
  · intro n
    exact div_nonneg (sq_nonneg _) (by linarith [hq n])
  · intro N
    exact finite_budget q f hq hrec N

theorem complete_budget
    (q f : ℕ → ℝ) (hq : ∀ n, 1 ≤ q n)
    (hrec : ∀ n, f (n + 1) = f n * (3 * q n / (3 * q n + 1))) :
    (∑' n, f n ^ 2 / q n) ≤ (16 / 7 : ℝ) * f 0 ^ 2 := by
  exact (reciprocal_cost_summable q f hq hrec).tsum_le_of_sum_range_le
    (finite_budget q f hq hrec)

theorem unit_initial_budget
    (q f : ℕ → ℝ) (hq : ∀ n, 1 ≤ q n)
    (hrec : ∀ n, f (n + 1) = f n * (3 * q n / (3 * q n + 1)))
    (hzero : f 0 = 1) :
    (∑' n, f n ^ 2 / q n) ≤ (16 / 7 : ℝ) := by
  simpa [hzero] using complete_budget q f hq hrec

end CollatzSquaredSurvival
