import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Lemmas



/-! PROPOSED Lean finite arithmetic core. NOT compiled or axiom-audited.
The analytic, orbit counting, and finite recognizer consumers are in README.md. -/
namespace Collatz.PhasePacking
set_option autoImplicit false

/-- Total clock and carry cost retain the terminal carry. -/
theorem clock_carry_identity (a b c : ℕ → ℕ) (n : ℕ)
    (h : ∀ i < n, a i + c (i + 1) = b i + 3 * c i) :
    (∑ i ∈ Finset.range n, a i) + c n =
      (∑ i ∈ Finset.range n, b i) + 2 * (∑ i ∈ Finset.range n, c i) + c 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hp := ih (fun i hi => h i (by omega))
    have hs := h n (by omega)
    simp only [Finset.sum_range_succ]
    omega

/-- The exact rational normalization, with the actual ordinary edge. -/
theorem normalized_complete (q r a b c d : ℕ)
    (he : 2 ^ a * r = 3 * q + 1) (hc : a + d = b + 3 * c) :
    2 ^ (b + 3 * c) * r = (3 * q + 1) * 2 ^ d := by
  rw [← hc, pow_add, ← he]
  ring

/-- Dividing by the destination carry removes it from the transition. -/
theorem normalized_edge (q r a b c d : ℕ)
    (he : 2 ^ a * r = 3 * q + 1) (hc : a + d = b + 3 * c) :
    (2 : ℚ) ^ b * ((r : ℚ) / 2 ^ d) ≤ 3 * ((q : ℚ) / 2 ^ c) + 1 := by
  have h : (2 : ℚ) ^ (b + 3 * c) * r = (3 * (q : ℚ) + 1) * 2 ^ d := by
    exact_mod_cast normalized_complete q r a b c d he hc
  have hp : b + 3 * c = (b + c) + 2 * c := by omega
  rw [hp, pow_add, pow_add] at h
  have hpow : (1 : ℚ) ≤ 2 ^ (2 * c) := one_le_pow₀ (by norm_num)
  have hc' : (1 : ℚ) ≤ 2 ^ c := one_le_pow₀ (by norm_num)
  have hleft : (2 : ℚ) ^ b * 2 ^ c * r ≤ (3 * (q : ℚ) + 1) * 2 ^ d := by
    calc
      _ ≤ ((2 : ℚ) ^ b * 2 ^ c * r) * 2 ^ (2 * c) := by
        exact le_mul_of_one_le_right (by positivity) hpow
      _ = _ := by rw [← h]; ring
  have hright : (3 * (q : ℚ) + 1) * 2 ^ d ≤ (3 * (q : ℚ) + 2 ^ c) * 2 ^ d := by
    exact mul_le_mul_of_nonneg_right (by linarith) (by positivity)
  have hh := hleft.trans hright
  have hdc : 0 < (2 : ℚ) ^ d * 2 ^ c := by positivity
  apply (mul_le_mul_iff_left₀ hdc).mp
  calc
    (2 : ℚ) ^ b * ((r : ℚ) / 2 ^ d) * (2 ^ d * 2 ^ c) =
        2 ^ b * 2 ^ c * r := by field_simp
    _ ≤ (3 * (q : ℚ) + 2 ^ c) * 2 ^ d := hh
    _ = (3 * ((q : ℚ) / 2 ^ c) + 1) * (2 ^ d * 2 ^ c) := by field_simp

/-- Height recovered from the integer carry guard, without real logarithms. -/
theorem cubic_height (q u y : ℚ) (hu : 0 < u) (hy : 1 ≤ y)
    (hq : q = y * u) (h : u ^ 3 ≤ 4 * q) : q ^ 2 ≤ 4 * y ^ 3 := by
  have ht : u ^ 2 ≤ 4 * y := by
    apply (mul_le_mul_iff_left₀ hu).mp
    calc
      u ^ 2 * u = u ^ 3 := by ring
      _ ≤ 4 * q := h
      _ = (4 * y) * u := by rw [hq]; ring
  calc
    q ^ 2 = y ^ 2 * u ^ 2 := by rw [hq]; ring
    _ ≤ y ^ 2 * (4 * y) := mul_le_mul_of_nonneg_left ht (pow_nonneg ((by norm_num : (0 : ℚ) ≤ 1).trans hy) 2)
    _ = 4 * y ^ 3 := by ring

