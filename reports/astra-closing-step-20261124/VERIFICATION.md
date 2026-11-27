# Fresh execution of the direct-closing packet

**PASS for the finite formal and computational scope. The universal
directed implication remains OPEN.**

The coordinator ran the new packet from the clean, complete checkout of
science commit **f872f7ad1b8ce809875198d6b9a1d5125e87bc77**, tree
**71ee679262912d900c85a16a91ba30253761048e**. The run on 24 November
2026 lasted from 11:32:23 UTC to 11:32:27 UTC. The checkout contained
656 tracked files and remained clean, at the same commit and tree,
with the same four scientific source files before and after execution.

The [full receipt](fresh_replay/receipt.json) records every command,
source hash, output hash, runtime version and named axiom audit.
The [whole-checkout structural receipt](fresh_replay/repository-validation.json)
records the required validator's actual execution.

## New module and finite controls

CanonicalSource.lean was compiled to a new object directory using
Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52,
with -j1, -DwarningAsError=true and -DautoImplicit=false.
It imports Std. Existing Lean standard-library objects were reused;
no project object from a prior compilation supplied its proofs.

The four printed declarations were:

- Collatz.CanonicalSource.run_add
- Collatz.CanonicalSource.all_odd
- Collatz.CanonicalSource.normalized_reaches_child
- Collatz.CanonicalSource.adjacent_mersenne

Their transitive dependencies contain only propext, Classical.choice
and Quot.sound. The source contains no sorry, admit, new axiom
declarations or native_decide. Compilation had no warnings or errors.
The [compiler output](fresh_replay/lean-descent-CanonicalSource.stdout.log)
records the individual audit lists.

The finite checker passed normally and under Python -O with
byte-identical stdout and stderr. It contains no assert statements.
It verifies 5,556 canonical-source paths, 1,360 dyadic endpoint
identities, 117 adjacent-Mersenne parameter controls, 50 terminal
family examples, the ten specified first hits and the exact base
inequality used for the infinite family. These are overlapping finite
identity checks, not a count of independently established universal
theorems. The large-j extension is a written monotonicity argument.

Both independent reviewers additionally replayed the upstream finite
table at its frozen PR193 commit. They checked 291 leaves over period
995328, 3,483 letters and 189 extra edges, recovering the exact maximum
input ratio 20970919/122875. Their reports pin the original Lean and
checker blobs. This upstream replay is separate from the new module
and is not represented as fresh compilation of the upstream theorem.

## Complete checkout and earlier packet

python -X utf8 -B tools/validate.py --receipt ... passed on the actual
clean 656-file checkout. Its structural, frozen-identity and validator
self-controls all passed. The optional regression bundle was not run.

The preceding [fourteen-declaration packet's execution record](../astra-global-budget-20261124/VERIFICATION.md)
pins its own clean science commit
174f5ce593473f49962ab253548693183314391e. All fourteen scientific file
hashes from that receipt were checked unchanged before preparing this
commit. The two recorded runs therefore cover eighteen named
declarations in four new Lean modules and four normal/optimized
Python control pairs. They do not constitute a whole-repository Lean
build.

This follow-up changes only execution records. The scientific source
manifests are compared again before the remote draft branch advances.

## Scope

The new Lean module proves physical path identities on natural numbers.
The least-counterexample extraction, the Evertse application and the
all-family exclusions are reviewed written arguments. The finite
table remains a precisely pinned dependency. No compiled declaration
asserts the unproved universal child-component contraction or the
Collatz conjecture.
