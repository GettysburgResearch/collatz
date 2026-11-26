import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Ring

namespace Collatz.GateDyadicMoment

open Finset

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def state : ℕ → ℕ → ℕ
  | 0, x => x
  | j + 1, x => shortcut (state j x)

def oddCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | j + 1, x => oddCount j x + state j x % 2

theorem shortcut_twice (x : ℕ) :
    2 * shortcut x = if x % 2 = 0 then x else 3 * x + 1 := by
  unfold shortcut
  split <;> omega

theorem shortcut_translate (x d : ℕ) :
    shortcut (x + 2*d) = shortcut x + 3^(x%2)*d := by
  have ht : (x+2*d)%2 = x%2 := by omega
  rw [shortcut, ht, shortcut]
  by_cases h : x%2 = 0
  · simp [h]
    omega
  · have ho : x%2 = 1 := by omega
    simp [ho]
    omega

/-- Translation by a full dyadic residue period has an ordinary affine effect
at the terminal and preserves all odd counts of that clock. -/
theorem full_period (j x d : ℕ) :
    oddCount j (x + 2^j*d) = oddCount j x ∧
    state j (x + 2^j*d) = state j x + 3^(oddCount j x)*d := by
  induction j generalizing x d with
  | zero => simp [oddCount, state]
  | succ j ih =>
    have he : x + 2^(j+1)*d = x+2^j*(2*d) := by ring
    obtain ⟨hc,hs⟩ := ih x (2*d)
    rw [he]
    have hp : (state j x+3^(oddCount j x)*(2*d))%2 = state j x % 2 := by
      rw [show 3^(oddCount j x)*(2*d) = 2*(3^(oddCount j x)*d) by ring]
      omega
    constructor
    · simp only [oddCount, hc, hs, hp]
    · simp only [state, hs, oddCount, pow_add]
      rw [show 3^(oddCount j x)*(2*d) = 2*(3^(oddCount j x)*d) by ring,
          shortcut_translate]
      ring

/-- Every pair of opposite dyadic lifts has complementary last parity. -/
theorem complementary_last (j x : ℕ) :
    state j x % 2 + state j (x+2^j) % 2 = 1 := by
  have hs := (full_period j x 1).2
  simp only [Nat.mul_one] at hs
  have ho : 3^(oddCount j x)%2 = 1 := by simp [Nat.pow_mod]
  rw [hs, Nat.add_mod, ho]
  omega

/-- A complete dyadic period has exactly the fair-binomial odd-count polynomial.
The coefficient identity is valid over an arbitrary commutative semiring. -/
theorem moment_period {R : Type*} [CommSemiring R] (j : ℕ) (z : R) :
    ∑ x ∈ range (2^j), z^(oddCount j x) = (1+z)^j := by
  induction j with
  | zero => simp [oddCount]
  | succ j ih =>
    rw [show (2:ℕ)^(j+1) = 2^j+2^j by ring, Finset.sum_range_add,
        ← Finset.sum_add_distrib]
    have hp (x : ℕ) :
        z^oddCount (j+1) x + z^oddCount (j+1) (2^j+x) =
          z^oddCount j x * (1+z) := by
      have hc := (full_period j x 1).1
      simp only [Nat.mul_one] at hc
      rw [Nat.add_comm (2^j) x]
      simp only [oddCount, pow_add, hc]
      have h := complementary_last j x
      by_cases he : state j x % 2 = 0
      · have ho : state j (x+2^j)%2 = 1 := by omega
        simp [he, ho, mul_add]
      · have ho : state j x%2 = 1 := by omega
        have he' : state j (x+2^j)%2 = 0 := by omega
        simp [ho, he', mul_add, add_comm]
    simp_rw [hp]
    rw [← Finset.sum_mul, ih, pow_succ]

/-- The source shell [2^j,2^(j+1)) obeys precisely the same identity. -/
theorem moment_shell {R : Type*} [CommSemiring R] (j : ℕ) (z : R) :
    ∑ x ∈ range (2^j), z^(oddCount j (2^j+x)) = (1+z)^j := by
  rw [← moment_period j z]
  apply Finset.sum_congr rfl
  intro x _
  have h := (full_period j x 1).1
  simp only [Nat.mul_one] at h
  rw [Nat.add_comm (2^j) x, h]

/-- In the physical affine word the normalized real intercept is at most
(3/2)^j-1. This form uses only natural arithmetic. -/
theorem affine_carry_bound (j x : ℕ) :
    2^j * state j x + 2^j ≤ 3^(oddCount j x)*x + 3^j := by
  induction j with
  | zero => simp [state, oddCount]
  | succ j ih =>
    simp only [state, oddCount, pow_add (3:ℕ) (oddCount j x), pow_succ (2:ℕ) j, pow_succ (3:ℕ) j]
    rw [Nat.mul_assoc (2^j) 2, shortcut_twice]
    by_cases he : state j x % 2 = 0
    · simp only [he, ite_true, pow_zero, Nat.mul_one]
      have hb : (2:ℕ)^j ≤ 3^j := Nat.pow_le_pow_left (by decide) j
      omega
    · have ho : state j x % 2 = 1 := by omega
      simp only [ho, Nat.one_ne_zero, ite_false, pow_one]
      have ht : 2^j*(3*state j x+1)+2^j*2 = 3*(2^j*state j x+2^j) := by ring
      rw [ht]
      calc
        _ ≤ 3*(3^(oddCount j x)*x+3^j) := Nat.mul_le_mul_left 3 ih
        _ = _ := by ring

end Collatz.GateDyadicMoment

#print axioms Collatz.GateDyadicMoment.shortcut_twice
#print axioms Collatz.GateDyadicMoment.shortcut_translate
#print axioms Collatz.GateDyadicMoment.full_period
#print axioms Collatz.GateDyadicMoment.complementary_last
#print axioms Collatz.GateDyadicMoment.moment_period
#print axioms Collatz.GateDyadicMoment.moment_shell
#print axioms Collatz.GateDyadicMoment.affine_carry_bound
