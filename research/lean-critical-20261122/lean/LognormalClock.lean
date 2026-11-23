import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! A single full-clock weight with every finite polynomial moment.

These estimates support the original-source reference in RETURN_ATTACK.md.
No uniform estimate in the return index is assumed or concluded here.
-/

namespace CollatzShell.LognormalClock

open Filter

noncomputable def weight (j : ℕ) : ℝ :=
  Real.exp (- (Real.log ((j : ℝ) + 2)) ^ 2)

theorem weight_pos (j : ℕ) : 0 < weight j := Real.exp_pos _

theorem weight_le_one (j : ℕ) : weight j ≤ 1 := by
  exact Real.exp_le_one_iff.mpr (neg_nonpos.mpr (sq_nonneg _))

/-- Past the explicit logarithmic threshold, any chosen polynomial
moment is bounded by the summable inverse-square sequence. -/
theorem polynomial_bound (r : ℕ) {x : ℝ} (hx : 1 ≤ x)
    (threshold : (r : ℝ) + 2 ≤ Real.log x) :
    x ^ r * Real.exp (-(Real.log x)^2) ≤ x ^ (-2 : ℝ) := by
  have xpos : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have lognonneg : 0 ≤ Real.log x := Real.log_nonneg hx
  rw [← Real.rpow_natCast, Real.rpow_def_of_pos xpos,
    Real.rpow_def_of_pos xpos, ← Real.exp_add]
  apply Real.exp_le_exp.mpr
  nlinarith [mul_le_mul_of_nonneg_left threshold lognonneg]

/-- Every time moment of the same clock weight is finite. -/
theorem all_time_moments (r : ℕ) :
    Summable (fun j : ℕ => ((j : ℝ) + 2)^r * weight j) := by
  have majorant : Summable (fun j : ℕ => ((j : ℝ) + 2)^(-2 : ℝ)) := by
    have h := (Real.summable_one_div_nat_add_rpow 2 2).mpr (by norm_num)
    apply h.congr
    intro j
    rw [abs_of_pos (by positivity : 0 < (j : ℝ) + 2)]
    rw [one_div, Real.rpow_neg (by positivity : 0 ≤ (j : ℝ) + 2) (2 : ℝ)]
  have top : Tendsto (fun j : ℕ => Real.log ((j : ℝ) + 2)) atTop atTop :=
    Real.tendsto_log_atTop.comp
      (tendsto_atTop_add_const_right atTop 2 tendsto_natCast_atTop_atTop)
  apply majorant.of_norm_bounded_eventually_nat
  filter_upwards [top.eventually (eventually_ge_atTop ((r : ℝ) + 2))] with j hj
  rw [Real.norm_eq_abs, abs_of_nonneg
    (mul_nonneg (pow_nonneg (by positivity) r) (weight_pos j).le)]
  exact polynomial_bound r (by have h := Nat.cast_nonneg (α := ℝ) j; linarith) hj

/-- The quadratic logarithmic cost is smaller than a linear source cost. -/
theorem log_square_le {x : ℝ} (hx : 1 ≤ x) :
    (Real.log x)^2 ≤ x - 1 := by
  have xp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have ly : 0 ≤ Real.log x := Real.log_nonneg hx
  have taylor := Real.sum_le_exp_of_nonneg ly 4
  norm_num [Finset.sum_range_succ, Nat.factorial] at taylor
  rw [Real.exp_log xp] at taylor
  have correction := mul_nonneg ly
    (add_nonneg (sq_nonneg (Real.log x - 3/2)) (by norm_num : (0 : ℝ) ≤ 15/4))
  nlinarith

