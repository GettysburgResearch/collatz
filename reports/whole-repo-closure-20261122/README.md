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

**PASS on the actual published mathematical commit**
`54af6f804ed432573762f1fe3d08e9909e1f5e47`, tree
`1d83b3ccc09957412767083ba4470013111a933f`.

The fresh replay ran from **00:11:47 to 00:12:24 UTC on 22 November 2026**
in a clean, complete detached checkout with 439 tracked files. It compiled
five modules: the three required imports `ShellCover`, `WitnessGlobal`, and
`WitnessSynthesis`, followed by the two new modules `CarryLanguage` and
`FixedBlockDenominator`. All **23 new public theorem audits** passed under
the axiom allowlist above. The four private carry helpers are included
through the public theorem dependency closures, not counted as additional
public audits.

The independent certificate checker accepted all eight supplied schemas and
rejected all eight deliberately corrupted certificates, both under ordinary
Python and under `python -O`. Regeneration matched the committed certificate
bytes exactly. All five default repository validation commands passed.
The checkout remained clean and all 19 recorded input hashes remained
unchanged.

- [Complete published replay receipt](published1-complete-replay.json).
- [Actual command logs](published1-logs/), including the
  [carry audit](published1-logs/10-CarryLanguage.log),
  [cycle audit](published1-logs/11-FixedBlockDenominator.log), and
  [repository gate](published1-logs/15-repository-validation.log).
- [Exact generated module-header differences](published1-module-port.patch).
- [Source continuity](published-source-continuity.json): all 19 new replay
  inputs and all 39 inputs from the preceding published replay retain their
  checked hashes. This evidence is appended in a reports-only checkpoint.

The pre-publication integration review caught and corrected an overly broad
cache sentinel in the new driver. The driver now checks the required
`Mathlib/Tactic/IntervalCases.olean`, rather than requiring an unused
top-level `Mathlib.olean`. The actual published replay above passed on its
first execution; no unsuccessful compiler attempt is hidden by this report.

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
