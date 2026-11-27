import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Positive integer separation of two paths using a common word.
The section equation is the cleared identity proved in MovingScenery.
The following kernels apply it to two ordinary odd paths, retain every
terminal tail length, and bound the clock covered by sparse disagreements. -/

namespace Collatz.Diagonal.WordSeparation

/-- In increasing order, both differences across a common ordinary word
belong to full binary and ternary progressions, including the odd factor. -/
theorem common_word_divisibility (d l u v : ℕ)
    (sectionEq : 2^d * u = 3^l * v) (evenU : 2 ∣ u) :
    2*3^l ∣ u ∧ 2^(d+1) ∣ v := by
  have hp : Nat.Coprime (2^d) (3^l) := Nat.Coprime.pow d l (by decide)
  have hu : 3^l ∣ u := hp.symm.dvd_of_dvd_mul_left (sectionEq ▸ dvd_mul_right _ _)
  have hv : 2^(d+1) ∣ v := by
    apply (Nat.Coprime.pow (d+1) l (by decide : Nat.Coprime 2 3)).dvd_of_dvd_mul_left
    obtain ⟨q, hq⟩ := evenU
    exact ⟨q, by rw [← sectionEq, hq, pow_succ]; ring⟩
  have h2 : Nat.Coprime 2 (3^l) := by
    simpa using (Nat.Coprime.pow 1 l (by decide : Nat.Coprime 2 3))
  exact ⟨h2.mul_dvd_of_dvd_of_dvd evenU hu, hv⟩

/-- If the common block is followed by r steps on each branch, at least
one of the two physical tail division totals pays this full power of three. -/
theorem terminal_tail_cost (l r z z' y s T T' : ℕ)
    (gap : 2*3^l ≤ max z z') (rootOrder : y ≤ s)
    (trunk : 3^r*z ≤ 2^T*y) (side : 3^r*z' ≤ 2^T'*s) :
    2*3^(l+r) ≤ 2^(max T T')*s := by
  have hb : 3^r*z ≤ 2^(max T T')*s :=
    trunk.trans (Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) (Nat.le_max_left _ _)) rootOrder)
  have hc : 3^r*z' ≤ 2^(max T T')*s :=
    side.trans (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) (Nat.le_max_right _ _)))
  calc
    2*3^(l+r) = 3^r*(2*3^l) := by rw [pow_add]; ring
    _ ≤ 3^r * max z z' := Nat.mul_le_mul_left _ gap
    _ ≤ _ := by rcases le_total z z' with h | h
                · simpa [max_eq_right h] using hc
                · simpa [max_eq_left h] using hb

/-- All gaps of a true word have exponent at least one. The quantitative
run argument then iterates an affine bound from one disagreement to the next. -/
theorem disagreement_clock (t : ℕ → ℚ) (L B : ℚ) (hL : 1 ≤ L)
    (zero : t 0 = 0) (step : ∀ i, t (i+1) ≤ L*t i + B) (k : ℕ) :
    (L-1)*t k + B ≤ B*L^k := by
  induction k with
  | zero => simp [zero]
  | succ k ih =>
    have hs := mul_le_mul_of_nonneg_left (step k) (sub_nonneg.mpr hL)
    have ht := mul_le_mul_of_nonneg_left ih (show 0 ≤ L by linarith)
    rw [pow_succ]
    nlinarith only [hs, ht]

end Collatz.Diagonal.WordSeparation
