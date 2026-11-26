import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
Finite Green identities for the simple symmetric jump chain in the Collatz
slope-level excursion. A path stops contributing at its first visit to zero.
Counts at depth t retain denominator 2^t, also when the path has been killed.
The ordinary physical waiting-time comparison is in the accompanying proof.
-/
namespace CollatzSlopeOccupation

/-- Potential for occupation of one level in a killed nearest-neighbor walk. -/
def green (s j : Nat) : Nat := 2 * min s j

/-- Total visits at the start of any of the first t jumps, with multiplicity
over all binary words of length t, excluding all times at or after killing. -/
def visits : Nat → Nat → Nat → Nat
  | 0, _, _ => 0
  | _ + 1, 0, _ => 0
  | t + 1, s + 1, j =>
    (if s + 1 = j then 2^(t+1) else 0) + visits t s j + visits t (s+2) j

/-- Total residual potential at the ends of the depth-t words. -/
def remainder : Nat → Nat → Nat → Nat
  | 0, s, j => green s j
  | _ + 1, 0, _ => 0
  | t + 1, s + 1, j => remainder t s j + remainder t (s+2) j

theorem green_step (s j : Nat) :
    green s j + green (s+2) j + (if s+1=j then 2 else 0) =
      2 * green (s+1) j := by
  unfold green
  split <;> omega

/-- Each binary node accounts for its immediate reward and both child
potentials. The exact identity leaves the finite-horizon residual visible. -/
theorem visits_add_remainder (t s j : Nat) :
    visits t s j + remainder t s j = 2^t * green s j := by
  induction t generalizing s with
  | zero => simp [visits, remainder]
  | succ t ih =>
    cases s with
    | zero => simp [visits, remainder, green]
    | succ s =>
      simp only [visits, remainder]
      have h := congrArg (fun a : Nat => 2^t * a) (green_step s j)
      have h₁ := ih s
      have h₂ := ih (s+2)
      by_cases he : s+1=j
      · simp only [he, ite_true, Nat.mul_add] at h ⊢
        rw [pow_succ]
        linear_combination (norm := ring_nf) h + h₁ + h₂
      · simp only [he, ite_false, add_zero, zero_add, Nat.mul_add] at h ⊢
        rw [pow_succ]
        linear_combination (norm := ring_nf) h + h₁ + h₂

/-- The unnormalized occupation of a band with arbitrary nonnegative
holding-cost bounds at the individual levels. -/
theorem weighted_band_visits_le (t s K : Nat) (cost : Nat → Nat) :
    (∑ j ∈ Finset.range (K+1), visits t s j * cost j) ≤
      2^t * ∑ j ∈ Finset.range (K+1), green s j * cost j := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro j _
  rw [← Nat.mul_assoc]
  exact Nat.mul_le_mul_right _ (Nat.le.intro (visits_add_remainder t s j))

end CollatzSlopeOccupation
