# Ordinary descent verification

The source directory is [closing/descent](../../../../research/astra-global-closure-20261124/closing/descent/README.md). The prior input for the five-letter partition is PR192, commit d2081d1cd2410e6004eaee9f9b13c5553afaf3f4, file research/astra-closure-attack-20261124/DESCENT_EXTENSION.md. Its SHA-256 is e902faffe7ee584ad354119d7809e0a4b663a12373fe7d2244dac5c84cb370d1.

## Strict Lean evidence

The compiler is Lean 4.34.1, x86_64-unknown-linux-gnu, commit 5045d0056413266e57c625dcd7c365b10e377c52. The executed binary was /workspace/scratch/ae8b5ba301f1/lean_env/lean-4.34.1-linux/bin/lean. Each checked module used -j1 -DwarningAsError=true, Std, and the listed local imports. The signed-lifting dependency CycleShadows.lean has SHA-256 05ef6b77b2ce9d571c598e5a0e4a526be3412b844349476ec72408b0bf145e99. Its olean and the compiled ResidualDescent.olean were available in /tmp/collatz192-lean through LEAN_PATH. The [long-past receipt](longpast-receipt.json) independently rebuilt both import sources from their exact frozen bytes before checking LongPast.

| Module | Selected public declarations | SHA-256 | Kernel outcome |
|---|---|---|---|
| SustainedResidual.lean | sustained_residual | 951817b99d9ab64b21520ccc4cc1c336c3822d02f96a536c157dc75188dc2920 | Exit 0, propext and Quot.sound. [Output](sustained-lean.txt) |
| ResidualDescent.lean | residual_descent | b5f149855866419b771e49127bdaabd1cb5749ec7d6f3b6091f3fb54bf1ccc98 | Exit 0, propext and Quot.sound. [Output](residual-lean.txt) |
| HeightPartner.lean | height_partner, no_predecessor_55, witness_55 | e908f6c8738f06754ebc3b76b7deac0335e700a2e0ffbddee7314f1cd0a1ec6f | Exit 0. height_partner also uses Classical.choice, no_predecessor_55 uses propext and Quot.sound, witness_55 has no axioms. [Output](height-lean.txt) |
| PastCylinder.lean | past_descent | 2f3904caf3ea257820b1328673a1c4745202b7f89a9723639eb055618b569fe3 | Exit 0, propext, Classical.choice, Quot.sound. [Output](past-lean.txt) |
| LongPast.lean | isolated_lights | 1566f437118187de95710b11ec2b3eef35f74e660772cd8d72cade8e3e030cb2 | Independent separate strict exit 0. [Output](longpast-lean.txt) |

These five modules contribute seven selected declarations. The seven-past theorem is an alternative clock on a cylinder already covered by PR192.

For a fresh replay, build CycleShadows.olean in a new temporary directory with the compiler's -o option. Set LEAN_PATH to that directory, compile ResidualDescent.lean to ResidualDescent.olean there, and run each remaining source with the same flags. Kernel output inventories concern the named statements and their transitive dependencies.

## Ordinary controls and written results

Both python -B controls.py and python -O -B controls.py ran successfully with identical stdout. The source SHA-256 is 950a7f1713be9d5de8d608a8651fff197ecdc4870749fd0278afad44c847a61e. Controls replayed 60 LPP cases, 84 two-gate cases, two ordinary overlapping seven-past alternatives, 48 explicit height partners and all 54 possible smaller starts for 55. They independently recomputed the three-letter ternary image and original 16-word partition. [Control output](controls.txt)

The main README SHA-256 is fc1822fe314b58b09595ba92fd56ee8664d3613223c0ae0cfc1bdb6c13daa695. The independently reviewed free-clock count in HEIGHT_CLOCKS.md has SHA-256 280349f0b49d6ca4be3421ec0ca4bcb56c740e08eff7d613710172fb9e423165.

The six old prefix rows retain PR192's mixed evidence status. Their finite-language partition, positive-height ordinary density, witnessed power-of-two subfamilies, free-clock density order, and local infinite-language forcing are written proofs. The density and finite-memory results are not formalized as additional Lean declarations. The [independent reconstruction](INDEPENDENT_REVIEW.md) checks exact arithmetic, trajectory transfer, original floors, scope and overlap. The separate [long-past source note](../../../../research/astra-global-closure-20261124/closing/descent/LONG_PAST.md) records its own nested history, comparison, and earlier-work assessment.
