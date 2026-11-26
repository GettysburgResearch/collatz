import Mathlib.Tactic

/-! One fair binary update of the three Collatz affine slope grades. -/

namespace CollatzTripleGrades

/-- The two adjacent gaps in nondecreasing order, multiplied together. -/
def sortedProduct (x y z : ℤ) : ℤ :=
  if x ≤ y then
    if y ≤ z then (y - x) * (z - y)
    else if x ≤ z then (z - x) * (y - z)
    else (x - z) * (y - x)
  else
    if x ≤ z then (x - y) * (z - x)
    else if y ≤ z then (z - y) * (x - z)
    else (y - z) * (x - y)

private theorem sortedProduct_of_le {x y z : ℤ} (h₁ : x ≤ y) (h₂ : y ≤ z) :
    sortedProduct x y z = (y - x) * (z - y) := by simp [sortedProduct, h₁, h₂]

/-- The two possible updates are bitwise complements. Their total product
loses two units precisely when only the middle arm has different parity. -/
theorem ordered_fair_step {x y z a b c : ℤ} (h₁ : x < y) (h₂ : y < z)
    (ha : a = 0 ∨ a = 1) (hb : b = 0 ∨ b = 1) (hc : c = 0 ∨ c = 1) :
    sortedProduct (x+a) (y+b) (z+c) +
    sortedProduct (x+(1-a)) (y+(1-b)) (z+(1-c)) =
    2 * (y-x) * (z-y) - (if a = c ∧ a ≠ b then 2 else 0) := by
  rw [sortedProduct_of_le (by omega) (by omega),
      sortedProduct_of_le (by omega) (by omega)]
  rcases ha with rfl | rfl <;> rcases hb with rfl | rfl <;>
    rcases hc with rfl | rfl <;> norm_num <;> ring

/-- Resolving an old tie can create at most one times the new spread. -/
theorem tie_step_le {x y z a b c : ℤ} (h₁ : x ≤ y) (h₂ : y ≤ z)
    (htie : x = y ∨ y = z) (ha : a = 0 ∨ a = 1) (hb : b = 0 ∨ b = 1)
    (hc : c = 0 ∨ c = 1) :
    sortedProduct (x+a) (y+b) (z+c) ≤ z-x+1 := by
  rcases htie with rfl | rfl <;> rcases ha with rfl | rfl <;>
    rcases hb with rfl | rfl <;> rcases hc with rfl | rfl <;>
    unfold sortedProduct <;> split_ifs <;> nlinarith

/-- Adjacent mixed steps count the isolated middle parity twice, after
subtracting the mixed steps of the two outer arms. -/
theorem mixed_middle_identity {a b c : ℤ} (ha : a = 0 ∨ a = 1)
    (hb : b = 0 ∨ b = 1) (hc : c = 0 ∨ c = 1) :
    2 * (if a = c ∧ a ≠ b then (1 : ℤ) else 0) =
      (if a ≠ b then 1 else 0) + (if b ≠ c then 1 else 0) -
      (if a ≠ c then 1 else 0) := by
  rcases ha with rfl | rfl <;> rcases hb with rfl | rfl <;>
    rcases hc with rfl | rfl <;> decide

end CollatzTripleGrades
