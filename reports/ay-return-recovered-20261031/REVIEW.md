# Recovery and continuation: evidence and review boundary

**All new mathematics remains PROPOSED. Collatz is unresolved.** This is an author-side reconstruction and adversarial checking report, not independent peer review or formal verification.

## Source boundary

The predecessor is PR #141 at `ccf1887cd07502c3772f8ccbd77c8dab22ea51c5`. The interrupted later workspace and its original 18 files were not available byte-for-byte. The recovery narrative was published at `83e942638d3ceac915a57a0e3a3c50fcb5205fb2`; its new checker followed at `df1920fb78b0d20f206422c4a91c78e02b5f89cc`. See [the reconstruction](../../research/ay-return-recovered-20261031/RECOVERY.md) for exactly what was preserved and what remained unreconstructed.

The new [continuation packet](../../research/ay-transversal-20261031/README.md) supplies a fresh proof of the previously quarantined ancestor-normalization claim and a stronger general theorem. It does not claim the old missing proof bytes have been found. No independent-agent launcher was available in this session; parallel execution here means concurrent standalone checker processes, not independent mathematical agents.

## Narrow mathematical verdicts

| Claim | Evidence and boundary |
|---|---|
| T1: proper-ancestor elimination | Written well-founded induction; requires deterministic killed dynamics, suffix closure of the RAW forward language, and strict rank admission. The budgeted version additionally needs additive nonnegative costs. Does not eliminate general two-arm mergers. |
| T2-T3: transverse rank descent and infinite separation | Exact affine and popcount proofs; 177 parameter instances checked, including 10,155-bit sources. Strictly enlarges the old candidate language; does not prove convergence of every endpoint. |
| T4: larger transverse candidates | Exact physical identities, finite menu. No additional successful seeds beyond unwrapping in this census. The revised resource bound excludes the optional ancestor test menu. |
| C2: finite-state inverse rank | All 4,374 unit residues and all three high-digit lifts checked by a verifier separate from the synthesis recurrence. The lifting proof makes the credit inequality universal. It ranks inverse conversion, NOT the original forward Collatz system. |
| C3: four-event cover | Complete 162-state preserving cover and terminal depths 1-4 checked. Yields the separate 3t bound. |
| C4: counting barrier | Analytic parity-word injection/counting argument with explicit all-prefix scope. Does not exclude changed prefixes, source-dependent comparisons, or general mergers. |
| Recovered section/kernel/carry claims | Algebraic reconstructions plus exact bounded replay; not a restoration of old files or a promotion of old review status. |

## Executions actually performed

[replay.json](replay.json) freezes ten files by SHA-256 and Git blob identity, records Python version, and records six successful processes: each of the three programs normally and under `-O`. Every run reproduced its recorded JSON bytes, and all frozen files were unchanged before/after. Explicit runtime checks survive `-O`; they are not Python assertions.

Reproduce from the repository root with Python 3.10+ and the standard library:

```sh
python -X utf8 -B experiments/ay-return-recovered-20261031/check_recovered.py
python -X utf8 -B experiments/ay-transversal-20261031/transversal.py
python -X utf8 -B experiments/ay-transversal-20261031/inverse_credit.py
```

Repeat each with `python -O -X utf8 -B`. Output should match the respective committed results JSON. To regenerate the explicit potential, pass `--certificate` to `inverse_credit.py`; the committed certificate is also directly accepted by its `verify` function.

Coverage includes 10,000 literal section returns, 82,944 kernel comparisons, 1,296 microscopic SRS edges, 6,240 run endpoints, 2,184 reconstructed cone identities, 6,558 new small-cone traces, and 99 larger cone traces. The new credit certificate checks 13,122 modular lifts and rejects an all-zero-potential mutation. The search census checks 4,096 odd seeds through 8191 and replays all successful chosen proof chains in all five menu variants under both admission policies.

Strict successes: forward 154, with unwrapping 156. Budgeted successes: forward 139, with unwrapping 142. Proper ancestors add none in this census, consistently with T1. Seeds 7 and 9 remain UNRESOLVED by this language; they are not Collatz counterexamples.

## Published-byte identity check

Before final commit creation, the remote science tree `49c454006eb16cfc23ce263858624e5b94b1eaec` was read back. Independently recomputed local Git subtree hashes matched the remote entries exactly:

- `experiments/ay-transversal-20261031`: `a94f76837576ed97675aef4a04150abe3690ea95`
- `experiments/ay-return-recovered-20261031`: `1dd89e4dae54aefce72b49f0dadda5a3ab5d07c2`
- `research/ay-transversal-20261031`: `37aa77e44c61bcec92dcb61357668667b1306b42`
- replay-only report directory before adding this document: `9ef1464298d6ed6128ca8bb6dd8a1d0bd47839c3`

This confirms that the tested code, recorded outputs, certificate, frozen proof notes and replay receipt were uploaded without byte changes. This report was added afterward and is not one of the ten files frozen in that receipt.

## What was not executed or established

The current local workspace was a partial reconstruction, not a complete repository checkout. `tools/validate.py` and the full repository regression suite were NOT run in this pass. The older complete-checkout validation remains pinned to its older commit only. No external proof-assistant build, independent agent review, new swarm launch, global well-founded order for all critical returns, or complete certificate-coverage theorem is claimed. No accepted-result registry was changed.

The first unsupported step remains universal coverage by source-persistent rank-decreasing diagrams. The new inverse rank cannot be transplanted to forward critical returns without a new argument, and complementary local ranks cannot be switched freely. Preserve the recovered false greedy cycle at 42 and the one-normalization obstruction at 27 as regressions.
