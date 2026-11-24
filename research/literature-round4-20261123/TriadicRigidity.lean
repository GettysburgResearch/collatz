import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.RingTheory.Coprime.Lemmas

/-!
# Rigidity of ordinary integral complementary pairs

The original coordinate is positive and integral; the other coordinate may
be any signed integer. Exact complementary steps have an elementary rank
outside the two standard pairs. This proves that an all-time integral
complement of a positive ordinary source exists only at 1 or 2.

The product estimates and the all-odd divisibility proof refine the pinned
PR178 TriadicDualClosure.lean (blob 8eed815f2dc89b16da80d759c965244513082ac4).
The extra marker for x=1 makes the rank apply outside the complete pair
cycle, including original states already equal to 1. No 2-adic existence,
universal triadic candidate, or conjectural Collatz premise is imported.

The accompanying note proves the reduced-denominator stopping statistic,
the logarithmic finite verifier, and its exact rigidity in ordinary
mathematics. Only the declarations below are formalized here.
-/

namespace CollatzShell.TriadicRigidity

set_option autoImplicit false

/-- Exact complementary integer steps. The equations themselves impose the
required opposite input parities. Positivity is supplied in the theorems. -/
def PairStep (x w x' w' : ℤ) : Prop :=
  (2 * x' = 3 * x + 1 ∧ 2 * w' = w) ∨
    (2 * x' = x ∧ 2 * w' = 3 * w + 1)

/-- The two phases of the standard complementary pair cycle. -/
def CyclePair (x w : ℤ) : Prop :=
  (x = 1 ∧ w = 2) ∨ (x = 2 ∧ w = 1)

theorem step_positive {x w x' w' : ℤ}
    (hx : 0 < x) (h : PairStep x w x' w') : 0 < x' := by
  rcases h with ⟨hx', _⟩ | ⟨hx', _⟩ <;> omega

theorem step_nonzero {x w x' w' : ℤ}
    (hw : w ≠ 0) (h : PairStep x w x' w') : w' ≠ 0 := by
  rcases h with ⟨_, hw'⟩ | ⟨_, hw'⟩ <;> omega

/-- No outside integral pair can enter either phase of the standard pair. -/
theorem cycle_of_step {x w x' w' : ℤ}
    (h : PairStep x w x' w') (hc : CyclePair x' w') : CyclePair x w := by
  rcases h with ⟨hx, hw⟩ | ⟨hx, hw⟩ <;>
    rcases hc with ⟨hx', hw'⟩ | ⟨hx', hw'⟩ <;>
    unfold CyclePair <;> omega

/-- The second marker also pays for the plateau at original coordinate 1. -/
def energy (x w : ℤ) : ℕ :=
  (3 * (x * |w|) + (if x = 1 then 1 else 0) +
    (if w = 1 then 1 else 0)).toNat

private theorem markers (x w : ℤ) :
    (0 : ℤ) ≤ (if x = 1 then 1 else 0) + (if w = 1 then 1 else 0) ∧
    (if x = 1 then 1 else 0) + (if w = 1 then 1 else 0 : ℤ) ≤ 2 := by
  split_ifs <;> omega

private theorem energy_lt_of_product_lt {x w x' w' : ℤ}
    (hx : 0 < x) (hw : w ≠ 0)
    (hp : x' * |w'| < x * |w|) : energy x' w' < energy x w := by
  have hP : 0 < x * |w| := mul_pos hx (abs_pos.mpr hw)
  have hm := markers x w
  have hm' := markers x' w'
  unfold energy
  apply (Int.toNat_lt_toNat (by omega)).mpr
  omega

private theorem odd_product_lt {x w x' w' : ℤ}
    (hx : 1 < x) (hw : w ≠ 0)
    (ex : 2 * x' = 3 * x + 1) (ew : 2 * w' = w) :
    x' * |w'| < x * |w| := by
  have ea : 2 * |w'| = |w| := by
    have hh := congrArg abs ew
    simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
  have ep : 4 * (x' * |w'|) = (3 * x + 1) * |w| := by
    calc
      4 * (x' * |w'|) = (2 * x') * (2 * |w'|) := by ring
      _ = (3 * x + 1) * |w| := by rw [ex, ea]
  have hd : 0 < (x - 1) * |w| := mul_pos (by omega) (abs_pos.mpr hw)
  nlinarith

