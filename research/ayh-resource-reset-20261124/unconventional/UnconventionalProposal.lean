import UnboundedQueryProposal
import AdelicParent
import PerfectPowerParents
import WallRuns81
import WallShifted

/-! Assembly of source-specific consequences at the original least reverse
defect. `RemainingExclusion` remains OPEN. Neither a dense set of successful
parameters nor an exclusion of a periodic wall is asserted to prove it. -/
set_option autoImplicit false
set_option warningAsError true

namespace UnconventionalProposal
open CollatzReverseBasin CollatzTwoOdd WordRank

/-- An actual smaller ordinary source reaching any phase before or at the
Mersenne peak of the supplied parent. All clocks and grades are unrestricted. -/
def SmallQueryCase (z : Nat) : Prop :=
  ∃ m u h w : Nat,
    81*z+271=128*2^(11+162*m) ∧ u≤11+162*m ∧ 0<w ∧
    run h w+1=3^u*2^(11+162*m-u) ∧ 2^40*w<z

def PerfectPowerCase (z : Nat) : Prop :=
  ∃ b : Nat, 81*z+271=128*2^(11+162*b^(2^2956))

private theorem run_basin (h x : Nat) : Basin (run h x) ↔ Basin x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (shortcut x)).trans (SignedCycleDilation.basin_value 1 x)

private theorem run_clock (h x : Nat) : run h x=CollatzMersenneParity.atClock h x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact ih (shortcut x)

theorem small_query_excluded (z : Nat) (query : SmallQueryCase z)
    (least : ∀ y, ReverseDefect y → z≤y) : Basin z := by
  obtain ⟨m,u,h,w,parent,up,wp,meeting,small⟩:=query
  let j:=11+162*m
  have original := (MersenneBarrier.mersenne_prefix z j parent).1
  change run 7 z+1=2^j at original
  change run h w+1=3^u*2^(j-u) at meeting
  have joined : run 7 z=2^j-1 := by omega
  have ascent : run u (2^j-1)=3^u*2^(j-u)-1 := by
    rw [run_clock]
    have e : 2^u*2^(j-u)=(2:Nat)^j := by
      rw [←pow_add,Nat.add_sub_of_le up]
    simpa only [e] using CollatzMersenneParity.ascent u (2^(j-u)) (by positivity)
  have common : run u (run 7 z)=run h w := by rw [joined,ascent]; omega
  by_contra bad
  have lower_bad : ¬Basin w := by
    intro good
    have reached := (run_basin h w).mpr good
    rw [←common] at reached
    exact bad ((run_basin 7 z).mp ((run_basin u (run 7 z)).mp reached))
  obtain ⟨y,dy,cap⟩:=FinalProofProposal.quantitative_return w wp lower_bad
  have lower := least y dy
  omega

/-- The same ordinary wall retains its signed difference at every finite
depth and cannot acquire the period-four tail at any later depth. -/
structure WallTrace (n : Nat) : Prop where
  mixed : WallRefinement.Mixed WallRefinement.actual n
  signed : ∀ k, WallRefinement.sparseSum WallRefinement.actual n k 0 0 =
    WallRefinement.dz WallRefinement.actual n
  no1011 : ∀ r, ∃ k,
    WallRefinement.index WallRefinement.actual
      (WallRefinement.index WallRefinement.actual n r) (4*k) ≠
    WallShadow.block (WallRefinement.index WallRefinement.actual n r) k
  bounded1011 : ∃ J, ∀ j≥J, ¬WallPeriodic.Copies WallRefinement.actual n j 81
  noCyclicShadow : ∀ r L p d : Nat,
    0<L → 0<p → d+1=2^L →
    WallGeneral.PositiveCycle d (-(p:Int)) →
    WallGeneral.PositiveCycle d ((d:Int)-p) →
    ∃ k, WallRefinement.index WallRefinement.actual
      (WallRefinement.index WallRefinement.actual n r) (L*k) ≠
      WallGeneral.address L p (WallRefinement.index WallRefinement.actual n r) k
  cappedCyclicShadow : ∀ L p d : Nat,
    0<L → 0<p → p<2^L → d+1=2^L →
    WallGeneral.PositiveCycle d (-(p:Int)) →
    WallGeneral.PositiveCycle d ((d:Int)-p) →
    ∃ B, 0<B ∧ ∃ J, ∀ j≥J,
      ¬WallWords.Copies WallRefinement.actual n j L p B
  repeatingShadow : ∀ L p d : Nat,
    0<L → 0<p → p<d → d+1=2^L →
    WallDichotomy.Repeats d (-(p:Int)) →
    WallDichotomy.Repeats d ((d:Int)-p) →
    3*p=d ∨ 3*p=2*d ∨
      ∃ B, 0<B ∧ ∃ J, ∀ j≥J,
        ¬WallWords.Copies WallRefinement.actual n j L p B
  capped18 : ∃ B, ∀ j,
    ¬WallWords.Copies WallRefinement.actual n j 18 87383 B

