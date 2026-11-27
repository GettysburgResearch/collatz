import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Lean.Elab.Tactic.Omega

/-!
Integer separation of two odd phases following the same accelerated clocks.
The recurrence includes an arbitrary common translation, so it applies to
reduced rational cycles after clearing their common denominator.
-/

namespace ClockShadow

def elapsed (gap : ℕ → ℕ) (n : ℕ) : ℕ :=
  ∑ i ∈ Finset.range n, gap i

theorem shared_edge {a d x₀ x₁ y₀ y₁ : ℤ}
    (hx : a * x₁ = 3 * x₀ + d) (hy : a * y₁ = 3 * y₀ + d) :
    a * (x₁ - y₁) = 3 * (x₀ - y₀) := by
  linear_combination hx - hy

theorem shared_segment (gap : ℕ → ℕ) (z : ℕ → ℤ) (n : ℕ)
    (h : ∀ i < n, 2 ^ gap i * z (i + 1) = 3 * z i) :
    2 ^ elapsed gap n * z n = 3 ^ n * z 0 := by
  induction n with
  | zero => simp [elapsed]
  | succ n ih =>
    have hprev := ih (fun i hi => h i (by omega))
    have hlast := h n (by omega)
    calc
      2 ^ elapsed gap (n + 1) * z (n + 1) =
          2 ^ elapsed gap n * (2 ^ gap n * z (n + 1)) := by
            rw [elapsed, Finset.sum_range_succ, pow_add, mul_assoc]
            rfl
      _ = 3 * (2 ^ elapsed gap n * z n) := by rw [hlast]; ring
      _ = 3 ^ (n + 1) * z 0 := by rw [hprev, pow_succ]; ring

theorem same_clock_relation (gap : ℕ → ℕ) (x y : ℕ → ℤ) (d : ℤ)
    (n : ℕ) (hx : ∀ i < n, 2 ^ gap i * x (i + 1) = 3 * x i + d)
    (hy : ∀ i < n, 2 ^ gap i * y (i + 1) = 3 * y i + d) :
    2 ^ elapsed gap n * (x n - y n) = 3 ^ n * (x 0 - y 0) :=
  shared_segment gap (fun i => x i - y i) n
    (fun i hi => shared_edge (hx i hi) (hy i hi))

private theorem coprime_two_three : IsCoprime (2 : ℤ) 3 :=
  ⟨-1, 1, by norm_num⟩

theorem integer_pair_parameter (e n : ℕ) {s t : ℤ}
    (h : (2 : ℤ) ^ e * t = 3 ^ n * s) :
    ∃ u : ℤ, s = 2 ^ e * u ∧ t = 3 ^ n * u := by
  have hcop : IsCoprime ((2 : ℤ) ^ e) (3 ^ n) := coprime_two_three.pow
  have hd : (2 : ℤ) ^ e ∣ 3 ^ n * s := ⟨t, h.symm⟩
  obtain ⟨u, hu⟩ := hcop.dvd_of_dvd_mul_left hd
  refine ⟨u, hu, ?_⟩
  have hmul : (2 : ℤ) ^ e * t = 2 ^ e * (3 ^ n * u) := by
    rw [h, hu]; ring
  exact mul_left_cancel₀ (by positivity : (2 : ℤ) ^ e ≠ 0) hmul

/-- Every phase numerator is odd. The terminal difference is therefore even. -/
theorem odd_pair_parameter (e n : ℕ) {s t : ℤ}
    (h : (2 : ℤ) ^ e * t = 3 ^ n * s) (heven : 2 ∣ t) :
    ∃ u : ℤ, s = 2 ^ (e + 1) * u ∧ t = 2 * 3 ^ n * u := by
  obtain ⟨u, hs, ht⟩ := integer_pair_parameter e n h
  have hc : IsCoprime (2 : ℤ) (3 ^ n) := coprime_two_three.pow_right
  have hdiv : (2 : ℤ) ∣ 3 ^ n * u := ht ▸ heven
  obtain ⟨v, hv⟩ := hc.dvd_of_dvd_mul_left hdiv
  exact ⟨v, by rw [hs, hv, pow_succ]; ring, by rw [ht, hv]; ring⟩

/-- The common dyadic suffix and ternary prefix divide simultaneously. -/
theorem shared_middle (pre suf turns : ℕ) {start mid u : ℤ}
    (hs : start = 2 ^ (pre + suf + 1) * u)
    (hm : (2 : ℤ) ^ pre * mid = 3 ^ turns * start) :
    mid = 2 ^ (suf + 1) * 3 ^ turns * u := by
  apply mul_left_cancel₀ (by positivity : (2 : ℤ) ^ pre ≠ 0)
  rw [hm, hs, Nat.add_assoc pre suf 1, pow_add]
  ring

theorem positive_match_lower (pre suf turns : ℕ) {start mid u : ℤ}
    (hs : start = 2 ^ (pre + suf + 1) * u)
    (hm : (2 : ℤ) ^ pre * mid = 3 ^ turns * start) (hu : u ≠ 0) :
    2 ^ (suf + 1) * 3 ^ turns ≤ |mid| := by
  rw [shared_middle pre suf turns hs hm, abs_mul, abs_of_nonneg (by positivity)]
  have hone : 1 ≤ |u| := by have := abs_pos.mpr hu; omega
  exact le_mul_of_one_le_right (by positivity) hone

/-- Finite growth estimate for arbitrary (possibly non-integer) positive phases. -/
theorem forward_growth (x : ℕ → ℚ) (n : ℕ)
    (h : ∀ i < n, x (i + 1) + 1 ≤ (3 / 2 : ℚ) * (x i + 1)) :
    x n + 1 ≤ (3 / 2 : ℚ) ^ n * (x 0 + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    calc
      x (n + 1) + 1 ≤ (3 / 2 : ℚ) * (x n + 1) := h n (by omega)
      _ ≤ (3 / 2 : ℚ) * ((3 / 2 : ℚ) ^ n * (x 0 + 1)) :=
        mul_le_mul_of_nonneg_left (ih (fun i hi => h i (by omega))) (by norm_num)
      _ = _ := by rw [pow_succ]; ring

/-- Iterating the prefix-time cap for a fixed number of clean pieces. -/
theorem geometric_chain {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (t : ℕ → K) (n : ℕ) (κ cost : K) (hk : 0 ≤ κ)
    (h : ∀ i < n, t (i + 1) ≤ (1 + κ) * t i + cost) :
    κ * t n + cost ≤ (1 + κ) ^ n * (κ * t 0 + cost) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hprev := ih (fun i hi => h i (by omega))
    calc
      κ * t (n + 1) + cost ≤ (1 + κ) * (κ * t n + cost) := by
        have hmul := mul_le_mul_of_nonneg_left (h n (by omega)) hk
        nlinarith
      _ ≤ (1 + κ) * ((1 + κ) ^ n * (κ * t 0 + cost)) :=
        mul_le_mul_of_nonneg_left hprev (by linarith)
      _ = _ := by rw [pow_succ]; ring

#print axioms shared_edge
#print axioms shared_segment
#print axioms same_clock_relation
#print axioms coprime_two_three
#print axioms integer_pair_parameter
#print axioms odd_pair_parameter
#print axioms shared_middle
#print axioms positive_match_lower
#print axioms forward_growth
#print axioms geometric_chain

end ClockShadow
