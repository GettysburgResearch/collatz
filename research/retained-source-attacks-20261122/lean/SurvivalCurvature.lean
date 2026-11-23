import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Order.BigOperators.Group.List
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite actual-path test for the analytic continuation attempt.

The polynomial is literally the product of the linearly deformed survival
factors. We check its first two formal derivatives and the strict negative
moment determinant for every nonempty list of positive ordinary states.
No infinite path, analytic continuation, or Collatz convergence is assumed.
-/

namespace CollatzRetained.SurvivalCurvature

noncomputable section

open Polynomial

def survival : List ℝ → Polynomial ℝ
  | [] => 1
  | w :: ws => (1 - C w * X) * survival ws

private theorem survival_zero (ws : List ℝ) : (survival ws).eval 0 = 1 := by
  induction ws with
  | nil => simp [survival]
  | cons w ws ih => simp [survival, ih]

private theorem survival_first (ws : List ℝ) :
    (derivative (survival ws)).eval 0 = -ws.sum := by
  induction ws with
  | nil => simp [survival]
  | cons w ws ih =>
    simp [survival, derivative_mul, derivative_sub, survival_zero, ih]
    ring

private theorem survival_second (ws : List ℝ) :
    (derivative (derivative (survival ws))).eval 0 =
      ws.sum ^ 2 - (ws.map (fun w => w ^ 2)).sum := by
  induction ws with
  | nil => simp [survival]
  | cons w ws ih =>
    simp [survival, derivative_mul, derivative_sub, derivative_add,
      survival_first, ih]
    ring

/-- The complete finite survival product fails the Laplace moment determinant
by exactly the sum of the squared original per-state weights. -/
theorem survival_moment_defect (ws : List ℝ) :
    (survival ws).eval 0 * (derivative (derivative (survival ws))).eval 0 -
      ((derivative (survival ws)).eval 0) ^ 2 =
      -(ws.map (fun w => w ^ 2)).sum := by
  rw [survival_zero, survival_first, survival_second]
  ring

def weight (n : Nat) : ℝ := 1 / (3 * (n : ℝ) + 1)

private theorem square_sum_nonneg (ws : List ℝ) :
    0 ≤ (ws.map (fun w => w ^ 2)).sum := by
  induction ws with
  | nil => simp
  | cons w ws ih =>
    simp only [List.map_cons, List.sum_cons]
    exact add_nonneg (sq_nonneg w) ih

/-- For every nonempty finite list of ordinary states, including every actual
retained path segment, the determinant is strictly negative. The statement is
about its literal polynomial; no positive-measure representation is assumed. -/
theorem ordinary_survival_strict_defect (n : Nat) (ns : List Nat) :
    let p := survival ((n :: ns).map weight)
    p.eval 0 * (derivative (derivative p)).eval 0 -
      ((derivative p).eval 0) ^ 2 < 0 := by
  dsimp only
  rw [survival_moment_defect]
  simp only [List.map_cons, List.sum_cons]
  have hn : 0 < weight n := by unfold weight; positivity
  have hs := square_sum_nonneg (ns.map weight)
  have hq : 0 < weight n ^ 2 := sq_pos_of_pos hn
  linarith

end

end CollatzRetained.SurvivalCurvature

#print axioms CollatzRetained.SurvivalCurvature.survival_moment_defect
#print axioms CollatzRetained.SurvivalCurvature.ordinary_survival_strict_defect
