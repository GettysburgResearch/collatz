# Machinery checkpoint: proof and execution scope

Date: 2026-11-22. Own parent: `f63204765438c83def68154e7f253ee9b660979c`.

## Fresh formal execution

`source-build.json` records two successful project-source compilations:
`BoundedLanguage.lean` and its separately importing audit. The compiler
was Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, with
warnings treated as errors and automatic implicit variables disabled.

The main source SHA256 is
`1231fdb21ba49c0d191a1fc4d54d0afa0697ea09093c9cbdcf8ebaae18ceded6`.
The audit source SHA256 is
`a3677f8bb7e6b7f77fdec3f6b6ec966aae82764fe9b4c8118da12dd662310008`.

Sixteen exported declarations, including the Collatz-count constructor,
were audited. All reported axioms are among `propext`, `Classical.choice`,
and `Quot.sound`. No `sorryAx` or custom axiom appears in these audits.
The arithmetic and exact finite recursion are formalized. The written
translation to parity words, valuation-optimal cutoff, zero-run extension,
automata statements, and all infinite analytic/deep arithmetic arguments
are outside this Lean claim.

Mathlib was pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612` with a
clean source worktree. Its installed objects and package dependencies
were reused. `bounded-language-import-closure.txt` lists the 2,450 module
names in the loaded environment, including the checked project module.
This is an import inventory, not 2,450 fresh dependency compilations.

`legacy-identity.json` verifies the exact hashes of all 21 sources in the
prior core-only build and its unchanged driver. Those old sources were
not recompiled in this pass. The new module is a separate Mathlib-based
build and does not import legacy project objects.

## Written proof review

The integrating agent independently reconstructed the final statements
below and checked the scopes of their hypotheses. Cross-lane receipts
are also included; these are internal mathematical reviews, not external
peer review or Lean verification.

| Final artifact | Independent review scope |
|---|---|
| Fixed-block cycle rigidity | Full compiler, exact Corvaja-Zannier statement, root-group confinement, bidegree, fixed buffers and physical fixed points |
| Bounded-language sources | Exact divisibility and finite recursion; base review plus BL4 addendum at final hash `63af23e8...` |
| Regular cycle-language corollary | Integrating agent reconstructed loop deletion from the reviewed fixed-schema theorem; nonempty accepted language retained |
| Moving ordinary fibres | Full-path law comparison, signed centered clocks, terminal digit, stopped inequality, compact BL selection, original labels and surviving submeasure |
| Tilted renewal and finite immigration | Square-weighted finite trace, last nonunit endpoints, complete depth budget, exact tail split, finite shifted averages and persistent ancestor |
| Exact run-weight commutator | Signed finiteness, original-charge negative-part domination, both killed-envelope signs, uniform Green-depth limit, component sum and supremum sandwich |
| Adaptive sibling attempt | Integrating agent reconstructed changed-word injection and terminal-height identity; both siblings retained where used; integer cutoffs specified |

The base bounded-language review records the earlier BL1-BL3-only hash
`b4707282...`. Its separate extension review pins the final note
`63af23e8...`, including BL4 and the explicit Lean/prose split. Both are
kept as scoped review records; the final source manifest identifies the
published bytes.

The entropy lane also reviewed the synthesized packet README. Its two
requested scope corrections were applied: the scalar supremum now
explicitly ranges over retained positive odd unit roots, and the tail
statement explicitly retains the scalar-tail input and aligned Cesàro
average. The corrected README SHA256 is
`2b877071ce4850d10ca690a5845065233aa3e2e0d8aa8bff528a28ac2eabbb3a`.
No individual-depth or unrestricted-root convergence is claimed.

`block-compiler-controls.json` contains the arithmetic lane's 11 exact
finite compiler/parity controls. They are bookkeeping checks, not a
premise of the infinite cycle theorem and not a global cycle search.

## Pinned inputs and publication check

`SOURCES.json` records 14 exact repository files and the external source
statements used. PR177 was refreshed during the work and its new
`e4ca6393...` arithmetic and energy arguments were read before the exact
commutator deduction. No complete re-verification of that PR or the
external manuscripts is claimed.

`FILES.json` identifies this packet's final files by SHA256. The required
repository integrity gate is run separately in a complete clean checkout
of the publication commit; its exact commit, tree, result, and receipt
are recorded in the PR description after that execution. It is not a
mathematical verification of the written infinite proofs.

Full Collatz, vanishing of the escaping-component charge, universal
original-target descent, and exclusion of every nontrivial positive
cycle remain unproved.
