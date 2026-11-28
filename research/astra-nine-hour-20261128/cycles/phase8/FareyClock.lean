import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Ring

/-! Finite comparison of two permutation orbits by integer crossing counts. -/

namespace Collatz.FareyClock

open Finset

/-- Summed comparison increments cancel the two cyclic phase permutations. -/
theorem sum_crossings {I J : Type*} [Fintype I] [Fintype J]
    (s : Equiv.Perm I) (t : Equiv.Perm J)
    (u : I → ℤ) (v : J → ℤ) (L : I → J → ℤ) :
    (∑ i, ∑ j, (u i - v j + L (s i) (t j) - L i j)) =
    (∑ i, u i) * (Fintype.card J : ℤ) - (∑ j, v j) * (Fintype.card I : ℤ) := by
  have h : (∑ i, ∑ j, L (s i) (t j)) = ∑ i, ∑ j, L i j := by
    simp only [Equiv.sum_comp t]
    exact Equiv.sum_comp s (fun i => ∑ j, L i j)
  simp only [sum_sub_distrib, sum_add_distrib, sum_const, card_univ, nsmul_eq_mul,
    ← mul_sum, h]
  ring

/-- If the total crossing number is positive, and at most one distinguished
pair can contribute one while every other pair contributes at most zero,
the two integer clocks have determinant one. -/
theorem determinant_one {I J : Type*} [Fintype I] [Fintype J]
    (s : Equiv.Perm I) (t : Equiv.Perm J)
    (u : I → ℤ) (v : J → ℤ) (L : I → J → ℤ)
    (i₀ : I) (j₀ : J) [DecidableEq I] [DecidableEq J]
    (cap : ∀ i j, u i - v j + L (s i) (t j) - L i j ≤
      if i = i₀ then (if j = j₀ then 1 else 0) else 0)
    (positive : 0 < (∑ i, u i) * (Fintype.card J : ℤ) -
      (∑ j, v j) * (Fintype.card I : ℤ)) :
    (∑ i, u i) * (Fintype.card J : ℤ) - (∑ j, v j) * (Fintype.card I : ℤ) = 1 := by
  have total := sum_crossings s t u v L
  have bound : (∑ i, ∑ j, (u i - v j + L (s i) (t j) - L i j)) ≤
      ∑ i : I, ∑ j : J, (if i = i₀ then (if j = j₀ then (1 : ℤ) else 0) else 0) :=
    sum_le_sum fun i _ => sum_le_sum fun j _ => cap i j
  rw [total] at bound
  simp [sum_ite_irrel] at bound
  omega

end Collatz.FareyClock
