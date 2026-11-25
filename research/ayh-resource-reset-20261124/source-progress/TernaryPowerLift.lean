import Mathlib.Tactic.Ring

namespace TernaryPowerLift

/-- The first new ternary digit of the dyadic period is one. -/
theorem period (j : Nat) :
    ∃ u : Nat, 2^(2*3^j) = 1 + 3^(j+1)*(3*u+1) := by
  induction j with
  | zero => exact ⟨0, by decide⟩
  | succ j ih =>
    obtain ⟨u,hu⟩ := ih
    let a := 3^j*(3*u+1)
    have ha : 2^(2*3^j)=1+3*a := by
      rw [hu]; dsimp [a]; ring
    refine ⟨u + 3^j*(3*u+1)^2 + (3^j)^2*(3*u+1)^3, ?_⟩
    rw [show 2*3^(j+1)=(2*3^j)*3 by ring, Nat.pow_mul, ha]
    dsimp [a]
    ring

private theorem fourMod (n : Nat) : 2^(2*n)%3=1 := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [show 2*(n+1)=2*n+2 by omega, Nat.pow_add,Nat.mul_mod,ih]

/-- Arbitrarily large powers of two in every unit class modulo any positive
power of three. The nonnegative affine quotient is part of the witness. -/
theorem cofinal (j b L : Nat) (hb : b%3≠0) :
    ∃ e k : Nat, L≤e ∧ 2^e = b + 3^(j+1)*k := by
  induction j with
  | zero =>
    let E := 2*(b+L)
    have hp : b≤2^E := by
      have h := Nat.lt_two_pow_self (n:=E)
      dsimp [E] at h ⊢; omega
    have hm : 2^E%3=1 := fourMod _
    by_cases h : b%3=1
    · exact ⟨E,(2^E-b)/3,by dsimp [E]; omega,by simp; omega⟩
    · have hm' : 2^(E+1)%3=2 := by rw [Nat.pow_succ,Nat.mul_mod,hm]
      have hp' : b≤2^(E+1) := by rw [Nat.pow_succ]; omega
      exact ⟨E+1,(2^(E+1)-b)/3,by dsimp [E]; omega,by simp; omega⟩
  | succ j ih =>
    obtain ⟨e,k,el,he⟩ := ih
    obtain ⟨u,hu⟩ := period j
    let D := 3^(j+1)
    let G := 2*3^j
    have hg : 2^G=1+D*(3*u+1) := hu
    have hd : D%3=0 := by dsimp [D]; rw [Nat.pow_succ]; simp
    change 2^e = b+D*k at he
    let k1 := k+2^e*(3*u+1)
    let k2 := k1+2^(e+G)*(3*u+1)
    have s1 : 2^(e+G)=b+D*k1 := by
      calc 2^(e+G)=2^e+ D*(2^e*(3*u+1)) := by rw [Nat.pow_add,hg]; ring
           _ = b+D*k1 := by dsimp [k1]; rw [he]; ring
    have s2 : 2^(e+G+G)=b+D*k2 := by
      calc 2^(e+G+G)=2^(e+G)+ D*(2^(e+G)*(3*u+1)) := by rw [Nat.pow_add,hg]; ring
           _ = b+D*k2 := by dsimp [k2]; rw [s1]; ring
    have me : 2^e%3=b%3 := by rw [he,Nat.add_mod,Nat.mul_mod,hd]; simp
    have me1 : 2^(e+G)%3=b%3 := by rw [s1,Nat.add_mod,Nat.mul_mod,hd]; simp
    have du : (3*u+1)%3=1 := by omega
    have m1 : k1%3=(k%3+b%3)%3 := by
      dsimp [k1]; rw [Nat.add_mod,Nat.mul_mod,me,du]; simp
    have m2 : k2%3=(k1%3+b%3)%3 := by
      dsimp only [k2]; rw [Nat.add_mod,Nat.mul_mod,me1,du]; simp
    have get (w v : Nat) (hw : L≤w) (eq : 2^w=b+D*v) (hv : v%3=0) :
        ∃ e k : Nat, L≤e ∧ 2^e=b+3^(j+1+1)*k := by
      refine ⟨w,v/3,hw,?_⟩
      rw [eq,Nat.pow_succ]
      change b+D*v=b+D*3*(v/3)
      have div : v=3*(v/3) := by omega
      calc b+D*v = b+D*(3*(v/3)) := congrArg (fun x => b+D*x) div
           _ = _ := by ring
    by_cases h : k%3=0
    · exact get e k el he h
    by_cases h1 : k1%3=0
    · exact get (e+G) k1 (by omega) s1 h1
    apply get (e+G+G) k2 (by omega) s2
    rcases (show b%3=1 ∨ b%3=2 by omega) with b1|b2 <;>
      rcases (show k%3=1 ∨ k%3=2 by omega) with r1|r2 <;>
      simp_all
end TernaryPowerLift
