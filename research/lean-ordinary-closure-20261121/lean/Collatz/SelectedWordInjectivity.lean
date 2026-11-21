import Collatz.Closure

/-!
The exact integer injectivity used by the weighted residue-counting lemma in
LINEAR_BLOCK_ATOM_FLOOR.md.  Exponents are stored in reverse order, so the head
is the last exponent of the corresponding outward inverse word.

This file formalizes the finite arithmetic input.  It does not formalize Tao's
analytic estimate, the uniform-density argument, or the Collatz conjecture.
-/

namespace CollatzSelectedWords

/-- Exact integer forms of the elementary numerical constants used in the
linear block proof. -/
theorem linear_block_constants :
    2 * 6 ^ 10 ≤ 7 ^ 10 ∧
    20 * 7 ^ 6 < 9 * 8 ^ 6 ∧
    9 * 7 ^ 17 < 8 ^ 17 := by
  decide

def Positive : List Nat → Prop
  | [] => True
  | a :: w => 0 < a ∧ Positive w

def Total : List Nat → Nat
  | [] => 0
  | a :: w => a + Total w

/-- `2 ^ Total(w)` times the real offset of the outward word. -/
def Numerator : List Nat → Nat
  | [] => 0
  | a :: w => 2 ^ a * Numerator w + 3 ^ w.length

theorem pow_three_odd (n : Nat) : 3 ^ n % 2 = 1 := by
  induction n with
  | zero => decide
  | succ n ih => simp [Nat.pow_succ, Nat.mul_mod, ih]

theorem pow_two_even {a : Nat} (ha : 0 < a) : 2 ^ a % 2 = 0 := by
  cases a with
  | zero => omega
  | succ a => simp [Nat.pow_succ]

theorem numerator_odd {a : Nat} {w : List Nat} (hp : Positive (a :: w)) :
    Numerator (a :: w) % 2 = 1 := by
  simp only [Positive] at hp
  simp [Numerator, Nat.add_mod, Nat.mul_mod, pow_two_even hp.1, pow_three_odd]

/-- An odd factor determines the exact power of two without importing a
valuation theory. -/
theorem two_power_odd_unique (a b u v : Nat)
    (hu : u % 2 = 1) (hv : v % 2 = 1)
    (h : 2 ^ a * u = 2 ^ b * v) : a = b ∧ u = v := by
  induction a generalizing b with
  | zero =>
      cases b with
      | zero => simpa using h
      | succ b =>
          have he : u % 2 = 0 := by
            have h' : u = 2 ^ (b + 1) * v := by simpa using h
            rw [h']
            simp [Nat.pow_succ, Nat.mul_mod]
          omega
  | succ a ih =>
      cases b with
      | zero =>
          have he : v % 2 = 0 := by
            have h' : v = 2 ^ (a + 1) * u := by simpa using h.symm
            rw [h']
            simp [Nat.pow_succ, Nat.mul_mod]
          omega
      | succ b =>
          have h' : 2 ^ a * u = 2 ^ b * v := by
            have hmul : 2 * (2 ^ a * u) = 2 * (2 ^ b * v) := by
              simpa [Nat.pow_succ, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h
            omega
          obtain ⟨hab, huv⟩ := ih b h'
          exact ⟨congrArg Nat.succ hab, huv⟩

/-- For positive exponents, length, total valuation and the integer offset
numerator determine the full word.  This is the injectivity needed when a
weighted residue sum is grouped by total valuation. -/
theorem word_determined_by_total_and_numerator
    (w v : List Nat) (hw : Positive w) (hv : Positive v)
    (hl : w.length = v.length)
    (ht : Total w = Total v)
    (hb : Numerator w = Numerator v) : w = v := by
  induction w generalizing v with
  | nil =>
      cases v with
      | nil => rfl
      | cons b v => simp at hl
  | cons a w ih =>
      cases v with
      | nil => simp at hl
      | cons b v =>
          have hlen : w.length = v.length := by simpa using hl
          cases w with
          | nil =>
              cases v with
              | nil =>
                  have hab : a = b := by simpa [Total] using ht
                  subst b
                  rfl
              | cons c v => simp at hlen
          | cons c w =>
              cases v with
              | nil => simp at hlen
              | cons d v =>
                  have hpw : Positive (c :: w) := hw.2
                  have hpv : Positive (d :: v) := hv.2
                  have hm : 2 ^ a * Numerator (c :: w) =
                      2 ^ b * Numerator (d :: v) := by
                    change 2 ^ a * Numerator (c :: w) + 3 ^ (c :: w).length =
                      2 ^ b * Numerator (d :: v) + 3 ^ (d :: v).length at hb
                    rw [hlen] at hb
                    exact Nat.add_right_cancel hb
                  obtain ⟨hab, hnum⟩ := two_power_odd_unique a b
                    (Numerator (c :: w)) (Numerator (d :: v))
                    (numerator_odd hpw) (numerator_odd hpv) hm
                  have htotal : Total (c :: w) = Total (d :: v) := by
                    simp only [Total] at ht ⊢
                    omega
                  have htail : c :: w = d :: v :=
                    ih (d :: v) hpw hpv hlen htotal hnum
                  subst b
                  rw [htail]

#print axioms word_determined_by_total_and_numerator
#print axioms linear_block_constants

end CollatzSelectedWords
