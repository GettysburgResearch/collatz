import ResidualDescent

/-! Finite, original-floor descent through every exit after a long enough
sequence of PLL loops. Only raw ordinary boundary equations are required. -/
namespace LoopCone
set_option maxHeartbeats 650000
set_option maxRecDepth 12000

private theorem light_run (q : Nat→Nat) (r : Nat)
    (light : ∀ j, j<r → 8*q (j+1)=9*q j+7) :
    8^r*(q r+7)=9^r*(q 0+7) := by
  suffices ∀ j, j≤r → 8^j*(q j+7)=9^j*(q 0+7) by exact this r (Nat.le_refl _)
  intro j hj
  induction j with
  | zero => simp
  | succ j ih =>
    have e := light j (by omega)
    have ez : 8*(q (j+1)+7)=9*(q j+7) := by omega
    calc
      8^(j+1)*(q (j+1)+7)=8^j*(8*(q (j+1)+7)) := by rw [Nat.pow_succ]; ac_rfl
      _=9*(8^j*(q j+7)) := by rw [ez]; ac_rfl
      _=_ := by rw [ih (by omega),Nat.pow_succ]; ac_rfl

private theorem loop_run (z : Nat→Nat) (s : Nat)
    (loop : ∀ j, j<s → 2048*z (j+1)=729*z j+4213) :
    2048^s*z s ≤ 729^s*z 0+4*2048^s := by
  suffices ∀ j, j≤s → 2048^j*z j ≤ 729^j*z 0+4*2048^j by exact this s (Nat.le_refl _)
  intro j hj
  induction j with
  | zero => simp
  | succ j ih =>
    have e := loop j (by omega)
    calc
      2048^(j+1)*z (j+1)=2048^j*(2048*z (j+1)) := by rw [Nat.pow_succ]; ac_rfl
      _=729*(2048^j*z j)+4213*2048^j := by rw [e,Nat.mul_add]; ac_rfl
      _≤729*(729^j*z 0+4*2048^j)+4213*2048^j :=
        Nat.add_le_add_right (Nat.mul_le_mul_left _ (ih (by omega))) _
      _≤729^(j+1)*z 0+4*2048^(j+1) := by
        rw [Nat.mul_add,Nat.pow_succ,Nat.pow_succ]
        have a : 729*(729^j*z 0)=729^j*729*z 0 := by ac_rfl
        rw [a]
        omega

private theorem join (G H U V x z y v : Nat)
    (light : G*v≤H*(x+7)) (loop : U*z≤V*v+4*U)
    (paid : 32*y=9*z+5) :
    32*((G*U)*y)≤9*((H*V)*(x+7))+41*(G*U) := by
  calc
    32*((G*U)*y)=G*(U*(32*y)) := by ac_rfl
    _=9*(G*(U*z))+5*(G*U) := by rw [paid,Nat.mul_add,Nat.mul_add]; ac_rfl
    _≤9*(G*(V*v+4*U))+5*(G*U) :=
      Nat.add_le_add_right (Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ loop)) _
    _=9*(V*(G*v))+41*(G*U) := by
      rw [Nat.mul_add,Nat.mul_add,Nat.add_assoc]
      have h : 9*(G*(4*U))=36*(G*U) := by ac_rfl
      rw [h,←Nat.add_mul]; ac_rfl
    _≤9*(V*(H*(x+7)))+41*(G*U) :=
      Nat.add_le_add_right (Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ light)) _
    _=_ := by ac_rfl

private theorem bound {M N x y : Nat} (posN : 0<N) (big : 512≤x) (res : 5*M≤13*N)
    (cost : 32*(N*y)≤9*(M*(x+7))+41*N) : y<x ∧ y<(3*x+1)/4 := by
  have lim : N*(160*y)≤N*(117*(x+7)+205) := calc
    _=5*(32*(N*y)) := by ac_rfl
    _≤5*(9*(M*(x+7))+41*N) := Nat.mul_le_mul_left _ cost
    _=9*((5*M)*(x+7))+205*N := by rw [Nat.mul_add]; ac_rfl
    _≤9*((13*N)*(x+7))+205*N :=
      Nat.add_le_add_right (Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ res)) _
    _=N*(117*(x+7)+205) := by
      rw [Nat.mul_add N]
      have e : 9*((13*N)*(x+7))=N*((9*13)*(x+7)) := by ac_rfl
      rw [e,Nat.mul_comm 205 N]
  have small := Nat.le_of_mul_le_mul_left lim posN
  omega

private theorem pll {x a b y : Nat} (h₁ : 32*a=9*x+5) (h₂ : 8*b=9*a+7)
    (h₃ : 8*y=9*b+7) : 2048*y=729*x+4213 := by
  have ab : 256*b=81*x+269 := by omega
  clear h₁ h₂
  omega

/-- The first paid boundary after all the loops already beats both floors.
Consequently the same point merges through every actual continuation. -/
theorem loop_exit_descent (q z u v : Nat→Nat) (r s w : Nat)
    (hr : 3≤r) (o₃ : q 3%2=1)
    (light : ∀ j, j<r → 8*q (j+1)=9*q j+7)
    (start : z 0=q r)
    (P : ∀ j, j<s → 32*u j=9*z j+5)
    (L₁ : ∀ j, j<s → 8*v j=9*u j+7)
    (L₂ : ∀ j, j<s → 8*z (j+1)=9*v j+7)
    (exit : 32*w=9*z s+5) (odd : w%2=1)
    (cone : 5*(9^r*729^s)≤13*(8^r*2048^s)) :
    0<w ∧ w%2=1 ∧ w<q 0 ∧ w<(3*q 0+1)/4 := by
  have h3 := light_run q 3 (fun j hj => light j (by omega))
  change 512*(q 3+7)=729*(q 0+7) at h3
  have dv : 1024 ∣ 729*(q 0+7) := by
    refine ⟨(q 3+7)/2,?_⟩
    rw [←h3]
    omega
  obtain ⟨k,hk⟩ := (show Nat.Coprime 1024 729 by decide).dvd_of_dvd_mul_left dv
  have big : 512≤q 0 := by omega
  have lr := light_run q r light
  have loops (j : Nat) (hj : j<s) : 2048*z (j+1)=729*z j+4213 := by
    exact pll (P j hj) (L₁ j hj) (L₂ j hj)
  have loop := loop_run z s loops
  rw [start] at loop
  have l : 8^r*q r≤9^r*(q 0+7) := by rw [←lr,Nat.mul_add]; omega
  have cost := join _ _ _ _ _ _ _ _ l loop exit
  obtain ⟨lt₁,lt₂⟩ := bound (Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))) big cone cost
  exact ⟨by omega,odd,lt₁,lt₂⟩

#print axioms loop_exit_descent
end LoopCone
