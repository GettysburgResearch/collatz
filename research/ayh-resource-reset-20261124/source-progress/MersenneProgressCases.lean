import MersenneTwoCheckpoints
import MersenneRescueCylinder
import MersenneFirstBad
import RankThreeFamily
import QuantitativeReturn

/-! Ordinary closure of one-sixteenth of the remaining e=7 parameter row,
using the proved quantitative return and the new source-dependent checkpoint.
This is a proved family exclusion at a least reverse defect, not a complete
cover of the Mersenne row. -/
namespace MersenneProgressCases
open CollatzReverseBasin CollatzTwoOdd

theorem sixteenth_closure (t z : Nat)
    (parent : 81*z+527=512*2^(98+162*(3+16*t)))
    (minimal : ∀ w : Nat, w%48=17 → w<z → Basin (3*w) → Basin w) : Basin z := by
  classical
  let m := 3+16*t
  let j := 97+162*m
  change 81*z+527=512*2^(98+162*m) at parent
  by_contra bad
  obtain ⟨v,k,_,eq,_,_,same⟩ := CollatzRankThree.rank_three_family m
  have vz : v=z := by omega
  subst v
  have merBad : ¬Basin (2^(98+162*m)-1) := fun h => bad (same.mpr h)
  obtain ⟨firstBad,earlier⟩ := CollatzMersenneFirstBad.exact_first_bad m z parent
    CollatzQuantitativeReturn.bounded_return minimal merBad
  have parent' : 81*z+527=1024*2^j := by
    rw [parent,show 98+162*m=j+1 by dsimp [j];omega,Nat.pow_succ]
    omega
  exact firstBad (CollatzMersenneTwoCheckpoints.exclude_sixteenth t z m j rfl rfl
    parent' minimal earlier)

theorem least_defect_not_sixteenth (t z : Nat) (bad : ReverseDefect z)
    (least : ∀ w : Nat, ReverseDefect w → z≤w)
    (parent : 81*z+527=512*2^(98+162*(3+16*t))) : False := by
  apply bad.2.2
  apply sixteenth_closure t z parent
  intro w residue smaller good
  by_contra notGood
  have h := least w ⟨residue,good,notGood⟩
  omega

/-- The explicit second-checkpoint progression also closes with the actual
quantitative return and first-bad-index theorem. -/
theorem cylinder_closure (t z : Nat)
    (parent : 81*z+527=512*2^(98+162*(CollatzMersenneRescueCylinder.firstIndex+
      CollatzMersenneRescueCylinder.period*t)))
    (minimal : ∀ w : Nat, w%48=17 → w<z → Basin (3*w) → Basin w) : Basin z := by
  classical
  let m := CollatzMersenneRescueCylinder.firstIndex+CollatzMersenneRescueCylinder.period*t
  let j := 97+162*m
  change 81*z+527=512*2^(98+162*m) at parent
  by_contra bad
  obtain ⟨v,k,_,eq,_,_,same⟩ := CollatzRankThree.rank_three_family m
  have vz : v=z := by omega
  subst v
  have merBad : ¬Basin (2^(98+162*m)-1) := fun h => bad (same.mpr h)
  obtain ⟨firstBad,earlier⟩ := CollatzMersenneFirstBad.exact_first_bad m z parent
    CollatzQuantitativeReturn.bounded_return minimal merBad
  have parent' : 81*z+527=1024*2^j := by
    rw [parent,show 98+162*m=j+1 by dsimp [j];omega,Nat.pow_succ]
    omega
  exact firstBad (CollatzMersenneRescueCylinder.cylinder_first_bad_excluded t z m j
    rfl rfl parent' minimal earlier)

theorem least_defect_not_cylinder (t z : Nat) (bad : ReverseDefect z)
    (least : ∀ w : Nat, ReverseDefect w → z≤w)
    (parent : 81*z+527=512*2^(98+162*(CollatzMersenneRescueCylinder.firstIndex+
      CollatzMersenneRescueCylinder.period*t))) : False := by
  apply bad.2.2
  apply cylinder_closure t z parent
  intro w residue smaller good
  by_contra notGood
  have h := least w ⟨residue,good,notGood⟩
  omega

#print axioms sixteenth_closure
#print axioms least_defect_not_sixteenth
#print axioms cylinder_closure
#print axioms least_defect_not_cylinder
end MersenneProgressCases
