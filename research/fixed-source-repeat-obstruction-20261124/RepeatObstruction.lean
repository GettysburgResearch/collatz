import Mathlib

/-!
Finite integer core for the repeated-factor obstruction.
Compiler replay is pending: this is proposed Lean source, not an executed audit.
All variables in the finite affine equations are ordinary integers.
-/

namespace Collatz.FixedSourceRepeat

private theorem cancel3_pow2 (a : ℕ) (u z : ℤ)
    (h : 3 * u = (2 : ℤ)^a * z) :
    ∃ v : ℤ, u = (2 : ℤ)^a * v := by
  induction a generalizing u z with
  | zero =>
      exact ⟨u, by simp⟩
  | succ a ih =>
      have h' : 3 * u = 2 * ((2 : ℤ)^a * z) := by
        rw [h, pow_succ]
        ring
      have hu : u = 2 * (u / 2) := by omega
      have h'' : 3 * (u / 2) = (2 : ℤ)^a * z := by
        linarith only [h', hu]
      obtain ⟨v, hv⟩ := ih (u / 2) z h''
      refine ⟨v, ?_⟩
      calc
        u = 2 * (u / 2) := hu
        _ = 2 * ((2 : ℤ)^a * v) := by rw [hv]
        _ = (2 : ℤ)^(a + 1) * v := by rw [pow_succ]; ring

private theorem cancel9_pow8 (a : ℕ) (u z : ℤ)
    (h : 9 * u = (8 : ℤ)^a * z) :
    ∃ v : ℤ, u = (8 : ℤ)^a * v := by
  induction a generalizing u z with
  | zero =>
      exact ⟨u, by simp⟩
  | succ a ih =>
      have h' : 9 * u = 8 * ((8 : ℤ)^a * z) := by
        rw [h, pow_succ]
        ring
      have hu : u = 8 * (u / 8) := by omega
      have h'' : 9 * (u / 8) = (8 : ℤ)^a * z := by
        linarith only [h', hu]
      obtain ⟨v, hv⟩ := ih (u / 8) z h''
      refine ⟨v, ?_⟩
      calc
        u = 8 * (u / 8) := hu
        _ = 8 * ((8 : ℤ)^a * v) := by rw [hv]
        _ = (8 : ℤ)^(a + 1) * v := by rw [pow_succ]; ring

theorem eq_zero_of_multiple_small (a u : ℤ) (ha : 0 < a)
    (hm : ∃ z : ℤ, u = a * z)
    (hlo : -a < u) (hhi : u < a) : u = 0 := by
  obtain ⟨z, hz⟩ := hm
  have hz0 : z = 0 := by
    by_contra hn
    by_cases hp : 0 < z
    · have hp' : (1 : ℤ) ≤ z := by omega
      have hm' := mul_le_mul_of_nonneg_left hp' (le_of_lt ha)
      have hbad : a ≤ u := by simpa [hz] using hm'
      omega
    · have hp' : z ≤ (-1 : ℤ) := by omega
      have hm' := mul_le_mul_of_nonneg_left hp' (le_of_lt ha)
      have hbad : u ≤ -a := by simpa [hz] using hm'
      omega
  rw [hz, hz0, mul_zero]

/-- A complete shared L/P factor forces divisibility of the original
integer-coordinate difference, with no resampling of either source. -/
theorem shared_lp_divisibility (d : ℤ) (Y : ℕ → ℤ)
    (s : ℕ → ℕ)
    (step : ∀ n, (8 : ℤ) * 4^(s n) * Y (n+1) =
      9 * Y n + 166 * d * (s n : ℤ))
    (m i j : ℕ) (same : ∀ k, k < m → s (i+k) = s (j+k)) :
    ∃ z : ℤ, Y j - Y i = (8 : ℤ)^m * z := by
  induction m generalizing i j with
  | zero =>
      exact ⟨Y j - Y i, by simp⟩
  | succ m ih =>
      have h0 : s i = s j := by simpa using same 0 (by omega)
      have hs : ∀ k, k < m → s ((i+1)+k) = s ((j+1)+k) := by
        intro k hk
        have h := same (k+1) (by omega)
        have hi : (i+1)+k = i+(k+1) := by omega
        have hj : (j+1)+k = j+(k+1) := by omega
        simpa only [hi, hj] using h
      obtain ⟨z, hz⟩ := ih (i+1) (j+1) hs
      have hi := step i
      have hj := step j
      rw [← h0] at hj
      have hd : 9 * (Y j - Y i) =
          (8 : ℤ) * 4^(s i) * (Y (j+1) - Y (i+1)) := by
        linear_combination hi - hj
      have he : 9 * (Y j - Y i) =
          (8 : ℤ)^(m+1) * ((4 : ℤ)^(s i) * z) := by
        rw [hd, hz, pow_succ]
        ring
      exact cancel9_pow8 (m+1) (Y j - Y i) _ he

theorem shared_lp_eq_of_small (d : ℤ) (Y : ℕ → ℤ)
    (s : ℕ → ℕ)
    (step : ∀ n, (8 : ℤ) * 4^(s n) * Y (n+1) =
      9 * Y n + 166 * d * (s n : ℤ))
    (m i j : ℕ) (same : ∀ k, k < m → s (i+k) = s (j+k))
    (hlo : -((8 : ℤ)^m) < Y j - Y i)
    (hhi : Y j - Y i < (8 : ℤ)^m) : Y i = Y j := by
  have h := eq_zero_of_multiple_small ((8 : ℤ)^m) (Y j - Y i)
    (by positivity) (shared_lp_divisibility d Y s step m i j same) hlo hhi
  omega

/-- Total binary clock of m consecutive odd transitions. -/
def clock (g : ℕ → ℕ) (i : ℕ) : ℕ → ℕ
  | 0 => 0
  | m+1 => g i + clock g (i+1) m

theorem clock_ge (g : ℕ → ℕ) (hg : ∀ i, 1 ≤ g i) (i m : ℕ) :
    m ≤ clock g i m := by
  induction m generalizing i with
  | zero => simp [clock]
  | succ m ih =>
      simp only [clock]
      have h1 := hg i
      have h2 := ih (i+1)
      omega

/-- Full binary modulus, including terminal oddness. The affine recurrence
is the literal accelerated map equation and not an independent endpoint model. -/
theorem shared_gap_full_divisibility (q : ℕ → ℤ) (g : ℕ → ℕ)
    (step : ∀ n, (2 : ℤ)^(g n) * q (n+1) = 3 * q n + 1)
    (odd : ∀ n, ∃ z : ℤ, q n = 2*z+1)
    (m i j : ℕ) (same : ∀ k, k < m → g (i+k) = g (j+k)) :
    ∃ z : ℤ, q j - q i = (2 : ℤ)^(clock g i m+1) * z := by
  induction m generalizing i j with
  | zero =>
      obtain ⟨u, hu⟩ := odd i
      obtain ⟨v, hv⟩ := odd j
      refine ⟨v-u, ?_⟩
      simp only [clock, Nat.zero_add, pow_one]
      linarith
  | succ m ih =>
      have h0 : g i = g j := by simpa using same 0 (by omega)
      have hs : ∀ k, k < m → g ((i+1)+k) = g ((j+1)+k) := by
        intro k hk
        have h := same (k+1) (by omega)
        have hi : (i+1)+k = i+(k+1) := by omega
        have hj : (j+1)+k = j+(k+1) := by omega
        simpa only [hi, hj] using h
      obtain ⟨z, hz⟩ := ih (i+1) (j+1) hs
      have hi := step i
      have hj := step j
      rw [← h0] at hj
      have hd : 3 * (q j - q i) =
          (2 : ℤ)^(g i) * (q (j+1) - q (i+1)) := by
        linear_combination hi - hj
      have he : 3 * (q j - q i) =
          (2 : ℤ)^(clock g i (m+1)+1) * z := by
        rw [hd, hz]
        have hc : clock g i (m+1)+1 =
            g i + (clock g (i+1) m+1) := by simp [clock, Nat.add_assoc]
        rw [hc, pow_add]
        ring
      exact cancel3_pow2 (clock g i (m+1)+1) (q j - q i) _ he

theorem shared_gap_eq_of_height (q : ℕ → ℤ) (g : ℕ → ℕ)
    (step : ∀ n, (2 : ℤ)^(g n) * q (n+1) = 3 * q n + 1)
    (odd : ∀ n, ∃ z : ℤ, q n = 2*z+1)
    (positive_gap : ∀ n, 1 ≤ g n)
    (m i j : ℕ) (same : ∀ k, k < m → g (i+k) = g (j+k))
    (hpi : 0 < q i) (hpj : 0 < q j)
    (hqi : q i ≤ (2 : ℤ)^(m+1))
    (hqj : q j ≤ (2 : ℤ)^(m+1)) : q i = q j := by
  obtain ⟨z, hz⟩ := shared_gap_full_divisibility q g step odd m i j same
  have hc := clock_ge g positive_gap i m
  let r := clock g i m - m
  have hr : clock g i m + 1 = (m+1) + r := by
    dsimp [r]
    omega
  have hm : ∃ w : ℤ, q j - q i = (2 : ℤ)^(m+1) * w := by
    refine ⟨(2 : ℤ)^r*z, ?_⟩
    rw [hz, hr, pow_add]
    ring
  have h := eq_zero_of_multiple_small ((2 : ℤ)^(m+1)) (q j-q i)
    (by positivity) hm (by omega) (by omega)
  omega

#print axioms eq_zero_of_multiple_small
#print axioms shared_lp_divisibility
#print axioms shared_lp_eq_of_small
#print axioms clock_ge
#print axioms shared_gap_full_divisibility
#print axioms shared_gap_eq_of_height

end Collatz.FixedSourceRepeat
