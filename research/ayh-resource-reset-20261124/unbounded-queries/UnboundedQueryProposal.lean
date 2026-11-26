import ClosingProposal
import RationalCenterPump
import FixedCofactorLeastParent
import WideCenterPump

/-! Assembly at the same original least reverse defect. The new exclusions
are proved families of ordinary queries. The pointwise global proposition
`RemainingExclusion` is OPEN. -/
set_option autoImplicit false
set_option warningAsError true

namespace UnboundedQueryProposal
open CollatzReverseBasin CollatzTwoOdd

/-- A finite ordinary two-phase pump with the required source and target. -/
def PumpCase (z : ℕ) : Prop :=
  ∃ n t w m : ℕ, w%48=17 ∧
    81*w+2399=128*(2^(11*n)*t) ∧
    6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936 ∧
    81*z+271=512*2^(9+162*m)

/-- The actual original parent on the preassigned valuation-128 family. -/
def FixedCofactorCase (z : ℕ) : Prop :=
  ∃ w : ℕ, 81*z+527=1024*2^(66*CollatzFixedCofactorLeastParent.sourceV w-5)

/-- Above the exact height cutoff the comparison has no residue restriction. -/
def WidePumpCase (z : ℕ) : Prop :=
  ∃ n t w m : ℕ, 405≤n ∧
    81*w+2399=128*(2^(11*n)*t) ∧
    6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936 ∧
    81*z+271=512*2^(9+162*m)

structure SurvivingCase (z j : ℕ) : Prop extends ClosingProposal.SurvivingCase z j where
  noPump : ¬PumpCase z
  noFixedCofactor : ¬FixedCofactorCase z
  noWidePump : ¬WidePumpCase z

/-- OPEN. This statement quantifies over every supplied survivor, with no
upper rank or bound on the original hitting clock. -/
def RemainingExclusion : Prop := ∀ z j : ℕ, SurvivingCase z j → False

theorem survivor_extends (z j : ℕ) (s : ClosingProposal.SurvivingCase z j) :
    SurvivingCase z j := by
  refine ⟨s,?_,?_,?_⟩
  · rintro ⟨n,t,w,m,wr,start,target,parent⟩
    exact RationalCenterPump.least_excluded n t w z m wr start target parent
      s.defect s.least
  · rintro ⟨w,parent⟩
    exact CollatzFixedCofactorLeastParent.leastExcluded w z parent s.defect s.least
  · rintro ⟨n,t,w,m,enough,start,target,parent⟩
    exact WideCenterPump.least_excluded n t w z m enough start target parent
      s.defect s.least

theorem collatz_from_remaining (remaining : RemainingExclusion) :
    FinalProofProposal.UniversalConvergence := by
  apply ClosingProposal.collatz_from_remaining
  exact fun z j s => remaining z j (survivor_extends z j s)

/-- Equivalence records the scope of the residual problem. The remaining
pointwise exclusion is an explicit premise of the forward consumer. -/
theorem collatz_iff_remaining :
    FinalProofProposal.UniversalConvergence ↔ RemainingExclusion := by
  constructor
  · intro all z j s
    exact (ClosingProposal.collatz_iff_remaining.mp all) z j s.toSurvivingCase
  · exact collatz_from_remaining

#print axioms survivor_extends
#print axioms collatz_from_remaining
#print axioms collatz_iff_remaining

end UnboundedQueryProposal
