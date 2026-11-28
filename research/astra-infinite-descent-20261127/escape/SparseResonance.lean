import Mathlib.Data.ZMod.Basic
import Mathlib.RingTheory.Nilpotent.Basic
import Mathlib.Algebra.Group.Equiv.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! The two-step cancellation at every nonzero ternary-unit character.
All maps act on the actual residue group at the chosen precision. -/
set_option autoImplicit false
set_option warningAsError true

namespace SparseResonance

abbrev RingAt (k : ℕ) := ZMod (3^k)
abbrev UnitAt (k : ℕ) := (RingAt k)ˣ

private theorem nil_three (k : ℕ) : IsNilpotent (3 : RingAt k) := by
  refine ⟨k, ?_⟩
  simpa only [Nat.cast_pow,Nat.cast_ofNat] using ZMod.natCast_self (3^k)

private noncomputable def translate {R : Type*} [CommRing R] {a : R}
    (nil : IsNilpotent a) (u : Rˣ) : Rˣ :=
  (nil.isUnit_add_right_of_commute u.isUnit (Commute.all _ _)).unit

@[simp] private theorem translate_val {R : Type*} [CommRing R] {a : R}
    (nil : IsNilpotent a) (u : Rˣ) : (translate nil u : R)=a+(u:R) :=
  IsUnit.unit_spec _

private noncomputable def translatePerm {R : Type*} [CommRing R] {a : R}
    (nil : IsNilpotent a) : Equiv.Perm Rˣ where
  toFun := translate nil
  invFun := translate nil.neg
  left_inv u := by apply Units.ext; simp
  right_inv u := by apply Units.ext; simp

/-- At any ternary precision, x ↦ 3 + 1/x permutes the units. -/
noncomputable def mobius (k : ℕ) : Equiv.Perm (UnitAt k) :=
  (Equiv.inv (UnitAt k)).trans (translatePerm (nil_three k))

theorem mobius_val (k : ℕ) (x : UnitAt k) :
    (mobius k x : RingAt k)=3+(↑(x⁻¹) : RingAt k) :=
  translate_val (nil_three k) (x⁻¹)

/-- This unit is 1+3x, the numerator in the geometric-branch character. -/
noncomputable def numerator (k : ℕ) (x : UnitAt k) : UnitAt k := mobius k x*x

theorem numerator_val (k : ℕ) (x : UnitAt k) :
    (numerator k x : RingAt k)=1+3*(x:RingAt k) := by
  rw [numerator,Units.val_mul,mobius_val,add_mul]
  simp [add_comm]

private theorem all_sum_zero {G F : Type*} [CommGroup G] [Fintype G] [Field F]
    (χ : G →* F) (nontrivial : ∃ a, χ a≠1) : ∑ x, χ x=0 := by
  obtain ⟨a,ha⟩ := nontrivial
  apply eq_zero_of_mul_eq_self_left ha
  simpa only [Finset.mul_sum,←map_mul] using (Group.mulLeft_bijective a).sum_comp χ

/-- Exact vanishing of the scalar produced by two resonant projections. -/
theorem mobius_character_sum (k : ℕ) {F : Type*} [Field F] (χ : UnitAt k →* F)
    (nontrivial : ∃ a, χ a≠1) : ∑ x, χ (mobius k x)=0 := by
  rw [(mobius k).bijective.sum_comp χ,all_sum_zero χ nontrivial]

/-- The unnormalized ideal character projection. Multiplying by the two
normalizing constants in the analytic kernel preserves the square-zero result. -/
noncomputable def project (k : ℕ) {F : Type*} [Field F]
    (χ : UnitAt k →* F) (f : UnitAt k → F) (y : UnitAt k) : F :=
  χ (y⁻¹) * ∑ x, χ (numerator k x)*f x

theorem project_twice (k : ℕ) {F : Type*} [Field F] (χ : UnitAt k →* F)
    (nontrivial : ∃ a, χ a≠1) (f : UnitAt k → F) (y : UnitAt k) :
    project k χ (project k χ f) y=0 := by
  simp only [project,←mul_assoc,←map_mul,numerator,mul_inv_cancel_right,
    ←Finset.sum_mul,mobius_character_sum k χ nontrivial,zero_mul,mul_zero]

/-- A character of the input that sees a nontrivial element of the last
reduction kernel has zero correlation with every output numerator function
at this precision. This is the strict conductor step in the clock-pole proof. -/
theorem conductor_orthogonality (k : ℕ) {F : Type*} [Field F]
    (ψ : UnitAt k →* F) (f : UnitAt k → F) (u : UnitAt k)
    (kernel : (3 : RingAt k) * (u : RingAt k) = 3) (seen : ψ u≠1) :
    ∑ x, ψ x * f (numerator k x)=0 := by
  have stable (x : UnitAt k) : numerator k (u*x)=numerator k x := by
    apply Units.ext
    rw [numerator_val,numerator_val,Units.val_mul,←mul_assoc,kernel]
  apply eq_zero_of_mul_eq_self_left seen
  have perm := (Group.mulLeft_bijective u).sum_comp (fun z => ψ z*f (numerator k z))
  simpa only [Function.comp_apply,stable,map_mul,Finset.mul_sum,mul_assoc] using perm

#print axioms conductor_orthogonality
#print axioms mobius_val
#print axioms numerator_val
#print axioms mobius_character_sum
#print axioms project_twice
end SparseResonance
