import FinalProgressProposal
import GuardedResidueCover
import DifferentCycleAnchors
import MersenneTwoCenter
import DefectClockFloor

/-! Final assembly of the proved source exclusions and clock constraints.

`RemainingExclusion` is OPEN. This file proves its exact equivalence with
universal convergence; it does not supply a proof of that proposition.
Every clock and query in the hypotheses concerns the supplied ordinary
source. A density statement or a successful lift at a different source
cannot discharge this obligation. -/
namespace ClosingProposal
open CollatzReverseBasin CollatzTwoOdd FinalProofProposal FinalProgressProposal

def CommonCycleCase (z : Nat) : Prop :=
  ∃ t w : Nat, w+1183=6442450944*t ∧ z+1183=7247757312*t

def DifferentCycleCase (z : Nat) : Prop :=
  ∃ t w : Nat, z+1807=1610612736*t ∧ w+127=75497472*t

def TwoCenterCase (z : Nat) : Prop :=
  ∃ i : Fin 13, ∃ t : Nat,
    81*z+271=512*2^(9+162*((MersenneTwoCenter.row i).first+
      (MersenneTwoCenter.row i).period*t))

def TernaryCase (z : Nat) : Prop :=
  ∃ k : Nat, 81*z+527=512*2^(98+162*(181+2187*k))

/-- Every condition here is a proved necessary condition on the same least
reverse defect. The upper certificate is an actual ordinary hit; it need
not be a first hit. This record is not asserted to have an inhabitant. -/
structure SurvivingCase (z j : Nat) : Prop where
  defect : ReverseDefect z
  least : ∀ w : Nat, ReverseDefect w → z≤w
  upperHit : Hits (3*z) j
  upperRank : 3≤CollatzTwoOdd.odds j (3*z)
  noTail : ¬SourceProgressCases.TailCase z
  noSixteenth : ¬SixteenthCase z
  noCylinder : ¬CylinderCase z
  noGuarded : ¬GuardedResidueCover.covered z
  noCommonCycle : ¬CommonCycleCase z
  noDifferentCycle : ¬DifferentCycleCase z
  noTwoCenter : ¬TwoCenterCase z
  noTernary : ¬TernaryCase z
  allClocks : ∀ h B : Nat, B≤2720 →
    B^(WordRank.odds h z)*2^h ≤ (3*B+1)^(WordRank.odds h z)*2^40
  clock1024 : 621≤WordRank.odds 1024 z

/-- OPEN universal, source-specific obligation. No theorem in this packet
proves it. A proof must exclude all records, with no upper-rank or clock
bound, including sources outside all finite banks. If it uses rational
references, no denominator-depth bound is assumed. -/
def RemainingExclusion : Prop := ∀ z j : Nat, SurvivingCase z j → False

/-- Attach all newly proved exclusions to the previous residual source. -/
theorem residual_survives (z j : Nat) (bad : ReverseDefect z)
    (least : ∀ w : Nat, ReverseDefect w → z≤w)
    (hit : Hits (3*z) j) (rank : 3≤CollatzTwoOdd.odds j (3*z))
    (noTail : ¬SourceProgressCases.TailCase z)
    (noSixteenth : ¬SixteenthCase z) (noCylinder : ¬CylinderCase z) :
    SurvivingCase z j := by
  refine ⟨bad,least,hit,rank,noTail,noSixteenth,noCylinder,?_,?_,?_,?_,?_,?_,?_⟩
  · exact fun cov => GuardedResidueCover.least_excluded z bad least cov
  · rintro ⟨t,w,hw,hz⟩
    exact SignedCycleDilation.least_not_minus1183 t w z hw hz bad least
  · rintro ⟨t,w,hz,hw⟩
    obtain ⟨residue,smaller,lower,upper⟩ := DifferentCycleAnchors.two_anchors t z w hz hw
    exact SignedCycleDilation.no_least_of_pair z w bad least residue smaller lower upper
  · rintro ⟨i,t,parent⟩
    exact MersenneTwoCenter.least_excluded i t z parent bad least
  · rintro ⟨k,parent⟩
    exact DefectClockFloor.least_not_ternary_row k z bad least parent
  · exact DefectClockFloor.least_all_clocks z bad least
  · exact DefectClockFloor.least_1024 z bad least

/-- Complete consumer, with its unproved mathematical input explicit. -/
theorem collatz_from_remaining (remaining : RemainingExclusion) : UniversalConvergence := by
  apply FinalProgressProposal.collatz_from_residual
  intro z j bad least hit rank noTail noSixteenth noCylinder
  exact remaining z j (residual_survives z j bad least hit rank noTail noSixteenth noCylinder)

/-- An exact description of the remaining strength, not a proof of either
side. In particular the reverse direction does not discharge `remaining`. -/
theorem collatz_iff_remaining : UniversalConvergence ↔ RemainingExclusion := by
  constructor
  · intro all z _ survivor
    have positive : 0<z := by have := survivor.defect.1; omega
    exact survivor.defect.2.2 (all z positive)
  · exact collatz_from_remaining

#print axioms residual_survives
#print axioms collatz_from_remaining
#print axioms collatz_iff_remaining
end ClosingProposal
