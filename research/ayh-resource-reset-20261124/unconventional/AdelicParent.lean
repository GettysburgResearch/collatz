import AdelicSwitch
import FinalProofProposal
import MersenneBarrier
import SignedCycleDilation

/-! Attach the dense ternary-cylinder construction to the original
positive least reverse defect, using its ordinary lower orbit. -/
namespace AdelicParent
open CollatzReverseBasin WordRank

private theorem run_basin (h x : Nat) : Basin (run h x) ↔ Basin x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (shortcut x)).trans (SignedCycleDilation.basin_value 1 x)

/-- Every supplied parent on one complete subprogression in every
prescribed ternary class reaches one under its own leastness bound. -/
theorem cylinder_excluded (k a : Nat) : ∃ v : Nat,
    v<3^(AdelicSwitch.tailDepth k 40+3) ∧ ∀ i z : Nat,
    let m:=a+3^k*v+3^(k+(AdelicSwitch.tailDepth k 40+3))*i
    81*z+271=128*2^(11+162*m) →
    (∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) → Basin z := by
  obtain ⟨h,v,_,vs,row⟩:=AdelicSwitch.cylinder k a 40
  refine ⟨v,vs,fun i z par least => ?_⟩
  let m:=a+3^k*v+3^(k+(AdelicSwitch.tailDepth k 40+3))*i
  let j:=11+162*m
  let H:=4+AdelicSwitch.tailDepth k 40+h
  obtain ⟨w,wp,_,ep,_,small⟩:=row i
  change run H w+1=2^j at ep
  change 2^40*w<2^j-1 at small
  change 81*z+271=128*2^j at par
  have orig := (MersenneBarrier.mersenne_prefix z j par).1
  change run 7 z+1=2^j at orig
  have hit : run 7 z=run H w := by omega
  have big : 2048≤(2:Nat)^j := Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 11≤j by dsimp [j]; omega)
  by_contra bad
  have wb : ¬Basin w := fun good => bad ((run_basin 7 z).mp (hit ▸ (run_basin H w).mpr good))
  obtain ⟨y,byd,cap⟩:=FinalProofProposal.quantitative_return w wp wb
  have bound := least y byd
  omega

#print axioms cylinder_excluded
end AdelicParent
