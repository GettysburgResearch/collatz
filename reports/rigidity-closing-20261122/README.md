# Published rigidity-closing checkpoint: exact replay

The research packet was replayed from the actual GitHub science commit
`e05cda51a2c04f08c9ba11bc1ec9fd797e953c42`, tree
`7d7adb511efb96ec71a4d3b493abbdf5720546ae`.
The complete checkout contained **690 tracked files** and was clean before
and after execution. The later report-only commit preserves every checked
source byte.

[The exact receipt](PUBLISHED_REPLAY.json) is copied byte-for-byte from the
external build. Its SHA256 is
`3463250c6e5651c600125f18daf0c187d4512c3d00beed2c998a1b395d8e62ba`.
All 17 command outputs are preserved byte-for-byte under [logs](logs).
The absolute log paths in the original receipt describe the actual run;
the corresponding archived logs have the same basenames and SHA256s.

## What ran

- Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- A clean isolated build of the **one required existing module**,
  `OriginalSourceEntropy`, followed by both new modules.
- **18 new public theorem audits:** eight `CanonicalRetracing` and ten
  `CyclotomicBlockExclusion` declarations. All use only the allowed
  standard kernel axioms. No admissions, custom axioms or native proof
  shortcuts were accepted.
- **21 inherited-module audits**, recorded separately and never included
  in the count of new results.
- Both small exact certificate scripts, once normally and once with
  `python -O`. These preserve one actual ordinary 36-gap source, the
  complete cyclotomic factors, the Bezout805 identity, the targeted
  15-by-15 resultant, two structural profile controls, and all thirteen
  rotation identities. Four deliberately damaged controls are rejected
  in each mode.
- `python -X utf8 -B tools/validate.py` from the clean complete published
  checkout.
- Final source hashes, compiler-source copies, HEAD, tree and clean
  status checks. All 17 commands exited zero.

## Scope

The finite scalar and polynomial theorems are Lean-checked. The actual
Markov-law interpretation, uniform total-variation identity, entropy
limit, and all-parameter parity-word correspondence are written and
independently reviewed mathematical arguments. The ordinary harmonic-flow
construction retains its stated external analytic qualifications.

The certificate scripts check their exact finite controls. They are not
a cycle census and do not verify an asymptotic theorem. The repository
gate checks integrity, not mathematical truth. No unrestricted cycle
exclusion, inverse branching onset, or full Collatz conclusion is claimed.

Start with the [research packet](../../research/rigidity-closing-20261122/README.md)
for the mathematics and the precise remaining closing targets.
