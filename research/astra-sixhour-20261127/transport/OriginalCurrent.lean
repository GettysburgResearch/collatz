import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Finite kernels for signed charges of actual shortcut-invariant labels.
The large-cycle rank count and infinite flux limits are written arguments. -/
namespace Collatz.OriginalCurrent
set_option autoImplicit false

variable (f : ℕ → ℚ)
variable (halve : ∀ t, f (2*t) = f t)
variable (oddStep : ∀ t, f (2*t+1) = f (3*t+2))

include halve oddStep

/-- One shortcut and one halving collapse a lifted source. -/
theorem fourPlusOne (t : ℕ) : f (4*t+1) = f (3*t+1) := by
  calc
    f (4*t+1) = f (2*(2*t)+1) := by congr 1; omega
    _ = f (3*(2*t)+2) := oddStep (2*t)
    _ = f (2*(3*t+1)) := by congr 1; omega
    _ = f (3*t+1) := halve (3*t+1)

/-- The lift has the identical label as the original when the latter is odd. -/
theorem oddLift (t : ℕ) : f (4*(2*t+1)+1) = f (2*t+1) := by
  calc
    _ = f (3*(2*t+1)+1) := fourPlusOne f halve oddStep (2*t+1)
    _ = f (2*(3*t+2)) := by congr 1; omega
    _ = f (3*t+2) := halve (3*t+2)
    _ = _ := (oddStep t).symm

/-- The odd-sign arm at a source 1 modulo 8 belongs to its physical component. -/
theorem goodArm (t : ℕ) : f (3*(8*t+1)+2) = f (8*t+1) := by
  calc
    _ = f (4*(6*t+1)+1) := by congr 1; omega
    _ = f (3*(6*t+1)+1) := fourPlusOne f halve oddStep (6*t+1)
    _ = f (2*(9*t+2)) := by congr 1; omega
    _ = f (9*t+2) := halve (9*t+2)
    _ = f (3*(3*t)+2) := by congr 1; omega
    _ = f (2*(3*t)+1) := (oddStep (3*t)).symm
    _ = f (3*(2*t)+1) := by congr 1; omega
    _ = f (4*(2*t)+1) := (fourPlusOne f halve oddStep (2*t)).symm
    _ = _ := by congr 1; omega

omit halve oddStep

/-- Current at the odd input 2j+1. -/
def currentAt (j : ℕ) : ℚ := f (2*j+1) - (2/3)*f (6*j+5) - (1/3)*f (6*j+1)

include oddStep

/-- The earliest nonzero charge when the absolute bad floor is s=6j+1. -/
theorem earliestLoss (j : ℕ) (large : 2 ≤ j)
    (floor : ∀ n < 6*j+1, f n = 0) (atFloor : f (6*j+1) = 1) :
    currentAt f j = -(1/3) ∧ ∀ i < j, currentAt f i = 0 := by
  have hgood : f (6*j+5) = 0 := by
    calc
      f (6*j+5) = f (3*(2*j+1)+2) := by congr 1; omega
      _ = f (2*(2*j+1)+1) := (oddStep (2*j+1)).symm
      _ = 0 := floor _ (by omega)
  constructor
  · unfold currentAt
    rw [atFloor, hgood, floor _ (by omega)]
    norm_num
  · intro i hi
    unfold currentAt
    rw [floor _ (by omega), floor _ (by omega), floor _ (by omega)]
    ring

include halve

/-- The exact charge at the lifted bad source, conditional on its true odd edge. -/
theorem raisedCurrent (k l : ℕ) (edge : 3*(2*k+1)+1=4*(2*l+1)) :
    currentAt f (4*k+2) =
    ((f (2*k+1)-f (3*(2*k+1))) +
      2*(f (2*l+1)-f (3*(2*l+1))))/3 := by
  have lower : f (6*(4*k+2)+1) = f (3*(2*k+1)) := by
    calc
      _ = f (4*(2*(3*k+1)+1)+1) := by congr 1; omega
      _ = f (2*(3*k+1)+1) := oddLift f halve oddStep (3*k+1)
      _ = _ := by congr 1; omega
  have upper : f (6*(4*k+2)+5) = f (3*(2*l+1)) := by
    calc
      _ = f (4*(4*(2*l+1))+1) := by congr 1; omega
      _ = f (3*(4*(2*l+1))+1) := fourPlusOne f halve oddStep (4*(2*l+1))
      _ = f (4*(2*(3*l+1)+1)+1) := by congr 1; omega
      _ = f (2*(3*l+1)+1) := oddLift f halve oddStep (3*l+1)
      _ = _ := by congr 1; omega
  have center : f (2*(4*k+2)+1) = f (2*k+1) := by
    calc
      _ = f (4*(2*k+1)+1) := by congr 1; omega
      _ = _ := oddLift f halve oddStep k
  have sameEdge : f (2*k+1) = f (2*l+1) := by
    calc
      _ = f (3*k+2) := oddStep k
      _ = f (2*(2*l+1)) := by congr 1; omega
      _ = _ := halve (2*l+1)
  unfold currentAt
  rw [center, lower, upper]
  linarith

omit halve oddStep

/-- The summable interior coefficient of the critical reciprocal flux. -/
theorem reciprocalDefect (b p a : ℚ) (hp : p ≠ 0) (hpa : p+a ≠ 0) :
    b/(p+a)-b/p = -b*a/(p*(p+a)) := by
  field_simp
  ring

#print axioms fourPlusOne
#print axioms oddLift
#print axioms goodArm
#print axioms earliestLoss
#print axioms raisedCurrent
#print axioms reciprocalDefect
end Collatz.OriginalCurrent
