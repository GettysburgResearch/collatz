# Nine-hour pass: critical ordinary sources and full returns

**Active research; Collatz remains unresolved.** This packet began at
2026-11-27 22:55:59 UTC and has a requested endpoint of 2026-11-28
07:55:59 UTC. The aim is to remove the exceptional ordinary source or
complete-return obstruction left by the preceding packets. Markdown
proofs and connected Lean kernels take priority over presentation work.

The branch starts from main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The preceding six-hour pass is
preserved in [PR211 at its closing head](https://github.com/GettysburgResearch/collatz/tree/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127).
The [intake](../../reports/astra-nine-hour-20261128/INTAKE.json) records
149 open PR heads; this is a metadata inventory, not verification of
149 mathematical packets.

## The three active directions

The [finite critical-tail certificate](FINITE_CRITICAL_TAIL.md) proves
that an actual positive source with the specified square-root-sized
parity deficit has already repeated a positive state. It uses only the
exact shortcut update and integer inequalities. It certifies entry into
some positive cycle without identifying that cycle.

- **Actual sources at the critical clock.** The
  [critical affine-correction law](escape/CRITICAL_CORRECTION.md) follows
  each original positive integer through first attainment of its own
  global orbit minimum. Under the named population inputs it identifies
  the cycle and escape mixture in one critical-time observable. It also
  expresses every below-center parity-count probability at that clock.
  The required Gaussian normalization remains an open arithmetic target.
- **Complete cycle arithmetic.** The
  [modular-quotient analysis](cycles/MODULAR_QUOTIENTS.md) uses a whole
  primitive positive rational cycle and its complete common denominator.
  It tests what a compatible finite congruence quotient would force on
  the entire binary calendar. Optional quotient compatibility is never
  silently asserted for an arbitrary cycle.
- **All finite congruences of actual ancestors.** The
  [profinite ancestor theorem](machinery/PROFINITE_ANCESTORS.md) extends
  the pinned positive entrance-family argument beyond the binary and
  ternary coordinates. It distinguishes fixed-modulus limits, direct
  source-wise steering, and the unresolved normalized flux at a specific
  escaping source.

These are proposed written deductions until their checkpoint review
states otherwise. A Lean file beside a note checks only its displayed
declarations and hypotheses; it does not formalize an external analytic
source by association.

## What a decisive result must establish

A full solution must exclude every additional positive cycle and every
unbounded positive orbit. Density-one periods, almost-everywhere parity
laws, compatible finite prefixes, and lower bounds for selected ancestor
families do not by themselves do that. In particular:

1. The preceding native extinction criterion leaves an unchanged
   reciprocal atom for each permanently passing ordinary source.
2. The preceding complete-denominator estimates leave exceptional least
   periods and high-complexity words.
3. The preceding inverse laws leave an atomic posterior at the original
   grade of a specified escaping ray. A limit with an increasing
   overshoot does not replace that original grade.
4. A Gaussian first-arrival clock does not automatically give a Gaussian
   parity count at a later deterministic clock. The actual intervening
   integer future must be retained.

The pass is testing these remaining statements directly, including new
tools from the current primary literature. Failed bridges and their
controls are retained with the exact premise that failed.

## Verification and checkpoints

The [replay driver](replay_lean.py) is adapted, with attribution, from
PR212's complete declaration audit. It rebuilds local modules into a
fresh directory, verifies the Lean release and clean pinned dependency
sources, and audits every local declaration including private ones.
The only permitted recursive axioms are `propext`, `Classical.choice`
and `Quot.sound`. There are no invented mathematical axioms, admitted
proofs, or native-decision shortcuts in the claimed kernels.

At the first publication the complete packet replay is **pending**;
the candidate sources must not be presented as a completed formal
proof. The [initial status](../../reports/astra-nine-hour-20261128/CHECKPOINT_01_LEAN_STATUS.md)
records successful individual compilations, repairs and the interrupted
batch. Later exact receipts determine the verified scope.

Lean is 4.34.1 at compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
Use a populated dependency cache, then run:

```sh
python -B replay_lean.py --lean /path/to/lean --mathlib /path/to/mathlib4 --receipt /outside/checkout/lean.json --build-parent /outside/checkout/builds
```

Finite arithmetic controls are run normally and with Python optimization
where applicable. Written arguments receive a separate reconstruction
record. The complete clean checkout also runs the repository integrity
validator; that validator checks repository structure and selected
regressions, not the mathematical truth of an asymptotic claim.

Checkpoint receipts are kept in
[the pass reports](../../reports/astra-nine-hour-20261128/README.md).
Scientific changes are committed and published during the pass. Main is
not merged as part of this research run.
