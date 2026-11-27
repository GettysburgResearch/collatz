module

public import SynchronousShadow
public import TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.HourTower

set_option autoImplicit false

private theorem positive {x : Nat} (hx : 0<x) (h : Nat) : 0<run h x := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih =>
    apply ih
    unfold step
    split <;> omega

private theorem cycle_lift (k t : Nat) :
    run (2*k) (1+2^(2*k)*t) = 1+3^k*t := by
  induction k generalizing t with
  | zero => simp [run]
  | succ k ih =>
    have len : 2*(k+1)=2+2*k := by omega
    have scale : 2^(2*(k+1))*t=4*(2^(2*k)*t) := by
      rw [len,Nat.pow_add,show 2^2=4 by decide,Nat.mul_assoc]
    have two (u : Nat) : run 2 (1+4*u)=1+3*u := by
      have first : step (1+4*u)=2+6*u := by unfold step; split <;> omega
      change step (step (1+4*u))=1+3*u
      rw [first]; unfold step; split <;> omega
    rw [scale,len,run_add,two,show 3*(2^(2*k)*t)=2^(2*k)*(3*t) by ac_rfl,ih,Nat.pow_succ]
    rw [Nat.mul_assoc]

private theorem thicken {r w j : Nat} (large : 1<w) (hit : run j (3^r*w)=1) (K : Nat) :
    ∃ m≥j, run m (3^r*w)=1 ∧
      ∀ t, run m (3^r*(w+2^m*3^K*t)) < w+2^m*3^K*t := by
  let S := TowerFrontier.track j (3^r*w) r
  have first : S.1=1 := by simpa [S,hit] using (TowerFrontier.affine j (3^r*w) r 0).symm
  let E := S.2
  let n := 4*E
  let m := j+2*n
  have shrink : 3^(n+E)≤2^(2*n) := by
    have e5 : n+E=5*E := by dsimp [n]; omega
    have e8 : 2*n=8*E := by dsimp [n]; omega
    rw [e5,e8,Nat.pow_mul,Nat.pow_mul]
    exact Nat.pow_le_pow_left (by decide : 3^5≤2^8) _
  have exact_run (t : Nat) : run m (3^r*(w+2^m*3^K*t))=1+3^(n+E)*3^K*t := by
    let u := 2^(2*n)*3^K*t
    have start : 3^r*(w+2^m*3^K*t)=3^r*w+2^j*3^r*u := by
      dsimp [m,u]; rw [Nat.mul_add,Nat.pow_add]; ac_rfl
    rw [start,show m=j+2*n by rfl,run_add,TowerFrontier.affine]
    change run (2*n) (S.1+3^E*u)=_
    rw [first,show 3^E*u=2^(2*n)*(3^E*3^K*t) by dsimp [u]; ac_rfl,cycle_lift,Nat.pow_add]
    ac_rfl
  refine ⟨m,by dsimp [m]; omega,by simpa using exact_run 0,?_⟩
  intro t
  rw [exact_run]
  have clock : 2^(2*n)≤2^m := Nat.pow_le_pow_right (by decide)
    (show 2*n≤m by dsimp [m]; omega)
  exact Nat.add_lt_add_of_lt_of_le large (Nat.mul_le_mul_right _
    (Nat.mul_le_mul_right _ (Nat.le_trans shrink clock)))

/-- Every prescribed positive binary/ternary base progression contains a
    refinement with uniform descent below each lift at the
    supplied rank. The center actually reaches 1 at the same clock. -/
