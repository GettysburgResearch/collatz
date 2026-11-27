# Verification of the new global-synthesis checkpoint

## Lean execution

The coordinating agent compiled all six new modules using the official
Lean 4.34.1 binary at release commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with `-j1` and
`-DwarningAsError=true`. Every module imports only `Std`. The audit
appends an axiom query for **every public theorem declaration**, including
public helper theorems omitted from an author's own printed queries.

| Module | Public theorems audited | Scope of the checked conclusion |
|---|---:|---|
| `section/ForwardAnchors.lean` | 9 | Integer critical lift and mark, physical products, moving-clock anchor identities, spliced transversals, short unit inverse and minimum sandwich. |
| `arithmetic/OctaveProfiles.lean` | 9 | Finite monotone-profile count interface, odd parity cylinder, full-divisor forcing, dyadic and triadic crossing arithmetic. |
| `merger/PaidPairs.lean` | 6 | Complete conditional paired-language ordinary comparison, including raw label classification and both odd floors. |
| `arithmetic/OptimalReset.lean` | 3 | Exact integer rounding and residue argument at a clock two, the incoming clock-one residue, and the short unit inverse. |
| `merger/MixedPaid.lean` | 3 | Complete conditional mixed singleton/pair ordinary comparison from raw labels, integrality and exact target equations. |
| `arithmetic/WindowControl.lean` | 2 | Exact inverse transfer and larger-source implication for the finite-window control. |
| **Total** | **32** | **All passed.** |

The only reported axioms are subsets of `propext`, `Classical.choice`,
and `Quot.sound`. No audited declaration depends on `sorryAx` or a
Collatz assumption. The literal comparison theorems quantify an actual
ordinary infinite input satisfying their explicitly restricted languages;
they do not assume existence of a smaller comparison source.

The [aggregate machine receipt](LEAN_AND_CONTROLS.json) includes source
SHA-256 hashes, all declaration names, their axiom lists, commands,
compiler version, exit codes and timing. The corresponding `.log`
files retain the compiler output. Before aggregation, the audited
copies were regenerated from the final sources and compared exactly,
so a source change during an earlier compilation cannot pass unnoticed.

## Exact finite controls

Every script was executed independently in normal and optimized Python.
All eight executions exited zero; each pair produced identical output.
Their arithmetic failures use explicit exceptions rather than removable
Python assertions.

| Script | Recorded bounded coverage |
|---|---|
| `arithmetic/check.py` | 9,774 moving profiles and 16,368 source occurrences; 941 primitive rational cycles, including 30 confined cycles and 29 nonintegral confined cycles; 5,627 dyadic and 32,459 triadic crossings; 506 noncoprime clock controls; 49,999 ordinary starts. |
| `merger/check.py` | 92 paired phase paths, 1,840 literal comparison edges, 72 finite asynchronous resets, and the two remaining small common-slope odd rational seeds. |
| `merger/mixed_check.py` | 581 mixed phase paths, including 233 with both cluster types; 12,782 literal comparison edges and 12,782 simultaneous strict floor comparisons. |
| `arithmetic/window_control.py` | 910 ordinary finite windows and 392,210 complete inverse words with weakly competitive clocks. The written uniform carry argument handles longer-clock competitors; the script does not enumerate infinitely many valuations. |

These examples supplement the proofs within their stated finite domains.
They establish neither an ordinary realization of every infinite symbolic
word nor the missing universal Collatz conclusion.

## Written proofs, inherited inputs and independent review

The real steering application, translated packing, infinite products,
absolute-width rigidity, full moving-window theorem, affine-permutation
cycle arguments, and distinct-component consequence are written
mathematics. The complete infinite statements are not asserted to be
formalized by their finite Lean arithmetic interfaces.

The section uses PR173's source-pinned steering theorem and PR193's
written translated-interval packing. Source signatures and mathematical
interfaces were read; older kernels were not rerun. The earlier 26
declarations already published in this PR remain at their prior receipts.
This checkpoint's count is the **32 new declarations** above.

Independent agent reviews are retained in the scientific packet:
`arithmetic/REVIEW_SECTION.md` and
`section/REVIEW_ARITHMETIC.md`, `REVIEW_MERGER.md`,
`REVIEW_OPTIMALITY.md`, `REVIEW_MIXED.md`.
[The coordinating review](ROOT_REVIEW.md) reconstructs the interfaces
and records the first unsupported universal inference. Model cross-review
is distinct from external human referee acceptance.

## Replay and checkout validation

From a complete checkout, with an official Lean 4.34.1 binary available:

```sh
python -B research/astra-global-synthesis-20261124/check.py \
  --lean /path/to/lean-4.34.1-linux/bin/lean \
  --out /tmp/collatz-global-synthesis-checks

python -X utf8 -B tools/validate.py \
  --receipt /tmp/collatz-global-checkout.json
```

The replay driver permits `--modules` and `--controls` subsets for a
changed-file replay. The original execution checked the first three
modules together, then checked each added module once and aggregated
the receipts. It did not recompile earlier unchanged kernels for the
sake of a single invocation.

Complete clean-checkout validation is a separate repository integrity
gate. Its exact commit and tree are recorded in the publication receipts
added after the scientific checkpoint. Integrity does not prove any
mathematical assertion.
