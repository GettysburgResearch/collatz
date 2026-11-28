import Mathlib.Data.Int.Interval
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact local kernels for transporting native extremal returns through
arbitrary mechanical clock surplus, with dyadic quantization. -/

namespace Collatz.AdaptiveEnvelope

/-- Quantizing the dyadic mantissas from below costs at most two on the
undivided register. The normalized source and low-bit remainder are retained explicitly. -/
theorem quantize_below {d d' x x' B source : ℤ} (hd : 0 < d) (hd' : 0 < d')
    (hB : 0 < B) (raw : B*x'*d = (3*x+source)*d')
    (carry : 3*(x % d) + source < 3*d) :
    B*(x'/d') ≤ 3*(x/d)+2 := by
  have h1 := Int.emod_add_mul_ediv x d
  have h2 := Int.emod_add_mul_ediv x' d'
  have hm2 := Int.emod_nonneg x' (by omega : d' ≠ 0)
  have hbil : B*(x'/d')*d*d' ≤ (3*(x/d)+2)*d*d' + (d-1)*d' := by
    calc
      B*(x'/d')*d*d' ≤ B*x'*d := by
        have hmain : (x'/d')*d' ≤ x' := by nlinarith only [h2, hm2]
        have := mul_le_mul_of_nonneg_left hmain (by positivity : 0 ≤ B*d)
        convert this using 1 <;> ring
      _ = (3*x+source)*d' := raw
      _ ≤ (3*(x/d)+2)*d*d' + (d-1)*d' := by
        have hmain : 3*x+source ≤ (3*(x/d)+2)*d+(d-1) := by nlinarith only [h1, carry]
        have := mul_le_mul_of_nonneg_right hmain (le_of_lt hd')
        convert this using 1; ring
  by_contra! bad
  have lower : 3*(x/d)+3 ≤ B*(x'/d') := by omega
  have := mul_le_mul_of_nonneg_right lower (show 0 ≤ d*d' by positivity)
  nlinarith only [this, hbil, hd']

/-- A native mantissa lifted by a positive integer factor gives a global
upper barrier at every allowed mechanical winding. -/
theorem lift_above {B z z' C : ℤ} (edge : B*z' = 3*z+C) (hC : 1 ≤ C) :
    B*(2*z'+1) - 3*(2*z+1) = B-1+2*(C-1) ∧
    B-1 ≤ B*(2*z'+1)-3*(2*z+1) := by
  constructor <;> nlinarith only [edge, hC]

/-- Entire integer native returns saturate every upper-ceiling digit,
independently of the orbit's archimedean width or exponent gcd. -/
theorem ordinary_saturates {B x y : ℤ} (edge : B*y = 3*x+1) :
    B*(2*y+1)-3*(2*x+1) = B-1 := by nlinarith only [edge]

end Collatz.AdaptiveEnvelope
