# Second checkpoint: exact execution scope

The science commit is `fa23414a7bfdbf829a837416c2aae23e9edcfe3c`, with tree
`2f48358939995fd0f0e1a33aa734ddcb6fe695d2`. It is identical to the locally
validated tree at `6be53d8c42cc5bb885dc965bdaf1c074762a230b`. The API-created
commit identity differs because its authorship metadata differs; the tree
was compared before publication and local branch alignment.

| Evidence | What was actually checked |
|---|---|
| [LEAN_REPLAY.json](LEAN_REPLAY.json) | A fresh root rebuild of all 20 local modules in the requested dependency chains, with strict flags and source hashes. All completed successfully. This includes 13 new modules and the root's complete scaled/postpeak finite-budget consumers. |
| [FINITE_REPLAY.json](FINITE_REPLAY.json) | The cycle spectrum and reflected-operator programs, each run normally and with Python optimization. Each pair produced identical output; the reflected output also matched its retained JSON exactly. |
| [LOCAL_REGRESSIONS.json](LOCAL_REGRESSIONS.json) | The complete repository validator and its enumerated regressions in a clean checkout of the local science commit. |
| [PUBLISHED_REGRESSIONS.json](PUBLISHED_REGRESSIONS.json) | The same complete validation on a clean checkout of the API-published science commit. |
| [DESCENT_AUTHOR_REPLAY.txt](DESCENT_AUTHOR_REPLAY.txt) | The descent author's earlier source hashes and four principal theorem axiom reports. The independent root rebuild above is the stronger retained build evidence. |
| [SCIENCE_MANIFEST.json](SCIENCE_MANIFEST.json) | SHA-256 hashes of the 33 science files changed at this checkpoint, read directly from the published commit. |
| [LEAN_CACHE_FAILURE.json](LEAN_CACHE_FAILURE.json) | An earlier, unsuccessful environment attempt: 13 modules compiled, then AllShift could not find a Mathlib dependency because a partial namespace directory shadowed the later cache. This is not a successful replay. |

The replay driver now merges pinned primary and supplemental Mathlib files
by symlink in its temporary dependency directory. Only Mathlib files are
admitted from the supplement, and every local proof dependency is rebuilt
into a fresh directory searched first. The successful replay followed this
fix. No mathematical source was changed to bypass that missing dependency.

Printed public theorem inventories contain only the permitted standard
axioms `propext`, `Classical.choice`, and `Quot.sound`; some declarations
need a smaller subset. Helper modules without a printed inventory are
checked through their consuming theorem inventories. The source files
contain no admitted proof placeholders. Across the first two checkpoints,
the root independently rebuilt 28 distinct local Lean modules.

[MANIFEST.json](MANIFEST.json) hashes the seven evidence files in the table.
It is an evidence-file manifest, not a self-hashing seal of this README.
The repository validator checks integrity and the specific old regression
programs it enumerates. It does not validate these new mathematical
conclusions. The operator, density, and analytic manuscripts remain written
proofs where stated. External Diophantine theorems and large numerical
verifications were not replayed here. The Collatz conjecture remains open.