theorem failure_has_wall (z : Nat) (positive : 0<z) (bad : ¬Basin z) :
    ∃ n, 0<n ∧ n<z ∧ WallTrace n := by
  obtain ⟨n,np,nz,mixed,_⟩:=WallRefinement.fixed_source positive bad
  refine ⟨n,np,nz,mixed,WallRefinement.source_difference _ n,?_,?_,?_,?_,?_,?_⟩
  · intro r
    exact WallPeriodic.no_infinite_period _ (WallRefinement.index_mixed _ mixed r)
  · exact WallBank.eventually_no_81 _ mixed
  · intro r L p d lp pp den left right
    exact WallGeneral.breaks _ (WallRefinement.index_mixed _ mixed r)
      L p d lp pp den left right
  · intro L p d lp pp fits den left right
    obtain ⟨B,bp,cap⟩ := WallWords.eventual_cap L p d lp pp fits den left right
    exact ⟨B,bp,cap _ n mixed⟩
  · intro L p d lp pp fits den left right
    rcases WallDichotomy.alternating_or_eventual_cap L p d lp pp fits den left right
      with fraction | fraction | ⟨B,bp,cap⟩
    · exact Or.inl fraction
    · exact Or.inr (Or.inl fraction)
    · exact Or.inr (Or.inr ⟨B,bp,cap _ n mixed⟩)
  · obtain ⟨B,cap⟩ := WallDensity.period18_uniform
    exact ⟨B,cap _ n mixed⟩

structure SurvivingCase (z j : Nat) : Prop extends
    toUnbounded : UnboundedQueryProposal.SurvivingCase z j where
  noSmallQuery : ¬SmallQueryCase z
  noPerfectPower : ¬PerfectPowerCase z
  wall : ∃ n, 0<n ∧ n<z ∧ WallTrace n

/-- OPEN: exclude every original ordinary survivor. No coverage of all
parameters and no annihilation of all aperiodic walls is supplied here. -/
def RemainingExclusion : Prop := ∀ z j : Nat, SurvivingCase z j → False

theorem survivor_extends (z j : Nat) (s : UnboundedQueryProposal.SurvivingCase z j) :
    SurvivingCase z j := by
  refine ⟨s,?_,?_,?_⟩
  · intro query
    exact s.defect.2.2 (small_query_excluded z query s.least)
  · rintro ⟨b,parent⟩
    exact s.defect.2.2 (PerfectPowerParents.excluded b z parent s.least)
  · exact failure_has_wall z (by have := s.defect.1; omega) s.defect.2.2

theorem collatz_from_remaining (remaining : RemainingExclusion) :
    FinalProofProposal.UniversalConvergence := by
  apply UnboundedQueryProposal.collatz_from_remaining
  exact fun z j s => remaining z j (survivor_extends z j s)

/-- Exact strength of the remaining proposition, with no hidden new axiom. -/
theorem collatz_iff_remaining :
    FinalProofProposal.UniversalConvergence ↔ RemainingExclusion := by
  constructor
  · intro all z j s
    exact UnboundedQueryProposal.collatz_iff_remaining.mp all z j s.toUnbounded
  · exact collatz_from_remaining

#print axioms small_query_excluded
#print axioms failure_has_wall
#print axioms survivor_extends
#print axioms collatz_from_remaining
#print axioms collatz_iff_remaining
end UnconventionalProposal
