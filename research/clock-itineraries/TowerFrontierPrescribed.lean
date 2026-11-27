module

public import TowerFrontierLimit
public import MixedBarrier
import all TowerFrontierLimit
import all MixedBarrier
import all TernaryItinerary

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false

private theorem increasing (N v : Nat) (hv : 0<v) {i j : Nat} (lt : i<j) (hj : j≤N) :
    run i (2^N*v-1) < run j (2^N*v-1) := by
  let q := 2^(N-j)*v
  have hq : 0<q := Nat.mul_pos (Nat.two_pow_pos _) hv
  let d := j-i
  have hd : 0<d := by dsimp [d]; omega
  have jrep : j=i+d := by dsimp [d]; omega
  have nrep : 2^N*v=2^j*q := by
    dsimp [q]
    rw [←Nat.mul_assoc, ←Nat.pow_add, Nat.add_sub_of_le hj]
  have irep : 2^N*v=2^i*(2^d*q) := by rw [nrep,jrep,Nat.pow_add,Nat.mul_assoc]
  rw [show run i (2^N*v-1)=3^i*(2^d*q)-1 by
    rw [irep,odd_steps _ _ (Nat.mul_pos (Nat.two_pow_pos _) hq)]]
  rw [nrep,odd_steps _ _ hq,jrep,Nat.pow_add]
  have p := Nat.pow_lt_pow_left (by decide : 2<3) (show d≠0 by omega)
  have z := Nat.mul_lt_mul_of_pos_right p hq
  have e := Nat.mul_lt_mul_of_pos_left z (Nat.pow_pos (n:=i) (by decide : 0<3))
  have pos := Nat.mul_pos (Nat.pow_pos (n:=i) (by decide : 0<3)) (Nat.mul_pos (Nat.two_pow_pos d) hq)
  rw [Nat.mul_assoc]
  omega

private theorem disjoint_lanes (H v : Nat) (hv : 0<v) :
    let x := 2^(H+7)*v-1
    ∀ i ≤ H, ∀ j ≤ H, x ≤ run i x ∧ x < run j (3*x) ∧ run i x ≠ run j (3*x) := by
  let x := 2^(H+7)*v-1
  change ∀ i ≤ H, ∀ j ≤ H, x ≤ run i x ∧ x < run j (3*x) ∧ run i x ≠ run j (3*x)
  have grows {a b : Nat} (hab : a<b) (hb : b≤H+7) : run a x < run b x :=
    increasing _ _ hv hab hb
  have base {a : Nat} (ha : a≤H+7) : x ≤ run a x := by
    cases a with
    | zero => exact Nat.le_refl _
    | succ a => exact Nat.le_of_lt (grows (show 0<a+1 by omega) ha)
  have between {j l : Nat} (hl : l+1≤H+7)
      (h₁ : run l x < run j (3*x)) (h₂ : run j (3*x) < run (l+1) x)
      {i : Nat} (hi : i≤H) : x < run j (3*x) ∧ run i x ≠ run j (3*x) := by
    refine ⟨Nat.lt_of_le_of_lt (base (by omega)) h₁,?_⟩
    by_cases h : i≤l
    · rcases Nat.lt_or_eq_of_le h with lt|rfl
      · exact Nat.ne_of_lt (Nat.lt_trans (grows lt (by omega)) h₁)
      · exact Nat.ne_of_lt h₁
    · by_cases same : i=l+1
      · rw [same]; exact (Nat.ne_of_lt h₂).symm
      · exact (Nat.ne_of_lt (Nat.lt_trans h₂ (grows (show l+1<i by omega) (by omega)))).symm
  intro i hi j hj
  refine ⟨base (by omega),?_⟩
  let m := 2^(H+3)*v
  have hm : 0<m := Nat.mul_pos (Nat.two_pow_pos _) hv
  have small : x=16*m-1 := by
    dsimp [x,m]
    rw [show H+7=(H+3)+4 by omega, Nat.pow_add,show 2^4=16 by decide]
    congr 1; ac_rfl
  have four (a : Nat) (ha : a≤4) : run a x = 3^a*(2^(4-a)*m)-1 := by
    have rep : 16*m=2^a*(2^(4-a)*m) := by
      rw [←Nat.mul_assoc (2^a) (2^(4-a)) m, ←Nat.pow_add,Nat.add_sub_of_le ha]
    rw [small,rep,odd_steps _ _ (Nat.mul_pos (Nat.two_pow_pos _) hm)]
  have right := first_three (2*m) (by omega)
  have sx : x=8*(2*m)-1 := by rw [small]; omega
  cases j with
  | zero =>
    apply between (l:=2) (by omega) _ _ hi
    · rw [four 2 (by decide),run,small]; change 9*(4*m)-1<3*(16*m-1); omega
    · rw [four 3 (by decide),run,small]; change 3*(16*m-1)<27*(2*m)-1; omega
  | succ j =>
    cases j with
    | zero =>
      have rr : run 1 (3*x)=36*(2*m)-4 := by rw [sx]; exact right.2.2.1
      apply between (l:=3) (by omega) _ _ hi
      · rw [four 3 (by decide),rr]; change 27*(2*m)-1<36*(2*m)-4; omega
      · rw [four 4 (by decide),rr]; change 36*(2*m)-4<81*(1*m)-1; omega
    | succ j =>
      cases j with
      | zero =>
        have rr : run 2 (3*x)=18*(2*m)-2 := by simp only [sx,run,right.2.2.1,right.2.2.2.1]
        apply between (l:=1) (by omega) _ _ hi
        · rw [four 1 (by decide),rr]; change 3*(8*m)-1<18*(2*m)-2; omega
        · rw [four 2 (by decide),rr]; change 18*(2*m)-2<9*(4*m)-1; omega
      | succ j =>
        let u := 2^((H+4)-j)*v
        have hu : 0<u := Nat.mul_pos (Nat.two_pow_pos _) hv
        have nrep : 2^(H+7)*v=8*(2^j*u) := by
          dsimp [u]
          rw [show H+7=(j+((H+4)-j))+3 by omega,Nat.pow_add,Nat.pow_add,show 2^3=8 by decide]
          ac_rfl
        have first : run j x=8*(3^j*u)-1 := by
          have eq : x=2^j*(8*u)-1 := by dsimp [x]; rw [nrep]; congr 1; ac_rfl
          rw [eq,odd_steps _ _ (by omega)]; congr 1; ac_rfl
        have next : run (j+1) x=12*(3^j*u)-1 := by
          have eq : x=2^(j+1)*(4*u)-1 := by dsimp [x]; rw [nrep,Nat.pow_succ]; congr 1; grind
          rw [eq,odd_steps _ _ (by omega),Nat.pow_succ]; congr 1; grind
        have init := first_three (2^j*u) (Nat.mul_pos (Nat.two_pow_pos _) hu)
        have rr : run (j+3) (3*x)=9*(3^j*u)-1 := by
          rw [Nat.add_comm j 3, run_add]
          have eq : run 3 (3*x)=9*(2^j*u)-1 := by
            dsimp [x]; rw [nrep]; simp only [run,init.2.2.1,init.2.2.2.1,init.2.2.2.2]
          rw [eq,show 9*(2^j*u)=2^j*(9*u) by ac_rfl,odd_steps _ _ (by omega)]
          congr 1; ac_rfl
        have pos := Nat.mul_pos (Nat.pow_pos (n:=j) (by decide : 0<3)) hu
        apply between (l:=j) (by omega) _ _ hi
        · rw [first,rr]; omega
        · rw [next,rr]; omega

