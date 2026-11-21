import CarryBlocks
import SectionDynamics

namespace CollatzShell.ForwardSection

/-- The rank absorbs every first-return expansion that occurs before the
current trailing-one run is exhausted. -/
theorem carryHeight_on_return (n : Nat) (hr : returnTime n≤twos (n+1)) :
    CarryBlocks.carryHeight (next n)=CarryBlocks.carryHeight n :=
  CarryBlocks.carryHeight_constant_prefix n (returnTime n) hr

#print axioms carryHeight_on_return

end CollatzShell.ForwardSection
