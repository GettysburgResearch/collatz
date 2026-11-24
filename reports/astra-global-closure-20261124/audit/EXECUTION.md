# Shadow rigidity execution receipt

The author executed both final Lean files under Lean 4.34.1, commit 5045d0056413266e57c625dcd7c365b10e377c52, release x86_64-unknown-linux-gnu. The Mathlib checkout was at d13f23b723b8a846827a245b89c10fc7d3f11612. LEAN_PATH comprised its .lake/build/lib/lean and each installed dependency's .lake/build/lib/lean. The compiler loaded existing library oleans; no fresh rebuild of Mathlib or the Lean toolchain is asserted.

| File | SHA-256 of checked source | Result |
|---|---|---|
| research/astra-global-closure-20261124/audit/MemoryShadow.lean | 3c12919535f8951fb04c3f2cd74e2369409189adfc7db8ec03f8b50301b79a54 | lean -j1 -DwarningAsError=true, exit 0, five axiom reports |
| research/astra-global-closure-20261124/audit/ResidueOrbit.lean | f5eb8ff6f62a344b289bbcec5bd2a13f762622a75445b1a25ee641764154a212 | lean -j1 -DwarningAsError=true, exit 0, five axiom reports |

The header of the first file imports Mathlib.Tactic.Linarith, Mathlib.Tactic.NormNum and Mathlib.Data.Rat.Cast.Order. The second file uses only Std. An earlier development compile of MemoryShadow.lean exposed a definitional mismatch in the induction. The final file transports the equality explicitly and the compiler exited successfully. The two sibling .axioms.txt files contain complete final output.

From the repository root both programs below exited 0 and printed identical output.

    python -X utf8 -B research/astra-global-closure-20261124/audit/shadow_checks.py
    python -O -X utf8 -B research/astra-global-closure-20261124/audit/shadow_checks.py

    gcd checks: 3249; past rows: 6; future rows: 5; finite L paths: 64; residue orbit size: 82; quotient orbits: 636

The gcd controls use k=1 through 9 and q=−180 through 180. The congruence controls enumerate all reachable states of 636 explicitly specified modular systems with D<320. They also check the predicted obstruction on four local integers at each admissible D. The finite L stress family is replayed on the ordinary odd map at all intermediate steps for horizons 1 through 64. The finite computations and source reads leave the written unbounded portions at their stated evidence levels.
