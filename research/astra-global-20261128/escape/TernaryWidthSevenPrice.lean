import Mathlib.Data.List.Basic
import Mathlib.Tactic.NormNum

/-! Exact finite cycle and price on the ternary width-seven leading-cell
graph. Leading mantissas run from 243 through 728. Each ideal even edge
starts at the rounded half. Below 486 there is one additional higher
neighbor. The ideal odd graph has exactly the same mantissa transitions and
adds one to the length change. -/

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 10000
set_option maxHeartbeats 4000000

namespace Collatz.TernaryWidthSevenPrice

def down (h : ℕ) : ℕ := if h < 486 then 1 else 0

def next (h : ℕ) : ℕ :=
  if h < 486 then 3 * h / 2 else h / 2

def walk : ℕ → ℕ → ℕ × ℕ
  | 0, h => (h, 0)
  | n + 1, h =>
    let rest := walk n (next h)
    (rest.1, down h + rest.2)

/-- An actual cycle of the deterministic *rounded* graph, including its
length decrement count and strict comparison with the unrounded slope. -/
theorem cycle_price :
    walk 19 246 = (246, 12) ∧ 2 ^ 19 < (3 : ℕ) ^ 12 := by
  decide

def cuts : List ℕ :=
  [246, 261, 276, 293, 310, 329, 348, 369, 391, 414, 439, 465,
   493, 522, 553, 586, 621, 658, 697]

def rank (h : ℕ) : ℕ := (cuts.filter (fun a => a ≤ h)).length

def allowed (h g : ℕ) : Prop :=
  g = next h ∨ (h < 486 ∧ g = next h + 1)

private def edgeTest (h : ℕ) : Bool :=
  decide (19 * down h + rank h ≤ 12 + rank (next h)) &&
    decide (h < 486 → 19 * down h + rank h ≤ 12 + rank (next h + 1))

private theorem verified :
    (List.range 486).all (fun i => edgeTest (243 + i)) = true := by
  decide

/-- The integer-valued dual potential inequality at every allowed
mantissa successor. Either parity uses it after its length increment
and parity price are canceled by the length coefficient minus one. -/
theorem all_edges (i : Fin 486) (g : ℕ) (hg : allowed (243 + i.val) g) :
    19 * down (243 + i.val) + rank (243 + i.val) ≤ 12 + rank g := by
  have hmem : i.val ∈ List.range 486 := List.mem_range.mpr i.isLt
  have ht := List.all_eq_true.mp verified i.val hmem
  simp only [edgeTest, Bool.and_eq_true, decide_eq_true_eq] at ht
  rcases hg with h | ⟨low, h⟩
  · simpa [h] using ht.1
  · simpa [h] using ht.2 low

end Collatz.TernaryWidthSevenPrice
