import Mathlib.Data.ZMod.Basic
import Mathlib.Topology.Algebra.InfiniteSum.ENNReal
import Mathlib.Tactic.LinearCombination

namespace AstraNine.PointwiseCongruence

/-- The actual affine maps on a finite quotient prime to six. -/
def inverse {q : ℕ} (third : ZMod q) (e : ℕ) (x : ZMod q) : ZMod q :=
  (2 ^ e * x - 1) * third

theorem small_swap {q : ℕ} (third x : ZMod q) (h : 3 * third = 1) :
    inverse third 2 (inverse third 4 x) =
      inverse third 4 (inverse third 2 x) + 4 * third := by
  unfold inverse
  linear_combination 4 * third * h

theorem global_swap {q : ℕ} (third x : ZMod q) :
    inverse third 1 (inverse third 2 x) =
      inverse third 2 (inverse third 1 x) + 2 * third ^ 2 := by
  unfold inverse
  ring

theorem global_loop {q : ℕ} (third : ZMod q) (h : 3 * third = 1) :
    inverse third 2 (inverse third 1 (-7)) = -7 := by
  unfold inverse
  linear_combination (-20 * third - 7) * h

theorem unit_loop {q : ℕ} (third : ZMod q) (h : 3 * third = 1) :
    inverse third 2 1 = 1 := by
  unfold inverse
  linear_combination h

/-- Incrementing a legal exponent by twice a supplied period prime to three
gives the two nontrivial cube roots of unity modulo nine. -/
theorem correction_multiplier (d : ℕ) (h : d % 3 ≠ 0) :
    (4 : ZMod 9) ^ d = 4 ∨ (4 : ZMod 9) ^ d = 7 := by
  have hsplit : d = 3 * (d / 3) + d % 3 := by omega
  have h3 : (4 : ZMod 9) ^ 3 = 1 := by decide
  have hpower : (4 : ZMod 9) ^ d = 4 ^ (d % 3) := by
    conv_lhs => rw [hsplit, pow_add, pow_mul, h3, one_pow, one_mul]
  rw [hpower]
  rcases (show d % 3 = 1 ∨ d % 3 = 2 by omega) with h₁ | h₂
  · left
    rw [h₁, pow_one]
  · right
    rw [h₂]
    decide

private theorem checked_ternary_digit :
    ∀ u m : ZMod 9, (u = 1 ∨ u = 4 ∨ u = 7) → (m = 4 ∨ m = 7) →
      ∃ k : Fin 3, u * m ^ (k : ℕ) = 4 := by
  rintro u m (rfl | rfl | rfl) (rfl | rfl)
  · exact ⟨1, by decide⟩
  · exact ⟨2, by decide⟩
  · exact ⟨0, by decide⟩
  · exact ⟨0, by decide⟩
  · exact ⟨2, by decide⟩
  · exact ⟨1, by decide⟩

theorem steer_ternary_digit (u : ZMod 9) (hu : u = 1 ∨ u = 4 ∨ u = 7)
    (d : ℕ) (hd : d % 3 ≠ 0) :
    ∃ k : Fin 3, u * ((4 : ZMod 9) ^ d) ^ (k : ℕ) = 4 :=
  checked_ternary_digit u (4 ^ d) hu (correction_multiplier d hd)

/-- Any countable positive mixture preserves a uniform lower bound relative
to the true row mass. The sums may include infinitely many legal words. -/
theorem mixture_floor {ι : Type*} (row mass event : ι → ENNReal) (c : ENNReal)
    (h : ∀ i, c * mass i ≤ event i) :
    c * (∑' i, row i * mass i) ≤ ∑' i, row i * event i := by
  rw [← ENNReal.tsum_mul_left]
  exact ENNReal.tsum_le_tsum (fun i => by
    calc
      c * (row i * mass i) = row i * (c * mass i) := by ac_rfl
      _ ≤ row i * event i := mul_le_mul_right (h i) _)

end AstraNine.PointwiseCongruence