theorem dense_capture (r H K a L : Nat) (pos : 0<a) :
    ∃ w>L, ∃ d m, w=a+2^H*3^K*d ∧ H≤m ∧ run m (3^r*w)=1 ∧
      ∀ t, run m (3^r*(w+2^m*3^K*t)) < w+2^m*3^K*t := by
  let v := a+2^H*3^K*(L+2)
  have off : L+2≤2^H*3^K*(L+2) := Nat.le_mul_of_pos_left _
    (Nat.mul_pos (Nat.two_pow_pos _) (Nat.pow_pos (by decide)))
  have vhigh : L+2≤v := by dsimp [v]; omega
  have xp := Nat.mul_pos (Nat.pow_pos (n:=r) (by decide : 0<3)) (show 0<v by omega)
  obtain ⟨j,q,hq,odd⟩ := split_twos _ (positive xp H)
  let J := H+j
  have reached : run J (3^r*v)=q := by rw [show J=H+j by rfl,run_add,hq,halve]
  let S := TowerFrontier.track J (3^r*v) r
  have endpt : S.1=q := by simpa [S,reached] using (TowerFrontier.affine J (3^r*v) r 0).symm
  obtain ⟨e,c,_,_,edge⟩ := Shadow.one_gap_cylinder (t:=1) odd (by decide) (by decide) (S.2+K)
  let delta := 2*3^K*c
  let w := v+2^J*delta
  have large : v≤w := Nat.le_add_right _ _
  have hit : run (J+e) (3^r*w)=1 := by
    have initial : 3^r*w=3^r*v+2^J*3^r*delta := by dsimp [w]; rw [Nat.mul_add]; ac_rfl
    rw [initial,run_add,TowerFrontier.affine]
    change run e (S.1+3^S.2*delta)=1
    rw [endpt,show 3^S.2*delta=2*(3^(S.2+K)*c) by dsimp [delta]; rw [Nat.pow_add]; ac_rfl,edge.follow]
  obtain ⟨m,mhi,center,all⟩ := thicken (by omega : 1<w) hit K
  refine ⟨w,by omega,L+2+2^j*(2*c),m,?_,by dsimp [J] at mhi; omega,center,all⟩
  dsimp [w,v,delta,J]
  simp only [Nat.pow_add,Nat.mul_add]
  ac_rfl

/-- All prescribed ranks are screened at their original, unshifted positions
    on a single subprogression of any supplied class. The clock may depend
    on the rank and is uniform on the entire subprogression. -/
theorem finite_dense_capture (ranks : List Nat) (H K a L : Nat) (pos : 0<a) :
    ∃ w>L, ∃ d m, w=a+2^H*3^K*d ∧ H≤m ∧
      ∀ r ∈ ranks, ∃ h≤m, ∀ t, run h (3^r*(w+2^m*3^K*t)) < w+2^m*3^K*t := by
  induction ranks generalizing a H with
  | nil =>
    refine ⟨a+2^H*3^K*(L+1),?_,L+1,H,rfl,by omega,by simp⟩
    have := Nat.le_mul_of_pos_left (L+1) (Nat.mul_pos (Nat.two_pow_pos H)
      (Nat.pow_pos (n:=K) (by decide : 0<3)))
    omega
  | cons r rest ih =>
    obtain ⟨v,vhi,d₁,n,vrep,hn,_,first⟩ := dense_capture r H K a L pos
    obtain ⟨w,whi,d₂,m,wrep,hm,tail⟩ := ih n v (by omega)
    have splitN : 2^n=2^H*2^(n-H) := by rw [←Nat.pow_add,Nat.add_sub_of_le hn]
    have splitM : 2^m=2^n*2^(m-n) := by rw [←Nat.pow_add,Nat.add_sub_of_le hm]
    refine ⟨w,whi,d₁+2^(n-H)*d₂,m,?_,by omega,?_⟩
    · rw [wrep,vrep,splitN,Nat.mul_add]; ac_rfl
    · intro s sel
      rcases List.mem_cons.mp sel with eq|mem
      · subst s
        refine ⟨n,hm,?_⟩
        intro t
        have rr : w+2^m*3^K*t=v+2^n*3^K*(d₂+2^(m-n)*t) := by
          rw [wrep,splitM,Nat.mul_add]; ac_rfl
        rw [rr]; exact first _
      · exact tail s mem

#print axioms dense_capture
#print axioms finite_dense_capture

end Collatz.Itinerary.HourTower
