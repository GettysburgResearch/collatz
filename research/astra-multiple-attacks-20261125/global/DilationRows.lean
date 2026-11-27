import Std

set_option autoImplicit false

/-! Ordinary row counts for the local dilation argument. The shortcut sends
2n to n and 2n+1 to 3n+2. All input and output indices are ordinary naturals.
The defect is retained explicitly so the bounds apply to a genuine visit mark. -/
namespace DilationRows

def countPrefix (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => countPrefix f n + f n

def gap (x y : Bool) : Nat := if x = y then 0 else 1

def edge (b : Nat → Bool) (n : Nat) : Nat := gap (b n) (b (n+1))

def oddDefect (b : Nat → Bool) (n : Nat) : Nat :=
  gap (b (2*n+1)) (b (3*n+2))

def cell (b : Nat → Bool) (q n : Nat) : Nat :=
  countPrefix (fun r => gap (b n) (b (q*n+r))) q

private theorem triangle (x y z : Bool) : gap x z ≤ gap x y + gap y z := by
  cases x <;> cases y <;> cases z <;> decide

private theorem symm (x y : Bool) : gap x y = gap y x := by
  cases x <;> cases y <;> decide

private theorem splitTwo (b : Nat → Bool) (n : Nat) :
    countPrefix (edge b) (2*(n+1)) =
    countPrefix (edge b) (2*n) + edge b (2*n) + edge b (2*n+1) := by
  rw [show 2*(n+1) = (2*n+1)+1 by omega]
  rfl

private theorem splitThree (b : Nat → Bool) (n : Nat) :
    countPrefix (edge b) (3*(n+1)) =
    countPrefix (edge b) (3*n) + edge b (3*n) + edge b (3*n+1) + edge b (3*n+2) := by
  rw [show 3*(n+1) = ((3*n+1)+1)+1 by omega]
  rfl

/-- Every binary subdivision mismatch uses the edge from 2n to 2n+1. -/
theorem binaryCount (b : Nat → Bool) (double : ∀ n, b (2*n) = b n) (N : Nat) :
    countPrefix (cell b 2) N ≤ countPrefix (edge b) (2*N) := by
  induction N with
  | zero => simp [countPrefix]
  | succ n ih =>
    have single : cell b 2 n = edge b (2*n) := by
      simp [cell, countPrefix, edge, double, gap]
    rw [countPrefix, single, splitTwo]
    omega

private theorem ternaryCell (b : Nat → Bool) (double : ∀ n, b (2*n) = b n) (n : Nat) :
    cell b 3 n ≤ 3*(edge b (2*n) + oddDefect b n) + edge b (3*n) + 2*edge b (3*n+1) := by
  have near := triangle (b n) (b (2*n+1)) (b (3*n+2))
  have mid := triangle (b n) (b (3*n+2)) (b (3*n+1))
  have far := triangle (b n) (b (3*n+1)) (b (3*n))
  rw [symm (b (3*n+2)) (b (3*n+1))] at mid
  rw [symm (b (3*n+1)) (b (3*n))] at far
  simp only [cell, countPrefix, Nat.add_zero, Nat.zero_add, edge, oddDefect, double, Nat.add_assoc, show 1+1 = 2 by decide]
  omega

/-- Total ternary mismatches through row N, including the exact charge
for any failed odd edges. The number of cells is independent of their colors. -/
theorem ternaryCount (b : Nat → Bool) (double : ∀ n, b (2*n) = b n) (N : Nat) :
    countPrefix (cell b 3) N ≤ 3*countPrefix (edge b) (2*N) +
      2*countPrefix (edge b) (3*N) + 3*countPrefix (oddDefect b) N := by
  induction N with
  | zero => simp [countPrefix]
  | succ n ih =>
    have single := ternaryCell b double n
    rw [countPrefix, splitTwo, splitThree]
    change _ ≤ _ + _ + 3 * (countPrefix (oddDefect b) n + oddDefect b n)
    omega

#print axioms binaryCount
#print axioms ternaryCount

end DilationRows
