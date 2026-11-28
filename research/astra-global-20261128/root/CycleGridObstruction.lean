import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Ring.Int.Parity
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! The ordinary odd-integer grid never zeros a cyclic Green characteristic.
This finite statement uses only the native killing weights and parity. The
infinite-operator spectral classification is a separately stated written proof.
-/
set_option autoImplicit false

namespace Collatz.Global.CycleGridObstruction

variable {I : Type*}

private theorem odd_finset_prod (s : Finset I) (x : I → ℤ)
    (hx : ∀ i ∈ s, Odd (x i)) : Odd (∏ i ∈ s, x i) := by
  classical
  revert hx
  refine Finset.induction_on s ?_ ?_
  · intro _
    simp
  · intro i s hi ih hx
    rw [Finset.prod_insert hi]
    exact (hx i (by simp)).mul (ih fun j hj => hx j (by simp [hj]))

/-- A nonempty product of odd differences cannot equal the product of the odd sites. -/
theorem odd_difference_product_ne (s : Finset I) (hs : s.Nonempty)
    (x : I → ℤ) (y : ℤ) (hx : ∀ i ∈ s, Odd (x i)) (hy : Odd y) :
    (∏ i ∈ s, (x i - y)) ≠ ∏ i ∈ s, x i := by
  classical
  obtain ⟨i, hi⟩ := hs
  have he : Even (∏ j ∈ s, (x j - y)) :=
    ((hx i hi).sub_odd hy).trans_dvd (Finset.dvd_prod_of_mem _ hi)
  intro h
  rw [h] at he
  exact (Int.not_even_iff_odd.mpr (odd_finset_prod s x hx)) he

/-- Native probability of killing at an ordinary odd input. -/
def grid (x : ℤ) : ℚ := 1 / (3 * (x : ℚ) + 1)

/-- The cyclic characteristic after clearing all native site denominators. -/
def clearedCharacteristic (s : Finset I) (x : I → ℤ) (z : ℚ) : ℚ :=
    (∏ i ∈ s, ((3 * (x i : ℚ) + 1) * z - 1)) -
      3 ^ s.card * (∏ i ∈ s, (x i : ℚ)) * z ^ s.card

/-- The numerator of the characteristic polynomial of a native cyclic Green block. -/
def nativeCharacteristic (s : Finset I) (x : I → ℤ) (z : ℚ) : ℚ :=
    (∏ i ∈ s, (z - grid (x i))) -
      (∏ i ∈ s, (3 * (x i : ℚ) / (3 * (x i : ℚ) + 1))) * z ^ s.card

/-- Multiplication by the original positive site denominators clears the native polynomial. -/
theorem clear_native_characteristic (s : Finset I) (x : I → ℤ) (z : ℚ)
    (hx : ∀ i ∈ s, 0 < x i) :
    clearedCharacteristic s x z =
      (∏ i ∈ s, (3 * (x i : ℚ) + 1)) * nativeCharacteristic s x z := by
  classical
  have hden (i : I) (hi : i ∈ s) : 3 * (x i : ℚ) + 1 ≠ 0 := by
    have hpos : (0 : ℚ) < (x i : ℚ) := by exact_mod_cast hx i hi
    positivity
  have hleft : (∏ i ∈ s, ((3 * (x i : ℚ) + 1) * z - 1)) =
      (∏ i ∈ s, (3 * (x i : ℚ) + 1)) * (∏ i ∈ s, (z - grid (x i))) := by
    rw [← Finset.prod_mul_distrib]
    apply Finset.prod_congr rfl
    intro i hi
    unfold grid
    field_simp [hden i hi]
  have hright : (∏ i ∈ s, (3 * (x i : ℚ) + 1)) *
      (∏ i ∈ s, (3 * (x i : ℚ) / (3 * (x i : ℚ) + 1))) =
        3 ^ s.card * ∏ i ∈ s, (x i : ℚ) := by
    rw [← Finset.prod_mul_distrib]
    calc
      _ = ∏ i ∈ s, (3 * (x i : ℚ)) := by
        apply Finset.prod_congr rfl
        intro i hi
        field_simp [hden i hi]
      _ = _ := by rw [Finset.prod_mul_distrib, Finset.prod_const]
  unfold clearedCharacteristic nativeCharacteristic
  rw [hleft, mul_sub, ← mul_assoc, hright]

/-- At a native grid value the entire characteristic reduces to one integer parity test. -/
theorem grid_characteristic_identity (s : Finset I) (x : I → ℤ) (y : ℤ)
    (hy : 3 * (y : ℚ) + 1 ≠ 0) :
    clearedCharacteristic s x (grid y) =
      (3 * grid y) ^ s.card *
        (((∏ i ∈ s, (x i - y)) - ∏ i ∈ s, x i : ℤ) : ℚ) := by
  classical
  have he (i : I) : (3 * (x i : ℚ) + 1) * grid y - 1 =
      (3 * grid y) * ((x i : ℚ) - (y : ℚ)) := by
    unfold grid
    field_simp
    ring
  unfold clearedCharacteristic
  simp_rw [he]
  rw [Finset.prod_mul_distrib, Finset.prod_const]
  simp only [Int.cast_sub, Int.cast_prod, mul_pow]
  ring

/-- Every positive odd grid point is excluded from every nonempty odd-site cycle polynomial. -/
theorem odd_grid_not_characteristic_zero (s : Finset I) (hs : s.Nonempty)
    (x : I → ℤ) (y : ℤ) (hx : ∀ i ∈ s, Odd (x i))
    (hy : Odd y) (hypos : 0 < y) :
    clearedCharacteristic s x (grid y) ≠ 0 := by
  have hden : 3 * (y : ℚ) + 1 ≠ 0 := by positivity
  rw [grid_characteristic_identity s x y hden]
  apply mul_ne_zero
  · apply pow_ne_zero
    exact mul_ne_zero (by norm_num) (one_div_ne_zero hden)
  · exact_mod_cast sub_ne_zero.mpr (odd_difference_product_ne s hs x y hx hy)

/-- The actual native-weight cycle characteristic excludes every positive odd physical grid point. -/
theorem odd_grid_not_native_zero (s : Finset I) (hs : s.Nonempty)
    (x : I → ℤ) (y : ℤ) (hx : ∀ i ∈ s, Odd (x i))
    (hxpos : ∀ i ∈ s, 0 < x i) (hy : Odd y) (hypos : 0 < y) :
    nativeCharacteristic s x (grid y) ≠ 0 := by
  intro hzero
  have hne := odd_grid_not_characteristic_zero s hs x y hx hy hypos
  apply hne
  rw [clear_native_characteristic s x (grid y) hxpos, hzero, mul_zero]

end Collatz.Global.CycleGridObstruction

#print axioms Collatz.Global.CycleGridObstruction.odd_difference_product_ne
#print axioms Collatz.Global.CycleGridObstruction.grid_characteristic_identity
#print axioms Collatz.Global.CycleGridObstruction.odd_grid_not_characteristic_zero
#print axioms Collatz.Global.CycleGridObstruction.clear_native_characteristic
#print axioms Collatz.Global.CycleGridObstruction.odd_grid_not_native_zero
