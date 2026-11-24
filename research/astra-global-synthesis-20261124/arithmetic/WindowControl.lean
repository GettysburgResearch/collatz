import Std

namespace Collatz.WindowControl

/-- Pulling a target difference divisible by three back one odd branch
loses one factor three and keeps the same complete clock. -/
theorem inverse_transfer (u y delta : Int) (e : Nat)
    (h : 3*u+1=(2:Int)^e*y) :
    3*(u+(2:Int)^e*delta)+1=(2:Int)^e*(y+3*delta) := by
  grind

/-- After the uniform carry bound, an extra binary factor forces a
strictly larger positive source, regardless of the larger word's length. -/
theorem larger_source (v x z u big carry extra y : Nat)
    (hx : v*x+carry=u*y) (hz : v*z+extra=big*y)
    (scale : 2*u ≤ big) (smallCarry : 2*extra<big*y) : x<z := by
  have hscale := Nat.mul_le_mul_right y scale
  rw [Nat.mul_assoc] at hscale
  have hp : v*x<v*z := by omega
  apply Classical.byContradiction
  intro bad
  have h := Nat.mul_le_mul_left v (by omega : z≤x)
  omega

#print axioms inverse_transfer
#print axioms larger_source
end Collatz.WindowControl
