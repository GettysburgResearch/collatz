import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Real determinant projections for the unrestricted period-window estimate.
The scale and signs are retained, so the same bound applies after arbitrary
translations in either coordinate. -/
set_option autoImplicit false
namespace Collatz.Global.PeriodSpectrum

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- The primitive direction projects points on parallel affine lines to a
constant integer. The real identity separates horizontal and signed-error
spans for any slope. -/
theorem determinant_range (α q a n₁ n₂ u₁ u₂ N e : F)
    (hn : |n₁ - n₂| ≤ N) (he₁ : |u₁ - n₁ * α| ≤ e)
    (he₂ : |u₂ - n₂ * α| ≤ e) :
    |(q*u₁ - a*n₁) - (q*u₂ - a*n₂)| ≤
       |q| * (2*e) + N*|q*α-a| := by
  have herr : |(u₁ - n₁*α) - (u₂ - n₂*α)| ≤ 2*e := by
    calc
      _ ≤ |u₁ - n₁*α| + |u₂ - n₂*α| := by
        simpa only [sub_eq_add_neg, abs_neg] using
          (abs_add_le (u₁ - n₁*α) (-(u₂ - n₂*α)))
      _ ≤ 2*e := by linarith
  calc
    _ = |q*((u₁-n₁*α)-(u₂-n₂*α)) + (n₁-n₂)*(q*α-a)| := by
      congr 1
      ring
    _ ≤ |q*((u₁-n₁*α)-(u₂-n₂*α))| + |(n₁-n₂)*(q*α-a)| :=
      abs_add_le _ _
    _ ≤ _ := by
      simp only [abs_mul]
      gcongr

/-- The determinant-index span times the number of primitive steps on the
longest occupied line costs at most four times the area parameter. -/
theorem scaled_determinant_span (α q a N e j r : F)
    (hN : 0 ≤ N) (he : 0 ≤ e) (hj : 0 ≤ j)
    (hq : j * |q| ≤ N) (hδ : j * |q*α-a| ≤ 2*e)
    (hr : r ≤ |q| * (2*e)+N*|q*α-a|) :
    r*j ≤ 4*N*e := by
  have h₁ := mul_le_mul_of_nonneg_right hr hj
  have h₂ := mul_le_mul_of_nonneg_right hq (mul_nonneg (by norm_num : (0:F) ≤ 2) he)
  have h₃ := mul_le_mul_of_nonneg_left hδ hN
  calc
    _ ≤ (j*|q|)*(2*e) + N*(j*|q*α-a|) := by
      calc
        _ ≤ _ := h₁
        _ = _ := by ring
    _ ≤ 4*N*e := by nlinarith only [h₂,h₃]

/-- For at least two distinct determinant classes, their number times the
largest fiber size is controlled by the strip area. -/
theorem rank_two_count (R J area card : F)
    (hR : 2 ≤ R) (hJ : 2 ≤ J)
    (hspan : (R-1)*(J-1) ≤ 4*area) (hcard : card ≤ R*J) :
    card ≤ 1 + 12*area := by
  have h₁ := mul_nonneg (show 0 ≤ R-2 by linarith) (show 0 ≤ J-1 by linarith)
  have h₂ := mul_nonneg (show 0 ≤ R-1 by linarith) (show 0 ≤ J-2 by linarith)
  nlinarith only [h₁,h₂,hspan,hcard]

/-- On any affine integer-clock line the signed errors have exactly the
primitive spacing times the difference of their scalar coordinates. -/
theorem affine_error_spacing (α q a x y i j : F) :
    |((x+i*q)*α-(y+i*a))-((x+j*q)*α-(y+j*a))| =
      |i-j| * |q*α-a| := by
  rw [← abs_mul]
  congr 1
  ring

end Collatz.Global.PeriodSpectrum

#print axioms Collatz.Global.PeriodSpectrum.determinant_range
#print axioms Collatz.Global.PeriodSpectrum.scaled_determinant_span
#print axioms Collatz.Global.PeriodSpectrum.rank_two_count
#print axioms Collatz.Global.PeriodSpectrum.affine_error_spacing
