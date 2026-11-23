import Mathlib.Tactic

/-!
Finite numerical estimates for a rational complementary candidate.
The complete visit/pigeonhole certificate is a separate written theorem.
The variables A and A' in the step estimates stand for absolute numerator
values. Their exact branch equations/inequalities are explicit hypotheses.
-/

namespace CollatzRationalExcursions

theorem abs_numerator_bounds (a a' q : ℤ) (hq : 0 ≤ q)
    (h : 2 * a' = 3 * a + q) :
    3 * |a| - q ≤ 2 * |a'| ∧ 2 * |a'| ≤ 3 * |a| + q := by
  rcases le_total 0 a with ha | ha <;>
    rcases le_total 0 a' with hb | hb
  · simp only [abs_of_nonneg ha, abs_of_nonneg hb]
    constructor <;> omega
  · simp only [abs_of_nonneg ha, abs_of_nonpos hb]
    constructor <;> omega
  · simp only [abs_of_nonpos ha, abs_of_nonneg hb]
    constructor <;> omega
  · simp only [abs_of_nonpos ha, abs_of_nonpos hb]
    constructor <;> omega

theorem large_even_contraction (n n' A A' q : ℚ)
    (hn : 0 ≤ n) (hq : 1 ≤ q) (hA : q + 1 ≤ A)
    (hx : 2 * n' = n) (hy : 2 * A' ≤ 3 * A + q) :
    4 * (q + 1) * (n' * A') ≤ (4 * q + 3) * (n * A) := by
  have hn' : 0 ≤ n' := by linarith
  have h1 : 4 * (n' * A') ≤ n * (3 * A + q) := by
    have hm := mul_le_mul_of_nonneg_left hy hn'
    nlinarith
  have h2 := mul_le_mul_of_nonneg_left h1 (by linarith : 0 ≤ q + 1)
  have h3 : 0 ≤ n * q * (A - (q + 1)) :=
    mul_nonneg (mul_nonneg hn (by linarith)) (by linarith)
  nlinarith

theorem large_odd_contraction (n n' A A' q : ℚ)
    (hn : 2 ≤ n) (hq : 1 ≤ q) (hA : 0 ≤ A)
    (hx : 2 * n' = 3 * n + 1) (hy : 2 * A' = A) :
    4 * (q + 1) * (n' * A') ≤ (4 * q + 3) * (n * A) := by
  have hp : 4 * (n' * A') = (3 * n + 1) * A := by
    calc
      4 * (n' * A') = (2 * n') * (2 * A') := by ring
      _ = (3 * n + 1) * A := by rw [hx, hy]
  have hg : 0 ≤ q * (n - 1) - 1 := by
    have hh := mul_nonneg (by linarith : 0 ≤ q - 1)
      (by linarith : 0 ≤ n - 1)
    nlinarith
  have hh := mul_nonneg hA hg
  have hs := congrArg (fun z : ℚ => (q + 1) * z) hp
  nlinarith

theorem small_step_growth (n n' A' q : ℚ)
    (hn' : 0 ≤ n') (hq : 1 ≤ q) (hx : n' ≤ 2 * n)
    (hy : A' ≤ 2 * q) :
    n' * max 1 A' ≤ 4 * q * n := by
  have hm : max 1 A' ≤ 2 * q := max_le (by linarith) hy
  have h1 := mul_le_mul_of_nonneg_left hm hn'
  have h2 := mul_le_mul_of_nonneg_right hx (by linarith : 0 ≤ 2 * q)
  nlinarith

/-- A block of b contractions b/(b+1) decreases a value by at least half. -/
theorem block_half (b : ℕ) (hb : 1 ≤ b) :
    ((b : ℚ) / ((b : ℚ) + 1)) ^ b ≤ (1 / 2 : ℚ) := by
  have hbpos : 0 < (b : ℚ) := by exact_mod_cast (by omega : 0 < b)
  have hbne : (b : ℚ) ≠ 0 := ne_of_gt hbpos
  have hb1 : (b : ℚ) + 1 ≠ 0 := by linarith
  have hber := one_add_mul_le_pow (a := 1 / (b : ℚ))
    (by have hh : (0 : ℚ) ≤ 1 / (b : ℚ) := by positivity
        linarith : (-2 : ℚ) ≤ 1 / (b : ℚ)) b
  have htwo : (2 : ℚ) ≤ (1 + 1 / (b : ℚ)) ^ b := by
    norm_num [hbne] at hber
    simpa only [one_div] using hber
  have hr : 0 ≤ ((b : ℚ) / ((b : ℚ) + 1)) ^ b := by positivity
  have hm := mul_le_mul_of_nonneg_right htwo hr
  have hid : (1 + 1 / (b : ℚ)) ^ b *
      ((b : ℚ) / ((b : ℚ) + 1)) ^ b = 1 := by
    rw [← mul_pow]
    have hi : (1 + 1 / (b : ℚ)) * ((b : ℚ) / ((b : ℚ) + 1)) = 1 := by
      field_simp
    rw [hi]
    simp
  rw [hid] at hm
  linarith

theorem geometric_decay (v : ℕ → ℚ) (rho : ℚ) (hr : 0 ≤ rho)
    (N : ℕ) (hstep : ∀ k < N, v (k + 1) ≤ rho * v k) :
    v N ≤ rho ^ N * v 0 := by
  induction N with
  | zero => simp
  | succ N ih =>
    have hp := ih (fun k hk => hstep k (by omega))
    calc
      v (N + 1) ≤ rho * v N := hstep N (by omega)
      _ ≤ rho * (rho ^ N * v 0) := mul_le_mul_of_nonneg_left hp hr
      _ = rho ^ (N + 1) * v 0 := by rw [pow_succ]; ring

/-- An integer-valued positive potential cannot stay in the large region this long. -/
theorem no_long_high_run (v : ℕ → ℚ) (b L : ℕ) (hb : 1 ≤ b)
    (hv : 0 ≤ v 0) (hsize : v 0 < (2 : ℚ) ^ L)
    (hend : 1 ≤ v (b * L))
    (hstep : ∀ k < b * L,
      v (k + 1) ≤ ((b : ℚ) / ((b : ℚ) + 1)) * v k) : False := by
  have hr : 0 ≤ (b : ℚ) / ((b : ℚ) + 1) := by positivity
  have hd := geometric_decay v _ hr (b * L) hstep
  have hh := block_half b hb
  have hpow : (((b : ℚ) / ((b : ℚ) + 1)) ^ b) ^ L ≤ (1 / 2 : ℚ) ^ L := by
    gcongr
  rw [pow_mul] at hd
  have hm := mul_le_mul_of_nonneg_right hpow hv
  have hlt := mul_lt_mul_of_pos_left hsize (pow_pos (by norm_num : (0 : ℚ) < 1 / 2) L)
  have hid : (1 / 2 : ℚ) ^ L * (2 : ℚ) ^ L = 1 := by
    rw [← mul_pow]
    norm_num
  rw [hid] at hlt
  nlinarith

end CollatzRationalExcursions
