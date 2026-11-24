# Verification and source boundaries

The scientific entry point is [the proof packet](../../research/astra-joint-closure-20261124/README.md). Three GPT-6.2 Astra agents developed complementary attacks and independently reconstructed one another's results. The coordinator inspected the proofs, reran the finite arithmetic, and compiled the final finite kernels. Agreement between agents is not itself a proof; the mathematical reconstructions and executable scopes are recorded separately.

## Reproduce the finite arithmetic

From a complete checkout, using Python 3.11 or newer:

```sh
python -B reports/astra-joint-closure-20261124/replay_controls.py > /tmp/collatz-joint-controls.json
```

This executes each of the three finite programs in normal and optimized mode, requires identical outputs, and compares the complete pressure payload to its frozen result. It checks the absence of assertion statements, so optimization does not remove a test. See [the executed receipt](CONTROLS_RECEIPT.json).

The pressure certificate exhausts its finite residue space; the rational orbit and ordinary merger controls test the displayed instances. None converts a bounded search into universal convergence.

## Reproduce Lean

Use Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, with a prebuilt mathlib checkout at `d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
python -B reports/astra-joint-closure-20261124/replay_lean.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib > /tmp/collatz-joint-lean.json
```

The runner verifies version pins and frozen original Git-blob identities, compiles temporary inputs with one Lean worker, and checks the printed axiom inventory against the three standard Lean axioms. It does not download, modify, or rebuild dependencies. The executed [Lean receipt](LEAN_RECEIPT.json) records transformed input hashes, all printed theorem dependencies, process exits, and diagnostics. Four working modules pass with warnings treated as errors. The two import-only source passes preserve all original proof bodies; one unused-binder warning in PR202 is retained in the receipt. The original umbrella-import inputs were not compiled unchanged.

The 25 distinct theorems include 14 declarations authored upstream and 11 new finite declarations. Full asymptotic theorems and the Python pressure enumeration are not kernel formalizations.

## Source and review pins

[SOURCE_INTAKE.json](SOURCE_INTAKE.json) records the main baseline and thirteen selected open PR heads. The initial connector search returned the latest 100 open PR records; that metadata scan is not an audit of every source in every PR. Source files and reviews in this packet are bound by [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json).

The independent reviews are [ordinary merger](arithmetic/REVIEW_ORDINARY.md), [paired pressure and first-hit packing](ordinary/REVIEW_PRESSURE.md), and [finite local rational cycles](pressure/REVIEW_ARITHMETIC.md). Their verdicts apply to the specific content hashes stated in each report. Publication on a research branch does not promote the project's canonical mathematical status.

## External sources inspected

The coordinator read the primary text of [rStation paper 48](https://rstation.ai/problems/collatz/papers/48), particularly Lemma 7, equation (76), and Theorem 8. Its stated joint floor matches the interface extracted in PR203: a fixed unit cylinder, central exact totals and a small fractional excess of ternary precision, with a bounded real offset. This is a source-interface check, not an independent reconstruction of the entire external analytic proof. The [ProofAtlas predecessor release](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) reports an external formalization; no rebuild of that package was performed here. Neither input is needed for the new elementary weighted-tree theorem.

The rational-cycle argument gives its own proof of the classical word formula and modular branch-group facts. Its historical references are Lagarias, *The set of rational cycles for the 3x+1 problem*, Acta Arith. 56 (1990), 33–53, [publisher record](https://doi.org/10.4064/aa-56-1-33-53), and Monks et al., *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, [primary preprint](https://arxiv.org/abs/1204.3904). No assertion that the new combined formulation is absent from all previous literature is made.

## Repository integrity

The complete-checkout validator is run after committing the scientific packet, with its receipt outside the checkout. Publication receipts identify the actual validated commit and tree. These checks concern repository integrity and the bounded regression suites, not mathematical truth. The branch does not change workflows, repository settings, the integrated registry, or existing source PRs.
