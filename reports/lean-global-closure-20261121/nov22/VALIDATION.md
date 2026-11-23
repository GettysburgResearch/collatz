# Published-checkout validation: 22 November continuation

## Actual scientific checkpoint

Commit: **`75e4c3be98db839646ffbb76fc0ac33649747c99`**

Tree: **`c3346d334a17877e5f54fd2f5f7663656227d54b`**

The complete checkout contained **430 tracked files** and was clean before
and after the executions below. The remote branch was re-queried and matched
this commit before the replay. The commit belongs to draft PR175 on
`research/lean-global-closure-20261121`.

## Fresh core Lean build — PASS

The actual command was:

```sh
TMPDIR=/workspace/scratch/957bb0caa6f2/wide-tmp \
python -B research/lean-global-closure-20261121/build_wide.py \
  --lean /tmp/collatz-lean-runtime/lean-4.34.1-linux/bin/lean \
  --output /workspace/scratch/957bb0caa6f2/nov22-evidence/core-build-75e4c3b \
  --receipt /workspace/scratch/957bb0caa6f2/nov22-evidence/source-build.json
```

It ran from the clean complete checkout of the displayed commit. The output
directory was newly created and contained no precompiled project objects.
`LEAN_PATH` contained only that fresh output directory. All eight vendored
foundation sources passed their stored SHA256 and Git-blob checks before
compilation.

- **19 of 19 source invocations passed.**
- Lean **4.34.1**, compiler commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Every source invocation used `-j1 -DwarningAsError=true -DautoImplicit=false`.
- **126 axiom reports**, including **55** from the three new modules.
- The union of all reported dependencies is exactly
  `Classical.choice`, `Quot.sound`, and `propext`.
- No `sorryAx` or custom Collatz axiom appears in a reported dependency closure.
- All 19 receipt-bound source hashes match the actual checked checkout.
- Total compiler time recorded across the invocations: **32.503 seconds**.
- **Mathlib was not required.**

The counts identify audited declarations, including supporting statements;
they are not a claim of 55 independent mathematical discoveries.

| New module | Axiom reports | Actual source SHA256 |
|---|---:|---|
| `SignedCarry` | 31 | `0729e2be27118d2f3c325b1f485a18c01da09b0e360d84b40effd851a2b0379f` |
| `MergerClockRigidity` | 22 | `4f7bff5ea23a750a3c784e12012c1ace0b862daac1f1301a4c1af1065355b497` |
| `FiniteProfileDrift` | 2 | `055d9d3fa252d3287c1eb8fa11e4fcd76c517008772596af37b9271ebc220d74` |

Full evidence: [compiler receipt](source-build.json) and
[parsed declaration-by-declaration audit](axiom-audit.json).

Compiler receipt SHA256:
`c5af309502421c0d6e187cf57ca75b2ecd667d6800c33e1b1a6b124098fc781f`.

## Complete repository gate — PASS

The actual command was:

```sh
python -X utf8 -B tools/validate.py \
  --receipt /workspace/scratch/957bb0caa6f2/nov22-evidence/repository.json
```

All five required commands passed, including the validator's own bounded
self-tests. The complete checkout identity was unchanged. The optional
`--regressions` bundle was not requested or run.

Full evidence: [repository receipt](repository.json), SHA256
`574dc639406b4cfd2fd4f5d7c457c59918113b5b59e66a41cd7a3b7866836dd0`.

This gate checks repository integrity and scoped finite controls. It is
separate from Lean execution and from mathematical review of written proofs.

## Written mathematics and independent review

The three formal modules retain the displayed hypotheses of their statements.
In particular the signed compiler's successful interval rule still takes its
lower-grade induction hypothesis and its actual interval guard explicitly.
The compiler's exhausted-word alternative is not replaced by a convergence
conclusion.

The real-asymptotic excessive-profile theorem is **written mathematics**.
Its finite ordered-ring row algebra and finite ordinary lifting bridge are
kernel checked. Its limits, modular coverage, and application of Monks's
published arithmetic-progression theorem are not presented as Lean results.
The elementary mixed-modulus proof and the arbitrary-modulus imported input
are distinguished in the notes.

Independent scoped semantic reviews:

- [Signed carry and complete-source transport](SIGNED_CARRY_REVIEW.md).
- [Affine merger rigidity and complete residue-class propagation](MERGER_RIGIDITY_REVIEW.md).
- [Sublinear profile obstruction and ordinary positive lifting](ENVELOPE_REVIEW.md).
- [Critical and superlinear profile obstruction](ALL_EXPONENTS_REVIEW.md).

The review authors reconstructed the arguments and did not relabel an author's
development compilation as their own execution. This integrating replay is
the separate fresh execution described above.

Publication removed one trailing space in `SignedCarry.lean` and terminal
blank lines in several incoming documents. The exact input and publication
hashes and transformation are recorded in
[PUBLICATION_NORMALIZATION.json](PUBLICATION_NORMALIZATION.json).
These are whitespace-only changes; original review input hashes remain
historical pins. The Lean receipt binds the normalized published source
bytes, not the earlier development bytes.

## Scope of the reporting follow-up

The reporting follow-up adds these actual receipts and links. The 19 compiled
Lean sources and the core driver retain the scientific checkpoint's hashes.
The final publication-head repository gate is recorded separately in the PR
description, avoiding a recursive requirement to commit a receipt that names
the commit containing itself.

No replay of the expanded legacy `build_band.py --full` Mathlib packet is
claimed. Its module list was updated to include the new core imports. Earlier
band and literature receipts remain evidence only for their original pins.

**Strongest remaining uncertainty:** no universal successful ordinary carry/
merger selector or uniform moving-target critical-potential estimate has been
proved. Full Collatz remains open in this contribution.
