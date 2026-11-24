import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Complete shortcut-word carries and finite modulus payment

The first bit is the first shortcut step. These are identities for the
whole word, including every affine correction. The construction of a
balanced word, its primitive marker, the rational-cycle minimum, and
Euler/Fermat parameter selection are written in CYCLE_IDEAL.md; they are
not hypotheses smuggled into a theorem claiming the full construction.
-/

namespace Collatz.HighVariance.CycleWordAlgebra

def ones : List Bool → Nat
  | [] => 0
  | b :: w => (if b then 1 else 0) + ones w

def carry : List Bool → Nat
  | [] => 0
  | b :: w => 3 ^ ones w * (if b then 1 else 0) + 2 * carry w

def repeatWord (w : List Bool) : Nat → List Bool
  | 0 => []
  | k + 1 => repeatWord w k ++ w

def denominator (w : List Bool) : Int := 2 ^ w.length - 3 ^ ones w

theorem ones_append (u v : List Bool) : ones (u ++ v) = ones u + ones v := by
  induction u with
  | nil => simp [ones]
  | cons b u ih => simp [ones, ih, Nat.add_assoc]

/-- Exact chronological concatenation, before any modular reduction. -/
theorem carry_append (u v : List Bool) :
    carry (u ++ v) = 3 ^ ones v * carry u + 2 ^ u.length * carry v := by
  induction u with
  | nil => simp [carry]
  | cons b u ih =>
    cases b <;> simp [carry, ones_append, ih, pow_add, pow_succ] <;> ring

/-- An adjacent exchange retains every earlier and later bit. -/
theorem adjacent_swap (u v : List Bool) :
    carry (u ++ [false, true] ++ v) =
      carry (u ++ [true, false] ++ v) + 2 ^ u.length * 3 ^ ones v := by
  simp [carry_append, carry, ones, pow_add, pow_succ]
  ring

/-- The single defect used in the construction has an exact unit carry. -/
theorem marked_swap (v : List Bool) :
    carry ([true, false, true] ++ v) =
      carry ([true, true, false] ++ v) + 2 * 3 ^ ones v := by
  simpa using adjacent_swap [true] v

theorem repeat_length (w : List Bool) (k : Nat) :
    (repeatWord w k).length = k * w.length := by
  induction k with
  | zero => simp [repeatWord]
  | succ k ih => simp [repeatWord, ih, Nat.add_mul]

theorem repeat_ones (w : List Bool) (k : Nat) :
    ones (repeatWord w k) = k * ones w := by
  induction k with
  | zero => simp [repeatWord, ones]
  | succ k ih => simp [repeatWord, ones_append, ih, Nat.add_mul]

variable {R : Type*} [CommRing R]

/-- Any ring quotient in which both block multipliers are one sees the
complete repeated carry as a translation by k times the block carry. -/
theorem repeat_carry_cast (w : List Bool) (k : Nat)
    (h2 : (2 : R) ^ w.length = 1) (h3 : (3 : R) ^ ones w = 1) :
    (carry (repeatWord w k) : R) = (k : R) * (carry w : R) := by
  induction k with
  | zero => simp [repeatWord, carry]
  | succ k ih =>
    have hp : (2 : R) ^ (repeatWord w k).length = 1 := by
      rw [repeat_length, Nat.mul_comm k w.length, pow_mul, h2, one_pow]
    simp only [repeatWord, carry_append, Nat.cast_add, Nat.cast_mul, Nat.cast_pow,
      Nat.cast_ofNat]
    rw [h3, hp, one_mul, one_mul, ih]
    push_cast
    ring

/-- Payment by two complete block families, without losing any denominator
prime through a norm or a proper-factor test. -/
theorem two_block_carry_cast (u v : List Bool) (r s : Nat)
    (u2 : (2 : R) ^ u.length = 1) (u3 : (3 : R) ^ ones u = 1)
    (v2 : (2 : R) ^ v.length = 1) (v3 : (3 : R) ^ ones v = 1) :
    (carry (repeatWord u r ++ repeatWord v s) : R) =
      (r : R) * (carry u : R) + (s : R) * (carry v : R) := by
  have hp : (2 : R) ^ (repeatWord u r).length = 1 := by
    rw [repeat_length, Nat.mul_comm r u.length, pow_mul, u2, one_pow]
  have hq : (3 : R) ^ ones (repeatWord v s) = 1 := by
    rw [repeat_ones, Nat.mul_comm s (ones v), pow_mul, v3, one_pow]
  simp only [carry_append, Nat.cast_add, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat]
  rw [hp, hq, one_mul, one_mul, repeat_carry_cast u r u2 u3,
    repeat_carry_cast v s v2 v3]

theorem two_block_denominator_cast (u v : List Bool) (r s : Nat)
    (u2 : (2 : R) ^ u.length = 1) (u3 : (3 : R) ^ ones u = 1)
    (v2 : (2 : R) ^ v.length = 1) (v3 : (3 : R) ^ ones v = 1) :
    (denominator (repeatWord u r ++ repeatWord v s) : R) = 0 := by
  simp only [denominator, Int.cast_sub,
    List.length_append, ones_append, repeat_length, repeat_ones, pow_add]
  rw [Nat.mul_comm r u.length, Nat.mul_comm s v.length,
    Nat.mul_comm r (ones u), Nat.mul_comm s (ones v)]
  simp [pow_mul, u2, u3, v2, v3]

/-- Multiplicity M pays every congruence in a quotient with M=0. -/
theorem fixed_modulus_payment (u v : List Bool) (k M : Nat)
    (hM : (M : R) = 0)
    (u2 : (2 : R) ^ u.length = 1) (u3 : (3 : R) ^ ones u = 1)
    (v2 : (2 : R) ^ v.length = 1) (v3 : (3 : R) ^ ones v = 1) :
    (carry (repeatWord u (k * M) ++ repeatWord v M) : R) = 0 ∧
      (denominator (repeatWord u (k * M) ++ repeatWord v M) : R) = 0 := by
  constructor
  · rw [two_block_carry_cast u v (k * M) M u2 u3 v2 v3]
    simp [hM]
  · exact two_block_denominator_cast u v (k * M) M u2 u3 v2 v3

/-- One of the two complete block multiplicities retains a nonzero carry. -/
theorem two_choice_nonzero (u v : R) (hne : u ≠ v) :
    u + v ≠ 0 ∨ 2 * u + v ≠ 0 := by
  by_cases h1 : u + v = 0
  · right
    intro h2
    have hu : u = 0 := by
      calc
        u = (2 * u + v) - (u + v) := by ring
        _ = 0 := by rw [h2, h1]; ring
    have hv : v = 0 := by simpa [hu] using h1
    exact hne (hu.trans hv.symm)
  · exact Or.inl h1

theorem scaled_two_choice_nonzero [IsDomain R] (m u v : R)
    (hm : m ≠ 0) (hne : u ≠ v) :
    m * (u + v) ≠ 0 ∨ m * (2 * u + v) ≠ 0 := by
  rcases two_choice_nonzero u v hne with h | h
  · exact Or.inl (mul_ne_zero hm h)
  · exact Or.inr (mul_ne_zero hm h)

end Collatz.HighVariance.CycleWordAlgebra
