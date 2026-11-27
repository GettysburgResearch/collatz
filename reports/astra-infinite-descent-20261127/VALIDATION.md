# First reproducible checkpoint

The fresh strict rebuild passed all **32 Lean modules** and audited **1,655
declarations**, including private helpers and generated declarations.
Every transitive axiom was one of `propext`, `Classical.choice`, or
`Quot.sound`. No `sorryAx` or added mathematical axiom was accepted.

This is a formal check of the statements actually written. It does not
prove the universal finite-mass estimate, the external premises of named
implications, or the written analytic results.

## Exact scope and receipts

- [Lean replay](CHECKPOINT_01_LEAN.json): a fresh unique object directory;
  all packet modules recompiled with `-j1`, `Elab.async=false`,
  `warningAsError=true`, `autoImplicit=false`, and a four-million-heartbeat
  limit. The generated audit selects declarations by their originating
  module and recursively collects their axioms. The replay ran from
  13:48:29 to 13:51:28 UTC on 2026-11-27.
- [Repository integrity](CHECKPOINT_01_INTEGRITY.json):
  `python -X utf8 -B tools/validate.py`, exit zero, in a clean complete
  checkout with clean state before and after. This checks repository
  structure, pins, links and scoped guards; it is not a mathematics test.
- [Independent finite controls](CHECKPOINT_01_BOUNDED.json): five packet
  programs, each run normally and with Python `-O`; every execution
  returned zero and each normal/optimized output pair was byte-identical.
  The controls cover sparse and moving cycle arithmetic, explicit
  rational cycles, ordinary asynchronous and cone formulas, exact sparse
  inverse clock rows, and four constructed large first-hit integer pairs.

The replayed code tree is
`1f9c41da43600655a730b6e04761aedbb5f7293f`; its local snapshot commit was
`00fa09e9c9231cec04561ef6f353bcefb8efa44c`. Publication adds the receipts
and this explanation to that code. The bounded-control snapshot was
`ef582dffaca86208a562ebf9381fb98d526398a6`; the only code change between
those snapshots repaired the audit wrapper's working directory. Every
scientific source hash is included in the receipts. A GitHub publication
commit can have different author metadata while retaining the exact
validated source bytes; the remote tree is checked separately.

## Pinned trusted dependencies

The compiler is Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`. The receipt includes its binary
SHA-256. Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All eight transitive package
heads matched its manifest, and their tracked sources were clean. The
packet rebuild used the prebuilt dependency objects; it did not rebuild
all of Mathlib or the compiler. A missing dense-subgroup object was
compiled earlier from that exact Mathlib source without tracked changes.

## Failed development runs remain visible

The first unfrozen aggregate run stopped in a then-developing threshold
proof; [its output](DEVELOPMENT_REPLAY.json) is preserved. The first frozen
run compiled all 32 mathematical modules, then failed because the
generated audit file was outside Lean's selected source root. That
[actual failure](DEVELOPMENT_AUDIT_FAILURE.json) is also preserved. The
wrapper was fixed, and the entire compilation and aggregate audit were
rerun in a new clean checkout and a new object directory. Neither failed
run is counted as a successful complete replay.

Several individual integration attempts were killed under memory
pressure. They were not treated as theorem failures or successful checks.
The successful aggregate receipt supersedes them only for its recorded
source hashes. Later source edits require their own checks.
