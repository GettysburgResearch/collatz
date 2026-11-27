import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! A finite consumer for a reusable positive clock-error envelope.

The ordinary synchronization and cut estimates are separate written inputs.
Here the clock is translated so that index zero is below every observed
support. The same error row is used at every transport time. -/
set_option autoImplicit false
set_option warningAsError true

namespace ClockEnvelope
open scoped BigOperators

theorem telescope (p : ℕ → ℕ → ℝ) (error : ℕ → ℝ)
    (zero : ∀ j, p j 0 = 0)
    (step : ∀ j k, p j (k+1) ≤ p (j+1) k + error k)
    (j k : ℕ) :
    p j k ≤ ∑ i ∈ Finset.range k, error i := by
  induction k generalizing j with
  | zero => simp [zero j]
  | succ k ih =>
    calc
      p j (k+1) ≤ p (j+1) k + error k := step j k
      _ ≤ (∑ i ∈ Finset.range k, error i) + error k :=
        add_le_add (ih (j+1)) le_rfl
      _ = ∑ i ∈ Finset.range (k+1), error i := by
        rw [Finset.sum_range_succ]

theorem atom_bound (p : ℕ → ℕ → ℝ) (error : ℕ → ℝ)
    (zero : ∀ j, p j 0 = 0)
    (step : ∀ j k, p j (k+1) ≤ p (j+1) k + error k)
    (nonneg : ∀ i, 0 ≤ error i) {k N : ℕ} (cap : k ≤ N) :
    p 0 k ≤ ∑ i ∈ Finset.range N, error i := by
  apply (telescope p error zero step 0 k).trans
  exact Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_mono cap)
    (by intro i _ _; exact nonneg i)

/-- Choose the clock separately in every component, before summing.
No lower bound on any component's mass is used. -/
theorem component_atoms {C : Type*} (S : Finset C)
    (p : C → ℕ → ℕ → ℝ) (error : C → ℕ → ℝ)
    (zero : ∀ c j, p c j 0 = 0)
    (step : ∀ c j k, p c j (k+1) ≤ p c (j+1) k + error c k)
    (nonneg : ∀ c i, 0 ≤ error c i)
    (clock : C → ℕ) (N : ℕ) (cap : ∀ c ∈ S, clock c ≤ N) :
    (∑ c ∈ S, p c 0 (clock c)) ≤
      ∑ c ∈ S, ∑ i ∈ Finset.range N, error c i := by
  apply Finset.sum_le_sum
  intro c hc
  exact atom_bound (p c) (error c) (zero c) (step c) (nonneg c) (cap c hc)

/-- An arbitrary set of at most w clocks in each component obeys the
same bound, with the factor w. The selected sets need not be intervals. -/
theorem component_windows {C : Type*} (S : Finset C)
    (p : C → ℕ → ℕ → ℝ) (error : C → ℕ → ℝ)
    (zero : ∀ c j, p c j 0 = 0)
    (step : ∀ c j k, p c j (k+1) ≤ p c (j+1) k + error c k)
    (nonneg : ∀ c i, 0 ≤ error c i)
    (clocks : C → Finset ℕ) (N w : ℕ)
    (cap : ∀ c ∈ S, ∀ k ∈ clocks c, k ≤ N)
    (width : ∀ c ∈ S, (clocks c).card ≤ w) :
    (∑ c ∈ S, ∑ k ∈ clocks c, p c 0 k) ≤
      (w:ℝ) * ∑ c ∈ S, ∑ i ∈ Finset.range N, error c i := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro c hc
  let mass : ℝ := ∑ i ∈ Finset.range N, error c i
  have mass_nonneg : 0 ≤ mass := Finset.sum_nonneg (by intro i _; exact nonneg c i)
  calc
    (∑ k ∈ clocks c, p c 0 k) ≤ ∑ _k ∈ clocks c, mass := by
      apply Finset.sum_le_sum
      intro k hk
      exact atom_bound (p c) (error c) (zero c) (step c) (nonneg c) (cap c hc k hk)
    _ = ((clocks c).card:ℝ) * mass := by simp [nsmul_eq_mul]
    _ ≤ (w:ℝ) * mass := mul_le_mul_of_nonneg_right (Nat.cast_le.mpr (width c hc)) mass_nonneg

#print axioms telescope
#print axioms component_atoms
#print axioms component_windows
end ClockEnvelope
