import MarkedCutoffArithmetic
import Mathlib.Tactic.Ring

/-! Source width at a fixed target and clock, for actual paths above a floor. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.FirstLandingCell

open Collatz.MarkedCutoffFlux

/-- Start, terminal, odd count and accumulated number of divisions by two.
Only departed states are required to stay above the floor. -/
inductive HighSegment (B : ℕ) : ℕ → ℕ → ℕ → ℕ → Prop where
  | nil (x : ℕ) : HighSegment B x x 0 0
  | cons {x y j s : ℕ} (high : B ≤ x)
      (tail : HighSegment B (landing x) y j s) :
      HighSegment B x y (j + 1) (gap x + s)

/-- The exact integer strip for the uncorrected physical source, including
the additive relative error from all the high departures. -/
theorem native_cell_strip {B x y j s : ℕ} (path : HighSegment B x y j s) :
    3 ^ j * x ≤ 2 ^ s * y ∧
      3 * B * (2 ^ s * y) ≤ 3 * B * (3 ^ j * x) + j * (2 ^ s * y) := by
  induction path with
  | nil x => simp
  | @cons x y j s high _ ih =>
    have lift := Nat.mul_le_mul_left (2 ^ gap x) ih.1
    have lifted : 3 ^ j * (3 * x + 1) ≤ 2 ^ gap x * (2 ^ s * y) := by
      calc
        3 ^ j * (3 * x + 1) = 2 ^ gap x * (3 ^ j * landing x) := by
          rw [← native_edge x]
          ring
        _ ≤ _ := lift
    have base : 3 * B ≤ 3 * x + 1 := by omega
    have err := (Nat.mul_le_mul_left (3 ^ j) base).trans lifted
    have liftErr := Nat.mul_le_mul_left (2 ^ gap x) ih.2
    rw [show 3 ^ (j + 1) = 3 ^ j * 3 from pow_succ 3 j,
        show 2 ^ (gap x + s) = 2 ^ gap x * 2 ^ s from pow_add 2 (gap x) s]
    constructor
    · calc
        3 ^ j * 3 * x ≤ 3 ^ j * (3 * x + 1) := by
          rw [Nat.mul_assoc]
          exact Nat.mul_le_mul_left _ (by omega)
        _ ≤ _ := by simpa [Nat.mul_assoc] using lifted
    · calc
        3 * B * (2 ^ gap x * 2 ^ s * y) ≤
            2 ^ gap x * (3 * B * (3 ^ j * landing x) + j * (2 ^ s * y)) := by
            simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using liftErr
        _ = 3 * B * (3 ^ j * 3 * x) + j * (2 ^ gap x * (2 ^ s * y)) +
            3 ^ j * (3 * B) := by
            have edge := native_edge x
            calc
              _ = 3 * B * 3 ^ j * (2 ^ gap x * landing x) +
                  j * (2 ^ gap x * (2 ^ s * y)) := by ring
              _ = _ := by rw [edge]; ring
        _ ≤ 3 * B * (3 ^ j * 3 * x) + j * (2 ^ gap x * (2 ^ s * y)) +
            2 ^ gap x * (2 ^ s * y) := Nat.add_le_add_left err _
        _ = _ := by ring

/-- Two sources contributing at precisely the same finite cell have
separation at most j/(3B) times the affine uncorrected source length. -/
theorem same_cell_width {B x x' y j s : ℕ}
    (left : HighSegment B x y j s) (right : HighSegment B x' y j s) :
    3 * B * (3 ^ j * x') ≤ 3 * B * (3 ^ j * x) + j * (2 ^ s * y) :=
  (Nat.mul_le_mul_left (3 * B) (native_cell_strip right).1).trans
    (native_cell_strip left).2

end Collatz.FirstLandingCell
