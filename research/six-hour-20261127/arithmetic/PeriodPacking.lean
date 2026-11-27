import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! An affine path on the common odd numerator lattice of a rational cycle.
The interval search and the estimates for the real rank positions are written
and computational results in PERIOD_GAP.md. -/
set_option autoImplicit false
set_option warningAsError true

namespace SixHour.PeriodPacking

/-- Numerator paths at denominator d, with exponents in chronological order. -/
def follows (d : ℤ) : List ℕ → ℤ → ℤ → Prop
  | [], x, y => x = y
  | a :: w, x, y => ∃ t : ℤ, 2^a * t = 3*x + d ∧ follows d w t y

/-- Subtract two whole paths on the same denominator and word. -/
theorem equal_word {d : ℤ} (w : List ℕ) {x y X Y : ℤ}
    (h₁ : follows d w x y) (h₂ : follows d w X Y) :
    2^w.sum * (y-Y) = 3^w.length * (x-X) := by
  induction w generalizing x X with
  | nil =>
    change x = y at h₁
    change X = Y at h₂
    simp [h₁, h₂]
  | cons a w ih =>
    obtain ⟨u, hu, hrest⟩ := h₁
    obtain ⟨v, hv, Hrest⟩ := h₂
    have edge : 2^a * (u-v) = 3 * (x-X) := by
      rw [mul_sub, hu, hv]
      ring
    simp only [List.sum_cons, List.length_cons, pow_add, pow_succ]
    calc
      2^a * 2^w.sum * (y-Y) = 2^a * (3^w.length * (u-v)) := by
        rw [mul_assoc, ih hrest Hrest]
      _ = 3^w.length * (2^a * (u-v)) := by ring
      _ = 3^w.length * 3 * (x-X) := by rw [edge]; ring

private theorem coprime23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩

/-- At a shared past and a shared future the complete product modulus acts on
the middle numerators. The odd future endpoints supply the last factor of two. -/
theorem two_sided_spacing {d x y a b c e : ℤ} {past future : List ℕ}
    (p₁ : follows d past a x) (p₂ : follows d past b y)
    (f₁ : follows d future x (2*c+1)) (f₂ : follows d future y (2*e+1)) :
    (3 : ℤ)^past.length * 2^(future.sum+1) ∣ x-y := by
  have hin := equal_word past p₁ p₂
  have hout := equal_word future f₁ f₂
  have h₃ : (3 : ℤ)^past.length ∣ 2^past.sum * (x-y) := ⟨a-b, hin⟩
  have h₂ : (2 : ℤ)^(future.sum+1) ∣ 3^future.length * (x-y) := by
    refine ⟨c-e, ?_⟩
    rw [← hout, pow_succ]
    ring
  exact coprime23.symm.pow.mul_dvd
    (coprime23.symm.pow.dvd_of_dvd_mul_left h₃)
    (coprime23.pow.dvd_of_dvd_mul_left h₂)

/-- The numerator span of n+1 physically ordered vertices in one word cell
is at least n times the whole spacing. The scaled strict inequality handles
half-open height bins of rational width. -/
theorem located_packing (x : ℕ → ℤ) {n : ℕ} {M B W : ℤ}
    (hB : 0 ≤ B)
    (gaps : ∀ i < n, x i < x (i+1) ∧ M ∣ x (i+1)-x i)
    (width : B * (x n-x 0) < W) : B*M*(n : ℤ) < W := by
  have span (j : ℕ) (hj : j ≤ n) : M*(j : ℤ) ≤ x j-x 0 := by
    induction j with
    | zero => simp
    | succ j ih =>
      obtain ⟨inc, div⟩ := gaps j (by omega)
      have sep : M ≤ x (j+1)-x j := Int.le_of_dvd (by omega) div
      have prior := ih (by omega)
      rw [Nat.cast_succ, mul_add, mul_one]
      omega
  calc
    B*M*(n : ℤ) = B*(M*(n : ℤ)) := mul_assoc _ _ _
    _ ≤ B*(x n-x 0) := mul_le_mul_of_nonneg_left (span n (by omega)) hB
    _ < W := width

#print axioms equal_word
#print axioms two_sided_spacing
#print axioms located_packing

end SixHour.PeriodPacking