/-- The bad pair may be placed at any prescribed adjacent ranks. Both rows
    avoid descent below their starting lower rank, even when their clocks
    can be chosen independently within the finite horizon. -/
theorem prescribed_rank_obstruction (r H L : Nat) :
    ∃ w > L, w%6=1 ∧ ∀ i ≤ H, ∀ j ≤ H,
      3^r*w ≤ run i (3^r*w) ∧ 3^r*w < run j (3^(r+1)*w) ∧
      run i (3^r*w) ≠ run j (3^(r+1)*w) := by
  let M := 3^(r+1)
  obtain ⟨t,ht⟩ := MixedBarrier.three_odd (r+1)
  obtain ⟨v,z,eq⟩ := MixedBarrier.inverse_two (H+7) M t ht
  let q := 2^(H+7)
  let A := 3^r
  have ma : M=3*A := by dsimp [M,A]; rw [Nat.pow_succ,Nat.mul_comm]
  have ep : q*v=1+M*z := eq
  let u := v*(A+1)+M*(L+1)
  let D := z*(A+1)+q*(L+1)
  let w := 1+3*D
  have identity : q*u = A*w+1 := by
    dsimp [u,w,D]
    rw [Nat.mul_add,←Nat.mul_assoc,ep,ma]
    grind
  have hq : 0<q := Nat.two_pow_pos _
  have hu : 0<u := by
    have hp := Nat.mul_pos (Nat.pow_pos (n:=r+1) (by decide : 0<3)) (show 0<L+1 by omega)
    dsimp [u,M] at *; omega
  have size : L+1≤q*(L+1) := Nat.le_mul_of_pos_left _ hq
  have oddw : w%2=1 := by
    have base : q=2*2^(H+6) := by dsimp [q]; rw [Nat.pow_succ 2 (H+6)]; ac_rfl
    have even : q*u%2=0 := by rw [base]; simp [Nat.mul_mod]
    rw [identity,Nat.add_mod,Nat.mul_mod,show A%2=1 by simp [A,Nat.pow_mod]] at even
    omega
  have mod3 : w%3=1 := by dsimp [w]; omega
  refine ⟨w,by dsimp [w,D]; omega,by omega,?_⟩
  have g := disjoint_lanes H u hu
  have x : 2^(H+7)*u-1=3^r*w := by change q*u-1=A*w; omega
  dsimp only at g
  rw [x] at g
  rw [show 3^(r+1)*w=3*(3^r*w) by rw [Nat.pow_succ]; ac_rfl]
  exact g

#print axioms prescribed_rank_obstruction

end Collatz.Itinerary.TowerFrontier
