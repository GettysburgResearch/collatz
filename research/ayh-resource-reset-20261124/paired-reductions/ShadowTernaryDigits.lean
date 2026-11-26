import Mathlib.Tactic.Ring

/-! How one fixed simultaneous-shadow family visits ternary residue classes.
The parameter counts shortcut exponents and carries no basin assertion. -/
namespace ShadowTernaryDigits

def index : Nat → Nat
  | 0 => 1
  | t+1 => 262144*index t+165053

theorem index_equation (t : Nat) : 27*index t+17=44*262144^t := by
  induction t with
  | zero => decide
  | succ t ih =>
    calc
      _ = 262144*(27*index t+17) := by rw [index]; ring
      _ = _ := by rw [ih,pow_succ]; ring

theorem shadow_equation (t : Nat) : 27*index t+17=44*2^(18*t) := by
  rw [index_equation,pow_mul]
  rfl

private theorem digit_power (d : Nat) :
    ∃ v : Nat, 262144^(3^d)=1+27*3^d*(3*v+1) := by
  induction d with
  | zero => exact ⟨3236,by decide⟩
  | succ d ih =>
    obtain ⟨v,h⟩ := ih
    let V := 3*v+1
    use v+9*3^d*V^2+81*(3^d)^2*V^3
    rw [pow_succ 3 d,pow_mul,h]
    dsimp [V]
    ring

private theorem digit_multiple (n d : Nat) :
    ∃ k : Nat, 262144^(n*3^d)=1+27*3^d*(n+3*k) := by
  obtain ⟨v,step⟩ := digit_power d
  induction n with
  | zero => exact ⟨0,by simp⟩
  | succ n ih =>
    obtain ⟨k,h⟩ := ih
    use k+v+9*3^d*(n+3*k)*(3*v+1)
    rw [Nat.succ_mul,pow_add,h,step]
    ring

/-- A shift by n times the d-th ternary place has exactly the same order
when n is a unit, and advances that digit by 2n mod 3. -/
theorem digit_displacement (t n d : Nat) :
    ∃ v : Nat, index (t+n*3^d)=index t+3^d*v ∧ v%3=(2*n)%3 := by
  obtain ⟨k,power⟩ := digit_multiple n d
  let v := 44*262144^t*(n+3*k)
  refine ⟨v,?_,?_⟩
  · have big := index_equation (t+n*3^d)
    rw [pow_add,power] at big
    have small := index_equation t
    have changed : 44*(262144^t*(1+27*3^d*(n+3*k))) =
        44*262144^t+27*(3^d*v) := by dsimp [v]; ring
    rw [changed,←small] at big
    omega
  · have one : (262144:Nat)^t%3=1 := by
      induction t with
      | zero => decide
      | succ t ih => rw [pow_succ,Nat.mul_mod,ih]
    dsimp [v]
    rw [Nat.mul_mod (44*_),Nat.mul_mod 44,one]
    have last : (n+3*k)%3=n%3 := by omega
    rw [last]
    exact (Nat.mul_mod 2 n 3).symm

/-- All three lifts of a fixed parameter representative occur among the
next three indices separated by 3^d. This is an exact finite residue
statement, independent of the ordinary Collatz conjecture. -/
theorem three_lifts (t d a : Nat) (same : index t % 3^d=a%3^d) :
    ∃ n : Nat, n<3 ∧ index (t+n*3^d)%3^(d+1)=a%3^(d+1) := by
  let S := 3^d
  let q := index t / S
  let u := a / S
  let n := (2*((u%3)+3-(q%3)))%3
  have nsmall : n<3 := Nat.mod_lt _ (by decide)
  obtain ⟨v,shift,digit⟩ := digit_displacement t n d
  have mod : (q+v)%3=u%3 := by dsimp [n] at digit; omega
  have same' : index t%S=a%S := same
  have lhs : index (t+n*S)=S*(q+v)+a%S := by
    have e : S*q+index t%S=index t := Nat.div_add_mod ..
    change index (t+n*S)=index t+S*v at shift
    rw [←e,same'] at shift
    rw [shift]
    ring
  have rhs : a=S*u+a%S := (Nat.div_add_mod ..).symm
  have form (b : Nat) :
      (S*b+a%S)%(S*3)=(S*(b%3)+a%S)%(S*3) := by
    have split : S*b+a%S = S*3*(b/3)+(S*(b%3)+a%S) := by
      calc _ = S*(3*(b/3)+b%3)+a%S := by rw [Nat.div_add_mod]
           _ = _ := by ring
    rw [split,Nat.mul_add_mod]
  refine ⟨n,nsmall,?_⟩
  rw [pow_succ]
  change index (t+n*S)%(S*3)=a%(S*3)
  rw [lhs,form,mod]
  conv_rhs => rw [rhs,form]

/-- Every block of 3^d consecutive shadow indices gives every residue.
As the domain and codomain have equal finite size, each occurs once. -/
theorem full_block (d a L : Nat) :
    ∃ i, i<3^d ∧ index (L+i)%3^d=a%3^d := by
  induction d with
  | zero => exact ⟨0,by decide,by simp only [pow_zero]; omega⟩
  | succ d ih =>
    obtain ⟨i,small,same⟩ := ih
    obtain ⟨n,cap,next⟩ := three_lifts (L+i) d a same
    refine ⟨i+n*3^d,?_,?_⟩
    · rcases (show n=0 ∨ n=1 ∨ n=2 by omega) with hn|hn|hn <;> rw [hn,pow_succ] <;> omega
    · simpa only [Nat.add_assoc] using next

theorem cofinal_residue (d a L : Nat) :
    ∃ t, L≤t ∧ index t%3^d=a%3^d := by
  obtain ⟨i,_,same⟩ := full_block d a L
  exact ⟨L+i,by omega,same⟩

/-- An eventually total finite ternary test on this single fixed shadow
family must cover the entire original parameter row. -/
theorem finite_screen (d L : Nat) (P : Nat → Prop)
    (periodic : ∀ i j, i%3^d=j%3^d → (P i ↔ P j))
    (cover : ∀ t, L≤t → P (index t)) : ∀ m, P m := by
  intro m
  obtain ⟨t,large,same⟩ := cofinal_residue d m L
  exact (periodic _ _ same).mp (cover t large)

#print axioms shadow_equation
#print axioms digit_displacement
#print axioms three_lifts
#print axioms full_block
#print axioms cofinal_residue
#print axioms finite_screen
end ShadowTernaryDigits
