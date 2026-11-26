import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith

namespace SixHour.CubicHeight

/-- Twice the valuation of one conjugate per unit of vertex valuation. -/
def weight (j : Fin 3) : ℤ := if j = 0 then 2 else -1

def delta (rotation j : Fin 3) : ℤ := weight j - weight (j + rotation)

/-- All nine embedding pairs, including the fixed root and both moving roots. -/
def jumpSum (a b : Fin 3) : ℤ :=
  ∑ i : Fin 3, ∑ j : Fin 3, |delta a i - delta b j|

theorem jumpSum_exact : ∀ a b : Fin 3, jumpSum a b =
    if a = 0 ∧ b = 0 then 0 else if a = 0 ∨ b = 0 then 18 else 24 := by
  decide

theorem internal_cost : (∑ i : Fin 3, ∑ j : Fin 3, |weight i - weight j|) = 12 := by
  decide

theorem endpoint_cost : (∑ i : Fin 3, |weight i|) = 4 := by
  decide

/-- A multiplier fixed by the chosen permutation disappears from the difference. -/
theorem fixed_multiplier_bound {ι : Type*} [Fintype ι] (π : Equiv.Perm ι)
    (u err c : ι → ℚ) (fixed : ∀ i, c (π i) = c i) :
    (∑ i, |u i - u (π i)|) ≤
      2 * (∑ i, |c i + u i + err i|) + 2 * (∑ i, |err i|) := by
  let v (i : ι) := c i + u i + err i
  have point (i : ι) : |u i - u (π i)| ≤
      |v i| + |v (π i)| + (|err i| + |err (π i)|) := by
    have h : u i - u (π i) = (v i - v (π i)) - (err i - err (π i)) := by
      dsimp [v]
      rw [fixed i]
      linarith
    rw [h]
    have h₁ := abs_sub (v i) (v (π i))
    have h₂ := abs_sub (err i) (err (π i))
    have h₃ := abs_sub (v i - v (π i)) (err i - err (π i))
    linarith
  have h := Finset.sum_le_sum (s := Finset.univ) (fun i _ => point i)
  simp only [Finset.sum_add_distrib] at h
  have hv : (∑ i, |v (π i)|) = ∑ i, |v i| := Equiv.sum_comp π (fun i => |v i|)
  have he : (∑ i, |err (π i)|) = ∑ i, |err i| := Equiv.sum_comp π (fun i => |err i|)
  rw [hv, he] at h
  change (∑ i, |u i - u (π i)|) ≤ 2 * (∑ i, |v i|) + 2 * (∑ i, |err i|)
  linarith

#print axioms jumpSum_exact
#print axioms internal_cost
#print axioms endpoint_cost
#print axioms fixed_multiplier_bound

end SixHour.CubicHeight

