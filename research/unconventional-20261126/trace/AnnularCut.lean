import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise

open Finset

namespace Collatz.AnnularCut

def shortcut (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- For a cutoff X, the entire incoming preimage lies in [0,2X]. -/
theorem preimage_bound {n X : ℕ} (h : shortcut n ≤ X) : n ≤ 2 * X := by
  unfold shortcut at h
  split at h <;> omega

variable {G : Type*} [AddCommGroup G]

def edge (X n : ℕ) (a : G) : G :=
  (if n ≤ X then a else 0) - (if shortcut n ≤ X then a else 0)

/-- The two signed intervals use exact integer endpoints and include all small cutoffs. -/
theorem edge_annular (X n : ℕ) (a : G) :
    edge X n a =
      (if n % 2 = 1 ∧ n ≤ X ∧ 2 * X < 3 * n + 1 then a else 0) -
      (if n % 2 = 0 ∧ X < n ∧ n ≤ 2 * X then a else 0) := by
  unfold edge shortcut
  by_cases he : n % 2 = 0
  · simp only [he, false_and, true_and, ite_true, ite_false, zero_ne_one]
    split_ifs <;> first | omega | simp_all
  · have ho : n % 2 = 1 := by omega
    simp only [ho, false_and, true_and, ite_false, one_ne_zero]
    split_ifs <;> first | omega | simp_all

def incoming (X v : ℕ) (w : ℕ → G) : G :=
  ∑ n ∈ range (2 * X + 1), if shortcut n = v then w n else 0

/-- Finite divergence theorem for the physical shortcut graph. The artificial
zero vertex maps to itself and cancels, so this equals the positive-integer cut. -/
theorem sum_divergence (X : ℕ) (w : ℕ → G) :
    ∑ v ∈ range (X + 1), (w v - incoming X v w) =
      ∑ n ∈ range (2 * X + 1), edge X n (w n) := by
  classical
  have hsrc : (∑ n ∈ range (2 * X + 1), if n ≤ X then w n else 0) =
      ∑ n ∈ range (X + 1), w n := by
    rw [← Finset.sum_filter]
    congr 1
    ext n
    simp only [mem_filter, mem_range]
    omega
  have hin : (∑ v ∈ range (X + 1), incoming X v w) =
      ∑ n ∈ range (2 * X + 1), if shortcut n ≤ X then w n else 0 := by
    unfold incoming
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro n _
    rw [Finset.sum_ite_eq (range (X + 1)) (shortcut n) (fun _ => w n)]
    simp only [mem_range, Nat.lt_succ_iff]
  simp only [edge, Finset.sum_sub_distrib, hsrc, hin]

end Collatz.AnnularCut

#print axioms Collatz.AnnularCut.preimage_bound
#print axioms Collatz.AnnularCut.edge_annular
#print axioms Collatz.AnnularCut.sum_divergence
