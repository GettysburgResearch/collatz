import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite comparison for the summable-loss radial iteration on geometric scales. -/

namespace Collatz.ReciprocalRigidity.GeometricScales

def accumulated (e : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => accumulated e n + e n

def compounded (f : ℕ → ℝ) : ℕ → ℝ
  | 0 => 1
  | n+1 => compounded f n * f n

theorem compounded_ge_one (f : ℕ → ℝ) (h : ∀ n, 1 ≤ f n)
    (n : ℕ) : 1 ≤ compounded f n := by
  induction n with
  | zero => exact le_rfl
  | succ n ih =>
    change 1 ≤ compounded f n * f n
    exact one_le_mul_of_one_le_of_one_le ih (h n)

theorem accumulated_nonneg (e : ℕ → ℝ) (h : ∀ n, 0 ≤ e n)
    (n : ℕ) : 0 ≤ accumulated e n := by
  induction n with
  | zero => exact le_rfl
  | succ n ih => exact add_nonneg ih (h n)

theorem radial_iteration (u f e : ℕ → ℝ) (hf : ∀ n, 1 ≤ f n)
    (he : ∀ n, 0 ≤ e n) (step : ∀ n, u (n+1) ≤ f n * (u n + e n))
    (n : ℕ) : u n ≤ (u 0 + accumulated e n) * compounded f n := by
  induction n with
  | zero => simp [accumulated, compounded]
  | succ n ih =>
    have hp := compounded_ge_one f hf n
    have hx : e n ≤ e n * compounded f n := by
      simpa using mul_le_mul_of_nonneg_left hp (he n)
    calc
      u (n+1) ≤ f n * (u n + e n) := step n
      _ ≤ f n * ((u 0 + accumulated e n) * compounded f n + e n * compounded f n) :=
        mul_le_mul_of_nonneg_left (add_le_add ih hx) (by linarith [hf n])
      _ = _ := by simp only [accumulated, compounded]; ring

theorem bounded_radial_iteration (u f e : ℕ → ℝ) (hf : ∀ n, 1 ≤ f n)
    (he : ∀ n, 0 ≤ e n) (h0 : 0 ≤ u 0)
    (step : ∀ n, u (n+1) ≤ f n * (u n + e n))
    (a b : ℝ) (ha : ∀ n, accumulated e n ≤ a) (hb : ∀ n, compounded f n ≤ b)
    (n : ℕ) : u n ≤ (u 0 + a)*b := by
  apply (radial_iteration u f e hf he step n).trans
  exact mul_le_mul (add_le_add (le_refl _) (ha n)) (hb n)
    (le_trans zero_le_one (compounded_ge_one f hf n))
    (add_nonneg h0 ((accumulated_nonneg e he n).trans (ha n)))

#print axioms radial_iteration
#print axioms bounded_radial_iteration

end Collatz.ReciprocalRigidity.GeometricScales
