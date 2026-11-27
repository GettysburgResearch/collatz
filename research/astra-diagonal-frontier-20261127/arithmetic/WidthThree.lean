import Mathlib.Tactic

namespace Collatz.WidthThree

def stencil (a b c d e f g h i : ℤ) : ℤ :=
  a - 2*b + c + d - 2*e + f + g - 2*h + i

theorem polynomialIdentity (x : ℤ) :
    stencil 1 x (x^3) (x^5) (x^8) (x^11) (x^13) (x^15) (x^16) =
      (x-1)^2 * (x^2-1) * (x^3-1) * (x^4-1) * (x^5-1) := by
  unfold stencil
  ring

theorem stencilMass (a b c d e f g h i : ℤ)
    (ha : 1 ≤ a ∧ a ≤ 2) (hb : 1 ≤ b ∧ b ≤ 2)
    (hc : 1 ≤ c ∧ c ≤ 2) (hd : 1 ≤ d ∧ d ≤ 2)
    (he : 1 ≤ e ∧ e ≤ 2) (hf : 1 ≤ f ∧ f ≤ 2)
    (hg : 1 ≤ g ∧ g ≤ 2) (hh : 1 ≤ h ∧ h ≤ 2) (hi : 1 ≤ i ∧ i ≤ 2) :
    -6 ≤ stencil a b c d e f g h i ∧ stencil a b c d e f g h i ≤ 6 := by
  unfold stencil
  omega

theorem forcedDivisibility (a b c d e f g h i : ℤ) :
    (4 : ℤ) ∣ stencil (4*a+2) (4*b+2) (4*c+2) (4*d+2) (4*e+2)
      (4*f+2) (4*g+2) (4*h+2) (4*i+2) := by
  refine ⟨stencil a b c d e f g h i, ?_⟩
  unfold stencil
  ring

theorem noBirthAtOne {v d w : ℤ} (hv : v ≤ 0) (hd : d ≤ 6)
    (hw : 2*w = 3*v+d) (hm : 4 ∣ w) : w ≤ 0 := by
  obtain ⟨k,hk⟩ := hm
  omega

theorem birthAtTwo {v d w : ℤ} (hv : v ≤ 0) (hd : d ≤ 6)
    (hw : 4*w = 3*v+d) (hp : 0 < w) : v = 0 ∧ w = 1 := by
  omega

theorem firstTwoState {v d w : ℤ} (hv : 1 ≤ v ∧ v ≤ 3) (hd : d ≤ 6)
    (hw : 2*w = 3*v+d) (hm : 4 ∣ w) (hp : 0 < w) : w = 4 := by
  obtain ⟨k,hk⟩ := hm
  omega

theorem afterFirstTwo {w : ℤ} (hw : 4*w = 3*4) : w = 3 := by
  omega

theorem longReturn {d w : ℤ} (hd : d ≤ 6) (hw : 4*w = 9+d) (hp : 0 < w) :
    1 ≤ w ∧ w ≤ 3 := by
  omega

theorem forcedSecondTwoExcludes {v : ℤ} (hf : 4 ∣ v) :
    v ≠ 3 ∧ v ≠ -3 := by
  obtain ⟨k,hk⟩ := hf
  omega

#print axioms polynomialIdentity
#print axioms stencilMass
#print axioms forcedDivisibility
#print axioms noBirthAtOne
#print axioms birthAtTwo
#print axioms firstTwoState
#print axioms afterFirstTwo
#print axioms longReturn
#print axioms forcedSecondTwoExcludes

end Collatz.WidthThree
