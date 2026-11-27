import Mathlib.Logic.Function.Iterate
import Mathlib.Analysis.Complex.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.Ring

/-! First-hit simplicity, source domination, and the finite complex occupation identity. -/

namespace CollisionOccupation

open Function
open scoped BigOperators

/-- A repeated state in a path shifts the final hit to an earlier time. -/
theorem firstHit_simple {X : Type*} (U : X → X) (x : X) (k : ℕ)
    (first : ∀ t < k, U^[t] x ≠ U^[k] x) {i j : ℕ}
    (hij : i < j) (hjk : j ≤ k) : U^[i] x ≠ U^[j] x := by
  intro eq
  have shifted := congrArg (U^[k-j]) eq
  rw [← iterate_add_apply, ← iterate_add_apply] at shifted
  have endIndex : k - j + j = k := by omega
  rw [endIndex] at shifted
  exact first (k-j+i) (by omega) shifted

/-- Dominate varying birth masses by a fixed source, before exchanging
    origin and suffix-clock sums. The test can already include survival. -/
theorem fixedSource_bound {X : Type*} (sites : Finset X) (horizon : ℕ)
    (birth visit : ℕ → X → ℝ) (cap : X → ℝ)
    (birth_le : ∀ t ∈ Finset.range horizon, ∀ x ∈ sites, birth t x ≤ cap x)
    (visit_nonneg : ∀ t ∈ Finset.range horizon, ∀ x ∈ sites, 0 ≤ visit t x) :
    (∑ t ∈ Finset.range horizon, ∑ x ∈ sites, birth t x * visit t x) ≤
    ∑ x ∈ sites, cap x * ∑ t ∈ Finset.range horizon, visit t x := by
  calc
    _ ≤ ∑ t ∈ Finset.range horizon, ∑ x ∈ sites, cap x * visit t x := by
      apply Finset.sum_le_sum
      intro t ht
      apply Finset.sum_le_sum
      intro x hx
      exact mul_le_mul_of_nonneg_right (birth_le t ht x hx) (visit_nonneg t ht x hx)
    _ = _ := by
      rw [Finset.sum_comm]
      simp_rw [Finset.mul_sum]

/-- Consecutive finite-period errors propagate with their sum under
    any contraction, including the joint endpoint/native-clock map. -/
theorem propagate_error {X : Type*} [PseudoMetricSpace X]
    (T : X → X) (contract : ∀ x y, dist (T x) (T y) ≤ dist x y)
    (p : ℕ → X) (err : ℕ → ℝ)
    (step : ∀ i, dist (p (i+1)) (T (p i)) ≤ err i) (j n : ℕ) :
    dist (p (j+n)) (T^[n] (p j)) ≤ ∑ i ∈ Finset.range n, err (j+i) := by
  induction n with
  | zero => simp
  | succ n hn =>
    rw [Finset.sum_range_succ, iterate_succ_apply']
    calc
      _ ≤ dist (p (j+n+1)) (T (p (j+n))) +
          dist (T (p (j+n))) (T (T^[n] (p j))) := dist_triangle _ _ _
      _ ≤ err (j+n) + ∑ i ∈ Finset.range n, err (j+i) :=
        add_le_add (step _) ((contract _ _).trans hn)
      _ = _ := add_comm _ _

/-- Averaging the source trit removes precisely the constant part of
    an exact marked fibre. No positivity or independence is needed. -/
theorem centered_trit (p₀ p₁ p₂ z₀ z₁ z₂ : ℝ) (hz : z₀ + z₁ + z₂ = 0) :
    z₀*p₀ + z₁*p₁ + z₂*p₂ =
    z₀*(p₀-(p₀+p₁+p₂)/3) + z₁*(p₁-(p₀+p₁+p₂)/3) +
    z₂*(p₂-(p₀+p₁+p₂)/3) := by
  linear_combination ((p₀+p₁+p₂)/3) * hz

/-- Multiplicative independence recovers both elapsed clocks from
    equality of corrected heights at a shared ordinary target. -/
theorem two_three_clocks {i j a b : ℕ}
    (h : 3^i * 2^b = 3^j * 2^a) : i = j ∧ a = b := by
  have f := congrArg Nat.factorization h
  simp only [Nat.factorization_mul (pow_ne_zero _ (by decide : (3 : ℕ) ≠ 0))
      (pow_ne_zero _ (by decide : (2 : ℕ) ≠ 0)), Nat.prime_three.factorization_pow,
      Nat.prime_two.factorization_pow] at f
  have h₃ := congrArg (fun z : ℕ →₀ ℕ => z 3) f
  have h₂ := congrArg (fun z : ℕ →₀ ℕ => z 2) f
  constructor
  · simpa using h₃
  · simpa using h₂.symm

/-- The gap-one edge exists on the actual ordinary residue in the
    minimum-height test. -/
theorem trit_two_parent (y : ℕ) (hOdd : y % 2 = 1) (hTrit : y % 3 = 2) :
    ∃ x : ℕ, 0 < x ∧ x % 2 = 1 ∧ 3*x+1 = 2*y := by
  refine ⟨(2*y-1)/3, ?_, ?_, ?_⟩ <;> omega

/-- A corrected-height minimizer in an inverse-closed positive
    component cannot occupy the source trit two. -/
theorem min_height_omits_two (C : Set ℕ) (P : ℕ → ℝ) (y : ℕ)
    (hy : y ∈ C) (hOdd : y % 2 = 1) (hPos : 0 < P y)
    (least : ∀ x ∈ C, P y ≤ P x)
    (pull : ∀ x : ℕ, 0 < x → x % 2 = 1 → 3*x+1 = 2*y →
      y ∈ C → x ∈ C ∧ 3 * P x = 2 * P y) : y % 3 ≠ 2 := by
  intro hTrit
  obtain ⟨x, hx, hxo, hxe⟩ := trit_two_parent y hOdd hTrit
  obtain ⟨hxC, hP⟩ := pull x hx hxo hxe hy
  exact (not_lt_of_ge (least x hxC)) (by linarith)

/-- A finite near-eigenfunction occupation sum has only boundary and
    one-step defect contributions. -/
theorem phase_telescope (z : ℕ → ℂ) (lam : ℂ) (n : ℕ) :
    (1 - lam) * ∑ i ∈ Finset.range n, z i =
    z 0 - z n + ∑ i ∈ Finset.range n, (z (i+1) - lam * z i) := by
  induction n with
  | zero => simp
  | succ n hn =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ, mul_add, hn]
    ring

/-- The defect cost can be bounded after retaining its magnitude at
    each actual state. -/
theorem phase_bound (z : ℕ → ℂ) (lam : ℂ) (n : ℕ) :
    ‖1 - lam‖ * ‖∑ i ∈ Finset.range n, z i‖ ≤
    ‖z 0‖ + ‖z n‖ + ∑ i ∈ Finset.range n, ‖z (i+1) - lam * z i‖ := by
  rw [← norm_mul, phase_telescope]
  calc
    _ ≤ ‖z 0 - z n‖ + ‖∑ i ∈ Finset.range n, (z (i+1) - lam * z i)‖ := norm_add_le _ _
    _ ≤ _ := add_le_add (norm_sub_le _ _) (norm_sum_le _ _)

#print axioms firstHit_simple
#print axioms fixedSource_bound
#print axioms propagate_error
#print axioms centered_trit
#print axioms two_three_clocks
#print axioms trit_two_parent
#print axioms min_height_omits_two
#print axioms phase_telescope
#print axioms phase_bound

end CollisionOccupation
