# Round 13 execution and mathematical scope

24 November 2026. Research parent: PR182
`cbec52dde5bed390a693310dd04e911033ba0cc9`, tree
`84ee1bbd745faa374e04b4424849d93260c9d4e5`.

**Collatz remains open. The finite Lean sources listed here were actually
compiled.** Written infinite arguments, finite exact arithmetic, a compiler
run, an axiom audit, and repository integrity checks have separate scopes.
The [scientific packet](../../research/astra-round13-20261124/README.md)
states the mathematical results and remaining obligations.

## Current follow-up verification

After publishing `cf1f04db7f9f84d3a31bfccf2546431b711312d0`, the three
original attack authors reviewed PR192–194 at their separately pinned
heads. The coordinating agent reconstructed the new fiber reduction,
unimodular clock construction, complete top-factor cancellation and cyclic
entropy calculation. [The follow-up review](ROOT_FOLLOWUP_REVIEW.md)
records the exact source hashes and remaining boundaries.

The updated [FOLLOWUP_LEAN_REPLAY.json](FOLLOWUP_LEAN_REPLAY.json) is a
second fresh private-directory build of the complete scoped source set,
now including `GuardedPredecessor.lean`. **All 16 source compilations
passed; all 82 named axiom audits contain only the standard axioms.**
There are now 49 new theorem targets. The three added results are the
general actual predecessor identity, its strict size saving for at least
two reversed odd steps, and the explicit five-clock LS3 specialization.
The original 15 source files are byte-identical to the first successful
build; their proof statements were not changed in this follow-up.

[FOLLOWUP_CONTROLS_REPLAY.json](FOLLOWUP_CONTROLS_REPLAY.json) records
**20 successful executions**, ten programs in normal and optimized modes,
with identical paired output. The added standard-library mixed-top
fixture replays all 17,160 literal odd gaps, checks primitive clock gcd 6,
complete numerical top-factor divisibility, full return, and the surviving
18,127-bit reduced denominator. Its minimum floor is 90,269. All earlier
finite programs were also replayed by the updated runner.

The new critical-summable residual set, the uniform cyclic entropy
deduction, the arbitrary-floor full-top-absorption family, and the
least-source consequence of the guarded predecessor remain **written
proofs**. Their scope is not included in the 49 Lean theorem targets.
No original Lean sources from PR192–194 were rebuilt by this follow-up.

## First checkpoint: consolidated source replay

[LEAN_REPLAY.json](LEAN_REPLAY.json) records a fresh, sequential replay of
15 source files from this checkout in one new private build directory.
It retains each command, SHA-256, elapsed time, exit code and complete
stdout/stderr. All 15 commands exited zero with warnings treated as errors.

- Lean 4.34.1 release, compiler commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, with its already built
  package dependencies. The shared toolchain was used read-only.
- Compiler flags: `-j1 -DwarningAsError=true`.
- Local modules were copied from the repository and compiled afresh in
  dependency order. No author-produced local `.olean` was used as a
  substitute for compiling those sources. Existing Mathlib/package build
  artifacts were used; Mathlib was not rebuilt from source in this pass.
- The named transitive audit printed **79 declarations**: 46 new theorem
  targets, 24 Round 11/12 declarations (including five definitions), and
  nine selected upstream results. This is not a count of all imported
  library declarations or all theorems in the repository.
- Every printed axiom is among `propext`, `Classical.choice`, `Quot.sound`.
  The two closed dyadic integer certificates print empty axiom sets and
  use `decide +kernel`. No `sorryAx`, extra mathematical axiom or
  native-decision axiom appears in any audited dependency set.

| Source group | Fresh compilations | Named audit | Exact formal scope |
|---|---:|---:|---|
| ShellCover, OffsetDescent, ForwardSection | 3 | 9 selected upstream results | Existing physical maps, affine descent and forced marked-section interfaces |
| AffinePairReturn, PairedLanguage, MarkedHalfReturn, AuditBandReturn | 4 | 14 theorems | Literal pair returns, finite accepted scripts, positive smaller marked partner, and `collatz_iff_residual_marked` |
| CycleBudget, IntegerClock, DyadicSubtotal | 3 | 10 theorems | Finite rational product inequalities, integer clock/carry implications, and two closed integer comparisons |
| CycleNormComplete, HighFloorNorm | 2 | 20 theorems | Polynomial identities, residual numerical gcd bounds and a conditional integer denominator inequality |
| DefectCover | 1 | 2 theorems | Literal shortcut intercept bound and finite rational aggregation |
| RepetitionWindow, PhasePacking | 2 | 24 declarations | Supplied finite affine paths, clock/carry identities, canonical differences and finite endpoint uniqueness |

### Round 11/12 repairs and earlier failures

The original broad-import attempts were incomplete under resource pressure;
one narrowed preliminary Round 11 run timed out. Those attempts are not
passes. The final replay above independently compiles the exact tracked
sources, including their updated audit commands and headers.

Round 11 now uses five explicit imports instead of `Mathlib.Tactic`; its
mathematical proof bodies are unchanged. Its 16 declarations are printed.
Round 12 uses explicit imports, replaces two nonexistent multiplication
lemma names with `mul_le_mul_iff_left₀`, removes two redundant `ring`
invocations after `field_simp` had closed the goals, and renames an unused
hypothesis `_hy`. The hypothesis and all eight theorem statements remain
the same. Preliminary Round 12 runs returned errors before these repairs;
only the final zero-exit run is claimed as successful.

The old authoring-session notices in the two README files are preserved
below dated Round 13 updates. They accurately describe their earlier
sessions, not the current compiler status.

## What has not been formalized

