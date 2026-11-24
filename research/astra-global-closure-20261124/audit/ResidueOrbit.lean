import Std

namespace Collatz.ShadowResidue

/-- With an odd denominator, multiplication by an eight-unit forces the
integer numerator of any successor to be a multiple of eight. Here k is
that numerator after clearing the source denominator. -/
theorem forbiddenFraction (d v c k : Int) (hd : d%2=1)
    (hv : v=0 ∨ v=1) (hc : c=5 ∨ c=7)
    (h : 8*k=9*(5*d+v*d+4)-d*c) : False := by
  rcases hv with rfl|rfl <;> rcases hc with rfl|rfl <;> omega

/-- If two L-source coordinates differ by one, their integer difference
after a common L input has no possible target carry. -/
theorem noUnitDifference (d c₁ c₂ : Int)
    (h₁ : c₁=5 ∨ c₁=7) (h₂ : c₂=5 ∨ c₂=7) (h : 8*d=9-c₁+c₂) :
    False := by
  rcases h₁ with rfl|rfl <;> rcases h₂ with rfl|rfl <;> omega

/-- A difference of two at P would produce the already impossible
difference of one at its successor. -/
theorem twoForcesOne (d c₁ c₂ : Int)
    (h₁ : 5≤c₁ ∧ c₁≤19) (h₂ : 5≤c₂ ∧ c₂≤19)
    (h : 32*d=18-c₁+c₂) : d=1 := by omega

/-- Before division by 256, reversing L and P changes the carry by F. -/
theorem translationNumerators (z f : Int) :
    9*(9*z+f) - (9*(9*z)+8*f) = f := by omega

theorem orderChecks : (53:Nat)^41%83=82 ∧ (53:Nat)^2%83=70 := by decide

#print axioms forbiddenFraction
#print axioms noUnitDifference
#print axioms twoForcesOne
#print axioms translationNumerators
#print axioms orderChecks
end Collatz.ShadowResidue