/-- Propagation of the difference from a canonical rational trajectory. -/
theorem canonical_difference (y y' z z' : ℚ) (b : ℕ)
    (hy : (2 : ℚ) ^ b * y' ≤ 3 * y + 1)
    (hz : (2 : ℚ) ^ b * z' = 3 * z + 1) :
    (2 : ℚ) ^ b * (y' - z') ≤ 3 * (y - z) := by
  rw [mul_sub, hz]
  linarith

/-- Finite majorant telescope: exact canonical prefix clock. -/
theorem canonical_prefix (y z : ℕ → ℚ) (b : ℕ → ℕ) (n : ℕ)
    (hy : ∀ i < n, (2 : ℚ) ^ b i * y (i + 1) ≤ 3 * y i + 1)
    (hz : ∀ i < n, (2 : ℚ) ^ b i * z (i + 1) = 3 * z i + 1) :
    (2 : ℚ) ^ (∑ i ∈ Finset.range n, b i) * (y n - z n) ≤
      3 ^ n * (y 0 - z 0) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hp := ih (fun i hi => hy i (by omega)) (fun i hi => hz i (by omega))
    have hs := canonical_difference (y n) (y (n+1)) (z n) (z (n+1)) (b n)
      (hy n (by omega)) (hz n (by omega))
    rw [Finset.sum_range_succ, pow_add, pow_succ]
    calc
      _ = (2 : ℚ) ^ (∑ i ∈ Finset.range n, b i) * (2 ^ b n * (y (n+1) - z (n+1))) := by ring
      _ ≤ (2 : ℚ) ^ (∑ i ∈ Finset.range n, b i) * (3 * (y n - z n)) :=
        mul_le_mul_of_nonneg_left hs (by positivity)
      _ = 3 * ((2 : ℚ) ^ (∑ i ∈ Finset.range n, b i) * (y n - z n)) := by ring
      _ ≤ 3 * (3 ^ n * (y 0 - z 0)) := mul_le_mul_of_nonneg_left hp (by norm_num)
      _ = _ := by ring

/-- A full contracting lap bounds every returning normalized coordinate. -/
theorem returning_bound (D A y z : ℚ) (hD : A < D)
    (h : D * (y - z) ≤ A * (y - z)) : y ≤ z := by
  by_contra! hn
  have hp := mul_pos (sub_pos.mpr hD) (sub_pos.mpr hn)
  nlinarith

/-- Complete past affine words identify endpoints below their ternary modulus. -/
theorem past_endpoint_unique (D A C n m q r : ℕ)
    (hc : Nat.Coprime A D) (h1 : D * q = A * n + C)
    (h2 : D * r = A * m + C) (hq : q < A) (hr : r < A) : q = r := by
  have div1 : A ∣ r - q := by
    have he : D * (r - q) = A * (m - n) := by
      simp only [Nat.mul_sub_left_distrib]
      omega
    exact hc.dvd_mul_left.mp ⟨m - n, he⟩
  have div2 : A ∣ q - r := by
    have he : D * (q - r) = A * (n - m) := by
      simp only [Nat.mul_sub_left_distrib]
      omega
    exact hc.dvd_mul_left.mp ⟨n - m, he⟩
  by_contra hn
  rcases lt_or_gt_of_ne hn with hh | hh
  · have := Nat.le_of_dvd (show 0 < r - q by omega) div1
    omega
  · have := Nat.le_of_dvd (show 0 < q - r by omega) div2
    omega

#print axioms clock_carry_identity
#print axioms normalized_complete
#print axioms normalized_edge
#print axioms cubic_height
#print axioms canonical_difference
#print axioms canonical_prefix
#print axioms returning_bound
#print axioms past_endpoint_unique

end Collatz.PhasePacking

namespace Collatz.PhasePacking
#print axioms clock_carry_identity
#print axioms normalized_complete
#print axioms normalized_edge
#print axioms cubic_height
#print axioms canonical_difference
#print axioms canonical_prefix
#print axioms returning_bound
#print axioms past_endpoint_unique
end Collatz.PhasePacking


/-! Round 11 finite arithmetic candidate. Compiler replay is pending.
    No assertion of arbitrary-source realization or Collatz convergence. -/
namespace Collatz.FixedSourceRepetition
set_option autoImplicit false

def denom (b : Bool) : ℕ := if b then 32 else 8
def carry (b : Bool) : ℕ := if b then 5 else 7
def Edge (b : Bool) (q r : ℕ) : Prop := denom b * r = 9 * q + carry b

def extra (s : ℕ → Bool) : ℕ → ℕ
  | 0 => 1
  | n + 1 => extra s n * (if s n then 4 else 1)

def wordDen (s : ℕ → Bool) (m : ℕ) : ℕ := 8 ^ m * extra s m

theorem wordDen_succ (s : ℕ → Bool) (m : ℕ) :
    wordDen s (m + 1) = wordDen s m * denom (s m) := by
  cases hs : s m <;> simp [wordDen, extra, denom, hs, pow_succ] <;> ring

/-- The complete additive carry cancels, without identifying the source states. -/
theorem aligned (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1))) :
    wordDen s m * r m + 9 ^ m * q 0 =
      wordDen s m * q m + 9 ^ m * r 0 := by
  induction m with
  | zero => simp [wordDen, extra, Nat.add_comm]
  | succ m ih =>
    have h := ih (fun i hi => hq i (by omega)) (fun i hi => hr i (by omega))
    have hq' : denom (s m) * q (m + 1) = 9 * q m + carry (s m) := hq m (by omega)
    have hr' : denom (s m) * r (m + 1) = 9 * r m + carry (s m) := hr m (by omega)
    calc
      wordDen s (m + 1) * r (m + 1) + 9 ^ (m + 1) * q 0 =
          wordDen s m * (denom (s m) * r (m + 1)) + 9 * (9 ^ m * q 0) := by
            rw [wordDen_succ, pow_succ]; ring
      _ = wordDen s m * (9 * r m + carry (s m)) + 9 * (9 ^ m * q 0) := by rw [hr']
      _ = 9 * (wordDen s m * r m + 9 ^ m * q 0) + wordDen s m * carry (s m) := by ring
      _ = 9 * (wordDen s m * q m + 9 ^ m * r 0) + wordDen s m * carry (s m) := by rw [h]
      _ = wordDen s m * (9 * q m + carry (s m)) + 9 * (9 ^ m * r 0) := by ring
      _ = wordDen s m * (denom (s m) * q (m + 1)) + 9 * (9 ^ m * r 0) := by rw [hq']
      _ = wordDen s (m + 1) * q (m + 1) + 9 ^ (m + 1) * r 0 := by
            rw [wordDen_succ, pow_succ]; ring

theorem difference_dvd (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1))) :
    8 ^ m ∣ r 0 - q 0 := by
  have he := aligned q r s m hq hr
  have hd : 9 ^ m * (r 0 - q 0) = wordDen s m * (r m - q m) := by
    simp only [Nat.mul_sub_left_distrib]
    omega
  have hc : Nat.Coprime (8 ^ m) (9 ^ m) :=
    ((show Nat.Coprime 8 9 by decide).pow_left _).pow_right _
  apply hc.dvd_mul_left.mp
  refine ⟨extra s m * (r m - q m), ?_⟩
  rw [hd, wordDen]
  ring

