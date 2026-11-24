prelude
import Init.Omega
import Init.Classical

namespace Collatz.IntegerClock

/-- The full clock overshoots the ternary clock by less than a factor of two.
A contracting canonical cycle can then carry no positive integer cost. -/
theorem zero_carry (k A B K : Nat) (hclock : A = B + 2 * K)
    (hcontract : 3^k < 2^B) (hupper : 2^A < 2 * 3^k) : K = 0 := by
  apply Classical.byContradiction
  intro hn
  have he : B + 1 ≤ A := by omega
  have hp : 2^(B + 1) ≤ 2^A := Nat.pow_le_pow_right (by decide) he
  rw [Nat.pow_succ] at hp
  omega

/-- At most one binary clock fits the one-bit band for each period. -/
theorem unique_clock (t A B : Nat)
    (ha₁ : t < 2^A) (ha₂ : 2^A < 2*t)
    (hb₁ : t < 2^B) (hb₂ : 2^B < 2*t) : A = B := by
  have f (i j : Nat) (hi : t < 2^i) (hj : 2^j < 2*t) : ¬ i < j := by
    intro h
    have hp : 2^(i+1) ≤ 2^j := Nat.pow_le_pow_right (by decide) h
    rw [Nat.pow_succ] at hp
    omega
  have hab := f A B ha₁ hb₂
  have hba := f B A hb₁ ha₂
  omega

#print axioms zero_carry
#print axioms unique_clock
end Collatz.IntegerClock
