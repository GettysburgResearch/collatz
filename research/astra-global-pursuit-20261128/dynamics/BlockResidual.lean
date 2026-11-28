import Std

/-! Integer identities for the common-prefix labels in GROWING_BLOCKS.md.
The real fractional-moment and external pair-absorption estimates are written. -/
namespace Collatz.BlockResidual

def bit (x : Int) : Int := x % 2

def slope (x : Int) : Int := if x % 2 = 0 then 1 else 3

def step (x : Int) : Int := if x % 2 = 0 then x / 2 else (3*x+1) / 2

def scaledResidual (scale multiplier r c : Int) : Int := scale*c - multiplier*r

theorem twiceStep (x : Int) : 2 * step x = slope x * x + bit x := by
  by_cases h : x % 2 = 0
  · simp [step, slope, bit, h]
    omega
  · simp [step, slope, bit, h]
    omega

theorem distinctDigitParities (a c : Int) (ha : a % 2 = 1) :
    bit c + bit (a+c) = 1 := by
  unfold bit
  omega

theorem residualTransport (scale a r c e : Int) :
    scaledResidual (2*scale) (slope (a*e+c) * a) (r+scale*e) (step (a*e+c))
      = slope (a*e+c) * scaledResidual scale a r c + scale * bit (a*e+c) := by
  have h := twiceStep (a*e+c)
  unfold scaledResidual
  grind

theorem sortedOffsetCancellation (scale a r c d k : Int) :
    scaledResidual scale (k*a) r d - k * scaledResidual scale a r c
      = scale*(d-k*c) := by
  unfold scaledResidual
  grind

theorem sameGradeSpacing (scale a r c d : Int) (hs : 0 ≤ scale) (hlt : c < d) :
    scaledResidual scale a r c + scale ≤ scaledResidual scale a r d := by
  unfold scaledResidual
  have h : 0 ≤ scale * (d-c-1) := Int.mul_nonneg hs (by omega)
  grind

#print axioms twiceStep
#print axioms distinctDigitParities
#print axioms residualTransport
#print axioms sortedOffsetCancellation
#print axioms sameGradeSpacing

end Collatz.BlockResidual