theorem small_shared_word (q r : ℕ → ℕ) (s : ℕ → Bool) (m : ℕ)
    (hq : ∀ i < m, Edge (s i) (q i) (q (i + 1)))
    (hr : ∀ i < m, Edge (s i) (r i) (r (i + 1)))
    (hqs : q 0 < 8 ^ m) (hrs : r 0 < 8 ^ m) : q 0 = r 0 := by
  by_contra hn
  rcases lt_or_gt_of_ne hn with h | h
  · have hd := difference_dvd q r s m hq hr
    have hl := Nat.le_of_dvd (show 0 < r 0 - q 0 by omega) hd
    omega
  · have hd := difference_dvd r q s m hr hq
    have hl := Nat.le_of_dvd (show 0 < q 0 - r 0 by omega) hd
    omega

theorem edge_height (b : Bool) (q r : ℕ) (h : Edge b q r) :
    8 * (r + 7) ≤ 9 * (q + 7) := by
  cases b <;> simp [Edge, denom, carry] at h <;> omega

theorem prefix_height (q : ℕ → ℕ) (s : ℕ → Bool) (j : ℕ)
    (h : ∀ i < j, Edge (s i) (q i) (q (i + 1))) :
    8 ^ j * (q j + 7) ≤ 9 ^ j * (q 0 + 7) := by
  induction j with
  | zero => simp
  | succ j ih =>
    have hp := ih (fun i hi => h i (by omega))
    have hs := edge_height (s j) (q j) (q (j + 1)) (h j (by omega))
    calc
      8 ^ (j + 1) * (q (j + 1) + 7) = 8 ^ j * (8 * (q (j + 1) + 7)) := by ring
      _ ≤ 8 ^ j * (9 * (q j + 7)) := Nat.mul_le_mul_left _ hs
      _ = 9 * (8 ^ j * (q j + 7)) := by ring
      _ ≤ 9 * (9 ^ j * (q 0 + 7)) := Nat.mul_le_mul_left _ hp
      _ = 9 ^ (j + 1) * (q 0 + 7) := by ring

theorem two_start_bounds (q : ℕ → ℕ) (s : ℕ → Bool) (H : ℕ)
    (he : ∀ i < 2 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H) : q H < 8 ^ H ∧ q (2 * H) < 8 ^ H := by
  have h1 := prefix_height q s H (fun i hi => he i (by omega))
  have h2 := prefix_height q s (2 * H) he
  have hp1 : (9 : ℕ) ^ H * 4 ^ H ≤ 8 ^ H * 8 ^ H := by
    simp only [← mul_pow]
    exact Nat.pow_le_pow_left (by norm_num) H
  have hp2 : (9 : ℕ) ^ (2 * H) * 4 ^ H ≤ 8 ^ (2 * H) * 8 ^ H := by
    calc
      (9 : ℕ) ^ (2 * H) * 4 ^ H = (9 ^ 2 * 4) ^ H := by rw [pow_mul, mul_pow]
      _ ≤ (8 ^ 2 * 8) ^ H := Nat.pow_le_pow_left (by norm_num) H
      _ = 8 ^ (2 * H) * 8 ^ H := by rw [mul_pow, ← pow_mul]
  have hl1 := lt_of_le_of_lt h1 (lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_left hs (by positivity : 0 < 9 ^ H)) hp1)
  have hl2 := lt_of_le_of_lt h2 (lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_left hs (by positivity : 0 < 9 ^ (2 * H))) hp2)
  constructor
  · by_contra! hn
    have hh := Nat.mul_le_mul_left (8 ^ H) (show 8 ^ H ≤ q H + 7 by omega)
    omega
  · by_contra! hn
    have hh := Nat.mul_le_mul_left (8 ^ (2 * H)) (show 8 ^ H ≤ q (2 * H) + 7 by omega)
    omega

/-- Matching shifted windows force equality of the actual states at their starts. -/
theorem early_repeat (q : ℕ → ℕ) (s : ℕ → Bool) (H : ℕ)
    (he : ∀ i < 3 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H)
    (hm : ∀ i < H, s (H + i) = s (2 * H + i)) : q H = q (2 * H) := by
  have hb := two_start_bounds q s H (fun i hi => he i (by omega)) hs
  have hl : ∀ i < H, Edge (s (H + i)) (q (H + i)) (q (H + (i + 1))) := by
    intro i hi
    simpa [Nat.add_assoc] using he (H + i) (by omega)
  have hr : ∀ i < H, Edge (s (H + i)) (q (2 * H + i)) (q (2 * H + (i + 1))) := by
    intro i hi
    rw [hm i hi]
    simpa [Nat.add_assoc] using he (2 * H + i) (by omega)
  have h := small_shared_word (fun i => q (H + i)) (fun i => q (2 * H + i))
    (fun i => s (H + i)) H hl hr (by simpa using hb.1) (by simpa using hb.2)
  simpa using h

/-- The two literal affine branches have disjoint integer source domains. -/
theorem edge_deterministic (s t : Bool) (q r u : ℕ)
    (hs : Edge s q r) (ht : Edge t q u) : s = t ∧ r = u := by
  cases s <;> cases t <;> simp [Edge, denom, carry] at hs ht ⊢ <;> omega

