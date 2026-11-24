# Verification record

The scientific source checkpoint is prepared for a clean complete-checkout replay by [replay.py](replay.py). The receipt will identify its exact commit, tree, source hashes, Lean declarations and normal/optimized Python controls. Until that receipt is recorded, this file does not assert a completed root replay.

The replay compiles both new Std-only Lean modules from source into fresh objects with warnings as errors, audits each requested declaration against the three standard axioms, runs all four finite controls in normal and optimized Python, and runs the complete repository integrity validator. It does not formally check the written analytic or topological proofs, recompile upstream research packets, or establish unrestricted Collatz convergence.
