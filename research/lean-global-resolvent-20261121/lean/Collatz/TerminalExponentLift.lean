import Collatz.Closure

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzTerminalExponentLift

/-- The first nonzero ternary digit of 4^(3^n)-1 is exactly one. -/
theorem four_power_lift (n : Nat) :
    ∃ c, 4^(3^n)=1+3^(n+1)*(1+3*c) := by
  induction n with
  | zero => exact ⟨0,by decide⟩
  | succ n ih =>
    obtain ⟨c,hc⟩ := ih
    refine ⟨c+3^n*(1+3*c)^2+(3^n)^2*(1+3*c)^3,?_⟩
    have power : 4^(3^(n+1))=(4^(3^n))^3 := by
      rw [Nat.pow_succ,Nat.pow_mul]
    rw [power,hc]
    have p1 : 3^(n+1)=3*3^n := by rw [Nat.pow_succ]; omega
    have p2 : 3^((n+1)+1)=9*3^n := by
      rw [Nat.pow_succ,p1]
      omega
    rw [p1,p2]
    simp only [Nat.pow_succ,Nat.pow_zero]
    grind

theorem even_power_mod_three (k : Nat) : 2^(2*k)%3=1 := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 2*(k+1)=2*k+2 by omega,Nat.pow_add,Nat.mul_mod,ih]

/-- One elementary lifting step for any target -c that is one modulo three.
Only the additions 0, 2*3^n and 4*3^n to the exponent are needed. -/
theorem lift_exponent {c n h q : Nat} (unit : c%3=2)
    (old : 3^(n+1)*q=2^h+c) :
    ∃ h' q', h≤h' ∧ 3^(n+2)*q'=2^h'+c := by
  obtain ⟨a,ha⟩ := four_power_lift n
  have period : 2^(2*3^n)=1+3^(n+1)*(1+3*a) := by
    rw [Nat.pow_mul]
    change 4^(3^n)=_
    exact ha
  have p1 : 3^(n+1)=3*3^n := by rw [Nat.pow_succ]; omega
  have p2 : 3^(n+2)=3*3^(n+1) := by
    rw [show n+2=(n+1)+1 by omega,Nat.pow_succ]
    omega
  have balance : 3*(3^n*q)=2^h+c := by rw [p1] at old; grind
  have Amod : 2^h%3=1 := by omega
  have cases : q%3=0 ∨ q%3=1 ∨ q%3=2 := by omega
  rcases cases with h0 | h1 | h2
  · refine ⟨h,q/3,by omega,?_⟩
    have qeq : q=3*(q/3) := by omega
    rw [p2]
    grind
  · let Q := q+2*2^h*(1+3*a)+3^(n+1)*2^h*(1+3*a)^2
    have Qform : Q=q+2*2^h+
        3*(2*2^h*a+3^n*2^h*(1+3*a)^2) := by dsimp [Q]; rw [p1]; grind
    have Qeq : Q=3*(Q/3) := by rw [Qform]; omega
    refine ⟨h+4*3^n,Q/3,by omega,?_⟩
    have power : 2^(h+4*3^n)=2^h*(1+3^(n+1)*(1+3*a))^2 := by
      rw [Nat.pow_add,show 4*3^n=(2*3^n)*2 by omega,Nat.pow_mul,period]
    rw [power,p2]
    have form : 3^(n+1)*Q=2^h*(1+3^(n+1)*(1+3*a))^2+c := by
      dsimp [Q]
      simp only [Nat.pow_succ,Nat.pow_zero]
      grind
    grind
  · let Q := q+2^h*(1+3*a)
    have Qform : Q=q+2^h+3*(2^h*a) := by dsimp [Q]; grind
    have Qeq : Q=3*(Q/3) := by rw [Qform]; omega
    refine ⟨h+2*3^n,Q/3,by omega,?_⟩
    have power : 2^(h+2*3^n)=2^h*(1+3^(n+1)*(1+3*a)) := by
      rw [Nat.pow_add,period]
    rw [power,p2]
    have form : 3^(n+1)*Q=2^h*(1+3^(n+1)*(1+3*a))+c := by
      dsimp [Q]
      grind
    grind

/-- Every positive unit target congruent to one modulo three has arbitrarily
large positive dyadic exponents realizing it, at every ternary precision.
The statement is purely finite integer arithmetic, not 3-adic approximation. -/
theorem arbitrarily_large_exponents {c : Nat} (unit : c%3=2) (n H : Nat) :
    ∃ h q, H<h ∧ 3^(n+1)*q=2^h+c := by
  induction n with
  | zero =>
    let h := 2*(H+1)
    have hm : 2^h%3=1 := even_power_mod_three (H+1)
    have dm : (2^h+c)%3=0 := by omega
    refine ⟨h,(2^h+c)/3,by dsimp [h]; omega,?_⟩
    change 3*((2^h+c)/3)=2^h+c
    omega
  | succ n ih =>
    obtain ⟨h,q,large,eq⟩ := ih
    obtain ⟨h',q',inc,eq'⟩ := lift_exponent unit eq
    refine ⟨h',q',by omega,?_⟩
    simpa only [show (n+1)+1=n+2 by omega] using eq'

end CollatzTerminalExponentLift
