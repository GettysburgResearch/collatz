import Std

/-! A retained selected-block word has a fixed lower bound for its
cumulative inverse division count minus seven-fourths of its odd clock.
One initial physical gap pays this bound simultaneously for all prefixes. -/

namespace SelectedBlockBarrier

/-- Retain a completed block whose total is at least 1.99 times its length.
The next length grows by at most one hundredth of the completed length. -/
theorem extendBlocks (base d b total w : Nat)
    (size : 100*b ≤ 100*base+d) (reserve : 199*d ≤ 100*total)
    (typical : 199*b ≤ 100*w) :
    100*(b+b/100) ≤ 100*base+(d+b) ∧
    199*(d+b) ≤ 100*(total+w) := by
  omega

/-- The partial clock is inside either the next selected block or the
last free segment, whose length is less than twice that block length. -/
theorem prefixDebt (base d b total u partialSum : Nat)
    (size : 100*b ≤ 100*base+d) (reserve : 199*d ≤ 100*total)
    (clock : u ≤ 2*b) (positiveGaps : u ≤ partialSum) :
    7*(d+u) ≤ 4*(total+partialSum)+6*base := by
  omega

/-- An initial gap creates any specified strict buffer at every clock. -/
theorem bridgePays (base t total e buffer : Nat)
    (debt : 7*t ≤ 4*total+6*base)
    (bridge : 6*base+7+4*buffer < 4*e) :
    7*(t+1)+4*buffer < 4*(total+e) := by
  omega

/-- The one-step bridge in particular makes a first visit to the target
the first permanently passing site on that ordinary trajectory, if it is
permanent. A failed full suffix already rules out each preceding site. -/
theorem failedSuffixPrecludesGate (gapTotal : Nat → Nat) (t : Nat)
    (bad : 7*t < 4*gapTotal t) : ¬ (∀ i, 4*gapTotal i ≤ 7*i) := by
  intro gate
  have := gate t
  omega

#print axioms extendBlocks
#print axioms prefixDebt
#print axioms bridgePays
#print axioms failedSuffixPrecludesGate

end SelectedBlockBarrier
