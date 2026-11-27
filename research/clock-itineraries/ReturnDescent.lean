module

public import TowerFrontierAffine
public import BasinTransport
import all TernaryItinerary
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.ReturnDescent

open TowerFrontier
set_option autoImplicit false
set_option maxHeartbeats 1000000

@[expose] def M (t : Nat) : Nat := 2^t-1

/-- The two supplied ordinary starts share a physical iterate, at independent clocks. -/
@[expose] def Meets (x y : Nat) : Prop := ∃ i j, run i x=run j y

theorem Meets.symm {x y : Nat} (h : Meets x y) : Meets y x := by
  obtain ⟨i,j,h⟩ := h
  exact ⟨j,i,h.symm⟩

theorem Meets.trans {x y z : Nat} (xy : Meets x y) (yz : Meets y z) : Meets x z := by
  obtain ⟨i,j,eq⟩ := xy
  obtain ⟨k,l,eq'⟩ := yz
  refine ⟨i+k,l+j,?_⟩
  rw [run_add,eq,←run_add,Nat.add_comm j k,run_add k,eq',←run_add]

theorem reaches_of_meets {x y : Nat} (hit : ReachesOne y) (meet : Meets x y) : ReachesOne x := by
  obtain ⟨i,j,h⟩ := meet
  obtain ⟨k,hk⟩ := hit
  by_cases le : j≤k
  · refine ⟨i+(k-j),?_⟩
    rw [run_add,h,←run_add,show j+(k-j)=k by omega,hk]
  · have dy := Nat.sub_add_cancel (show k≤j by omega)
    have aft : run j y=run (j-k) 1 := by
      calc
        run j y=run (k+(j-k)) y := congrArg (fun t => run t y) (by omega)
        _ = _ := by rw [run_add,hk]
    have lap (n : Nat) : run (2*n) 1=1 := by
      induction n with
      | zero => rfl
      | succ n ih => rw [Nat.mul_succ,run_add,ih]; rfl
    refine ⟨i+(j-k),?_⟩
    rw [run_add,h,aft,←run_add,show j-k+(j-k)=2*(j-k) by omega,lap]

private theorem ramp (t u : Nat) (hu : 0<u) :
    run t (2^t*u-1)=3^t*u-1 := by
  simpa only [Nat.zero_add,Nat.pow_zero,Nat.one_mul,run] using BasinTransport.affine_rays t 0 0 u hu

theorem peak (t : Nat) : run t (M t)=3^t-1 := by
  simpa only [M,Nat.mul_one] using ramp t 1 (by decide)

private theorem three_odd (a : Nat) : ∃ u, 3^(2*a+1)=4*u+3 := by
  induction a with
  | zero => exact ⟨0,rfl⟩
  | succ a ih =>
    obtain ⟨u,hu⟩ := ih
    refine ⟨9*u+6,?_⟩
    rw [show 2*(a+1)+1=(2*a+1)+2 by omega,Nat.pow_add,hu]
    omega

/-- Consecutive exponents with odd first exponent share a positive future. -/
theorem neighbors (a : Nat) : Meets (M (2*a+1)) (M (2*a+2)) := by
  obtain ⟨u,hu⟩ := three_odd a
  have big : 3^(2*a+2)=(4*u+3)*3 := by rw [show 2*a+2=(2*a+1)+1 by omega,Nat.pow_succ,hu]
  refine ⟨(2*a+1)+2,(2*a+2)+2,?_⟩
  rw [run_add,peak,run_add,peak,hu,big]
  simp only [run,step]
  split <;> split <;> split <;> split <;> omega

theorem track_run (h n e : Nat) : (track h n e).1=run h n := by
  induction h generalizing n e with
  | zero => rfl
  | succ h ih => simp only [run,track,step]; split <;> apply ih

private theorem same_grade (h n u e : Nat) :
    (track h (n+2^h*u) e).2=(track h n e).2 := by
  induction h generalizing n u e with
  | zero => rfl
  | succ h ih =>
    have shape : 2^(h+1)*u=2*(2^h*u) := by rw [Nat.pow_succ]; ac_rfl
    rw [shape,track,track,show (n+2*(2^h*u))%2=n%2 by omega]
    split
    · rw [show (n+2*(2^h*u))/2=n/2+2^h*u by omega,ih]
    · rw [show (3*(n+2*(2^h*u))+1)/2=(3*n+1)/2+2^h*(3*u) by rw [Nat.mul_left_comm _ 3]; omega,ih]

theorem track_lift (h n u : Nat) :
    track h (n+2^h*u) 0 = ((track h n 0).1+3^(track h n 0).2*u,(track h n 0).2) := by
  apply Prod.ext
  · rw [track_run]
    simpa only [Nat.pow_zero,Nat.mul_one] using affine h n 0 u
  · exact same_grade h n u 0

private theorem track_halves (j e : Nat) : track j (2^j) e=(1,e) := by
  induction j generalizing e with
  | zero => rfl
  | succ j ih =>
    simp only [Nat.pow_succ,track,show 2^j*2%2=0 by omega,↓reduceIte,
      show 2^j*2/2=2^j by omega]
    apply ih

private theorem track_append (i j n e : Nat) :
    track (i+j) n e=track j (track i n e).1 (track i n e).2 := by
  induction i generalizing n e with
  | zero => simp [track]
  | succ i ih => rw [Nat.succ_add,track,track]; split <;> apply ih

/-- A three-odd canonical representative at a controlled clock and height. -/
@[expose] def Representative (t H Y : Nat) : Prop :=
  Y%48=17 ∧ Y<2^H ∧ track H (3*Y) 0=(1,3) ∧ Meets Y (M t)

private def liftFactor : Nat → Nat
  | 0 => 0
  | j+1 => liftFactor j+2^(162*j)*((2^162-1)/243)

private theorem liftFactor_spec (j : Nat) : 1+243*liftFactor j=2^(162*j) := by
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [liftFactor,Nat.mul_add 243,Nat.mul_succ 162 j,Nat.pow_add 2,
      show 1+(243*liftFactor j+243*(2^(162*j)*((2^162-1)/243))) =
        (1+243*liftFactor j)+2^(162*j)*(243*((2^162-1)/243)) by ac_rfl,ih]
    exact (show ∀ x : Nat, x+x*(243*((2^162-1)/243))=x*2^162 by
      intro x
      rw [Nat.add_comm,←Nat.mul_succ]) _

/-- One verified ordinary template extends to every exponent on its full row. -/
theorem extend_row {t H Y a b h u v : Nat} (small : Y<2^H) (classY : Y%48=17)
    (size : 4≤H) (Lclock : h+a=H) (Uclock : u+v=H) (base : a+b=t)
    (lower : track h Y 0=(2^a*3^b-1,b+4))
    (upper : track u (3*Y) 0=(2^v,3)) (j : Nat) :
    ∃ y, Representative (t+162*j) (H+162*j) y := by
  let D := liftFactor j
  let y := Y+2^H*(3*D)
  have factor : 1+243*D=2^(162*j) := liftFactor_spec j
  have mul_split (s c : Nat) (eq : s+c=H) : 2^H=2^s*2^c := by rw [←eq,Nat.pow_add]
  have yl : y=Y+2^h*(2^a*(3*D)) := by dsimp only [y]; rw [mul_split h a Lclock,Nat.mul_assoc]
  have yu : 3*y=3*Y+2^u*(2^v*(9*D)) := by
    dsimp only [y]
    rw [Nat.mul_add,mul_split u v Uclock]
    change 3*Y+3*(2^u*2^v*(3*D))=3*Y+2^u*(2^v*((3*3)*D))
    ac_rfl
  have lp := track_lift h Y (2^a*(3*D))
  have up := track_lift u (3*Y) (2^v*(9*D))
  rw [←yl,lower] at lp
  rw [←yu,upper] at up
  have positive : 0<2^a*3^b := Nat.mul_pos (Nat.two_pow_pos _) (Nat.pow_pos (by decide))
  have lowerValue : 2^a*3^b-1+3^(b+4)*(2^a*(3*D))=2^(a+162*j)*3^b-1 := by
    rw [Nat.pow_add 2 a,←factor,Nat.pow_add 3 b 4,Nat.mul_add,Nat.mul_one]
    have calcEq : 3^b*3^4*(2^a*(3*D))=2^a*(243*D)*3^b := by
      change 3^b*(81:Nat)*(2^a*(3*D))=2^a*((81*3)*D)*3^b
      ac_rfl
    rw [calcEq,Nat.add_mul]
    omega
  have upperValue : 2^v+3^3*(2^v*(9*D))=2^(v+162*j) := by
    rw [Nat.pow_add,←factor,Nat.mul_add,Nat.mul_one]
    congr 1
    change 27*(2^v*(9*D))=2^v*((27*9)*D)
    ac_rfl
  have lrun : run h y=2^(a+162*j)*3^b-1 := by rw [←track_run h y 0,lp,lowerValue]
  have urun : track (H+162*j) (3*y) 0=(1,3) := by
    rw [show H+162*j=u+(v+162*j) by omega,track_append,up,upperValue,track_halves]
  have ht : y%48=17 := by
    have powsp := mul_split 4 (H-4) (by omega)
    have fact : 2^H*(3*D)=48*(2^(H-4)*D) := by rw [powsp]; change 16*2^(H-4)*(3*D)=(16*3)*(2^(H-4)*D); ac_rfl
    dsimp only [y]
    rw [fact,Nat.add_mul_mod_self_left,classY]
  have bound : y<2^(H+162*j) := by
    rw [Nat.pow_add,←factor,Nat.mul_add,Nat.mul_one]
    exact Nat.add_lt_add_of_lt_of_le small (Nat.mul_le_mul_left _ (by omega))
  refine ⟨y,ht,bound,urun,h+(a+162*j),t+162*j,?_⟩
  rw [run_add,lrun,ramp _ _ (Nat.pow_pos (by decide)),peak,←Nat.pow_add]
  congr 2
  omega

/-- The original three-odd hard parent at Mersenne exponent 11+162j. -/
@[expose] def hardParent (m : Nat) : Nat := (2^(m+7)-271)/81

theorem hard_source_data (j : Nat) :
    let m := 11+162*j
    let z := hardParent m
    2^m<z ∧ z%48=17 ∧ run 7 z=M m ∧ track 9 (3*z) 0=(2^(m-2),3) ∧
    track (m+7) (3*z) 0=(1,3) := by
  intro m z
  let D := liftFactor j
  have fd : 1+243*D=2^(162*j) := liftFactor_spec j
  have pow : 2^m=2048*(1+243*D) := by rw [fd]; exact Nat.pow_add ..
  have xp : 2^(m+7)=128*2^m := by rw [Nat.pow_add,Nat.mul_comm]
  have form : z=3233+786432*D := by
    change (2^(m+7)-271)/81=_
    rw [xp,pow]; omega
  have lo : z=3233+2^7*(6144*D) := by rw [form]; omega
  have up : 3*z=9699+2^9*(4608*D) := by rw [form]; omega
  have lref : track 7 3233 0=(2047,4) := by decide
  have uref : track 9 9699 0=(512,3) := by decide
  have ld := track_lift 7 3233 (6144*D)
  have ud := track_lift 9 9699 (4608*D)
  rw [←lo,lref] at ld
  rw [←up,uref] at ud
  have endU : 512+3^3*(4608*D)=2^(9+162*j) := by
    rw [Nat.pow_add,←fd]; omega
  refine ⟨by rw [form,pow]; omega,by rw [form]; omega,?_,?_,?_⟩
  · rw [←track_run 7 z 0,ld,M,pow]
    change 2047+81*(6144*D)=2048*(1+243*D)-1
    omega
  · rw [ud,endU,show m-2=9+162*j by dsimp only [m]; omega]
  · rw [show m+7=9+(9+162*j) by dsimp only [m]; omega,track_append,ud,endU,track_halves]

theorem hard_source (j : Nat) :
    let m := 11+162*j
    let z := hardParent m
    2^m<z ∧ z%48=17 ∧ run 7 z=M m ∧ track (m+7) (3*z) 0=(1,3) := by
  obtain ⟨a,b,c,_,d⟩ := hard_source_data j
  exact ⟨a,b,c,d⟩

private theorem laps (d e : Nat) : track (2*d) 1 e=(1,e+d) := by
  induction d with
  | zero => rfl
  | succ d ih =>
    rw [Nat.mul_succ,track_append,ih]
    simp [track,Nat.add_assoc]

private theorem next_lap (d e : Nat) : track (2*d+1) 1 e=(2,e+d+1) := by
  rw [track_append,laps]
  simp [track]

private theorem cycle_size (a e : Nat) : (track a 1 e).1≤2 := by
  by_cases bit : a%2=0
  · rw [show a=2*(a/2) by omega,laps]; exact Nat.le_succ 1
  · rw [show a=2*(a/2)+1 by omega,next_lap]; exact Nat.le_refl 2

private theorem pow_prefix (a b e : Nat) : track a (2^(a+b)) e=(2^b,e) := by
  induction a generalizing e with
  | zero => simp [track]
  | succ a ih =>
    rw [Nat.succ_add,Nat.pow_succ,track]
    simp only [show 2^(a+b)*2%2=0 by omega,↓reduceIte,show 2^(a+b)*2/2=2^(a+b) by omega,ih]

/-- Every supplied upper hit of a hard parent transfers with the same odd
    count and clock saving when a canonical return has upper clock H≤m. -/
theorem transfer_upper_hit {j m Y H G p : Nat} (row : m=11+162*j)
    (budget : H≤m) (upper : track H (3*Y) 0=(1,3))
    (given : track G (3*hardParent m) 0=(1,p)) :
    ∃ d, G=m+7+2*d ∧ p=3+d ∧ track (H+2*d) (3*Y) 0=(1,p) ∧ H+2*d+7≤G := by
  obtain ⟨_,_,_,checkpoint,finish⟩ := hard_source_data j
  rw [←row] at checkpoint finish
  have big : 2<2^(m-2) := Nat.lt_of_lt_of_le (by decide : 2<2^2)
    (Nat.pow_le_pow_right (by decide) (by omega))
  have nine : 9≤G := by
    apply Classical.byContradiction
    intro small
    have eq := track_append G (9-G) (3*hardParent m) 0
    rw [show G+(9-G)=9 by omega,checkpoint,given] at eq
    have bound := cycle_size (9-G) p
    have fst := congrArg Prod.fst eq
    change 2^(m-2)=(track (9-G) 1 p).1 at fst
    omega
  have first : m+7≤G := by
    apply Classical.byContradiction
    intro small
    have eq := track_append 9 (G-9) (3*hardParent m) 0
    rw [show 9+(G-9)=G by omega,given,checkpoint,
      show m-2=(G-9)+(m+7-G) by omega,pow_prefix] at eq
    have fst := congrArg Prod.fst eq
    change 1=2^(m+7-G) at fst
    have rise := Nat.pow_le_pow_right (by decide : 0<2) (show 1≤m+7-G by omega)
    omega
  let n := G-(m+7)
  have follow := track_append (m+7) n (3*hardParent m) 0
  rw [show m+7+n=G by dsimp only [n]; omega,given,finish] at follow
  have even : n%2=0 := by
    apply Classical.byContradiction
    intro odd
    rw [show n=2*(n/2)+1 by omega,next_lap] at follow
    have impossible : (1:Nat)=2 := congrArg Prod.fst follow
    omega
  let d := n/2
  have nform : n=2*d := by dsimp only [d]; omega
  rw [nform,laps] at follow
  have rank : p=3+d := congrArg Prod.snd follow
  have gform : G=m+7+2*d := by dsimp only [n] at nform; omega
  exact ⟨d,gform,rank,by rw [track_append,upper,laps,rank],by omega⟩

#print axioms transfer_upper_hit

end Collatz.Itinerary.ReturnDescent
