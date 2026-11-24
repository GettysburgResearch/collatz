module

public import Mathlib.Algebra.Order.Field.Rat
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite arithmetic core from PR 182 round 12, with the ordered cancellation lemma updated for Mathlib v4.34.1.
The analytic, orbit counting, and finite recognizer consumers are in README.md. -/
@[expose] public section

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
    _ ≤ y ^ 2 * (4 * y) := mul_le_mul_of_nonneg_left ht (pow_nonneg (zero_le_one.trans hy) 2)
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
