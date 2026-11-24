# Published global continuation checkpoint

The scientific checkpoint was published to [PR193](https://github.com/GettysburgResearch/collatz/pull/193) on branch `research/astra-universal-descent-20261124`. The branch ref and PR head were both read back at:

- **Scientific commit:** `fbcd019f7324e1d610d163d5a23c0d6bffff749e`.
- **Scientific tree:** `9a085e8418e262923625dcf210ca580372f875aa`.
- **Parent:** `5f160a843750f209ea1251dfb01ea0b23e532fd6`.
- **New files:** 31, comprising 19 scientific/source/review files and 12 initial execution, intake and coordinator records.
- **Complete scientific checkout:** 508 tracked files.

The API-created tree exactly matched the locally committed and validated tree. The local staging commit was `4cc7c330cb19b020c06dd139cffeafc6008714fe`. The publication commit has the same tree and uses the previous actual PR head as its parent. No existing scientific file was changed by this continuation.

## Verification actually performed

The new packet's [execution receipt](kernel/CHECKS.json) records successful compilation and axiom audits for **24 public theorems in four Std-only modules** under official Lean 4.34.1. Both new exact Python controls passed in normal and optimized mode with byte-identical output. Their source hashes remained stable during execution. The [signed-pair control](residual-control.json) checks only the two displayed rational examples. The independent mathematical reviews and their scopes are linked in [ROOT_REVIEW.md](ROOT_REVIEW.md).

The [local clean-checkout validation](local-checkout-validation.json) passed. After publishing the science, the actual remote commit was fetched into a fresh complete checkout and passed:

```text
python -X utf8 -B /workspace/scratch/cf806951b2d5/global-published-checkout/tools/validate.py \
  --receipt /workspace/scratch/cf806951b2d5/global-published-science-validation.json
```

The [published-science receipt](published-science-validation.json) records the actual remote commit and tree. These checkout checks establish repository integrity, not the truth of the infinite mathematical arguments. Earlier Lean packets and large historical search bundles were not rerun.

## Evidence follow-up and status

The follow-up commit containing this note and the two checkout receipts adds three report files only. It does not change any source, reviewed hash, or theorem in the scientific checkpoint. The final follow-up branch head is subsequently read back from GitHub and validated as a clean complete checkout; its identity is reported in the PR description.

The previous PR description is preserved exactly as title/body fields in [PRIOR_PR_DESCRIPTION.json](PRIOR_PR_DESCRIPTION.json). The PR remains a draft research checkpoint. The full ordinary convergence theorem has not been established: the universal directed implication on `36k+8,72k+17` is still open, and the written arithmetic and collision routes retain their explicit missing implications.
