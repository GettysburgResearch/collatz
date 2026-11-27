import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FullDenominatorPacking

/-- A common square-root residue on the entire squared denominator
clears both coordinates in the quotient of two Pell elements. -/
theorem taggedQuotient (D d R X Y V W : ℤ)
    (hx : d^2 ∣ X-R*V) (hy : d^2 ∣ Y-R*W) (hr : d^2 ∣ R^2-D) :
    d^2 ∣ X*Y-D*V*W ∧ d^2 ∣ X*W-Y*V := by
  obtain ⟨a, ha⟩ := hx
  obtain ⟨b, hb⟩ := hy
  obtain ⟨k, hk⟩ := hr
  have hX : X=R*V+d^2*a := by linarith only [ha]
  have hY : Y=R*W+d^2*b := by linarith only [hb]
  have hD : D=R^2-d^2*k := by linarith only [hk]
  subst X Y D
  constructor
  · exact ⟨k*V*W + R*(V*b+W*a) + d^2*a*b, by ring⟩
  · exact ⟨a*W-b*V, by ring⟩

/-- The cleared quotient is a norm-one unit in integer coordinates. -/
theorem quotientUnit (D d X Y V W u v : ℤ) (hd : d≠0)
    (hx : X^2-D*V^2=d^2) (hy : Y^2-D*W^2=d^2)
    (hu : X*Y-D*V*W=d^2*u) (hv : X*W-Y*V=d^2*v) :
    u^2-D*v^2=1 := by
  have id : (X*Y-D*V*W)^2-D*(X*W-Y*V)^2=(X^2-D*V^2)*(Y^2-D*W^2) := by ring
  rw [hu, hv, hx, hy] at id
  have hz : d^4*(u^2-D*v^2-1)=0 := by linear_combination id
  have h := (mul_eq_zero.mp hz).resolve_left (pow_ne_zero _ hd)
  linarith only [h]

/-- The normalized return norm retains the odd numerator at an equal
joint residue, including non-unit complete denominators. -/
theorem normalizedReturn (D d A B K X Y V W u : ℤ)
    (hx : X^2-D*V^2=d^2) (hy : Y^2-D*W^2=d^2)
    (hu : X*Y-D*V*W=d^2*u) (hK : B*Y-A*X=d*K) :
    (d*K)^2-D*(B*W-A*V)^2=d^2*(A^2+B^2-2*A*B*u) := by
  rw [← hK]
  linear_combination A^2*hx+B^2*hy-2*A*B*hu

theorem oddNormalizedNorm (a b u : ℤ) :
    Odd ((2*a+1)^2+(2*b)^2-2*(2*a+1)*(2*b)*u) := by
  exact ⟨2*a^2+2*a+2*b^2-2*(2*a+1)*b*u, by ring⟩

/-- Descent from an exact diagonal cubic to a homogeneous integral form
representing one after fixing the complete-denominator cube-root residue. -/
theorem cubicLift (A B d R U V Z k : ℤ) (hd : d≠0)
    (he : B*V^3-A*U^3=d) (hv : V=R*U+d*Z) (hk : B*R^3-A=d*k) :
    B*d^2*Z^3+3*B*R*d*Z^2*U+3*B*R^2*Z*U^2+k*U^3=1 := by
  rw [hv] at he
  have hz : d*(B*d^2*Z^3+3*B*R*d*Z^2*U+3*B*R^2*Z*U^2+k*U^3-1)=0 := by
    linear_combination he-U^3*hk
  have h := (mul_eq_zero.mp hz).resolve_left hd
  linarith only [h]

/-- The six possible units modulo nine have just the two indicated cube
values, so quotienting by signs removes the unknown cube factor. -/
theorem cubesModNine : ∀ u : Fin 9, u.val%3≠0 →
    u.val^3%9=1 ∨ u.val^3%9=8 := by decide +kernel

/-- Direct kernel checks of the unrestricted cubic-rank comparison. -/
theorem cubicRankFloor : 4*5^15 < (137500000000 : ℕ) := by decide +kernel

#print axioms taggedQuotient
#print axioms quotientUnit
#print axioms normalizedReturn
#print axioms oddNormalizedNorm
#print axioms cubicLift
#print axioms cubesModNine
#print axioms cubicRankFloor

end Collatz.FullDenominatorPacking
