import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Int.Interval
import Mathlib.Tactic.Ring

/-! Exact endpoint, paired-cell, and arithmetic interlacing kernels. -/

namespace Collatz.ClockInversion

/-- Failure to hit the old minimum on the lattice twice as fine forces the
two possible integer defects at the final quarter-scale ceiling. -/
theorem minimum_seam_defect {x U : ℤ}
    (last : U = (3*x+3)/4) (finer : (3*x+1)/2 < 2*U) :
    4*U-3*x = 2 ∨ 4*U-3*x = 3 := by omega

/-- A genuine physical two-grade edge places the next unused integer
immediately above its folded label on the upper ceiling schedule. -/
theorem adjacent_ceiling {z z' B c : ℤ} (hB : B = 2 ∨ B = 4)
    (hc : c = 1 ∨ c = 2) (edge : B*z' = 3*z+c) :
    0 ≤ B*(z'+1) - 3*(z+1) ∧ B*(z'+1) - 3*(z+1) < B ∧
      B-1 - (B*(z'+1) - 3*(z+1)) = 2-c := by
  rcases hB with rfl | rfl <;> rcases hc with rfl | rfl <;> omega

/-- A second larger ceiling orbit is equivalent at each date to a
nonnegative floor register with a single binary input equal to 2-c. -/
theorem adjacent_difference {z z' k k' B c : ℤ} (hB : B = 2 ∨ B = 4)
    (edge : B*z' = 3*z+c) :
    (0 ≤ B*(z'+1+k') - 3*(z+1+k) ∧ B*(z'+1+k')-3*(z+1+k) < B) ↔
    k' = (3*k + (2-c))/B := by
  rcases hB with rfl | rfl <;> omega

/-- Two Apéry indicators formed by shifts a distance D apart alternate
inside a D-progression. This finite prefix formula has no primality premise. -/
theorem progression_interlace (F : ℤ → ℤ) (s v D : ℤ) (n : ℕ) :
    (∑ j ∈ Finset.range n, (F (s-(j:ℤ)*D-v) - F (s-(j:ℤ)*D-(v+D)))) =
      F (s-v) - F (s-(n:ℤ)*D-v) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    push_cast
    have h : s-(n:ℤ)*D-(v+D) = s-((n:ℤ)+1)*D-v := by ring
    rw [h]
    omega

end Collatz.ClockInversion
