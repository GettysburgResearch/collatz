import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
An exact obstruction to a globally decreasing completely additive potential
for the ordinary accelerated Collatz map. This is not a Collatz cycle and
does not rule out potentials required to work only above an arbitrary floor.

`OddEdge n m` includes the full odd-to-odd equation, a positive power of two,
and odd positive endpoints. Hence its exponent is the exact removed power.
No probabilistic, rational-cycle, or formal-word surrogate is used.
-/

namespace CollatzReassessment.PrimePotentialCirculation

def OddEdge (n m : ℕ) : Prop :=
  0 < n ∧ n % 2 = 1 ∧ 0 < m ∧ m % 2 = 1 ∧
    ∃ a : ℕ, 0 < a ∧ 3 * n + 1 = 2 ^ a * m

def CompletelyAdditive (F : ℕ → ℝ) : Prop :=
  ∀ a b : ℕ, 0 < a → 0 < b → F (a * b) = F a + F b

theorem edge_25_19 : OddEdge 25 19 := by
  exact ⟨by decide, by decide, by decide, by decide,
    2, by decide, by decide⟩

theorem edge_19_29 : OddEdge 19 29 := by
  exact ⟨by decide, by decide, by decide, by decide,
    1, by decide, by decide⟩

theorem edge_29_11 : OddEdge 29 11 := by
  exact ⟨by decide, by decide, by decide, by decide,
    3, by decide, by decide⟩

theorem edge_55_83 : OddEdge 55 83 := by
  exact ⟨by decide, by decide, by decide, by decide,
    1, by decide, by decide⟩

theorem edge_83_125 : OddEdge 83 125 := by
  exact ⟨by decide, by decide, by decide, by decide,
    1, by decide, by decide⟩

/-- The exact multiplicative balance of the two open paths' endpoints. -/
theorem endpoint_product : (25 : ℕ) * 55 = 11 * 125 := by decide

/-- All five actual integer edge equations obey the full product identity. -/
theorem ordinary_product_balance :
    (3 * 25 + 1) * (3 * 19 + 1) * (3 * 29 + 1) *
      (3 * 55 + 1) * (3 * 83 + 1) =
      2 ^ 8 * (25 * 19 * 29 * 55 * 83 : ℕ) := by decide

theorem additive_endpoint_balance (F : ℕ → ℝ)
    (hF : CompletelyAdditive F) :
    F 25 + F 55 = F 11 + F 125 := by
  have left := hF 25 55 (by decide) (by decide)
  have right := hF 11 125 (by decide) (by decide)
  norm_num at left right
  linarith

/-- The sum of the five exact edge changes is zero for arbitrary prime weights. -/
theorem additive_edge_balance (F : ℕ → ℝ)
    (hF : CompletelyAdditive F) :
    (F 19 - F 25) + (F 29 - F 19) + (F 11 - F 29) +
      (F 83 - F 55) + (F 125 - F 83) = 0 := by
  have balance := additive_endpoint_balance F hF
  linarith

/-- Weak decrease on these five genuine edges forces equality on every edge. -/
theorem five_weak_edges_are_flat (F : ℕ → ℝ)
    (hF : CompletelyAdditive F)
    (h25 : F 19 ≤ F 25) (h19 : F 29 ≤ F 19)
    (h29 : F 11 ≤ F 29) (h55 : F 83 ≤ F 55)
    (h83 : F 125 ≤ F 83) :
    F 19 = F 25 ∧ F 29 = F 19 ∧ F 11 = F 29 ∧
      F 83 = F 55 ∧ F 125 = F 83 := by
  have balance := additive_endpoint_balance F hF
  exact ⟨by linarith, by linarith, by linarith,
    by linarith, by linarith⟩

/-- Even a strict order required only on sources at least 19 is impossible.
The quantifier includes every odd source at that fixed floor, not every floor. -/
theorem no_global_strict_additive_potential (F : ℕ → ℝ)
    (hF : CompletelyAdditive F) :
    ¬ (∀ n m : ℕ, 19 ≤ n → n % 3 ≠ 0 → OddEdge n m → F m < F n) := by
  intro decrease
  have h25 := decrease 25 19 (by decide) (by decide) edge_25_19
  have h19 := decrease 19 29 (by decide) (by decide) edge_19_29
  have h29 := decrease 29 11 (by decide) (by decide) edge_29_11
  have h55 := decrease 55 83 (by decide) (by decide) edge_55_83
  have h83 := decrease 83 125 (by decide) (by decide) edge_83_125
  have balance := additive_endpoint_balance F hF
  linarith

/-- The fixed two-word product equation is a nonzero divisor equation.
This prevents extrapolating the displayed control to an arbitrary floor. -/
theorem fixed_word_hyperbola (x y : ℤ) :
    (27 * x + 29) * (9 * y + 5) = 256 * x * y ↔
      (13 * x - 261) * (13 * y - 135) = 37120 := by
  constructor <;> intro h <;> nlinarith [h]

end CollatzReassessment.PrimePotentialCirculation
