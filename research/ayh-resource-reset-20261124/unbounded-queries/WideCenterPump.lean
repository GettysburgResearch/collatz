import RationalCenterPump
import FinalProofProposal

/-! Use the exact source height to remove the ternary residue requirement
from the repeated negative cycle comparison. -/
namespace WideCenterPump
open CollatzReverseBasin WordRank

set_option exponentiation.threshold 1000 in
theorem threshold :
    6561*2187^404 < (2:Nat)^40*2048^(404+1) ∧
    (2:Nat)^40*2048^(405+1) ≤ 6561*2187^405 ∧
    2187^422 < (2:Nat)^40*2048^422 ∧
    (2:Nat)^40*2048^423 ≤ 2187^423 := by decide +kernel

set_option exponentiation.threshold 1000 in
private theorem slope (n : Nat) (enough : 405≤n) :
    2^40*2048*2^(11*n) ≤ 6561*3^(7*n) := by
  obtain ⟨k,hk⟩ : ∃ k, n=405+k := ⟨n-405,by omega⟩
  rw [hk,pow_mul (2:Nat) 11 _,pow_mul (3:Nat) 7 _]
  change 2^40*2048*2048^(405+k) ≤ 6561*2187^(405+k)
  have base : 2^40*2048*2048^405≤6561*2187^405 := by
    calc _ = 2^40*2048^(405+1) := by rw [pow_succ]; ac_rfl
         _ ≤ _ := threshold.2.1
  have extension := Nat.mul_le_mul base (Nat.pow_le_pow_left (by decide : 2048≤2187) k)
  simpa only [pow_add,Nat.mul_assoc] using extension

/-- The original positive comparison source is below the quantitative
reverse-defect return floor, with no congruence on the comparator. -/
theorem height (n t w z N : Nat) (enough : 405≤n)
    (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*N+101936)
    (parent : 81*z+271=512*N) : 2^40*w<z := by
  have bound := Nat.mul_le_mul_right t (slope n enough)
  rw [Nat.mul_assoc (2^40*2048) _ t,Nat.mul_assoc 6561 _ t,target] at bound
  omega

private theorem run_basin (h x : Nat) : Basin (run h x) ↔ Basin x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (shortcut x)).trans (SignedCycleDilation.basin_value 1 x)

/-- The lower merger alone now contradicts original-parent minimality.
The reverse-defect return is applied to w itself. -/
theorem least_excluded (n t w z m : Nat) (enough : 405≤n)
    (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936)
    (parent : 81*z+271=512*2^(9+162*m))
    (bad : CollatzTwoOdd.ReverseDefect z)
    (least : ∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) : False := by
  have small := height n t w z _ enough start target parent
  have pos : 0<w := by omega
  let j:=11+162*m
  have ext : 4*2^(9+162*m)=2^j := by
    dsimp [j]; rw [show 11+162*m=2+(9+162*m) by omega,pow_add (2:Nat) 2 (9+162*m)]; rfl
  have orig := (MersenneBarrier.mersenne_prefix z j (by rw [←ext]; omega)).1
  change run 7 z+1=2^j at orig
  obtain ⟨lo,_,_,_⟩ := RationalCenterPump.physical n t w _ start target
  have meeting : run (18+11*n) w=run 7 z := by rw [ext] at lo; omega
  have wb : ¬ Basin w := fun good =>
    bad.2.2 ((run_basin 7 z).mp (meeting ▸ (run_basin _ _).mpr good))
  obtain ⟨y,byd,cap⟩:=FinalProofProposal.quantitative_return w pos wb
  exact (Nat.not_le_of_gt (lt_of_le_of_lt cap small)) (least y byd)

private def digit (n : Nat) : Nat := ((2:Nat)^(20+11*n)*2)%3

private theorem two_unit (e : Nat) : 2^e%3=1 ∨ 2^e%3=2 := by
  induction e with
  | zero => decide
  | succ e ih => rw [pow_succ,Nat.mul_mod]; rcases ih with h|h <;> rw [h] <;> decide

private theorem digit_unit (n : Nat) : digit n=1 ∨ digit n=2 := by
  unfold digit; rw [Nat.mul_mod]
  rcases two_unit (20+11*n) with h|h <;> rw [h] <;> decide

