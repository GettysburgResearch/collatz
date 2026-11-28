import MarkedCutoffArithmetic
import Mathlib.Tactic.Ring

/-! Positive affine offset on a supplied finite segment of native odd edges. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.NativeOffsetFloor

open Collatz.MarkedCutoffFlux

/-- The final edge is appended at its true landing and valuation. Each
departure in an odd segment has at least one actual division by two. -/
inductive Segment (x : ℕ) : ℕ → ℕ → ℕ → Prop where
  | empty : Segment x x 0 0
  | extend {z j s : ℕ} (earlier : Segment x z j s) (positive : 1 ≤ gap z) :
      Segment x (landing z) (j + 1) (s + gap z)

theorem divisions_ge_grade {x y j s : ℕ} (path : Segment x y j s) : j ≤ s := by
  induction path with
  | empty => exact Nat.le_refl _
  | extend _ positive ih => omega

/-- After dividing by the slope, the true positive offset is at least
1 − (2/3)^j. The displayed inequality has no rational denominators. -/
theorem full_offset_floor {x y j s : ℕ} (path : Segment x y j s) :
    3 ^ j * (x + 1) ≤ 2 ^ s * y + 2 ^ j := by
  induction path with
  | empty => simp
  | @extend z j s earlier _ ih =>
    have clock := divisions_ge_grade earlier
    have powClock : 2 ^ j ≤ (2 : ℕ) ^ s := Nat.pow_le_pow_right (by decide) clock
    have grow := Nat.mul_le_mul_left 3 ih
    calc
      3 ^ (j + 1) * (x + 1) = 3 * (3 ^ j * (x + 1)) := by ring
      _ ≤ 3 * (2 ^ s * z + 2 ^ j) := grow
      _ ≤ 2 ^ s * (3 * z + 1) + 2 ^ (j + 1) := by
        calc
          _ = 3 * (2 ^ s * z) + 2 ^ j + 2 ^ (j + 1) := by ring
          _ ≤ 3 * (2 ^ s * z) + 2 ^ s + 2 ^ (j + 1) := by omega
          _ = _ := by ring
      _ = 2 ^ (s + gap z) * landing z + 2 ^ (j + 1) := by
        rw [pow_add 2 s (gap z), Nat.mul_assoc, native_edge]

/-- Every positive-length segment has the intrinsic 1/3 native source
strip, which gives uniqueness when two candidates have a common slope. -/
theorem third_offset_floor {x y j s : ℕ} (path : Segment x y (j + 1) s) :
    3 ^ j * (3 * x + 1) ≤ 2 ^ s * y := by
  have h := full_offset_floor path
  have powers : (2 : ℕ) ^ j ≤ 3 ^ j := Nat.pow_le_pow_left (by decide) j
  rw [pow_succ, pow_succ] at h
  calc
    3 ^ j * (3 * x + 1) = 3 ^ j * 3 * (x + 1) - 2 * 3 ^ j := by
      have eq : 3 ^ j * 3 * (x + 1) = 3 ^ j * (3 * x + 1) + 2 * 3 ^ j := by ring
      omega
    _ ≤ 2 ^ s * y := by omega

end Collatz.NativeOffsetFloor
