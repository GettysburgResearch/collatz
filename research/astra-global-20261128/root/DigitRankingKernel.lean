import CoreBranching
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Tactic.Linarith

/-! Finite algebra and actual ordinary paths used by the digit-ranking proof.
The analytic invariant-measure reduction and Host's theorem are not assumed
as Lean axioms and are not formalized in this file. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.DigitRankingKernel

open CoreBranching
open scoped BigOperators

/-- Discrete integration by parts, retaining both endpoint terms. -/
theorem weighted_telescoping (w h : ℕ → ℝ) (n : ℕ) :
    (∑ i ∈ Finset.range n, w i * (h (i + 1) - h i)) =
      w n * h n - w 0 * h 0 -
        ∑ i ∈ Finset.range n, (w (i + 1) - w i) * h (i + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    simp only [Finset.sum_range_succ]
    rw [ih]
    ring

/-- A local coboundary with polynomial weights leaves an explicit boundary
and a first-difference weight. -/
theorem weighted_coboundary (w h g : ℕ → ℝ) (β : ℝ) (n : ℕ)
    (hg : ∀ i < n, g i = β + h (i + 1) - h i) :
    (∑ i ∈ Finset.range n, w i * g i) =
      β * (∑ i ∈ Finset.range n, w i) + w n * h n - w 0 * h 0 -
        ∑ i ∈ Finset.range n, (w (i + 1) - w i) * h (i + 1) := by
  have he : (∑ i ∈ Finset.range n, w i * g i) =
      β * (∑ i ∈ Finset.range n, w i) +
        ∑ i ∈ Finset.range n, w i * (h (i + 1) - h i) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro i hi
    rw [hg i (Finset.mem_range.mp hi)]
    ring
  rw [he, weighted_telescoping]
  ring

/-- The first difference of a degree-(d+1) monomial contains only powers
through degree d, with exact binomial coefficients. -/
theorem power_first_difference (d : ℕ) (x : ℝ) :
    (x + 1) ^ (d + 1) - x ^ (d + 1) =
      ∑ j ∈ Finset.range (d + 1), ((d + 1).choose j : ℝ) * x ^ j := by
  have h := add_pow x (1 : ℝ) (d + 1)
  simp only [one_pow, mul_one] at h
  rw [Finset.sum_range_succ] at h
  simp only [Nat.choose_self, Nat.cast_one, mul_one] at h
  rw [h]
  simp only [Finset.sum_congr rfl (fun i _ => mul_comm (x ^ i) ((d + 1).choose i : ℝ))]
  ring

/-- A polynomial in the whole numeral length can be written as a sum of
lower-degree position weights. -/
theorem length_power_sum (d n : ℕ) :
    (n : ℝ) ^ (d + 1) =
      ∑ i ∈ Finset.range n, (((i : ℝ) + 1) ^ (d + 1) - (i : ℝ) ^ (d + 1)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ← ih]
    push_cast
    ring

theorem step_pred_double (m : ℕ) (hm : 0 < m) :
    step (2 * m - 1) = 3 * m - 1 := by
  have he : 2 * m - 1 = 2 * (m - 1) + 1 := by omega
  rw [he, step_odd]
  omega

theorem pred_double_odd (m : ℕ) (hm : 0 < m) : (2 * m - 1) % 2 = 1 := by
  have he : 2 * m - 1 = 2 * (m - 1) + 1 := by omega
  rw [he]
  omega

/-- A literal all-odd run, with an arbitrary positive multiplier. -/
theorem all_odd_run (J q : ℕ) (hq : 0 < q) :
    run J (2 ^ J * q - 1) = 3 ^ J * q - 1 := by
  induction J generalizing q with
  | zero => simp [run]
  | succ J ih =>
    have hp : 0 < 2 ^ J * q := Nat.mul_pos (pow_pos (by decide) J) hq
    have hi : 2 ^ (J + 1) * q = 2 * (2 ^ J * q) := by rw [pow_succ]; ring
    have ho : 3 * (2 ^ J * q) = 2 ^ J * (3 * q) := by ring
    simp only [run, hi, step_pred_double _ hp, ho]
    rw [ih (3 * q) (by omega)]
    congr 1
    rw [pow_succ]
    ring

/-- Summing the proposed odd loss along that genuine run. Every departure
remains above the original floor. -/
theorem all_odd_loss (F : ℕ → ℝ) (ε : ℝ) (floor : ℕ)
    (loss : ∀ n, floor < n → n % 2 = 1 → F (step n) ≤ F n - ε)
    (J q : ℕ) (hq : 0 < q) (hf : floor < 2 ^ J * q - 1) :
    F (3 ^ J * q - 1) ≤ F (2 ^ J * q - 1) - ε * (J : ℝ) := by
  induction J generalizing q with
  | zero => simp
  | succ J ih =>
    have hp : 0 < 2 ^ J * q := Nat.mul_pos (pow_pos (by decide) J) hq
    have hi : 2 ^ (J + 1) * q = 2 * (2 ^ J * q) := by rw [pow_succ]; ring
    have ho : 2 ^ J * (3 * q) = 3 * (2 ^ J * q) := by ring
    have hf0 : floor < 2 * (2 ^ J * q) - 1 := by simpa only [hi] using hf
    have hs := loss (2 * (2 ^ J * q) - 1) hf0 (pred_double_odd _ hp)
    rw [step_pred_double _ hp] at hs
    have hnext : floor < 2 ^ J * (3 * q) - 1 := by rw [ho]; omega
    have ht := ih (3 * q) (by omega) hnext
    rw [ho] at ht
    have he : 3 ^ (J + 1) * q = 3 ^ J * (3 * q) := by rw [pow_succ]; ring
    rw [hi, he]
    push_cast
    linarith

/-- A bounded perturbation of any monotone height cannot pay more than
twice its error along an increasing all-odd native run. -/
theorem monotone_odd_budget (F g : ℕ → ℝ) (C ε : ℝ) (floor J q : ℕ)
    (mono : Monotone g)
    (lower : ∀ n, g n - C ≤ F n)
    (upper : ∀ n, F n ≤ g n + C)
    (loss : ∀ n, floor < n → n % 2 = 1 → F (step n) ≤ F n - ε)
    (hq : 0 < q) (hf : floor < 2 ^ J * q - 1) :
    ε * (J : ℝ) ≤ 2 * C := by
  have hh : 2 ^ J * q - 1 ≤ 3 ^ J * q - 1 := by
    have hp := Nat.mul_le_mul_right q (Nat.pow_le_pow_left (show (2 : ℕ) ≤ 3 by decide) J)
    omega
  have hg := mono hh
  have hl := lower (3 ^ J * q - 1)
  have hu := upper (2 ^ J * q - 1)
  have hd := all_odd_loss F ε floor loss J q hq hf
  linarith

/-- The exact obstruction used after the analytic reduction to a
nondecreasing length term plus a bounded remainder. -/
theorem no_monotone_odd_ranking (F g : ℕ → ℝ) (C ε : ℝ) (floor : ℕ)
    (mono : Monotone g)
    (lower : ∀ n, g n - C ≤ F n)
    (upper : ∀ n, F n ≤ g n + C)
    (positive : 0 < ε) :
    ¬ (∀ n, floor < n → n % 2 = 1 → F (step n) ≤ F n - ε) := by
  intro loss
  obtain ⟨J, hJ⟩ := exists_nat_gt (max (2 * C / ε) ((floor : ℝ) + 1))
  have hratio : 2 * C / ε < (J : ℝ) := lt_of_le_of_lt (le_max_left _ _) hJ
  have hjfloor : (floor : ℝ) + 1 < (J : ℝ) := lt_of_le_of_lt (le_max_right _ _) hJ
  have hn : floor + 1 < J := by exact_mod_cast hjfloor
  have hp : J < 2 ^ J := Nat.lt_two_pow_self
  have hf : floor < 2 ^ J * 1 - 1 := by omega
  have hb := monotone_odd_budget F g C ε floor J 1 mono lower upper loss (by decide) hf
  have hm : 2 * C < (J : ℝ) * ε := (div_lt_iff₀ positive).mp hratio
  nlinarith

end Collatz.DigitRankingKernel
