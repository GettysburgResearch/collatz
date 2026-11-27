import AsynchronousGuard
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith

/-! Unit-preserving inverse steps with bounded extra clock cost on the actual
shortcut Collatz map. The quantitative interval statements using the
irrational rotation and the fixed-total inverse floor are in the note. -/
set_option autoImplicit false
set_option warningAsError true

namespace InverseSpreading
open CoreBranching PeakRigidity

def unitOdd (n : ℕ) : Prop := n%2=1 ∧ n%3≠0

theorem run_doubling_lift (k n : ℕ) : run k (2^k*n)=n := by
  induction k with
  | zero => simp [run]
  | succ i ih =>
    rw [show 2^(i+1)*n=2*(2^i*n) by ring,run,step_double,ih]

private theorem product_unit (E y : ℕ) (hy : y%3≠0) : (2^E*y)%3≠0 := by
  intro h
  have d := Nat.dvd_of_mod_eq_zero h
  rcases Nat.prime_three.dvd_mul.mp d with pow|target
  · exact (by decide : ¬3∣2) (Nat.prime_three.dvd_of_dvd_pow pow)
  · exact hy (Nat.mod_eq_zero_of_dvd target)

private theorem residue_choice (p : ℕ) (hp : p%3≠0) :
    ∃ r : ℕ, r≤3 ∧ ((2^r*p)%9=4 ∨ (2^r*p)%9=7) := by
  have hr : p%9=1 ∨ p%9=2 ∨ p%9=4 ∨ p%9=5 ∨ p%9=7 ∨ p%9=8 := by omega
  rcases hr with h|h|h|h|h|h
  · exact ⟨2,by decide,Or.inl (by rw [Nat.mul_mod,h]; decide)⟩
  · exact ⟨1,by decide,Or.inl (by rw [Nat.mul_mod,h]; decide)⟩
  · exact ⟨0,by decide,Or.inl (by simpa using h)⟩
  · exact ⟨3,by decide,Or.inl (by rw [Nat.mul_mod,h]; decide)⟩
  · exact ⟨0,by decide,Or.inr (by simpa using h)⟩
  · exact ⟨1,by decide,Or.inr (by rw [Nat.mul_mod,h]; decide)⟩

theorem inverse_run {x y e : ℕ} (evenClock : 0<e) (odd : x%2=1)
    (edge : 3*x+1=2^e*y) : run e x=y := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have twice : 2^(k+1)*y=2*(2^k*y) := by ring
  rw [run]
  have first : step x=2^k*y := by
    rw [step,ite_eq_right (by omega),edge,twice]; omega
  rw [first,run_doubling_lift]

private theorem join_grade (a b n : ℕ) :
    grade (a+b) n=grade a n+grade b (run a n) := by
  induction b with
  | zero => simp [grade]
  | succ b ih => rw [Nat.add_succ,grade,ih,run_add,grade,Nat.add_assoc]

theorem grade_doubling_lift (k n : ℕ) : grade k (2^k*n)=0 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [show k+1=1+k by omega,join_grade]
    have form : 2^(1+k)*n=2*(2^k*n) := by rw [pow_add]; ring
    simp [form,grade,run,step_double,ih]

private theorem inverse_grade {x y e : ℕ} (evenClock : 0<e) (odd : x%2=1)
    (edge : 3*x+1=2^e*y) : grade e x=1 := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have twice : 2^(k+1)*y=2*(2^k*y) := by ring
  have first : step x=2^k*y := by
    rw [step,ite_eq_right (by omega),edge,twice]; omega
  rw [show k.succ=1+k by omega,join_grade]
  simp [grade,run,odd,first,grade_doubling_lift]

/-- Starting from any positive valuation cutoff, at most three further
doublings suffice to choose a positive odd unit with this one-gap future. -/
theorem bounded_inverse {y E : ℕ} (hy : unitOdd y) (start : 0<E) :
    ∃ e x : ℕ, E≤e ∧ e≤E+3 ∧ unitOdd x ∧ 3*x+1=2^e*y ∧ run e x=y := by
  obtain ⟨r,hr,hmod⟩ := residue_choice (2^E*y) (product_unit E y hy.2)
  let e := E+r
  have expand : 2^r*(2^E*y)=2^e*y := by dsimp [e]; rw [pow_add]; ring
  rw [expand] at hmod
  let x := (2^e*y-1)/3
  have he : 0<e := by dsimp [e]; omega
  have eqn : 3*x+1=2^e*y := by dsimp [x]; omega
  have hx3 : x%3≠0 := by dsimp [x]; omega
  obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
  have even : 2^e*y=2*(2^k*y) := by rw [hk,pow_succ]; ring
  have hx2 : x%2=1 := by omega
  exact ⟨e,x,by dsimp [e]; omega,by dsimp [e]; omega,
    ⟨hx2,hx3⟩,eqn,inverse_run he hx2 eqn⟩

