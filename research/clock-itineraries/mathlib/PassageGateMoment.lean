module

public import FixedGate
public import Mathlib.Analysis.SpecialFunctions.Log.Base
public import Mathlib.Data.Nat.Factorization.Basic
import all FixedGate
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open FixedGate
set_option autoImplicit false

/-- Number of odd departures whose exact exponent exceeds one. -/
def interruptions (a : ℕ) : ℕ → ℕ
  | 0 => 0
  | i+1 => interruptions a i + if (next (after i a)).1=1 then 0 else 1

/-- Two-adic valuation of the shifted positive integer. -/
def twos (x : ℕ) : ℕ := (x+1).factorization 2

private theorem twos_one {x y : ℕ} (eqn : 2*y=3*x+1) :
    twos y+1=twos x := by
  have shifted : 2*(y+1)=3*(x+1) := by omega
  have e := congrArg (fun n : ℕ => n.factorization 2) shifted
  simp only [Nat.factorization_mul (by decide : (2:ℕ)≠0) (Nat.succ_ne_zero _),
    Nat.factorization_mul (by decide : (3:ℕ)≠0) (Nat.succ_ne_zero _),
    Finsupp.add_apply] at e
  have two : (2:ℕ).factorization 2=1 := Nat.prime_two.factorization_self
  have three : (3:ℕ).factorization 2=0 := Nat.factorization_eq_zero_of_not_dvd (by decide)
  change (2:ℕ).factorization 2 + (y+1).factorization 2 =
    (3:ℕ).factorization 2 + (x+1).factorization 2 at e
  rw [two,three,zero_add,add_comm] at e
  exact e

private theorem twos_le_log (x : ℕ) : (twos x : ℝ) ≤ Real.logb 2 (x+1) := by
  have dv : 2^(twos x) ∣ x+1 :=
    (Nat.prime_two.pow_dvd_iff_le_factorization (Nat.succ_ne_zero _)).mpr le_rfl
  have le : 2^(twos x) ≤ x+1 := Nat.le_of_dvd (by omega) dv
  have realLe : (2:ℝ)^(twos x) ≤ (x:ℝ)+1 := by exact_mod_cast le
  have e := Real.logb_le_logb_of_le (by norm_num : (1:ℝ)<2) (by positivity) realLe
  simpa only [Real.logb_pow,Real.logb_self_eq_one (by norm_num : (1:ℝ)<2),mul_one] using e

private theorem current_odd {a : ℕ} (odd : a%2=1) (i : ℕ) : after i a%2=1 := by
  induction i generalizing a with
  | zero => exact odd
  | succ i ih => exact ih (next_gap odd).oddTarget

private theorem current_gap {a : ℕ} (odd : a%2=1) (i : ℕ) :
    Gap (next (after i a)).1 (after i a) (after (i+1) a) := by
  rw [after_add]
  exact next_gap (current_odd odd i)

private theorem size_growth {a : ℕ} (odd : a%2=1) (i : ℕ) :
    (after i a:ℝ)+1 ≤ (3/2:ℝ)^i*((a:ℝ)+1) := by
  induction i with
  | zero => simp [after]
  | succ i ih =>
    have g := current_gap odd i
    have pos := g.pos
    have pw : 2 ≤ 2^(next (after i a)).1 := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) pos
    have cap := (Nat.mul_le_mul_right (after (i+1) a) pw).trans_eq g.eqn
    have stepLe : (2:ℝ)*(after (i+1) a:ℝ) ≤ 3*(after i a:ℝ)+1 := by exact_mod_cast cap
    rw [pow_succ]
    nlinarith

/-- Constant for the logarithmic waiting time normalized by the source. -/
noncomputable def clockScale : ℝ := Real.logb 2 3
noncomputable def sourceScale (a : ℕ) : ℝ :=
  (Real.logb 2 ((a:ℝ)+1)+clockScale)/(clockScale-1)

