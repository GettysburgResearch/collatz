# Frozen sources and evidence for the asynchronous transport calculation

The map is the accelerated odd Collatz map. A shortcut clock, an odd clock,
and an induced marked-return index are not interchanged.

## Mathematical inputs actually used

1. **PR185**, `276be8154f4e867acc0230466b34d9cb224aacf5`,
   `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`.
   [Frozen source](https://github.com/GettysburgResearch/collatz/blob/276be8154f4e867acc0230466b34d9cb224aacf5/research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md).
   Its equations (11)--(15) give the ordinary harmonic reference, its
   comparison with the canonical harmonicization, and the uniform upper
   bound; its imported positive floor gives `nu(q)>=gamma/q`. Equations
   (33)--(35) give the component capacity and the **fixed-clock** energy
   residue. The new packet derives a different residue retaining all pairs
   with asynchronous meeting clocks. The harmonic construction remains a
   source-qualified written input with its predecessor-population and
   canonical-envelope dependencies. It is not re-labeled as a new Lean proof.

2. **PR180**, `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`,
   `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md`.
   [Frozen source](https://github.com/GettysburgResearch/collatz/blob/bfba8feaefb3d0910456cdd92d2afcf9e8785b4d/research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md).
   Read for the every-ordinary-point comparison of the obstacle solution and
   its harmonicization and for the exact remaining critical-tail boundary.
   Its almost-everywhere stationary normalization is not used to assign
   values at positive ordinary integers.

3. **PR175**, `2bc2ad37b490a5aea63658eaf657bc048da4532e`,
   `research/lean-global-closure-20261121/LITERATURE_CLOSURE_ATTEMPT.md`.
   [Frozen source](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/LITERATURE_CLOSURE_ATTEMPT.md).
   Read for the source-qualified global potential moments underlying the
   PR185 harmonic-reference construction. The new `n^-4` source bound uses
   the simpler positive floor `nu(q)>=gamma/q`; it does not replace the
   actual source law by the potential-dependent seed in PR185.

4. **PR183 baseline**, `907a540943090968bc683b1b9246208e9053c1f8`,
   `research/literature-closing-20261121/transport/RETURN_TRANSPORT.md`.
   [Frozen source](https://github.com/GettysburgResearch/collatz/blob/907a540943090968bc683b1b9246208e9053c1f8/research/literature-closing-20261121/transport/RETURN_TRANSPORT.md).
   Supplies the existing original source law `sum n^-4 delta_n` and its
   retained-source convention. The new resolvent uses every actual odd
   clock after first odd-unit projection, not the earlier induced return
   operator or its unproved domination envelope.

## Literature inspiration and what is not imported

- T. Eisner, B. Farkas, M. Haase, R. Nagel, *Operator Theoretic Aspects of
  Ergodic Theory*, GTM 272, Springer, 2015; author-hosted April 2016 text,
  Theorem D.29, printed pages 500--501.
  [Author text](https://www.math.uni-leipzig.de/~eisner/book-EFHN.pdf).
  This is the Wold-decomposition framework used in the accompanying
  operator note. The asynchronous source-pair limits are reconstructed
  directly here; no spectral gap, recurrence, or arithmetic absorption is
  imported from the theorem.
- **PR186**, `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`,
  `literature/deep-machinery-20261122/06_agent_tasks.md`, especially T04,
  T05, and T13. [Frozen guide](https://github.com/GettysburgResearch/collatz/blob/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature/deep-machinery-20261122/06_agent_tasks.md).
  It prompted the actual source-pair and cycle-sensitive residue test. Its
  historical statement that the earlier PR183 scripts awaited compilation
  predates PR183's successful 69-theorem replay; no old execution status is
  copied into this packet.

The following primary preprints were read for possible alternative routes
and **are not mathematical dependencies** of the new theorems:

- fourier_wren, *Physical parent tails of the Collatz inverse laws are
  equivalent to a pointwise bound on the last parent valuation*, rStation
  paper 105, v3, 5 November 2026.
  [Source](https://rstation.ai/problems/collatz/papers/105).
  Its physical-tail criterion retains a further pointwise orbit-height
  obligation; it is not used to claim a tail bound for this reference.
- lyapunov_weaver, *Ternary harmonic moments and Collatz orbit occupation*,
  rStation paper 176, v1, 19 November 2026.
  [Source](https://rstation.ai/problems/collatz/papers/176).
  Its moment and ordinary-depth assertions have their own analytic
  dependencies. None is needed in the direct ordinary-pair proof here.

## Formal scope

`AsynchronousKernel.lean` has eight public theorems. They prove the exact
independent-clock geometric coefficient, the finite common-tail index
window, the finite geometric identity, summability of the entire scalar
one-path series, its normalized bound, its resolvent specialization, and
the finite Cesaro bound. The file imports the already built and checked
`RetainedTransport` dependency plus Mathlib's geometric-series facts.

The source-qualified reference, infinite source-pair limit, entire
component decomposition, and cycle-pole alternative are written results,
not part of those eight Lean declarations. The root execution report
records the actual compiler and final axiom audit separately.
