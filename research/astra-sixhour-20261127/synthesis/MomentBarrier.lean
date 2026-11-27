import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Linarith

namespace Collatz.MomentBarrier

/-- The five rational lower envelopes used in the written moment argument.
This definition and the inequalities below do not formalize Fourier analysis. -/
def lowerMoment (q : ℚ) : ℚ :=
  if q ≤ 2 then (47/100)*(q-1)
  else if q ≤ 61/18 then (47/200)*q
  else if q ≤ 4 then 109/100 - (12/25)*(4-q)
  else if q ≤ 5 then (109/400)*q
  else (47/100)*q-1

theorem envelope_gap (q : ℚ) (hq : 1 < q) :
    (1/3 + 1/30000)*(q-1) ≤ lowerMoment q := by
  unfold lowerMoment
  split_ifs <;> linarith

theorem above_cubic (q : ℚ) (hq : 1 < q) :
    (q-1)/3 < lowerMoment q := by
  have h := envelope_gap q hq
  linarith

#print axioms Collatz.MomentBarrier.envelope_gap
#print axioms Collatz.MomentBarrier.above_cubic

end Collatz.MomentBarrier
