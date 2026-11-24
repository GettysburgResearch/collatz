module

public import TernaryItinerary

public section
namespace Collatz.Itinerary.CycleRows

set_option autoImplicit false

/-- A nonempty ordinary odd lap through an endpoint above the trivial cycle. -/
@[expose] def NontrivialCycle : Prop :=
  ∃ (q s : Nat) (marks : List Bool), 2<q ∧ 0<marks.length ∧ Route q marks s q

/-- The endpoint and all its intermediate gaps are ordinary. The last
inequality tests sixth-power multiplicative distortion without division. -/
@[expose] def Witness (b : Nat) : Prop :=
  ∃ (q x : Nat) (marks : List Bool), 2<q ∧ marks.length=b ∧ Route q marks (2*b) x ∧
    (b+1)*(3^b*x)^6 < (2^(2*b)*q)^6

end Collatz.Itinerary.CycleRows
