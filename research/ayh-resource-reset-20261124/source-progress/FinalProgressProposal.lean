import SourceProgressCases
import MersenneProgressCases

/-! The final proposed residual obligation after the proved cases in this
packet. ResidualExclusion is OPEN. No theorem below establishes it. -/
namespace FinalProgressProposal
open CollatzReverseBasin CollatzTwoOdd FinalProofProposal SourceProgressCases

def SixteenthCase (z : Nat) : Prop :=
  ∃ t : Nat, 81*z+527=512*2^(98+162*(3+16*t))

def CylinderCase (z : Nat) : Prop :=
  ∃ t : Nat, 81*z+527=512*2^(98+162*(CollatzMersenneRescueCylinder.firstIndex+
    CollatzMersenneRescueCylinder.period*t))

/-- OPEN pointwise obligation. The least reverse defect would have to avoid
the established two-odd layer, every admitted delayed-tail test, and the new
one-sixteenth and second-checkpoint families. The supplied j is an actual
upper ordinary hit. -/
def ResidualExclusion : Prop :=
  ∀ z j : Nat, ReverseDefect z →
    (∀ w : Nat, ReverseDefect w → z≤w) →
    Hits (3*z) j → 3≤CollatzTwoOdd.odds j (3*z) →
    ¬TailCase z → ¬SixteenthCase z → ¬CylinderCase z → False

/-- Complete consumer of the remaining explicit proposition. -/
theorem collatz_from_residual (residual : ResidualExclusion) : UniversalConvergence := by
  classical
  apply Residue17Closure.collatz_iff_reverse_seventeen.mpr
  intro z hz good
  by_contra bad
  have existsDefect : ∃ w : Nat, ReverseDefect w := ⟨z,hz,good,bad⟩
  let w := Nat.find existsDefect
  have hw : ReverseDefect w := Nat.find_spec existsDefect
  have least : ∀ u : Nat, ReverseDefect u → w≤u :=
    fun u hu => Nat.find_min' existsDefect hu
  have noTail := least_defect_not_tail w hw least
  have noSixteenth : ¬SixteenthCase w := by
    rintro ⟨t,parent⟩
    exact MersenneProgressCases.least_defect_not_sixteenth t w hw least parent
  have noCylinder : ¬CylinderCase w := by
    rintro ⟨t,parent⟩
    exact MersenneProgressCases.least_defect_not_cylinder t w hw least parent
  obtain ⟨j,hit⟩ := hw.2.1
  have lower := upper_has_two_odds w j hw.1 hit
  have notTwo := least_defect_not_two_odd quantitative_return w hw least j hit
  exact residual w j hw least hit (by omega) noTail noSixteenth noCylinder

/-- This records the exact remaining strength; it is not a proof of the
left side because the right side has not been established. -/
theorem collatz_iff_residual : UniversalConvergence ↔ ResidualExclusion := by
  constructor
  · intro all z _ bad _ _ _ _ _ _
    exact bad.2.2 (all z (by have := bad.1; omega))
  · exact collatz_from_residual

#print axioms collatz_from_residual
#print axioms collatz_iff_residual
end FinalProgressProposal
