import Std

namespace Collatz.FixedSourceWindow

/-- Binary division time on [start, start + length). -/
def clock (a : Nat → Nat) (start : Nat) : Nat → Nat
  | 0 => 0
  | l+1 => clock a start l + a (start+l)

/-- D clears denominators of the virtual rational states t_i / D. -/
def defect (a : Nat → Nat) (t : Nat → Int) (D : Int) (i : Nat) : Int :=
  3*t i+D-(2:Int)^(a i)*t (i+1)

/-- Recursion gives one ternary weight to the accumulated defects at
 each extension and binary weight to the new signed error. -/
def weightedErrors (a : Nat → Nat) (t : Nat → Int) (D : Int) (j : Nat) : Nat → Int
  | 0 => 0
  | l+1 => 3*weightedErrors a t D j l+(2:Int)^(clock a j l)*defect a t D (j+l)

/-- Clear denominators, then telescope a genuinely arbitrary translated
 window. The certificate uses only the actual edge equations on the window. -/
theorem virtual_window (q t : Nat → Int) (a : Nat → Nat) (D : Int) (j l : Nat)
    (he : ∀ i, j ≤ i → i < j+l → (2:Int)^(a i)*q (i+1)=3*q i+1) :
    (2:Int)^(clock a j l)*(D*q (j+l)-t (j+l)) =
    (3:Int)^l*(D*q j-t j)+weightedErrors a t D j l := by
  induction l with
  | zero => simp [clock, weightedErrors]
  | succ l ih =>
    have h := ih (fun i lo hi => he i lo (by omega))
    have e := he (j+l) (by omega) (by omega)
    have localEdge : (2:Int)^(a (j+l))*(D*q (j+l+1)-t (j+l+1)) =
        3*(D*q (j+l)-t (j+l))+defect a t D (j+l) := by
      unfold defect
      grind
    simp only [clock, weightedErrors, Int.pow_add, Int.pow_succ]
    change (2:Int)^(clock a j l)*(2:Int)^(a (j+l))*(D*q (j+l+1)-t (j+l+1)) = _
    rw [Int.mul_assoc, localEdge]
    grind

#print axioms virtual_window
end Collatz.FixedSourceWindow
