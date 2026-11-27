import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Exact finite shortcut current with the actual odd-edge defect retained. -/
set_option autoImplicit false

namespace Collatz.Diagonal.OrdinaryCurrent

def harmonic (b : ℕ → ℚ) (N : ℕ) : ℚ :=
  ∑ k ∈ Finset.range N, b (k+1) / ((k:ℚ)+1)

theorem harmonic_succ (b : ℕ → ℚ) (N : ℕ) :
    harmonic b (N+1) = harmonic b N + b (N+1)/((N:ℚ)+1) := by
  exact Finset.sum_range_succ _ _

theorem odd_harmonic (b : ℕ → ℚ) (evenRule : ∀ n, b (2*n)=b n) (N : ℕ) :
    (∑ k ∈ Finset.range N, b (2*k+1)/(2*(k:ℚ)+1)) =
      harmonic b (2*N) - harmonic b N/2 := by
  induction N with
  | zero => simp [harmonic]
  | succ N ih =>
    rw [Finset.sum_range_succ, ih, Nat.mul_succ, harmonic_succ, harmonic_succ,
      harmonic_succ]
    have hb : b (2*N+1+1) = b (N+1) := by
      simpa only [Nat.mul_succ, Nat.add_assoc] using evenRule (N+1)
    rw [hb]
    push_cast
    have h : (N:ℚ)+1 ≠ 0 := by positivity
    have h' : (2*(N:ℚ)+1+1) = 2*((N:ℚ)+1) := by ring
    rw [h']
    field_simp
    ring

theorem odd_edge_identity (b : ℕ → ℚ) (k : ℕ) :
    b (3*k+2)/(3*(k:ℚ)+2) +
      (2/3:ℚ)*b (2*k+1)/((2*(k:ℚ)+1)*(3*(2*(k:ℚ)+1)+1)) +
      2*(b (2*k+1)-b (3*k+2))/(3*(2*(k:ℚ)+1)+1) =
        (2/3:ℚ)*(b (2*k+1)/(2*(k:ℚ)+1)) := by
  field_simp
  ring

/-- The residue-two sum is indexed by precisely its positive representatives
up to 3N. The last summand retains b(n)-b(T n) on every true odd edge. -/
theorem finite_current (b : ℕ → ℚ) (evenRule : ∀ n, b (2*n)=b n) (N : ℕ) :
    (∑ k ∈ Finset.range N,
        (b (3*k+2)/(3*(k:ℚ)+2) +
        (2/3:ℚ)*b (2*k+1)/((2*(k:ℚ)+1)*(3*(2*(k:ℚ)+1)+1)) +
        2*(b (2*k+1)-b (3*k+2))/(3*(2*(k:ℚ)+1)+1))) -
      harmonic b (3*N)/3 =
      (2*harmonic b (2*N)-harmonic b N-harmonic b (3*N))/3 := by
  have heq : (∑ k ∈ Finset.range N,
        (b (3*k+2)/(3*(k:ℚ)+2) +
        (2/3:ℚ)*b (2*k+1)/((2*(k:ℚ)+1)*(3*(2*(k:ℚ)+1)+1)) +
        2*(b (2*k+1)-b (3*k+2))/(3*(2*(k:ℚ)+1)+1))) =
      ∑ k ∈ Finset.range N, (2/3:ℚ)*(b (2*k+1)/(2*(k:ℚ)+1)) := by
    apply Finset.sum_congr rfl
    intro k _
    exact odd_edge_identity b k
  rw [heq, ← Finset.mul_sum, odd_harmonic b evenRule]
  ring

end Collatz.Diagonal.OrdinaryCurrent
