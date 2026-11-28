# The positive-predecessor dependency: authenticated source, incomplete fresh replay

**SOURCE-QUALIFIED external input. No new formal verification of the three
announced predecessor theorems is claimed here.** This distinction matters:
the semiprime and collision reductions use positive lower density to turn a
single ordinary counterexample into a population obstruction.

## What was obtained and checked

The original [ProofAtlas interface](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html)
links a thin source release and its exact public supporting archive. Both
were downloaded from their original HTTPS locations and authenticated:

| Input | Bytes | SHA-256 |
|---|---:|---|
| [Predecessor extension v1.1](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/positive-lower-density-collatz-predecessors-v1.1-source.zip) | 55,103 | `55ceb4df0cca17ae728dc65b30bf5077000e1b47f2dc322454eea9f637ac75b3` |
| [Positive-density baseline v2.1](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/positive-density-log-time-collatz-v2.1-source.zip) | 914,975 | `23f5cac4d66e696401144658752cf180a13ce70373a122f00693e1e1fe969c1f` |

The source-provided assembler authenticated the baseline's release identity
and every selected source digest, resolved the transitive imports, and
created a fresh assembly. Its independent assembly verifier passed. The
result has **388 project files in the public interface import closure**,
plus the separate release audit, for 389 Lean sources. These comprise 377
baseline modules, ten extension implementation/support modules, the wrapper,
and the audit. All 404 assembled source/configuration/notice/tool files were
then rehashed independently against the assembly manifest.

The [intake receipt](../../reports/astra-collision-factor-bridge-20261128/external/predecessor-source-intake.json)
and [complete assembled input inventory](../../reports/astra-collision-factor-bridge-20261128/external/predecessor-assembled-inputs.json)
retain these identities. The supporting source revision is
`830b9d3f38f2a8da8cd921bf6a9310dd69336fd0`.

## Statements and map convention actually inspected

The wrapper `CollatzPredecessorDensity.lean` states:

1. Every positive target not divisible by three has a predecessor set of
   positive lower natural density.
2. One ordinary counterexample implies a positive-lower-density set of
   nonconvergent starts.
3. Proportions of convergent positive starts arbitrarily close to one at
   arbitrarily large cutoffs imply convergence of every positive start.

Its map is the **ordinary** map, with odd step \(3n+1\), and counts are
strictly below a natural cutoff. The separate audit restates these
statistical quantifiers directly and prints the actual root axiom closures.
It also checks that the unproved universal conjecture declaration is not
imported. Source inspection of this code is distinct from executing it.

For a shortcut target \(v\) prime to three, our proofs apply the ordinary
target result at \(2v\). Every ordinary visitor of \(2v\) is a shortcut
visitor of \(v\), after combining the odd step with the following halving.
This avoids silently changing the formal interface's map convention.

## Historical verification versus this pass's experiment

The original release pins Lean `4.30.0-rc2` and Mathlib
`5450b53e5ddc75d46418fabb605edbf36bd0beb6`. Its reproduction documentation
reports a successful eleven-module extension compilation and three-root
audit against authenticated but reused supporting objects. It explicitly
discloses the limitations of the earlier versus later baseline object
inventories. That is the author's historical evidence, not a fresh replay
performed in this pass.

The available environment here is Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. An unchanged-source compatibility
experiment freshly compiled the first seven project modules, then exceeded
the 180-second per-module wall limit at `Erdos1135.StoppingTime`. No proof
source was edited, no announced theorem root was reached, and no completed
root audit was produced. The experiment therefore **does not establish**
compatibility or correctness of the full development in the newer environment.
A timeout is not a mathematical counterexample or a rejected proof.

The next reproducibility step is a complete assembly build and audit in the
original pinned environment, or a separately documented successful migration.
Until then, the positive-predecessor theorem remains the named external
input in this packet. Its source identity, exact statements and map
normalization have been checked; a fresh complete theorem rebuild has not.
