import MinimumWindow
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Order.Interval.Finset.Nat

/-! Exact ordinary-source population identity underlying the native size walk.
This file contains no probability or asymptotic mixing assertion. -/

namespace Collatz.NativeSizeRecursion

open Finset Collatz.MinimumWindow

theorem odd_image {n : ℕ} (hn : n % 2 = 1) :
    0 < step n ∧ step n % 3 = 2 ∧ 2 * step n = 3 * n + 1 := by
  have hne : ¬ n % 2 = 0 := by omega
  simp only [step, ite_eq_right hne]
  omega

theorem odd_preimage {y : ℕ} (hy : y % 3 = 2) :
    0 < (2*y-1)/3 ∧ ((2*y-1)/3) % 2 = 1 ∧ step ((2*y-1)/3) = y := by
  have hn : ((2*y-1)/3) % 2 = 1 := by omega
  have hne : ¬ ((2*y-1)/3) % 2 = 0 := by omega
  simp only [step, ite_eq_right hne]
  omega

theorem even_population (N t : ℕ) (f : ℕ → ℕ → ℤ) :
    (∑ n ∈ (Icc 1 N).filter (fun n => n % 2 = 0),
       f (count oddMark (t+1) n) (orbit (t+1) n)) =
    ∑ m ∈ Icc 1 (N/2), f (count oddMark t m) (orbit t m) := by
  apply sum_bij (fun n _ => n/2)
  · intro n hn
    simp only [mem_filter, mem_Icc] at hn ⊢
    omega
  · intro n hn n' hn' h
    simp only [mem_filter, mem_Icc] at hn hn'
    omega
  · intro m hm
    simp only [mem_Icc] at hm
    refine ⟨2*m, ?_, ?_⟩
    · simp only [mem_filter, mem_Icc]
      omega
    · omega
  · intro n hn
    have he : n % 2 = 0 := (mem_filter.mp hn).2
    simp [count, oddMark, orbit, step, he]

theorem odd_population (N t : ℕ) (f : ℕ → ℕ → ℤ) :
    (∑ n ∈ (Icc 1 N).filter (fun n => ¬ n % 2 = 0),
       f (count oddMark (t+1) n) (orbit (t+1) n)) =
    ∑ y ∈ (Icc 1 ((3*N+1)/2)).filter (fun y => y % 3 = 2),
       f (1 + count oddMark t y) (orbit t y) := by
  apply sum_bij (fun n _ => (3*n+1)/2)
  · intro n hn
    simp only [mem_filter, mem_Icc] at hn ⊢
    omega
  · intro n hn n' hn' h
    simp only [mem_filter, mem_Icc] at hn hn'
    omega
  · intro y hy
    simp only [mem_filter, mem_Icc] at hy
    refine ⟨(2*y-1)/3, ?_, ?_⟩
    · simp only [mem_filter, mem_Icc]
      omega
    · omega
  · intro n hn
    have he : ¬ n % 2 = 0 := (mem_filter.mp hn).2
    have ho : n % 2 = 1 := by omega
    simp [count, oddMark, orbit, step, ho]

/-- Every bounded integer-valued test of the true native count and endpoint
obeys this exact source split. The population cutoffs and ternary class
are explicit; replacing the ternary class by its mean is a separate input. -/
theorem population_recursion (N t : ℕ) (f : ℕ → ℕ → ℤ) :
    (∑ n ∈ Icc 1 N, f (count oddMark (t+1) n) (orbit (t+1) n)) =
      (∑ m ∈ Icc 1 (N/2), f (count oddMark t m) (orbit t m)) +
      ∑ y ∈ (Icc 1 ((3*N+1)/2)).filter (fun y => y % 3 = 2),
        f (1 + count oddMark t y) (orbit t y) := by
  rw [← sum_filter_add_sum_filter_not (Icc 1 N) (fun n => n % 2 = 0)]
  rw [even_population, odd_population]

#print axioms odd_image
#print axioms odd_preimage
#print axioms population_recursion

end Collatz.NativeSizeRecursion
