/-!
Integer certificate pieces for the independent P^a Q^b cycle exclusion.

P is the binary word 11100011110, with affine map (2187*x+5699)/2048;
Q is 10, with affine map (3*x+1)/4.

The companion written proof supplies the arbitrary-exponent reduction to
either the Farey interval below or the bounded full-denominator cases.
These theorems do not assume or formalize Matveev, logarithm bounds, or a
global Collatz assertion.  `decide` is kernel checked; no native_decide is used.
-/

namespace CollatzIndependentPQCertificate

def clockCutoff : Nat := 4722397970736130105600

/-- An exact Farey gap contains no rational with the permitted denominator.
No coprimality assumption on `L,S` is required. -/
theorem tail_farey_obstruction {L S : Nat}
    (clock : S ≤ clockCutoff)
    (lower : 7373006092034578625129 * S < 4651848916728231124485 * L)
    (upper : 205632218873398596256 * L < 325919355854421968365 * S) :
    False := by
  unfold clockCutoff at clock
  omega

def fullNumerator (a b : Nat) : Nat :=
  2048 ^ a * 4 ^ b + 41 * 2187 ^ a * 3 ^ b - 42 * 2048 ^ a * 3 ^ b

def denominatorPositivePart (a b : Nat) : Nat :=
  2048 ^ a * 4 ^ b - 2187 ^ a * 3 ^ b

/-- Exact finite exhaustion of all remaining independent exponent pairs.
The first alternative handles a nonpositive signed cycle denominator;
the second excludes divisibility by the entire positive denominator. -/
theorem small_full_denominator_exclusion :
    ∀ a b : Fin 16, 0 < a.val → 0 < b.val → b.val < a.val →
      (2048 ^ a.val * 4 ^ b.val ≤ 2187 ^ a.val * 3 ^ b.val ∨
       fullNumerator a.val b.val % denominatorPositivePart a.val b.val ≠ 0) := by
  decide

/-- The same finite theorem with ordinary natural-number parameters. -/
theorem small_natural_exponent_exclusion {a b : Nat}
    (apos : 0 < a) (asmall : a < 16) (bpos : 0 < b) (blt : b < a) :
    2048 ^ a * 4 ^ b ≤ 2187 ^ a * 3 ^ b ∨
      fullNumerator a b % denominatorPositivePart a b ≠ 0 := by
  exact small_full_denominator_exclusion ⟨a, asmall⟩ ⟨b, by omega⟩ apos bpos blt

#print axioms tail_farey_obstruction
#print axioms small_full_denominator_exclusion
#print axioms small_natural_exponent_exclusion

end CollatzIndependentPQCertificate