theorem equal_start_future (q : ℕ → ℕ) (s : ℕ → Bool) (a b t : ℕ)
    (hab : a ≤ b) (he : ∀ i < b + t + 1, Edge (s i) (q i) (q (i + 1)))
    (h0 : q a = q b) : q (a + t) = q (b + t) ∧ s (a + t) = s (b + t) := by
  induction t with
  | zero =>
    have hl := he a (by omega)
    have hr := he b (by omega)
    rw [h0] at hl
    exact ⟨by simpa using h0, by simpa using (edge_deterministic _ _ _ _ _ hl hr).1⟩
  | succ t ih =>
    have hprev := ih (fun i hi => he i (by omega))
    have hl := he (a + t) (by omega)
    have hr := he (b + t) (by omega)
    rw [hprev.1] at hl
    have hnext : q (a + (t + 1)) = q (b + (t + 1)) := by
      simpa [Nat.add_assoc] using (edge_deterministic _ _ _ _ _ hl hr).2
    have hnl := he (a + (t + 1)) (by omega)
    have hnr := he (b + (t + 1)) (by omega)
    rw [hnext] at hnl
    exact ⟨hnext, (edge_deterministic _ _ _ _ _ hnl hnr).1⟩

/-- The finite repeat/mismatch interface for all bit-cap scripts. -/
theorem four_window_reject (q : ℕ → ℕ) (s : ℕ → Bool) (H t : ℕ)
    (he : ∀ i < 4 * H, Edge (s i) (q i) (q (i + 1)))
    (hs : q 0 + 7 < 4 ^ H)
    (hm : ∀ i < H, s (H + i) = s (2 * H + i))
    (ht : t < 2 * H) (hd : s (H + t) ≠ s (2 * H + t)) : False := by
  have h0 := early_repeat q s H (fun i hi => he i (by omega)) hs hm
  have hf := equal_start_future q s H (2 * H) t (by omega)
    (fun i hi => he i (by omega)) h0
  exact hd hf.2

end Collatz.FixedSourceRepetition

namespace Collatz.FixedSourceRepetition
#print axioms denom
#print axioms carry
#print axioms Edge
#print axioms extra
#print axioms wordDen
#print axioms wordDen_succ
#print axioms aligned
#print axioms difference_dvd
#print axioms small_shared_word
#print axioms edge_height
#print axioms prefix_height
#print axioms two_start_bounds
#print axioms early_repeat
#print axioms edge_deterministic
#print axioms equal_start_future
#print axioms four_window_reject
end Collatz.FixedSourceRepetition


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

namespace Collatz.FixedSourceRepeat
#print axioms cancel3_pow2
#print axioms cancel9_pow8
#print axioms eq_zero_of_multiple_small
#print axioms shared_lp_divisibility
#print axioms shared_lp_eq_of_small
#print axioms clock
#print axioms clock_ge
#print axioms shared_gap_full_divisibility
#print axioms shared_gap_eq_of_height
end Collatz.FixedSourceRepeat


/-! Candidate formalization of the finite carry amortization kernel.
Compilation and axiom audit are pending; no universal phase bound is assumed. -/
namespace Collatz.ScalarCarryCocycle

set_option autoImplicit false

private theorem succ_le_two_pow (n : ℕ) : n + 1 ≤ 2 ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ]
    omega

private theorem fourth_bound (n : ℕ) : (n + 1)^4 ≤ 8^(2*n) := by
  have h := succ_le_two_pow n
  calc
    (n + 1)^4 ≤ (2^n)^4 := by gcongr
    _ = 16^n := by
      rw [← pow_mul, Nat.mul_comm n 4, pow_mul]
      norm_num
    _ ≤ 64^n := by gcongr; norm_num
    _ = 8^(2*n) := by rw [pow_mul]; norm_num

/-- All possible carry changes, including arbitrarily large carries.
    The fourth-power potential pays for the cubed clock multiplier. -/
theorem carry_power (c d : ℕ) (hd : d ≤ 3*c+2) :
    8^d * (c+1)^4 ≤ 8^(3*c) * (d+1)^4 := by
  by_cases hdc : d ≤ c
  · have hc := fourth_bound c
    have hp : (1 : ℕ) ≤ (d+1)^4 := by
      have : 0 < (d+1)^4 := by positivity
      omega
    calc
      8^d * (c+1)^4 ≤ 8^c * 8^(2*c) := by gcongr
      _ = 8^(3*c) := by rw [← pow_add]; congr 1; omega
      _ ≤ 8^(3*c) * (d+1)^4 := by
        simpa using Nat.mul_le_mul_left (8^(3*c)) hp
  · by_cases h3 : d ≤ 3*c
    · have hcd : c+1 ≤ d+1 := by omega
      gcongr
    · have hs : d = 3*c+1 ∨ d = 3*c+2 := by omega
      rcases hs with hs | hs
      · rw [hs]
        have hsmall : 2*(c+1) ≤ 3*c+1+1 := by omega
        have hfour : 8*(c+1)^4 ≤ (3*c+1+1)^4 := by
          calc
            8*(c+1)^4 ≤ 16*(c+1)^4 :=
              Nat.mul_le_mul_right _ (by norm_num)
            _ = (2*(c+1))^4 := by ring
            _ ≤ (3*c+1+1)^4 := by gcongr
        calc
          8^(3*c+1)*(c+1)^4 = 8^(3*c)*(8*(c+1)^4) := by
            rw [pow_succ]; ring
          _ ≤ 8^(3*c)*(3*c+1+1)^4 := Nat.mul_le_mul_left _ hfour
      · rw [hs]
        have hfour : 64*(c+1)^4 ≤ (3*c+2+1)^4 := by
          calc
            64*(c+1)^4 ≤ 81*(c+1)^4 :=
              Nat.mul_le_mul_right _ (by norm_num)
            _ = (3*c+2+1)^4 := by ring
        calc
          8^(3*c+2)*(c+1)^4 = 8^(3*c)*(64*(c+1)^4) := by
            rw [pow_add]; norm_num; ring
          _ ≤ 8^(3*c)*(3*c+2+1)^4 := Nat.mul_le_mul_left _ hfour

