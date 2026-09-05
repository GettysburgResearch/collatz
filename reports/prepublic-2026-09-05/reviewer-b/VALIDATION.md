# Reviewer B validation receipt

## What was actually executed

The source files below were read through GitHub, locally materialized, and matched to their **Git blob SHA-1** before the final replays. Local names differ only for isolation. The frozen source commits are #91 `b8c88843726ee7ac11cf91323c69bf911ca50706` and #92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`.

| Evidence | Original source / local execution | Exact result |
|---|---|---|
| E91 | `X-ATR-001-three-routes/run.py` -> `pr91_run.py`; `--check pr91-canonical-reconstructed.json` | Full payload reproduced; generator blob `9e0d0386d7f248095e1bb91ccbbaed76579ffb46` |
| E91 | Same protocol `verify.py` -> `pr91_verify.py`; also executed under `python -O -B` | Full payload independently reconstructed; verifier blob `c410f5d4846b71f1a5b1a01df9e2c8ffbe88fda7`; four documented resealed mutations rejected |
| E5B | `X-ASTRA3-005-rank-budget/verify.py` -> `rank_budget_verify.py`; normal and optimized `--self-test` | Published payload digest matched; blob `d87e438bac13f7b7c6ad0aec77625d8d4c923c86`; 10 resealed mutations rejected |
| E5S | `X-ASTRA3-005-spectrum-switch/verify.py` -> `spectrum_verify.py`; normal and optimized `--self-test` | Published payload digest matched; blob `72f5460184c745b1251b8a21bff42f9e88d2518a`; 8 resealed mutations rejected |
| EB | Reviewer-authored `targeted_checks.py`, with no author/repository imports | Whole-source H64 cone at k=0 and19; 18,847 vertices at19; exact outward mass/tail inequalities; rational-cycle, rank/safe-set and constant checks |

Published semantic payload hashes matched:

```text
E91 7f0043a57062d879843936c1df324346c0381787fa9fb8b82cda7edc596e2f66
E5B 1dc5510f205dd8b4a106a636af68ef8a7252a867fc1e4c10310d93e54567fb5d
E5S 45888e331821905d73141de70258b9cbfc03df94ec58208a94b5d66f9d687aee
EB  f3d7dfb4b445b8fba1306c295d4435fa0edf3236ad21336c02c5452096edc9cd
```

The two fifth-pass **generators were read in full, not separately executed**. A canonical payload reconstructed by the original verifier and matched to the published semantic digest is not described as a byte-for-byte copy of the original serialized JSON file. The generator and verifier source hashes above do match the exact remote bytes. The PR91 generator was fixed locally for a transcription-only missing blank line before the final source-hash match and final replay; no upstream file changed.

The 22 resealed mutation rejections comprise 4 in E91, 10 in E5B, 8 in E5S. Their hashes were recomputed after mutation; rejection is not merely a stale outer hash. Logs are in [logs/](logs/). Original scripts/data are deliberately not bundled here; obtain them at the frozen repository paths above. The review packet includes only the reviewer's own targeted script, its result and execution receipts.

## Selected coverage, not a sum of theorem proofs

E91 covers 16,384 inverse-fan endpoints and 32,766 edges, 28,666 frozen jets, 11,187 explicitly unfrozen pairs, 32 progression certificates, 31+120 guarded repayment samples and 24 resolvent intervals. E5B includes six exact rank balls (largest 2^24 with 10,195 members), 45 peak-barrier inputs, 96 switch inputs and 10 corruption cases. E5S includes 16,383 physical modules, nine rank balls, 6 finite-time whole-source mass enclosures, 44+28 guarded repayment samples and ten bounded merging searches. These finite cases do not prove universal coverage; the general arguments were reviewed independently as mathematics.

EB bounds every omitted source by an analytic arithmetic-progression tail. It proves `3*Q_lower > M_upper` at k19 (rejecting the one-third ceiling), while `200*Q_upper < 69*M_lower` at the two selected times. It also reconstructs the rational control's preperiod13/period30 and distinguishes the quarter-safe from nonincreasing-safe sets at3->4. These are finite-horizon checks, not a new all-time theorem.

## Code audit without full replay

All earlier #92 run/verify/test code was read, including physical guards, inverse completeness, cap derivations, rounding direction, omitted-source tails and mutation logic. The first large cone through k36/40 (up to 2,510,783 vertices) and full protocols2–4 were **not** rerun here. Their author-reported counts/digests remain inspected evidence, except for the specifically reconstructed EB interface. No reconstructed bounded test is presented as a replay of those full payloads.

Static finding: early pass2 `validate` and witness checks use Python assertions and have no explicit refusal of `-O`. Those assertions disappear under optimization. This review does not claim to have run the entire early protocol under `-O`; recommend explicit checks or an interpreter guard and a declared support policy. Latest budget/spectrum and the PR91 verifier use active error checks and were actually run optimized.

## Full-repository validation: NOT RUN

`tools/check_integration_state.py` at baseline was read completely (blob `3df5f1c51c6cbd841e10a6e7091677738918cfce`). The active front-door/status/index/archive files it references were inspected through GitHub. No authenticated full checkout was available. Actual Git attempts returned:

```text
fatal: unable to access 'https://github.com/GettysburgResearch/collatz.git/':
Could not resolve host: github.com
```

Therefore **`python tools/check_integration_state.py` was not run on a full checkout**, and no fixture or packaging-tree result is labelled as such. Run it at the specified baseline and proposed integrated head before acceptance. The checker is curated structural/status validation; it does not certify new mathematics, source licenses, live PR contents or the new namespace collisions.

## Independence and exclusions

The original pairs of programs were written by their source authors. This reviewer independently reconstructed their mathematics and ran the selected frozen programs; agreement of the original two implementations alone is not treated as an independent research review. EB was separately written for this audit. This review is not formal verification.

No external Lean build, large predecessor payload replay, comprehensive literature-priority check, full original #90 proof review, secret/history scan, rights clearance or effective-permissions audit was performed. The external predecessor input remains source-qualified. No numerical experiment assumes high-range convergence to remove unchecked sources.