/-- An explicit bound uniform in the original source height. The coefficient
may depend on the fixed return index through `a`; that dependence is retained. -/
theorem logarithmic_cost_absorption {a c L : ℝ}
    (ha : 0 ≤ a) (hc : 0 ≤ c) (hL : 1 ≤ L) :
    a * (c + Real.log L)^2 ≤
      (L-1)/2 + 2*a*(c + Real.log (1+4*a))^2 := by
  let K : ℝ := 1+4*a
  have hK : 1 ≤ K := by dsimp [K]; linarith
  have Kpos : 0 < K := lt_of_lt_of_le zero_lt_one hK
  have Lpos : 0 < L := lt_of_lt_of_le zero_lt_one hL
  have logL : 0 ≤ Real.log L := Real.log_nonneg hL
  have logK : 0 ≤ Real.log K := Real.log_nonneg hK
  change a*(c+Real.log L)^2 ≤ (L-1)/2 + 2*a*(c+Real.log K)^2
  by_cases small : L ≤ K
  · have logs : Real.log L ≤ Real.log K := Real.log_le_log Lpos small
    have sqbound : (c+Real.log L)^2 ≤ (c+Real.log K)^2 := by nlinarith
    have weighted := mul_le_mul_of_nonneg_left sqbound ha
    have extra := mul_nonneg ha (sq_nonneg (c+Real.log K))
    nlinarith
  · have zlarge : 1 ≤ L/K := (le_div_iff₀ Kpos).mpr (by linarith)
    have zsq := log_square_le zlarge
    have factor : K*(L/K)=L := mul_div_cancel₀ L Kpos.ne'
    have split : Real.log L=Real.log K+Real.log (L/K) := by
      rw [Real.log_div Lpos.ne' Kpos.ne']
      ring
    have sumsq : (c+Real.log L)^2 ≤
        2*(c+Real.log K)^2 + 2*(Real.log (L/K))^2 := by
      rw [split]
      nlinarith [sq_nonneg ((c+Real.log K)-Real.log (L/K))]
    have scaled := mul_le_mul_of_nonneg_left sumsq ha
    have tail := mul_le_mul_of_nonneg_left zsq (by positivity : 0 ≤ 2*a)
    have floor : 0 ≤ L/K-1 := by linarith
    have relation : L=(1+4*a)*(L/K) := by simpa [K] using factor.symm
    nlinarith

theorem reciprocal_weight (j : ℕ) (a : ℝ) :
    (weight j)^(-a)=Real.exp (a*(Real.log ((j : ℝ)+2))^2) := by
  rw [Real.rpow_def_of_pos (weight_pos j)]
  simp only [weight, Real.log_exp]
  congr 1
  ring

/-- The exact source-power absorption used in the complete-fiber Lp bound. -/
theorem exponential_cost_bound {a c x : ℝ}
    (ha : 0 ≤ a) (hc : 0 ≤ c) (hx : 1 ≤ x) :
    Real.exp (a*(c+Real.log (1+Real.log x))^2) ≤
      Real.exp (2*a*(c+Real.log (1+4*a))^2) * x^(1/2 : ℝ) := by
  have xp : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have logx : 0 ≤ Real.log x := Real.log_nonneg hx
  have cost := logarithmic_cost_absorption ha hc
    (show 1 ≤ 1+Real.log x by linarith)
  calc
    Real.exp (a*(c+Real.log (1+Real.log x))^2) ≤
        Real.exp (((1+Real.log x)-1)/2 +
          2*a*(c+Real.log (1+4*a))^2) := Real.exp_le_exp.mpr cost
    _ = Real.exp (2*a*(c+Real.log (1+4*a))^2) * x^(1/2 : ℝ) := by
      rw [Real.rpow_def_of_pos xp, ← Real.exp_add]
      congr 1
      ring

/-- Quantified concentration loss under a clock whose logarithm grows by
at most a factor five. This is an exact scalar identity consequence, with
the strict parameter gap retained. -/
theorem quadratic_parameter_loss {a b z y : ℝ} (gap : 25*b < a) :
    b*(5*z+y)^2-a*z^2 ≤ a*b/(a-25*b)*y^2 := by
  have positive_gap : 0 < a-25*b := by linarith
  rw [div_mul_eq_mul_div]
  apply (le_div_iff₀ positive_gap).mpr
  nlinarith [sq_nonneg ((a-25*b)*z-5*b*y)]

#print axioms weight_pos
#print axioms weight_le_one
#print axioms polynomial_bound
#print axioms all_time_moments
#print axioms log_square_le
#print axioms logarithmic_cost_absorption
#print axioms reciprocal_weight
#print axioms exponential_cost_bound
#print axioms quadratic_parameter_loss

end CollatzShell.LognormalClock
