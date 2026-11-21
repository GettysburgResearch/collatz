module

public import HarmonicTransport
public import FiniteResolvent

@[expose] public section

/-!
# An explicit positive unit-mass seed and the unconditional quadratic bound

The seed is `coefficient n = 1 / ((n+1)*(n+2))`. Its finite-mass certificate
uses an exact telescoping identity, with no infinite-series interface.
The final theorem supplies the quadratic transport baseline for every
nonnegative finite incoming history. No improvement on that baseline is
asserted.
-/

namespace CollatzFiniteResolvent

open scoped BigOperators
open CollatzHarmonic

theorem coefficient_telescope (n : ℕ) :
    coefficient n = 1 / ((n : ℝ) + 1) - 1 / ((n : ℝ) + 2) := by
  have h1 : (n : ℝ) + 1 ≠ 0 := ne_of_gt (by positivity)
  have h2 : (n : ℝ) + 2 ≠ 0 := ne_of_gt (by positivity)
  unfold coefficient
  field_simp
  ring

theorem coefficient_prefix (N : ℕ) :
    (∑ n ∈ Finset.range N, coefficient n) = 1 - 1 / ((N : ℝ) + 1) := by
  induction N with
  | zero => norm_num
  | succ N ih =>
      rw [Finset.sum_range_succ, ih, coefficient_telescope]
      simp only [Nat.cast_add, Nat.cast_one]
      ring

theorem coefficient_prefix_le_one (N : ℕ) :
    (∑ n ∈ Finset.range N, coefficient n) ≤ 1 := by
  rw [coefficient_prefix]
  have h : 0 ≤ (1 : ℝ) / ((N : ℝ) + 1) := by positivity
  linarith

/-- Every original integer receives an explicitly positive atom, and every
finite source collection has mass at most one. -/
theorem coefficient_finiteMass : FiniteMass coefficient 1 := by
  constructor
  · intro n
    exact le_of_lt (coefficient_pos n)
  · intro E
    let N := E.sup (fun n => n) + 1
    have hsub : E ⊆ Finset.range N := by
      intro n hn
      apply Finset.mem_range.mpr
      exact Nat.lt_succ_of_le (Finset.le_sup (f := fun n : ℕ => n) hn)
    calc
      (∑ n ∈ E, coefficient n) ≤ ∑ n ∈ Finset.range N, coefficient n :=
        Finset.sum_le_sum_of_subset_of_nonneg hsub
          (fun n _ _ => le_of_lt (coefficient_pos n))
      _ ≤ 1 := coefficient_prefix_le_one N

theorem growth_mul_coefficient (k : ℕ) :
    growth k * coefficient k = coefficient 0 := by
  have hd : ((k : ℝ) + 1) * ((k : ℝ) + 2) ≠ 0 := ne_of_gt (by positivity)
  rw [coefficient_zero]
  unfold growth coefficient
  calc
    ((((k : ℝ) + 1) * ((k : ℝ) + 2)) / 2) *
        (1 / (((k : ℝ) + 1) * ((k : ℝ) + 2))) =
        ((((k : ℝ) + 1) * ((k : ℝ) + 2)) *
          (1 / (((k : ℝ) + 1) * ((k : ℝ) + 2)))) / 2 := by ring
    _ = 1 / 2 := by rw [mul_one_div_cancel hd]

/-- Retaining the depth-k incoming mass alone always proves the quadratic
baseline; a smaller relative budget remains a separate arithmetic claim. -/
theorem quadratic_baseline (b : ℕ → ℝ) (k : ℕ)
    (hb : ∀ j ≤ k, 0 ≤ b j) :
    coefficient 0 * b k ≤ growth k * budget b k := by
  have hterm : coefficient k * b k ≤ budget b k := by
    unfold budget
    have h := Finset.single_le_sum
      (fun r (_hr : r ∈ Finset.range (k + 1)) => by
        have hbr := hb (k - r) (Nat.sub_le k r)
        have hcr := le_of_lt (coefficient_pos (k - r))
        show 0 ≤ coefficient (k - r) * (1 / 2 : ℝ)^r * b (k - r)
        positivity)
      (show 0 ∈ Finset.range (k + 1) by simp)
    simpa only [Nat.sub_zero, pow_zero, mul_one] using h
  calc
    coefficient 0 * b k = (growth k * coefficient k) * b k := by
      rw [growth_mul_coefficient]
    _ = growth k * (coefficient k * b k) := by ring
    _ ≤ growth k * budget b k :=
      mul_le_mul_of_nonneg_left hterm (growth_nonneg k)

end CollatzFiniteResolvent
