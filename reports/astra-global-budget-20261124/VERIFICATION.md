# Fresh execution of the global-budget packet

**PASS for the recorded scope. Collatz and the directed transfer remain OPEN.**

The coordinator executed the packet from a clean, complete checkout of
science commit **174f5ce593473f49962ab253548693183314391e**, tree
**4bb883a89afe58477867420752bad9467ac8fe8f**, on 24 November 2026.
The run started at 11:04:26 UTC and finished at 11:04:46 UTC. Its
[receipt](fresh_replay/receipt.json) contains exact source hashes,
compiler version, dependency commit, commands, output hashes and all
fourteen named axiom audits. The checkout had 623 tracked files and
remained clean with the same commit, tree and scientific source bytes.

## What ran

Three new modules were compiled to a new, previously nonexistent object
directory with Lean 4.34.1, compiler commit
5045d0056413266e57c625dcd7c365b10e377c52. The flags were
-j1, -DwarningAsError=true and -DautoImplicit=false.
Pinned prebuilt Mathlib dependencies at
d13f23b723b8a846827a245b89c10fc7d3f11612 were reused.
This was a fresh compilation of these three project modules, not a
rebuild of all dependencies or of all older repository Lean files.

All fourteen requested declarations printed their transitive axiom
dependencies. Only propext, Classical.choice and Quot.sound appeared.
The replay rejects sorry, admit, new axiom declarations and native_decide
in these sources. No warnings or errors occurred.

Each of the three Python controls ran once normally and once under -O.
All six runs passed. Both stdout and stderr were byte-identical between
the two modes for each source; the AST check found no assert statements.

| Stream | Executed finite coverage |
|---|---|
| Arithmetic | 2,048 positive sources and two-clock controls; 2,046 first-hit decodes; 8,469 numerator candidates; 15,856 primitive lift tuples and companion-precision checks; 64 zero-parent terminals |
| Cost | 1,920 exact carry comparisons; 9 block-residue depths; 17 stopping records; 1,584 cost blocks |
| Renewal | 658 complete words; 1,316 unit-cell memberships; 144 fixed-pair imports with 160 sources; 1,872 coarse-prefix ordinary two-arm lifts |

These counts describe the exact finite controls; they do not test
asymptotic universal claims. The separate reviewers' additional checks
are recorded in their own reports and are not silently included here.

The required whole-checkout command
python -X utf8 -B tools/validate.py --receipt ...
passed. Its [complete structural receipt](fresh_replay/repository-validation.json)
records the integration checks, frozen-identity checks and built-in
validator controls. The optional bounded regression bundle was not
requested or run. Structural success does not certify mathematical truth.

## Replay

Run reports/astra-global-budget-20261124/replay.py from this clean science
commit, supplying --lean, --mathlib, --leanpath-file and a new --output
directory outside the checkout. The driver records the actual runtime,
compiles new objects, audits the named theorems, compares both Python
modes, executes the required validator and checks the complete checkout
and source manifest before and after.

The published follow-up adds these execution records and the later
direct-closing packet. It does not change this packet's fourteen
scientific files. The later packet has its own exact-commit replay.

## Mathematical boundary

The printed Lean declarations establish the finite algebraic, decoding
and counting statements in the three modules. The balanced-word theorem,
global toll argument, S-unit estimates, infinite renewal bounds and
final-refresh addenda are written mathematics. Their independent reviews
are linked from ROOT_REVIEW.md. External probability floors and marked
return estimates remain explicitly assumed inputs. No successful
universal child selector, global cost budget or fixed-state paired
closure has been proved.
