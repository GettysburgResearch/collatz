import OAI.LinearAlgebra.FiniteFourier.BatchedTimeShift
import Mathlib.Tactic.NormNum

/-! A directly imported rank budget for removing states from a finite transfer.
For a layered graph C is its state adjacency, T injects initial sources, and
readout retains the chosen endpoint labels. The determinant condition is
explicit so that the statement also applies to unique feedback systems. -/

namespace Collatz.OpenAIFourier

open Matrix
open scoped Classical

variable {K S I O : Type*} [Field K] [Fintype S] [Fintype I] [DecidableEq S]

/-- Impose a diagonal deletion mask before each state update. Source and
readout matrices are shared. The rank cost counts only the deleted states. -/
theorem rank_after_deleting_states (C : Matrix S S K) (T V W : Matrix S I K)
    (readout : Matrix O S K) (mask : S → K)
    (det_nonzero : (1 - C).det ≠ 0) (full : V = C * V + T)
    (trimmed : W = (1 - diagonal mask) * (C * W + T)) :
    (readout * V - readout * W).rank ≤ Fintype.card {s : S // mask s ≠ 0} := by
  classical
  rw [← Matrix.mul_sub]
  apply (Matrix.rank_mul_le_right _ _).trans
  have budget := OAI.LinearAlgebra.FiniteFourier.rank_feedback_difference
    C 1 (1 - diagonal mask) T V W (by simpa using det_nonzero)
    (by simpa using full) trimmed
  simpa [Matrix.rank_diagonal] using budget

/-- A deletion budget controls a count when the transfer retains a separate
source label on both sides and its discrepancy has no off-diagonal entries.
The equality hypothesis is the missing representation for actual head colors. -/
theorem count_labeled_disagreements [DecidableEq I]
    (C : Matrix S S K) (T V W : Matrix S I K)
    (readout : Matrix I S K) (mask : S → K) (disagreement : I → K)
    (det_nonzero : (1 - C).det ≠ 0) (full : V = C * V + T)
    (trimmed : W = (1 - diagonal mask) * (C * W + T))
    (labels : readout * V - readout * W = diagonal disagreement) :
    Fintype.card {i : I // disagreement i ≠ 0} ≤ Fintype.card {s : S // mask s ≠ 0} := by
  classical
  have budget := rank_after_deleting_states C T V W readout mask det_nonzero full trimmed
  rwa [labels, Matrix.rank_diagonal] at budget

/-- The ordinary odd sources 3 and 13 land at 5 after one and three
halvings respectively: two distinct input columns in a single target row. -/
theorem ordinary_collision_at_five :
    3 * (3 : ℕ) + 1 = 2 ^ 1 * 5 ∧ 3 * (13 : ℕ) + 1 = 2 ^ 3 * 5 := by
  norm_num

/-- Two genuine depth-two ordinary paths have the same halving total and
terminal. Their words (1,7) and (7,1) generate the first collision block.
The sources and all quotients appearing here are positive and odd. -/
theorem equal_clock_collision_at_seventeen :
    3 * (483 : ℕ) + 1 = 2 ^ 1 * 725 ∧ 3 * (725 : ℕ) + 1 = 2 ^ 7 * 17 ∧
    3 * (469 : ℕ) + 1 = 2 ^ 7 * 11 ∧ 3 * (11 : ℕ) + 1 = 2 ^ 1 * 17 := by
  norm_num

/-- One row of the common-target incidence graph has nonzero entries in
every column. A one-state broadcast also makes every output row nonzero.
Its rank stays at most one even as both finite index sets grow. -/
theorem dense_broadcast_rank_le_one (rows cols : ℕ) :
    Matrix.rank ((fun _ _ => 1) : Matrix (Fin rows) (Fin cols) ℚ) ≤ 1 := by
  let A : Matrix (Fin rows) (Fin 1) ℚ := fun _ _ => 1
  let B : Matrix (Fin 1) (Fin cols) ℚ := fun _ _ => 1
  have h : ((fun _ _ => 1) : Matrix (Fin rows) (Fin cols) ℚ)
      = A * B := by
    ext i j
    rw [Matrix.mul_apply]
    simp [A, B]
  rw [h]
  exact (Matrix.rank_mul_le_left _ _).trans (by simpa using Matrix.rank_le_card_width A)

end Collatz.OpenAIFourier
