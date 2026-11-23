import Mathlib.Tactic

/-!
An exact bounded *forced* real itinerary. Its branches are selected by
an interval test, not by the parity of a rational 2-adic integer.
This module does not construct a Collatz orbit or counterexample.
-/

namespace CollatzRealAdicControl

def denominator (k : ℕ) : ℤ := 2 ^ (k + 1)

def numerator : ℕ → ℤ
  | 0 => 3
  | k + 1 => if 2 * denominator k ≤ numerator k then numerator k
    else 3 * numerator k - denominator k

def digit (k : ℕ) : ℕ :=
  if 2 * denominator k ≤ numerator k then 0 else 1

def ones : ℕ → ℕ
  | 0 => 0
  | k + 1 => ones k + digit k

def carry : ℕ → ℤ
  | 0 => 0
  | k + 1 => if 2 * denominator k ≤ numerator k then carry k
    else 3 * carry k + 2 ^ k

theorem denominator_pos (k : ℕ) : 0 < denominator k := by
  exact pow_pos (by norm_num) _

theorem denominator_succ (k : ℕ) :
    denominator (k + 1) = 2 * denominator k := by
  simp only [denominator, pow_succ]
  ring

theorem denominator_even (k : ℕ) : denominator k % 2 = 0 := by
  simp [denominator, pow_succ]

/-- The forced states stay in [1,5/2] and have an odd numerator. -/
theorem bounded_odd (k : ℕ) :
    denominator k ≤ numerator k ∧
    2 * numerator k ≤ 5 * denominator k ∧ numerator k % 2 = 1 := by
  induction k with
  | zero => norm_num [denominator, numerator]
  | succ k ih =>
    have hd := denominator_pos k
    have he := denominator_even k
    rw [denominator_succ, numerator]
    split_ifs with h
    · omega
    · omega

theorem digit_zero_one (k : ℕ) : digit k = 0 ∨ digit k = 1 := by
  unfold digit
  split_ifs <;> simp

/-- Every zero branch is followed by a one branch. -/
theorem no_two_zeroes (k : ℕ) (h : digit k = 0) : digit (k + 1) = 1 := by
  have hg : 2 * denominator k ≤ numerator k := by
    simpa [digit] using h
  have hb := bounded_odd k
  have hd := denominator_pos k
  have hn : numerator (k + 1) = numerator k := by simp [numerator, hg]
  have hnext : ¬ 2 * denominator (k + 1) ≤ numerator (k + 1) := by
    rw [denominator_succ, hn]
    omega
  simp [digit, hnext]

/-- Exact finite Bernstein carry identity, with initial real state -3/2. -/
theorem finite_bernstein (k : ℕ) :
    numerator k + 2 * carry k = 3 * (3 : ℤ) ^ ones k := by
  induction k with
  | zero => norm_num [numerator, carry, ones]
  | succ k ih =>
    by_cases hg : 2 * denominator k ≤ numerator k
    · simpa [numerator, carry, ones, digit, hg] using ih
    · simp only [numerator, carry, ones, digit, ite_eq_right hg, pow_succ]
      have hd : denominator k = 2 * (2 : ℤ) ^ k := by
        simp [denominator, pow_succ, mul_comm]
      rw [hd]
      nlinarith

/-- The residual decays geometrically in the number of one branches. -/
theorem residual_bound (k : ℕ) :
    numerator k * (2 : ℤ) ^ ones k ≤ 3 * (5 : ℤ) ^ ones k := by
  induction k with
  | zero => norm_num [numerator, ones]
  | succ k ih =>
    by_cases hg : 2 * denominator k ≤ numerator k
    · simpa [numerator, ones, digit, hg] using ih
    · simp only [numerator, ones, digit, ite_eq_right hg, pow_succ]
      have hp : 0 ≤ (2 : ℤ) ^ ones k := le_of_lt (pow_pos (by norm_num) _)
      have hstep : 2 * (3 * numerator k - denominator k) ≤ 5 * numerator k := by
        omega
      have hmul := mul_le_mul_of_nonneg_right hstep hp
      nlinarith

end CollatzRealAdicControl
