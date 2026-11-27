import AffineCorrection

/-! An unconditional finite cycle certificate in the critical parity tail.

The clock and count tests use natural-number powers only. No density law,
Gaussian approximation, or convergence hypothesis occurs in this file.
-/

namespace Collatz.MinimumWindow

theorem correction_square_bound {n : ℕ} (hn : 0 < n) :
    correction n ^ 2 ≤ ((n : ℚ) + 1) / n := by
  have hp : (0 : ℚ) < n := by exact_mod_cast hn
  have h1 : (1 : ℚ) ≤ n := by exact_mod_cast hn
  unfold correction
  split
  · simp only [one_pow]
    apply (le_div_iff₀ hp).2
    linarith
  · rw [div_pow]
    apply (div_le_div_iff₀ (by positivity) hp).2
    nlinarith [sq_nonneg ((n : ℚ) - 1)]

private theorem square_set_product (s : Finset ℕ)
    (pos : ∀ x ∈ s, 0 < x) :
    (∏ x ∈ s, correction x ^ 2) ≤ (s.card : ℚ) + 1 := by
  induction s using Finset.strongInductionOn with
  | _ s ih =>
    by_cases hs : s.Nonempty
    · let m := s.max' hs
      have hm : m ∈ s := Finset.max'_mem s hs
      have hmp := pos m hm
      have subs : s ⊆ Finset.Icc 1 m := by
        intro x hx
        exact Finset.mem_Icc.mpr ⟨pos x hx, Finset.le_max' _ _ hx⟩
      have hc : s.card ≤ m := by simpa using Finset.card_le_card subs
      have ht := ih (s.erase m) (Finset.erase_ssubset hm)
        (fun x hx => pos x (Finset.mem_of_mem_erase hx))
      have hcard : (s.erase m).card + 1 = s.card := Finset.card_erase_add_one hm
      have hcardq : ((s.erase m).card : ℚ) + 1 = s.card := by exact_mod_cast hcard
      rw [hcardq] at ht
      have hmq : (0 : ℚ) < m := by exact_mod_cast hmp
      have hcm : (s.card : ℚ) ≤ m := by exact_mod_cast hc
      calc
        (∏ x ∈ s, correction x ^ 2) =
            (∏ x ∈ s.erase m, correction x ^ 2) * correction m ^ 2 :=
          (Finset.prod_erase_mul s (fun x => correction x ^ 2) hm).symm
        _ ≤ (s.card : ℚ) * correction m ^ 2 :=
          mul_le_mul_of_nonneg_right ht (sq_nonneg _)
        _ ≤ (s.card : ℚ) * (((m : ℚ) + 1) / m) :=
          mul_le_mul_of_nonneg_left (correction_square_bound hmp) (by positivity)
        _ ≤ _ := by
          rw [← mul_div_assoc]
          apply (div_le_iff₀ hmq).2
          nlinarith
    · simp [Finset.not_nonempty_iff_eq_empty.mp hs]

theorem simple_correction_square {t n : ℕ} (hn : 0 < n)
    (simple : Set.InjOn (fun i => orbit i n) (Finset.range t : Set ℕ)) :
    accumulated t n ^ 2 ≤ (t : ℚ) + 1 := by
  let s := (Finset.range t).image (fun i => orbit i n)
  have hs : ∀ x ∈ s, 0 < x := by
    intro x hx
    obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp hx
    exact orbit_positive i hn
  have hp := square_set_product s hs
  have heq : (∏ x ∈ s, correction x ^ 2) = accumulated t n ^ 2 := by
    rw [Finset.prod_image simple]
    simp only [accumulated, Finset.prod_pow]
  have hc : s.card = t := by
    change ((Finset.range t).image (fun i => orbit i n)).card = t
    rw [Finset.card_image_of_injOn simple, Finset.card_range]
  rwa [heq, hc] at hp

theorem ternary_dominates_square (d : ℕ) (hd : 1 ≤ d) :
    4 * (d ^ 2 + 1) ≤ 3 ^ (d + 1) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hd
  induction k with
  | zero => norm_num
  | succ k ih =>
    have hpow : 3 ^ (1 + (k + 1) + 1) = 3 * 3 ^ (1 + k + 1) := by
      ring
    rw [hpow]
    nlinarith

