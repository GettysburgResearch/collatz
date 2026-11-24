import Mathlib.Tactic
import Mathlib.Data.Nat.Factorial.BigOperators
import Mathlib.Data.Nat.Choose.Bounds

/-!
# Global excursion accounting for a rational complementary candidate

The exact original and signed-numerator branch equations are retained.
Original states equal to one are terminal for the certificate; the
uniform contraction deliberately assumes x >= 2. The complete finite
visit/repetition certificate and rational interpretation are written in
TRIADIC_CONSTRUCTION.md. No universal candidate selector is assumed.
-/

namespace Collatz.ClosureRoundFive.RationalAccounting

set_option autoImplicit false

def PairStep (q x w x' w' : ℤ) : Prop :=
  (2 * x' = 3 * x + 1 ∧ 2 * w' = w) ∨
  (2 * x' = x ∧ 2 * w' = 3 * w + q)

def potential (x w : ℤ) : ℤ := x * max 1 |w|

private theorem abs_bounds {w w' q : ℤ} (hq : 0 ≤ q)
    (h : 2 * w' = 3 * w + q) :
    3 * |w| - q ≤ 2 * |w'| ∧ 2 * |w'| ≤ 3 * |w| + q := by
  rcases le_total 0 w with hw | hw <;>
    rcases le_total 0 w' with hw' | hw'
  · simp only [abs_of_nonneg hw, abs_of_nonneg hw']; constructor <;> omega
  · simp only [abs_of_nonneg hw, abs_of_nonpos hw']; constructor <;> omega
  · simp only [abs_of_nonpos hw, abs_of_nonneg hw']; constructor <;> omega
  · simp only [abs_of_nonpos hw, abs_of_nonpos hw']; constructor <;> omega

private theorem abs_halve {w w' : ℤ} (h : 2 * w' = w) :
    2 * |w'| = |w| := by
  have hh := congrArg abs h
  simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh

private theorem potential_eq {x w : ℤ} (h : 1 ≤ |w|) :
    potential x w = x * |w| := by
  unfold potential
  rw [max_eq_right h]

private theorem potential_nonneg {x w : ℤ} (hx : 0 ≤ x) :
    0 ≤ potential x w := by
  exact mul_nonneg hx (le_trans (by norm_num) (le_max_left _ _))

theorem large_step_nonincrease {q x w x' w' : ℤ}
    (hq : 1 ≤ q) (hx : 2 ≤ x) (hw : q < |w|)
    (h : PairStep q x w x' w') :
    1 ≤ |w'| ∧ potential x' w' ≤ potential x w := by
  have hw1 : 1 ≤ |w| := by omega
  rcases h with ⟨ex, ew⟩ | ⟨ex, ew⟩
  · have ea := abs_halve ew
    have hw'1 : 1 ≤ |w'| := by omega
    have ep : 4 * (x' * |w'|) = (3 * x + 1) * |w| := by
      calc
        _ = (2 * x') * (2 * |w'|) := by ring
        _ = _ := by rw [ex, ea]
    refine ⟨hw'1, ?_⟩
    rw [potential_eq hw'1, potential_eq hw1]
    have hn := mul_nonneg (by omega : 0 ≤ x - 1) (abs_nonneg w)
    nlinarith
  · obtain ⟨ha, hb⟩ := abs_bounds (by omega) ew
    have hw'1 : 1 ≤ |w'| := by omega
    have hx' : 0 ≤ x' := by omega
    have hm := mul_le_mul_of_nonneg_left hb hx'
    have hd := mul_nonneg (by omega : 0 ≤ x) (by omega : 0 ≤ |w| - q)
    refine ⟨hw'1, ?_⟩
    rw [potential_eq hw'1, potential_eq hw1]
    nlinarith

theorem odd_step_five_sixths {x w x' w' : ℤ}
    (hx : 2 ≤ x) (hw : 2 ≤ |w|)
    (ex : 2 * x' = 3 * x + 1) (ew : 2 * w' = w) :
    6 * potential x' w' ≤ 5 * potential x w := by
  have hx3 : 3 ≤ x := by omega
  have ea := abs_halve ew
  have hw'1 : 1 ≤ |w'| := by omega
  have ep : 4 * (x' * |w'|) = (3 * x + 1) * |w| := by
    calc
      _ = (2 * x') * (2 * |w'|) := by ring
      _ = _ := by rw [ex, ea]
  rw [potential_eq hw'1, potential_eq (by omega : 1 ≤ |w|)]
  have hd := mul_nonneg (by omega : 0 ≤ x - 3) (abs_nonneg w)
  nlinarith

private theorem even_negative_three_fourths {q x w x' w' : ℤ}
    (hq : 1 ≤ q) (hx : 2 ≤ x) (hw : w < -q)
    (ex : 2 * x' = x) (ew : 2 * w' = 3 * w + q) :
    4 * potential x' w' ≤ 3 * potential x w := by
  have hw' : w' < 0 := by omega
  have hw1 : 1 ≤ |w| := by rw [abs_of_neg (by omega : w < 0)]; omega
  have hw'1 : 1 ≤ |w'| := by rw [abs_of_neg hw']; omega
  rw [potential_eq hw1, potential_eq hw'1,
    abs_of_neg (by omega : w < 0), abs_of_neg hw']
  have hp := mul_nonneg (by omega : 0 ≤ x) (by omega : 0 ≤ q)
  nlinarith

theorem very_large_step_seven_eighths {q x w x' w' : ℤ}
    (hq : 1 ≤ q) (hx : 2 ≤ x) (hw : 2 * q < |w|)
    (h : PairStep q x w x' w') :
    8 * potential x' w' ≤ 7 * potential x w := by
  have hv := potential_nonneg (w := w) (by omega : 0 ≤ x)
  obtain ⟨hw'1, _⟩ := large_step_nonincrease hq hx (by omega) h
  rcases h with ⟨ex, ew⟩ | ⟨ex, ew⟩
  · have hh := odd_step_five_sixths hx (by omega) ex ew
    nlinarith
  · obtain ⟨_, hb⟩ := abs_bounds (by omega) ew
    have hm := mul_le_mul_of_nonneg_left hb (by omega : 0 ≤ x')
    have hd := mul_nonneg (by omega : 0 ≤ x) (by omega : 0 ≤ |w| - 2 * q)
    rw [potential_eq hw'1, potential_eq (by omega : 1 ≤ |w|)]
    nlinarith

/-- Two consecutive large numerator clocks contract uniformly in q. -/
theorem large_two_step_seven_eighths {q x w x' w' x'' w'' : ℤ}
    (hq : 1 ≤ q) (hx : 2 ≤ x) (hx' : 2 ≤ x')
    (hw : q < |w|) (hw' : q < |w'|)
    (h : PairStep q x w x' w') (h' : PairStep q x' w' x'' w'') :
    8 * potential x'' w'' ≤ 7 * potential x w := by
  have hn := (large_step_nonincrease hq hx hw h).2
  have hn' := (large_step_nonincrease hq hx' hw' h').2
  have hv := potential_nonneg (w := w) (by omega : 0 ≤ x)
  rcases h with ⟨ex, ew⟩ | ⟨ex, ew⟩
  · have hh := odd_step_five_sixths hx (by omega) ex ew
    nlinarith
  · by_cases hwpos : 0 ≤ w
    · have hbig : 2 * q < w' := by rw [abs_of_nonneg hwpos] at hw; omega
      have habig : 2 * q < |w'| := by
        rw [abs_of_nonneg (by omega : 0 ≤ w')]; exact hbig
      have hh := very_large_step_seven_eighths hq hx' habig h'
      nlinarith
    · have hneg : w < -q := by rw [abs_of_neg (by omega : w < 0)] at hw; omega
      have hh := even_negative_three_fourths hq hx hneg ex ew
      nlinarith

/-- Charge a nonzero small numerator by its own magnitude, rather than
charging every small visit by the worst factor q. -/
theorem nonzero_step_charge {q x w x' w' : ℤ}
    (hq : 1 ≤ q) (hx : 2 ≤ x) (hw : w ≠ 0)
    (h : PairStep q x w x' w') :
    |w| * potential x' w' ≤ (|w| + q) * potential x w := by
  have hw1 : 1 ≤ |w| := by have := abs_pos.mpr hw; omega
  have hv := potential_nonneg (w := w) (by omega : 0 ≤ x)
  rcases h with ⟨ex, ew⟩ | ⟨ex, ew⟩
  · have ea := abs_halve ew
    have hw2 : 2 ≤ |w| := by omega
    have hh := odd_step_five_sixths hx hw2 ex ew
    have hn : potential x' w' ≤ potential x w := by nlinarith
    have hm := mul_le_mul_of_nonneg_left hn (abs_nonneg w)
    have hqv := mul_nonneg (by omega : 0 ≤ q) hv
    nlinarith
  · obtain ⟨_, hb⟩ := abs_bounds (by omega) ew
    have hb' : 2 * max 1 |w'| ≤ 3 * |w| + q := by
      rcases le_total 1 |w'| with hh | hh
      · rw [max_eq_right hh]; exact hb
      · rw [max_eq_left hh]; omega
    have hm := mul_le_mul_of_nonneg_left hb' (by omega : 0 ≤ x')
    have ep : 4 * potential x' w' ≤ x * (3 * |w| + q) := by
      unfold potential
      nlinarith
    have hm' := mul_le_mul_of_nonneg_left ep (abs_nonneg w)
    have hd := mul_nonneg (by omega : 0 ≤ |w| + 3 * q) hv
    rw [potential_eq hw1] at hv hd ⊢
    nlinarith

open scoped BigOperators

/-- Exact one-sign distinct-value charge. -/
theorem distinct_charge_product (q : ℕ) :
    (∏ k ∈ Finset.range q, (1 + (q : ℚ) / (k + 1))) =
      ((2 * q).choose q : ℚ) := by
  calc
    _ = ∏ k ∈ Finset.range q,
        (((q + 1 + k : ℕ) : ℚ) / ((k + 1 : ℕ) : ℚ)) := by
      apply Finset.prod_congr rfl
      intro k _
      push_cast
      field_simp
      ring
    _ = (((q + 1).ascFactorial q : ℕ) : ℚ) / ((q.factorial : ℕ) : ℚ) := by
      rw [Finset.prod_div_distrib]
      congr 1
      · exact_mod_cast (Nat.ascFactorial_eq_prod_range (q + 1) q).symm
      · exact_mod_cast Finset.prod_range_add_one_eq_factorial q
    _ = ((2 * q).choose q : ℚ) := by
      rw [Nat.ascFactorial_eq_factorial_mul_choose]
      push_cast
      have hf : (q.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero q
      have he : q + q = 2 * q := by omega
      rw [he]
      field_simp

/-- Both signs, each magnitude at most once per sign, cost at most 16^q. -/
theorem signed_distinct_charge_bound (q : ℕ) :
    (∏ k ∈ Finset.range q, (1 + (q : ℚ) / (k + 1))) ^ 2 ≤
      (16 : ℚ) ^ q := by
  rw [distinct_charge_product]
  have hc : ((2 * q).choose q : ℚ) ≤ (2 : ℚ) ^ (2 * q) := by
    exact_mod_cast Nat.choose_le_two_pow (2 * q) q
  have hpow : (((2 * q).choose q : ℚ)) ^ 2 ≤ ((2 : ℚ) ^ (2 * q)) ^ 2 := by
    gcongr
  calc
    _ ≤ ((2 : ℚ) ^ (2 * q)) ^ 2 := hpow
    _ = (16 : ℚ) ^ q := by
      rw [← pow_mul]
      have he : 2 * q * 2 = 4 * q := by omega
      rw [he, pow_mul]
      norm_num

/-- The accumulated pair contraction contradicts positive integrality. -/
theorem global_charge_contradiction (V M : ℚ) (L P : ℕ)
    (hV : 1 ≤ V) (hM : 0 ≤ M) (hsize : M < (2 : ℚ) ^ L)
    (hp : 7 * L ≤ P) (hbound : V ≤ M * (7 / 8 : ℚ) ^ P) : False := by
  have hhalf : (7 / 8 : ℚ) ^ 7 ≤ 1 / 2 := by norm_num
  have hdec : (7 / 8 : ℚ) ^ P ≤ (7 / 8 : ℚ) ^ (7 * L) := by
    exact pow_le_pow_of_le_one (by norm_num) (by norm_num) hp
  have hpow : ((7 / 8 : ℚ) ^ 7) ^ L ≤ (1 / 2 : ℚ) ^ L := by gcongr
  rw [pow_mul] at hdec
  have hprod := mul_le_mul_of_nonneg_left (le_trans hdec hpow) hM
  have hlt := mul_lt_mul_of_pos_right hsize
    (pow_pos (by norm_num : (0 : ℚ) < 1 / 2) L)
  have hid : (2 : ℚ) ^ L * (1 / 2 : ℚ) ^ L = 1 := by
    rw [← mul_pow]; norm_num
  rw [hid] at hlt
  linarith

end Collatz.ClosureRoundFive.RationalAccounting
