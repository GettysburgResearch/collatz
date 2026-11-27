import FiniteTrace
import HeckeRank

/-! Rank obstruction on the exact ordinary all-odd excursion.
The support and doubling hypotheses describe the finite graph coefficient array. -/
namespace Collatz.ReciprocalRigidity

open Polynomial

theorem cutoff_rank_gap {k N H : ℕ} {a : ℕ → ℚ} {p : ℤ[X]} (hp : p ≠ 0)
    (hfit : HeckeRank.Fits p a N) (hk : 2 ≤ k) (hn : 2^k-1 ≤ N)
    (hNH : N ≤ H) (hH : H < 3^k-1)
    (hsupport : ∀ n, 0 < n → n ≤ H →
      (a n = 0 ↔ FiniteTrace.reachesOneBelow H n))
    (hdyadic : ∀ n, 2*n ≤ N → 4*a (2*n) = a n) : N+2 < 4*p.natDegree :=
  HeckeRank.finite_recurrence_gap hp hfit hdyadic
    (FiniteTrace.finite_prefix_nonzero hk hn hNH hH hsupport)

#print axioms FiniteTrace.odd_run
#print axioms FiniteTrace.cutoff_obstruction
#print axioms HeckeRank.recurrent_dyadic_zero
#print axioms HeckeRank.finite_recurrence_gap
#print axioms cutoff_rank_gap

end Collatz.ReciprocalRigidity
