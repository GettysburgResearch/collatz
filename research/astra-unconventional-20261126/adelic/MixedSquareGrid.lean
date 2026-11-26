import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Ternary separation of the first three polynomial parts of a square-root expansion.
The coefficients are the elementary symmetric functions in the cleared actual rows. -/

namespace Collatz.MixedSquareGrid

open Polynomial

set_option autoImplicit false

variable {ι : Type*} [Fintype ι]

noncomputable def elementary (w : ι → ℤ) : ℤ[X] := ∏ i, (1 + C (w i) * X)

/-- The unique last ternary unit leaves a single linear factor after reduction. -/
theorem single_factor (w : ι → ℤ) (j : ι)
    (other : ∀ i, i ≠ j → (w i : ZMod 3) = 0) :
    (elementary w).map (Int.castRingHom (ZMod 3)) = 1 + C (w j : ZMod 3) * X := by
  simp only [elementary, Polynomial.map_prod, Polynomial.map_add, Polynomial.map_one,
    Polynomial.map_mul, Polynomial.map_C, Polynomial.map_X, Int.coe_castRingHom]
  apply Finset.prod_eq_single j
  · intro i _ hij
    simp [other i hij]
  · simp

/-- A second factor is divisible by three, so the root of the whole product also vanishes there. -/
theorem square_root_vanishes (w : ι → ℤ) {s : ℤ} (i : ι) (hi : (w i : ZMod 3) = 0)
    (hs : s ^ 2 = ∏ v, w v) : (s : ZMod 3) = 0 := by
  have hz := congrArg (Int.castRingHom (ZMod 3)) hs
  simp only [map_pow, map_prod, Int.coe_castRingHom] at hz
  rw [Finset.prod_eq_zero (Finset.mem_univ i) hi] at hz
  exact (pow_eq_zero_iff (by decide : 2 ≠ 0)).mp hz

/-- These grid numerators are twice, eight times and sixteen times the degree 1, 2 and 3
homogeneous terms of `sqrt(prod (1 + w_i X))`, respectively. -/
def grid1 (p : ℤ[X]) : ℤ := p.coeff 1
def grid2 (p : ℤ[X]) : ℤ := 4 * p.coeff 2 - (p.coeff 1)^2
def grid3 (p : ℤ[X]) : ℤ := 8 * p.coeff 3 - 4 * p.coeff 1 * p.coeff 2 + (p.coeff 1)^3

theorem ternary_grid_separation (w : ι → ℤ) {s : ℤ} (i j : ι) (hne : i ≠ j)
    (unit : (w j : ZMod 3) ≠ 0) (other : ∀ v, v ≠ j → (w v : ZMod 3) = 0)
    (hs : s ^ 2 = ∏ v, w v) :
    2 * s ≠ grid1 (elementary w) ∧ 8 * s ≠ grid2 (elementary w) ∧
    16 * s ≠ grid3 (elementary w) := by
  have hz := square_root_vanishes w i (other i hne) hs
  have hm := single_factor w j other
  rw [Polynomial.C_mul_X_eq_monomial] at hm
  have hc (k : ℕ) := congrArg (fun p : (ZMod 3)[X] => p.coeff k) hm
  have hc1 : ((elementary w).coeff 1 : ZMod 3) = w j := by simpa [Polynomial.coeff_one, Polynomial.coeff_monomial] using hc 1
  have hc2 : ((elementary w).coeff 2 : ZMod 3) = 0 := by simpa [Polynomial.coeff_one, Polynomial.coeff_monomial] using hc 2
  have hc3 : ((elementary w).coeff 3 : ZMod 3) = 0 := by simpa [Polynomial.coeff_one, Polynomial.coeff_monomial] using hc 3
  constructor
  · intro he
    have h := congrArg (Int.castRingHom (ZMod 3)) he
    simp [grid1, hz, hc1] at h
    exact unit h.symm
  constructor
  · intro he
    have h := congrArg (Int.castRingHom (ZMod 3)) he
    simp [grid2, hz, hc1, hc2, unit] at h
  · intro he
    have h := congrArg (Int.castRingHom (ZMod 3)) he
    simp [grid3, hz, hc1, hc2, hc3] at h
    exact pow_ne_zero 3 unit h.symm

omit [Fintype ι] in
/-- In a physical ascending ternary-index list, clearing the greatest denominator makes all
strictly earlier rows divisible by 3. The leading row keeps its unit numerator. -/
theorem shifted_grid {w : ι → ℤ} {j : ι} {exponent : ι → ℕ} {u : ι → ℤ}
    (hj : (u j : ZMod 3) ≠ 0) (h : ∀ i, w i = 3 ^ (exponent j - exponent i) * u i)
    (hmax : ∀ i, i ≠ j → exponent i < exponent j) :
    (w j : ZMod 3) ≠ 0 ∧ ∀ i, i ≠ j → (w i : ZMod 3) = 0 := by
  constructor
  · simpa [h] using hj
  · intro i hij
    have hp : exponent j - exponent i ≠ 0 := by have := hmax i hij; omega
    rw [h]
    push_cast
    have h3 : (3 : ZMod 3) = 0 := by decide
    rw [h3, zero_pow hp, zero_mul]

#print axioms single_factor
#print axioms square_root_vanishes
#print axioms ternary_grid_separation
#print axioms shifted_grid

end Collatz.MixedSquareGrid
