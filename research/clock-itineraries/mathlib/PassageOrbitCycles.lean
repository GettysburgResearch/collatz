module
public import PassageOrbitHeightPrice
import all PassageOrbitDenominator
import all PassageOrbitHeights
import all TernaryItinerary
public section

namespace Collatz.Itinerary.PassageOrbit

private theorem minimum_carry {a t : ℕ} (minimum : ∀i<t, a≤run i a) :
    (3*a+1)*carry a t≤t*(2^t*run t a) := by
  induction t with
  | zero => simp [carry]
  | succ t ih =>
    have prev := ih (fun i hi => minimum i (by omega))
    have last := minimum t (by omega)
    let x := run t a
    by_cases even : x%2=0
    · have edge : 2*step x=x := by simp [step,even]; omega
      have id : 2^(t+1)*run (t+1) a=2^t*x := by rw [state_succ,pow_succ,Nat.mul_assoc]; exact congrArg _ edge
      rw [id,carry,ite_eq_left_iff.mpr (fun h => False.elim (h even))]
      exact prev.trans (Nat.mul_le_mul_right _ (Nat.le_succ _))
    · have edge : 2*step x=3*x+1 := by simp [step,even]; omega
      have id : 2^(t+1)*run (t+1) a=2^t*(3*x+1) := by
        rw [state_succ,pow_succ,Nat.mul_assoc]; exact congrArg _ edge
      rw [id,carry,ite_eq_right_iff.mpr (fun h => False.elim (even h))]
      have current : (3*a+1)*2^t≤(3*x+1)*2^t := Nat.mul_le_mul_right _ (by dsimp [x]; omega)
      have scale := Nat.mul_le_mul_left 3 prev
      change 3*((3*a+1)*carry a t)≤3*(t*(2^t*x)) at scale
      calc
        _ = 3*((3*a+1)*carry a t)+(3*a+1)*2^t := by ring
        _ ≤ 3*(t*(2^t*x))+(3*x+1)*2^t := Nat.add_le_add scale current
        _ ≤ (t+1)*(2^t*(3*x+1)) := by nlinarith only [Nat.zero_le (t*2^t)]

/-- A full positive lap rooted at its minimum has small minimum whenever
its relative lap determinant is large. This is an exact integer inequality. -/
theorem cycle_minimum_bound {a P : ℕ} (pos : 0<a) (ret : run P a=a)
    (minimum : ∀i<P, a≤run i a) :
    (3*a+1)*determinant a P≤P*2^P := by
  have edge := affine_identity a P
  rw [ret] at edge
  have le : 3^(oddCount a P)≤2^P := Nat.le_of_mul_le_mul_right
    (by omega : 3^(oddCount a P)*a≤2^P*a) pos
  have eq : carry a P=determinant a P*a := by
    unfold determinant Nat.dist
    rw [Nat.sub_eq_zero_of_le le,Nat.add_zero,Nat.sub_mul]
    omega
  have z := minimum_carry minimum
  rw [ret,eq,←Nat.mul_assoc,←Nat.mul_assoc] at z
  exact Nat.le_of_mul_le_mul_right z pos

private theorem reverse_cap (x h : ℕ) : x≤2^h*run h x := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    have one : x≤2*step x := by unfold step; split <;> omega
    rw [run,pow_succ]
    calc
      x ≤ 2*step x := one
      _ ≤ 2*(2^h*run h (step x)) := Nat.mul_le_mul_left _ (ih (step x))
      _ = _ := by ring

/-- Reduction on a proper prefix j native steps short of a positive lap
loses at most 2^j times the fixed starting value, outside any chosen primes. -/
theorem near_lap_rough {a t j : ℕ} (ps : List ℕ) (ret : run (t+j) a=a) (nr : run t a≠a) :
    outside ps (determinant a t)≤(2^j*a)*outside ps (denominator a t) := by
  have back := reverse_cap (run t a) j
  rw [←run_add,ret] at back
  have self : a≤2^j*a := by simpa using Nat.mul_le_mul_right a (Nat.one_le_two_pow (n:=j))
  have nz : 0<Nat.dist (run t a) a := by unfold Nat.dist; omega
  let g := (determinant a t).gcd (Nat.dist (run t a) a)
  have gb : g≤2^j*a := (Nat.le_of_dvd nz (Nat.gcd_dvd_right ..)).trans
    ((diff_le_max ..).trans (max_le back self))
  have recov : g*denominator a t=determinant a t := Nat.mul_div_cancel' (Nat.gcd_dvd_left ..)
  rw [←recov,outside_mul]
  exact Nat.mul_le_mul_right _ ((outside_le ps g).trans gb)

/-- A rational ordinary phase n/b can be followed with the initial
denominator b kept in every state. This finite inequality works directly
from the unrolled affine equation, even if the displayed fractions reduce. -/
theorem rational_arc_rough {t u n q b C K : ℕ} (ps : List ℕ)
    (edge : 2^t*q=3^u*n+b*C) (nr : q≠n) (heights : max q n≤K) :
    let D := Nat.dist (2^t) (3^u)
    outside ps D≤K*outside ps (D/D.gcd C) := by
  let D := Nat.dist (2^t) (3^u)
  let g := D.gcd C
  have dd : g ∣ D := Nat.gcd_dvd_left ..
  have dc : g ∣ C := Nat.gcd_dvd_right ..
  have clock := dvd_diff.mp dd
  have cop : g.Coprime (2^t) := (diff_coprime_left
    (((by decide : Nat.Coprime 2 3).pow_left t).pow_right u)).of_dvd_left dd
  have cv : b*C ≡ 0 [MOD g] := Nat.modEq_zero_iff_dvd.mpr (dvd_mul_of_dvd_right dc _)
  have states : q ≡ n [MOD g] := by
    apply Nat.ModEq.cancel_left_of_coprime cop
    rw [edge]
    simpa using (clock.mul_right n).symm.add cv
  have diffpos : 0<Nat.dist q n := by unfold Nat.dist; omega
  have bound : g≤K := (Nat.le_of_dvd diffpos (dvd_diff.mpr states)).trans
    ((diff_le_max ..).trans heights)
  let d := D/g
  have recov : g*d=D := Nat.mul_div_cancel' dd
  change outside ps D≤K*outside ps d
  conv_lhs => rw [←recov,outside_mul]
  exact Nat.mul_le_mul_right _ ((outside_le ps g).trans bound)

#print axioms cycle_minimum_bound
#print axioms near_lap_rough
end Collatz.Itinerary.PassageOrbit
