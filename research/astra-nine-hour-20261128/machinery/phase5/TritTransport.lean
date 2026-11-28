import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Rat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace AstraNine.TritTransport

/-- Increasing an inverse exponent by two replaces the child by four times
the former child plus one. -/
theorem add_two_to_gap (parent child gap : ℕ)
    (legal : 2 ^ gap * parent = 3 * child + 1) :
    2 ^ (gap + 2) * parent = 3 * (4 * child + 1) + 1 := by
  calc
    2 ^ (gap + 2) * parent = 4 * (2 ^ gap * parent) := by rw [pow_add]; ring
    _ = 3 * (4 * child + 1) + 1 := by rw [legal]; ring

/-- The three possible final exponent repairs can prescribe any trit. -/
theorem cycle_trits (child trit : ℕ) (h : trit < 3) :
    child % 3 = trit ∨ (4 * child + 1) % 3 = trit ∨
    (4 * (4 * child + 1) + 1) % 3 = trit := by
  have step (x : ℕ) : (4 * x + 1) % 3 = (x % 3 + 1) % 3 := by
    rw [Nat.add_mod, Nat.mul_mod]
    simp
  rw [step (4 * child + 1), step child]
  have cases : child % 3 = 0 ∨ child % 3 = 1 ∨ child % 3 = 2 := by omega
  rcases cases with he | he | he <;> rw [he] <;> omega

/-- Averaging a feasible Bellman inequality on a joint law compares its
slope with the exact discrepancy from replacing the true last lift. Both
endpoint observables in this statement are sampled under the same law. -/
theorem average_dual {ι : Type*} [Fintype ι] (weight source actual uniform cost : ι → ℚ)
    (slope : ℚ) (nonneg : ∀ i, 0 ≤ weight i) (unitSum : ∑ i, weight i = 1)
    (dual : ∀ i, slope + source i ≤ cost i + uniform i)
    (stationary : ∑ i, weight i * source i = ∑ i, weight i * actual i) :
    slope - ∑ i, weight i * cost i ≤ ∑ i, weight i * (uniform i - actual i) := by
  have scaled : ∑ i, weight i * (slope + source i) ≤ ∑ i, weight i * (cost i + uniform i) :=
    Finset.sum_le_sum (fun i _ => mul_le_mul_of_nonneg_left (dual i) (nonneg i))
  simp only [mul_add, Finset.sum_add_distrib, ← Finset.sum_mul, unitSum, one_mul,
    stationary] at scaled
  simp only [mul_sub, Finset.sum_sub_distrib]
  linarith

/-- Two currents on a directed interval with the same injection-minus-
removal increments differ by the same constant at every cut. -/
theorem current_difference (one two : ℕ → ℚ)
    (balance : ∀ k, one (k + 1) - one k = two (k + 1) - two k) (n : ℕ) :
    one n - two n = one 0 - two 0 := by
  induction n with
  | zero => rfl
  | succ n ih => linarith [balance n]

/-- Once a mandatory-first-edge current is tight on one cut, every other
feasible current of the same balance has at least the total transport cost. -/
theorem least_current {ι : Type*} [Fintype ι] (imbalance initial : ι → ℚ)
    (candidate other : ℚ) (tight : ∃ i, imbalance i + candidate = initial i)
    (feasible : ∀ i, initial i ≤ imbalance i + other) :
    ∑ i, (imbalance i + candidate) ≤ ∑ i, (imbalance i + other) := by
  obtain ⟨i, hi⟩ := tight
  have h : candidate ≤ other := by linarith [feasible i]
  exact Finset.sum_le_sum (fun j _ => add_le_add_right h (imbalance j))

end AstraNine.TritTransport
