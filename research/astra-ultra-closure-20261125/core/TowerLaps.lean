import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring

namespace Collatz.TowerLaps

/-- If two distinct powers above one base are integral lifts about a positive
control, one with displacement 4^k*t and the other with displacement 3^k*t,
then their common base strictly exceeds 3^k. -/
theorem base_gt_lap_power {w j d k u t : Nat}
    (hd : 0 < d) (hk : 0 < k) (hu : 0 < u)
    (high : 3^(j+d)*w = u + 4^k*t)
    (low : 3^j*w = u + 3^k*t) : 3^k < w := by
  let A := 4^k
  let B := 3^k
  let D := A - B
  let C := 3^d - 1
  have hAB : B < A := Nat.pow_lt_pow_left (by decide) (by omega : k ≠ 0)
  have hD : D+B=A := by dsimp [D]; omega
  have hq : 1 < 3^d := Nat.one_lt_pow (by omega) (by decide)
  have hC : C+1=3^d := by dsimp [C]; omega
  have hc : 0<C := by dsimp [C]; omega
  change 3^j*w = u + B*t at low
  have hi : (C+1)*(3^j*w) = u + (D+B)*t := by
    rw [hC,hD,←high,pow_add]; ring
  rw [Nat.add_mul,Nat.one_mul,Nat.add_mul,low] at hi
  have prod : D*t = C*(3^j*w) := by rw [low]; omega
  have strict : B*C < D := by
    have g := Nat.mul_lt_mul_of_pos_left (show B*t < 3^j*w by omega) hc
    rw [←prod] at g
    have eq : C*(B*t)=(B*C)*t := by ring
    rw [eq] at g
    exact Nat.lt_of_mul_lt_mul_right g
  have copAB : A.Coprime B := ((show Nat.Coprime 4 3 by decide).pow_left k).pow_right k
  have copDB : D.Coprime B := (Nat.coprime_sub_self_left (Nat.le_of_lt hAB)).2 copAB
  have cop3 : D.Coprime 3 := (Nat.coprime_pow_right_iff hk _ _).1 copDB
  have dvd : D ∣ 3^j*(C*w) := ⟨t,by rw [prod]; ring⟩
  have dvd' : D ∣ C*w := (cop3.pow_right j).dvd_of_dvd_mul_left dvd
  have wpos : 0<w := by
    by_contra h
    have z : w=0 := by omega
    simp [z] at low
    omega
  have le := Nat.le_of_dvd (Nat.mul_pos hc wpos) dvd'
  have fin : C*B < C*w := by rw [Nat.mul_comm C B]; omega
  exact Nat.lt_of_mul_lt_mul_left fin

/-- At the minimum base there is no common positive integral control of this
form, for any number of full laps or any positive gap of ternary exponents. -/
theorem no_pure_power_laps {j d k u t : Nat}
    (hd : 0<d) (hk : 0<k) (hu : 0<u)
    (high : 3^(j+d) = u+4^k*t) (low : 3^j = u+3^k*t) : False := by
  have lower := base_gt_lap_power (w:=1) hd hk hu (by simpa using high) (by simpa using low)
  have pos : 0<3^k := Nat.pow_pos (by decide)
  omega

#print axioms base_gt_lap_power
#print axioms no_pure_power_laps

end Collatz.TowerLaps
