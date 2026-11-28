import AffineTransporter
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

/-! A genuine rational-word gap around negative dyadic sources.
This is the arithmetic obstruction used to improve finite inverse windows.
-/

namespace Collatz.NegativeAffineGap

open Collatz.AffineTransporter

def value (w : List ℕ) : ℚ := offset w - slope w

theorem value_nil : value [] = -1 := by norm_num [value, offset, slope]

theorem value_cons (e : ℕ) (w : List ℕ) :
    value (e :: w) = (1 + 3 * value w) / 2 ^ e := by
  simp only [value, offset, slope_cons]
  ring

/-- Negative word values at -1 have a genuine open gap (-1/2,-1/4). -/
theorem negative_gap (w : List ℕ) (h : Valid w) :
    value w = -1 ∨ value w = -(1/2 : ℚ) ∨ -(1/4 : ℚ) ≤ value w := by
  induction w with
  | nil => exact Or.inl value_nil
  | cons e w ih =>
    have he : 1 ≤ e := h e (by simp)
    have hp : 0 < (2 : ℚ)^e := by positivity
    have htwo : (2 : ℚ) ≤ 2^e := by
      have ht := pow_le_pow_right₀ (by norm_num : (1:ℚ) ≤ 2) he
      simpa using ht
    rcases ih (valid_tail h) with hm | hh | hq
    · by_cases h1 : e = 1
      · left
        norm_num [value_cons, h1, hm]
      · by_cases h2 : e = 2
        · right; left
          norm_num [value_cons, h2, hm]
        · right; right
          have he3 : 3 ≤ e := by omega
          have h8 : (8 : ℚ) ≤ 2^e := by
            have ht := pow_le_pow_right₀ (by norm_num : (1:ℚ) ≤ 2) he3
            norm_num at ht ⊢
            exact ht
          rw [value_cons, hm]
          apply (le_div_iff₀ hp).mpr
          linarith
    · right; right
      rw [value_cons, hh]
      apply (le_div_iff₀ hp).mpr
      linarith
    · right; right
      have hn : 0 < (1 : ℚ) + 3 * value w := by linarith
      have hv : 0 < value (e :: w) := by
        rw [value_cons]
        exact div_pos hn hp
      linarith

/-- Only the first gap needs a cap. Later positive gaps can be arbitrary. -/
theorem capped_first_negative (R e : ℕ) (w : List ℕ)
    (h : Valid (e :: w)) (hcap : e ≤ R) (hneg : value (e :: w) < 0) :
    value (e :: w) ≤ -(1 / (2:ℚ)^(R+1)) := by
  have hp : 0 < (2:ℚ)^e := by positivity
  have he : (2:ℚ)^e ≤ 2^(R+1) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  have he2 : (2:ℚ)^(e+1) ≤ 2^(R+1) :=
    pow_le_pow_right₀ (by norm_num) (by omega)
  rcases negative_gap w (valid_tail h) with hm | hh | hq
  · rw [value_cons, hm]
    have hi : (1:ℚ) / 2^(R+1) ≤ 1 / 2^e :=
      one_div_le_one_div_of_le hp he
    have hj : (0:ℚ) ≤ 1 / 2^e := by positivity
    calc
      (1 + 3 * -(1:ℚ)) / 2^e = -(1 / 2^e) - 1 / 2^e := by ring
      _ ≤ -(1 / 2^e) := by linarith
      _ ≤ -(1 / (2:ℚ)^(R+1)) := neg_le_neg hi
  · rw [value_cons, hh]
    have hpow : (2:ℚ)^(e+1) = 2^e * 2 := by rw [pow_succ]
    have hi : (1:ℚ) / 2^(R+1) ≤ 1 / 2^(e+1) :=
      one_div_le_one_div_of_le (by positivity) he2
    calc
      (1 + 3 * -(1/2 : ℚ)) / 2^e = -(1 / (2:ℚ)^(e+1)) := by
        rw [hpow]
        field_simp
        ring
      _ ≤ -(1 / (2:ℚ)^(R+1)) := neg_le_neg hi
  · have hn : 0 < (1:ℚ) + 3 * value w := by linarith
    have hv : 0 < value (e :: w) := by rw [value_cons]; exact div_pos hn hp
    linarith

theorem excludes_small_dyadic (R e k : ℕ) (w : List ℕ)
    (h : Valid (e :: w)) (hcap : e ≤ R) (hk : R+2 ≤ k) :
    value (e :: w) ≠ -(1 / (2:ℚ)^k) := by
  intro heq
  have hp : 0 < (1:ℚ) / 2^k := by positivity
  have hneg : value (e :: w) < 0 := by rw [heq]; linarith
  have hb := capped_first_negative R e w h hcap hneg
  have hpow : (2:ℚ)^(R+1) < 2^k :=
    pow_lt_pow_right₀ (by norm_num) (by omega)
  have hi : (1:ℚ) / 2^k < 1 / 2^(R+1) :=
    one_div_lt_one_div_of_lt (by positivity) hpow
  rw [heq] at hb
  linarith

/-- A whole open interval is excluded, independently of the word length. -/
theorem excludes_open_gap (w : List ℕ) (h : Valid w) (x : ℚ)
    (hlo : -(1/2 : ℚ) < x) (hhi : x < -(1/4 : ℚ)) :
    value w ≠ x := by
  intro heq
  rcases negative_gap w h with hm | hh | hq <;> rw [heq] at * <;> linarith

/-- A sufficiently small positive witness enters the excluded interval
under every first inverse gap below the supplied cap. -/
theorem capped_inverse_enters_gap (R e : ℕ) (z : ℚ) (he : e ≤ R)
    (hz : 0 < z) (hsmall : z < 1 / (2:ℚ)^(R+2)) :
    -(1/3 : ℚ) < ((2:ℚ)^e*z-1)/3 ∧
      ((2:ℚ)^e*z-1)/3 < -(1/4 : ℚ) := by
  have hp : 0 < (2:ℚ)^e := by positivity
  have hpow : (2:ℚ)^e ≤ 2^R := pow_le_pow_right₀ (by norm_num) he
  have hmul : (2:ℚ)^e*z ≤ 2^R*z := mul_le_mul_of_nonneg_right hpow (le_of_lt hz)
  have hbound : (2:ℚ)^R*z < 1/4 := by
    have hd : 0 < (2:ℚ)^(R+2) := by positivity
    have hb := (lt_div_iff₀ hd).mp hsmall
    rw [pow_add] at hb
    norm_num at hb
    nlinarith
  constructor <;> nlinarith [mul_pos hp hz]

end Collatz.NegativeAffineGap
