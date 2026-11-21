import ShellCover
import Mathlib.Data.Nat.ModEq

/-! Exact ordinary words and modular-ray placement for narrow section returns. -/

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzShell.BandWord

/-- A canonical residue occurs in every forward interval of length twice the
    modulus, with a formula that stays in the ordinary natural numbers. -/
theorem ray_interval {M r : Nat} (hM : 0<M) (hr : r<M) (L : Nat) :
    ∃ k, L<r+M*k ∧ r+M*k<L+2*M := by
  refine ⟨L/M+1,?_,?_⟩
  all_goals
    have decomp := Nat.mod_add_div L M
    have small := Nat.mod_lt L hM
    rw [Nat.mul_add,Nat.mul_one]
    omega

/-- Coprimality gives an ordinary solution of a multiplicative congruence.
    The first CRT modulus enforces an exact division; no inverse in a
    completion is substituted for a natural number. -/
theorem solve_mul_mod {a M : Nat} (cop : a.Coprime M) (b : Nat) :
    ∃ x, Nat.ModEq M (a*x) b := by
  let z := Nat.chineseRemainder cop 0 b
  have zero : (z:Nat)%a=0 := by simpa [Nat.ModEq] using z.property.1
  have dvd : a∣(z:Nat) := Nat.dvd_of_mod_eq_zero zero
  refine ⟨(z:Nat)/a,?_⟩
  rw [Nat.mul_div_cancel' dvd]
  exact z.property.2

theorem solve_affine_mod {a M : Nat} (hM : 0<M) (cop : a.Coprime M) (b c : Nat) :
    ∃ x, Nat.ModEq M (a*x+c) b := by
  let r := b+M-c%M
  obtain ⟨x,hx⟩ := solve_mul_mod cop r
  have rem := Nat.mod_lt c hM
  have eq : r+c=b+M+M*(c/M) := by
    have dv := Nat.mod_add_div c M
    dsimp [r]
    omega
  refine ⟨x,(hx.add_right c).trans ?_⟩
  rw [eq]
  simp [Nat.ModEq,Nat.add_mod]

/-- One fixed ordinary residue simultaneously meets the affine ternary
    constraint and the binary endpoint residue. -/
theorem simultaneous_residue {a M : Nat} (hM : 0<M)
    (cop : a.Coprime M) (four : Nat.Coprime 4 M) (b c : Nat) :
    ∃ r, r<4*M ∧ r%4=1 ∧ Nat.ModEq M (a*r+c) b := by
  obtain ⟨x,hx⟩ := solve_affine_mod hM cop b c
  let z := Nat.chineseRemainder four 1 x
  refine ⟨z,?_,?_,?_⟩
  · exact Nat.chineseRemainder_lt_mul four 1 x (by decide) hM.ne'
  · simpa [Nat.ModEq] using z.property.1
  · exact ((z.property.2.mul_left a).add_right c).trans hx

/-- The simultaneous residue has cofinal ordinary representatives in short
    specified intervals, preserving both congruences. -/
theorem affine_interval {a M : Nat} (hM : 0<M)
    (cop : a.Coprime M) (four : Nat.Coprime 4 M) (b c L : Nat) :
    ∃ m, L<m ∧ m<L+2*(4*M) ∧ m%4=1 ∧ Nat.ModEq M (a*m+c) b := by
  obtain ⟨r,hr,r4,rc⟩ := simultaneous_residue hM cop four b c
  obtain ⟨k,lo,hi⟩ := ray_interval (by positivity : 0<4*M) hr L
  refine ⟨r+(4*M)*k,lo,hi,?_,?_⟩
  · simp [Nat.add_mod,Nat.mul_mod,r4]
  · have eq : a*(r+(4*M)*k)+c=(a*r+c)+M*(4*a*k) := by ring
    rw [eq]
    exact (Nat.add_modulus_mul_modEq_iff).mpr rc

private theorem coprime_pow_two_three (b c : Nat) : Nat.Coprime (2^b) (3^c) :=
  (show Nat.Coprime 2 3 by decide).pow b c

/-- The exact factor equation supplies an actual legal ordinary prefix:
    one odd step, one halving, b odd steps, and h halvings. -/
theorem factored_word {b h n m : Nat}
    (eq : 3^b*(3*n+5)=2^(b+2)*(2^h*m+1)) :
    n%4=1 ∧ orbit (b+h+2) n=m := by
  have div : 2^(b+2)∣3^b*(3*n+5) := by rw [eq]; exact dvd_mul_right _ _
  have cop : Nat.Coprime (2^(b+2)) (3^b) := coprime_pow_two_three _ _
  obtain ⟨u,nu⟩ := cop.dvd_of_dvd_mul_left div
  have du : 2^(b+2)*u=3*n+5 := nu.symm
  have p : 0<2^b := by positivity
  have us : 0<u := by by_contra! z; simp [show u=0 by omega] at du
  have four : 4*(2^b*u)=3*n+5 := by
    simpa [pow_add,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using du
  have mod : n%4=1 := by omega
  have odd : n%2≠0 := by omega
  have first : step n=2*(2^b*u-1) := by simp [step,odd]; omega
  have two : orbit 2 n=2^b*u-1 := by
    change step (step n)=_
    rw [first,step_double]
  have total : 2^(b+2)*(3^b*u)=2^(b+2)*(2^h*m+1) := by
    calc _ = 3^b*(2^(b+2)*u) := by ring
         _ = 3^b*(3*n+5) := by rw [du]
         _ = _ := eq
  have endpoint : 3^b*u=2^h*m+1 := Nat.eq_of_mul_eq_mul_left (by positivity) total
  refine ⟨mod,?_⟩
  have clock : b+h+2=2+b+h := by omega
  rw [clock,orbit_add,orbit_add,two,(odd_run b u us).1,endpoint]
  simpa using orbit_pad h m

/-- The unfactored coefficients match the parity word used in the analytic
    section construction, retaining all offset terms. -/
theorem word_of_identity {p t n m : Nat} (hp : 1≤p) (ht : p+1≤t)
    (eq : 3^p*n+5*3^(p-1)=2^t*m+2^(p+1)) :
    n%4=1 ∧ orbit t n=m := by
  let b := p-1
  let h := t-p-1
  have pb : p=b+1 := by dsimp [b]; omega
  have tc : t=b+h+2 := by dsimp [b,h]; omega
  have factors : 3^b*(3*n+5)=2^(b+2)*(2^h*m+1) := by
    have e : p-1=b := rfl
    rw [e,pb,tc,pow_succ,show b+1+1=b+2 by omega,
      show b+h+2=(b+2)+h by omega,pow_add] at eq
    nlinarith only [eq]
  simpa [←tc] using factored_word factors

/-- Complete ordinary realization inside a chosen short interval. This theorem
    supplies both the congruence choice and its legal forward orbit. -/
theorem section_word_in_interval (p t L : Nat) (hp : 2≤p) (ht : p+2≤t)
    (large : 5*3^p≤L) :
    ∃ n m, L<m ∧ m<L+2*(4*3^p) ∧ m%4=1 ∧ n%4=1 ∧ orbit t n=m ∧
      3^p*n+5*3^(p-1)=2^t*m+2^(p+1) := by
  have Mpos : 0<(3:Nat)^p := by positivity
  have cp : Nat.Coprime (2^t) (3^p) := coprime_pow_two_three _ _
  have cf : Nat.Coprime 4 (3^p) := (show Nat.Coprime 4 3 by decide).pow_right p
  obtain ⟨m,lo,hi,m4,mc⟩ := affine_interval Mpos cp cf (5*3^(p-1)) (2^(p+1)) L
  have powers : (3:Nat)^(p-1)≤3^p := Nat.pow_le_pow_right (by decide) (by omega)
  have one : 1≤(2:Nat)^t := Nat.one_le_pow _ _ (by decide)
  have prod := Nat.mul_le_mul_right m one
  have enough : 5*3^(p-1)≤2^t*m+2^(p+1) := by
    calc 5*3^(p-1) ≤ 5*3^p := Nat.mul_le_mul_left 5 powers
         _ ≤ L := large
         _ ≤ m := lo.le
         _ ≤ 2^t*m := by simpa using prod
         _ ≤ _ := Nat.le_add_right _ _
  have divisible : 3^p∣2^t*m+2^(p+1)-5*3^(p-1) :=
    (Nat.modEq_iff_dvd' enough).mp mc.symm
  let n := (2^t*m+2^(p+1)-5*3^(p-1))/3^p
  have eq : 3^p*n+5*3^(p-1)=2^t*m+2^(p+1) := by
    dsimp [n]
    rw [Nat.mul_div_cancel' divisible,Nat.sub_add_cancel enough]
  obtain ⟨n4,hit⟩ := word_of_identity (by omega) (by omega) eq
  exact ⟨n,m,lo,hi,m4,n4,hit,eq⟩

end CollatzShell.BandWord

#print axioms CollatzShell.BandWord.ray_interval
#print axioms CollatzShell.BandWord.solve_mul_mod
#print axioms CollatzShell.BandWord.solve_affine_mod
#print axioms CollatzShell.BandWord.simultaneous_residue
#print axioms CollatzShell.BandWord.affine_interval
#print axioms CollatzShell.BandWord.factored_word
#print axioms CollatzShell.BandWord.word_of_identity
#print axioms CollatzShell.BandWord.section_word_in_interval
