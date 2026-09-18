# Curated finite investigations

Open the new desk and use **Load** for `*.v2.json`. These are recipes: mathematics is recomputed on import, and the recorded result/kernel digests are compared. They are not trusted cached results or theorem certificates.

| File | Investigation |
|---|---|
| `paired-investigation.v2.json` | 27 with bit 3 flipped to 19, independent shortcut/odd clocks, a 64-source carry-motif trial, exact rank/module fixture, weighted transport, the repeated `1110` ghost and the isolated `5n+1` cycle. |
| `huge-pair.v2.json` | Exact 1025-bit neighbors; finite acceleration support and explicit bit cropping. No assertion of divergence beyond the budget. |
| `unfinished-controls.v2.json` | 8-bit-limited trajectories and unfinished trial members, a rank-increasing module, bounded killed/unresolved transport, a 4096-branch ghost and the separate `3n-1` control cycle. |
| `27-19-meeting.json` | One finite witness: common state 40 at raw arrivals 103 and 12, shortcut A arrival 63 and hidden B odd-clock arrival. Check with `python -m observatory.verify observatory/examples/27-19-meeting.json`. This is not a workspace recipe. |

The v0.1 `*.collatz.json` files remain for `/classic`. The new desk's migration preserves their complete original recipe as `importedClassic` but only converts orbit/comparison into the paired workspace; do not mistake that for replay of all classic panels.

For the paired example's exact 64-source trial, the current receipt records **28 supports, 24 counterexamples, 6 control passes and 6 control failures**. These categories concern a specified 30-raw-step implication, not convergence or independent random observations. Small sources and shared tails are intentional inspection fixtures, not a statistically representative research corpus.

The JSON fingerprints identify the kernel used to prepare these examples. When deliberately changing that kernel, preserve the historical receipt and regenerate only after independently checking the new finite results; do not replace expected evidence simply to hide a failing arithmetic test.
