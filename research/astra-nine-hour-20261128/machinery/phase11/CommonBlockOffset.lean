import AffineReachability
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Exact physical affine formula on a fully coincident parity block.
The real-law occupation and anti-concentration arguments are analytic. -/

namespace Collatz.CommonBlockOffset

open Collatz.AffineReachability

def prefixMark (w : List Bool) : ℚ := (offset w : ℚ) / scale w

def inverseMultiplier (w : List Bool) : ℚ := 2^w.length / (scale w : ℚ)

def physical (w : List Bool) (x : ℚ) : ℚ :=
  ((scale w : ℚ)*x + offset w) / 2^w.length

def updated (w : List Bool) (k : ℕ) (c : ℚ) : ℚ :=
  ((scale w : ℚ)*c + (1-3^k)*(offset w : ℚ)) / 2^w.length

theorem scale_q_ne_zero (w : List Bool) : (scale w : ℚ) ≠ 0 := by
  have ho := scale_odd w
  have h : scale w ≠ 0 := by omega
  exact_mod_cast h

theorem common_affine (w : List Bool) (k : ℕ) (c x : ℚ) :
    physical w (3^k*x+c) = 3^k*physical w x + updated w k c := by
  unfold physical updated
  ring

/-- Cleared signed mark identity; taking absolute values gives equation (4). -/
theorem normalized_common_offset (w : List Bool) (k : ℕ) (c : ℚ) :
    (updated w k c / 3^k) * inverseMultiplier w =
      c / 3^k - (1-1/3^k)*prefixMark w := by
  unfold updated inverseMultiplier prefixMark
  have hn := scale_q_ne_zero w
  have h₂ : (2 : ℚ)^w.length ≠ 0 := by positivity
  have h₃ : (3 : ℚ)^k ≠ 0 := by positivity
  field_simp
  ring

end Collatz.CommonBlockOffset
