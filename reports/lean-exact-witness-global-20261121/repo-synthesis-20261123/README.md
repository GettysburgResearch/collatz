# Repository synthesis: evidence and exact proof boundaries

23 November 2026. **Full Collatz, the residue-512 implication, and
FloorIntervalStep remain open.**

[Scientific packet](../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/README.md) ·
[All-PR inventory](REPOSITORY_INVENTORY.json) ·
[Root's actual executions](ROOT_REPLAY.json) ·
[Source and inspection ledger](SOURCES.json) ·
[Changed-file bindings](FILES.json)

## What the checkpoint establishes

| Result | Evidence and scope |
|---|---|
| At most `12 X^(799/800)` disjoint upper-sibling basins contain a positive source at height at most X; sharper eta approximately 0.99586542 under the separately pinned critical orbit theorem | Complete new written proof. Internal reconstructions check all ordinary-source, first-hit, carry, binomial and orbit-count steps. Finite actual controls include nonunit full-basin minima. The real exponent estimate is not advertised as a Lean theorem. |
| Actual Green ratios have summable s-th roots for every s>1; in particular square roots at s=2 | Written complete-tail cutoff, dyadic concavity and nonnegative-limit argument. No predecessor-density, Haar or random-gap premise. The ordinary lower comparison remains open. |
| The same conclusion covers every off-spine inverse parent, and complete ordinary capacity increments have summable s-th roots | Written exact partition of the whole unchanged component, root count below `24 Y^(39/40)`, basin-minimum count `64 X^(799/800)`, and full-kernel weights. No new Lean declaration or finite census is claimed for this extension. |
| Literal positive infinite word paths in the certified changing-defect language reach their common fixed point by an explicit integer quotient clock | End-to-end Lean consumer, including actual parity traces and intermediate ordinary integers. Arbitrary changing exponents and even an infinite defect family are allowed under the uniform complete-carry cutoff. |
| Exact finite search for every joint-edit merger budget, with complete source-tuple transport | Lean normalization, all-clock bound, search soundness/completeness and witness consumer. Python emits and checks the original full exponent identity. A universal successful edit budget is not asserted. |

The preceding scientific files remain at their original hashes. The
cumulative packet README is the only changed earlier file. Historical
manifests retain their original-commit meaning rather than being rewritten
to authenticate the new mutable index.

## Actual fresh root executions

The coordinating agent freshly compiled all three new modules with
`-j 1 -DwarningAsError=true`:

| Module | Public declarations audited | Dependencies |
|---|---:|---|
| `candidate/JointEditCompiler.lean` | 23 | Core/Std |
| `cycles/LatticeDescent.lean` | 20 | Core/Std |
| `escape/BasinPacking.lean` | 13 | Pinned Mathlib |
| **Total** | **56** | Only standard axioms in the audit |

Compiler: Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib for the finite pressure module:
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
The reported axiom union is `propext`, `Classical.choice`, `Quot.sound`;
`orbit_succ` is axiom-free. There is no `sorryAx` or custom research axiom.

All four new exact Python checkers were also freshly executed by root
normally and under `-O`, with byte-identical paired outputs. The root
receipt contains eleven selected execution records: three Lean compiles
and eight checker executions. The first displayed minima-checker output
was truncated, so it was rerun with full stdout captured outside the
checkout. Its SHA256 and byte equality with the complete checked-in
artifact are recorded, rather than calling a truncated display complete.

| Checker | Actual finite coverage |
|---|---|
| Joint-edit compiler | 1,024 independent grid comparisons, 2,016 common-run valuations, four damaged certificates, complete tuples and terminal padding; exact 39-edit optimum on the closed 1,848-state product for 193/385 |
| Infinite dictionary | 1,012 cutoff words, 250 ordinary traces, 750 macroedges, 20,084 literal shortcut steps, 1,112 paid affine edges; rational-cycle and missing-lookahead controls |
| Basin pressure | Twelve actual convergent basins with exact minima, 13,312 full carries, 192 complete finite source cutoffs and 64 sharp abstract controls; overlapping/omitted-source/minimum failures |
| Basin minima | Eighteen actual incomparable roots, all starts through 4096 resolved, nine exact minima, 140 first-hit partitions, 170 strict-hit controls, 40,960 carries, 2,047 complete cylinders and 65 exact binomial horizons |

These are finite implementation controls. They neither simulate an
escaping source nor establish infinite conclusions by extrapolation.
The root count, binomial asymptotics, pressure limits, real interpolation,
and original residue-512 coverage have the separate scopes described in
the manuscripts and module inventories.

## Internal proof reconstruction

- [Joint-edit compiler](reviews/REVIEW_JOINT_EDIT_COMPILER.md): an independent
  forward heap Dijkstra reconstructs the exact optimum on 1,848 states and
  4,598 edges, independently of the author's reverse zero/one algorithm.
- [Infinite dictionary](reviews/REVIEW_INFINITE_DICTIONARY.md): independent
  reconstruction of the lattice, cutoff, all-time clock and literal-word
  wrapper, plus a separate fresh strict compile.
- [Sparse basin minima](reviews/REVIEW_SPARSE_BASIN_MINIMA.md): independent
  proof of BM3--BM15, including a primary file read of the pinned PR182
  critical whole-orbit input. A further escape-lane reconstruction discloses
  its contribution to the rational constants.
- [Pressure packing](reviews/REVIEW_BASIN_PRESSURE.md): independent complete
  reconstruction of the source tail, power sums, Harnack consumer and
  signed-cost orientation.
- [Coordinating all-branch reconstruction](reviews/REVIEW_ALL_BRANCH_CAPACITY.md):
  the complete component partition, root count, enlarged basin-minimum
  constant, capacity increments and exact inverse-kernel weights. The
  coordinating reviewer coauthored the underlying first-hit argument;
  this is disclosed rather than described as external independence.

All reviews bind exact source hashes and retain their claim boundaries.
They are internal research checks, not external referee acceptance.

## Repository-wide orientation and source use

The complete nontruncated main tree at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` contains 315 tracked blobs.
All 145 PR records were retrieved: 122 open and 23 closed. The integrated
catalog, map, current errata and selected latest proof files were read.
The inventory does not assert independent reconstruction of every proof
on every historical branch. Source descriptions and metadata inspection
are distinguished from actual proof dependencies in `SOURCES.json` and
the lane ledgers.

An apparent new separated-visit count in the escape lane was identified
as existing PR182 work before publication. It is credited and used at its
pinned scope, not republished as a new theorem. The actual new connection
is the first-hit basin-minimum split and its pressure consequence.

## Complete-checkout publication gate

The required gate is run only after freezing a local commit, in a clean
complete checkout:

```bash
python -X utf8 -B tools/validate.py --receipt /absolute/path/outside/checkout.json
```

Its exact checked commit, tree, receipt hash and observed result are
recorded in the PR publication description after execution. The published
remote tree is compared with that checked tree, and its head and parent
are read back. This file records the already executed mathematical checks;
it does not fabricate a future checkout result or remote CI run.

Repository integrity, source identity, kernel checking and written proof
review establish different things. A successful publication gate is not
used as a proof of Collatz.
