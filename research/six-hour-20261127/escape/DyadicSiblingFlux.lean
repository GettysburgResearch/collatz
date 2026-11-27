import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

/-! Algebra of a binary label at a dyadic parent and its two children.
The left child retains the parent label. No analytic input is assumed. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeDyadicSiblingFlux

/-- On a parent with differently labeled children, the sign of its
predictable change is the sign belonging to the current binary label. -/
theorem opportunity_sign (b c : ℤ) (hb : b=0 ∨ b=1)
    (hc : c=0 ∨ c=1) (different : c≠b) : c-b=1-2*b := by
  rcases hb with rfl | rfl <;> rcases hc with rfl | rfl <;> omega

/-- On the next opportunity, an odd choice reverses the sign while an
even choice keeps it. Between opportunities the label is unchanged. -/
theorem next_opportunity_sign (b j : ℤ) :
    1-2*(b+j*(1-2*b))=(1-2*b)*(1-2*j) := by ring

/-- Twice the actual label change is its predictable sign plus a
mean-zero fair-bit increment. -/
theorem split_change (j e : ℤ) : 2*(j*e)=e+(2*j-1)*e := by ring

/-- The centered increment has zero mean on the two equal children. -/
theorem fair_children_mean (e : ℤ) : (-e)+e=0 := by ring

/-- The centered increment contributes e squared to the average conditional
second moment. The integer expression is doubled to remove fractions. -/
theorem fair_children_square (m e : ℤ) :
    (m-e)^2+(m+e)^2=2*m^2+2*e^2 := by ring

/-- A binary label's signed change has square equal to its absolute change. -/
theorem binary_change_square (b c : ℤ) (hb : b=0 ∨ b=1)
    (hc : c=0 ∨ c=1) :
    (c-b)^2=if c=b then 0 else 1 := by
  rcases hb with rfl | rfl <;> rcases hc with rfl | rfl <;> decide

#print axioms opportunity_sign
#print axioms next_opportunity_sign
#print axioms split_change
#print axioms fair_children_mean
#print axioms fair_children_square
#print axioms binary_change_square

end EscapeDyadicSiblingFlux
