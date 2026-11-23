/-
A genuine exponent contraction: every even Mersenne exponent e >= 2 folds
to e-1 by ordinary moves. This proves a smaller-instance reduction, not
convergence of the remaining odd-exponent family.
Interface: Collatz.Closure from PR174, 7034109ed60a26bc49824e1ed43c239ceca81194.
-/
import Collatz.Closure

open CollatzReverseBasin

namespace CollatzGlobal

private theorem odd_three_pow_mod_four (r : Nat) : 3^(2*r+1) % 4 = 3 := by
  induction r with
  | zero => rfl
  | succ r ih =>
    have e : 2*(r+1)+1 = (2*r+1)+1+1 := by omega
    rw [e, Nat.pow_succ, Nat.pow_succ]
    omega

/-- The same positive ordinary endpoint is reached after halving the odd-index
ternary predecessor and taking its next odd move. -/
theorem ternary_even_exponent_fold (r : Nat) :
    Basin (3^(2*r+2)-1) ↔ Basin (3^(2*r+1)-1) := by
  let z := (3^(2*r+1)-1)/2
  have mod4 := odd_three_pow_mod_four r
  have p : 0 < 3^(2*r+1) := Nat.pow_pos (by omega)
  have odd : z % 2 = 1 := by dsimp [z]; omega
  have old : 3^(2*r+1)-1 = 2*z := by dsimp [z]; omega
  have e : 2*r+2 = (2*r+1)+1 := by omega
  have new : 3^(2*r+2)-1 = 2*(3*z+1) := by
    rw [e, Nat.pow_succ]
    omega
  rw [new, old]
  exact (CollatzClosure.basin_twice _).trans
    ((CollatzClosure.basin_odd z odd).trans (CollatzClosure.basin_twice z).symm)

/-- A terminating step in the exponent: e=2r+2 reduces to e-1=2r+1.
Both corresponding power-of-two source certificates are known; the smaller
source is exactly the first halving tail of the larger source. -/
theorem mersenne_even_exponent_fold (r : Nat) :
    Basin (2^(2*r+2)-1) ↔ Basin (2^(2*r+1)-1) := by
  have old := CollatzClosure.basin_pow_two_pred (2*r+2) 1 (by omega)
  have new := CollatzClosure.basin_pow_two_pred (2*r+1) 1 (by omega)
  simp only [Nat.mul_one] at old new
  exact old.trans ((ternary_even_exponent_fold r).trans new.symm)

end CollatzGlobal
