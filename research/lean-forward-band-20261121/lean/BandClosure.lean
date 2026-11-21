import RisingReturns
import CarrySection
import BandTransport
import BandParityBridge
import BandPopulationCriterion
import UnitPopulationTransport
import WitnessGlobal
import InverseDensityPotential
import MarkedDensityPotential

/-!
New results building on the pinned actual forward-section theorem.

The exact transport, marked-family component descent, and carry identities
are unconditional.  The finite survivor equivalence explicitly takes the
analytic population theorem as a hypothesis.  Neither that analytic theorem
nor the missing survivor upper bound is declared as a Lean axiom here.

The continuation adds exact unit-source population transport and complete
terminal-gap certificate results.  Its inverse-density and marked-density
closing theorems retain their upper-envelope and finite-base hypotheses.
The written analytic construction of a positive harmonic envelope is not
silently imported as a Lean axiom, and its marked sublinearity remains open.
-/
