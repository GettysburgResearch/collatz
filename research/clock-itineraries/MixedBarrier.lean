module

public import DescentClocks
public import SynchronousShadow
import all FixedGate
import all TernaryItinerary

public section
namespace Collatz.Itinerary.MixedBarrier
open Sparse
set_option autoImplicit false

private theorem three_odd (n : Nat) : ∃ t, 3^n=2*t+1 := by
  induction n with
  | zero => exact ⟨0,rfl⟩
  | succ n ih =>
    obtain ⟨t,ht⟩ := ih
    exact ⟨3*t+1,by rw [Nat.pow_succ,ht]; omega⟩

private theorem inverse_two (H M t : Nat) (odd : M=2*t+1) :
    ∃ v z, 2^H*v=1+M*z := by
  induction H with
  | zero => exact ⟨1,0,by simp⟩
  | succ H ih =>
    obtain ⟨v,z,eq⟩ := ih
    refine ⟨(t+1)*v,z+1+M*z,?_⟩
    have h : 2*(t+1)=M+1 := by omega
    rw [Nat.pow_succ,show 2^H*2*((t+1)*v)=(2^H*v)*(2*(t+1)) by ac_rfl,eq,h]
    grind

private theorem unit_limb (k w : Nat) (hw : 0<w) :
    Path (List.replicate k 1) (2*(2^k*w)-1) (2*(3^k*w)-1) := by
  induction k generalizing w with
  | zero => simpa using Path.nil (2*w-1)
  | succ k ih =>
    have base := Nat.mul_pos (Nat.two_pow_pos k) hw
    have big : 2^(k+1)*w=2*(2^k*w) := by rw [Nat.pow_succ]; ac_rfl
    have next : 2^k*(3*w)=3*(2^k*w) := by ac_rfl
    have edge : Gap 1 (2*(2^(k+1)*w)-1) (2*(2^k*(3*w))-1) := by
      rw [big,next]
      refine ⟨by decide,by omega,by omega,?_⟩
      change 2*(2*(3*(2^k*w))-1)=3*(2*(2*(2^k*w))-1)+1
      omega
    have tail := ih (3*w) (by omega)
    have far : 3^(k+1)*w=3^k*(3*w) := by rw [Nat.pow_succ]; ac_rfl
    rw [List.replicate_succ,far]
    exact .cons edge tail

private theorem physical {es : List Nat} {x q : Nat} (p : Path es x q) :
    run es.sum x=q := by
  induction p with
  | nil => rfl
  | cons g _ ih => rw [List.sum_cons,run_add,g.follow,ih]

private theorem sum_ones (k : Nat) : (List.replicate k 1 : List Nat).sum=k := by
  induction k with
  | zero => rfl
  | succ k ih => rw [List.replicate_succ,List.sum_cons,ih]; omega

private theorem all_prefixes {H a q : Nat} (p : Path (List.replicate H 1) a q) :
    ∀ k, k≤H → FixedGate.elapsed k a=k ∧ a≤FixedGate.after k a := by
  induction H generalizing a q with
  | zero =>
    intro k hk
    have h : k=0 := by omega
    subst k; exact ⟨rfl,Nat.le_refl _⟩
  | succ H ih =>
    rw [List.replicate_succ] at p
    cases p with
    | @cons _ y _ _ _ g tail =>
      have step := FixedGate.gap_next g
      have upper : a≤y := by have h := g.eqn; change 2*y=3*a+1 at h; omega
      intro k hk
      cases k with
      | zero => exact ⟨rfl,Nat.le_refl _⟩
      | succ k =>
        have ⟨ck,up⟩ := ih tail k (by omega)
        simp only [FixedGate.elapsed,FixedGate.after,step,ck]
        exact ⟨by omega,Nat.le_trans upper up⟩

