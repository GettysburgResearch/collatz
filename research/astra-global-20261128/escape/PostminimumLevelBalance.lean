import MarkedCutoffArithmetic
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Ring

/-! Exact discounted level-crossing balance for the actual positive odd map. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.PostminimumLevelBalance

open Collatz.MarkedCutoffFlux
noncomputable section

def high (B x : ℕ) : ℝ := if B < x then 1 else 0
def weight (x : ℕ) : ℝ := (3 * (x : ℝ)) / (3 * (x : ℝ) + 1)
def atDate (x : ℕ) : ℕ → ℕ
  | 0 => x
  | n + 1 => atDate (landing x) n

def survive (x : ℕ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => weight x * survive (landing x) n

/-- Each directed crossing carries survival through its outgoing edge. -/
def outward (B x : ℕ) : ℕ → ℝ
  | 0 => 0
  | n + 1 => weight x *
      ((if x ≤ B ∧ B < landing x then 1 else 0) + outward B (landing x) n)

def inward (B x : ℕ) : ℕ → ℝ
  | 0 => 0
  | n + 1 => weight x *
      ((if landing x ≤ B ∧ B < x then 1 else 0) + inward B (landing x) n)

/-- Local kills are assigned to the departed state. -/
def highKills (B x : ℕ) : ℕ → ℝ
  | 0 => 0
  | n + 1 => (1 - weight x) * high B x + weight x * highKills B (landing x) n

private theorem edge_indicator (B x y : ℕ) :
    ((if x ≤ B ∧ B < y then 1 else 0) : ℝ) -
      (if y ≤ B ∧ B < x then 1 else 0) = high B y - high B x := by
  by_cases hx : B < x
  · by_cases hy : B < y
    · simp [high, hx, hy, Nat.not_le_of_lt hx, Nat.not_le_of_lt hy]
    · simp [high, hx, hy, Nat.not_le_of_lt hx, Nat.le_of_not_gt hy]
  · by_cases hy : B < y
    · simp [high, hx, hy, Nat.le_of_not_gt hx, Nat.not_le_of_lt hy]
    · simp [high, hx, hy]

/-- Finite weighted flux identity on consecutive native odd landings.
It allows arbitrary returns and does not divide by the survival factor. -/
theorem weighted_level_balance (B x n : ℕ) :
    outward B x n - inward B x n =
      survive x n * high B (atDate x n) - high B x + highKills B x n := by
  induction n generalizing x with
  | zero => simp [outward, inward, survive, atDate, highKills]
  | succ n ih =>
    simp only [outward, inward, survive, atDate, highKills]
    calc
      _ = weight x *
          ((((if x ≤ B ∧ B < landing x then 1 else 0) : ℝ) -
            (if landing x ≤ B ∧ B < x then 1 else 0)) +
            (outward B (landing x) n - inward B (landing x) n)) := by ring
      _ = _ := by rw [edge_indicator, ih]; ring

/-- A donor starting below the floor and ending above it pays its retained
terminal survival, plus every intervening kill at a high departure. -/
theorem from_low_to_high {B x n : ℕ} (start : x ≤ B) (finish : B < atDate x n) :
    outward B x n = inward B x n + survive x n + highKills B x n := by
  have h := weighted_level_balance B x n
  simp [high, Nat.not_lt_of_ge start, finish] at h
  rw [sub_eq_iff_eq_add] at h
  rw [h]
  ring

/-- Splitting a finite original trajectory at any specified date retains
the source survival multiplying the complete later outward occupation. -/
theorem split_outward (B x j k : ℕ) :
    outward B x (j + k) =
      outward B x j + survive x j * outward B (atDate x j) k := by
  induction j generalizing x with
  | zero => simp [outward, survive, atDate]
  | succ j ih =>
    rw [Nat.succ_add]
    simp only [outward, survive, atDate]
    rw [ih]
    ring

end
end Collatz.PostminimumLevelBalance
