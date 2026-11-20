# Review and replay record for the all-hands closure attempts

The [research packet](../../research/allhands-global-closure-20261120/README.md)
contains three scoped mathematical results and the exact remaining gaps.
**No complete Collatz proof is claimed.**

## Written reviews

| Review | Scope and independence |
|---|---|
| [Root reconstruction](REVIEW_ROOT.md) | Reconstructs all three arguments and checks their source boundaries. |
| [Prime-support review](REVIEW_PRIME_SUPPORT.md) | A different agent reconstructs P13 and implements the finite arithmetic independently, including a different maximizer choice. |
| [Circulation review](REVIEW_CIRCULATION.md) | A different agent reconstructs DC1--DC3. The numerical review reuses the author's path producer but independently checks edges, affine multiplicities, quotient flows and clipping. |
| [Second circulation review](REVIEW_DIRECTED_CIRCULATION.md) | Another agent checks the written return construction, summation order and clipping proof; no independent execution is claimed in this review. |
| [Depth-two review](REVIEW_DIRECTED_DEPTH.md) | A different agent reconstructs the classification, complete-orbit separation and both clocks, and inspects both implementations without claiming a new execution. |

These are independent AI reconstructions within this session. A scoped
VERIFIED verdict does not promote the packet into the repository's accepted
mathematical baseline. External predecessor-count and analytic inputs retain
their stated qualifications.

## Retained numerical evidence

| Program | Retained report | Principal finite coverage |
|---|---|---|
| Author circulation | `directed-circulation-report.json` | 218 sources; 24,039 literal edges; three exact quotient flows; three damaged paths rejected. |
| Author prime support | `prime-support-report.json` | 306,559 affine pairs; 10,917 peak-cost windows; 85,170 retained-tail checks; seven negative controls. |
| Author depth two | `directed-depth-report.json` | 99 parameters, sources up to 6,145 bits, 62,500 classified candidates; nine damaged/domain witnesses rejected. |
| Reviewer circulation | `circulation-review-report.json` | Separate edge/label checks and 44,217 rational clipping cases. |
| Reviewer prime support | `prime-support-independent-report.json` | 70 sources; 1,317 peak windows; 7,968 valuation tails; exact integer inversion and logarithm enclosures. |
| Root depth two | `directed-depth-independent-report.json` | Independently generated literal orbits, prefixes and classification; no author import. |

The expanded circulation report additionally records the reviewing agent's
normal-mode execution including 1,3,9,27,81: 388,919 literal edges and three
balanced quotient flows on 26,498 vertices. It is not represented as an
optimized-mode run or a second implementation of the path producer.

## Reproduce the packet

From a complete checkout, using Python 3.11 or later:

    python -X utf8 -B reports/2026-11-20-allhands/replay_packet.py --output-dir /tmp/collatz-allhands-replay

This runs six programs normally and with `-OO`, for twelve executions.
Every output must equal its retained report byte for byte, and each pair
of normal/optimized outputs must agree. The output directory must be outside
the checkout. `execution-receipt.json` records the actual commands, program
hashes, return codes, output identities and timings of the integrated replay.

To replay only the expanded circulation review:

    python -X utf8 -B reports/2026-11-20-allhands/review_circulation.py --author-path research/allhands-global-closure-20261120/check_directed_circulation.py --extra-sources --output /tmp/collatz-circulation-expanded.json

`CONTENT_MANIFEST.json` fixes the scientific and review files. Universal
statements rely on the written proofs, not on the finite examples. The
publication record separately identifies a clean complete remote checkout
and the repository-wide validation actually run on it.
