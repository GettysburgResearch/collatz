# Checkpoint 11 execution and evidence

Scientific entry: [direct closure attempt](../../research/lean-global-resolvent-20261121/overview/central/README.md).

The pass did not obtain a positive global closing estimate. It established
the cofinal source-only obstruction and the arithmetic cost of retaining a
complete supplied prefix when lifting to ordinary siblings. The latter's
actual trajectory legality, unit condition and infinite weight sum have
written proofs; its formal core checks divisibility, the affine lift and
height bounds. The abstract extension of the record obstruction to other
well-founded certificate orders is also written only.

## Fresh integrated Lean build

[checkpoint11-lean.json](checkpoint11-lean.json) records the exact commands,
timings, outputs and source hashes. The reproduction driver and its
manifest are in the scientific packet.

**Result: all sixteen commands passed; all fourteen public audits passed;
the source hashes were unchanged.** The audit union contains only the
three standard axioms listed below. No `sorryAx` was reported.

- Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Fresh empty output directory, with no preexisting project object files.
- Thirteen reused core dependency modules, two new proof modules and the
  record audit: sixteen compilation commands in total.
- `-j1 -DwarningAsError=true` on each compilation.
- Four public record audits and ten public sibling-arithmetic audits.
- Actual axiom union: `propext`, `Classical.choice`, `Quot.sound`.
- Source hashes checked before and after the build.

The record proof itself needs Lean core only. Mathlib is used by the
standalone sibling module. The earlier checkpoint modules outside this
exact import closure were not replayed.

The first integrated invocation used an optional authenticated dependency
mirror that lacked `Mathlib.NumberTheory.Multiplicity.olean`. It compiled
the complete record closure and then stopped on the missing object before
checking the sibling source. The final invocation uses the pinned Mathlib
installation directly, with a new empty output directory; the receipt is
for that complete invocation. No proof source was changed to resolve the
environment issue.

## Review and publication boundary

The three explanatory notes and three Lean files are byte-identical to
their independently reviewed packets. Root reviewed both formal cores.
The analytic agent reconstructed the full sibling proof and the actual
record argument; the arithmetic agent independently checked the abstract
well-founded-order corollary. The record agent separately checked the
integrated README and source/review wrapper and reported no correction.
The exact evidence boundaries and file hashes are recorded in
[SOURCES_AND_REVIEW.md](../../research/lean-global-resolvent-20261121/overview/central/SOURCES_AND_REVIEW.md).

The complete repository integrity command is:

```sh
python -X utf8 -B tools/validate.py --receipt /tmp/checkpoint11-repository.json
```

It is run on clean complete commits, including the actual published head.
Its final commit/tree and execution outcome are recorded in
[PR176](https://github.com/GettysburgResearch/collatz/pull/176), avoiding a
self-referential commit hash in the committed receipt. That gate checks
repository integrity; it does not verify either written proof or establish
Collatz convergence. No optional numerical regression search is needed for
the new general theorems.
