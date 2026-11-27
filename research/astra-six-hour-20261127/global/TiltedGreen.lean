import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

/-! Finite rational identities used in the ternary Green test.
No integral, infinite sum, or pointwise upper estimate is asserted here. -/
namespace Collatz.SixHour.TiltedGreen

theorem cycle_weight_floor {x : ℚ} (hx : 13≤x) :
    1 < (25/24:ℚ)^2 * (3*x/(3*x+1))^3 := by
  have hd : 0 < 3*x+1 := by linarith
  have hr : (39/40:ℚ) ≤ 3*x/(3*x+1) := by
    apply (le_div_iff₀ hd).2
    linarith
  have hu := pow_le_pow_left₀ (show (0:ℚ)≤39/40 by norm_num) hr 3
  nlinarith [hu]

theorem certain_cycle_weight : (25/24:ℚ)^2 * (3/4:ℚ)^3 < 1 := by
  norm_num

theorem haar_ratio_squared_control :
    (25/24:ℚ)^2 * 3 < 9 - 4*(99/70:ℚ) ∧ 2 < (99/70:ℚ)^2 := by
  norm_num

theorem affine_ghost_exit : (3*(-1:ℚ)+1)/4 = -(1/2:ℚ) := by norm_num

theorem one_steps (h : ℕ) (x : ℚ) :
    (fun z : ℚ => (3*z+1)/2)^[h] x = (3/2:ℚ)^h*(x+1)-1 := by
  induction h with
  | zero => simp
  | succ h ih =>
    rw [Function.iterate_succ_apply', ih, pow_succ]
    ring

theorem dense_family_formula (h d : ℕ) :
    (3*((fun z : ℚ => (3*z+1)/2)^[h] (-(1/2)))+1)/(2:ℚ)^d
      = ((3/2:ℚ)^(h+1)-2)/2^d := by
  rw [one_steps, pow_succ]
  ring

theorem ghost_numerator_odd {a : ℤ} {b : ℕ} (ha : a%2=1) (hb : 0<b) :
    (3*a+(2:ℤ)^b)%2=1 := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hb)
  rw [pow_succ]
  omega

theorem negative_shadow_cost {L x a b : ℕ} (hx : 0<x) (hb : 0<b)
    (hclock : 2^(L+1) ∣ b*x+a) (ha : a≤2^L) : 2^L ≤ b*x := by
  have hd := Nat.le_of_dvd (show 0<b*x+a by positivity) hclock
  rw [pow_succ] at hd
  omega

end Collatz.SixHour.TiltedGreen
