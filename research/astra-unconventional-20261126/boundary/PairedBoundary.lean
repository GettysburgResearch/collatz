import Mathlib.Tactic.Ring
import Mathlib.Data.Int.Basic

namespace Collatz.PairedBoundary

variable {α : Type*} (f : ℕ → α)
variable (halving : ∀ n, f (2*n) = f n)
variable (oddStep : ∀ n, f (2*n+1) = f (3*n+2))

include oddStep

/-- All odd shortcuts in a long rise, expressed in the labels of its endpoints. -/
theorem rise (h z : ℕ) (positive : 0 < z) :
    f (2^h*z-1) = f (3^h*z-1) := by
  induction h generalizing z with
  | zero => simp
  | succ h ih =>
    have hp : 0 < 2^h*z := Nat.mul_pos (Nat.pow_pos (by decide)) positive
    calc
      f (2^(h+1)*z-1) = f (2*(2^h*z-1)+1) := by
        congr 1
        rw [pow_succ]
        have he : 2^h*2*z = 2*(2^h*z) := by ring
        omega
      _ = f (3*(2^h*z-1)+2) := oddStep _
      _ = f (2^h*(3*z)-1) := by
        congr 1
        have he : 2^h*(3*z) = 3*(2^h*z) := by ring
        omega
      _ = f (3^h*(3*z)-1) := ih (3*z) (by omega)
      _ = f (3^(h+1)*z-1) := by rw [pow_succ]; ring_nf

include halving

/-- If the first crest lies in the indicated class mod four, the two adjacent
    source labels coincide. The exponent in the statement is one more than h. -/
theorem paired_rise (h z u : ℕ) (positive : 0 < z)
    (crest : 3^h*z = 4*u+3) :
    f (2^(h+1)*z-2) = f (2^(h+1)*z-1) := by
  have hp : 0 < 2^h*z := Nat.mul_pos (Nat.pow_pos (by decide)) positive
  have left_arg : 2^(h+1)*z-2 = 2*(2^h*z-1) := by
    rw [pow_succ]
    have he : 2^h*2*z = 2*(2^h*z) := by ring
    omega
  have right_arg : 3^(h+1)*z-1 = 2*(2*(3*u+2)) := by
    rw [pow_succ]
    have he : 3^h*3*z = 3*(3^h*z) := by ring
    omega
  calc
    f (2^(h+1)*z-2) = f (2^h*z-1) := by rw [left_arg, halving]
    _ = f (3^h*z-1) := rise f oddStep h z positive
    _ = f (2*(2*u+1)) := by congr 1; omega
    _ = f (2*u+1) := halving _
    _ = f (3*u+2) := oddStep _
    _ = f (2*(2*(3*u+2))) := by rw [halving, halving]
    _ = f (3^(h+1)*z-1) := by rw [right_arg]
    _ = f (2^(h+1)*z-1) := (rise f oddStep (h+1) z positive).symm

#print axioms rise
#print axioms paired_rise

end Collatz.PairedBoundary
