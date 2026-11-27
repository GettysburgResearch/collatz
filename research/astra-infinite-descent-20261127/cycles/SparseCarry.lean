import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-! Literal shortcut words, telescoped odd runs and two independent edits. -/

namespace Collatz.InfiniteDescent.SparseCarry

def bit (b : Bool) : ℕ := if b then 1 else 0

def ones (w : List Bool) : ℕ := (w.map bit).sum

def carry : List Bool → ℤ
  | [] => 0
  | b :: w => 3 ^ ones w * (bit b : ℤ) + 2 * carry w

@[simp] theorem ones_cons (b : Bool) (w : List Bool) :
    ones (b :: w) = bit b + ones w := by simp [ones]

@[simp] theorem ones_append (u v : List Bool) :
    ones (u ++ v) = ones u + ones v := by simp [ones]

theorem carry_append (u v : List Bool) :
    carry (u ++ v) = 3 ^ ones v * carry u + 2 ^ u.length * carry v := by
  induction u with
  | nil => simp [carry]
  | cons b w ih =>
    simp only [List.cons_append, carry, ones_append, pow_add, ih, List.length_cons, pow_succ]
    ring

@[simp] theorem ones_true (a : ℕ) : ones (List.replicate a true) = a := by
  induction a with
  | zero => rfl
  | succ a ih => simp [List.replicate_succ, ih, bit, Nat.add_comm]

@[simp] theorem ones_false (a : ℕ) : ones (List.replicate a false) = 0 := by
  induction a with
  | zero => rfl
  | succ a ih => simp [List.replicate_succ, ih, bit]

theorem carry_true (a : ℕ) : carry (List.replicate a true) = 3 ^ a - 2 ^ a := by
  induction a with
  | zero => simp [carry]
  | succ a ih => simp [List.replicate_succ, carry, ih, bit, pow_succ]; ring

@[simp] theorem carry_false (a : ℕ) : carry (List.replicate a false) = 0 := by
  induction a with
  | zero => rfl
  | succ a ih => simp [List.replicate_succ, carry, ih, bit]

abbrev Runs := List (ℕ × ℕ)

def word : Runs → List Bool
  | [] => []
  | (a,b) :: tail => List.replicate a true ++ List.replicate b false ++ word tail

/-- One positive and one negative endpoint for each odd run, including empty test runs. -/
def boundarySum (date : ℕ) : Runs → ℤ
  | [] => 0
  | (a,b) :: tail => 2 ^ date * 3 ^ (a + ones (word tail))
        - 2 ^ (date+a) * 3 ^ ones (word tail) + boundarySum (date+a+b) tail

theorem literal_run_sum (r : Runs) (date : ℕ) :
    boundarySum date r = 2 ^ date * carry (word r) := by
  induction r generalizing date with
  | nil => simp [boundarySum, word, carry]
  | cons pair tail ih =>
    rcases pair with ⟨a,b⟩
    simp only [boundarySum, word, ih, carry_append, ones_false,
      carry_false, carry_true, List.length_append, List.length_replicate, pow_add]
    ring

/-- Reversing a mixed pair preserves its grade. -/
def pair (orientation : Bool) : List Bool := [orientation, !orientation]

@[simp] theorem pair_length (b : Bool) : (pair b).length = 2 := by cases b <;> rfl
@[simp] theorem pair_grade (b : Bool) : ones (pair b) = 1 := by cases b <;> rfl

def sign (orientation : Bool) : ℤ := if orientation then 1 else -1

theorem pair_change (b : Bool) : carry (pair (!b)) - carry (pair b) = sign b := by
  cases b <;> rfl

/-- The two edits may have any intervening word or exterior context. The second
bracket retains the exact principal integer whose common factors can cancel. -/
theorem two_swap_difference (u m v : List Bool) (b c : Bool) :
    carry (u ++ pair (!b) ++ m ++ pair (!c) ++ v)
      - carry (u ++ pair b ++ m ++ pair c ++ v)
    = 2 ^ u.length * 3 ^ ones v *
      (sign b * 3 ^ (ones m + 1) + sign c * 2 ^ (m.length + 2)) := by
  have hb := pair_change b
  have hc := pair_change c
  simp only [carry_append, pair_grade, List.length_append, pair_length, pow_add]
  linear_combination
    (2 ^ u.length * 3 ^ ones v * 3 ^ ones m * 3) * hb +
    (2 ^ u.length * 3 ^ ones v * 2 ^ m.length * 4) * hc

/-- Every simultaneous denominator-clearing multiple of the two words must
clear their sparse difference. If the old numerator is integral at D, this
is an equivalence for every integer multiple, including all prime powers. -/
theorem clearing_edit_iff {D original edited unit stamp : ℤ}
    (h : edited - original = unit * stamp) (cop : IsCoprime D unit)
    (originalIntegral : D ∣ original) (t : ℤ) :
    D ∣ t * edited ↔ D ∣ t * stamp := by
  have horig : D ∣ t * original := dvd_mul_of_dvd_right originalIntegral t
  have ident : t * edited - t * original = unit * (t * stamp) := by
    rw [← mul_sub, h]; ring
  constructor
  · intro he
    exact cop.dvd_of_dvd_mul_left (ident ▸ dvd_sub he horig)
  · intro hs
    rw [← sub_add_cancel (t * edited) (t * original), ident]
    exact dvd_add (dvd_mul_of_dvd_right hs unit) horig

#print axioms literal_run_sum
#print axioms two_swap_difference
#print axioms clearing_edit_iff

end Collatz.InfiniteDescent.SparseCarry
