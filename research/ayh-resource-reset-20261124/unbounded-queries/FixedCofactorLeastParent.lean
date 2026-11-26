import FixedCofactorRescue
import MersenneProgressCases

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 4096
set_option maxHeartbeats 1200000

namespace CollatzFixedCofactorLeastParent
open CollatzReverseBasin CollatzTwoOdd CollatzMersenneParity

def sourceV (w : ℕ) : ℕ := 2^128*(1+2^49*(27*w))
def sourceM (w : ℕ) : ℕ := (11*sourceV w-17)/27

theorem rowArithmetic (w : ℕ) :
    sourceV w % 27=4 ∧ 27*sourceM w+17=11*sourceV w ∧
    97+162*sourceM w=66*sourceV w-5 ∧ 42*sourceV w+21<66*sourceV w-5 := by
  dsimp [sourceV,sourceM]
  omega

/-- Exact overlap with the older sixteenth, binary cylinder and ternary row. -/
theorem oldRows (w : ℕ) :
    sourceM w % 16=13 ∧
    CollatzMersenneRescueCylinder.firstIndex%16=7 ∧
    (sourceM w%2187=181 ↔ w%2187=403) ∧ sourceM 0%2187=2121 := by
  have m : sourceM w=138633556893715670299893358583312975037+(11*2^177)*w := by
    dsimp [sourceV,sourceM]
    omega
  rw [m]
  refine ⟨by omega,by decide,?_,by decide⟩
  have e : (138633556893715670299893358583312975037+(11*2^177)*w)%2187 =
      (2121+565*w)%2187 := by omega
  rw [e]
  constructor
  · intro h
    have comb : (565*w+1940)%2187=0 := by omega
    omega
  · omega

private theorem memClock (k n : ℕ) : Basin (atClock k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    refine (ih (shortcut n)).trans ⟨?_,?_⟩
    · rintro ⟨t,ht⟩; exact ⟨t+1,ht⟩
    · rintro ⟨t,ht⟩
      cases t with
      | zero => change n=1 at ht; subst n; exact ⟨1,rfl⟩
      | succ t => exact ⟨t,ht⟩

/-- The source equation alone selects the same ordinary rank-three parent.
The only comparison premise is the usual absence of smaller reverse defects. -/
theorem parentBasin (w z : ℕ) (parent : 81*z+527=1024*2^(66*sourceV w-5))
    (minimal : ∀ y : ℕ, y%48=17 → y<z → Basin (3*y) → Basin y) :
    Basin z := by
  classical
  let v:=sourceV w
  let m:=sourceM w
  let j:=97+162*m
  obtain ⟨_,_,row,earlierN⟩:=rowArithmetic w
  change j=66*v-5 at row
  change 42*v+21<66*v-5 at earlierN
  have big : 128≤v := by dsimp [v,sourceV]; omega
  have parent' : 81*z+527=1024*2^j := by rw [row]; exact parent
  have nextIndex : 98+162*m=j+1 := by dsimp [j]; omega
  have parentNext : 81*z+527=512*2^(98+162*m) := by
    rw [nextIndex,pow_succ,parent']
    omega
  by_contra bad
  obtain ⟨z',_,_,eq,_,_,same⟩:=CollatzRankThree.rank_three_family m
  have ident : z'=z := by omega
  subst z'
  have merBad : ¬Basin (2^(98+162*m)-1) := fun good => bad (same.mpr good)
  obtain ⟨first,earlier⟩:=CollatzMersenneFirstBad.exact_first_bad m z parentNext
    CollatzQuantitativeReturn.bounded_return minimal merBad
  have second:=(CollatzMersenneTwoCheckpoints.two_bad_checkpoints m z j rfl
    parent' minimal first).2
  have r : (j-1)%11=5 := by omega
  have s : 3+7*((j-1)/11)=42*v-4 := by omega
  rw [r,s,show (2:ℕ)^5=32 by decide,Nat.mul_comm] at second
  have good:=earlier (42*v+21) (by omega) (by change 42*v+21<j; omega)
  have hit:=CollatzFixedCofactorRescue.fixedCofactorFamily (27*w)
  change atClock 183 (32*3^(42*v-4)-17) =
    atClock ((42*v+21)+178) (2^(42*v+21)-1) at hit
  have endGood := (memClock ((42*v+21)+178) (2^(42*v+21)-1)).mpr good
  rw [←hit] at endGood
  exact second ((memClock 183 (32*3^(42*v-4)-17)).mp endGood)

/-- Complete consumer at the fixed original least reverse defect, including
the case w=0 with the preassigned cofactor one. -/
theorem leastExcluded (w z : ℕ) (parent : 81*z+527=1024*2^(66*sourceV w-5))
    (bad : ReverseDefect z) (least : ∀ y, ReverseDefect y → z≤y) : False := by
  apply bad.2.2 (parentBasin w z parent ?_)
  intro y res lt good
  by_contra nb
  exact (Nat.not_le_of_lt lt) (least y ⟨res,good,nb⟩)

#print axioms rowArithmetic
#print axioms oldRows
#print axioms parentBasin
#print axioms leastExcluded

end CollatzFixedCofactorLeastParent
