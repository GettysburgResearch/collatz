import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
Cleared arithmetic behind fixed-sibling rational pullbacks and signed
block extrapolation. No ordinary integer-repair existence, infinite
convergence, valuation theorem, or Subspace Theorem is assumed or claimed.
-/

namespace CollatzAdelicRepair

theorem shadow_numerator (x q C z p h : ℤ)
    (word : p * x + C = z * q) :
    z * ((1 + 3 * h) * q + h) - C =
      p * x + h * z * (3 * q + 1) := by
  have hx : z * q - C = p * x := by omega
  calc
    z * ((1 + 3 * h) * q + h) - C =
        (z * q - C) + h * z * (3 * q + 1) := by ring
    _ = p * x + h * z * (3 * q + 1) := by rw [hx]

theorem shadow_next_edge (x q C z p h u qnext : ℤ)
    (word : p * x + C = z * q)
    (edge : 3 * q + 1 = u * qnext) :
    z * ((1 + 3 * h) * q + h) - C =
      p * x + h * z * u * qnext := by
  rw [shadow_numerator x q C z p h word, edge]
  ring

theorem numerator_recurrence (x C z p h znext : ℤ) :
    (1 + 3 * h) * (3 * p) * x +
        3 * h * (3 * C + z) + h * znext =
      3 * ((1 + 3 * h) * p * x + 3 * h * C + h * z) +
        h * znext := by ring

theorem first_sibling_primitive_numerator (x qnext powthree powtwo : ℤ) :
    3 * powthree * x + 21 * powtwo * qnext =
      3 * (powthree * x + 7 * powtwo * qnext) := by ring

theorem extrapolation_displacement (x q D z P Q C : ℚ)
    (source : D = z * q - x) (different : P ≠ Q) :
    (Q - P) * (D + z * C / (P - Q) + x) =
      z * ((Q - P) * q - C) := by
  rw [source]
  have hn : P - Q ≠ 0 := sub_ne_zero.mpr different
  field_simp [hn]
  ring

theorem actual_block_displacement (q qnext P Q C : ℤ)
    (edge : P * q + C = Q * qnext) :
    (Q - P) * q - C = Q * (q - qnext) := by
  calc
    (Q - P) * q - C = Q * q - (P * q + C) := by ring
    _ = Q * (q - qnext) := by rw [edge]; ring

#print axioms shadow_numerator
#print axioms shadow_next_edge
#print axioms numerator_recurrence
#print axioms first_sibling_primitive_numerator
#print axioms extrapolation_displacement
#print axioms actual_block_displacement

end CollatzAdelicRepair
