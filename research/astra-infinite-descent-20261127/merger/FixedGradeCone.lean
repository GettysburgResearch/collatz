import AllProgressions
import ClockCone

/-! Composition of a supplied inverse path budget with ordinary fixed-clock
finite-pattern routing. Both the physical clock and grade are specified. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FixedGradeCone
open TwoGapRouting FirstArrival

/-- Every odd ternary unit admits an actual ternary-unit predecessor at each
prescribed exact grade, within the indicated affine clock budget. -/
def Strategy (A B : ℕ) : Prop := ∃K : ℕ, ∀y : ℕ, y%2=1 → y%3≠0 → ∀d : ℕ,
  ∃w m : ℕ, w%3≠0 ∧ run m w=y ∧ odds m w=d ∧ A*m≤B*d+K

/-- The same lower source block supplies every residue of the prescribed
modulus at each eligible pair of target clock and grade, including for
even targets. A and B may be specialized to any certified strategy. -/
theorem of_strategy (A B : ℕ) (ap : 0<A) (strategy : Strategy A B)
    (F : List ℕ) (q : ℕ) (qp : 0<q) :
    ∃G C : ℕ, ∀d M : ℕ, G≤d → B*d+C≤A*M → ∀y : ℕ, y%3≠0 →
      ∃z : ℕ, 0<z ∧ ∀c : ℕ, ∃j<q, z+j ≡ c [MOD q] ∧
        ∀i∈0::F, First M (z+j+i) y ∧ odds M (z+j+i)=d := by
  obtain ⟨K,paths⟩:=strategy
  obtain ⟨H,g,core⟩:=AllProgressions.all_clocks F q qp
  refine ⟨g+1,K+A*(H+10),?_⟩
  intro d M large budget y unit
  obtain ⟨b,e,bo,bu,_,eb,away,leg,eg⟩:=branch y unit
  obtain ⟨w,m,wu,hit,gr,price⟩:=paths b bo bu (d-(g+1))
  have upper : A*m≤B*d+K := price.trans (Nat.add_le_add_right (Nat.mul_le_mul_left B (Nat.sub_le ..)) _)
  have allowed : H+m+e≤M := Nat.le_of_mul_le_mul_left (calc
    A*(H+m+e)=A*m+A*(H+e) := by ring
    _≤(B*d+K)+A*(H+10) := Nat.add_le_add upper (Nat.mul_le_mul_left A (by omega))
    _≤A*M := by omega) ap
  let shift:=M-(m+e)
  have pre : shift+m+e=M := by dsimp [shift]; omega
  obtain ⟨z,zp,classes⟩:=core shift (by dsimp [shift]; omega) w wu
  refine ⟨z,zp,?_⟩
  intro c
  obtain ⟨j,jq,res,arms⟩:=classes c
  refine ⟨j,jq,res,?_⟩
  intro i hi
  obtain ⟨arrival,g0⟩:=arms i hi
  obtain ⟨v,o⟩:=append shift m (z+j+i)
  rw [arrival.1,hit] at v
  rw [g0,arrival.1,gr] at o
  have finalGrade:=(append (shift+m) e (z+j+i)).2
  rw [pre,o,v,eg] at finalGrade
  exact ⟨by rw [←pre]; exact join v away leg,by omega⟩

/-- The existing elementary ternary potential gives a fully unconditional
slope-three first-arrival cone for every finite pattern and source modulus. -/
theorem elementary (F : List ℕ) (q : ℕ) (qp : 0<q) :
    ∃G C : ℕ, ∀d M : ℕ, G≤d → 3*d+C≤M → ∀y : ℕ, y%3≠0 →
      ∃z : ℕ, 0<z ∧ ∀c : ℕ, ∃j<q, z+j ≡ c [MOD q] ∧
        ∀i∈0::F, First M (z+j+i) y ∧ odds M (z+j+i)=d := by
  have strategy : Strategy 1 3 := by
    refine ⟨3,?_⟩
    intro y _ unit d
    simpa only [Nat.one_mul] using ClockCone.unit_budget d y unit
  simpa only [Nat.one_mul] using of_strategy 1 3 (by decide) strategy F q qp

#print axioms of_strategy
#print axioms elementary
end Collatz.FixedGradeCone
