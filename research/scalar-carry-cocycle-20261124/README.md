# Scalar carry cocycle and residue-defect norms

Status: **proposed research, not a proof of Collatz**. Two mathematical routes are developed below. The [Astra continuation](../astra-closure-20261124/README.md) develops stronger actual-source packing and carry theorems and broader cycle exclusions. It also repairs and compiles both original finite Lean kernels under the pinned Lean 4.34.1 toolchain; all ten explicit axiom reports contain only standard axioms. The original written proofs and finite controls remain a separate evidence layer.

## Closing targets

1. [Scalar carry cocycle](SCALAR_COCYCLE.md): replaces bounds on individual carries by an exact amortized bound over every interval, including arbitrary resets. Combined with PR185's actual-orbit packing theorem, this forces polynomially large canonical ternary-phase drawups on any nonperiodic actual odd orbit. It also has a weaker self-contained proof that does not require PR185.
2. [Residue-defect norm](RESIDUE_NORM.md): retains the entire numerical gcd, including prime powers, in a degree-p algebraic norm. Gives a complete arithmetic exclusion of nonstandard mechanical cycles, a proof for eventually mechanical itineraries, and a finite-period theorem for one nontrivial interval-defect class (the last uses an external effective logarithmic-forms input).

Neither covers unrestricted actual scalar phases or arbitrary cycle words. In particular, exponential phase drawups occur on abstract rational phases; the new escape criterion is not an unconditional upper bound on them. Norm estimates for unrestricted residue-defect profiles and noncoprime cycle counts remain open.

## Current repository landscape

Inspected PR metadata and selected relevant proof sources, not a fresh audit of all upstream proof modules. Exact source snapshots:

| PR | Head | Relevant interface and remaining issue |
|---|---|---|
| 182 | f94a2ae1caba9a1857feda892ee1779695eea9d2 | Actual scalar recurrence and triadic equivalence; low-phase returns, arbitrary carries and finite towers; no universal scalar classification |
| 185 | 2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d | Uniform actual injective-segment packing and collision lower bound; matching upper control remains open |
| 177 | 25bf9b95a9404998e8e55aa401773488cd3dd4b8 | All-template/source-pressure bounds, density-free germ criteria; arithmetic continuation remains open |
| 175 | 67664c6bf555bf7f7fcec987acb79500071dce4b | Global cycle-defect budgets, gcd and fixed-source arithmetic; no universal cycle exclusion |
| 178 | 398b3a04da071e96362005792417bd5cf8cc6497 | Full numerical gcd on particular pattern classes; conditional germ route |
| 176 | 81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a | Finite gap insertion and entropy/occupation; all-gap control open |
| 180 | 7cfd911d35382d9d3bc988060ba88ade78a4267e | IID carry/Renyi analysis; actual orbit transfer open |
| 173 | fa0c9e2a2851e6324391e39c17afcb5913185aec | Forced dyadic-band entry; entry does not ensure descent |
| 184 | 366dab89ee9548084ab9b5e4e90ff82abf287a20 | Lower merger certificates; universal cover open |
| 183 | 68345f60a4f757acb42a69a4ac95910f8ce26163 | Arbitrary-debt and independent-block arithmetic; global closure open |
| 186 | 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493 | Literature guide |

## Reproduction and evidence

- CarryCocycle.lean: finite carry-amortization kernel, repaired and compiled in the Astra continuation.
- ResidueDefect.lean: finite residue/evaluation identities, compiled and axiom-audited in the Astra continuation.
- controls.js and controls-receipt.json: exact BigInt finite controls, executed via the available JavaScript execution environment before the first commit. Run the script with Node.js. These are not Lean proof certificates or exhaustive checks.
- [Current replay instructions](../astra-closure-20261124/REPLAY.md) give the exact toolchain and isolated module build. The original compiler outputs and source hashes are in [the carry receipt](../../reports/astra-closure-20261124/carry-lean-receipt.json).
- At the original `beed685ab713923191ae40c9559bf7400298d2d3` checkpoint, Lean and a full local checkout were unavailable and the files were explicitly uncompiled drafts. The later compiler and repository validation receipts apply to the repaired continuation, not retrospectively to that old source tree.

The evidence is scoped: the full mathematical routes below are written proofs; upstream results retain their source qualifications; numerical controls are finite; compilation covers only the named formal declarations.
