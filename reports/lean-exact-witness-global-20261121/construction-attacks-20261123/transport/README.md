# Full-source finite certificate: evidence and boundary

23 November 2026. **The universal moving-sibling mass construction remains
OPEN. Full Collatz and the residue-512 implication remain OPEN.**

[Proof and actual projection](../../../../research/lean-exact-witness-global-20261121/construction-attacks-20261123/transport/FULL_SOURCE_FINITE_CERTIFICATE.md)
· [Execution receipt](REPLAY.json) · [Source ledger](SOURCES.json)

## Result

Any finite set `G` of full positive shortcut ancestors of one unchanged
unit target gives a finite set of unit-odd ancestors. Remove initial
powers of two; if the odd part is divisible by three, take its first odd
successor. Every projection prefix is part of the supplied actual hitting
path. The projected height is at most `5n/3`, with equality at `3 -> 5`.

All collisions are retained in an explicit two-parameter fiber. For every
`s>0` the weighted loss is at most

`C_s = [1 + (5/3)^s/(1 - 64^(-s))] / (1 - 2^(-s))`.

At `s=2`, `C_2=111404/22113<6`. For nonempty `G`, this gives the earlier
ordinary free-energy certificate directly from the positive mass
`sum_(n in G)n^(-s)`, without a logarithmic source-counting loss. The
count-height version requires `N>=1`. The unnormalized finite projection
inequality remains valid for empty `G` as well. A separate exact formula
gives a pressure multiplier depending only on the projected integer modulo
nine; full shortcut and
unit-odd sibling Green ratios are comparable by explicit constants.

The construction makes unrestricted ordinary predecessor data usable.
It does not produce those data at the height and population required to
contradict the preceding root-summability theorem.

## Formal scope and actual execution

`UnitProjection.lean` passed with `-j 1 -DwarningAsError=true` under Lean
4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

Six public declarations are audited:

- `odd_part_reaches`: actual initial halving removal preserves the same odd target.
- `nonunit_odd_successor_reaches`: actual odd acceleration of the nonunit odd part preserves the same unit target.
- `full_source_projects`: the combined ordinary path consumer.
- `odd_successor_unit`: the exact odd-step equation excludes divisibility by three.
- `projected_height`: the `5/3` height estimate in the nonunit case; the unit case is the immediate odd-part inequality.
- `finite_projection_mass`: finite fiber aggregation with duplicate images removed and a supplied fiber budget.

The printed axiom union is `propext`, `Classical.choice`, and `Quot.sound`.
There is no `sorryAx` or custom axiom. The countable geometric fiber sums,
arbitrary real inverse powers, and full pressure comparison are written
proofs; the finite aggregation theorem does not silently assume they were
formalized.

The exact checker passed normally and under `-O`, with identical output:

| Finite control | Count |
|---|---:|
| Full ordinary predecessor pools | 25 |
| Actual source atoms and projection paths | 13,700 |
| Sources with nonunit odd part | 4,424 |
| Projected suffix steps checked | 126,062 |
| Complete finite fiber rectangles | 201 |
| Complete fiber atoms | 7,035 |
| Failed-strengthening controls | 5 |

The five controls reject an uncharged height increase, bounded unweighted
multiplicity, discarded dyadic weight, a lost nonunit source, and confusing
one shortcut step with one complete odd acceleration. The actual
`75 -> 113 -> 170 -> 85` source is retained. Exact rational arithmetic
drives every pass/fail test; a few rounded output ratios are labeled
display values and paired with exact-ratio hashes.

`REPLAY.json` records the selected final commands, working directories,
actual exit codes, complete outputs and exact source hashes. These finite
examples include convergent ordinary components. They do not simulate an
escaping component or prove the unconstructed population bound.
