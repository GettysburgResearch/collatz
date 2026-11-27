import Mathlib.Tactic

namespace Collatz.HigherDifference

private def d3 : List ℤ := [-1,3,-3,1]
private def d4 : List ℤ := [1,-4,6,-4,1]
private def dot (u v : List ℤ) : ℤ := (u.zipWith (· * ·) v).sum

private def checkEdge (weights : List ℤ) (b : Nat) (c d : List ℤ) (h g : ℤ) : Bool :=
  (c.length == weights.length) && (d.length == weights.length) &&
  (2^b * g == 3*h + dot weights c) &&
  ((c.zipWith (fun u v => (2^b*v == 2*u) || (2^b*v == 4*u)) d).all id) &&
  (c.all (fun u => u == 2 || u == 4 || (b == 1 && u == 1)))

private def checkWord (weights : List ℤ) : List Nat → List (List ℤ) → List ℤ → Bool
  | [], [_], [_] => true
  | b :: bs, c :: d :: cs, h :: g :: hs =>
      checkEdge weights b c d h g && checkWord weights bs (d :: cs) (g :: hs)
  | _, _, _ => false

theorem thirdTable :
    checkWord d3 [1,2,1,2,2,1,2]
      [[2,2,2,2],[2,2,4,4],[1,2,2,4],[2,4,2,4],[2,2,2,4],
       [1,1,2,2],[2,2,4,2],[2,2,2,2]] [0,0,-1,0,2,2,2,0] = true := by decide

theorem fourthTable :
    checkWord d4 [1,2,1,2,2,1]
      [[2,2,2,2,2],[2,4,4,4,2],[2,2,2,2,1],[4,2,4,2,2],
       [4,2,2,2,2],[2,2,1,2,2],[2,2,2,2,2]] [0,0,-1,-2,2,2,0] = true := by decide

theorem nativeEdge {b a c d x y : ℤ} (hc : c ≠ 0)
    (hscaled : b * (d*y) = 3*(c*x) + c) (hclock : b*d = a*c) :
    a*y = 3*x+1 := by
  apply mul_left_cancel₀ hc
  calc
    c*(a*y) = (b*d)*y := by rw [hclock]; ring
    _ = c*(3*x+1) := by linear_combination hscaled

/-- Removing the signed carry in the final slot retains exactly its original lattice residue. -/
theorem closeLast {M A y : ℤ} (h : M ∣ A + y) :
    (y - (A+y)) ≡ y [ZMOD M] ∧ A + (y - (A+y)) = 0 := by
  constructor
  · apply Int.modEq_iff_dvd.mpr
    convert h using 1
    ring
  · ring

theorem cubicLift (A B i : ℤ) :
    (A+B*(i+4)^3)-4*(A+B*(i+3)^3)+6*(A+B*(i+2)^3)
      -4*(A+B*(i+1)^3)+(A+B*i^3) = 0 := by ring

theorem quadraticLift (A B i : ℤ) :
    (A+B*(i+3)^2)-3*(A+B*(i+2)^2)+3*(A+B*(i+1)^2)-(A+B*i^2) = 0 := by ring

#print axioms thirdTable
#print axioms fourthTable
#print axioms nativeEdge
#print axioms closeLast
#print axioms cubicLift
#print axioms quadraticLift

end Collatz.HigherDifference
