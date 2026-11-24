import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Eval.Defs

/-!
# The positive real pole survives every chronological prefix

This file checks the finite, ordered-word part of RATIONAL_SELECTION.md.
The recursive polynomial retains every odd affine correction in its
chronological position. At the positive root of a repeated block's full
denominator, its numerator is positive, even after an arbitrary prefix.
Consequently no polynomial factor vanishing at that root cancels.

The binomial irreducibility, nonarchimedean Taylor-radius argument, and
the external arithmetic-germ rationality theorem are written mathematics,
not claims formalized in this file. No universal germ is constructed.
-/

namespace Collatz.ProfoundRoundSix.RationalSelection

set_option autoImplicit false

open Polynomial

noncomputable section

def ones : List Bool → ℕ
  | [] => 0
  | b :: w => (if b then 1 else 0) + ones w

/-- The first Boolean is the first shortcut step. -/
def carryPolynomial : List Bool → Polynomial ℝ
  | [] => 0
  | b :: w =>
      C (if b then (3 : ℝ) ^ ones w else 0) + X * carryPolynomial w

theorem ones_append (u w : List Bool) : ones (u ++ w) = ones u + ones w := by
  induction u with
  | nil => simp [ones]
  | cons b u ih => simp [ones, ih, Nat.add_assoc]

/-- Polynomial chronological concatenation, before any evaluation or reduction. -/
theorem carryPolynomial_append (u w : List Bool) :
    carryPolynomial (u ++ w) =
      C ((3 : ℝ) ^ ones w) * carryPolynomial u +
        X ^ u.length * carryPolynomial w := by
  induction u with
  | nil => simp [carryPolynomial]
  | cons b u ih =>
    cases b <;>
      simp [carryPolynomial, ones_append, ih, pow_add, pow_succ, C_mul] <;> ring

theorem carry_eval_nonneg (w : List Bool) {r : ℝ} (hr : 0 ≤ r) :
    0 ≤ (carryPolynomial w).eval r := by
  induction w with
  | nil => simp [carryPolynomial]
  | cons b w ih =>
    cases b
    · simpa [carryPolynomial] using mul_nonneg hr ih
    · simpa [carryPolynomial] using
        add_nonneg (le_of_lt (pow_pos (by norm_num : (0 : ℝ) < 3) (ones w)))
          (mul_nonneg hr ih)

theorem carry_eval_pos (w : List Bool) {r : ℝ} (hr : 0 < r)
    (hw : 0 < ones w) :
    0 < (carryPolynomial w).eval r := by
  induction w with
  | nil => simp [ones] at hw
  | cons b w ih =>
    cases b
    · have hw' : 0 < ones w := by simpa [ones] using hw
      simpa [carryPolynomial] using mul_pos hr (ih hw')
    · simpa [carryPolynomial] using
        add_pos_of_pos_of_nonneg (pow_pos (by norm_num : (0 : ℝ) < 3) (ones w))
          (mul_nonneg (le_of_lt hr) (carry_eval_nonneg w (le_of_lt hr)))

def blockDenominator (w : List Bool) : Polynomial ℝ :=
  C ((3 : ℝ) ^ ones w) - X ^ w.length

/-- Numerator of the actual prefix followed by the periodically repeated block.
The overall scalar factor 3^(-ones u) has no polynomial zeros. -/
def periodicNumerator (u w : List Bool) : Polynomial ℝ :=
  carryPolynomial u * blockDenominator w + X ^ u.length * carryPolynomial w

theorem periodic_numerator_eval (u w : List Bool) {r : ℝ}
    (hroot : r ^ w.length = (3 : ℝ) ^ ones w) :
    (periodicNumerator u w).eval r =
      r ^ u.length * (carryPolynomial w).eval r := by
  simp [periodicNumerator, blockDenominator, hroot]

theorem periodic_numerator_positive (u w : List Bool) {r : ℝ}
    (hr : 0 < r) (hw : 0 < ones w)
    (hroot : r ^ w.length = (3 : ℝ) ^ ones w) :
    0 < (periodicNumerator u w).eval r := by
  rw [periodic_numerator_eval u w hroot]
  exact mul_pos (pow_pos hr _) (carry_eval_pos w hr hw)

/-- This rules out cancellation of every denominator factor having the
positive real root, rather than testing a proper arithmetic denominator. -/
theorem no_cancellation_at_positive_root (u w : List Bool)
    (factor : Polynomial ℝ) {r : ℝ}
    (hr : 0 < r) (hw : 0 < ones w)
    (hroot : r ^ w.length = (3 : ℝ) ^ ones w)
    (hfactor : factor.eval r = 0) :
    ¬ factor ∣ periodicNumerator u w := by
  rintro ⟨q, hq⟩
  have hpos := periodic_numerator_positive u w hr hw hroot
  rw [hq, eval_mul, hfactor, zero_mul] at hpos
  exact lt_irrefl 0 hpos

end

end Collatz.ProfoundRoundSix.RationalSelection
