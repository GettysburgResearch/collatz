# Verification scope

The new packet has four Lean modules and three Python control programs. The coordinator and independent lanes compiled the elementary proofs with Lean 4.34.1, treating warnings as errors. `MinimumFailure.lean` imports the newly built `SourceDeletion` object and defines the actual existential basin of 1. These are not assumptions about a symbolic coloring substituted for convergence.

Every public theorem has a named axiom audit. The only permitted transitive axioms are `propext`, `Classical.choice` and `Quot.sound`. No unchecked proof placeholder, added axiom, or native decision escape is permitted. Private lemmas are kernel checked and included transitively in the public audits.

`replay.py` is the authoritative coordinator replay procedure. It requires a clean complete checkout, builds fresh objects for all four new modules in dependency order, checks that every public theorem is audited, and runs each new control program in ordinary and optimized Python with byte-identical output and zero AST assertions. It then runs the repository validator and checks that the science bytes, commit, tree, and checkout cleanliness remain unchanged. Existing pinned Lean/Mathlib dependencies are reused. Earlier unchanged research modules and upstream PR tables are not claimed as rebuilt by this continuation.

The exact scientific commit, source hashes, command outputs, proof counts and validator receipt will be recorded in the publication follow-up after that real clean-checkout execution. Author and peer checks are separately preserved under `arithmetic/`, `descent/` and `renewal/`; their narrower scopes and exact hashes remain authoritative for those executions.

Mathematical scope: the table, bounded induction, least ordinary disagreement and its basin orientation, finite paired affine rows, and the parameterized first-exit identities are kernel checked. The asymptotic arithmetic-progression consequence and the assembly with the earlier canonical source are written arguments with independent reviews. None of these checks proves a successful descent for every remaining source.
