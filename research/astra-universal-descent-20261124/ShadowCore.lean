import Std

/-!
Positive-input ordinary shortcut dynamics and a guarded smaller partner at every ternary height.
The supplementary lower bounds on competing diagrams are in shadow.md.
-/
namespace ShadowCore

def oddBit (x : Int) : Bool := x % 2 == 1
def step (x : Int) : Int :=
  if oddBit x then (3*x+1)/2 else x/2

def run : Nat → Int → Int
  | 0, x => x
  | t+1, x => step (run t x)

theorem step_even (x : Int) : step (2*x) = x := by
  simp [step, oddBit]

theorem step_odd (x : Int) : step (2*x-1) = 3*x-1 := by
  have h : (2*x-1)%2 = 1 := by omega
  simp only [step, oddBit, h, beq_self_eq_true, ite_true]
  omega

theorem run_add (s t : Nat) (x : Int) : run (s+t) x = run t (run s x) := by
  induction t with
  | zero => rfl
  | succ t ih => exact congrArg step ih

theorem run_first (t : Nat) (x : Int) : run (t+1) x = run t (step x) := by
  rw [Nat.add_comm, run_add]
  rfl

theorem ones (d : Nat) (z : Int) :
    run d (2^d*z-1) = 3^d*z-1 := by
  induction d generalizing z with
  | zero => simp [run]
  | succ d ih =>
    rw [run_first, Int.pow_succ']
    rw [Int.mul_assoc, step_odd]
    have he : 3*(2^d*z) = 2^d*(3*z) := by ac_rfl
    rw [he, ih, Int.pow_succ']
    ac_rfl

theorem pair (q : Int) : run 2 (1+4*q) = 1+3*q := by
  change step (step (1+4*q)) = _
  have h : 1+4*q = 2*(1+2*q)-1 := by omega
  rw [h, step_odd]
  have h' : 3*(1+2*q)-1 = 2*(1+3*q) := by omega
  rw [h', step_even]

theorem pairs (j : Nat) (u : Int) :
    run (2*j) (1+4^j*u) = 1+3^j*u := by
  induction j generalizing u with
  | zero => simp [run]
  | succ j ih =>
    have hj : 2*(j+1) = 2+2*j := by omega
    rw [hj, run_add, Int.pow_succ', Int.mul_assoc, pair]
    have he : 3*(4^j*u) = 4^j*(3*u) := by ac_rfl
    rw [he, ih, Int.pow_succ']
    ac_rfl

theorem guarded_meet (h d : Nat) (u z n : Int)
    (hn : n = 3^h*u) (ho : n%2 = 1)
    (hz : 3^d*z = 1+2*4^h*u) :
    run (d+2*(h+1)+1) (2^(d+1)*z-1) = step n := by
  rw [run, run_add, Int.pow_succ, Int.mul_assoc, ones]
  have he : 3^d*(2*z)-1 = 1+4^(h+1)*u := by
    have hm : 3^d*(2*z) = 2*(3^d*z) := by ac_rfl
    rw [hm, hz, Int.pow_succ']
    simp only [Int.mul_assoc]
    omega
  rw [he, pairs, Int.pow_succ', Int.mul_assoc, ← hn]
  have heven : (1+3*n)%2 = 0 := by omega
  simp only [step, oddBit, heven, ho, beq_self_eq_true]
  simp
  omega

private theorem powers (h : Nat) :
    (2:Int)^(h+5)*2*4^h < 3^(h+4)*3^h := by
  induction h with
  | zero => decide
  | succ h ih =>
    have h5 : h+1+5 = (h+5)+1 := by omega
    have h4 : h+1+4 = (h+4)+1 := by omega
    rw [h5, h4, Int.pow_succ', Int.pow_succ' 4, Int.pow_succ' 3 (h+4), Int.pow_succ' 3 h]
    have hl : 2*2^(h+5)*2*(4*4^h) = (8:Int)*(2^(h+5)*2*4^h) := by
      change (2:Int)*_ *2*(4*_) = (2*4)*(_*2*_)
      ac_rfl
    have hr : (3:Int)*3^(h+4)*(3*3^h) = 9*(3^(h+4)*3^h) := by
      change (3:Int)*_*(3*_) = (3*3)*(_*_)
      ac_rfl
    rw [hl, hr]
    have hp : 0 < (3:Int)^(h+4)*3^h := Int.mul_pos (Int.pow_pos (by decide)) (Int.pow_pos (by decide))
    omega

private theorem intercept (h : Nat) : (2:Int)^(h+5) < 3^(h+4) := by
  induction h with
  | zero => decide
  | succ h ih =>
    have h5 : h+1+5 = h+5+1 := by omega
    have h4 : h+1+4 = h+4+1 := by omega
    rw [h5, h4, Int.pow_succ', Int.pow_succ' 3]
    have hp : 0 < (3:Int)^(h+4) := Int.pow_pos (by decide)
    omega

theorem guarded_smaller (h : Nat) (u z : Int) (hu : 0 < u)
    (hz : 3^(h+4)*z = 1+2*4^h*u) :
    2^(h+5)*z-1 < 3^h*u := by
  have hi := intercept h
  have hp := Int.mul_lt_mul_of_pos_right (powers h) hu
  have he : (3:Int)^(h+4)*(2^(h+5)*z) =
      2^(h+5) + (2^(h+5)*2*4^h)*u := by
    calc
      _ = 2^(h+5)*(3^(h+4)*z) := by ac_rfl
      _ = _ := by rw [hz, Int.mul_add, Int.mul_one]; ac_rfl
  have hr : (3:Int)^(h+4)*(3^h*u+1) = (3^(h+4)*3^h)*u + 3^(h+4) := by
    rw [Int.mul_add, Int.mul_one, Int.mul_assoc]
  have hh : (3:Int)^(h+4)*(2^(h+5)*z) < 3^(h+4)*(3^h*u+1) := by
    rw [he, hr]
    omega
  have hpos : 0 < (3:Int)^(h+4) := Int.pow_pos (by decide)
  have hh' := (Int.mul_lt_mul_left hpos).mp hh
  omega

theorem guarded_certificate (h : Nat) (u : Int) (hu : 0 < u)
    (ho : (3^h*u)%2 = 1) (hg : (3:Int)^(h+4) ∣ 1+2*4^h*u) :
    ∃ m : Int, 0 < m ∧ m < 3^h*u ∧ run (3*h+7) m = step (3^h*u) := by
  obtain ⟨z, hz⟩ := hg
  have h4 : 0 < (4:Int)^h := Int.pow_pos (by decide)
  have h4u : 0 < (4:Int)^h*u := Int.mul_pos h4 hu
  have hzpos : 0 < z := by
    apply Int.pos_of_mul_pos_right (a := (3:Int)^(h+4))
    · rw [← hz]
      have he : 2*(4^h*u) = (2:Int)*4^h*u := by ac_rfl
      omega
    · exact Int.pow_pos (by decide)
  have hm : 0 < (2:Int)^(h+5)*z-1 := by
    rw [show h+5=(h+4)+1 by omega, Int.pow_succ']
    have hp : 0 < (2:Int)^(h+4)*z := Int.mul_pos (Int.pow_pos (by decide)) hzpos
    rw [Int.mul_assoc]
    omega
  refine ⟨2^(h+5)*z-1, hm, guarded_smaller h u z hu hz.symm, ?_⟩
  have ht : 3*h+7=(h+4)+2*(h+1)+1 := by omega
  rw [ht]
  exact guarded_meet h (h+4) u z (3^h*u) rfl ho hz.symm

#print axioms step_even
#print axioms step_odd
#print axioms run_add
#print axioms run_first
#print axioms ones
#print axioms pair
#print axioms pairs
#print axioms guarded_certificate
#print axioms guarded_meet
#print axioms guarded_smaller
end ShadowCore
