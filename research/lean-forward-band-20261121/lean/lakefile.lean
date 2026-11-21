import Lake
open Lake DSL

package «forward-band-closure» where
  leanOptions := #[⟨`warningAsError, true⟩]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "d13f23b723b8a846827a245b89c10fc7d3f11612"

@[default_target] lean_lib ForwardBand where
  roots := #[`ShellCover, `ForwardSection, `SectionDynamics, `RisingReturns, `CarryBlocks, `CarrySection, `BandTransport, `BandParityBridge,
    `BandPopulationCriterion, `UnitPopulationTransport, `WitnessGlobal,
    `InverseDensityPotential, `MarkedDensityPotential, `BandClosure, `Audit]
