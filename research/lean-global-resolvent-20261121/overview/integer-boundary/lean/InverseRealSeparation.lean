import Mathlib.Analysis.Complex.Exponential
import Mathlib.Topology.Order.MonotoneConvergence
import Mathlib.Tactic

/-!
The real side of an inverse affine word.  The reciprocal budget is an
explicit premise, not an axiom asserting Collatz or an unproved analytic
estimate.  The companion written argument supplies that budget for a
simple ordinary inverse ray by an elementary integer-cylinder count.
-/

noncomputable section

namespace CollatzInverseReal

open Finset Filter
open scoped Topology

def multiplier (c : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∏ i ∈ range n, (3 / c i)

def partialSum (c : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ i ∈ range n, multiplier c i / c i

def correction (q : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∏ i ∈ range n, (1 + 1 / (3 * q (i + 1)))

theorem multiplier_pos (c : ℕ → ℝ) (hc : ∀ i, 0 < c i) (n : ℕ) :
    0 < multiplier c n := by
  apply Finset.prod_pos
  intro i _
  exact div_pos (by norm_num) (hc i)

theorem affine_telescope (q c : ℕ → ℝ)
    (hc : ∀ i, 0 < c i)
    (hedge : ∀ i, c i * q i = 3 * q (i + 1) + 1) (n : ℕ) :
    partialSum c n + multiplier c n * q n = q 0 := by
  induction n with
  | zero => simp [partialSum, multiplier]
  | succ n ih =>
    rw [partialSum, Finset.sum_range_succ]
    change partialSum c n + multiplier c n / c n +
      multiplier c (n + 1) * q (n + 1) = q 0
    have hmul : multiplier c (n + 1) = multiplier c n * (3 / c n) := by
      simp only [multiplier, Finset.prod_range_succ]
    rw [hmul, ← ih]
    have hn := hedge n
    have hc0 : c n ≠ 0 := ne_of_gt (hc n)
    field_simp
    nlinarith [congrArg (fun z : ℝ => multiplier c n * z) hn]

theorem product_telescope (q c : ℕ → ℝ)
    (hq : ∀ i, 0 < q i) (hc : ∀ i, 0 < c i)
    (hedge : ∀ i, c i * q i = 3 * q (i + 1) + 1) (n : ℕ) :
    multiplier c n * q n * correction q n = q 0 := by
  induction n with
  | zero => simp [multiplier, correction]
  | succ n ih =>
    have hmul : multiplier c (n + 1) = multiplier c n * (3 / c n) := by
      simp only [multiplier, Finset.prod_range_succ]
    have hcor : correction q (n + 1) = correction q n *
        (1 + 1 / (3 * q (n + 1))) := by
      simp only [correction, Finset.prod_range_succ]
    rw [hmul, hcor, ← ih]
    have hn := hedge n
    have hc0 : c n ≠ 0 := ne_of_gt (hc n)
    have hq0 : q (n + 1) ≠ 0 := ne_of_gt (hq (n + 1))
    field_simp
    nlinarith [congrArg (fun z : ℝ => multiplier c n * correction q n * z) hn]

theorem correction_le_exp (q : ℕ → ℝ) (hq : ∀ i, 0 < q i)
    (n : ℕ) (B : ℝ)
    (hbudget : (∑ i ∈ range n, 1 / (3 * q (i + 1))) ≤ B) :
    correction q n ≤ Real.exp B := by
  have hnonneg : ∀ i, 0 ≤ 1 / (3 * q (i + 1)) := by
    intro i
    exact one_div_nonneg.mpr (le_of_lt (mul_pos (by norm_num) (hq (i + 1))))
  exact (Real.prod_one_add_le_exp_sum (range n) hnonneg).trans
    (Real.exp_le_exp.mpr hbudget)

theorem partial_separation (q c : ℕ → ℝ)
    (hq : ∀ i, 0 < q i) (hc : ∀ i, 0 < c i)
    (hedge : ∀ i, c i * q i = 3 * q (i + 1) + 1)
    (n : ℕ) (B : ℝ)
    (hbudget : (∑ i ∈ range n, 1 / (3 * q (i + 1))) ≤ B) :
    partialSum c n ≤ q 0 * (1 - Real.exp (-B)) := by
  have hp : 0 ≤ multiplier c n * q n :=
    le_of_lt (mul_pos (multiplier_pos c hc n) (hq n))
  have ht := product_telescope q c hq hc hedge n
  have he := correction_le_exp q hq n B hbudget
  have hbound : q 0 ≤ (multiplier c n * q n) * Real.exp B := by
    rw [← ht]
    exact mul_le_mul_of_nonneg_left he hp
  have htail : q 0 * Real.exp (-B) ≤ multiplier c n * q n := by
    calc
      q 0 * Real.exp (-B) ≤
          (multiplier c n * q n * Real.exp B) * Real.exp (-B) :=
        mul_le_mul_of_nonneg_right hbound (le_of_lt (Real.exp_pos _))
      _ = multiplier c n * q n := by
        rw [mul_assoc, ← Real.exp_add]
        simp
  have ha := affine_telescope q c hc hedge n
  nlinarith

theorem partial_monotone (c : ℕ → ℝ) (hc : ∀ i, 0 < c i) :
    Monotone (partialSum c) := by
  apply monotone_nat_of_le_succ
  intro n
  have hterm : 0 ≤ multiplier c n / c n :=
    le_of_lt (div_pos (multiplier_pos c hc n) (hc n))
  simpa only [partialSum, Finset.sum_range_succ] using
    le_add_of_nonneg_right hterm

theorem exists_real_limit_with_gap (q c : ℕ → ℝ)
    (hq : ∀ i, 0 < q i) (hc : ∀ i, 0 < c i)
    (hedge : ∀ i, c i * q i = 3 * q (i + 1) + 1)
    (B : ℝ)
    (hbudget : ∀ n, (∑ i ∈ range n, 1 / (3 * q (i + 1))) ≤ B) :
    ∃ L : ℝ, Tendsto (partialSum c) atTop (𝓝 L) ∧
      L ≤ q 0 * (1 - Real.exp (-B)) ∧ L < q 0 := by
  have hupper : ∀ n, partialSum c n ≤ q 0 * (1 - Real.exp (-B)) :=
    fun n => partial_separation q c hq hc hedge n B (hbudget n)
  have hbdd : BddAbove (Set.range (partialSum c)) := by
    use q 0 * (1 - Real.exp (-B))
    rintro _ ⟨n, rfl⟩
    exact hupper n
  have hlim := tendsto_atTop_ciSup (partial_monotone c hc) hbdd
  refine ⟨_, hlim, le_of_tendsto' hlim hupper, ?_⟩
  have hle := le_of_tendsto' hlim hupper
  have hpos := mul_pos (hq 0) (Real.exp_pos (-B))
  nlinarith

theorem multiplier_pow_two (e : ℕ → ℕ) (n : ℕ) :
    multiplier (fun i => (2 : ℝ) ^ e i) n =
      3 ^ n / 2 ^ (∑ i ∈ range n, e i) := by
  simp [multiplier, Finset.prod_div_distrib, Finset.prod_pow_eq_pow_sum]

theorem partialSum_pow_two (e : ℕ → ℕ) (n : ℕ) :
    partialSum (fun i => (2 : ℝ) ^ e i) n =
      ∑ i ∈ range n, (3 : ℝ) ^ i / 2 ^ (∑ j ∈ range (i + 1), e j) := by
  apply Finset.sum_congr rfl
  intro i _
  rw [multiplier_pow_two, Finset.sum_range_succ, pow_add, div_div]

/-- This is the literal numen series at one supplied ordinary inverse ray.
The sole analytic input is the displayed finite reciprocal budget. -/
theorem ordinary_inverse_numen_separated (q e : ℕ → ℕ)
    (hq : ∀ i, 0 < q i)
    (hedge : ∀ i, 2 ^ e i * q i = 3 * q (i + 1) + 1)
    (hbudget : ∀ n, (∑ i ∈ range n, 1 / (q (i + 1) : ℝ)) ≤ 200) :
    ∃ L : ℝ,
      Tendsto (fun n => ∑ i ∈ range n,
        (3 : ℝ) ^ i / 2 ^ (∑ j ∈ range (i + 1), e j)) atTop (𝓝 L) ∧
      (q 0 : ℝ) * Real.exp (-(200 / 3 : ℝ)) ≤ (q 0 : ℝ) - L ∧
      L < (q 0 : ℝ) := by
  have hqr : ∀ i, 0 < (q i : ℝ) := by
    intro i
    exact_mod_cast hq i
  have hcr : ∀ i, 0 < (2 : ℝ) ^ e i := by
    intro i
    positivity
  have her : ∀ i, (2 : ℝ) ^ e i * (q i : ℝ) = 3 * (q (i + 1) : ℝ) + 1 := by
    intro i
    exact_mod_cast hedge i
  have hbr : ∀ n, (∑ i ∈ range n, 1 / (3 * (q (i + 1) : ℝ))) ≤ (200 / 3 : ℝ) := by
    intro n
    calc
      (∑ i ∈ range n, 1 / (3 * (q (i + 1) : ℝ))) =
          (∑ i ∈ range n, 1 / (q (i + 1) : ℝ)) / 3 := by
        rw [Finset.sum_div]
        apply Finset.sum_congr rfl
        intro i _
        rw [div_div]
        congr 1
        ring
      _ ≤ (200 / 3 : ℝ) := div_le_div_of_nonneg_right (hbudget n) (by norm_num)
  obtain ⟨L, hlim, hle, hlt⟩ := exists_real_limit_with_gap
    (fun i => (q i : ℝ)) (fun i => (2 : ℝ) ^ e i) hqr hcr her (200 / 3) hbr
  refine ⟨L, ?_, ?_, hlt⟩
  · have hfun : partialSum (fun i => (2 : ℝ) ^ e i) =
        (fun n => ∑ i ∈ range n, (3 : ℝ) ^ i / 2 ^ (∑ j ∈ range (i + 1), e j)) :=
        funext (partialSum_pow_two e)
    simpa only [hfun] using hlim
  · nlinarith

end CollatzInverseReal
