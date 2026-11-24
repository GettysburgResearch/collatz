# Descent execution evidence

Base commit 07aa5124f7ca482b6665d61355fac0af5f6e55b2. Lean 4.34.1, binary /workspace/scratch/ae8b5ba301f1/lean_env/lean-4.34.1-linux/bin/lean, commit 5045d0056413266e57c625dcd7c365b10e377c52. Every selected declaration below compiled with -j1 -DwarningAsError=true. The local compile used LEAN_PATH=/tmp/collatz192-lean with the frozen CycleShadows.olean and ResidualDescent.olean. TwoLight.olean was built with the same flags before checking ResetTiles. The separate packet-wide run rebuilt the complete import chain from source in a fresh directory.

| Source | SHA-256 | Checked declaration and resulting standard axioms |
|---|---|---|
| TwoLight.lean | fdddc3ede29502691ea2a27354abdd8b09faee98fc0f338bb3b970c9cf141964 | TwoLight.two_light_descent, propext, Classical.choice, Quot.sound. [Output](two-light-lean.txt) |
| ResetTiles.lean | 78a285a2933ef970f4f0f91d64e169f5c42ec3fe7b7fb1575c13e0e6ac3f69a3 | ResetTiles.tile_descent, propext and Quot.sound; ResetTiles.catalog, no axioms. [Output](reset-tiles-lean.txt) |
| LoopCone.lean | a468fc36f293b3314342558ef438f6de46d7baf1ff0dc87c3571a9cf80a93c60 | LoopCone.loop_exit_descent, propext, Classical.choice, Quot.sound. [Output](loop-cone-lean.txt) |

The Python replay used python -B controls.py and python -O -B controls.py, with identical stdout. It reconstructed all six catalog carries, 432 ordinary three-tile paths, 478 ordinary parameter-cone sources and four sign-changing seed carries, each checked against positive ordinary lifts. It also verified the worst three-paid normalized slope bound for the infinite-family reset obstruction. [Controls](controls.txt)

The six-tile all-position corollary, finite phase extensions, all-sixteen-header application and non-reset obstruction are written statements. The signed-seed numerics and actual finite controls support those arguments. No universal ordinary L/P descent is claimed. [Main proof](../../../../research/astra-global-closure-20261124/round3/descent/README.md) · [Avoidance scope](../../../../research/astra-global-closure-20261124/round3/descent/RESET_AVOIDANCE.md)
