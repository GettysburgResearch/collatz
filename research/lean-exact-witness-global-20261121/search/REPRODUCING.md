# Exact source-witness search checkpoint

**The global theorem remains open.** The Lean source-witness kernels prove that a complete, strictly decreasing certificate family would close the implication. The searches here do not provide such a complete family.

This directory is self-contained Python 3.9 or newer, using only the standard library. No pickle, large availability dump, network access, external source checkout, or optional solver is needed.

## Contents

| File | Role |
|---|---|
| `check_source_certificates.py` | Exact positive affine replay; oriented query extraction; independent explicit forward-prefix audit; rank checks; dependency pruning; adaptive binary-partition audit. |
| `source-prefix-words.json` | 738 frozen accepted paths from the earlier mixed candidate pool, stored as move words. Affine coefficients and every claimed guard are regenerated. This file does not claim to reproduce the larger heuristic search. |
| `source_frontier.py` | Exhaustive fixed-cell one-query positive-clock grammar, with zero-query ordinary mergers retained. |
| `source_energy_frontier.py` | Exhaustive fixed-cell one-query removed-peak grammar, with a mathematically derived finite inverse-tree bound. |
| `refine_source_clock.py` | Binary refinement of unresolved clock cells; retains every unresolved branch and activates queried coarse cells. |
| `refine_source_energy.py` | Binary refinement of unresolved energy cells; also retains finite entrance exceptions explicitly. |
| `reports/…/search/*-receipt.json` | Small frozen replay summaries and semantic hashes. |
| `reports/…/search/search-provenance.json` | Hashes of the original process artifacts and the portable source files. |

## What the fixed grammars exhaust

The comparison kinds are `F3(n): Basin(n) → Basin(3n)` and `R3(n): Basin(3n) → Basin(n)`. Ordinary operations are `D(n)=2n`, `E(n)=n/2` on even inputs, `O(n)=(3n+1)/2` on odd inputs, and `I(n)=(2n−1)/3` when it is an integer. Every affine slope and intercept is positive, and every guard is checked for the whole parameter progression.

For an affine form, ordinary forward steps reduce the binary valuation of its slope by one. Its unique form with odd slope is invariant along every legal ordinary edge. Consequently, a normalized one-query source with positive clock decrease lies in the inverse tree of the parent source frontier at depth strictly less than the parent's slope height. Equality of desired-target frontiers supplies the other ordinary arm. This is a complete finite enumeration for that grammar, not an arbitrary word-depth cutoff and not completeness for arbitrary witness transformations.

For the removed-peak grammar, let `P` be the largest slope on the parent's ordinary forward prefix. An inserted inverse-tree node with slope greater than `P` cannot be dominated on any eventual parameter tail and cannot cancel a parent-prefix value. Its descendant branch is therefore pruned. Every inverse slope has the form `g·2^h·3^j`, where `g` is the fixed odd part coprime to three and `j≥0`; hence `h≤floor(log2(P/g))`. Equal slopes are retained and receive exact intercept checks. The final accepted row is independently checked using two actual forward prefixes with a common endpoint.

These statements concern the stated normalized one-query grammars and eventual affine prefix dominance. They do not rule out other witnesses, other query alphabets, multiple-query strategies, or other ranks.

## Frozen outcomes

- Historical frozen paths: 137 ordinary mergers, 188 forward-consumption rules, 386 multiset-replacement rules, and 27 length-only rules. The energy-compatible rules insert at most eight values, so base nine suffices. Hitting-time and energy coverage are checked separately; each closes only 5 of the 80 essential `R3` cells.
- Fixed clock grammar, modulus 1440: 450 rows, comprising 360 strict-clock candidates and 90 ordinary mergers. Twenty essential roots have candidates before pruning; only five survive complete dependency pruning.
- Fixed energy grammar, modulus 1440: 565 rows, 23,700 inverse nodes, maximum derived inverse depth 12. Base ten suffices for the accepted prefixes. Ten essential roots have candidates before pruning; only five survive complete dependency pruning.
- Adaptive clock checkpoint: 20,000 processed cells; 2,947 resolved leaves; 15,372 unresolved cells; 1,266 activated coarse states; 17,053 binary splits. Three leaves flag a possible parameter-zero early visit to one.
- Adaptive energy checkpoint: 10,000 processed cells; 1,486 resolved leaves; 8,099 unresolved cells; 1,071 activated coarse states; 8,514 binary splits; 324,272 inverse nodes. Base fifteen covers the accepted insertions. The 1,257 finite entrance exceptions remain listed and unproved by this search.

The adaptive checker verifies that resolved leaves together with unresolved cells form a disjoint, complete binary partition of every activated coarse progression. It separately checks that all queried coarse states were activated. A nonempty unresolved frontier is not a completed induction and is not an impossibility theorem.

## Replay commands

Run these commands from this directory. Generated outputs are disposable; the compact receipts in the reports directory remain the frozen reference.

```sh
python3 check_source_certificates.py source-prefix-words.json --expect ../../../reports/lean-exact-witness-global-20261121/search/source-prefix-receipt.json
python3 -O check_source_certificates.py source-prefix-words.json --expect ../../../reports/lean-exact-witness-global-20261121/search/source-prefix-receipt.json

python3 source_frontier.py --out /tmp/collatz-clock-fixed.json
python3 check_source_certificates.py /tmp/collatz-clock-fixed.json --expect ../../../reports/lean-exact-witness-global-20261121/search/fixed-clock-receipt.json

python3 source_energy_frontier.py --out /tmp/collatz-energy-fixed.json
python3 check_source_certificates.py /tmp/collatz-energy-fixed.json --expect ../../../reports/lean-exact-witness-global-20261121/search/fixed-energy-receipt.json

python3 refine_source_clock.py --budget 20000 --out /tmp/collatz-clock-adaptive.json
python3 check_source_certificates.py /tmp/collatz-clock-adaptive.json --expect ../../../reports/lean-exact-witness-global-20261121/search/adaptive-clock-receipt.json

python3 refine_source_energy.py --budget 10000 --seconds 300 --out /tmp/collatz-energy-adaptive.json
python3 check_source_certificates.py /tmp/collatz-energy-adaptive.json --expect ../../../reports/lean-exact-witness-global-20261121/search/adaptive-energy-receipt.json
```

The energy checkpoint originally completed its 10,000-cell budget inside a 30-second wall budget. The larger replay wall allowance above protects the same deterministic cell budget on slower machines. The semantic digest excludes only elapsed seconds, code-file provenance hashes, and the wall allowance; all mathematical records, statistics, active states, unresolved cells, and finite exceptions remain covered by the digest.

The checker uses explicit exceptions for validation. Its checks remain enabled under `python3 -O`. The historical mixed-path receipt independently validates the stored accepted rows; regeneration of the much larger preceding heuristic candidate pool is outside this compact checkpoint's scope.
