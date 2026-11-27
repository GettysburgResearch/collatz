import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

/-! Finite coefficient bounds in the prefix-dependent Green function.
The input r in the comparison may be any positive representative below n. -/
namespace Collatz.SixHour.AdaptiveGreen

def shape (x : ℚ) : ℚ := 1 + 1/(2*x) + 1/(12*x^2)

def boost (x : ℚ) : ℚ := shape (max x 13)

def edge (x : ℚ) : ℚ := 3*x/(3*x+1)

theorem shape_one_le {x : ℚ} (hx : 0<x) : 1 ≤ shape x := by
  unfold shape
  have ha : (0:ℚ)≤1/(2*x) := div_nonneg (by norm_num) (mul_nonneg (by norm_num) hx.le)
  have hb : (0:ℚ)≤1/(12*x^2) := div_nonneg (by norm_num) (mul_nonneg (by norm_num) (sq_nonneg x))
  linarith

theorem shape_anti {x y : ℚ} (hx : 0<x) (hxy : x≤y) : shape y ≤ shape x := by
  have ha : 0 < 2*x := by positivity
  have hb : 0 < 12*x^2 := by positivity
  have hy : 0<y := lt_of_lt_of_le hx hxy
  have h1 : 1/(2*y)≤1/(2*x) := (div_le_div_iff₀ (by positivity) ha).mpr (by linarith)
  have hs := mul_nonneg (sub_nonneg.mpr hxy) (show 0≤y+x by linarith)
  have h2 : 1/(12*y^2)≤1/(12*x^2) := (div_le_div_iff₀ (by positivity) hb).mpr (by nlinarith [hs])
  unfold shape
  linarith

theorem boost_anti {r n : ℚ} (hr : r≤n) : boost n ≤ boost r := by
  apply shape_anti (show 0<max r 13 by exact lt_of_lt_of_le (by norm_num) (le_max_right _ _))
  exact max_le_max hr le_rfl

theorem boost_bounds (r : ℚ) : 1 ≤ boost r ∧ boost r ≤ shape 13 := by
  constructor
  · apply shape_one_le
    exact lt_of_lt_of_le (by norm_num : (0:ℚ)<13) (le_max_right _ _)
  · apply shape_anti (by norm_num)
    exact le_max_right _ _

theorem multiplier_constants :
    shape 13 < 26/25 ∧ (shape 13)^4 < 2 ∧
    (shape 13)^2*(33/34)^3<1 ∧ (shape 13)^2*(3/4)^3<1 := by
  norm_num [shape]

theorem exact_high_gain {x : ℚ} (hx : 13≤x) :
    shape x ^ 2 * edge x ^ 3 - 1 =
      (36*x^2+20*x+3)/(16*x*(3*x+1)^3) := by
  have h1 : x≠0 := by linarith
  have h2 : 3*x+1≠0 := by linarith
  unfold shape edge
  field_simp
  ring

theorem high_energy_bridge {r n : ℚ} (hr : r≤n) (hn : 13≤n) :
    1+1/(32*n^2) ≤ boost r ^ 2 * edge n ^ 3 := by
  have hn0 : 0<n := by linarith
  have hp : 0<3*n+1 := by linarith
  have he : 0 ≤ edge n ^ 3 := pow_nonneg (div_nonneg (mul_nonneg (by norm_num) hn0.le) hp.le) _
  have hv := boost_anti hr
  have hb := (boost_bounds n).1
  have hm := mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by linarith : 0≤boost n) hv 2) he
  have hbn : boost n = shape n := by simp [boost, max_eq_left hn]
  rw [hbn] at hm
  have hd := exact_high_gain hn
  have hsmall : 1/(32*n^2) ≤ (36*n^2+20*n+3)/(16*n*(3*n+1)^3) := by
    rw [div_le_div_iff₀ (show 0 < 32*n^2 by positivity) (show 0 < 16*n*(3*n+1)^3 by exact mul_pos (by positivity) (pow_pos hp _))]
    nlinarith [sq_nonneg n, pow_pos hn0 3, pow_pos hn0 4,
      mul_nonneg (show 0≤n-1 by linarith) (show 0≤n by linarith)]
  linarith

theorem low_energy_bridge {r n : ℚ} (hn : 1≤n) :
    1/4 ≤ boost r ^ 2 * edge n ^ 3 := by
  have he : (3/4:ℚ) ≤ edge n := by
    unfold edge
    exact (le_div_iff₀ (by linarith)).mpr (by linarith)
  have hb := (boost_bounds r).1
  have h0 := pow_le_pow_left₀ (by norm_num : (0:ℚ)≤3/4) he 3
  have h1 := pow_le_pow_left₀ (by norm_num : (0:ℚ)≤1) hb 2
  nlinarith [mul_nonneg (show 0≤boost r ^ 2-1 by nlinarith) (show 0≤edge n ^ 3 by linarith)]

theorem telescoping_factor {n : ℚ} (hn : 1≤n) :
    1+1/(12*n^2) ≤ (n+1)^2/(n*(n+2)) := by
  have h : 0<n := by linarith
  have h2 : 0<n+2 := by linarith
  rw [le_div_iff₀ (mul_pos h h2)]
  field_simp
  nlinarith [sq_nonneg (n-1), mul_nonneg (sub_nonneg.mpr hn) (show 0≤n by linarith)]

end Collatz.SixHour.AdaptiveGreen
