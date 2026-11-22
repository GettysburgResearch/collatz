module

public import Mathlib.NumberTheory.Multiplicity
public import Mathlib.Data.Nat.GCD.Basic
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

@[expose] public section

/-!
# Literal-prefix sibling lifts

An accelerated odd word with `s` odd steps and total binary clock `A`
has an affine equation `2^A*q = 3^s*p + C`.  Replacing its endpoint by
the ordinary odd sibling `4^j*q + (4^j-1)/3` and retaining the entire
word is arithmetically possible exactly when `3^s` divides `j`.

This module checks the unrestricted-depth divisibility calculation and
the exact natural-number lift.  Its companion note checks actual gap
legality and the sum of original inverse-square source weights.  No
bound on the canonical potential of a lifted source is asserted.
-/

namespace CollatzSiblingLift

local instance : Fact (Nat.Prime 3) := ⟨by decide⟩

def sibling (j q : Nat) : Nat := 4^j*q + (4^j-1)/3

def liftQuotient (s j : Nat) : Nat := (4^j-1)/3^(s+1)

def liftedSource (s A p q j : Nat) : Nat :=
  p + 2^A*(3*q+1)*liftQuotient s j

theorem four_pow_sub_one_valuation (j : Nat) (hj : j ≠ 0) :
    padicValNat 3 (4^j-1) = 1 + padicValNat 3 j := by
  simpa using padicValNat.pow_sub_pow (p := 3) (x := 4) (y := 1)
    (by decide : Odd 3) (by decide) (by decide) (by decide) hj

theorem sibling_index_divisibility (s j : Nat) :
    3^(s+1) ∣ 4^j-1 ↔ 3^s ∣ j := by
  by_cases hj : j = 0
  · simp [hj]
  have hpow : 1 < 4^j := by
    simpa using Nat.pow_lt_pow_left (by decide : 1 < 4) hj
  rw [padicValNat_dvd_iff_le (Nat.sub_ne_zero_of_lt hpow),
    four_pow_sub_one_valuation j hj, padicValNat_dvd_iff_le hj]
  omega

theorem affine_correction_coprime (s A C : Nat) :
    Nat.Coprime (3^(s+1)) (3*C+2^A) := by
  apply Nat.Coprime.pow_left
  simpa using (by decide : Nat.Coprime 3 2).pow_right A

theorem affine_numerator_divisibility (s A C j : Nat) :
    3^(s+1) ∣ (4^j-1)*(3*C+2^A) ↔ 3^s ∣ j := by
  rw [(affine_correction_coprime s A C).dvd_mul_right]
  exact sibling_index_divisibility s j

theorem sibling_affine (j q : Nat) :
    3*sibling j q+1 = 4^j*(3*q+1) := by
  have hd : 3 ∣ 4^j-1 := by
    simpa using (sibling_index_divisibility 0 j).2 (one_dvd j)
  have hm : 3*((4^j-1)/3) = 4^j-1 := Nat.mul_div_cancel' hd
  have hp : 0 < 4^j := by positivity
  have hm' : 3*((4^j-1)/3)+1 = 4^j := by omega
  unfold sibling
  nlinarith only [hm']

theorem lift_quotient_exact (s j : Nat) (hj : 3^s ∣ j) :
    3^(s+1)*liftQuotient s j = 4^j-1 := by
  exact Nat.mul_div_cancel' ((sibling_index_divisibility s j).2 hj)

theorem lifted_source_expansion (s A p q C j : Nat)
    (hbase : 2^A*q = 3^s*p+C) (hj : 3^s ∣ j) :
    liftedSource s A p q j =
      4^j*p + liftQuotient s j*(3*C+2^A) := by
  have hquot := lift_quotient_exact s j hj
  have hp : 0 < 4^j := by positivity
  have hpow : 3^(s+1) = 3^s*3 := pow_succ 3 s
  have he : 3^(s+1)*liftQuotient s j+1 = 4^j := by omega
  rw [liftedSource, ← he, hpow]
  calc
    p + 2^A*(3*q+1)*liftQuotient s j =
        p + 3*liftQuotient s j*(2^A*q) + 2^A*liftQuotient s j := by ring
    _ = p + 3*liftQuotient s j*(3^s*p+C) + 2^A*liftQuotient s j := by rw [hbase]
    _ = _ := by ring

theorem lifted_source_affine (s A p q C j : Nat)
    (hbase : 2^A*q = 3^s*p+C) (hj : 3^s ∣ j) :
    2^A*sibling j q = 3^s*liftedSource s A p q j+C := by
  have hquot := lift_quotient_exact s j hj
  have hsib := sibling_affine j q
  have hp : 0 < 4^j := by positivity
  have he : 3^(s+1)*liftQuotient s j+1 = 4^j := by omega
  have hx' : sibling j q = q+3^s*liftQuotient s j*(3*q+1) := by
    rw [← he, pow_succ] at hsib
    nlinarith only [hsib]
  rw [hx', liftedSource]
  calc
    2^A*(q+3^s*liftQuotient s j*(3*q+1)) =
      2^A*q+3^s*(2^A*(3*q+1)*liftQuotient s j) := by ring
    _ = 3^s*p+C+3^s*(2^A*(3*q+1)*liftQuotient s j) := by rw [hbase]
    _ = _ := by ring

theorem lifted_source_height (s A p q C j : Nat)
    (hbase : 2^A*q = 3^s*p+C) (hj : 3^s ∣ j) :
    4^j*p ≤ liftedSource s A p q j := by
  rw [lifted_source_expansion s A p q C j hbase hj]
  omega

theorem first_nonzero_lift_height (s A p q C j : Nat)
    (hbase : 2^A*q = 3^s*p+C) (hj : 3^s ∣ j) (hj0 : 0 < j) :
    4^(3^s)*p ≤ liftedSource s A p q j := by
  have he : 3^s ≤ j := Nat.le_of_dvd hj0 hj
  have hp : 4^(3^s) ≤ 4^j := Nat.pow_le_pow_right (by decide) he
  exact (Nat.mul_le_mul_right p hp).trans (lifted_source_height s A p q C j hbase hj)

end CollatzSiblingLift

#print axioms CollatzSiblingLift.four_pow_sub_one_valuation
#print axioms CollatzSiblingLift.sibling_index_divisibility
#print axioms CollatzSiblingLift.affine_correction_coprime
#print axioms CollatzSiblingLift.affine_numerator_divisibility
#print axioms CollatzSiblingLift.sibling_affine
#print axioms CollatzSiblingLift.lift_quotient_exact
#print axioms CollatzSiblingLift.lifted_source_expansion
#print axioms CollatzSiblingLift.lifted_source_affine
#print axioms CollatzSiblingLift.lifted_source_height
#print axioms CollatzSiblingLift.first_nonzero_lift_height
