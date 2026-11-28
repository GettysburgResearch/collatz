import AffineCorrection

/-! A same-clock meeting across a gap between consecutive ternary slopes
forces a specified amount of actual additive correction. -/

namespace Collatz.MinimumWindow

theorem accumulated_one_le (t n : ℕ) (hn : 0 < n) :
    1 ≤ accumulated t n := by
  induction t generalizing n with
  | zero => simp [accumulated]
  | succ t ih =>
    rw [accumulated_succ]
    exact one_le_mul_of_one_le_of_one_le (correction_bounds hn).1
      (ih _ (step_positive hn))

theorem ternary_gap_forces_correction (a b : ℕ) (x y u v c : ℚ)
    (hx : 0 < x) (hy : 0 < y) (hc : 0 < c)
    (hu : 1 ≤ u) (hv : 1 ≤ v)
    (lower : 3 * c * x ≤ y) (upper : c * y ≤ 9 * x)
    (meet : (3 : ℚ)^a * x * u = 3^b * y * v) :
    c ≤ u ∨ c ≤ v := by
  by_contra! reject
  by_cases grades : a ≤ b + 1
  · have slopes : (3 : ℚ)^a ≤ 3^b * 3 := by
      simpa only [pow_succ] using
        (pow_le_pow_right₀ (show (1 : ℚ) ≤ 3 by norm_num) grades)
    have bound : (3 : ℚ)^a * x * c ≤ 3^b * y := by
      calc
        (3 : ℚ)^a * x * c ≤ (3^b * 3) * x * c :=
          mul_le_mul_of_nonneg_right
            (mul_le_mul_of_nonneg_right slopes hx.le) hc.le
        _ = 3^b * (3 * c * x) := by ring
        _ ≤ _ := mul_le_mul_of_nonneg_left lower (by positivity)
    have small : (3 : ℚ)^a * x * u < 3^a * x * c :=
      mul_lt_mul_of_pos_left reject.1 (by positivity)
    have big : (3 : ℚ)^b * y ≤ 3^b * y * v := by
      simpa only [mul_one] using
        (mul_le_mul_of_nonneg_left hv (show 0 ≤ (3 : ℚ)^b * y by positivity))
    exact (not_lt_of_ge (meet.ge)) (lt_of_lt_of_le small (bound.trans big))
  · have grades' : b + 2 ≤ a := by omega
    have slopes : (3 : ℚ)^b * 9 ≤ 3^a := by
      have h := pow_le_pow_right₀ (show (1 : ℚ) ≤ 3 by norm_num) grades'
      rw [pow_add] at h
      norm_num at h ⊢
      exact h
    have bound : (3 : ℚ)^b * y * c ≤ 3^a * x := by
      calc
        (3 : ℚ)^b * y * c = 3^b * (c * y) := by ring
        _ ≤ 3^b * (9 * x) := mul_le_mul_of_nonneg_left upper (by positivity)
        _ = (3^b * 9) * x := by ring
        _ ≤ _ := mul_le_mul_of_nonneg_right slopes hx.le
    have small : (3 : ℚ)^b * y * v < 3^b * y * c :=
      mul_lt_mul_of_pos_left reject.2 (by positivity)
    have big : (3 : ℚ)^a * x ≤ 3^a * x * u := by
      simpa only [mul_one] using
        (mul_le_mul_of_nonneg_left hu (show 0 ≤ (3 : ℚ)^a * x by positivity))
    exact (not_lt_of_ge (meet.le)) (lt_of_lt_of_le small (bound.trans big))

theorem meeting_forces_correction (t n m : ℕ) (c : ℚ)
    (hn : 0 < n) (hm : 0 < m) (hc : 0 < c)
    (lower : 3 * c * (n : ℚ) ≤ m) (upper : c * (m : ℚ) ≤ 9 * n)
    (meet : orbit t n = orbit t m) :
    c ≤ accumulated t n ∨ c ≤ accumulated t m := by
  apply ternary_gap_forces_correction (count oddMark t n)
    (count oddMark t m) (n : ℚ) (m : ℚ)
    (accumulated t n) (accumulated t m) c
    (by exact_mod_cast hn) (by exact_mod_cast hm) hc
    (accumulated_one_le t n hn) (accumulated_one_le t m hm) lower upper
  calc
    _ = (2 : ℚ)^t * (orbit t n : ℚ) := (arithmetic_product t n hn).symm
    _ = (2 : ℚ)^t * (orbit t m : ℚ) := by rw [meet]
    _ = _ := arithmetic_product t m hm

theorem fivefold_meeting_forces_correction (t n : ℕ) (hn : 0 < n)
    (meet : orbit t n = orbit t (5*n)) :
    (5 : ℚ)/3 ≤ accumulated t n ∨ (5 : ℚ)/3 ≤ accumulated t (5*n) := by
  apply meeting_forces_correction t n (5*n) (5/3) hn (by omega) (by norm_num)
    _ _ meet
  · push_cast
    linarith
  · push_cast
    have h : (0 : ℚ) ≤ n := by positivity
    linarith

#print axioms ternary_gap_forces_correction
#print axioms meeting_forces_correction
#print axioms fivefold_meeting_forces_correction

end Collatz.MinimumWindow
