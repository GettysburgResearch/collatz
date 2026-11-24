# Published ordinary-source checkpoint

The science was published to [PR193](https://github.com/GettysburgResearch/collatz/pull/193) on branch `research/astra-universal-descent-20261124`. The GitHub branch ref and PR head were re-read after the update and both showed:

- Science commit: `a5c0eaa979170ff0ba8f85809cb904e78e657ccd`.
- Science tree: `777fec7bf713d4113762a5554b233c0b309df4ec`.
- Parent: `ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784`.
- Complete checkout: **474 tracked files**.
- New science and first execution/review records: **26 files**.

The API-created tree exactly matched the locally committed and validated tree. The local staging commit was `d0aac477d3fc1915d5c64d79c43a487f00220be5`; the publication commit uses the same tree and the actual previous PR head as its parent.

## Execution

[Local checkout validation](local-checkout-validation.json) passed on a clean complete checkout of the staging commit. After publication the actual remote commit was fetched, checked out in a fresh worktree, and passed the same required driver:

```text
python -X utf8 -B tools/validate.py --receipt /workspace/scratch/cf806951b2d5/ordinary-published-validation.json
```

The [published-science receipt](published-science-validation.json) records the actual remote commit and tree. This is repository integrity validation, not verification of the mathematical conclusions.

The new packet's [Lean and exact-control receipt](kernel/CHECKS.json) records 11 successful declarations under official Lean 4.34.1, the standard-axiom audit, stable source hashes, and identical successful normal/optimized Python control output. Only the three new Lean modules were rebuilt.

The follow-up commit containing this publication note and the two checkout receipts adds evidence only. It does not alter the scientific packet or its reviewed hashes. The PR remains a draft research checkpoint. Universal convergence, arbitrary cycle exclusion, and escape exclusion have not been proved.
