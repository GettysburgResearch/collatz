import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite arithmetic and signed-kernel interfaces for the all-parent Green spectrum. -/
set_option autoImplicit false
namespace Collatz.Global.GreenSpectralKernels

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- A common lower row of mass `a` contracts the finite zero-mass subspace. -/
theorem doeblin_signed_contraction {I : Type*} [Fintype I]
    (kernel : I → I → F) (common mass : I → F) (a : F)
    (hkernel : ∀ x, ∑ y, kernel x y = 1) (hcommon : ∑ y, common y = 1)
    (hlower : ∀ x y, a * common y ≤ kernel x y) (hmass : ∑ x, mass x = 0) :
    ∑ y, |∑ x, mass x * kernel x y| ≤ (1-a)* ∑ x, |mass x| := by
  classical
  have centered (y : I) : ∑ x, mass x * kernel x y =
      ∑ x, mass x * (kernel x y-a*common y) := by
    simp_rw [mul_sub]
    rw [Finset.sum_sub_distrib, ← Finset.sum_mul, hmass, zero_mul, sub_zero]
  have row (x : I) : ∑ y, (kernel x y-a*common y) = 1-a := by
    rw [Finset.sum_sub_distrib, ← Finset.mul_sum, hkernel, hcommon, mul_one]
  calc
    ∑ y, |∑ x, mass x * kernel x y| =
        ∑ y, |∑ x, mass x*(kernel x y-a*common y)| := by simp_rw [centered]
    _ ≤ ∑ y, ∑ x, |mass x*(kernel x y-a*common y)| :=
      Finset.sum_le_sum fun y _ => Finset.abs_sum_le_sum_abs _ _
    _ = ∑ x, ∑ y, |mass x| *(kernel x y-a*common y) := by
      rw [Finset.sum_comm]
      simp_rw [abs_mul, abs_of_nonneg (sub_nonneg.mpr (hlower _ _))]
    _ = (1-a)* ∑ x, |mass x| := by
      simp_rw [← Finset.mul_sum, row, ← Finset.sum_mul, mul_comm (1-a)]

/-- Splitting off the first physical edge forces a principal mode to be constant along it. -/
theorem green_principal_edge (u v survival loss : F) (hs : 0 < survival)
    (hpartition : loss+survival=1) (h : u=loss*u+survival*v) : u=v := by
  have heq : survival*(u-v) = 0 := by
    calc
      survival*(u-v) = (loss+survival)*u - (loss*u+survival*v) := by ring
      _ = 0 := by rw [hpartition, one_mul, ← h, sub_self]
  exact sub_eq_zero.mp ((mul_eq_zero.mp heq).resolve_left (ne_of_gt hs))

omit [LinearOrder F] [IsStrictOrderedRing F] in
/-- Clearing the positive fourth-power denominator of the damped complex derivative. -/
theorem resonant_imaginary_numerator (c d s t : F) (hcircle : c^2+d^2=1) :
    t*(2*c*(1-s*t*c)*(s*t*d)+d*((1-s*t*c)^2-(s*t*d)^2)) =
      t*(1-s^2*t^2)*d := by
  calc
    _ = t*(1-s^2*t^2*(c^2+d^2))*d := by ring
    _ = _ := by rw [hcircle, mul_one]

/-- The native stationary killing-site weight is reciprocal height on an odd cycle. -/
theorem physical_stationary_weight (x : F) (hx : 0 < x) :
    (1 / (3*x+1)) / (3*x / (3*x+1)) = 1/(3*x) := by
  have hx' : x ≠ 0 := ne_of_gt hx
  have hden : 3*x+1 ≠ 0 := by positivity
  field_simp

end Collatz.Global.GreenSpectralKernels

#print axioms Collatz.Global.GreenSpectralKernels.doeblin_signed_contraction
#print axioms Collatz.Global.GreenSpectralKernels.green_principal_edge
#print axioms Collatz.Global.GreenSpectralKernels.resonant_imaginary_numerator
#print axioms Collatz.Global.GreenSpectralKernels.physical_stationary_weight
