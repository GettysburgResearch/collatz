import FiniteTrace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-! Ordinary stopped prefix maxima and the finite defect lower bound. -/

namespace Collatz.ReciprocalRigidity.OrdinaryDefect

open Collatz.ReciprocalRigidity.FiniteTrace

def slope (n : ℕ) : ℚ := if n % 2 = 0 then 1/2 else 3/2

theorem slope_pos (n : ℕ) : 0 < slope n := by
  unfold slope
  split <;> norm_num

def along (f : ℕ → ℚ) : ℕ → ℕ → ℚ
  | 0, _ => 1
  | k+1, n => f n * along f k (step n)

/-- Include both time zero and first arrival at a marked source. -/
def stoppedMaximum (mark : ℕ → Bool) : ℕ → ℕ → ℚ
  | 0, _ => 1
  | k+1, n => if mark n then 1 else max 1 (slope n * stoppedMaximum mark k (step n))

theorem maximum_ge_one (mark : ℕ → Bool) (k n : ℕ) :
    1 ≤ stoppedMaximum mark k n := by
  cases k with
  | zero => exact le_rfl
  | succ k =>
    simp only [stoppedMaximum]
    split <;> first | exact le_rfl | exact le_max_left _ _

/-- Every genuine prefix before an earlier gate occurs lies below the stopped maximum. -/
theorem prefix_le_maximum (mark : ℕ → Bool) (t fuel n : ℕ) (hf : t ≤ fuel)
    (clear : ∀ i < t, mark (orbit i n) = false) :
    along slope t n ≤ stoppedMaximum mark fuel n := by
  induction t generalizing fuel n with
  | zero => exact maximum_ge_one mark fuel n
  | succ t ih =>
    cases fuel with
    | zero => omega
    | succ fuel =>
      have hn : mark n = false := clear 0 (by omega)
      have hnext : ∀ i < t, mark (orbit i (step n)) = false := by
        intro i hi
        exact clear (i+1) (by omega)
      simp only [along, stoppedMaximum, hn, Bool.false_eq_true, ↓reduceIte]
      exact (mul_le_mul_of_nonneg_left (ih fuel (step n) (by omega) hnext)
        (le_of_lt (slope_pos n))).trans (le_max_right _ _)

def excess (u : ℕ → ℚ) (n : ℕ) : ℚ :=
  max 1 ((slope n)^2 * u n / u (step n))

theorem excess_ge_one (u : ℕ → ℚ) (n : ℕ) : 1 ≤ excess u n := le_max_left _ _

theorem edge_comparison (u : ℕ → ℚ) (hu : ∀ n, 0 < u n) (n : ℕ) :
    (slope n)^2 * u n ≤ excess u n * u (step n) :=
  (div_le_iff₀ (hu _)).mp (le_max_right _ _)

/-- Positive edge defects dominate the signed slope-product comparison on each path. -/
theorem path_comparison (u : ℕ → ℚ) (hu : ∀ n, 0 < u n) (t n : ℕ) :
    (along slope t n)^2 * u n ≤ along (excess u) t n * u (orbit t n) := by
  induction t generalizing n with
  | zero => simp [along, orbit]
  | succ t ih =>
    change (slope n * along slope t (step n))^2 * u n ≤
      (excess u n * along (excess u) t (step n)) * u (orbit t (step n))
    calc
      _ = (along slope t (step n))^2 * ((slope n)^2 * u n) := by ring
      _ ≤ (along slope t (step n))^2 * (excess u n * u (step n)) :=
        mul_le_mul_of_nonneg_left (edge_comparison u hu n) (sq_nonneg _)
      _ = excess u n * ((along slope t (step n))^2 * u (step n)) := by ring
      _ ≤ excess u n * (along (excess u) t (step n) * u (orbit t (step n))) :=
        mul_le_mul_of_nonneg_left (ih (step n)) (zero_le_one.trans (excess_ge_one u n))
      _ = _ := by ring

#print axioms prefix_le_maximum
#print axioms edge_comparison
#print axioms path_comparison

end Collatz.ReciprocalRigidity.OrdinaryDefect
