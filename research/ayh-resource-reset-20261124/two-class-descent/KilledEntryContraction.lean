import Mathlib

/-! A killed skeleton with geometric drift and a small-set absorbing chance. -/

namespace Collatz.KilledEntryContraction

/-- In the skeleton block, `v` is the incoming Lyapunov value, `w` its
expected terminal value (zero at death), and `u` the mass still alive. The
same contraction applies throughout the live state space. -/
theorem uniform_weighted_contraction {q B L C p : ℝ}
    (hq : q < 1) (hL : 0 < L) (hC : 0 < C)
    (hlarge : 2*B ≤ (1-q)*L) (hsmall : B < p*C) :
    ∃ δ : ℝ, 0 < δ ∧ δ < 1 ∧
      ∀ v w u : ℝ, 0 ≤ v → w ≤ q*v+B → u ≤ 1 →
      (v ≤ L → u ≤ 1-p) →
      w+C*u ≤ (1-δ)*(v+C) := by
  let δ : ℝ := min (1/2) (min ((p*C-B)/(L+C)) (((1-q)/2)*L/(L+C)))
  have hden : 0 < L+C := by positivity
  have hd : 0 < δ := by
    dsimp [δ]
    apply lt_min (by norm_num)
    apply lt_min
    · exact div_pos (by linarith) hden
    · exact div_pos (mul_pos (by linarith) hL) hden
  refine ⟨δ, hd, lt_of_le_of_lt (min_le_left _ _) (by norm_num), ?_⟩
  intro v w u hv hw hu hminor
  have hδ₁ : δ ≤ (p*C-B)/(L+C) :=
    le_trans (min_le_right _ _) (min_le_left _ _)
  have hδ₂ : δ ≤ ((1-q)/2)*L/(L+C) :=
    le_trans (min_le_right _ _) (min_le_right _ _)
  have h₁ := (le_div_iff₀ hden).mp hδ₁
  have h₂ := (le_div_iff₀ hden).mp hδ₂
  by_cases small : v ≤ L
  · have hmass := mul_le_mul_of_nonneg_left (hminor small) hC.le
    have hsize := mul_le_mul_of_nonneg_left small hd.le
    have hgrad := mul_nonneg (sub_nonneg.mpr hq.le) hv
    nlinarith
  · have hLv : L ≤ v := le_of_lt (lt_of_not_ge small)
    have hmass := mul_le_mul_of_nonneg_left hu hC.le
    have hδq : δ ≤ (1-q)/2 := by
      have hrest := mul_nonneg hd.le hC.le
      have hprod : (δ-(1-q)/2)*L ≤ 0 := by nlinarith
      by_contra hn
      have hp := mul_pos (sub_pos.mpr (lt_of_not_ge hn)) hL
      linarith
    have hsize := mul_nonneg (sub_nonneg.mpr hδq) (sub_nonneg.mpr hLv)
    have hlift := mul_le_mul_of_nonneg_left hLv (sub_nonneg.mpr hq.le)
    nlinarith

end Collatz.KilledEntryContraction

#print axioms Collatz.KilledEntryContraction.uniform_weighted_contraction