- The marked-domain densities `16/31` and `32/63`, the rational infinite
  reset, and the linear-horizon obstruction are written proofs.
- The forward-invariant-set dyadic count, infinite summation, recurrence
  identification with binomial tails, logarithmic consequences and full
  contracting-phase classification are written proofs. The kernel checks
  the stated recurrence integers, not that entire mathematical chain.
- The arbitrary-word grouping, rational realization, prime-power
  classification, clock approximants and arbitrary-high-floor family
  construction are written proofs. `HighFloorNorm.denominator_bound`
  takes the numeric specialization hypotheses explicitly.
- The arbitrary-defect cover's cyclic expansion, common-denominator
  congruence, boundary span and two-logarithm argument are written proofs.
- Barina's verification below `2^71` is an external published input when
  extending the high-floor cycle classification to every nonstandard
  cycle. That large computation was not replayed or formalized here.
- No alternative Lean kernel, universal residual convergence theorem,
  universal economical word cover, or all-cycle exclusion is claimed.

## Exact finite controls

[CONTROLS_REPLAY.json](CONTROLS_REPLAY.json) records **18 successful
executions**: nine programs, each in normal and optimized Python modes.
Every pair produced byte-identical stdout. SymPy 1.14.0 is used only by
the affine-ray program; the remaining arithmetic programs use Python's
standard library.

| Program | Recorded finite coverage |
|---|---|
| band_controls | 144 ordinary paired-return sources, with rising clocks through 98 and return depth through 7; finite mixed-script densities |
| cycle_budget | Exact shells 69–511, rational geometric tail bound, and three phase divisibility examples of lengths 512, 1025, 4097 |
| prime_power_controls | 95,266 nonperiodic and 327 repeated words in the prescribed positive-clock prime-power range through total clock 18; 33 exceptional-family shifts |
| affine_ray_controls | 1,431 specified rays and 17,172 specialized complete denominators |
| high_floor_control | 3,826 arbitrary-prefix templates and two 1,224-odd-step rational fixtures with 1,446-bit reduced denominators |
| cover_control | 95,474 disjoint covers on 585 primitive positive rational necklaces through shortcut period 12; 36,606 mixed expansion/contraction cases and 60,881 empty-defect cases |
| horizon_controls | All 345 integer parameters `T=6..350`; physical marked condition, rejection, strict height and independent-clock disjointness |
| repetition_controls (Round 11) | 3,432 paths, 53,868 repeated windows, 1,548 fixed-source tests and 48 cap replays |
| phase_controls (Round 12) | 24,703 actual edges, 17,030 candidate decisions, 113,588 past-residue checks, and the stated confined graph of 2,509,976 odd vertices |

The coordinator found assertion-only checks in the two newly supplied
prime-power and affine-ray programs and replaced all seven assertions by
explicit conditional exceptions before the consolidated replay. Their
optimized executions now perform those checks. The original author
source hashes are not relabeled as the updated ones; the consolidated
receipt and source manifest identify the final bytes.

The unchanged Round 12 Python program emits the historical scope text
`finite exact arithmetic only; Lean not run`. That correctly describes
what this Python program executes. The separate Lean receipt above is
the evidence for the now-checked finite module.

## Independent review and provenance

Six GPT-6.2 Astra agents worked in two waves, with three concurrent workers
at a time. Author work and cross-review are separated. These are in-session
agent reviews, not claims of external human referee acceptance.

- [Semantic review](SEMANTIC_REVIEW.md) reconstructs the literal map,
  quantified marked reduction, all 508 binomial recurrence rows and the
  actual formalization boundaries. Its requested nonempty/high-set
  qualification was applied to the synthesis README.
- [Second-wave review](SECOND_WAVE_REVIEW.md) reconstructs the arbitrary
  defect denominator proof and the independent-clock horizon obstruction.
- [Cross-review](CROSS_REVIEW.md) reconstructs marked densities and the
  full-denominator cancellation. Its early marked-source pin is historical;
  the semantic review and consolidated replay bind the final marked source.
- [Mahler source review](MAHLER_REVIEW.md) records the scope of PR190's
  binary substitution argument, without claiming an arbitrary-word bridge.
- The `AUTHOR_*` files preserve individual compiler evidence. The
  consolidated replay is the current exact-source compilation record.

Gouillon's primary 2006 paper was opened and Corollary 2.3 on printed
page 128 checked directly. Its lower bound for `log|Lambda|` is linear in
`h`, with `h=O(1+log(p+1))` for the fixed inputs 2 and 3 and `A=O(p+1)`.
This supports the polynomial lower bound used in DEFECT_COVER.md. It is
an external theorem, not a newly Lean-checked dependency.

## Reproduction and checkout integrity

From the repository root, with the pinned compiler and a built pinned
Mathlib checkout:

```bash
python -X utf8 -B research/astra-round13-20261124/checks/replay_lean.py --lean /path/to/lean --mathlib /path/to/mathlib --receipt /tmp/round13-lean.json
python -X utf8 -B research/astra-round13-20261124/checks/replay_controls.py --receipt /tmp/round13-controls.json
python -X utf8 -B tools/validate.py --receipt /tmp/round13-checkout.json
```

The final command requires a clean, complete checkout and validates
repository structure and frozen identities. It does not establish the
mathematical arguments. The base `cbec52d...` passed all five default
commands in this session before the edits. Exact new-commit publication
receipts are recorded separately after those commit identities exist.

The staged whitespace lint reports an extra blank line at EOF in each of
the frozen `CycleNormComplete.lean` and `HighFloorNorm.lean` files. Those
two source bytes are retained to preserve their author/review/compiler
identities. This lint is not recorded as a pass; neither diagnostic is a
Lean compilation warning or a proof error.
