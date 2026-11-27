import FixedGradeCone

/-! A finite ternary potential condition implies physical inverse paths at
every exact supplied grade, with a uniform total clock. The numeric table
instance is separately verified by the packet's exact integer checker. -/
set_option autoImplicit false
set_option warningAsError true
namespace InversePotential
open Collatz.TwoGapRouting

def q : ℕ := 531441

def Local (V : ℕ → ℕ) : Prop := ∀r, r<3*q → r%3≠0 →
  ∃e u, 0<e ∧ e≤6 ∧ u%3≠0 ∧ 3*u+1=2^e*r ∧ 6*e+V (u%q)≤13+V (r%q)

theorem physical_gap {V : ℕ → ℕ} (cert : Local V) {y : ℕ} (unit : y%3≠0) :
    ∃e z, 0<e ∧ e≤6 ∧ z%3≠0 ∧ 3*z+1=2^e*y ∧ 6*e+V (z%q)≤13+V (y%q) := by
  let r:=y%(3*q)
  let j:=y/(3*q)
  have repr : r+3*q*j=y := Nat.mod_add_div y (3*q)
  have inRange : r<3*q := Nat.mod_lt _ (by decide)
  have ru : r%3≠0 := by dsimp [r,q]; omega
  obtain ⟨e,u,ep,eb,uu,eq,h⟩:=cert r inRange ru
  let z:=u+q*(2^e*j)
  have zu : z%3≠0 := by dsimp [z,q]; omega
  have zq : z%q=u%q := by simp [z,Nat.add_mod]
  have yq : y%q=r%q := by rw [←repr]; simp [Nat.add_mod,Nat.mul_assoc,Nat.mul_left_comm]
  have actual : 3*z+1=2^e*y := by
    calc
      3*z+1=(3*u+1)+2^e*(3*q*j) := by dsimp [z]; ring
      _=2^e*(r+3*q*j) := by rw [eq]; ring
      _=_ := by rw [repr]
  exact ⟨e,z,ep,eb,zu,actual,by rwa [zq,yq]⟩

/-- The potential telescopes on an actual positive inverse chain.
The source and target are odd units at the two endpoints. -/
theorem exact_grade {V : ℕ → ℕ} (cert : Local V) (b d : ℕ) (bo : b%2=1) (bu : b%3≠0) :
    ∃w m, w%2=1 ∧ w%3≠0 ∧ run m w=b ∧ odds m w=d ∧
      6*m+V (w%q)≤13*d+V (b%q) := by
  induction d with
  | zero => exact ⟨b,0,bo,bu,rfl,rfl,by simp⟩
  | succ d ih =>
    obtain ⟨w,m,_,wu,reach,grade,cost⟩:=ih
    obtain ⟨e,z,ep,_,zu,equ,pay⟩:=physical_gap cert wu
    obtain ⟨hit,count,odd⟩:=gap e z w ep equ
    obtain ⟨joined,added⟩:=append e m z
    rw [hit,reach] at joined
    rw [count,hit,grade] at added
    exact ⟨z,e+m,odd,zu,joined,by omega,by omega⟩

theorem clock_bound {V : ℕ → ℕ} (cert : Local V) (finite : ∀r<q,V r≤48)
    (b d : ℕ) (bo : b%2=1) (bu : b%3≠0) :
    ∃w m, w%2=1 ∧ w%3≠0 ∧ run m w=b ∧ odds m w=d ∧ 6*m≤13*d+48 := by
  obtain ⟨w,m,wo,wu,reach,g,cost⟩:=exact_grade cert b d bo bu
  have bound:=finite _ (Nat.mod_lt b (by decide : 0<q))
  exact ⟨w,m,wo,wu,reach,g,by omega⟩

/-- Every unit inverse choice with exponent at most five is forced on a
positive integer shadowing 1/13 modulo a sufficiently high power of three. -/
theorem cap_five_step {y z e d n : ℕ} (ep : 0<e) (cap : e≤5) (unit : z%3≠0)
    (relation : 3*z+1=2^e*y) (shadow : 13*y=1+9*(3^d*n)) :
    e=4 ∧ 13*z=1+3*(3^d*(16*n)) := by
  have residue : y%9=7 := by omega
  have forced : e=4 := by
    rcases (show e=1 ∨ e=2 ∨ e=3 ∨ e=4 ∨ e=5 by omega) with rfl|rfl|rfl|rfl|rfl
      <;> norm_num at relation ⊢ <;> omega
  refine ⟨forced,?_⟩
  rw [forced] at relation
  norm_num at relation
  nlinarith only [relation,shadow]

theorem strategy {V : ℕ → ℕ} (cert : Local V) (finite : ∀r<q,V r≤48) :
    Collatz.FixedGradeCone.Strategy 6 13 := by
  refine ⟨48,?_⟩
  intro y yo yu d
  obtain ⟨w,m,_,wu,hit,g,cost⟩:=clock_bound cert finite y d yo yu
  exact ⟨w,m,wu,hit,g,cost⟩

#print axioms strategy
#print axioms cap_five_step
#print axioms physical_gap
#print axioms exact_grade
#print axioms clock_bound
end InversePotential
