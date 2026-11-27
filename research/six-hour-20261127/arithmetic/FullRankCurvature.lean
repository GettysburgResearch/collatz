import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FullRankCurvature

theorem carry {q a b c u v w A B C : ℤ}
    (ha : q*A=3*a+u) (hb : q*B=3*b+v) (hc : q*C=3*c+w) :
    q*(A-2*B+C)=3*(a-2*b+c)+u-2*v+w := by
  linear_combination ha-2*hb+hc

structure State where
  left : Int
  mid : Int
  right : Int
  curvature : Int
  deriving BEq, DecidableEq

private def previousLowbits (m y : Int) : List Int :=
  let allowed := if m == 1 then [1, 2, 4] else [2, 4]
  let q : Int := if m == 1 then 2 else 4
  allowed.filter fun x => q*y == 2*x || q*y == 4*x

/-- Three independent ordinary lowbits and the signed curvature are kept
together. The zero-curvature equal-lowbit case is an ordinary progression. -/
private def previous (m : Int) (t : State) : List State :=
  (previousLowbits m t.left).flatMap fun a =>
  (previousLowbits m t.mid).flatMap fun b =>
  (previousLowbits m t.right).filterMap fun c =>
    let q : Int := if m == 1 then 2 else 4
    let difference := a-2*b+c
    let num := q*t.curvature-difference
    let h := num/3
    if num%3 == 0 && (h-difference)%(2*min a (min (2*b) c)) == 0
        && (h != 0 || a != b || b != c) then
      some ⟨a,b,c,h⟩
    else
      none

private def letters : List Int :=
  [2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,2,2]

set_option maxRecDepth 20000 in
set_option maxHeartbeats 4000000 in
/-- Kernel evaluation of the entire nonuniform 35-step backward seam. -/
theorem no_seam_predecessor :
    letters.foldl (fun states m => (states.flatMap (previous m)).eraseDups)
      [⟨4,1,4,-2⟩] = [] := by decide +kernel

#print axioms carry
#print axioms no_seam_predecessor

end Collatz.FullRankCurvature
