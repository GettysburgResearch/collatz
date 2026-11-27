import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite core of the completed-word cell and prescribed-pair argument. -/
namespace Collatz.PairedCellPressure
open Finset
open scoped BigOperators

/-- A lower total and a uniform cap force many cells above threshold. -/
theorem heavy_cells {ι : Type*} [DecidableEq ι] (cells : Finset ι)
    (mass : ι → ℕ) (threshold cap : ℕ)
    (upper : ∀ r ∈ cells, mass r ≤ cap)
    (total : 2 * (cells.card * threshold) ≤ ∑ r ∈ cells, mass r) :
    cells.card * threshold ≤ (cells.filter (fun r => threshold ≤ mass r)).card * cap := by
  let heavy := cells.filter (fun r => threshold ≤ mass r)
  have each (r : ι) (hr : r ∈ cells) :
      mass r ≤ threshold + (if r ∈ heavy then cap else 0) := by
    by_cases hh : r ∈ heavy
    · simp [hh]
      exact le_trans (upper r hr) (Nat.le_add_left _ _)
    · have hl : ¬ threshold ≤ mass r := by
        intro ht
        exact hh (Finset.mem_filter.mpr ⟨hr, ht⟩)
      simp [hh]
      omega
  have hhsub : heavy ⊆ cells := Finset.filter_subset _ _
  have hff : cells.filter (fun r => r ∈ heavy) = heavy := by
    ext r
    simp only [mem_filter]
    exact ⟨And.right, fun hr => ⟨hhsub hr, hr⟩⟩
  have major := Finset.sum_le_sum each
  have val : (∑ r ∈ cells, (threshold + if r ∈ heavy then cap else 0)) =
      cells.card * threshold + heavy.card * cap := by
    rw [Finset.sum_add_distrib, ← Finset.sum_filter, hff]
    simp
  rw [val] at major
  change cells.card * threshold ≤ heavy.card * cap
  omega

/-- Compose the exact positive-integer affine rows, including both carries. -/
theorem prescribed_row (x q middle carry e p h : ℕ)
    (first : 2 ^ e * middle = 3 ^ p * x + carry)
    (last : 2 ^ h * q = 9 * middle + 7) :
    2 ^ (e+h) * q = 3 ^ (p+2) * x + 9 * carry + 7 * 2^e := by
  calc
    2 ^ (e+h) * q = 2^e * (2^h*q) := by rw [pow_add, Nat.mul_assoc]
    _ = 9 * (2^e * middle) + 7 * 2^e := by rw [last]; ring
    _ = 3 ^ (p+2) * x + 9 * carry + 7 * 2^e := by rw [first, pow_add]; ring

#print axioms heavy_cells
#print axioms prescribed_row
end Collatz.PairedCellPressure
