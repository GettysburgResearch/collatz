# Verification of the ordinary-step attempt

The root replay succeeded on the complete clean scientific checkout **d75b5235691bc2cee50833a7b776cd28f3e22c0c**, tree **f1b2d46240179baeffde71bf8d7a4befdfdcbffa**, from 08:17:37 to 08:17:40 UTC on 24 November 2026. The subsequent receipt commit adds only this report and replay records; it does not change the tested research sources.

[Machine-readable receipt](fresh_replay/receipt.json) · [Repository validation](fresh_replay/repository-validation.json) · [Independent written review](INDEPENDENT_REVIEW.md) · [Root written review](ROOT_REVIEW.md)

## What executed

* Official Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52. Each module compiled with one worker and warnings treated as errors into a newly created directory outside the checkout. The arithmetic module imported the freshly built descent object. Only bundled Std and that local dependency were used.
* All **ten named public declarations** were queried for axioms. The reported union is propext, Classical.choice and Quot.sound. The replay rejects sorry, admit and custom axiom declarations and checks the requested names against the actual output.
* The exact control script passed both ordinary and optimized Python, with identical stdout/stderr and no assert statements that disappear under optimization. It checked the rational decay/smoothing constants, five smoothing levels, 756 positive powered histories, ten distinct matching pairs, and two examples omitting the reference word. These are finite controls, not empirical evidence of universal convergence.
* `python -X utf8 -B tools/validate.py` passed on the complete clean checkout. The replay confirmed unchanged HEAD, tree, scientific source hashes and clean status afterward. This is repository integrity, not mathematical verification.

Receipt SHA-256: `676cdc142cfb5f761761242c8c29be33ace1bd73f735ccc16ef5b36de2dadeab`.

## Reproduction

From a clean complete checkout of the scientific checkpoint, invoke [replay.py](replay.py) with `--lean` pointing to Lean 4.34.1 and `--output` pointing to a new directory outside the repository. The program preserves command arguments, compiler version, fresh object hashes, all output hashes, named axiom reports and before/after scientific source hashes.

The analytic kernel bound, weighted-norm summation, rational amplification and logarithmic matching-length deductions remain written proofs. The Lean modules certify their named finite arithmetic interfaces. Universal descent, control of all unmatched histories and exclusion of nontrivial positive cycles remain **OPEN**.
