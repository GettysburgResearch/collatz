import CappedMass
import Mathlib.Data.Finset.Max

/-! An actual-clock coefficient of the finite six-gap multiplier polynomial.
All counts include their common 64^grade scaling. -/
set_option autoImplicit false
set_option warningAsError true
namespace CappedClock
open CappedMass Finset

def coefficient : ℕ → ℕ → ℕ → ℕ
  | 0,m,y => if m=0 ∧ y%3≠0 then 1 else 0
  | d+1,m,y =>
      ∑i∈range 6, if allowed (i+1) y ∧ i+1≤m then
        3*2^(6-(i+1))*coefficient d (m-(i+1)) (2^(i+1)*y/3) else 0

private theorem outside (d m y : ℕ) (high : 6*d<m) : coefficient d m y=0 := by
  induction d generalizing m y with
  | zero => simp [coefficient,show m≠0 by omega]
  | succ d ih =>
    unfold coefficient
    apply sum_eq_zero
    intro i hi
    have le:=mem_range.mp hi
    split
    · rw [ih _ _ (by omega),Nat.mul_zero]
    · rfl

private theorem shifted (d y e : ℕ) (ep : e≤6) :
    (∑m∈range (6*(d+1)+1), if e≤m then coefficient d (m-e) y else 0)=
    ∑m∈range (6*d+1), coefficient d m y := by
  rw [show 6*(d+1)+1=e+((6*d+1)+(6-e)) by omega, sum_range_add]
  have empty : (∑m∈range e, if e≤m then coefficient d (m-e) y else 0)=0 := by
    apply sum_eq_zero
    intro m hm
    simp [show ¬e≤m by have lt:=mem_range.mp hm; omega]
  rw [empty,zero_add]
  simp only [Nat.le_add_right,ite_true,Nat.add_sub_cancel_left]
  rw [sum_range_add]
  have beyond : (∑i∈range (6-e),coefficient d (6*d+1+i) y)=0 := by
    apply sum_eq_zero
    intro i _
    apply outside
    omega
  rw [beyond,add_zero]

theorem complete (d y : ℕ) :
    (∑m∈range (6*d+1),coefficient d m y)=numerator d y := by
  induction d generalizing y with
  | zero =>
    by_cases u:y%3=0 <;> simp [coefficient,numerator,u]
  | succ d ih =>
    simp only [coefficient,numerator,op,Finset.sum_comm (s:=range (6*(d+1)+1)) (t:=range 6)]
    apply sum_congr rfl
    intro i hi
    have ep:=mem_range.mp hi
    by_cases ok:allowed (i+1) y
    · simp only [ok,true_and,ite_true]
      rw [←ih (2^(i+1)*y/3),←shifted d (2^(i+1)*y/3) (i+1) (by omega),mul_sum]
      apply sum_congr rfl
      intro m _
      split <;> simp
    · simp [ok]

/-- Some physical gap-clock row has the indicated positive multiplier
numerator at every positive unit target. -/
theorem some_clock (d y : ℕ) (unit : y%3≠0) :
    ∃m≤6*d, 52*48^d≤1000*(6*d+1)*coefficient d m y := by
  obtain ⟨m,hm,big⟩:=exists_max_image (range (6*d+1)) (fun k => coefficient d k y)
    (show (range (6*d+1)).Nonempty from ⟨0,mem_range.mpr (by omega)⟩)
  have total : numerator d y≤(6*d+1)*coefficient d m y := by
    rw [←complete]
    calc
      _ ≤ ∑_∈range (6*d+1),coefficient d m y := sum_le_sum big
      _ = _ := by simp
  exact ⟨m,by have mm:=mem_range.mp hm; omega,
    (unit_mass d y unit).trans (by simpa only [Nat.mul_assoc] using Nat.mul_le_mul_left 1000 total)⟩

#print axioms complete
#print axioms some_clock
end CappedClock
