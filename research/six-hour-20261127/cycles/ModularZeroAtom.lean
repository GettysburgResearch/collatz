import Mathlib.Algebra.Group.Equiv.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.ZMod.Basic

/-! Zero-shift domination for finite additive-group correlation and literal ordered fourfold counts. -/

namespace ModularZeroAtom

variable {G : Type*} [AddGroup G] [Fintype G]

/-- A finite autocorrelation attains its maximum at zero. The weights may be signed. -/
theorem correlation_le_zero {R : Type*} [CommSemiring R] [LinearOrder R]
    [IsStrictOrderedRing R] [ExistsAddOfLE R] (weight : G → R) (shift : G) :
    ∑ x, weight x * weight (x + shift) ≤ ∑ x, (weight x) ^ 2 := by
  have translate : (∑ x, (weight (x + shift)) ^ 2) = ∑ x, (weight x) ^ 2 :=
    Equiv.sum_comp (Equiv.addRight shift) (fun x => (weight x) ^ 2)
  apply (mul_le_mul_iff_right₀ (zero_lt_two' R)).mp
  calc
    2 * ∑ x, weight x * weight (x + shift) =
        ∑ x, 2 * weight x * weight (x + shift) := by
          simp only [Finset.mul_sum, mul_assoc]
    _ ≤ ∑ x, ((weight x) ^ 2 + (weight (x + shift)) ^ 2) :=
      Finset.sum_le_sum fun x _ => two_mul_le_add_sq _ _
    _ = 2 * ∑ x, (weight x) ^ 2 := by
      rw [Finset.sum_add_distrib, translate, two_mul]

theorem nat_correlation_le_zero (weight : G → ℕ) (shift : G) :
    ∑ x, weight x * weight (x + shift) ≤ ∑ x, (weight x) ^ 2 :=
  correlation_le_zero weight shift

theorem rat_correlation_le_zero (weight : G → ℚ) (shift : G) :
    ∑ x, weight x * weight (x + shift) ≤ ∑ x, (weight x) ^ 2 :=
  correlation_le_zero weight shift

variable {I : Type*} [Fintype I] [DecidableEq G]

/-- Number of source labels with a given group value. Repeated values count separately. -/
def multiplicity (value : I → G) (x : G) : ℕ :=
  (Finset.univ.filter fun i => value i = x).card

/-- Number of ordered source pairs whose second label is the first label translated by shift. -/
def orderedAtom (value : I → G) (shift : G) : ℕ :=
  (Finset.univ.filter fun p : I × I => value p.2 = value p.1 + shift).card

theorem orderedAtom_eq_correlation (value : I → G) (shift : G) :
    orderedAtom value shift = ∑ x, multiplicity value x * multiplicity value (x + shift) := by
  classical
  calc
    orderedAtom value shift = ∑ i, multiplicity value (value i + shift) := by
      simp only [orderedAtom, multiplicity, Finset.card_filter, Fintype.sum_prod_type]
    _ = ∑ x, ∑ i ∈ Finset.univ.filter (fun i => value i = x),
          multiplicity value (value i + shift) :=
      (Finset.sum_fiberwise Finset.univ value (fun i => multiplicity value (value i + shift))).symm
    _ = ∑ x, multiplicity value x * multiplicity value (x + shift) := by
      apply Finset.sum_congr rfl
      intro x _
      calc
        _ = ∑ i ∈ Finset.univ.filter (fun i => value i = x), multiplicity value (x + shift) :=
          Finset.sum_congr rfl fun i hi => by rw [(Finset.mem_filter.mp hi).2]
        _ = _ := by simp [multiplicity]

theorem orderedAtom_le_zero (value : I → G) (shift : G) :
    orderedAtom value shift ≤ orderedAtom value 0 := by
  simpa only [orderedAtom_eq_correlation, add_zero, pow_two] using
    nat_correlation_le_zero (multiplicity value) shift

/-- Ordered quadruples with the second pair sum equal to the first pair sum plus a group shift. -/
def fourfoldAtom (value : I → G) (shift : G) : ℕ :=
  orderedAtom (fun p : I × I => value p.1 + value p.2) shift

theorem fourfoldAtom_le_zero (value : I → G) (shift : G) :
    fourfoldAtom value shift ≤ fourfoldAtom value 0 :=
  orderedAtom_le_zero (fun p : I × I => value p.1 + value p.2) shift

/-- Modulo a power of two, an arbitrary signed incoming carry requires the second pair sum
to be the first pair sum plus the ternary-scaled carry. -/
theorem fourfoldAtom_inherited_carry (bits steps : ℕ) (wordValue : I → ℤ) (carry : ℤ) :
    fourfoldAtom (fun i => (wordValue i : ZMod (2 ^ bits)))
        ((3 : ZMod (2 ^ bits)) ^ steps * (carry : ZMod (2 ^ bits))) ≤
      fourfoldAtom (fun i => (wordValue i : ZMod (2 ^ bits))) 0 :=
  fourfoldAtom_le_zero _ _

end ModularZeroAtom

#print axioms ModularZeroAtom.correlation_le_zero
#print axioms ModularZeroAtom.nat_correlation_le_zero
#print axioms ModularZeroAtom.rat_correlation_le_zero
#print axioms ModularZeroAtom.orderedAtom_eq_correlation
#print axioms ModularZeroAtom.orderedAtom_le_zero
#print axioms ModularZeroAtom.fourfoldAtom_le_zero

#print axioms ModularZeroAtom.fourfoldAtom_inherited_carry
