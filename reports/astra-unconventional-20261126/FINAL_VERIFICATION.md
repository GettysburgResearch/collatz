# Final verification of the unconventional pass

**PASS, 26 November 2026. Collatz remains open.** This record covers
actual execution of the final science packet and the precise boundaries
of that execution. The [closing proposal](../../research/astra-unconventional-20261126/FINAL_PROPOSAL.md)
states the mathematical results and the still-unproved universal step.

## Exact checked source

| Item | Value |
|---|---|
| Science commit | `d0611ca619a783e85a533bc695fa4abef5013ce7` |
| Science tree | `59a4eeeacf3b0737add0b3fdb7f76c652f4506c1` |
| Complete tracked checkout | 1,173 files |
| Replay started | 2026-11-26 21:33:00 UTC |
| Replay completed | 2026-11-26 21:37:35 UTC |
| Lean | 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52` |
| Mathlib | `d13f23b723b8a846827a245b89c10fc7d3f11612` |
| C++ compiler | g++ 14.2.0, Debian 14.2.0-19 |

The replay used a new detached complete Git checkout and a new initially
empty directory for every project object. It did not reuse earlier
project `.olean` files. Pinned compiler and Mathlib dependency objects
were reused. A separate checkout of the pinned Mathlib source was
compared against the cached source: all 9,114 Lean/configuration files
matched, with manifest SHA256
`19356a0bbc13f8a6c54ce09ba884b03f2e51aa238e8b83c304d77ac7d6045359`.
This is source provenance, not a rebuild of Mathlib or the Lean compiler.

The complete science checkout and its source manifest remained unchanged
through the replay. [Machine-readable receipt](final_replay/receipt.json)
contains the source hashes, exact commands, time and output hashes,
individual theorem names and transitive axioms.

## Formal scope

**21 modules and 106 public named theorem audits passed.** Every public
theorem was audited exactly once. The driver compiled with
`-DwarningAsError=true -DautoImplicit=false` and rejected unexpected
diagnostics. Its source scan rejected `sorry`, `admit`, explicit
`axiom` declarations and `native_decide`. The only permitted transitive
axioms were `propext`, `Classical.choice` and `Quot.sound`.

| Lane | Modules | Public named audits |
|---|---:|---:|
| Arithmetic, units and cubic fields | 8 | 41 |
| Ordinary sources and signed delays | 8 | 36 |
| Paired arithmetic and transport | 5 | 29 |
| Total | 21 | 106 |

The total includes the first checkpoint's 31 audits. It is a count of
checked declarations, not a claim of 106 independent new mathematical
discoveries. Some kernels re-establish prior physical rows used as
controls, with their provenance stated in the mathematics.

The actual canonical descent, all-precision cofinal address construction,
and the fixed-parent all-earlier-peak delay are among the formal
statements. The global counting estimates, local field arguments,
Bloch torsion applications, infinite Galois statements and mixed-phase
logarithmic-form argument are written mathematics. Compiling their
algebraic kernels does not formally verify those entire arguments.

## Independent executable controls

**Nine normal/optimized Python pairs passed with byte-identical stdout
and stderr.** The selected controls contain no `assert` nodes, so their
guards do not disappear under optimization. They cover initial arithmetic
and inverse constructions, local units, regulator-sign enclosures and
the explicit seven-adic surviving boundary, paired translations, signed
Mersenne rows and index digits, the literal fixed-parent peak-delay
example, the first thirty paid repairs at preassigned delayed parents,
and the independent dyadic distortion certificate.

Decimal evaluations of real special functions in the unit control are
finite numerical tests. The regulator-sign interval and the distortion
certificate use exact rational bounds. Their infinite conclusions
depend on the written tail arguments; a finite sample is not promoted
to an all-input proof.

**The rank-twelve C++ certificate passed both ordinary and
undefined-behavior-sanitized execution**, with identical summaries:

```
R=12 rate=90/100 raised=835391 updates=32674072 max_raised_abs_carry=2684354560 root_weight=190 build_checks=189473786 verification_checks=23090720
```

The independent immutable pass performed 23,090,720 comparisons,
including duplicates. Its finite weight corrections are joined to an
analytic bound for every remaining carry. The stated theorem covers
all carries with normalized relative rank `r=1+b-a` satisfying
`|r|≤12`, and deletes paths exiting that strip. The C++ calculation is
not a Lean proof. Its integer ranges and transition/predecessor formulas
were separately reviewed. [Written certificate](../../research/astra-unconventional-20261126/operator/RANK_PRESSURE.md)
and [root review](SECOND_REVIEW.md) give the full scope.

## Repository integrity

`python -X utf8 -B tools/validate.py --regressions` passed all eleven
commands on the clean 1,173-file science checkout. The receipt records
the same commit, tree and file count before and after execution.
[Complete validator receipt](final_replay/repository-validation.json).
This checks structure, frozen identities and selected finite regressions;
it does not verify Collatz or the written infinite arguments.

## Publication changes and identity

The publication child adds these execution receipts, this report and
the prior PR description. Every science-packet file is byte-identical
to the exact checked science commit, including all Lean, Python and C++
sources and all individual lane proofs. The shifted relative-rank
clarification and the late paid-repair supplement are already in that
checked science commit. [Publication input comparison](PUBLICATION_INPUTS.json)
records the complete packet hash comparison with zero differences.

Before the branch update, the publication gate uses another fresh
complete checkout, compares its packet against the checked source
hashes with no exceptions, and runs the repository validator again.
The remote branch is moved with an expected-head lease and then
reread. The final PR description records the published head and that
gate's outcome.

## Mathematical outcome

The pass supplies a new canonical subprogression descent with exact
upper-certificate cost, exact paid repairs at the first thirty
preassigned delayed parents, all-clock paired counts, an all-carry strip
certificate, actual smaller-source coverage through a bounded number
of even departures, and an ordinary joint obstruction to two bounded
comparison schemes. The arithmetic lane supplies independent cubic
fields, coherent fixed-place identities and regulator corrections.

It does **not** supply the universal original-source selector. The
all-state uniform per-clock pressure extension is refuted by explicit
long low-odd loops, while accessibility from the specified root is
open. The regulator expression still has a finite-prime boundary.
These are the remaining proof obligations; none is hidden in a new
axiom or in a passing compilation report.