private theorem even_product_lt {x w x' w' : ℤ}
    (hx : 0 < x) (_hw : w ≠ 0) (hw1 : w ≠ 1)
    (ex : 2 * x' = x) (ew : 2 * w' = 3 * w + 1) :
    x' * |w'| < x * |w| := by
  have ea : 2 * |w'| = |3 * w + 1| := by
    have hh := congrArg abs ew
    simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
  have ep : 4 * (x' * |w'|) = x * |3 * w + 1| := by
    calc
      4 * (x' * |w'|) = (2 * x') * (2 * |w'|) := by ring
      _ = x * |3 * w + 1| := by rw [ex, ea]
  have hd : |3 * w + 1| < 4 * |w| := by
    by_cases h : 0 ≤ w
    · rw [abs_of_nonneg h, abs_of_nonneg (by omega : 0 ≤ 3 * w + 1)]
      omega
    · rw [abs_of_neg (by omega : w < 0),
        abs_of_neg (by omega : 3 * w + 1 < 0)]
      omega
  have hh := mul_lt_mul_of_pos_left hd hx
  nlinarith

/-- Every nonzero integral pair outside the two phases loses rank at its
next exact complementary step, even when the original coordinate is 1. -/
theorem step_energy {x w x' w' : ℤ}
    (hx : 0 < x) (hw : w ≠ 0) (hc : ¬ CyclePair x w)
    (h : PairStep x w x' w') : energy x' w' < energy x w := by
  rcases h with ⟨ex, ew⟩ | ⟨ex, ew⟩
  · by_cases hx1 : x = 1
    · subst x
      have hx' : x' = 2 := by omega
      have hw1 : w ≠ 1 := by omega
      have hw'1 : w' ≠ 1 := by
        intro hh
        apply hc
        exact Or.inl ⟨rfl, by omega⟩
      have ea : 2 * |w'| = |w| := by
        have hh := congrArg abs ew
        simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
      subst x'
      unfold energy
      simp only [show (2 : ℤ) ≠ 1 by norm_num, hw1, hw'1,
        ite_false, ite_true, one_mul, add_zero]
      have hpos : 0 < 3 * |w| + 1 := by have := abs_nonneg w; omega
      apply (Int.toNat_lt_toNat (by omega)).mpr
      omega
    · exact energy_lt_of_product_lt hx hw
        (odd_product_lt (by omega) hw ex ew)
  · by_cases hw1 : w = 1
    · subst w
      have hw' : w' = 2 := by omega
      have hx1 : x ≠ 1 := by omega
      have hx'1 : x' ≠ 1 := by
        intro hh
        apply hc
        exact Or.inr ⟨by omega, rfl⟩
      subst w'
      unfold energy
      simp only [hx1, hx'1, show (2 : ℤ) ≠ 1 by norm_num,
        ite_false, ite_true, abs_of_pos (show (0 : ℤ) < 1 by norm_num),
        abs_of_pos (show (0 : ℤ) < 2 by norm_num), mul_one, add_zero]
      apply (Int.toNat_lt_toNat (by omega)).mpr
      omega
    · exact energy_lt_of_product_lt hx hw (even_product_lt hx hw hw1 ex ew)

/-- A finite sequence of exact integer-pair steps exceeding its initial
rank must already start on the standard pair cycle. This finite rank
bound is distinct from the sharper logarithmic bound proved in the note. -/
theorem finite_pair_rigidity (x w : ℕ → ℤ) (k : ℕ)
    (hx : 0 < x 0) (hw : w 0 ≠ 0)
    (hs : ∀ i, i < k → PairStep (x i) (w i) (x (i + 1)) (w (i + 1)))
    (hk : energy (x 0) (w 0) < k) : CyclePair (x 0) (w 0) := by
  by_contra hc
  have haux : ∀ i, i ≤ k →
      0 < x i ∧ w i ≠ 0 ∧ ¬ CyclePair (x i) (w i) ∧
      energy (x i) (w i) + i ≤ energy (x 0) (w 0) := by
    intro i
    induction i with
    | zero => intro _; exact ⟨hx, hw, hc, by omega⟩
    | succ i ih =>
      intro hi
      obtain ⟨hp, hn, hnc, he⟩ := ih (by omega)
      have ht := hs i (by omega)
      have hr := step_energy hp hn hnc ht
      exact ⟨step_positive hp ht, step_nonzero hn ht,
        fun hh => hnc (cycle_of_step ht hh), by omega⟩
  have hh := (haux k (by omega)).2.2.2
  omega