/-- A single shift by the wider period preserves physical integrality and
increments the ternary output by a fixed nonzero digit. -/
theorem integral_shift (n m t w : Nat)
    (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936) :
    ∃ s y : Nat, 81*y+2399=128*(2^(11*n)*s) ∧
      6561*(3^(7*n)*s)=8192*2^(9+162*(m+3^(7+7*n)))+101936 ∧
      y%3=(w+digit n)%3 := by
  let P:=3^(7+7*n)
  let N:=2^(9+162*m)
  obtain ⟨u,eu⟩:=TernaryPowerLift.period (11+7*n)
  have pe : 2*3^(11+7*n)=162*P := by
    dsimp [P]; rw [show 11+7*n=4+(7+7*n) by omega,pow_add]; ring
  have fact : 3^(11+7*n+1)=6561*81*3^(7*n) := by
    rw [show 11+7*n+1=12+7*n by omega,pow_add]; rfl
  rw [pe,fact] at eu
  let A:=3*u+1
  let s:=t+8192*81*N*A
  let y:=w+2^(20+11*n)*N*A
  refine ⟨s,y,?_,?_,?_⟩
  · dsimp [s,y]
    rw [show 81*(w+2^(20+11*n)*N*A)+2399=
      (81*w+2399)+81*(2^(20+11*n)*N*A) by ring,start,pow_add (2:Nat) 20 (11*n)]
    ring
  · change 6561*(3^(7*n)*s)=8192*2^(9+162*(m+P))+101936
    change 6561*(3^(7*n)*t)=8192*N+101936 at target
    rw [show 9+162*(m+P)=(9+162*m)+162*P by ring,pow_add,eu]
    dsimp only [s]
    change 6561*(3^(7*n)*(t+8192*81*N*A))=8192*(N*(1+6561*81*3^(7*n)*A))+101936
    linarith only [target]
  · have Nmod : N%3=2 := by
      dsimp [N]; rw [pow_add,pow_mul,Nat.mul_mod,Nat.pow_mod (2^162) m 3]
      rw [show (2:Nat)^162%3=1 by decide,one_pow]; decide
    have Amod : A%3=1 := by dsimp [A]; omega
    have inc : (2^(20+11*n)*N*A)%3=digit n := by
      rw [Nat.mul_mod, Nat.mul_mod (2^(20+11*n)) N, Nmod,Amod]
      dsimp [digit]
      rw [Nat.mul_mod (2^(20+11*n)) 2]
      omega
    dsimp [y]; rw [Nat.add_mod w _ 3,inc,←Nat.add_mod_mod]
    exact (Nat.add_mod w (digit n) 3).symm

private theorem ternary_residue (w : Nat) (r : w%48=17) : w%3=2 := by omega

private theorem cover_digits (b : Fin 3) (w x y d : Nat) (old : w%3=2) (f : y%3=(2+d)%3)
    (g : x%3=(y%3+d)%3) (unit : d=1 ∨ d=2) : b.val=w%3 ∨ b.val=y%3 ∨ b.val=x%3 := by
  rcases unit with v|v <;> rw [v] at f g <;> omega
/-- Starting at an actual narrow-class parameter, the same wider period
gives three consecutive integral pumps that exhaust all ternary digits. -/
theorem three_digits (n L : Nat) :
    ∃ m : Nat, L≤m ∧ ∀ b : Fin 3, ∃ i t w : Nat, i<3 ∧ w%3=b.val ∧
      81*w+2399=128*(2^(11*n)*t) ∧
      6561*(3^(7*n)*t)=8192*2^(9+162*(m+i*3^(7+7*n)))+101936 := by
  obtain ⟨m,t,w,large,res,sta,tar⟩:=RationalCenterPump.cofinal_pumps n L
  let P:=3^(7+7*n)
  obtain ⟨s,y,sy,ty,dy⟩:=integral_shift n m t w sta tar
  obtain ⟨r,x,sx,tx,dx⟩:=integral_shift n (m+P) s y sy ty
  have old : w%3=2 := ternary_residue _ res
  have f : y%3=(2+digit n)%3 := by rw [dy,Nat.add_mod w,old,Nat.add_mod_mod]
  have g : x%3=(y%3+digit n)%3 := by rw [dx,Nat.add_mod y,Nat.add_mod_mod]
  refine ⟨m,large,fun b => ?_⟩
  have cover := cover_digits b w x y (digit n) old f g (digit_unit n)
  rcases cover with b0|b1|b2
  · exact ⟨0,t,w,by decide,b0.symm,sta,by simpa using tar⟩
  · exact ⟨1,s,y,by decide,b1.symm,sy,by simpa using ty⟩
  · refine ⟨2,r,x,by decide,b2.symm,sx,?_⟩
    change 6561*(3^(7*n)*r)=8192*2^(9+162*(m+2*P))+101936
    rwa [show m+2*P=m+P+P by ring]

/-- The same base m and period work at every nonnegative progression index.
Every parent in that full progression is excluded. -/
theorem excluded_progression (n L : Nat) (enough : 405≤n) : ∃ m, L≤m ∧ ∀ i z : Nat,
    81*z+271=512*2^(9+162*(m+i*3^(7+7*n))) →
    CollatzTwoOdd.ReverseDefect z → (∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) → False := by
  obtain ⟨m,t,w,large,_,sta,tar⟩ := RationalCenterPump.cofinal_pumps n L
  let P:=3^(7+7*n)
  have row (i : Nat) : ∃ s y : Nat, 81*y+2399=128*(2^(11*n)*s) ∧
      6561*(3^(7*n)*s)=8192*2^(9+162*(m+i*P))+101936 := by
    induction i with
    | zero => exact ⟨t,w,sta,by simpa using tar⟩
    | succ i ih =>
      obtain ⟨s,y,a,b⟩:=ih
      obtain ⟨v,x,c,d,_⟩:=integral_shift n (m+i*P) s y a b
      refine ⟨v,x,c,?_⟩
      change 6561*(3^(7*n)*v)=8192*2^(9+162*((m+i*P)+P))+101936 at d
      rwa [show m+(i+1)*P=(m+i*P)+P by ring]
  refine ⟨m,large,fun i z par bad least => ?_⟩
  obtain ⟨s,y,a,b⟩:=row i
  exact least_excluded n s y z (m+i*P) enough a b par bad least

#print axioms excluded_progression
#print axioms threshold
#print axioms height
#print axioms least_excluded
#print axioms integral_shift
#print axioms three_digits
end WideCenterPump
