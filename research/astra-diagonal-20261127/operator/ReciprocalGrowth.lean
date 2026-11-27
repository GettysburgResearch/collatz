import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Exact finite Riccati comparison for a same-source side-mass proposal.
The quadratic lower gain and the uniform upper bound are hypotheses.
Neither is manufactured by replacing the original Collatz source law.
-/

namespace CollatzReciprocalGrowth

/-- A quadratic positive gain produces a fixed reciprocal decrease. -/
theorem reciprocal_decrease {q r δ M : ℝ}
    (hq : 0 < q) (hδ : 0 < δ) (hqM : q ≤ M)
    (hgain : q + δ * q ^ 2 ≤ r) :
    δ / (1 + δ * M) ≤ 1 / q - 1 / r := by
  have hqδ : 0 < q + δ * q ^ 2 := by positivity
  have hDq : 0 < 1 + δ * q := by positivity
  have hDM : 1 + δ * q ≤ 1 + δ * M := by nlinarith only [hδ, hqM]
  have hfrac := one_div_le_one_div_of_le hDq hDM
  have hlast := one_div_le_one_div_of_le hqδ hgain
  calc
    δ / (1 + δ * M) = δ * (1 / (1 + δ * M)) := by ring
    _ ≤ δ * (1 / (1 + δ * q)) := mul_le_mul_of_nonneg_left hfrac hδ.le
    _ = 1 / q - 1 / (q + δ * q ^ 2) := by
      field_simp [ne_of_gt hq, ne_of_gt hqδ, ne_of_gt hDq]
      ring
    _ ≤ 1 / q - 1 / r := sub_le_sub_left hlast _

/-- The reciprocal bound telescopes through an arbitrary finite horizon. -/
theorem reciprocal_horizon (q : ℕ → ℝ) (δ M : ℝ) (K : ℕ)
    (hδ : 0 < δ)
    (hpositive : ∀ j ≤ K, 0 < q j)
    (hbound : ∀ j ≤ K, q j ≤ M)
    (hgain : ∀ j < K, q j + δ * (q j) ^ 2 ≤ q (j + 1)) :
    (K : ℝ) * (δ / (1 + δ * M)) ≤ 1 / q 0 - 1 / q K := by
  have htel : ∀ n ≤ K,
      (n : ℝ) * (δ / (1 + δ * M)) ≤ 1 / q 0 - 1 / q n := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
      intro hn
      have hnK : n < K := Nat.lt_of_succ_le hn
      have hnle : n ≤ K := Nat.le_of_lt hnK
      have hb := ih hnle
      have hs := reciprocal_decrease (hpositive n hnle) hδ
        (hbound n hnle) (hgain n hnK)
      push_cast
      linarith only [hb, hs]
  exact htel K le_rfl

/-- In particular a bounded sequence with quadratic gain has a finite lifespan.
For `δ = c / a` and `M = C * a`, the bound is linear in `a`.
-/
theorem quadratic_gain_lifespan (q : ℕ → ℝ) (δ M : ℝ) (K : ℕ)
    (hδ : 0 < δ) (hstart : 1 ≤ q 0)
    (hpositive : ∀ j ≤ K, 0 < q j)
    (hbound : ∀ j ≤ K, q j ≤ M)
    (hgain : ∀ j < K, q j + δ * (q j) ^ 2 ≤ q (j + 1)) :
    (K : ℝ) < M + 1 / δ := by
  have hM : 0 < M := lt_of_lt_of_le (hpositive 0 (Nat.zero_le K))
    (hbound 0 (Nat.zero_le K))
  have hD : 0 < 1 + δ * M := by positivity
  have htel := reciprocal_horizon q δ M K hδ hpositive hbound hgain
  have hq0 : 1 / q 0 ≤ 1 := by
    simpa only [one_div_one] using one_div_le_one_div_of_le (by norm_num : (0:ℝ) < 1) hstart
  have hqK : 0 < 1 / q K := one_div_pos.mpr (hpositive K le_rfl)
  have hlt : (K : ℝ) * (δ / (1 + δ * M)) < 1 := by linarith only [htel, hq0, hqK]
  have hmul : (K : ℝ) * δ < 1 + δ * M := by
    have hdiv : (K : ℝ) * δ / (1 + δ * M) < 1 := by
      simpa only [mul_div_assoc] using hlt
    simpa only [one_mul] using (div_lt_iff₀ hD).mp hdiv
  have heq : M + 1 / δ = (1 + δ * M) / δ := by
    field_simp
    ring
  rw [heq]
  exact (lt_div_iff₀ hδ).2 hmul

end CollatzReciprocalGrowth
