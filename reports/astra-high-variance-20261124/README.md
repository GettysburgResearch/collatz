# Execution record: unrestricted closing attempts and ordinary comparisons

This report accompanies the [research packet](../../research/astra-high-variance-20261124/README.md).
**Collatz remains open.** The universal closing attempts, written infinite
arguments, Lean results, finite arithmetic certificates and repository
integrity have separate scopes.

## Fresh execution on the published source

**PASS.** The integrating replay ran from 2026-11-24 07:20:47 UTC to 07:20:56 UTC
on the clean complete checkout at source commit
`182a44fac3567d8bf1a450935d64d7ffe52593e6`, tree
`5c537f3a961459473a9898a4a08ac0747787d3a5`, with 478 tracked files.
The head, tree, source hashes and fully clean status were unchanged afterward.

All five new Lean modules compiled into fresh objects. All fourteen named
transitive axiom inventories were subsets of `propext`, `Classical.choice`
and `Quot.sound`. No custom axiom or `sorryAx` was reported. Every module
imports only Std. The compiler was official Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with one worker and warnings
treated as errors. No old project module or Mathlib build was used.

[Complete source-hashed receipt](fresh_replay/receipt.json) ·
[Repository validation receipt](fresh_replay/repository-validation.json) ·
[Repository validation log](fresh_replay/repository-validation.stdout.log).

## Exactly what Lean checked

| Module | Named declarations audited | Formal boundary |
|---|---:|---|
| descent_macro.lean | 5 | Infinite ordinary comparison for the specified five-macro tail, finite entrance, original-floor descent for long initial L runs, and the short-run inequalities |
| arithmetic_equal_clock.lean | 2 | Literal mixed half-script endpoints with equal odd counts |
| rewriting_front.lean | 2 | Arbitrary binary suffix carry and one-digit exchange |
| root_delayed_transversal.lean | 3 | Common-clock maximum, tagged transversal soundness, and settlement advance |
| central_closure.lean | 2 | Strong-induction meeting equivalence for a map fixing one, and paired affine lifts |

The universal shifted-moment identity is a written proof. Its decay is unproved.
The complete all-header/unbounded-run extension, analytic counts, Diophantine
bounds, stationary arguments and inverse optimization remain written results.
They are not promoted to Lean conclusions by this receipt.

## Exact finite controls

All seven scripts passed normally and under optimization, with byte-identical
paired stdout and stderr. The replay checked that none uses Python `assert`
as a guard. A fresh cache location prevented reuse of project bytecode.

| Control | Recorded finite evidence |
|---|---|
| arithmetic_controls.py | 25,797 accepted physical source pairs, 117 padded separation pairs, 8,184 inverse prefixes |
| arithmetic_macro.py | Exact signed prefix/period certificates for both comparison multipliers and their all-length classification |
| central_descent.py | Every positive odd below 256 reaches one; exact reciprocal bound 247/1512; all 35 signed-start cases in the first-paid-prefix argument |
| descent_all_headers.py | All three profile transition families, entrance words and floor inequalities |
| descent_macro.py | Five-macro resets, three entrances, initial-floor inequalities and signed controls |
| descent_paid_runs.py | Free/interior transitions, arbitrary-run decomposition certificates and signed entrance controls |
| rewriting_front.py | 16,383 literal odd rewrites and 484 joint gluing traces |

Individual complete outputs are retained in `fresh_replay`; hashes and command
arguments are in the receipt. The finite controls support only their stated
finite scope and the algebraic certificates used by the written arguments.

## Complete-checkout validation

At the same clean source commit, `python -X utf8 -B tools/validate.py` passed
all five default commands. The optional historical regression bundle was not
rerun. This gate checks repository structure and frozen identities, not
mathematical truth. The successor commit adds these receipts and updates this
report; it changes none of the tested research sources or the replay program.
The PR body records the validation of the exact final published head, avoiding
a self-referential receipt commit.

## Reproduction

[replay.py](replay.py) refuses a dirty source checkout, source mutation, missing
audits, unexpected axioms, optimized-away guards, or differing paired outputs.
Choose an output directory outside the repository that does not yet exist:

```sh
python -X utf8 -B reports/astra-high-variance-20261124/replay.py \
  --lean /absolute/path/to/lean \
  --output /absolute/path/to/new-output-directory
```

The output includes fresh object identities, source SHA-256 values, all stdout
and stderr logs, exit codes, and paired-output comparisons. Compiled objects
stay outside the repository; their exact identities are recorded in the receipt.
