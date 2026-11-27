import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.NormNum

/-! Every three-dimensional subspace in length 13 has a nonzero member of weight at most 7.
The local labels are the seven nonzero subsums of three generators. -/

namespace Collatz.ShortRelations

set_option autoImplicit false

/-- The seven nonempty subsets of three row selectors, evaluated at one coordinate. -/
def choices (a b c : Bool) : Fin 7 → Bool :=
  ![a, b, c, a ^^ b, a ^^ c, b ^^ c, a ^^ b ^^ c]

private theorem column_budget (a b c : Bool) :
    ∑ j : Fin 7, (if choices a b c j then 1 else 0 : ℕ) ≤ 4 := by
  decide +revert

/-- With 13 coordinates the seven row subsums cannot all have weight at least eight. -/
theorem short_relation (a b c : Fin 13 → Bool) :
    ∃ j : Fin 7, (∑ i : Fin 13, (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ)) ≤ 7 := by
  by_contra! h
  have lower : (∑ _j : Fin 7, (8 : ℕ)) ≤
      ∑ j : Fin 7, ∑ i : Fin 13, (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ) := by
    apply Finset.sum_le_sum
    intro j _
    exact h j
  have upper : (∑ i : Fin 13, ∑ j : Fin 7,
      (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ)) ≤ ∑ _i : Fin 13, (4 : ℕ) := by
    apply Finset.sum_le_sum
    intro i _
    exact column_budget _ _ _
  rw [Finset.sum_comm] at lower
  have hc := lower.trans upper
  norm_num at hc

/-- With independent generators every choice is nonzero. With even row kernels the short
member has weight 2, 4 or 6, exactly the three protected real/ternary grids. -/
theorem protected_weight (a b c : Fin 13 → Bool)
    (nonzero : ∀ j : Fin 7, 0 < ∑ i : Fin 13,
      (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ))
    (parity : ∀ j : Fin 7, Even (∑ i : Fin 13,
      (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ))) :
    ∃ j : Fin 7, let w := ∑ i : Fin 13,
      (if choices (a i) (b i) (c i) j then 1 else 0 : ℕ); w = 2 ∨ w = 4 ∨ w = 6 := by
  obtain ⟨j, hj⟩ := short_relation a b c
  refine ⟨j, ?_⟩
  have hp := nonzero j
  obtain ⟨k, hk⟩ := parity j
  omega

#print axioms short_relation
#print axioms protected_weight

end Collatz.ShortRelations