/-- a = actual gap, b = canonical centered ternary gap, c,d = carries. -/
theorem clock_step (a b c d : ℕ) (ha : 1 ≤ a) (hb : b ≤ 3)
    (he : a+d = b+3*c) :
    8^b * (c+1)^4 ≤ 8^a * (d+1)^4 := by
  have hd : d ≤ 3*c+2 := by omega
  have h := Nat.mul_le_mul_left (8^b) (carry_power c d hd)
  have hl : 8^b*(8^d*(c+1)^4) = 8^d*(8^b*(c+1)^4) := by ring
  have hr : 8^b*(8^(3*c)*(d+1)^4) = 8^d*(8^a*(d+1)^4) := by
    calc
      _ = 8^(b+3*c)*(d+1)^4 := by rw [pow_add]; ring
      _ = 8^(d+a)*(d+1)^4 := by rw [show b+3*c = d+a by omega]
      _ = _ := by rw [pow_add]; ring
  rw [hl, hr] at h
  by_contra hn
  have ht : 8^a*(d+1)^4 < 8^b*(c+1)^4 := lt_of_not_ge hn
  have hm := Nat.mul_lt_mul_of_pos_left ht (show 0 < 8^d by positivity)
  exact (not_lt_of_ge h) hm

def clock (f : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => clock f n + f n

/-- No bound on the carries, horizon, or number of resets. -/
theorem clock_amortized (a b c : ℕ → ℕ)
    (ha : ∀ i, 1 ≤ a i) (hb : ∀ i, b i ≤ 3)
    (he : ∀ i, a i+c (i+1) = b i+3*c i) (n : ℕ) :
    8^(clock b n)*(c 0+1)^4 ≤ 8^(clock a n)*(c n+1)^4 := by
  induction n with
  | zero => simp [clock]
  | succ n ih =>
    have hs := clock_step (a n) (b n) (c n) (c (n+1))
      (ha n) (hb n) (he n)
    calc
      8^(clock b (n+1))*(c 0+1)^4 =
          8^(b n)*(8^(clock b n)*(c 0+1)^4) := by
            simp only [clock, pow_add]; ring
      _ ≤ 8^(b n)*(8^(clock a n)*(c n+1)^4) :=
          Nat.mul_le_mul_left _ ih
      _ = 8^(clock a n)*(8^(b n)*(c n+1)^4) := by ring
      _ ≤ 8^(clock a n)*(8^(a n)*(c (n+1)+1)^4) :=
          Nat.mul_le_mul_left _ hs
      _ = 8^(clock a (n+1))*(c (n+1)+1)^4 := by
            simp only [clock, pow_add]; ring

/-- The same theorem with any prescribed starting clock. -/
theorem clock_amortized_shift (a b c : ℕ → ℕ)
    (ha : ∀ i, 1 ≤ a i) (hb : ∀ i, b i ≤ 3)
    (he : ∀ i, a i+c (i+1) = b i+3*c i) (j n : ℕ) :
    8^(clock (fun i => b (j+i)) n)*(c j+1)^4 ≤
      8^(clock (fun i => a (j+i)) n)*(c (j+n)+1)^4 := by
  have h := clock_amortized (fun i => a (j+i)) (fun i => b (j+i))
    (fun i => c (j+i)) (fun i => ha (j+i)) (fun i => hb (j+i))
    (fun i => by simpa only [Nat.add_assoc] using he (j+i)) n
  simpa using h

#print axioms clock_amortized_shift
end Collatz.ScalarCarryCocycle

namespace Collatz.ScalarCarryCocycle
#print axioms succ_le_two_pow
#print axioms fourth_bound
#print axioms carry_power
#print axioms clock_step
#print axioms clock
#print axioms clock_amortized
#print axioms clock_amortized_shift
end Collatz.ScalarCarryCocycle


/-! Candidate formalization of the coprime-cycle residue kernel.
No existence of an ordinary cycle or of an unrestricted selector is asserted.
Compilation and axiom audit are pending. -/
namespace Collatz.ResidueDefect

set_option autoImplicit false
variable {R : Type*} [CommRing R]

def geom (x : R) : ℕ → R
  | 0 => 0
  | n+1 => geom x n + x^n

theorem geom_mul (x : R) (n : ℕ) :
    (x-1)*geom x n = x^n-1 := by
  induction n with
  | zero => simp [geom]
  | succ n ih =>
    simp only [geom, mul_add, ih, pow_succ]
    ring

/-- In the Bezout-root quotient x^p = 2, the balanced sum is a unit. -/
theorem balanced_unit (x : R) (p : ℕ) (hx : x^p = 2) :
    (x-1)*geom x p = 1 := by
  rw [geom_mul, hx]
  norm_num

theorem exponent_transport (x : R) (p A d i e : ℕ)
    (hp : x^p = 2) (hA : x^A = 3) (he : A*i+e = p*d) :
    (3:R)^i*x^e = (2:R)^d := by
  calc
    _ = (x^A)^i*x^e := by rw [hA]
    _ = x^(A*i+e) := by rw [pow_add, pow_mul]
    _ = x^(p*d) := by rw [he]
    _ = _ := by rw [pow_mul, hp]

theorem cycle_term (x : R) (p A d i e : ℕ)
    (hi : i < p) (hp : x^p = 2) (hA : x^A = 3)
    (he : A*i+e = p*d) :
    (3:R)^(p-1-i)*(2:R)^d = (3:R)^(p-1)*x^e := by
  rw [← exponent_transport x p A d i e hp hA he, ← mul_assoc, ← pow_add]
  rw [show p-1-i+i = p-1 by omega]

/-- A complete inverse witness, rather than a prime-field test. -/
theorem balanced_numerator_inverse (x y : R) (p : ℕ)
    (hp : x^p = 2) (hy : y*3 = 1) :
    ((x-1)*y^(p-1))*((3:R)^(p-1)*geom x p) = 1 := by
  calc
    _ = ((x-1)*geom x p)*(y*3)^(p-1) := by rw [mul_pow]; ring
    _ = 1 := by rw [balanced_unit x p hp, hy]; simp

/-- A single interior interval of elevated coefficients has a trinomial defect. -/
theorem single_interval_defect (x : R) (p u v : ℕ) (hp : x^p = 2) :
    (x-1)*(geom x p + (geom x v-geom x u)) = 1+x^v-x^u := by
  rw [mul_add, mul_sub, balanced_unit x p hp, geom_mul, geom_mul]
  ring

#print axioms balanced_numerator_inverse
#print axioms single_interval_defect
end Collatz.ResidueDefect

namespace Collatz.ResidueDefect
#print axioms geom
#print axioms geom_mul
#print axioms balanced_unit
#print axioms exponent_transport
#print axioms cycle_term
#print axioms balanced_numerator_inverse
#print axioms single_interval_defect
end Collatz.ResidueDefect


/-! Finite arithmetic core for stationary-carry-rigidity-20261124.
    Source candidate, not compiled in the authoring environment.
    All scalar/physical hypotheses are explicit; no convergence axiom. -/

namespace Collatz.StationaryCarryRigidity

def prefixSum (f : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => prefixSum f n + f n

theorem prefixSum_congr (f f' : ℕ → ℕ) :
    ∀ m : ℕ, (∀ i, i < m → f i = f' i) →
      prefixSum f m = prefixSum f' m := by
  intro m
  induction m with
  | zero => intro h; rfl
  | succ m ih =>
    intro h
    simp only [prefixSum]
    rw [ih (fun i hi => h i (Nat.lt_succ_of_lt hi)),
        h m (Nat.lt_succ_self m)]

theorem prefixSum_ge_length (b : ℕ → ℕ) (hb : ∀ i, 1 ≤ b i)
    (m : ℕ) : m ≤ prefixSum b m := by
  induction m with
  | zero => simp [prefixSum]
  | succ m ih =>
    simp only [prefixSum]
    have h := hb m
    omega

/-- Full phase/carry telescope in naturals: no truncated subtraction. -/
theorem carry_telescope (g b k : ℕ → ℕ)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i) (m : ℕ) :
    prefixSum g m + k m =
      prefixSum b m + 2*prefixSum k m + k 0 := by
  induction m with
  | zero => simp [prefixSum]
  | succ m ih =>
    simp only [prefixSum]
    have hs := h m
    omega

/-- A supplied exact integer height budget implies a carry-sum budget.
    H+R is the explicit endpoint-height allowance (including rounding). -/
theorem carry_budget (g b k : ℕ → ℕ)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i)
    (hb : ∀ i, 1 ≤ b i) (m H R : ℕ)
    (hheight : 3*k m + prefixSum g m ≤ H+R) :
    6*prefixSum k m + 3*m ≤ 2*prefixSum g m + H+R := by
  have ht := carry_telescope g b k h m
  have hB := prefixSum_ge_length b hb m
  omega

/-- At fixed clock and phase, the final carry and complete gap word
    are determined by the first m carries. -/
theorem carry_word_determined (g g' b k k' : ℕ → ℕ) (m : ℕ)
    (hm : 0 < m)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i)
    (h' : ∀ i, g' i + k' (i+1) = b i + 3*k' i)
    (hk : ∀ i, i < m → k i = k' i)
    (hA : prefixSum g m = prefixSum g' m) :
    k m = k' m ∧ ∀ i, i < m → g i = g' i := by
  have hsum := prefixSum_congr k k' m hk
  have hz := hk 0 hm
  have ht := carry_telescope g b k h m
  have ht' := carry_telescope g' b k' h' m
  have hend : k m = k' m := by omega
  refine ⟨hend, ?_⟩
  intro i hi
  have hki := hk i hi
  have hkNext : k (i+1) = k' (i+1) := by
    by_cases hn : i+1 < m
    · exact hk (i+1) hn
    · have he : i+1 = m := by omega
      rw [he]
      exact hend
  have e1 := h i
  have e2 := h' i
  omega

/-- Exact forbidden transition used by the KL argument. -/
theorem no_carry_birth {g kNext : ℕ} (hg : 1 ≤ g)
    (h : g+kNext = 1) : kNext = 0 := by
  omega

end Collatz.StationaryCarryRigidity

#print axioms Collatz.StationaryCarryRigidity.carry_telescope
#print axioms Collatz.StationaryCarryRigidity.carry_budget
#print axioms Collatz.StationaryCarryRigidity.carry_word_determined
#print axioms Collatz.StationaryCarryRigidity.no_carry_birth

namespace Collatz.StationaryCarryRigidity
#print axioms prefixSum
#print axioms prefixSum_congr
#print axioms prefixSum_ge_length
#print axioms carry_telescope
#print axioms carry_budget
#print axioms carry_word_determined
#print axioms no_carry_birth
end Collatz.StationaryCarryRigidity


/-! Finite algebraic core for the physical Mahler substitution packet.
    Proposed Lean source: compiler and axiom replay pending.
    No analytic or transcendence theorem is asserted here. -/
namespace MahlerPhysical

def weight (x y : ℚ) : List Bool → ℚ
  | [] => 1
  | false :: w => x * weight x y w
  | true :: w => y * weight x y w

def zeroSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => 1 + x * zeroSum x y w
  | true :: w => y * zeroSum x y w

def oneSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => x * oneSum x y w
  | true :: w => 1 + y * oneSum x y w

theorem telescope (x y : ℚ) (w : List Bool) :
    (1-x) * zeroSum x y w + (1-y) * oneSum x y w =
      1 - weight x y w := by
  induction w with
  | nil => simp [zeroSum, oneSum, weight]
  | cons a w ih =>
    cases a
    · simp only [zeroSum, oneSum, weight]
      linear_combination x * ih
    · simp only [zeroSum, oneSum, weight]
      linear_combination y * ih

theorem weight_append (x y : ℚ) (u v : List Bool) :
    weight x y (u ++ v) = weight x y u * weight x y v := by
  induction u with
  | nil => simp [weight]
  | cons a u ih => cases a <;> simp [weight, ih, mul_assoc]

theorem oneSum_append (x y : ℚ) (u v : List Bool) :
    oneSum x y (u ++ v) =
      oneSum x y u + weight x y u * oneSum x y v := by
  induction u with
  | nil => simp [weight, oneSum]
  | cons a u ih => cases a <;> simp [weight, oneSum, ih] <;> ring

def substitute (u v : List Bool) : List Bool → List Bool
  | [] => []
  | false :: w => u ++ substitute u v w
  | true :: w => v ++ substitute u v w

theorem weight_substitute (x y : ℚ) (u v w : List Bool) :
    weight x y (substitute u v w) =
      weight (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, weight]
  | cons a w ih =>
    cases a <;> simp [substitute, weight_append, weight, ih]

theorem oneSum_substitute (x y : ℚ) (u v w : List Bool) :
    oneSum x y (substitute u v w) =
      oneSum x y u * zeroSum (weight x y u) (weight x y v) w +
      oneSum x y v * oneSum (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, oneSum, zeroSum]
  | cons a w ih =>
    cases a <;> simp [substitute, oneSum_append, oneSum, zeroSum, ih] <;> ring

theorem finite_mahler (x y : ℚ) (u v w : List Bool) :
    (1 - weight x y u) * oneSum x y (substitute u v w) =
      oneSum x y u * (1 - weight (weight x y u) (weight x y v) w) +
      ((1 - weight x y u) * oneSum x y v -
       (1 - weight x y v) * oneSum x y u) *
        oneSum (weight x y u) (weight x y v) w := by
  rw [oneSum_substitute]
  have h := telescope (weight x y u) (weight x y v) w
  linear_combination (oneSum x y u) * h

def affineWord (x y a e : ℚ) : List Bool → ℚ → ℚ
  | [], z => z
  | false :: w, z => a + x * affineWord x y a e w z
  | true :: w, z => e + y * affineWord x y a e w z

theorem affine_expand (x y a e : ℚ) (w : List Bool) (z : ℚ) :
    affineWord x y a e w z =
      a * zeroSum x y w + e * oneSum x y w + weight x y w * z := by
  induction w with
  | nil => simp [affineWord, zeroSum, oneSum, weight]
  | cons i w ih =>
    cases i <;> simp [affineWord, zeroSum, oneSum, weight, ih] <;> ring

theorem eliminate_zero (x y a e u v : ℚ)
    (hx : 1-x ≠ 0) (h : (1-x)*u + (1-y)*v = 1) :
    a*u + e*v = a/(1-x) + (e-a*(1-y)/(1-x))*v := by
  have hu : u = (1-(1-y)*v)/(1-x) := by
    apply (eq_div_iff hx).2
    linear_combination h
  rw [hu]
  ring

#print axioms telescope
#print axioms oneSum_substitute
#print axioms finite_mahler
#print axioms affine_expand
#print axioms eliminate_zero

end MahlerPhysical

namespace MahlerPhysical
#print axioms weight
#print axioms zeroSum
#print axioms oneSum
#print axioms telescope
#print axioms weight_append
#print axioms oneSum_append
#print axioms substitute
#print axioms weight_substitute
#print axioms oneSum_substitute
#print axioms finite_mahler
#print axioms affineWord
#print axioms affine_expand
#print axioms eliminate_zero
end MahlerPhysical


/-!
FINITE KERNEL CANDIDATES ONLY. Lean/Lake/Elan were not available in the
authoring environment. Compiler and transitive axiom audit are pending.
The cyclic extremum selection, cyclotomic determinant, and full ordinary
parity attachment are supplied separately in the written proof.
-/

namespace Collatz.TwoSidedPacking

/-- The two actual edges into a cyclic minimum and maximum suffice. -/
theorem cycle_spread_bound
    (N M d lo hi cmin cmax u v cu cv : ℤ)
    (hM : 0 ≤ M) (hd : 0 ≤ d)
    (hu : lo ≤ u) (hv : v ≤ hi)
    (hcu : cmin ≤ cu) (hcv : cv ≤ cmax)
    (edgeLo : N * lo = M * u + d * cu)
    (edgeHi : N * hi = M * v + d * cv) :
    (N-M)*(hi-lo) ≤ d*(cmax-cmin) := by
  have h1 := mul_le_mul_of_nonneg_left hu hM
  have h2 := mul_le_mul_of_nonneg_left hv hM
  have h3 := mul_le_mul_of_nonneg_left hcu hd
  have h4 := mul_le_mul_of_nonneg_left hcv hd
  nlinarith only [h1,h2,h3,h4,edgeLo,edgeHi]

/-- Consecutive sorted distinct numerators in a G-lattice cost at
least G each. The finite ordering is a separate consumer. -/
theorem lattice_step (G x y z : ℤ) (hG : 0 < G)
    (hxy : x < y) (hz : y-x = G*z) : G ≤ y-x := by
  have hzpos : 0 < z := by
    by_contra! hn
    have hprod := mul_nonpos_of_nonneg_of_nonpos (le_of_lt hG) hn
    linarith only [hxy,hz,hprod]
  have hz1 : 1 ≤ z := by omega
  have hh := mul_le_mul_of_nonneg_left hz1 (le_of_lt hG)
  nlinarith only [hh,hz]

theorem spaced_span (G : ℤ) (x : ℕ → ℤ) (r : ℕ)
    (h : ∀ i < r, G ≤ x (i+1)-x i) :
    G*(r : ℤ) ≤ x r-x 0 := by
  induction r with
  | zero => simp
  | succ r ih =>
    have hp : ∀ i < r, G ≤ x (i+1)-x i := by
      intro i hi
      exact h i (Nat.lt_trans hi (Nat.lt_succ_self r))
    have hprev := ih hp
    have hlast := h r (Nat.lt_succ_self r)
    rw [Nat.cast_succ]
    nlinarith only [hprev,hlast]

/-- Exact cancellation of the common binary/ternary lattice factor. -/
theorem denominator_packing_core (D G d delta span : ℤ) (r : ℕ)
    (hD : 0 ≤ D) (hG : 0 < G)
    (hspan : G*(r : ℤ) ≤ span)
    (hcarry : D*span ≤ d*G*delta) :
    D*(r : ℤ) ≤ d*delta := by
  have hh := mul_le_mul_of_nonneg_left hspan hD
  have hc : G*(D*(r : ℤ)) ≤ G*(d*delta) := by
    nlinarith only [hh,hcarry]
  by_contra! hbad
  have hstrict := mul_lt_mul_of_pos_left hbad hG
  linarith only [hc,hstrict]

/-- Common prefix and suffix cancel exactly from carry differences. -/
theorem composed_carry_difference
    (Mmid Msuf Npre Nmid Cpre Cmid1 Cmid2 Csuf : ℤ) :
    (Mmid*Msuf*Cpre+Npre*Msuf*Cmid1+Npre*Nmid*Csuf) -
    (Mmid*Msuf*Cpre+Npre*Msuf*Cmid2+Npre*Nmid*Csuf) =
    Npre*Msuf*(Cmid1-Cmid2) := by ring

/-- Integer-coordinate shadow of the L block. -/
theorem shadow_L (q r y z : ℤ)
    (edge : 8*r=9*q+7)
    (hq : 83*y=60*q+5) (hr : 83*z=60*r+5) :
    8*z=9*y+5 := by omega

/-- Integer-coordinate shadow of the P block. -/
theorem shadow_P (q r y z : ℤ)
    (edge : 32*r=9*q+5)
    (hq : 83*y=60*q+5) (hr : 83*z=60*r+5) :
    32*z=9*y+5 := by omega

theorem shadow_smaller_odd (q y : ℤ) (hq : 0 < q)
    (hy : 83*y=60*q+5) : 0 < y ∧ 4*y<3*q+1 ∧ y%2=1 := by
  omega

theorem shadow_exists (q : ℤ) (h : ∃ k : ℤ, q+7=83*k) :
    ∃ y : ℤ, 83*y=60*q+5 := by
  obtain ⟨k,hk⟩ := h
  exact ⟨60*k-5, by omega⟩

theorem shifted83_L (q r : ℤ) (edge : 8*r=9*q+7)
    (h : 83 ∣ q+7) : 83 ∣ r+7 := by omega

theorem shifted83_P (q r : ℤ) (edge : 32*r=9*q+5)
    (h : 83 ∣ q+7) : 83 ∣ r+7 := by omega

/-- Full odd endpoints of either shadow block force its first gap
to be exactly one. The next quotient is the literal odd endpoint. -/
theorem shadow_first_gap (y z N : ℤ)
    (hN : N=8 ∨ N=32) (hy : y%2=1) (hz : z%2=1)
    (h : N*z=9*y+5) :
    (3*y+1)%4=2 ∧ ∃ mid : ℤ,
      2*mid=3*y+1 ∧ mid%2=1 ∧ N*z=2*(3*mid+1) := by
  rcases hN with hN | hN
  · subst N
    refine ⟨by omega, (3*y+1)/2, ?_, ?_, ?_⟩ <;> omega
  · subst N
    refine ⟨by omega, (3*y+1)/2, ?_, ?_, ?_⟩ <;> omega

/-- Finite Bezout torus identity for the noncoprime norm.
Use x,y as units modulo the full cyclotomic gcd, not a field. -/
theorem bezout_torus {G : Type*} [CommGroup G]
    (x y : G) (a b u v : ℤ) (h : b*u-a*v=1) :
    (x^u*y^(-v))^b=x*(x^a*y^(-b))^v ∧
    (x^u*y^(-v))^a=y*(x^a*y^(-b))^u := by
  have h1 : u*b=1+a*v := by nlinarith only [h]
  have h2 : (-v)*b=(-b)*v := by ring
  have h3 : u*a=a*u := by ring
  have h4 : (-v)*a=1+(-b)*u := by nlinarith only [h]
  constructor
  · simp only [mul_zpow, ← zpow_mul, h1, h2, zpow_add, zpow_one, mul_assoc]
  · simp only [mul_zpow, ← zpow_mul, h3, h4, zpow_add, zpow_one]
    ac_rfl

#print axioms cycle_spread_bound
#print axioms lattice_step
#print axioms spaced_span
#print axioms denominator_packing_core
#print axioms composed_carry_difference
#print axioms shadow_L
#print axioms shadow_P
#print axioms shadow_smaller_odd
#print axioms shadow_exists
#print axioms shifted83_L
#print axioms shifted83_P
#print axioms shadow_first_gap
#print axioms bezout_torus

end Collatz.TwoSidedPacking

namespace Collatz.TwoSidedPacking
#print axioms cycle_spread_bound
#print axioms lattice_step
#print axioms spaced_span
#print axioms denominator_packing_core
#print axioms composed_carry_difference
#print axioms shadow_L
#print axioms shadow_P
#print axioms shadow_smaller_odd
#print axioms shadow_exists
#print axioms shifted83_L
#print axioms shifted83_P
#print axioms shadow_first_gap
#print axioms bezout_torus
end Collatz.TwoSidedPacking
