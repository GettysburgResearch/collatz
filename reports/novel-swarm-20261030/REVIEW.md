# Scoped self-audit and execution receipt

Date: 2026-10-30. Status: **PROPOSED; SELF-AUDITED ONLY**. This is not independent review, formal verification, a complete repository validation, or a complete Collatz proof.

## Frozen scope

Research: `OCCUPATION.md`, `CONCENTRATION.md`, and `ADELIC_SHADOWS.md` under `research/novel-swarm-20261030/`. Standalone executable: `experiments/novel-swarm-20261030/check.py`. Frozen output: `reports/novel-swarm-20261030/checks.json`.

The original chat's source packet was not recovered. Its computation counts and review claims are not reused. The reconstruction and the current continuation have distinct provenance from that missing packet.

## Checks actually executed

Python 3.13.5, standard library only. At the exact source SHA-256 below, the following three executions exited successfully:

```sh
python -B experiments/novel-swarm-20261030/check.py --output <normal.json>
python -OO -B experiments/novel-swarm-20261030/check.py --output <optimized.json>
python -B experiments/novel-swarm-20261030/check.py --workers 1 --output <serial.json>
```

The paths were absolute within the local standalone packet during execution; the commands above are the equivalent repository-root replay. `cmp` confirmed normal=optimized=serial byte for byte. Checks use explicit exceptions, not Python assertions, so optimization does not disable them. The parallel modes use four process workers, not four independent reasoning agents.

The output records all bounded ranges and counts. In particular: 1,364 words; 4,092 ordinary lifts; 10,912 repeated-word cases; 20 actual positive-cycle exceptions retained; 4 invalid/mismatched inputs rejected; 9,438 CRT witnesses; 12,285 binary cylinders; 38 rational probability distributions; six balanced-block model constants; eight exact ternary stationary laws; and an induction covering every positive integer through 4096. Transcript digests are over the specified finite enumeration, not hashes of an unexecuted claimed proof.

Logarithms are enclosed by exact rational atanh series with a proved geometric tail bound, followed by outward rounding. The `1/20` comparison is rationally certified; floating-point estimates are not used to decide it. Infinite geometric exponent tails in ternary models are summed into exact congruence-class weights.

## Reconstructed proof audit

- O1 uses bounded continuous truncations of the valuation, removes mass at the pole, and only then passes invariance through the discontinuous map. No unproved uniform integrability is assumed.
- O2 separately checks preservation of absolute continuity and singularity and identifies the absolutely continuous invariant part using Haar ergodicity.
- E2 does not assume the occupation limit is ergodic. Its shortcut odd frequency is `integral 1/bbar`, not `1/integral bbar`; Jensen supplies the needed inequality.
- E1's valuation-block rate and E2's dyadic-precision rate are different. Their conversion is displayed explicitly.
- E3 distinguishes entropy sharpness from collision sharpness. The latter is an infimum over balanced-block constructions, not an assertion about the iid model.
- E4 covers cycles as a necessary condition but does not exclude them. A finite cycle has collision exponent one.
- A1 uses the actual 2-adic valuation of its coded state. A3 follows the same ordinary source through every displayed state; A4 explicitly changes the source between finite segments.
- A5 retains the zero-defect positive-cycle case. Twenty instances of that exception occur in the bounded check.
- E5 keeps the occupation limit before the precision limit and requires one source/common subsequence. Its recurrence estimate remains OPEN.

No blocking error was found in this self-audit within these scopes. This is not an independent correctness certification. The main conceptual debt is substantial: no fixed-source arithmetic bound delivers the collision upper estimate, and low entropy alone does not imply the long repetitions needed for the source-size bound.

## Byte pins

| File | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `check.py` | 12333 | `0c91568e7b206d2eecef984c5b68d11c0a0b48c33a8d806bcb3a9ae5b11921f3` | `e0084ea5a85fb30fafcc18f3cac866226daba611` |
| `checks.json` | 5380 | `59714d1aeec898719486c803879df43d1d5d99c8a09dda0f0605df1e1cb78c73` | `770c8525e0f6a83167663f07b970d452128ec7c0` |
| `CONCENTRATION.md` | 8987 | `5f9a44aa16f1dcf82d10fc75a7a8b7b38ed0399f5edb9f08bff120b54973f119` | `b36e4fbcfcbb46de1c1b4108edf3c8ee3fdd3b7a` |
| `ADELIC_SHADOWS.md` | 9164 | `804f9a6a5a316d4db3e395d7ecfbce1c4f4bc1f93294ee64161bcf5dd4888c35` | `ba0838a27a0a08ae68b2fef4755ee8fd9804263e` |

GitHub blob creation returned these same four Git blob IDs. Branch attachment and PR-head readback are separate publication checks, recorded in the PR rather than inferred from blob creation.

## Execution deliberately not claimed

Direct Git clone failed at DNS. No complete checkout was reconstructed, and `tools/validate.py` was not run. Only the additive standalone packet was executed. No formal proof assistant, independent agent reviewer, full literature-priority audit, exhaustive current-PR review, or proof of Collatz is claimed. Classical coding, geometric Syracuse laws, and the existing repository entropy coefficient are credited in the mathematical files.
