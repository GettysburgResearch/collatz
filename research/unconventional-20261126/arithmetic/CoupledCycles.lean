import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Compiling paired shortcut words

The branches here are prescribed affine maps. Physical realizability of their
positive rational fixed points is the separate rotated-word argument in the
accompanying proof.
-/

namespace CoupledCycles

/-- Bits are supplied in chronological order. -/
def run : List Bool → ℚ → ℚ
  | [], x => x
  | e :: w, x => run w (if e then (3 * x + 1) / 2 else x / 2)

theorem run_append (v w : List Bool) (x : ℚ) : run (v ++ w) x = run w (run v x) := by
  induction v generalizing x with
  | nil => rfl
  | cons e v ih =>
      simp only [List.cons_append, run]
      exact ih _

/-- Each letter chooses a pair of words with the same clock and affine conjugacy. -/
inductive Block where | a | b | c

def input : Block → List Bool
  | .a => [true, false]
  | .b => [false, true, false]
  | .c => [true, true, false, true, false, false, false, false, false, false, false, true]

def output : Block → List Bool
  | .a => [false, true]
  | .b => [true, false, false]
  | .c => [false, false, false, false, false, true, true, true, false, true, false, false]

theorem one_block (letter : Block) (x : ℚ) : run (output letter) (3*x-1) = 3*run (input letter) x-1 := by
  cases letter <;> simp [input, output, run] <;> ring

theorem any_blocks (bs : List Block) (x : ℚ) :
    run (bs.flatMap output) (3*x-1) = 3*run (bs.flatMap input) x-1 := by
  induction bs generalizing x with
  | nil => rfl
  | cons letter bs ih =>
      simp only [List.flatMap_cons, run_append, one_block]
      exact ih _

/-- The marker supplies actual algebraic reciprocal tripling identities at its
specified cuts. The first eleven input letters and first five output letters
are the two marked odd phases. -/
theorem reciprocal (z : ℚ) :
    64 * run ((input .c).take 11) z = 9 * run ((output .c).take 5) (3*z-1) + 1 ∧
    (9 * run ((input .c).take 11) z + 1)/2 = run (output .c) (3*z-1) := by
  constructor <;> norm_num [input, output, run] <;> ring

#print axioms run_append
#print axioms one_block

end CoupledCycles

#print axioms CoupledCycles.any_blocks
#print axioms CoupledCycles.reciprocal
