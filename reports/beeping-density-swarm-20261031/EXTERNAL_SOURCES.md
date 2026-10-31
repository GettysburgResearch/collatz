# Rebuilt source ledger and qualification boundary

**Recovery replacement, not the exact original ledger.** The original
ledger's recorded hash is retained in SOURCE_MANIFEST.json. This document
records the sources used in the present continuation and points to the
original manuscripts for their inherited attribution. It is not an exhaustive
independent audit of the whole repository or all historical references.

## Project baseline

Repository: `GettysburgResearch/collatz`.
PR142: `research/beeping-density-swarm-20261030` at
`d0f48c472d45a336e9083b37b45e1a8d39a2cf16`.

The prior packet's inverse-density and rank-envelope conventions remain the
starting point. Current repository guidance, README, research map, and scoped
errata were read at that pin. The recovered second packet itself lists
claim-level inherited dependencies, including the earlier actual-prefix
rank and orbitwise reciprocal estimates. No earlier theorem's review scope
is enlarged by recovering its citation.

## Canonical trace and predecessor-density manuscript

Author attribution: Lucas Valbuena.
Repository: `x1xhlol/collatz-two-coordinate-obstruction`.
Commit: `a7275d5a73814d3d9a400c6fe6577de9542b03a3`.
File: [paper/tao-basin-densities.tex](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).
Git blob: `63ca82653986b0dfa4c54bac17ed80199b806448`.

The present pass read the opening scope, canonical identification and forward
component boundary, uniform inverse-linear basin floor and canonical-floor
proofs, and first-hit depth estimates (requested source line ranges 1--180,
1200--1500, 1800--2000, and 2000--2260). Some connector responses were truncated;
no claim to inspect every source line or every dependency is made.

Named source statements:

- `thm:ct-canonical-identification`: canonical Cesaro/normalized-Abel trace.
- `thm:ct-inverse-linear-basin-floor`: d_N>=3/(128*K_seed*N) for units.
- `prop:ct-uniform-canonical-floor`: g(N)>=3*delta/(128*K_seed*P0)>0 for units.
- `prop:ct-first-hit-depth-bound`: positive first-hit depth bounds, including
  periodic targets, via nonperiodic unit siblings and disjoint basin charges.
- `prop:ct-forward-components`: the remaining global forward sublinearity
  condition; the manuscript explicitly does not prove Collatz.

These source claims depend on further results, including weighted predecessor
construction and coalescence inputs. No external Lean development or entire
source dependency chain was executed in the current pass. Their use in
PFB-003 is **SOURCE-QUALIFIED**, not an unconditional local theorem. The
stationary rho sequence is distinct from the source's weighted reference
varrho. The external source already states pointwise depth/trace results;
this package does not appropriate those as new discoveries.

## Critical-energy source retained from the recovered packet

At the same repository pin:
[paper/quadratic-cylinder-energy.tex](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/quadratic-cylinder-energy.tex),
recorded blob `2aeeda46df2e78b5fa541626d8a94f216a82702f`.
The recovered CRITICAL_ENERGY.md credits Valbuena's short non-L2 argument and
separates its clipping consequence from a claim about actual basin density.
The replay checks exact finite residue laws; it does not verify an infinite
formal development.

## Other inherited inputs

The recovered IFT-006 uses an external positive fast-density premise and
keeps it source-qualified. Its lower bound is target-dependent and is not
the uniform floor required by PFB-001. Historical references and proof
reconstructions in the recovered manuscripts remain scoped to their own
statements; recovery does not change their epistemic status.