private theorem no_all_odd (x : ℕ → ℤ) (hpos : 0 < x 0)
    (hstep : ∀ i, 2 * x (i + 1) = 3 * x i + 1) : False := by
  have h23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hpow : ∀ k i : ℕ, (2 : ℤ) ^ k ∣ x i + 1 := by
    intro k
    induction k with
    | zero => intro i; simp
    | succ k ih =>
      intro i
      have hd : (2 : ℤ) ^ (k + 1) ∣ 3 * (x i + 1) := by
        obtain ⟨a, ha⟩ := ih (i + 1)
        refine ⟨a, ?_⟩
        rw [pow_succ]
        nlinarith [hstep i]
      exact h23.pow_left.dvd_of_dvd_mul_left hd
  let k := (x 0 + 1).toNat
  have hk : (k : ℤ) = x 0 + 1 := Int.toNat_of_nonneg (by omega)
  have hsmall : (2 : ℤ) ^ k ≤ x 0 + 1 :=
    Int.le_of_dvd (by omega) (hpow k 0)
  have hbig : (k : ℤ) < (2 : ℤ) ^ k := by
    exact_mod_cast (Nat.lt_two_pow_self (n := k))
  omega

/-- Signed integer duals, including the zero case, admit no positive
ordinary all-time complementary source outside 1 and 2. -/
theorem alltime_integral_pair_rigidity (x w : ℕ → ℤ)
    (hx : 0 < x 0)
    (hs : ∀ i, PairStep (x i) (w i) (x (i + 1)) (w (i + 1))) :
    CyclePair (x 0) (w 0) := by
  have hw : w 0 ≠ 0 := by
    intro hz
    have hall : ∀ i, w i = 0 := by
      intro i
      induction i with
      | zero => exact hz
      | succ i ih =>
        rcases hs i with ⟨_, he⟩ | ⟨_, he⟩ <;> omega
    apply no_all_odd x hx
    intro i
    rcases hs i with ⟨he, _⟩ | ⟨_, he⟩
    · exact he
    · have hi := hall i
      omega
  exact finite_pair_rigidity x w (energy (x 0) (w 0) + 1)
    hx hw (fun i _ => hs i) (by omega)

/-- Elementary exponent core for the denominator stopping-time bound.
The separate written argument identifies b with r+1 and supplies the
complete original affine inequality. -/
theorem odd_count_lt_twice_even_count (s b : ℕ) (hb : 0 < b)
    (h : 3 ^ s ≤ 2 ^ (s + b)) : s < 2 * b := by
  by_contra hnot
  have hle : 2 * b ≤ s := by omega
  obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hle
  have h89 : (8 : ℕ) ^ b < 9 ^ b :=
    Nat.pow_lt_pow_left (by decide) (by omega)
  have h23 : (2 : ℕ) ^ d ≤ 3 ^ d := Nat.pow_le_pow_left (by decide) d
  have hp : 0 < (2 : ℕ) ^ d := Nat.pow_pos (by decide)
  have hlt : (8 : ℕ) ^ b * 2 ^ d < 9 ^ b * 3 ^ d :=
    lt_of_lt_of_le (mul_lt_mul_of_pos_right h89 hp) (Nat.mul_le_mul_left _ h23)
  have he : 2 * b + d + b = 3 * b + d := by omega
  rw [hd, he, pow_add, pow_add, pow_mul, pow_mul] at h
  norm_num at h
  omega

theorem clock_lt_three_even_count (s b : ℕ) (hb : 0 < b)
    (h : 3 ^ s ≤ 2 ^ (s + b)) : s + b < 3 * b := by
  have hh := odd_count_lt_twice_even_count s b hb h
  omega

end CollatzShell.TriadicRigidity
