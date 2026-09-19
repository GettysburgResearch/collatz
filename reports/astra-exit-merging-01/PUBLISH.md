# Publication and independent-review handoff

## Current delivery status

**This packet has NOT been pushed to GitHub in its authoring session.**
There is no new remote commit or PR to cite. The current session's discovered
GitHub connector actions are read-only. The installed plugin was checked for
an alternative publishing action; none was exposed. The direct Git attempt
failed DNS resolution for github.com; `gh` was not installed. No credential
was requested, inferred, or copied into the packet.

The user authorized research and publication by saying GO following issue
#121. Publication remains incomplete for that tool-access reason, not because
the research packet needs permission to be explored. The native proofs,
experiments, canonical results, and exact validation receipt are provided
as repository-layout additions and an application patch.

## Intended repository and source base

```text
repository: GettysburgResearch/collatz
base:       ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a
branch:     research/astra-exit-merging-20260919
issue:      #121 (reference only; do not close)
```

The new paths are isolated under:

```text
research/astra-exit-merging/
experiments/X-AEM-001-exit-merging/
reports/astra-exit-merging-01/
```

No main-branch file, canonical scientific status, existing proof/artifact,
workflow, license, repository setting, or PR lifecycle should change.

## Publishing from an authenticated clean checkout

First inspect the supplied source and the manifest; do not execute downloaded
code without reviewing it. Preserve an unrelated dirty worktree rather than
resetting it. In a clean checkout where the pinned base is available:

```bash
git fetch origin
git switch -c research/astra-exit-merging-20260919 ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a
git apply --check /path/to/collatz_exit_merging.patch
git apply --index /path/to/collatz_exit_merging.patch
git diff --cached --check

python -B experiments/X-AEM-001-exit-merging/run.py \
  --check experiments/X-AEM-001-exit-merging/results/canonical.json
python -B experiments/X-AEM-001-exit-merging/verify.py \
  experiments/X-AEM-001-exit-merging/results/canonical.json --self-test
python -O -B experiments/X-AEM-001-exit-merging/verify.py \
  experiments/X-AEM-001-exit-merging/results/canonical.json --self-test

# This full-tree validation was NOT possible in the authoring environment.
python -X utf8 -B tools/validate.py --regressions
```

Inspect and record any divergence between current main and the frozen base;
do not silently treat an unreviewed rebase as the same tree. Record fresh
publisher results separately from the author's receipt. A failure must not
be hidden by weakening an old validator or changing canonical artifacts.

After review and successful checks, create an addition-only commit and push
the new branch. Open a **draft exploratory PR** using PR_BODY.md as the starting
text; insert the real resulting head and any newly executed checks. Read
back that remote head before reporting success. Add the resulting PR link
and the real SHA to issue #121, using ISSUE_121_COMMENT.md as a starting note.
Do not close #121: the universal cover remains open.

## What the independent reviewer should check first

1. The whole-residue seven-bit bridge, including positivity and parity on both
   arms, not just its affine endpoint identity.
2. The conversion X=2Y+1, the actual second odd-run length h, its final mod4
   guard, and every resulting clock.
3. The one-third source and equal-clock composition when 3|n.
4. The all-intermediate no-forward-descent estimate with the +617 constant,
   and the exact boundary: only the displayed arm, not all possible diagrams.
5. The CRT specialization and separation of all-parameter proofs from the
   finite corpus, with honest external credit for the first odd-exit rule.

The current results are PROPOSED pending that mathematical review. This
handoff is not a merge recommendation or evidence of universal coverage.
