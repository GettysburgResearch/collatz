import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite arithmetic kernels for the ordinary smaller-parent row and the
positive route-defect bound. The measure and infinite-path conclusions in
PARENT_ROWS.md use the written arguments. -/

namespace Collatz.ParentRows

set_option autoImplicit false

/-- Composition at one child with multiplier M=2^e, carrying the
unnormalized affine sum W and the current positive row scale H. -/
theorem appendRow {q v u H M W c : ℚ} (hH : H ≠ 0)
    (hprefix : 3*v+1=H*(3*q+1+W)) (edge : 3*u+1=M*(3*v+1+c)) :
    3*u+1=(H*M)*(3*q+1+(W+c/H)) := by
  rw [edge, hprefix]
  field_simp
  ring

/-- For two equal final branches, the endpoint difference is the parent
difference times the exact dyadic branch multiplier. -/
theorem undoSameBranch {v w p q M c : ℤ}
    (left : 3*v+1=M*(3*p+1+c)) (right : 3*w+1=M*(3*q+1+c)) :
    v-w=M*(p-q) := by
  nlinarith [left, right]

/-- The leftmost possible value of the coded residual is -4 and the
rightmost is 2. The two first-gap parities leave an open gap. -/
theorem initialParityGap {W u v : ℚ} (lo : -4 ≤ W) (hi : W ≤ 2)
    (hu : 0 ≤ u) (hv : 0 ≤ v) (oddBound : u ≤ 1/2) (evenBound : v ≤ 1/4) :
    (-1 ≤ 1+u*W ∧ 1+u*W ≤ 2) ∧
    (-4 ≤ -3+v*W ∧ -3+v*W ≤ -5/2) := by
  constructor
  · constructor
    · nlinarith [mul_nonneg hu (show 0 ≤ W+4 by linarith)]
    · nlinarith [mul_nonneg hu (show 0 ≤ 2-W by linarith)]
  · constructor
    · nlinarith [mul_nonneg hv (show 0 ≤ W+4 by linarith)]
    · nlinarith [mul_nonneg hv (show 0 ≤ 2-W by linarith)]

/-- Any edge whose inverse multiplier is at least 4/3 creates excess
of at least 2/3 above the all-ones fixed defect 1. -/
theorem firstNonunitGain {inv next : ℚ} (hi : 4/3 ≤ inv) (hn : 1 ≤ next) :
    1+2/3 ≤ 1/3+inv*next := by
  nlinarith [mul_nonneg (show 0 ≤ inv by linarith) (show 0 ≤ next-1 by linarith)]

/-- A run of odd exponents equal to one propagates that strict excess
back to the fixed original state. -/
theorem initialRunDefect (defect : ℕ → ℚ) (n : ℕ) (m : ℚ)
    (run : ∀ i < n, defect i=1/3+(2/3)*defect (i+1))
    (tail : 1+m ≤ defect n) :
    1+(2/3)^n*m ≤ defect 0 := by
  induction n generalizing defect m with
  | zero => simpa using tail
  | succ n ih =>
    have rest : ∀ i < n, (fun i => defect (i+1)) i =
        1/3+(2/3)*(fun i => defect (i+1)) (i+1) := by
      intro i hi
      exact run (i+1) (by omega)
    have rr := ih (fun i => defect (i+1)) m rest tail
    have first := run 0 (Nat.zero_lt_succ n)
    rw [pow_succ]
    dsimp at rr
    nlinarith

#print axioms appendRow
#print axioms undoSameBranch
#print axioms initialParityGap
#print axioms firstNonunitGain
#print axioms initialRunDefect

end Collatz.ParentRows
