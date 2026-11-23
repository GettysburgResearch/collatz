import WitnessGlobal
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp

/-!
An actual ordinary inverse cylinder forces a nonzero finite density error.
The finite transfer matrices and their mean-one normalization are written
inputs to the analytic application; the finite inequalities below retain
those hypotheses explicitly. No limiting Collatz assertion is assumed.
-/

namespace CollatzShell.MixingCylinder

open Finset WitnessGlobal

/-- An elementary certificate for the period used to group the complete
valuation series into a finite rational row. -/
theorem ternary_power_lift (r : ℕ) :
    ∃ k : ℕ, 4^(3^r) = 1 + 3^(r+1)*k := by
  induction r with
  | zero => exact ⟨1, by norm_num⟩
  | succ r ih =>
    obtain ⟨k, hk⟩ := ih
    refine ⟨k + 3^(r+1)*k^2 + 3^r*3^(r+1)*k^3, ?_⟩
    calc
      4^(3^(r+1)) = (4^(3^r))^3 := by rw [pow_succ, pow_mul]
      _ = (1+3^(r+1)*k)^3 := by rw [hk]
      _ = 1+3^(r+1+1)*(k+3^(r+1)*k^2+3^r*3^(r+1)*k^3) := by
        simp only [pow_succ]
        ring

theorem ternary_exponent_period (r : ℕ) :
    2^(2*3^r) % 3^(r+1) = 1 := by
  obtain ⟨k, hk⟩ := ternary_power_lift r
  have hp : 1 < 3^(r+1) := by
    have h : 1 ≤ 3^r := Nat.one_le_pow r 3 (by decide)
    rw [pow_succ]
    omega
  calc
    2^(2*3^r) % 3^(r+1) = 4^(3^r) % 3^(r+1) := by
      rw [pow_mul]
      norm_num
    _ = (1+3^(r+1)*k) % 3^(r+1) := by rw [hk]
    _ = 1 := by simp [Nat.add_mod, Nat.mod_eq_of_lt hp]

/-- Every gap of this ordinary cylinder is one. Choosing u=2 makes
all endpoints positive odd integers, including the terminal target. -/
theorem all_one_trace (r u : ℕ) (hu : 0 < u) :
    GapTrace (2^r*u-1) (3^r*u-1) (List.replicate r 1) := by
  induction r generalizing u with
  | zero => simp [GapTrace]
  | succ r ih =>
    have positive : 0 < 2^r*u := by positivity
    have edge : 3*(2^(r+1)*u-1)+1 = 2*(2^r*(3*u)-1) := by
      rw [show 2^(r+1)*u = 2*(2^r*u) by ring,
        show 2^r*(3*u) = 3*(2^r*u) by ring]
      omega
    simp only [List.replicate_succ, GapTrace]
    refine ⟨by decide, 2^r*(3*u)-1, by simpa using edge, ?_⟩
    simpa only [pow_succ, Nat.mul_assoc] using ih (3*u) (by omega)

theorem ordinary_cylinder (r : ℕ) :
    GapTrace (2^(r+1)-1) (2*3^r-1) (List.replicate r 1) ∧
      orbit r (2^(r+1)-1) = 2*3^r-1 := by
  have trace := all_one_trace r 2 (by decide)
  have typed : GapTrace (2^(r+1)-1) (2*3^r-1) (List.replicate r 1) := by
    simpa only [pow_succ, Nat.mul_comm] using trace
  exact ⟨typed, by simpa using trace_orbit typed⟩

/-- Equal total masses make one positive discrepancy count twice in L1. -/
theorem zero_mass_l1 {ι : Type*} [Fintype ι] (f : ι → ℝ)
    (total : ∑ i, f i = 0) (a : ι) :
    2*f a ≤ ∑ i, |f i| := by
  classical
  have nonnegative : ∀ i, 0 ≤ |f i| + f i := by
    intro i
    linarith [neg_abs_le (f i)]
  calc
    2*f a ≤ |f a|+f a := by linarith [le_abs_self (f a)]
    _ ≤ ∑ i, (|f i|+f i) := single_le_sum (fun i _ => nonnegative i) (mem_univ a)
    _ = ∑ i, |f i| := by rw [sum_add_distrib, total, add_zero]

