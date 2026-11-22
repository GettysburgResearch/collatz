import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebra for the canonical first-contact expansion.  The density and
contact-probability estimates are explicit hypotheses.  No Collatz upper
bound or ordinary mixing assertion is assumed as an axiom.
-/

namespace CollatzContactCapture

open scoped BigOperators

noncomputable def frontWeight (L : ℕ) : ℝ :=
  ∑ j ∈ Finset.range L, (4 * (j : ℝ) + 2) * (3 / 2 : ℝ) ^ j

theorem frontWeight_exact (L : ℕ) :
    frontWeight L = 20 + (8 * (L : ℝ) - 20) * (3 / 2 : ℝ) ^ L := by
  induction L with
  | zero => norm_num [frontWeight]
  | succ L ih =>
    simp only [frontWeight, Finset.sum_range_succ] at ih ⊢
    rw [ih, pow_succ]
    push_cast
    ring

theorem frontWeight_le (L : ℕ) :
    frontWeight L ≤ 8 * (L : ℝ) * (3 / 2 : ℝ) ^ L := by
  have hp : (1 : ℝ) ≤ (3 / 2 : ℝ) ^ L := one_le_pow₀ (by norm_num)
  rw [frontWeight_exact]
  nlinarith

theorem finite_front_le {F : ℕ → ℝ} {b : ℝ} (hb : 0 ≤ b) (L : ℕ)
    (bound : ∀ j < L, F j ≤ b * (4 * (j : ℝ) + 2) * (3 / 2 : ℝ) ^ j) :
    (∑ j ∈ Finset.range L, F j) ≤
      8 * b * (L : ℝ) * (3 / 2 : ℝ) ^ L := by
  have first : (∑ j ∈ Finset.range L, F j) ≤ b * frontWeight L := by
    rw [frontWeight, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro j hj
    have h := bound j (Finset.mem_range.mp hj)
    simpa only [mul_assoc] using h
  have second := mul_le_mul_of_nonneg_left (frontWeight_le L) hb
  nlinarith

/-- The density front and a weak stopped-chain capture probability suffice.
Here R is the height scale, usually log(q+2), and C is a fixed front constant. -/
theorem capture_ratio_bound {v p f q R c C : ℝ}
    (hv : 0 ≤ v) (hq : 0 < q) (hR : 0 < R) (hc : 0 < c)
    (capture : v * p ≤ f) (front : R ^ 2 * f ≤ C * q)
    (probability : c ≤ R * p) : v / q ≤ C / (c * R) := by
  have first := mul_le_mul_of_nonneg_right probability (mul_nonneg hR.le hv)
  have second := mul_le_mul_of_nonneg_left capture (sq_nonneg R)
  have product : (c * R) * v ≤ C * q := by nlinarith
  apply (div_le_div_iff₀ hq (mul_pos hc hR)).mpr
  nlinarith

/-- This is a quantified marked-height implication.  The only global input
not supplied by finite algebra is the stated actual contact-probability lower
bound together with the front estimate. -/
theorem marked_sublinear_of_capture
    {Mark : ℕ → Prop} {V prob front R : ℕ → ℝ} {c C : ℝ}
    (hc : 0 < c)
    (positive : ∀ q, 0 < q → Mark q → 0 < R q)
    (nonnegative : ∀ q, 0 < q → Mark q → 0 ≤ V q)
    (captured : ∀ q, 0 < q → Mark q → V q * prob q ≤ front q)
    (front_bound : ∀ q, 0 < q → Mark q → (R q)^2 * front q ≤ C * (q : ℝ))
    (capture_lower : ∀ q, 0 < q → Mark q → c ≤ R q * prob q)
    (scale_diverges : ∀ B : ℝ, ∃ N : ℕ, ∀ q, N ≤ q → 0 < q → Mark q → B < R q) :
    ∀ δ : ℝ, 0 < δ → ∃ N : ℕ, ∀ q, N ≤ q → 0 < q → Mark q →
      V q / (q : ℝ) < δ := by
  intro δ hδ
  obtain ⟨N, hN⟩ := scale_diverges (C / (c * δ))
  refine ⟨N, ?_⟩
  intro q hqN hq mark
  have hR := positive q hq mark
  have bound := capture_ratio_bound (nonnegative q hq mark)
    (by exact_mod_cast hq : (0 : ℝ) < q) hR hc
    (captured q hq mark) (front_bound q hq mark) (capture_lower q hq mark)
  have growth : C < R q * (c * δ) := (div_lt_iff₀ (mul_pos hc hδ)).mp (hN q hqN hq mark)
  have small : C / (c * R q) < δ := by
    apply (div_lt_iff₀ (mul_pos hc hR)).mpr
    nlinarith
  exact bound.trans_lt small

end CollatzContactCapture

#print axioms CollatzContactCapture.frontWeight_exact
#print axioms CollatzContactCapture.frontWeight_le
#print axioms CollatzContactCapture.finite_front_le
#print axioms CollatzContactCapture.capture_ratio_bound
#print axioms CollatzContactCapture.marked_sublinear_of_capture
