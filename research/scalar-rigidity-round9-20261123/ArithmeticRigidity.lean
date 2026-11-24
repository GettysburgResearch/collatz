import Mathlib.Tactic

/-! Finite scalar arithmetic only; no real-series or CRT construction is imported. -/
namespace Collatz.Round9ArithmeticRigidity

def scalarPrefix : List ℕ → ℚ → ℚ
  | [], t => t
  | g :: gs, t => ((g : ℚ) + scalarPrefix gs t) / 3

def blocks : List Bool → List ℕ
  | [] => []
  | b :: bs => (if b then 1 else 2) :: (if b then 4 else 1) :: blocks bs

theorem block_charges (b : Bool) :
    0 < (if b then 1 else 2 : ℕ) ∧
    0 < (if b then 4 else 1 : ℕ) ∧
    3 * (if b then 1 else 2 : ℕ) + (if b then 4 else 1 : ℕ) = 7 := by
  cases b <;> norm_num

theorem block_length (bs : List Bool) : (blocks bs).length = 2 * bs.length := by
  induction bs with
  | nil => simp [blocks]
  | cons b bs ih => simp [blocks, ih]; omega

theorem arbitrary_word_scalar (bs : List Bool) :
    scalarPrefix (blocks bs) (7 / 8 : ℚ) = 7 / 8 := by
  induction bs with
  | nil => rfl
  | cons b bs ih =>
    cases b <;> simp [blocks, scalarPrefix, ih] <;> norm_num

theorem prefix_tail_difference (gs : List ℕ) (s t : ℚ) :
    scalarPrefix gs s - scalarPrefix gs t = (s - t) / 3 ^ gs.length := by
  induction gs with
  | nil => simp [scalarPrefix]
  | cons g gs ih =>
    calc
      scalarPrefix (g :: gs) s - scalarPrefix (g :: gs) t =
          (scalarPrefix gs s - scalarPrefix gs t) / 3 := by simp [scalarPrefix]; ring
      _ = ((s - t) / 3 ^ gs.length) / 3 := by rw [ih]
      _ = (s - t) / 3 ^ (g :: gs).length := by
        simp only [List.length_cons, pow_succ, div_div]

theorem arbitrary_word_shadow (bs : List Bool) (t : ℚ) :
    scalarPrefix (blocks bs) t - 7 / 8 = (t - 7 / 8) / 3 ^ (2 * bs.length) := by
  have h := prefix_tail_difference (blocks bs) t (7 / 8)
  rw [arbitrary_word_scalar, block_length] at h
  exact h

theorem candidate_block_states (b : Bool) :
    3 * (7 / 8 : ℚ) - (if b then 1 else 2) = 5 / 8 + (if b then 1 else 0) ∧
    3 * (5 / 8 + (if b then 1 else 0) : ℚ) - (if b then 4 else 1) = 7 / 8 := by
  cases b <;> norm_num

/-- The coupled equation adds no constraint once the exact scalar power is supplied. -/
theorem coupled_equation_iff (q q' y y' z : ℝ)
    (hy' : y' ≠ 0) (hpower : z * y' = y ^ 3) :
    (3 * q + 1) * y' = q' * y ^ 3 ↔ z * q' = 3 * q + 1 := by
  rw [← hpower]
  constructor
  · intro h
    apply mul_right_cancel₀ hy'
    nlinarith only [h]
  · intro h
    rw [← h]
    ring

end Collatz.Round9ArithmeticRigidity
