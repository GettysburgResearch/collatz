import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Int.Basic
import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.LinearCombination

/-! Exact two-place and synchronous balance statements for finite history graphs. -/
namespace Collatz.HistoryTrades

set_option autoImplicit false

/-- Matching the future classes directly and the past classes after a permutation
forces the full signed integer sum to carry both coprime moduli. -/
theorem trade_dvd {n : ℕ} (a b : Fin n → ℤ) (τ : Equiv.Perm (Fin n))
    {M N : ℤ} (hmn : IsCoprime M N)
    (future : ∀ i, M ∣ a i - b i) (past : ∀ i, N ∣ a i - b (τ i)) :
    M * N ∣ (∑ i, a i) - ∑ i, b i := by
  apply hmn.mul_dvd
  · rw [← Finset.sum_sub_distrib]
    exact Finset.dvd_sum fun i _ => future i
  · rw [← Equiv.sum_comp τ b, ← Finset.sum_sub_distrib]
    exact Finset.dvd_sum fun i _ => past i

/-- The product test becomes equality throughout an interval narrower than
that product, even for cycles with more than four edges. -/
theorem trade_zero {n : ℕ} (a b : Fin n → ℤ) (τ : Equiv.Perm (Fin n))
    {M N : ℤ} (hmn : IsCoprime M N)
    (future : ∀ i, M ∣ a i - b i) (past : ∀ i, N ∣ a i - b (τ i))
    (width : ((∑ i, a i) - ∑ i, b i).natAbs < (M*N).natAbs) :
    (∑ i, a i) = ∑ i, b i := by
  by_contra h
  exact (not_le_of_gt width) (Int.natAbs_le_of_dvd_ne_zero
    (trade_dvd a b τ hmn future past) (sub_ne_zero.mpr h))

/-- A matched multiset of corrections transports an actual signed state
balance in either direction across one common-clock step. -/
theorem transport_balance {n : ℕ} (u v un vn cu cv : Fin n → ℤ)
    (τ : Equiv.Perm (Fin n)) {D G : ℤ} (hd : D ≠ 0) (hg : G ≠ 0)
    (plus : ∀ i, D * un i = G * u i + cu i)
    (minus : ∀ i, D * vn i = G * v i + cv i)
    (matchDigit : ∀ i, cu i = cv (τ i)) :
    (∑ i, un i) = ∑ i, vn i ↔ (∑ i, u i) = ∑ i, v i := by
  have hc : (∑ i, cu i) = ∑ i, cv i := by
    simpa only [matchDigit] using Equiv.sum_comp τ cv
  have ha : D * (∑ i, un i) = G * (∑ i, u i) + ∑ i, cu i := by
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib, plus]
  have hb : D * (∑ i, vn i) = G * (∑ i, v i) + ∑ i, cv i := by
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib, minus]
  constructor
  · intro eqn
    apply mul_left_cancel₀ hg
    rw [eqn, hb, hc] at ha
    exact (add_right_cancel ha).symm
  · intro eqn
    apply mul_left_cancel₀ hd
    rw [ha, hb, eqn, hc]

#print axioms trade_dvd
#print axioms trade_zero
#print axioms transport_balance

end Collatz.HistoryTrades