/-- At depth r+1 there is a real ordinary predecessor with a prescribed
long first reverse gap. The slack term keeps the relative additive defect
uniform in depth. Further reverse gaps lie between three and six. -/
theorem spread_witness {y L : ℕ} (hy : unitOdd y) (hL : 0<L) (r : ℕ) :
    ∃ x S B : ℕ, unitOdd x ∧ run S x=y ∧ grade S x=r+1 ∧ L+3*r≤S ∧ S≤L+3+6*r ∧
      3^(r+1)*x+B=2^S*y ∧
      5*2^L*B+2^L*3^(r+1)≤8*2^S := by
  induction r with
  | zero =>
    obtain ⟨e,x,lo,hi,ux,edge,visit⟩ := bounded_inverse hy hL
    refine ⟨x,e,1,ux,visit,inverse_grade (by omega) ux.1 edge,by omega,by omega,by simpa using edge,?_⟩
    have hp : (2:ℕ)^L≤2^e := Nat.pow_le_pow_right (by decide) lo
    simp only [Nat.zero_add, pow_one, mul_one]
    omega
  | succ r ih =>
    obtain ⟨x,S,B,ux,visit,gr,lo,hi,form,slack⟩ := ih
    obtain ⟨e,z,elo,ehi,uz,edge,reaches⟩ := bounded_inverse ux (by decide : 0<3)
    have gain : 8≤(2:ℕ)^e := Nat.pow_le_pow_right (by decide : 0<2) elo
    refine ⟨z,e+S,2^e*B+3^(r+1),uz,?_,?_,by omega,by omega,?_,?_⟩
    · rw [run_add,reaches,visit]
    · rw [join_grade,reaches,gr,inverse_grade (by omega) uz.1 edge]; omega
    · rw [pow_succ (3:ℕ) (r+1),pow_add]
      calc
        _ = 3^(r+1)*(3*z+1)+2^e*B := by ring
        _ = 2^e*(3^(r+1)*x+B) := by rw [edge]; ring
        _ = _ := by rw [form]; ring
    · rw [pow_succ (3:ℕ) (r+1),pow_add]
      calc
        _ = 2^e*(5*2^L*B)+8*(2^L*3^(r+1)) := by ring
        _ ≤ 2^e*(5*2^L*B)+2^e*(2^L*3^(r+1)) :=
          Nat.add_le_add_left (Nat.mul_le_mul_right _ gain) _
        _ = 2^e*(5*2^L*B+2^L*3^(r+1)) := by ring
        _ ≤ 2^e*(8*2^S) := Nat.mul_le_mul_left _ slack
        _ = _ := by ring

theorem lift_run_grade_unit (k S a y : ℕ) (state : run S a=y) (unit : a%3≠0) :
    run (k+S) (2^k*a)=y ∧ grade (k+S) (2^k*a)=grade S a ∧ (2^k*a)%3≠0 := by
  rw [run_add,join_grade,run_doubling_lift,grade_doubling_lift,zero_add,state]
  exact ⟨rfl,rfl,product_unit _ _ unit⟩

/-- Every physical affine numerator has height at most
2^t ((3/2)^grade - 1). This bounds *all* predecessors at the given grade. -/
theorem grade_defect (t n : ℕ) :
    2^(grade t n)*(AsynchronousGuard.offset t n+2^t) ≤ 3^(grade t n)*2^t := by
  induction t with
  | zero => simp [grade,AsynchronousGuard.offset]
  | succ t ih =>
    have bit : run t n%2=0 ∨ run t n%2=1 := by omega
    rcases bit with zero|one
    · simp only [grade,AsynchronousGuard.offset,zero,Nat.add_zero,pow_zero,one_mul,
        zero_mul,pow_succ 2 t]
      have powers := Nat.pow_le_pow_left (by decide : 2≤3) (grade t n)
      have comp := Nat.mul_le_mul_right (2^t) powers
      nlinarith only [ih,comp]
    · simp only [grade,AsynchronousGuard.offset,one,one_mul,pow_succ]
      nlinarith only [ih]

#print axioms grade_defect
#print axioms bounded_inverse
#print axioms spread_witness
end InverseSpreading
