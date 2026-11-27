module
public import PassageOrbitPlaces
import all PassageOrbitDenominator
import all PassageOrbitHeights
import all TernaryItinerary
public section

namespace Collatz.Itinerary.PassageOrbit

/-- The all-odd parity word maximizes the unreduced carry at fixed native time. -/
theorem carry_cap (a t : ℕ) : carry a t+2^t≤3^t := by
  induction t with
  | zero => simp [carry]
  | succ t ih =>
    rw [carry,pow_succ,pow_succ]
    split <;> omega

/-- Binary cylinder identity for any actual nonreturn. The reduced fixed
point may be positive or negative. -/
theorem nonreturn_balance {a t : ℕ} (nr : run t a≠a) :
    2^t*(determinant a t).gcd (Nat.dist (run t a) a)≤determinant a t*a+carry a t := by
  have pos : 0<Nat.dist (run t a) a := by unfold Nat.dist; omega
  have g := Nat.le_of_dvd pos (Nat.gcd_dvd_right (determinant a t) _)
  let x : ℕ := 2^t
  let y : ℕ := 3^(oddCount a t)
  let c := carry a t
  calc
    _ ≤ x*Nat.dist (run t a) a := Nat.mul_le_mul_left _ g
    _ = Nat.dist (x*run t a) (x*a) := (Nat.dist_mul_left ..).symm
    _ = Nat.dist (y*a+c) (x*a) := by rw [show x*run t a=y*a+c from affine_identity ..]
    _ ≤ Nat.dist (y*a+c) (y*a)+Nat.dist (y*a) (x*a) := Nat.dist.triangle_inequality ..
    _ = determinant a t*a+carry a t := by
      rw [Nat.dist_mul_right,Nat.dist_comm y x,show Nat.dist (y*a+c) (y*a)=c by unfold Nat.dist; omega]
      exact Nat.add_comm ..

/-- A finite sharp-scale height price. Every nonreturn with complete
denominator supported on S has a*d at least half the binary modulus once
the stated prime-to-S determinant bound holds. -/
theorem supported_height_price {a t : ℕ} (ps : List ℕ) (long : 4≤t) (nr : run t a≠a)
    (supp : outside ps (denominator a t)=1)
    (outsideBound : 2^(7*t)≤(outside ps (determinant a t))^8) :
    2^t≤2*(a*denominator a t) := by
  let D := determinant a t
  let d := denominator a t
  let g := D.gcd (Nat.dist (run t a) a)
  have gp : 0<g := Nat.gcd_pos_of_pos_left _ (determinant_pos (a:=a) (by omega))
  have recov : g*d=D := Nat.mul_div_cancel' (Nat.gcd_dvd_left ..)
  have eq : outside ps D=outside ps g := by
    rw [←recov,outside_mul]; change _*outside ps (denominator a t)=_; rw [supp,Nat.mul_one]
  have gb : 2^(7*t)≤g^8 := by
    change 2^(7*t)≤(outside ps D)^8 at outsideBound
    rw [eq] at outsideBound
    exact outsideBound.trans (Nat.pow_le_pow_left (outside_le ..) 8)
  have small : 2*3^t≤2^t*g := by
    apply (Nat.pow_le_pow_iff_left (by decide : 8≠0)).mp
    calc
      (2*3^t)^8 = (2^8)*3^(8*t) := by rw [mul_pow,←pow_mul,Nat.mul_comm t 8]
      _ ≤ 4^t*3^(8*t) := Nat.mul_le_mul_right _
        ((by decide : 2^8≤4^4).trans (Nat.pow_le_pow_right (by decide) long))
      _ ≤ 2^(15*t) := by rw [pow_mul,pow_mul,←mul_pow]; exact Nat.pow_le_pow_left (by decide) _
      _ = (2^t)^8*2^(7*t) := by rw [←pow_mul,←pow_add]; congr 1; ring
      _ ≤ (2^t)^8*g^8 := Nat.mul_le_mul_left _ gb
      _ = (2^t*g)^8 := (mul_pow ..).symm
  have bal := nonreturn_balance nr
  change 2^t*g≤D*a+carry a t at bal
  rw [←recov] at bal
  have cap : carry a t≤3^t := (Nat.le_add_right ..).trans (carry_cap a t)
  apply Nat.le_of_mul_le_mul_right (c:=g) _ gp
  change 2^t*g ≤ 2*(a*d)*g
  rw [show 2*(a*d)*g=2*(g*d*a) by ring]
  omega

/-- The known positive cycle has one finite-rank return class, and its
intervening nonreturns have the full determinant as reduced denominator. -/
theorem trivial_cycle_phases (j : ℕ) :
    run (2*j) 1=1 ∧ run (2*j+1) 1=2 ∧ oddCount 1 (2*j)=j ∧ oddCount 1 (2*j+1)=j+1 := by
  induction j with
  | zero => decide
  | succ j ih =>
    have even : run (2*(j+1)) 1=1 := by
      rw [show 2*(j+1)=2*j+1+1 by omega,state_succ,ih.2.1]; decide
    have odd : run (2*(j+1)+1) 1=2 := by rw [state_succ,even]; decide
    have count : oddCount 1 (2*(j+1))=j+1 := by
      rw [show 2*(j+1)=2*j+1+1 by omega,oddCount,ih.2.2.2,ih.2.1]
    refine ⟨even,odd,count,?_⟩
    rw [oddCount,count,even]

theorem trivial_nonreturn_denominator (j : ℕ) : denominator 1 (2*j+1)=Nat.dist (2*4^j) (3^(j+1)) := by
  have ph := trivial_cycle_phases j
  unfold denominator determinant
  rw [ph.2.1,ph.2.2.2,show Nat.dist 2 1=1 by decide,Nat.gcd_one_right,Nat.div_one,pow_succ,pow_mul]
  congr 1
  exact Nat.mul_comm ..

theorem trivial_return_denominator {j : ℕ} (positive : 0<j) : denominator 1 (2*j)=1 :=
  return_denominator (by omega) (trivial_cycle_phases j).1

#print axioms supported_height_price
#print axioms trivial_nonreturn_denominator
end Collatz.Itinerary.PassageOrbit
