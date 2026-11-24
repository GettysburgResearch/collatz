# Publication checkpoints

## Scientific heads

1. `654d0fbb39326a6b8e5f3202e5702c3f15dc9a26`:
   initial partner, synchronization, and reduced-denominator packet.
   Tree `e0fc250aedce8c4ca371630c22599ecc9aba2efe`.
   [Actual remote-head integrity receipt](checkpoint1/INTEGRITY.json).
2. `52beff703fd3ce798c430e5af8199eb58d41bf93`:
   concrete odd-core transport, ordinary coverage-cost theorem, and
   high-complexity rational controls.
   Tree `d3ed05863719de1d07e212f554459d458ee5a506`.
   [Actual remote-head integrity receipt](checkpoint2/INTEGRITY.json).

Both scientific commits were read back from the remote and validated in
complete clean checkouts. The connector-created trees matched the locally
checked trees byte for byte. The last publication commit adds only the
second integrity receipt and this index; it changes no mathematical
source, Lean theorem, or replay program.

## Exact verification boundary

The current source set has 26 audited public Lean declarations: 8 in
CycleCore, 8 in EscapeCore, and 10 in ShadowCore. Checkpoint 1 compiled all
three original modules. Checkpoint 2 recompiled the changed EscapeCore and
added three concrete odd-core transport lemmas. Unchanged theorem bytes
were not redundantly rebuilt.

Both checks used official Lean 4.34.1 with warnings as errors and checked
every public theorem's transitive axiom list. The lists contain only the
standard axioms propext, Classical.choice, Quot.sound. The complete guarded
positive partner statement is formalized; the global counting and
denominator conclusions retain their stated written-proof boundary.

Four exact Python programs passed in normal and optimized execution. The
new coverage program evaluates a combinatorial constant and a rigorous
infinite-tail enclosure. It does not claim bounded source enumeration
settles the conjecture.

The three agents independently developed their assigned lanes and
cross-inspected the stated written arguments. No external peer review,
alternative kernel replay, universal source coverage, or proof of Collatz
is claimed. No repository settings, workflows, or other contributors'
branches or PR states were changed.

## PR

https://github.com/GettysburgResearch/collatz/pull/193
