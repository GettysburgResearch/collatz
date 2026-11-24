import Std

namespace Collatz.CyclePartition

def jumps (w c : Nat → Int) : Nat → Int
  | 0 => 0
  | n + 1 => jumps w c n + w (n + 1) * (c n - c (n + 1))

/-- Equation (3) with zero-indexed windows, after clearing center denominators. -/
theorem centered_telescope (w z c : Nat → Int)
    (edge : ∀ j, w (j+1) * (z (j+1) - c j) = w j * (z j - c j)) (n : Nat) :
    w (n+1) * (z (n+1) - c n) - w 0 * (z 0 - c 0) = jumps w c n := by
  induction n with
  | zero => rw [edge 0]; simp [jumps]
  | succ n ih =>
    rw [edge (n+1), jumps, ← ih]
    grind

#print axioms centered_telescope
end Collatz.CyclePartition
