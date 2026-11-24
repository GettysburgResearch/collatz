# Ordinary inverse-cylinder checks and proof scope

The [scientific note](../../../../research/astra-global-closure-20261124/round5/renewal/README.md) proves its probability and entropy estimates on paper from the PR200 reverse-cylinder bound and the PR146 marked-gap tail. The [Lean module](../../../../research/astra-global-closure-20261124/round5/renewal/OrdinaryAtoms.lean) formalizes the whole signed-row decoder, positivity of every integral inverse at a positive target, the fixed-clock counting bound, its translated carry-localized version, the first-odd carry lower bound, truncation of gap sums and the physical shortcut clock floor. The analytic results and sufficient lower estimate (6) are outside the Lean module; (6) is open.

Lean 4.34.1 `5045d0056413266e57c625dcd7c365b10e377c52` compiled the module directly from source with `-j1 -DwarningAsError=true` and fresh project output, using the compiled package dependencies of Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. Exit status was zero. Seven selected declarations report only `propext`, `Classical.choice` and `Quot.sound`, or subsets. The [compiler output](OrdinaryAtoms.log) records each declaration. The two preceding research inputs and their analytic prerequisites were not formalized in this replay.

The [Python checker](../../../../research/astra-global-closure-20261124/round5/renewal/check.py) uses physical shortcut iteration and explicit exceptions on failed identities. Both `python -X utf8 -B` and `python -O -X utf8 -B` on Python 3.12.14 reproduced [the exact JSON](controls.json) byte for byte. It exhausted all 16,383 chronological words through length 14 starting at an odd input and physically replayed three positive inverse lifts per word. It checked 34,638 fixed-clock height counts and 57,730 real-offset localized counts. It also checked 2,048 translations of ten-clock marked-prefix tests, all 1,330 tested floor implications for observed marks in ordinary sources through 4,096, the partial mark at 37, 24 binomial cutoffs and 15,000 deterministic truncated gap sums.

A separate complete short enumeration through nine odd inputs counts marked words with shortcut length exactly twice the odd count. For odd counts 2 through 9 the symbolic counts are `0, 0, 1, 1, 8, 22, 88, 270`. Every odd starting binary residue was inspected; a terminal odd sentinel may always be selected in the next binary lift. A second census exhausts positive odd unit sources up to 69,684, the common upper cap for all central words at targets 1, 5 and 7 with at most 32 odd inputs. The first witnessed source for target 1 was 3,733 at 29 odd inputs, and for target 7 it was 511 at 15 odd inputs. Target 5 had no central witness in this finite range. These bounds follow directly from \(x\le q(4/3)^p\), so the full counts at the stated targets and depths are covered. They do not estimate the large-depth lower mass.

| File | SHA-256 |
| --- | --- |
| Scientific note | `086edd77d933b3cc3bf5788e44c9e62938142e902d166befe9044a9a019c536a` |
| Lean source | `4d5a52e54196a956233a911a6a03b36a2367dd90f503b3d6041486839e8860da` |
| Lean output | `2a6fb29a99a359fcb036323974ff6785c547578cf029f8ac3222ed687382e6c1` |
| Python source | `b1583abd53255337c900891658086ed0143200514cf49232d152d39d5d53b2ae` |
| Python output | `2d2cd706bf0f9c3b85a6216b3d6cf7f6376184d4ee51e21b05b849edc1da2ff2` |
