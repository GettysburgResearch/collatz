import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Ring

/-!
The finite positive occupation decomposition on the actual odd Collatz map.
The source and endpoint in every released term are the same as in the input.
No density or asymptotic assertion is formalized here.
-/

namespace Collatz.Diagonal.CompensatedOccupation

def oddStep (x : ℕ) : ℕ := ordCompl[2] (3 * x + 1)
def edge (x : ℕ) : ℚ := 3 * (x : ℚ) / (3 * (x : ℚ) + 1)

def survival : ℕ → ℕ → ℚ
  | 0, _ => 1
  | n + 1, x => survival n x * edge (oddStep^[n] x)

/-- Each complementary edge weight is released once along the true path. -/
theorem released_sum (n x : ℕ) :
    ∑ i ∈ Finset.range n, survival i x * (1 - edge (oddStep^[i] x)) =
      1 - survival n x := by
  induction n with
  | zero => simp [survival]
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    simp only [survival]
    ring

/-- Subsequent iterations preserve the original terminal site. -/
theorem retained_endpoint {i n : ℕ} (hi : i ≤ n) (x : ℕ) :
    oddStep^[n - i] (oddStep^[i] x) = oddStep^[n] x := by
  rw [← Function.iterate_add_apply, Nat.sub_add_cancel hi]

/-- Duhamel's identity on any supplied finite set of ordinary sources. -/
theorem finite_occupation (n : ℕ) (sources : Finset ℕ)
    (sourceWeight test : ℕ → ℚ) :
    ∑ x ∈ sources, sourceWeight x * test (oddStep^[n] x) =
      (∑ x ∈ sources, sourceWeight x * survival n x * test (oddStep^[n] x)) +
      ∑ i ∈ Finset.range n, ∑ x ∈ sources,
        (sourceWeight x * (survival i x * (1 - edge (oddStep^[i] x)))) *
          test (oddStep^[n-i] (oddStep^[i] x)) := by
  rw [Finset.sum_comm (s := Finset.range n) (t := sources)]
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  have inner :
      (∑ i ∈ Finset.range n,
        sourceWeight x * (survival i x * (1 - edge (oddStep^[i] x))) *
          test (oddStep^[n-i] (oddStep^[i] x))) =
      sourceWeight x * (1 - survival n x) * test (oddStep^[n] x) := by
    rw [← released_sum n x, Finset.mul_sum, Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro i hi
    rw [retained_endpoint (Nat.le_of_lt (Finset.mem_range.mp hi))]
  rw [inner]
  ring

end Collatz.Diagonal.CompensatedOccupation