/-- At one known converging gate an arbitrarily long increasing forward limb
and an arbitrarily deep obstruction to smaller incoming sources hold together. -/
theorem converging_mixed_barrier (H A : Nat) :
    ∃ a q e z, A<a ∧ 2<a ∧ a%2=1 ∧ a%3=1 ∧ a=1+3^(H+1)*z ∧
      Path (List.replicate H 1) a q ∧ Gap e q 1 ∧ run (H+e) a=1 ∧
      (∀ es x, es≠[] → es.length≤H → Path es x a → a<x) ∧
      ∀ k, k≤H → FixedGate.elapsed k a=k ∧ a≤FixedGate.after k a ∧
        (2^(FixedGate.elapsed k a))^6≤(k+1)*(3^k)^6 := by
  let M := 3^(H+1)
  have mp : 0<M := Nat.pow_pos (by decide : 0<3)
  obtain ⟨t,mt⟩ := three_odd (H+1)
  obtain ⟨v,z,inverse⟩ := inverse_two H M t mt
  let w := v+M*(A+2)
  have ge := Nat.mul_le_mul_right (A+2) (show 1≤M by omega)
  have wp : A+2≤w := by dsimp [w]; omega
  let z₀ := z+2^H*(A+2)
  have wt : 2^H*w=1+M*z₀ := by
    dsimp [w,z₀]; rw [Nat.mul_add,inverse,Nat.mul_add]; grind
  let a₀ := 2*(2^H*w)-1
  let q₀ := 2*(3^H*w)-1
  have pw := Nat.mul_le_mul_right w (show 1≤2^H from Nat.two_pow_pos _)
  have qw := Nat.mul_pos (Nat.pow_pos (n:=H) (by decide : 0<3)) (show 0<w by omega)
  have ao : a₀%2=1 := by dsimp [a₀]; omega
  have qo : q₀%2=1 := by dsimp [q₀]; omega
  have start : a₀=1+M*(2*z₀) := by
    dsimp [a₀]; rw [wt]; grind
  obtain ⟨e,d,_,_,exit,shadow⟩ := Shadow.simultaneous_shadow qo (t:=1)
    (by decide) (by decide) H H (H+1)
  let a := a₀+2*(2^H*(M*d))
  let q := q₀+2*(3^(H+(H+1))*d)
  let D := 2*z₀+2*(2^H*d)
  have cls : a=1+M*D := by dsimp [a,D]; rw [start,Nat.mul_add]; grind
  have unit : a%3=1 := by
    have mult : M*D=3*(3^H*D) := by dsimp [M]; rw [Nat.pow_succ]; ac_rfl
    rw [cls,mult]; omega
  have high : A<a₀ ∧ 2<a₀ := by dsimp [a₀]; omega
  have aHigh : A<a ∧ 2<a := by dsimp [a]; omega
  have aOdd : a%2=1 := by dsimp [a]; omega
  have chain : Path (List.replicate H 1) a q :=
    shadow _ a₀ (by simp) (sum_ones H) (unit_limb H w (by omega))
  have reach := physical chain
  rw [sum_ones] at reach
  refine ⟨a,q,e,D,aHigh.1,aHigh.2,aOdd,unit,cls,chain,exit,?_,?_,?_⟩
  · rw [run_add,reach,exit.follow]
  · intro es x nonempty depth p
    obtain ⟨f,hf⟩ := Nat.pow_dvd_pow 3 (show es.length≤H+1 by omega)
    have pos : 1<3^es.length := by
      cases es with
      | nil => simp at nonempty
      | cons y ys =>
        simp only [List.length_cons,Nat.pow_succ]
        have h := Nat.pow_pos (n:=ys.length) (by decide : 0<3)
        omega
    have shape : a=1+3^es.length*(f*D) := by change a=1+_ ; rw [cls]; dsimp [M]; rw [hf]; ac_rfl
    have modClass : a%3^es.length=1 := by
      rw [shape,Nat.add_mul_mod_self_left,Nat.mod_eq_of_lt pos]
    exact DescentClocks.no_descent_at_one_cylinder p nonempty (by omega) aOdd modClass
  · intro k hk
    obtain ⟨clock,order⟩ := all_prefixes chain k hk
    refine ⟨clock,order,?_⟩
    rw [clock]
    have le := Nat.pow_le_pow_left (Nat.pow_le_pow_left (by decide : 2≤3) k) 6
    have last := Nat.mul_le_mul_right ((3^k)^6) (show 1≤k+1 by omega)
    simpa using Nat.le_trans le (by simpa using last)

#print axioms converging_mixed_barrier
end Collatz.Itinerary.MixedBarrier