/-- The exact clock inequality holds at
`t = floor (2 log X / log (4/3))`. A positive square-root deficit
already forces a repeated ordinary state within the observed prefix. -/
theorem critical_tail_not_simple (X n t d : ℕ)
    (hn : 0 < n) (hnX : n ≤ X) (hd : 1 ≤ d)
    (hdef : t = 2 * count oddMark t n + d) (ht : t ≤ d ^ 2)
    (hclock : X ^ 2 * 3 ^ (t + 1) < 4 ^ (t + 1)) :
    ¬ Set.InjOn (fun i => orbit i n) (Finset.range t : Set ℕ) := by
  intro simple
  have hb := simple_correction_square hn simple
  have he := arithmetic_product t n hn
  have hz : (1 : ℚ) ≤ orbit t n := by
    exact_mod_cast orbit_positive t hn
  have hnXq : (n : ℚ) ≤ X := by exact_mod_cast hnX
  have hclockq : (X : ℚ) ^ 2 * 3 ^ (t + 1) < 4 ^ (t + 1) := by
    exact_mod_cast hclock
  have hsquare : (4 : ℚ) ^ t * (orbit t n : ℚ) ^ 2 =
      (9 : ℚ) ^ (count oddMark t n) * (n : ℚ) ^ 2 * accumulated t n ^ 2 := by
    have h := congrArg (fun z : ℚ => z ^ 2) he
    have htwo : ((2 : ℚ)^t)^2 = 4^t := by
      rw [← pow_mul, Nat.mul_comm t 2, pow_mul]
      norm_num
    have hthree : ((3 : ℚ)^(count oddMark t n))^2 = 9^(count oddMark t n) := by
      rw [← pow_mul, Nat.mul_comm (count oddMark t n) 2, pow_mul]
      norm_num
    simpa only [mul_pow, htwo, hthree] using h
  have hbound : (4 : ℚ) ^ t ≤
      (9 : ℚ) ^ (count oddMark t n) * (X : ℚ) ^ 2 * ((t : ℚ) + 1) := by
    calc
      (4 : ℚ)^t ≤ 4^t * (orbit t n : ℚ)^2 := by
        have hh : (1 : ℚ) ≤ (orbit t n : ℚ)^2 := by nlinarith
        nlinarith [pow_nonneg (by norm_num : (0 : ℚ) ≤ 4) t]
      _ = _ := hsquare
      _ ≤ (9 : ℚ)^(count oddMark t n) * (n : ℚ)^2 * ((t : ℚ)+1) :=
        mul_le_mul_of_nonneg_left hb (by positivity)
      _ ≤ _ := by
        have hh : (n : ℚ)^2 ≤ (X : ℚ)^2 := by nlinarith
        exact mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left hh (by positivity)) (by positivity)
  have hpoly : 4 * (t + 1) ≤ 3 ^ (d + 1) :=
    (Nat.mul_le_mul_left 4 (Nat.add_le_add_right ht 1)).trans
      (ternary_dominates_square d hd)
  have hpolyq : (4 : ℚ) * ((t : ℚ) + 1) ≤ 3 ^ (d + 1) := by
    exact_mod_cast hpoly
  have hsplit : (3 : ℚ) ^ (t + 1) =
      (9 : ℚ) ^ (count oddMark t n) * 3 ^ (d + 1) := by
    rw [hdef]
    rw [show 2 * count oddMark t n + d + 1 =
      2 * count oddMark t n + (d + 1) by omega, pow_add, pow_mul]
    norm_num
  have hfinal : (4 : ℚ) ^ (t + 1) ≤ (X : ℚ)^2 * 3 ^ (t + 1) := by
    calc
      (4 : ℚ)^(t+1) = 4 * 4^t := by ring
      _ ≤ 4 * ((9 : ℚ)^(count oddMark t n) * (X : ℚ)^2 * ((t : ℚ)+1)) :=
        mul_le_mul_of_nonneg_left hbound (by norm_num)
      _ = (9 : ℚ)^(count oddMark t n) * (X : ℚ)^2 * (4*((t : ℚ)+1)) := by ring
      _ ≤ (9 : ℚ)^(count oddMark t n) * (X : ℚ)^2 * 3^(d+1) :=
        mul_le_mul_of_nonneg_left hpolyq (by positivity)
      _ = _ := by rw [hsplit]; ring
  exact (not_lt_of_ge hfinal) hclockq

#print axioms correction_square_bound
#print axioms simple_correction_square
#print axioms ternary_dominates_square
#print axioms critical_tail_not_simple

end Collatz.MinimumWindow
