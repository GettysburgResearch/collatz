# Ordinary basin pressure: execution and proof scope

23 November 2026. **Full Collatz and the original residue-512 implication
remain open.** The scientific entry points are
[`SPARSE_BASIN_MINIMA.md`](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/SPARSE_BASIN_MINIMA.md)
and
[`BASIN_PRESSURE_PACKING.md`](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/BASIN_PRESSURE_PACKING.md).

The coordinating first-hit argument proves an explicit bound
`12 X^(799/800)` for the number of disjoint upper-sibling basins meeting
the small ordinary source range. The pressure lane retains each source
weight and proves all-sibling s-th-root Green summability for every s>1.
In particular the square roots of the fixed-sibling Green ratios are
summable along the unchanged hypothetical escaping ray. No analytic
predecessor-density input is used.

## Formal declarations actually compiled

[`BasinPacking.lean`](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/BasinPacking.lean)
contains thirteen new public declarations:

| Declaration | Exact finite scope |
|---|---|
| `descent_forces_earlier_hit` | A smaller positive endpoint of one basin minimum forces a hit of its specified root within the same supplied clock. |
| `shortcut_positive` | The actual natural-number shortcut preserves positivity. |
| `shortcut_height` | The actual one-step integer height inequality. |
| `shortcut_iterate_height` | Its complete arbitrary-clock integer iteration. |
| `two_hits_comparable` | Two targets reached from one deterministic source are comparable. |
| `iterate_on_ray` | Exact forward iteration on the supplied actual ray. |
| `off_ray_roots_incomparable` | Distinct off-ray roots entering that ray in one step cannot reach each other. |
| `predecessor_roots_unique` | One source cannot reach two such roots. |
| `finite_predecessor_basins_disjoint` | Realized finite predecessor sets are pairwise disjoint. |
| `touched_card_le` | Disjoint basins meeting a finite low-source set inject into that set. |
| `untouched_mass_le_tail` | Every untouched source weight is retained in the displayed finite tail. |
| `finite_source_cutoff_with_capacity` | The full finite cutoff bound with an explicit bound on touched basins. |
| `finite_source_cutoff` | The bound using the elementary one-source-per-touched-basin capacity. |

Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` were used. All declarations
were audited in an actual compilation with `-j 1 -DwarningAsError=true`.
The only axioms printed are subsets of `propext`, `Classical.choice`,
and `Quot.sound`; no `sorryAx` or custom research axiom appears.

The formal minimum theorem quantifies over a minimum of the entire
positive predecessor set. The formal graph theorem assumes the supplied
ray, root edges, off-ray condition and injectivity explicitly. The real
power saving for the basin-minimum count, infinite component pressure,
real-power concavity, tail integrals, rearrangement exponents and proposed
Green comparison are written scope, not implicit Lean conclusions.

## Exact finite controls actually executed

The new checker was run normally and with Python optimization. Both
exited zero and produced byte-identical JSON, SHA256
`a3214e38af388a1b2a6c41fcf65853c763d19e809f7ec4764bb5425866a52b2a`.
It takes the first twelve noncyclic odd states from source 41 and their
upper siblings. It enumerates all positive sources through 14,933,
thereby obtaining the exact minima of those twelve actual basins.
These ordinary examples converge; they are not purported escaping data.

- 115 actual predecessor sources are retained in the finite weight pool.
- 145 first-hit/height checks, including 86 descending endpoints.
- 13,312 literal full-carry identities and 13 exact no-descent capacities.
- 192 finite source-cutoff inequalities with the complete specified tail.
- 64 exact abstract sharpness controls, explicitly not Collatz basins.
- Three damaged or false extensions rejected: overlapping basins,
  an omitted source, and removal of the true-minimum hypothesis.

For the last control, the actual ancestor 1566 descends to 783 in one
shortcut step but does not reach target 2645 until clock four. Its
smaller ancestor 783 is the genuine basin minimum. This exposes why an
arbitrary small ancestor cannot replace the minimum in the first-hit
argument.

[`REPLAY.json`](REPLAY.json) preserves all three actual command records,
combined outputs, exact source hashes, compiler/dependency identity, and
normal/optimized comparison. [`SOURCES.json`](SOURCES.json) distinguishes
proof dependencies, current-head inspections, duplicate detection and
the unimported literature lead. Root's separate checker and publication
gate are reported by the coordinating agent, not counted as these three
executions.

## Reproduce this finite layer

From the pinned Mathlib environment:

```bash
lake env lean -j 1 -DwarningAsError=true /absolute/path/to/BasinPacking.lean
```

From the repository root:

```bash
python -X utf8 -B research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/check_basin_packing.py
python -O -X utf8 -B research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/check_basin_packing.py
```

The checker takes under a second in the recorded environment. No
historical mathematical corpus, large census, or upstream formal package
was rerun. Kernel checking, bounded arithmetic controls, written proof
review and repository integrity remain distinct evidence.
