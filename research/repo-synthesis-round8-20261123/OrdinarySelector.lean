import Mathlib.Tactic

/-!
Finite arithmetic core for ORDINARY_SELECTOR.md. The real scalar construction,
modular existence, and all-parameter ordinary attachment are written results.
-/

namespace Collatz.Round8OrdinarySelector

def low (q : ℚ) : ℚ := (9 * q + 7) / 8

def paid (q : ℚ) : ℚ := (9 * q + 5) / 32

def lowRun : ℕ → ℚ → ℚ
  | 0, q => q
  | m + 1, q => low (lowRun m q)

/-- The odd quotients certify exact gaps (2,1), not only divisibility. -/
theorem low_complete_gaps (z : ℕ) :
    3 * (16 * z + 9) + 1 = 4 * (12 * z + 7) ∧
    3 * (12 * z + 7) + 1 = 2 * (18 * z + 11) ∧
    Odd (12 * z + 7) ∧ Odd (18 * z + 11) := by
  refine ⟨by ring, by ring, ?_, ?_⟩
  · exact ⟨6 * z + 3, by omega⟩
  · exact ⟨9 * z + 5, by omega⟩

/-- The odd quotients certify exact gaps (1,4). -/
theorem paid_complete_gaps (z : ℕ) :
    3 * (64 * z + 3) + 1 = 2 * (96 * z + 5) ∧
    3 * (96 * z + 5) + 1 = 16 * (18 * z + 1) ∧
    Odd (96 * z + 5) ∧ Odd (18 * z + 1) := by
  refine ⟨by ring, by ring, ?_, ?_⟩
  · exact ⟨48 * z + 2, by omega⟩
  · exact ⟨9 * z, by omega⟩

theorem low_shift (q : ℚ) : low q + 7 = (9 / 8 : ℚ) * (q + 7) := by
  dsimp [low]
  ring

theorem low_run_shift (m : ℕ) (q : ℚ) :
    lowRun m q + 7 = (9 / 8 : ℚ) ^ m * (q + 7) := by
  induction m with
  | zero => simp [lowRun]
  | succ m ih =>
    rw [lowRun, low_shift, ih, pow_succ]
    ring

/-- Complete affine composite, including its inhomogeneous term. -/
theorem low_run_paid (m : ℕ) (q : ℚ) :
    paid (lowRun m q) =
      (9 / 32 : ℚ) * (9 / 8 : ℚ) ^ m * (q + 7) - 29 / 16 := by
  have hs := low_run_shift m q
  dsimp [paid]
  linarith

theorem low_scalar_prefix (h₀ h₁ h₂ : ℚ)
    (hfirst : h₁ = 3 * h₀ - 2) (hsecond : h₂ = 3 * h₁ - 1) :
    h₀ = (7 + h₂) / 9 := by
  linarith

theorem paid_scalar_prefix (h₀ h₁ h₂ : ℚ)
    (hfirst : h₁ = 3 * h₀ - 1) (hsecond : h₂ = 3 * h₁ - 4) :
    h₀ = (7 + h₂) / 9 := by
  linarith

theorem low_scalar_interval (h : ℚ)
    (hlower : 5 / 6 < h) (hupper : h < 7 / 8) :
    1 / 2 < 3 * h - 2 ∧ 3 * h - 2 < 5 / 8 := by
  constructor <;> linarith

theorem paid_scalar_intervals (b : ℚ)
    (hlower : 1 / 2 < b) (hupper : b < 5 / 8) :
    5 / 6 < (7 + b) / 9 ∧ (7 + b) / 9 < 7 / 8 ∧
    3 / 2 < (4 + b) / 3 ∧ (4 + b) / 3 < 37 / 24 := by
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

/-- The elementary exponential estimate funding the actual scalar tail bound. -/
theorem tail_exponential_bound (m : ℕ) : 48 * m + 124 < 3 ^ (m + 5) := by
  induction m with
  | zero => norm_num
  | succ m ih =>
    have hp : 3 ^ (m + 1 + 5) = 3 * 3 ^ (m + 5) := by
      rw [show m + 1 + 5 = (m + 5) + 1 by omega, pow_succ]
      ring
    rw [hp]
    omega

/-- A positive affine remainder preserves any strictly smaller slope target. -/
theorem affine_return_expansion (q r A C : ℚ)
    (hq : 0 < q) (hA : 1 ≤ A) (hC : C < A)
    (hr : r = A * q + 7 * A - 29 / 16) : C * q < r := by
  have hp : 0 < (A - C) * q := mul_pos (sub_pos.mpr hC) hq
  nlinarith

end Collatz.Round8OrdinarySelector
