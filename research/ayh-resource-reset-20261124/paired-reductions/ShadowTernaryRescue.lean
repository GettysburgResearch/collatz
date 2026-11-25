import OddClockFloor
import OppositeArm
import RankThreeFamily

/-! The ternary positive-cycle query excludes the specified indices in the
simultaneous binary-shadow family, at the original parent. -/
namespace ShadowTernaryRescue

open CollatzReverseBasin CollatzTwoOdd CollatzMersenneParity

set_option exponentiation.threshold 100000 in
private theorem power_residue (u : Nat) :
    2^(18*(2034+2187*u))%59049=32320 := by
  induction u with
  | zero => decide +kernel
  | succ u ih =>
    rw [show 18*(2034+2187*(u+1))=18*(2034+2187*u)+39366 by omega,
      pow_add,Nat.mul_mod,ih,show (2:Nat)^39366%59049=1 by decide +kernel]

set_option maxHeartbeats 2000000 in
theorem shadow_parameter (u m : Nat) (shadow : 27*m+17=44*2^(18*(2034+2187*u))) :
    m=181+2187*(m/2187) := by
  have rhs : (44*2^(18*(2034+2187*u)))%59049=4904 := by
    rw [Nat.mul_mod,power_residue]
  have v : (27*m+17)%59049=4904 := (congrArg (·%59049) shadow).trans rhs
  clear shadow rhs
  omega

private theorem clock_run (k n : Nat) : atClock k n=WordRank.run k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (shortcut n)

/-- The returned source is the specified parent; uniqueness follows from
its displayed integer equation. Only the existing quantitative return
theorem is a parameter in this dependency-light module. -/
theorem ternary_row_excluded (k z : Nat) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w)
    (back : ∀ n, 0<n → ¬Basin n → ∃ w, ReverseDefect w ∧ w≤2^40*n)
    (parent : 81*z+527=512*2^(98+162*(181+2187*k))) : False := by
  let m := 181+2187*k
  obtain ⟨z',_,_,he,_,_,same⟩ := CollatzRankThree.rank_three_family m
  change 81*z+527=512*2^(98+162*m) at parent
  have eq : z'=z := by omega
  subst z'
  have known := CollatzMersenneParity.even_mersenne_basin (48+81*m)
  rw [show 2*(48+81*m)+2=98+162*m by omega,
      show 2*(48+81*m)+1=97+162*m by omega] at known
  have mbad : ¬Basin (2^(97+162*m)-1) := fun good => bad.2.2 (same.mpr (known.mpr good))
  have j : 97+162*m=29419+354294*k := by dsimp [m]; omega
  have parent' : 81*z+527=2^(29429+354294*k) := by
    rw [show 98+162*m=(97+162*m)+1 by omega,j,Nat.pow_succ] at parent
    rw [show 29429+354294*k=(29419+354294*k)+10 by omega,pow_add]
    omega
  obtain ⟨w,v,hw,_,vp,small,low,_,drop⟩ := CollatzOppositeArm.family_query k
  have veq : v=z := by omega
  subst v
  have wb : ¬Basin w := by
    intro good
    apply mbad
    rw [j,←low,clock_run]
    exact (PositiveWordDescent.basinRun 21 w).mpr good
  have common : Basin (atClock 224 (3*w)) ↔ Basin (3*w) := by
    rw [clock_run]; exact PositiveWordDescent.basinRun ..
  by_cases triple : Basin (3*w)
  · exact Nat.not_le_of_lt small (least w ⟨hw,triple,wb⟩)
  · have hp : 0<atClock 224 (3*w) := by
      rw [clock_run]; exact OddClockFloor.run_pos _ _ (by omega)
    obtain ⟨y,hy,bound⟩ := back _ hp (fun good => triple (common.mp good))
    have impossible := least y hy
    omega

/-- The same t and original z are supplied in both equations. -/
theorem simultaneous_shadow_rescue (u m z : Nat)
    (shadow : 27*m+17=44*2^(18*(2034+2187*u)))
    (parent : 81*z+527=512*2^(98+162*m)) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w)
    (back : ∀ n, 0<n → ¬Basin n → ∃ w, ReverseDefect w ∧ w≤2^40*n) : False := by
  have eq := shadow_parameter u m shadow
  apply ternary_row_excluded (m/2187) z bad least back
  simpa only [←eq] using parent

#print axioms shadow_parameter
#print axioms ternary_row_excluded
#print axioms simultaneous_shadow_rescue
end ShadowTernaryRescue
