import MersenneCrests
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

namespace Collatz.ClockRectangle

open Collatz.MersenneCrests (run)

def corrected (j s : Nat) : Rat := 5 * 2^s / 3^j
def multiplier (n j s : Nat) : Rat := corrected j s / n

/-- Four literal first visits, with both clocks retained and no earlier visit to five. -/
theorem firstHits :
    run (81,0) 12 = (5,5) ∧ (∀ t : Fin 12, (run (81,0) t.val).1 ≠ 5) ∧
    run (135,0) 24 = (5,12) ∧ (∀ t : Fin 24, (run (135,0) t.val).1 ≠ 5) ∧
    run (69,0) 7 = (5,2) ∧ (∀ t : Fin 7, (run (69,0) t.val).1 ≠ 5) ∧
    run (115,0) 19 = (5,9) ∧ (∀ t : Fin 19, (run (115,0) t.val).1 ≠ 5) := by
  decide

/-- The source equality is a genuine four-distinct-entry multiplicative rectangle. -/
theorem literalRectangle :
    (81 : Nat)*115 = 69*135 ∧
    (81 : Nat) ≠ 135 ∧ (81 : Nat) ≠ 69 ∧ (81 : Nat) ≠ 115 ∧
    (135 : Nat) ≠ 69 ∧ (135 : Nat) ≠ 115 ∧ (69 : Nat) ≠ 115 := by
  decide

/-- Both native clock sums and the exact correction multipliers agree. -/
theorem clockRectangle :
    (5 : Nat)+9 = 2+12 ∧ (12 : Nat)+19 = 7+24 ∧
    corrected 5 12 * corrected 9 19 = corrected 2 7 * corrected 12 24 ∧
    multiplier 81 5 12 * multiplier 115 9 19 =
      multiplier 69 2 7 * multiplier 135 12 24 := by
  norm_num [multiplier, corrected]

/-- None of the corrected values is a repeated value hidden in the relation. -/
theorem correctedValuesDistinct :
    corrected 5 12 ≠ corrected 12 24 ∧
    corrected 5 12 ≠ corrected 2 7 ∧
    corrected 5 12 ≠ corrected 9 19 ∧
    corrected 12 24 ≠ corrected 2 7 ∧
    corrected 12 24 ≠ corrected 9 19 ∧
    corrected 2 7 ≠ corrected 9 19 := by
  norm_num [corrected]

end Collatz.ClockRectangle
