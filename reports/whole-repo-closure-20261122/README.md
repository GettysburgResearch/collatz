# Whole-repository continuation: proof and execution evidence

The [research packet](../../research/whole-repo-closure-20261122/README.md)
contains three distinct results with deliberately different evidence levels.

| Result | Evidence and scope |
|---|---|
| Effective classification of every supplied fixed linear block schema | Written proof, SHA-pinned mathematical review, exact certificate generator, and an independently reviewed checker. The generic theorem is not yet a generic Lean formalization. |
| Exclusion of the repeated odd-gap family `(1,1,4,1,1,1,2)^k (2)^k` for all `k>0` | Sixteen public Lean theorem audits, including the exact gap-path bridge and a uniform proof with no parameter census. |
| Literal-tail carry rule for `1 {2,3}* 2 1` | Seven public Lean theorem audits. The final interval rule retains the explicitly stated lower-grade `IntervalHyp`; universal dispatch is not proved. |
| Ordinary harmonic flow and actual source-collision energy | Written deduction from explicitly pinned analytic inputs, with mathematical reconstruction. No Lean formalization or unconditional absorption theorem is claimed. |

## Individual research-lane executions

The two new Lean modules passed strict compilation under Lean 4.34.1,
commit `5045d0056413266e57c625dcd7c365b10e377c52`, with warnings treated as
errors. Every public theorem was audited. The reported axioms are confined
to `propext`, `Classical.choice`, and `Quot.sound`.

- [Cycle-lane receipt](cycle-agent-lean-receipt.json) and [compiler log](cycle-agent-lean.log).
- [Carry-lane receipt](carry-agent-lean-receipt.json) and [compiler log](carry-agent-lean.log).
- [Mathematical reconstruction](SEMANTIC_REVIEW.md).
- [Independent fixed-schema proof review](REVIEW_FIXED_BLOCK_CYCLES.md).
- [Independent generic-checker review](REVIEW_GENERIC_CLASSIFIER.md) and [review pins](generic-classifier-review-pins.json).

The agent receipts record their actual scratch paths. The carry note's
`carry_receipt.json` and `CarryLanguage.log` are preserved here with the
`carry-agent-lean` prefix. The combined replay records its own header-only
port patch; the original vendor proof sources are included unchanged.

## Combined replay on the published checkpoint

The initial science checkpoint contains the complete fresh-replay driver.
The combined published-checkout receipt will be appended in a separate
reports-only checkpoint after execution; the individual receipts above do
not stand in for that execution.

From a clean, complete checkout, with the pinned built Mathlib revision
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
python -X utf8 -B research/whole-repo-closure-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /a/fresh/directory/outside/the/checkout
```

The driver compiles only the new modules and their required local imports;
checks every new public theorem's reported axioms; runs the independent
integer certificate checker and eight malformed-certificate checks under
both ordinary and optimized Python; regenerates the certificate suite
byte-for-byte; and runs the repository's five default validation commands.
It requires the checkout to remain clean and all recorded input hashes to
remain unchanged. Compiler artifacts and generated sources stay outside
the repository.

The preceding 23-module/140-audit execution remains a separate historical
receipt at its actual mathematical commit. It is not counted as a new
execution of those unchanged sources.
