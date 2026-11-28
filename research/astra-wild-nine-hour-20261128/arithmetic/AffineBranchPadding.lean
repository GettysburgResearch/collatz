import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Ring

/-! Numerators for chronological shortcut parity words. The fixed suffix
can consume any number of additional native steps and odd departures.
Separation at the full earlier modulus survives the complete new modulus. -/

set_option autoImplicit false

namespace Collatz.AffineBranchPadding

def grade : List Bool → ℕ
  | [] => 0
  | b :: w => grade w + if b then 1 else 0

def numerator : List Bool → ℤ
  | [] => 0
  | b :: w => (if b then 3 ^ grade w else 0) + 2 * numerator w

theorem grade_append (u v : List Bool) :
    grade (u ++ v) = grade u + grade v := by
  induction u with
  | nil => simp [grade]
  | cons b u ih =>
    cases b <;> simp [grade, ih, Nat.add_comm, Nat.add_left_comm]

theorem numerator_append (u v : List Bool) :
    numerator (u ++ v) = 3 ^ grade v * numerator u + 2 ^ u.length * numerator v := by
  induction u with
  | nil => simp [numerator]
  | cons b u ih =>
    cases b <;> simp [numerator, grade_append, ih, pow_add, pow_succ] <;> ring

theorem suffix_preserves_residue (u w v : List Bool)
    (sameLength : u.length = w.length) (sameGrade : grade u = grade w)
    (collision : numerator (u ++ v) ≡ numerator (w ++ v) [ZMOD 3 ^ grade (u ++ v)]) :
    numerator u ≡ numerator w [ZMOD 3 ^ grade w] := by
  rw [numerator_append, numerator_append, sameLength, grade_append, sameGrade,
      Nat.add_comm (grade w), pow_add] at collision
  apply Int.ModEq.mul_left_cancel' (c := (3 : ℤ) ^ grade v) (pow_ne_zero _ (by decide))
  exact Int.ModEq.add_right_cancel' _ collision

#print axioms grade_append
#print axioms numerator_append
#print axioms suffix_preserves_residue

end Collatz.AffineBranchPadding
