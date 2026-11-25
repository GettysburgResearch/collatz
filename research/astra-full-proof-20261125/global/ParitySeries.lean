import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Exact identities for the finite prefixes of the weighted parity series.
    The two-place lifting argument for its infinite series is in README.md. -/
namespace Collatz.WeightedParity

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def bit (x : Nat) : Nat := x % 2

def weight (x : Nat) : Nat := if x % 2 = 0 then 3 else 1

def trajectory (x : Nat) : Nat → Nat
  | 0 => x
  | n + 1 => trajectory (step x) n

def evens (x : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => (if x % 2 = 0 then 1 else 0) + evens (step x) n

def sectionSum (x : Nat) : Nat → ℚ → ℚ
  | 0, _ => 0
  | n + 1, z => bit x + weight x * z * sectionSum (step x) n z

theorem one_clock (x : Nat) :
    3 * (x : ℚ) + bit x = 2 * weight x * step x := by
  have h : 3 * x + bit x = 2 * weight x * step x := by
    by_cases even : x % 2 = 0
    · simp [step, weight, bit, even]
      omega
    · simp [step, weight, bit, even]
      omega
  exact_mod_cast h

theorem prefix_value (x n : Nat) :
    3 * (x : ℚ) + sectionSum x n (2 / 3) =
      3 * (2 / 3 : ℚ) ^ n * 3 ^ evens x n * trajectory x n := by
  induction n generalizing x with
  | zero => simp [sectionSum, trajectory, evens]
  | succ n ih =>
    have hw : (weight x : ℚ) =
        (3 : ℚ) ^ (if x % 2 = 0 then 1 else 0 : Nat) := by
      by_cases he : x % 2 = 0 <;> simp [weight, he]
    calc
      _ = (weight x * (2 / 3 : ℚ)) *
          (3 * step x + sectionSum (step x) n (2 / 3)) := by
            rw [sectionSum]
            rw [← add_assoc, one_clock x]
            ring
      _ = _ := by
            rw [ih, hw]
            simp only [evens, trajectory, pow_add, pow_succ]
            ring

/-- The coefficients in chronological order, prior to specialization. -/
def coeff (x i : Nat) : Nat := bit (trajectory x i) * 3 ^ evens x i

theorem prefix_append_clock (x n : Nat) (z : ℚ) :
    sectionSum x (n + 1) z = sectionSum x n z + (coeff x n : ℚ) * z ^ n := by
  induction n generalizing x with
  | zero => simp [sectionSum, coeff, trajectory, evens]
  | succ n ih =>
    have hw : (weight x : ℚ) =
        (3 : ℚ) ^ (if x % 2 = 0 then 1 else 0 : Nat) := by
      by_cases he : x % 2 = 0 <;> simp [weight, he]
    change bit x + weight x * z * sectionSum (step x) (n+1) z =
      (bit x + weight x * z * sectionSum (step x) n z) + (coeff x (n+1) : ℚ) * z^(n+1)
    simp only [ih (step x), coeff, evens, trajectory, Nat.cast_mul,
      Nat.cast_pow, Nat.cast_ofNat, pow_add, pow_succ, hw]
    ring

#print axioms one_clock
#print axioms prefix_value
#print axioms prefix_append_clock
end Collatz.WeightedParity
