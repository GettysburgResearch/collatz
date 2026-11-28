import Init.Omega

/-! Exact finite disagreement accounting at a dyadic refinement.
    The two child intervals have equal length. -/

namespace Collatz.DyadicMidpoint

def flip (u v : Bool) : Nat := if u = v then 0 else 1

@[simp] theorem flip_self (u : Bool) : flip u u = 0 := by simp [flip]

theorem flip_triangle (u v w : Bool) : flip u w ≤ flip u v + flip v w := by
  cases u <;> cases v <;> cases w <;> decide

def mismatches (f g : Nat → Bool) (a : Nat) : Nat → Nat
  | 0 => 0
  | n+1 => mismatches f g a n + flip (f (a+n)) (g (a+n))

theorem mismatches_triangle (f g h : Nat → Bool) (a n : Nat) :
    mismatches f h a n ≤ mismatches f g a n + mismatches g h a n := by
  induction n with
  | zero => simp [mismatches]
  | succ n ih =>
    have last := flip_triangle (f (a+n)) (g (a+n)) (h (a+n))
    simp only [mismatches]
    omega

theorem midpoint_identity (f : Nat → Bool) (even : ∀ n, f (2*n) = f n)
    (a n : Nat) :
    mismatches f (fun x => f (x/2)) (2*a) (2*n) =
      mismatches (fun x => f (2*x+1)) f a n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have z : 2*(n+1) = (2*n+1)+1 := by omega
    rw [z]
    change mismatches f (fun x => f (x/2)) (2*a) (2*n) +
        flip (f (2*a+2*n)) (f ((2*a+2*n)/2)) +
        flip (f (2*a+(2*n+1))) (f ((2*a+(2*n+1))/2)) =
      mismatches (fun x => f (2*x+1)) f a n + flip (f (2*(a+n)+1)) (f (a+n))
    have evenIndex : 2*a+2*n = 2*(a+n) := by omega
    have oddIndex : 2*a+(2*n+1) = 2*(a+n)+1 := by omega
    have lower : (2*(a+n))/2 = a+n := by omega
    have upper : (2*(a+n)+1)/2 = a+n := by omega
    rw [ih, evenIndex, oddIndex, lower, upper, even, flip_self, Nat.add_zero]

#print axioms midpoint_identity

end Collatz.DyadicMidpoint
