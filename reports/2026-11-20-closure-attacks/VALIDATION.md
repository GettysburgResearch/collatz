# Actual execution on the published scientific commit

The research branch was created from main
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a.
The GitHub Git-data tree was compared with the locally staged tree before
the commit and branch were created. The remote branch was read back, then
the real GitHub commit was fetched into a complete detached review checkout.

## Executed source

| Field | Exact value |
|---|---|
| Scientific commit | 5204a6f19beb490fb7c305908188bb3f392abd2e |
| Tree | bb44677a39eba39792610879eb3be39759dc94b8 |
| Tracked files | 346 |
| Review checkout | /workspace/scratch/6c37546fb87e/collatz-review |
| Scientific execution | 20 November 2026, 20:27:07--20:27:09 UTC |
| Clean before and after | Yes |
| Scientific content hashes verified | 30 |
| Fresh scientific report comparisons | 5, all passed and byte-identical |
| Repository validation with regressions | 11 commands, all passed |

The [scientific execution receipt](execution-content-science.json) has
SHA256 ef72ca6840bbfd136d7b6469211edfbccab3ca82889e80171eda3196ac864a48.
It records every executed command, return code, duration and expected/actual
report digest. The five comparisons cover the multiplier descent, physical
return, arithmetic theorem controls, independent arithmetic controls, and
local energy bridge.

The [repository receipt](execution-content-repository.json) has
SHA256 89d555ec894161bcb04641a12c196f0835a038e0712dd081e25ff2da7aed5570.
The command was the repository's required validator with regressions.
Its complete output and exact checkout identities are retained in the
receipt. This is an actual complete execution, not a source inspection,
partial fixture run, or inferred result.

Before that execution, the new notes' 60 local Markdown links and the
staged whitespace diff were checked successfully. Source-authored normal
and optimized-mode checks are separately recorded in the adjacent peer
reviews; the publication driver above ran each scientific checker once
on the real scientific commit.

## Metadata child and final-head boundary

The next commit only attaches these two receipts, this validation narrative,
and a link from the report index. All 30 files listed in
CONTENT_SHA256.json remain byte-for-byte unchanged. The receipt above
therefore continues to identify the scientific bytes precisely; it is
not relabeled as an execution at a later commit.

The final PR body records the final metadata head, verifies the unchanged
manifest, and attaches the separate required checkout-validation receipt
from that final clean head. Keeping that last receipt outside the tracked
tree avoids an endless sequence of commits whose only change is a receipt
for their parent.

## Mathematical limit

The executions support the exact algebra, finite replay and file integrity
specified in the research notes. The universal elementary arguments were
also independently reconstructed at exact file hashes. Neither the
validator nor the numerical diagnostics proves the remaining physical five
closure, the missing global energy comparison, or unrestricted cycle
exclusion. The analytic note retains its explicit source-qualified inputs.
