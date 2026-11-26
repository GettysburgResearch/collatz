import SignedCycleDilation
import Mathlib.Tactic.Linarith

namespace DifferentCycleAnchors
open SignedCycleDilation CollatzReverseBasin CollatzTwoOdd

/-- A finite augmented-state test for distinct signed anchors. The slopes
and intercepts are required to agree at the displayed physical clocks. -/
theorem align (h k x y : Nat) (a b s t : Int)
    (hx : (x:Int)=2^h*s+a) (hy : (y:Int)=2^k*t+b)
    (base : orbit h a=orbit k b)
    (scale : 3^(count h a)*s=3^(count k b)*t) :
    Basin x ↔ Basin y := by
  have equality : orbit h (x:Int)=orbit k (y:Int) := by
    rw [hx,hy,lift,lift,base,scale]
  rw [nat_orbit,nat_orbit] at equality
  have vv : value h x=value k y := by omega
  rw [←basin_value h x,←basin_value k y,vv]

/-- At the first anchor the lower and upper arms enter the -1 and -5
cycles, respectively. The second anchor supplies the same ordered pair
at different entry grades. No shared cycle between the arms is needed. -/
theorem two_anchors (t z w : Nat) (hz : z+1807=1610612736*t)
    (hw : w+127=75497472*t) :
    w%48=17 ∧ w<z ∧ (Basin w ↔ Basin z) ∧ (Basin (3*w) ↔ Basin (3*z)) := by
  have small : w<z := by omega
  refine ⟨by omega,small,?_,?_⟩
  · apply align 19 25 w z (-127) (-1807) (144*(t:Int)) (48*(t:Int))
    · norm_num; omega
    · norm_num; omega
    · decide
    · have hwg : count 19 (-127)=8 := by decide
      have hzg : count 25 (-1807)=9 := by decide
      rw [hwg,hzg]; ring
  · apply align 23 29 (3*w) (3*z) (-381) (-5421) (27*(t:Int)) (9*(t:Int))
    · push_cast; omega
    · push_cast; omega
    · decide
    · have hwg : count 23 (-381)=11 := by decide
      have hzg : count 29 (-5421)=12 := by decide
      rw [hwg,hzg]; ring

/-- Arithmetic core of the post-ascent denominator lower bound. Here
c is the nonzero absolute numerator of the terminal signed displacement
and Q=2^v. The orbit argument supplies its two displayed inequalities. -/
theorem height_debt (A D M Q c : Nat) (hd : 0<D) (hq : 0<Q) (hc : 0<c)
    (sep : 81*Q≤D+c) (budget : A*c≤D*(M*Q+1)) :
    81*A≤81*D+2*M*D^2 := by
  by_cases short : 81*Q≤2*D
  · have a_le : A≤A*c := by simpa using (Nat.mul_le_mul_left A hc)
    have m := Nat.mul_le_mul_left (D*M) short
    have b := Nat.mul_le_mul_left 81 (a_le.trans budget)
    nlinarith only [m,b]
  · have c_le : 81*Q≤2*c := by omega
    have m := Nat.mul_le_mul_left A c_le
    have b := Nat.mul_le_mul_left 2 budget
    have d_le : 2*D≤2*D*Q := by simpa using Nat.mul_le_mul_left (2*D) hq
    have prod : (81*A)*Q≤(2*D*(M+1))*Q := by nlinarith only [m,b,d_le]
    have divide := Nat.le_of_mul_le_mul_right prod hq
    have md : (2*M*D)*1≤(2*M*D)*D := Nat.mul_le_mul_left _ hd
    nlinarith only [divide,md]

#print axioms align
#print axioms two_anchors
#print axioms height_debt
end DifferentCycleAnchors
