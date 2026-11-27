module

public import PassageGatePrefix
public import PassageGateMoment
import all PassageGateMoment
import all PassageGatePrefix
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open FixedGate HourTower
set_option autoImplicit false

private theorem scale_bounds : (3:ℝ)/2 ≤ clockScale ∧ clockScale≤2 := by
  have lo := Real.logb_le_logb_of_le (by norm_num : (1:ℝ)<2)
    (by norm_num : (0:ℝ)<2^3) (by norm_num : (2:ℝ)^3≤3^2)
  have hi := Real.logb_le_logb_of_le (by norm_num : (1:ℝ)<2)
    (by norm_num : (0:ℝ)<3) (by norm_num : (3:ℝ)≤2^2)
  simp only [Real.logb_pow,Real.logb_self_eq_one (by norm_num : (1:ℝ)<2),Nat.cast_ofNat,
    mul_one] at lo hi
  unfold clockScale
  constructor <;> linarith

/-- At a physical source shell, late odd departures must spend a
corresponding amount of the *remaining* even budget. This applies to
the positive integer actually reached after closing the unfinished gap. -/
theorem remaining_clock_floor {x n k : ℕ} (odd : x%2=1)
    (shell : x+1≤2^(k+1)) (within : k≤elapsed n x)
    (gate : ∀ j≤n, 4*elapsed j x≤7*j) :
    (n:ℝ)+1 ≤ 8*((k:ℝ)+1)*clockScale^(elapsed n x-n-(k-count k x)) := by
  let l := count k x
  let y := after l x
  let b := elapsed n x-n-(k-l)
  have grade : l≤k := count_le k x
  obtain ⟨_,pre,suffix⟩ := stopped_shell odd within gate
  change l≤n at pre
  change elapsed (n-l) y+k≤elapsed n x at suffix
  have residual : elapsed (n-l) y-(n-l)≤b := by dsimp [b]; omega
  have yo : y%2=1 := current_odd odd l
  have point := source_excess yo (n-l)
  have low := scale_bounds.1
  have high := scale_bounds.2
  have pos : 0<clockScale := by linarith
  have factor := pow_le_pow_right₀ (le_of_lt one_lt_scale) residual
  have initial : (x:ℝ)+1≤(2:ℝ)^(k+1) := by exact_mod_cast shell
  have length : (3/2:ℝ)^l ≤ 2^k := (pow_le_pow_left₀ (by norm_num) (by norm_num) l).trans
    (pow_le_pow_right₀ (by norm_num) grade)
  have growth := size_growth odd l
  have yc : (y:ℝ)+1≤(2:ℝ)^(k+(k+1)) := by
    rw [pow_add]
    exact growth.trans (mul_le_mul length initial (by positivity) (by positivity))
  have logy := Real.logb_le_logb_of_le (by norm_num : (1:ℝ)<2) (by positivity) yc
  rw [Real.logb_pow,Real.logb_self_eq_one (by norm_num : (1:ℝ)<2),mul_one] at logy
  push_cast at logy
  have idn := source_identity y
  have nonneg : 0≤Real.logb 2 ((y:ℝ)+1) :=
    Real.logb_nonneg (by norm_num) (le_add_of_nonneg_left (Nat.cast_nonneg y))
  have hs : 0≤sourceScale y := div_nonneg (by linarith) (by linarith)
  have cs := mul_nonneg (show 0≤clockScale-3/2 by linarith) hs
  have cap : Real.logb 2 ((y:ℝ)+1)+sourceScale y≤7*((k:ℝ)+1) := by nlinarith
  have right := mul_le_mul factor cap (add_nonneg nonneg hs) (pow_nonneg pos.le _)
  have one : (1:ℝ)≤clockScale^b := one_le_pow₀ one_lt_scale.le
  have lg : (l:ℝ)≤k := by exact_mod_cast grade
  rw [Nat.cast_sub pre] at point
  change (n:ℝ)+1 ≤ 8*((k:ℝ)+1)*clockScale^b
  nlinarith [mul_nonneg (show (0:ℝ)≤(k:ℝ)+1 by positivity) (sub_nonneg.mpr one)]

#print axioms remaining_clock_floor
end Collatz.Itinerary.PassageGate
