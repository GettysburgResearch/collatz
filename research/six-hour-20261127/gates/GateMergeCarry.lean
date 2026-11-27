import GateDyadicMoment

namespace Collatz.GateMergeCarry

open Collatz.GateDyadicMoment

/-- The unnormalised integer translation in the length-k shortcut word. -/
def carry : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k + 1, x =>
    if state k x % 2 = 0 then carry k x else 3 * carry k x + 2^k

theorem word_affine (k x : ℕ) :
    2^k * state k x = 3^(oddCount k x) * x + carry k x := by
  induction k with
  | zero => simp [state, oddCount, carry]
  | succ k ih =>
    simp only [state, oddCount, carry, pow_succ (2:ℕ) k,
      pow_add (3:ℕ) (oddCount k x), Nat.mul_assoc (2^k) 2, shortcut_twice]
    by_cases he : state k x % 2 = 0
    · simpa [he] using ih
    · have ho : state k x % 2 = 1 := by omega
      simp only [ho, Nat.one_ne_zero, ite_false, pow_one]
      calc
        _ = 3 * (2^k * state k x) + 2^k := by ring
        _ = _ := by rw [ih]; ring

/-- Equal endpoint and equal odd count turn a change of source into the
opposite weighted change of translation. -/
theorem balanced_carry (k x r : ℕ)
    (hs : state k x = state k (x+r))
    (hq : oddCount k x = oddCount k (x+r)) :
    carry k x = carry k (x+r) + 3^(oddCount k x) * r := by
  have hx := word_affine k x
  have hr := word_affine k (x+r)
  rw [← hs, ← hq, Nat.mul_add] at hr
  omega

end Collatz.GateMergeCarry

#print axioms Collatz.GateMergeCarry.word_affine
#print axioms Collatz.GateMergeCarry.balanced_carry
