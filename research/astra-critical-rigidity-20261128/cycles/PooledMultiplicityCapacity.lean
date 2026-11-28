import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.BigOperators

/-!
A finite binary coordinate code on k+1 actual columns. Distinct
multiplicity vectors of total h give distinct full row-sum vectors.
Padding k independently chosen counts with the reference column gives
the individual-cell capacity inequality used in the sharp pooled theorem.
-/

set_option autoImplicit false

namespace Collatz.PooledMultiplicityCapacity

/-- All declared coordinates may be the active ones: on other rows all
columns coincide and equal total multiplicities already give equal sums. -/
theorem padded_binary_capacity (k n h cap : ℕ) (budget : k * cap ≤ h)
    (digit : Fin (k + 1) → Fin n → ℕ) (binary : ∀ i t, digit i t ≤ 1)
    (multiset_separation : ∀ a b : Fin (k + 1) → ℕ,
      (∑ i, a i) = h → (∑ i, b i) = h →
      (∀ t, (∑ i, a i * digit i t) = ∑ i, b i * digit i t) → a = b) :
    (cap + 1) ^ k ≤ (h + 1) ^ n := by
  classical
  let pad (u : Fin k → Fin (cap + 1)) : Fin (k + 1) → ℕ :=
    Fin.cons (h - ∑ i, (u i).val) (fun i => (u i).val)
  have mass (u : Fin k → Fin (cap + 1)) : (∑ i, pad u i) = h := by
    have ub : (∑ i, (u i).val) ≤ h := by
      calc
        _ ≤ ∑ _i : Fin k, cap := Finset.sum_le_sum (fun i _ => Nat.le_of_lt_succ (u i).isLt)
        _ = k * cap := by simp
        _ ≤ h := budget
    rw [Fin.sum_univ_succ]
    simp only [pad, Fin.cons_zero, Fin.cons_succ]
    omega
  let encode (u : Fin k → Fin (cap + 1)) (t : Fin n) : Fin (h + 1) :=
    ⟨∑ i, pad u i * digit i t, by
      apply Nat.lt_succ_of_le
      calc
        _ ≤ ∑ i, pad u i * 1 := Finset.sum_le_sum
          (fun i _ => Nat.mul_le_mul_left (pad u i) (binary i t))
        _ = h := by simpa only [Nat.mul_one] using mass u⟩
  have inj : Function.Injective encode := by
    intro u v eq
    have same : pad u = pad v := multiset_separation _ _ (mass u) (mass v)
      (fun t => congrArg Fin.val (congrFun eq t))
    funext i
    apply Fin.ext
    simpa only [pad, Fin.cons_succ] using congrFun same i.succ
  simpa only [Fintype.card_fun, Fintype.card_fin] using Fintype.card_le_of_injective encode inj

#print axioms padded_binary_capacity

end Collatz.PooledMultiplicityCapacity
