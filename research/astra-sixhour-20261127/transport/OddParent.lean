import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact three-child odd-parent arithmetic. The numerical branch length e is
represented by an odd power index (2k+1) or a positive even one (2k+2). -/

namespace Collatz.OddParent

set_option autoImplicit false

private theorem four_remainder (k : ℕ) : ∃ t : ℕ, 4^k = 3*t+1 := by
  induction k with
  | zero => exact ⟨0, rfl⟩
  | succ k ih =>
    obtain ⟨t, ht⟩ := ih
    exact ⟨4*t+1, by rw [pow_succ, ht]; omega⟩

/-- Every odd-exponent inverse child has Syracuse image 3q+2. -/
theorem plus_child (q k : ℕ) :
    ∃ v : ℕ, v % 2 = 1 ∧ 3*v+1 = (2*4^k)*(3*q+2) := by
  obtain ⟨t, ht⟩ := four_remainder k
  refine ⟨(2*4^k)*q+4*t+1, ?_, ?_⟩
  · rw [show (2*4^k)*q+4*t+1 = 2*(4^k*q+2*t)+1 by ring]
    omega
  · rw [ht]
    ring

/-- Every positive even-exponent inverse child has Syracuse image 3q-2.
Here q=2u+1 is positive by construction. -/
theorem minus_child (u k : ℕ) :
    ∃ v : ℕ, v % 2 = 1 ∧ 3*v+1 = (4*4^k)*(6*u+1) := by
  obtain ⟨t, ht⟩ := four_remainder k
  refine ⟨(8*4^k)*u+4*t+1, ?_, ?_⟩
  · rw [show (8*4^k)*u+4*t+1 = 2*(4*4^k*u+2*t)+1 by ring]
    omega
  · rw [ht]
    ring

#print axioms plus_child
#print axioms minus_child

end Collatz.OddParent
