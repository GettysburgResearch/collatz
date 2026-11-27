import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite projected lower bounds for nonstationary transfer.
The original positive input mass and its actual one-step mass are retained.
The Collatz block and its finite-resolution minorization are written inputs. -/

namespace Collatz.Diagonal.MesoscopicMinorization

private theorem residual_eval {ι : Type*} (I : Finset ι)
    (u p f : ι → ℚ) (a : ℚ) :
    ∑ i ∈ I, (p i - a * u i) * f i =
      (∑ i ∈ I, p i * f i) - a * ∑ i ∈ I, u i * f i := by
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

/-- On the finite input partition, g is the block evaluation of the
requested output cell, t is the one-step total-mass evaluation, and
u is the input Haar mass. The residual can therefore be propagated
using the actual first-step mass rather than the unweighted input mass. -/
theorem one_block {ι : Type*} (I : Finset ι) (u p g t : ι → ℚ)
    (a c m : ℚ)
    (dom : ∀ i ∈ I, a * u i ≤ p i)
    (block : ∀ i ∈ I, c * t i * m ≤ g i)
    (haarBlock : ∑ i ∈ I, u i * g i = m)
    (haarStep : ∑ i ∈ I, u i * t i = 1) :
    (a + c * ((∑ i ∈ I, p i * t i) - a)) * m ≤
      ∑ i ∈ I, p i * g i := by
  have hsum :
      ∑ i ∈ I, (p i - a * u i) * (c * t i * m) ≤
        ∑ i ∈ I, (p i - a * u i) * g i := by
    apply Finset.sum_le_sum
    intro i hi
    exact mul_le_mul_of_nonneg_left (block i hi) (sub_nonneg.mpr (dom i hi))
  have hs :
      ∑ i ∈ I, (p i - a * u i) * (c * t i * m) =
        (c*m) * ∑ i ∈ I, (p i - a * u i) * t i := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    ring
  rw [hs, residual_eval, residual_eval, haarStep, haarBlock, mul_one] at hsum
  nlinarith only [hsum]

/-- Every successful finite block recovers the same fraction of the
remaining window floor. -/
theorem regeneration (a : ℕ → ℚ) (H c : ℚ)
    (ha : 0 ≤ a 0) (hc : c ≤ 1)
    (step : ∀ i, a i + c * (H - a i) ≤ a (i+1)) (n : ℕ) :
    H * (1 - (1-c)^n) ≤ a n := by
  induction n with
  | zero => simpa using ha
  | succ n ih =>
    have ht := mul_le_mul_of_nonneg_left ih (sub_nonneg.mpr hc)
    rw [pow_succ]
    nlinarith only [ht, step n]

end Collatz.Diagonal.MesoscopicMinorization
