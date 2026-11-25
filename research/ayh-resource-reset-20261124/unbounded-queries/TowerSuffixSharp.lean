import TowerLowerCone

set_option autoImplicit false
set_option warningAsError true

namespace TowerSuffixSharp
open CollatzReverseBasin WordRank

/-- At the selected residue the first synchronous equality of the two
suffixes occurs at clock five. All nonnegative quotients share the words. -/
theorem suffix (a : ℕ) (digit : a%32=5) :
    (∀ t≤4, run t (a+1) ≠ run t (3*a+1)) ∧ run 5 (a+1)=run 5 (3*a+1) := by
  let w:=a/32
  have lx : a+1=2^5*w+6 := by dsimp [w]; omega
  have rx : 3*a+1=2^5*(3*w)+16 := by dsimp [w]; omega
  rw [lx,rx]
  constructor
  · intro t bound
    have phase (q x : ℕ) : run t (2^5*q+x) =
        3^(odds t x)*(2^(5-t)*q)+run t x := by
      rw [show 2^5*q=2^t*(2^(5-t)*q) by
        rw [←Nat.mul_assoc,←pow_add,show t+(5-t)=5 by omega]]
      exact (liftPrefix t _ x).1
    rw [phase w 6,phase (3*w) 16]
    have cases : t=0 ∨ t=1 ∨ t=2 ∨ t=3 ∨ t=4 := by omega
    rcases cases with e|e|e|e|e <;> subst t
    · change 1*(32*w)+6 ≠ 1*(32*(3*w))+16; omega
    · change 1*(16*w)+3 ≠ 1*(16*(3*w))+8; omega
    · change 3*(8*w)+5 ≠ 1*(8*(3*w))+4; omega
    · change 9*(4*w)+8 ≠ 1*(4*(3*w))+2; omega
    · change 9*(2*w)+4 ≠ 1*(2*(3*w))+1; omega
  · rw [(liftPrefix 5 w 6).1,(liftPrefix 5 (3*w) 16).1]
    change 9*w+2=3*(3*w)+2
    omega

/-- On every supplied high-rank edge with this residue suffix and no meeting
by H, the first independent-clock meeting has exact deadline H+5. -/
theorem exact_deadline (z r H a : ℕ) (positive : 0<z) (high : H+4≤r)
    (digit : a%32=5) (left : run H (3^r*z)=a+1)
    (right : run H (3^(r+1)*z)=3*a+1)
    (early : ∀ i≤H, ∀ j≤H, run i (3^r*z)≠run j (3^(r+1)*z)) :
    (∀ i≤H+4, ∀ j≤H+4, run i (3^r*z)≠run j (3^(r+1)*z)) ∧
    run (H+5) (3^r*z)=run (H+5) (3^(r+1)*z) := by
  obtain ⟨prior,join⟩:=suffix a digit
  constructor
  · intro i hi j hj meet
    have eq := (TowerLowerCone.high_tower_merger z r (r+1) (H+4) i j positive
      hi hj (by omega) (by omega) meet).1
    subst j
    by_cases low : i≤H
    · exact early i low i low meet
    · obtain ⟨q,eq⟩:=Nat.exists_eq_add_of_le (show H≤i by omega)
      have cap : q≤4 := by omega
      rw [eq,runAdd H q,runAdd H q,left,right] at meet
      exact prior q cap meet
  · rw [runAdd H 5,runAdd H 5,left,right]
    exact join

#print axioms suffix
#print axioms exact_deadline

end TowerSuffixSharp
