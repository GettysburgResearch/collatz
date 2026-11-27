import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.RivalPressure

/-- Propagate an actual scaled affine rival along two ordinary inverse edges.
The coefficient and offset equalities are independently checked at each finite
transducer edge. All quantities here are integers. -/
theorem affine_reverse {x X y Y a b A B C A' B' C' : ℤ}
    (hB : B ≠ 0) (native : 3*X = a*x-1) (rival : 3*Y = b*y-1)
    (before : B*y = A*x+C) (slope : B'*b*A = B*A'*a)
    (offset : 3*B*C' = B'*b*C+B*A'-B*B') :
    B'*Y = A'*X+C' := by
  have cancel : (3:ℤ)*B ≠ 0 := mul_ne_zero (by norm_num) hB
  apply mul_left_cancel₀ cancel
  calc
    3*B*(B'*Y) = B*B'*(3*Y) := by ring
    _ = B*B'*(b*y-1) := by rw [rival]
    _ = B'*b*(B*y)-B*B' := by ring
    _ = B'*b*(A*x+C)-B*B' := by rw [before]
    _ = (B'*b*A)*x+(B'*b*C+B*A'-B*B')-B*A' := by ring
    _ = (B*A'*a)*x+(3*B*C')-B*A' := by rw [slope, offset]
    _ = B*A'*(a*x-1)+3*B*C' := by ring
    _ = B*A'*(3*X)+3*B*C' := by rw [← native]
    _ = 3*B*(A'*X+C') := by ring

/-- The weight bound composes across a return when its three grade counts
are merely upper bounds. All masses and comparison weights are rational here. -/
theorem weighted_return (a b c u v w U V W bound : ℚ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c)
    (hu : u ≤ U) (hv : v ≤ V) (hw : w ≤ W)
    (budget : a*U+b*V+c*W ≤ bound) :
    a*u+b*v+c*w ≤ bound := by
  calc
    a*u+b*v+c*w ≤ a*U+b*V+c*W :=
      add_le_add (add_le_add (mul_le_mul_of_nonneg_left hu ha)
                             (mul_le_mul_of_nonneg_left hv hb))
                 (mul_le_mul_of_nonneg_left hw hc)
    _ ≤ bound := budget

private def legal (b : Fin 2) (old new : Fin 2) : Bool :=
  decide (1 ≤ (b.val:ℤ)+1+new.val-old.val ∧ (b.val:ℤ)+1+new.val-old.val ≤ 2)

private def ways (b old₁ old₂ : Fin 2) (target : ℕ) : ℕ :=
  ((List.finRange 2).flatMap fun x =>
    (List.finRange 2).filter fun y =>
      legal b old₁ x && legal b old₂ y && (x.val+y.val == target)).length

/-- Any fixed orientation of the untracked equal-pair side has two eligible
predecessors exactly on an extreme-to-middle allowed move. -/
theorem complement_ways :
    ∀ b i j x y : Fin 2, legal b i x = true → legal b j y = true →
      ways b i j (x.val+y.val) =
        if x.val+y.val = 1 ∧ i.val+j.val ≠ 1 then 2 else 1 := by decide

#print axioms affine_reverse
#print axioms weighted_return
#print axioms complement_ways

end Collatz.RivalPressure