private theorem one_lt_scale : 1<clockScale := by
  rw [clockScale,←Real.logb_self_eq_one (by norm_num : (1:ℝ)<2)]
  apply Real.strictMonoOn_logb (by norm_num : (1:ℝ)<2) <;> norm_num

private theorem log_growth {a : ℕ} (odd : a%2=1) (i : ℕ) :
    (twos (after i a) : ℝ) ≤ Real.logb 2 ((a:ℝ)+1)+(clockScale-1)*i := by
  have le := Real.logb_le_logb_of_le (by norm_num : (1:ℝ)<2)
    (by positivity) (size_growth odd i)
  rw [Real.logb_mul (by positivity) (by positivity),Real.logb_pow,
    Real.logb_div (by norm_num) (by norm_num),
    Real.logb_self_eq_one (by norm_num : (1:ℝ)<2)] at le
  have v := twos_le_log (after i a)
  unfold clockScale
  linarith

private theorem source_identity (a : ℕ) :
    (clockScale-1)*sourceScale a=Real.logb 2 ((a:ℝ)+1)+clockScale := by
  unfold sourceScale
  field_simp [(sub_pos.mpr one_lt_scale).ne']

/-- A single positive ordinary seed cannot sustain arbitrarily many
minimum-clock departures with a fixed number of interruptions. This
bound counts interrupted runs, even when one exponent is very large. -/
theorem source_interruptions {a : ℕ} (odd : a%2=1) (n : ℕ) :
    (n:ℝ)+twos (after n a)+sourceScale a ≤
      clockScale^(interruptions a n)*(twos a+sourceScale a) := by
  induction n with
  | zero => simp [interruptions,after]
  | succ i ih =>
    have g := current_gap odd i
    by_cases one : (next (after i a)).1=1
    · have eqn := g.eqn
      rw [one,pow_one] at eqn
      have fall := twos_one eqn
      have ff : (twos (after (i+1) a):ℝ)+1=twos (after i a) := by exact_mod_cast fall
      simp only [interruptions,one,↓reduceIte,Nat.add_zero,Nat.cast_add,Nat.cast_one]
      linarith
    · rw [interruptions,ite_eq_right one,pow_succ]
      have nonneg : 0≤clockScale := le_trans (by norm_num) (le_of_lt one_lt_scale)
      have mult := mul_le_mul_of_nonneg_left ih nonneg
      have size := log_growth odd (i+1)
      have correction := source_identity a
      have v : 0≤(twos (after i a):ℝ) := by positivity
      have remain := mul_nonneg nonneg v
      push_cast at *
      nlinarith

private theorem elapsed_budget {a : ℕ} (odd : a%2=1) (n : ℕ) :
    n + interruptions a n ≤ elapsed n a := by
  induction n with
  | zero => simp [elapsed,interruptions]
  | succ i ih =>
    rw [snoc_clock,interruptions]
    have pos := (current_gap odd i).pos
    split <;> omega

/-- Positive integral pointwise clock floor, valid before any descent
and on all eventual fates. -/
theorem source_excess {a : ℕ} (odd : a%2=1) (n : ℕ) :
    (n:ℝ)+sourceScale a ≤ clockScale^(elapsed n a-n)*
      (Real.logb 2 ((a:ℝ)+1)+sourceScale a) := by
  have scale := one_lt_scale
  have positive : 0≤Real.logb 2 ((a:ℝ)+1) := by
    exact Real.logb_nonneg (by norm_num) (le_add_of_nonneg_left (Nat.cast_nonneg a))
  have sp : 0≤sourceScale a := div_nonneg (by linarith) (by linarith)
  have point := source_interruptions odd n
  have elapsedBound := elapsed_budget odd n
  have clocks := pow_le_pow_right₀ scale.le (show interruptions a n ≤ elapsed n a-n by omega)
  have seeds := twos_le_log a
  have both := mul_le_mul clocks (add_le_add_right seeds (sourceScale a)) (by positivity)
    (by positivity)
  have v : 0≤(twos (after n a):ℝ) := by positivity
  nlinarith

#print axioms source_interruptions
#print axioms source_excess
end Collatz.Itinerary.PassageGate