/-- Finite densities of equal mass retain the full rare-cell discrepancy. -/
theorem finite_density_error_lower {ι : Type*} [Fintype ι]
    (fine coarse : ι → ℝ) (m : ℕ) (a : ι)
    (mass : ∑ i, fine i = ∑ i, coarse i)
    (ray : (9/4 : ℝ)^m ≤ fine a)
    (cap : coarse a ≤ (2 : ℝ)^m) :
    2*((9/4 : ℝ)^m-(2 : ℝ)^m) ≤ ∑ i, |fine i-coarse i| := by
  have zero : ∑ i, (fine i-coarse i) = 0 := by
    rw [sum_sub_distrib, mass, sub_self]
  have bound := zero_mass_l1 (fun i => fine i-coarse i) zero a
  linarith

/-- The exact finite mixing error is bounded below by an ordinary cylinder.
The scalar normalization is kept as a premise of this finite theorem. -/
theorem critical_error_floor (m : ℕ) (hm : 1 ≤ m) (ε : ℝ)
    (cell : 2*((9/4 : ℝ)^m-(2 : ℝ)^m) ≤ (9 : ℝ)^m*ε) :
    (2/9 : ℝ)*(1/4 : ℝ)^m ≤ ε := by
  have hp : 0 < (9/4 : ℝ)^m := by positivity
  have contraction : (8/9 : ℝ)^m ≤ 8/9 := by
    obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m ≠ 0)
    rw [pow_succ]
    have h : (8/9 : ℝ)^k ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
    nlinarith
  have factor : (8/9 : ℝ)^m*(9/4 : ℝ)^m = (2 : ℝ)^m := by
    rw [← mul_pow]
    norm_num
  have short := mul_le_mul_of_nonneg_right contraction hp.le
  rw [factor] at short
  have gap : (2/9 : ℝ)*(9/4 : ℝ)^m ≤ (9 : ℝ)^m*ε := by
    nlinarith only [short, cell]
  have normal : (9 : ℝ)^m*((2/9 : ℝ)*(1/4 : ℝ)^m) =
      (2/9 : ℝ)*(9/4 : ℝ)^m := by
    calc
      (9 : ℝ)^m*((2/9 : ℝ)*(1/4 : ℝ)^m) =
          (2/9 : ℝ)*((9 : ℝ)*(1/4 : ℝ))^m := by rw [mul_pow]; ring
      _ = (2/9 : ℝ)*(9/4 : ℝ)^m := by norm_num
  exact (le_of_mul_le_mul_left (by simpa only [normal] using gap)
    (by positivity : 0 < (9 : ℝ)^m))

/-- The rare cylinder gives an intrinsic upper budget for this calibration.
This bounds the particular finite-error construction, not Collatz clocks. -/
theorem calibration_ceiling (m : ℕ) (H ε E : ℝ)
    (floor : (2/9 : ℝ)*(1/4 : ℝ)^m ≤ ε)
    (regularized : ε ≤ E) (calibrated : H^4*E ≤ 1) :
    2*H^4 ≤ 9*(4 : ℝ)^m := by
  have lower := mul_le_mul_of_nonneg_left (floor.trans regularized)
    (by positivity : 0 ≤ H^4)
  have pay : H^4*((2/9 : ℝ)*(1/4 : ℝ)^m) ≤ 1 := lower.trans calibrated
  have product : (1/4 : ℝ)^m*(4 : ℝ)^m = 1 := by
    rw [← mul_pow]
    norm_num
  have paid := mul_le_mul_of_nonneg_right pay (by positivity : 0 ≤ (4 : ℝ)^m)
  have identity : H^4*((2/9 : ℝ)*(1/4 : ℝ)^m)*(4 : ℝ)^m = (2/9 : ℝ)*H^4 := by
    calc
      _ = (2/9 : ℝ)*H^4*((1/4 : ℝ)^m*(4 : ℝ)^m) := by ring
      _ = (2/9 : ℝ)*H^4 := by rw [product, mul_one]
  rw [identity, one_mul] at paid
  nlinarith

#print axioms ternary_power_lift
#print axioms ternary_exponent_period
#print axioms all_one_trace
#print axioms ordinary_cylinder
#print axioms zero_mass_l1
#print axioms finite_density_error_lower
#print axioms critical_error_floor
#print axioms calibration_ceiling

end CollatzShell.MixingCylinder
