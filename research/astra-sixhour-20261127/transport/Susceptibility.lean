import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-! Finite ordinary-source conservation kernels for the real-marked susceptibility.
The countable limiting canonical-fibre statements are proved in SUSCEPTIBILITY.md. -/

namespace Collatz.Susceptibility

set_option autoImplicit false

/-- Both terms of the canonical inverse first-real-moment recursion after
division by the square of the terminal. The hypothesis is the exact
one-odd-step affine equation, with branch multiplier b. -/
theorem momentCoefficients (x y b moment trace : ℚ) (hx : 0 < x)
    (hy : y ≠ 0) (hstep : 3*y = b*(3*x+1)) :
    (b^2*moment + b^2*trace/3)/y^2 =
      (3*x/(3*x+1))^2*(moment/x^2) + 3*trace/(3*x+1)^2 := by
  have hp : 3*x+1 ≠ 0 := by positivity
  have hb : b = 3*y/(3*x+1) := (eq_div_iff hp).2 hstep.symm
  rw [hb]
  field_simp

/-- The pathwise flux telescope, with arbitrary edge survival factors. -/
theorem onePath (w : ℕ → ℚ) (n : ℕ) :
    (∑ j ∈ Finset.range n, (∏ i ∈ Finset.range j, w i ^ 2)*(1-w j ^ 2))
      + (∏ i ∈ Finset.range n, w i ^ 2) = 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, Finset.prod_range_succ]
    linear_combination ih

/-- Sum of sources minus all losses accumulated so far equals the actual
surviving source mass. The factors can depend arbitrarily on the source. -/
theorem finiteGreenBalance {ι : Type*} (sources : Finset ι)
    (c : ι → ℚ) (w : ι → ℕ → ℚ) (n : ℕ) :
    (∑ x ∈ sources, c x) -
      (∑ x ∈ sources, c x *
        (∑ j ∈ Finset.range n, (∏ i ∈ Finset.range j, w x i ^ 2)*(1-w x j ^ 2))) =
      ∑ x ∈ sources, c x * (∏ i ∈ Finset.range n, w x i ^ 2) := by
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro x _
  linear_combination -(c x) * onePath (w x) n

#print axioms momentCoefficients
#print axioms onePath
#print axioms finiteGreenBalance

end Collatz.Susceptibility
