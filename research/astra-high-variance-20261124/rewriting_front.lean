import Std

namespace Collatz.RewriteFront

/-- The incoming ternary digit and one binary digit exchange positions. -/
theorem commute_digit (b t : Nat) (hb : b < 2) (ht : t < 3) :
    2 * ((3*b+t)/2) + ((3*b+t)%2) = 3*b+t ∧ (3*b+t)/2 < 3 := by omega

/-- Read a k-bit binary suffix from right to left with incoming carry 2. -/
def sweep : Nat → Nat → Nat → Nat
  | 0, _, t => t
  | k+1, s, t => sweep k (s/2) ((3*(s%2)+t)/2)

/-- Exact carry emerging from an arbitrary binary suffix. -/
theorem sweep_closed (k s t : Nat) :
    sweep k s t = (3*(s % 2^k)+t)/2^k := by
  induction k generalizing s t with
  | zero => simp [sweep, Nat.mod_one]
  | succ k ih =>
    rw [sweep, ih, Nat.pow_succ]
    have split : s % (2^k * 2) = 2 * ((s/2) % 2^k) + s%2 := by
      rw [Nat.mul_comm, Nat.mod_mul]
      omega
    rw [split]
    generalize (s/2) % 2^k = u
    rw [Nat.mul_comm (2^k) 2, ← Nat.div_div_eq_div_mul]
    congr 1
    omega

#print axioms commute_digit
#print axioms sweep_closed

end Collatz.RewriteFront
