import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! A common integer linear combination of ranks through one mechanical window.
The finite identities keep the endpoint, the complete denominator, and every power
of two in the cancellation of adjacent coefficient numerators. -/

namespace Collatz.SixHour.RankDivision

open Finset

theorem window_identity (z c b u v : ℕ → ℚ)
    (edge : ∀ j, b j * z (j+1) = 3*z j+c j)
    (carry : ∀ j, v (j+1) = b j*u j) (n : ℕ) :
    (∑ j ∈ range n, (v j-3*u j)*z j) + v n*z n
      = v 0*z 0 + ∑ j ∈ range n, u j*c j := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [sum_range_succ, sum_range_succ, carry]
    linear_combination ih + u n * edge n

theorem adjacent_coefficient_integral {M t k k' : ℤ}
    (unit : IsCoprime M t) (left : M ∣ t*k-1)
    (right : M ∣ t*(3*k')-1) : M ∣ k-3*k' := by
  apply unit.dvd_of_dvd_mul_left
  convert dvd_sub left right using 1
  ring

theorem complete_denominator {d source image scale error : ℤ}
    (primitive : IsCoprime d source) (identity : scale*image=source+d*error) :
    IsCoprime d image := by
  obtain ⟨a,b,h⟩ := primitive
  refine ⟨a-b*error,b*scale,?_⟩
  linear_combination h + b * identity

end Collatz.SixHour.RankDivision
