# Switch the shadow, complete the missing seed

**PROPOSED pending independent mathematical review.** This is a continuation
of [PR #124](https://github.com/GettysburgResearch/collatz/pull/124), frozen at
`1d4dfc103055648def3db73860778a383a91ea3c`, under programme
[issue #121](https://github.com/GettysburgResearch/collatz/issues/121).
It is not a complete Collatz proof, a universal successful selector, or a
claim of external novelty. Parent proofs and statuses are unchanged.

Read [the complete proof](PROOF.md), then [sources and limits](SOURCES_AND_LIMITS.md).

## The new mechanism

The old companions shared the original source's negative centre -5. The new
companion can follow an all-odd prefix around centre -1 instead:

    n=8^k u-5  --(110)^k--> 9^k u-5,
    m=4^k u-1  --1^(2k)--> 9^k u-1.

For k>=3, this companion is below n/2^k. Prefix endpoints differ by four;
this is not automatically a merger. AES-002 gives a general dyadic-gap
merger, with both the 110 cycle and the eleven-step negative cycle through
-17 as explicit applications. No negative path is used as a positive source.

## The old missing seed has a finite, complete entry rule

For v=9^(k-1)u=1 mod16 with v>1, read t=v2(v-1).
When t is odd choose the old companion (3n-5)/4; when t is even choose the
new companion 4^k u-1. Both produce adjacent states whose relevant valuation
is even. The exact two-step comparison

    (q+1,q) -> ((3q+1)/4+1,(3q+1)/4), q=1 mod4, q>1,

reduces that valuation by two. It therefore reaches an EVEN adjacent pair
after a finite number determined by t. The credited adjacent rule then
merges or produces the old H(C)=(9C+2,C) comparison. The n=3 endpoint is
handled separately. Thus the selector has no OUTSIDE_SEED result anywhere
in the complete k>=1, positive odd-u representation.

**Entry is not success.** H returns can still leave their language or exhaust
a budget; infinite hard-return paths and sources outside the representation
are not excluded. Those outputs remain explicit failures of the selector.

## A strong original-root certificate in the newly handled class

For k=26,u=137 the new source and companion are

    n=41405709321801049233686523,
    m=616993148949757951.

They meet at clocks 85/59, at 62238390386066313887370728. Every positive-time
state of the n-arm is above n, and 2^26*m<n. Since n is divisible by three,
no smaller pure ancestor exists at any backward depth. This example belongs
to the parent's OUTSIDE_SEED class; its all-parameter theorem is AES-005.

## Replay

From the repository root:

```sh
python -B experiments/X-AEM-004-shadow-switching/run.py --source 131
python -B experiments/X-AEM-004-shadow-switching/run.py --check experiments/X-AEM-004-shadow-switching/results/canonical.json
python -B experiments/X-AEM-004-shadow-switching/verify.py experiments/X-AEM-004-shadow-switching/results/canonical.json --self-test
python -O -B experiments/X-AEM-004-shadow-switching/verify.py experiments/X-AEM-004-shadow-switching/results/canonical.json --self-test
python -B experiments/X-AEM-004-shadow-switching/run.py --full aes-full.json
```

The implementation uses only Python's standard library and exact integers.
The full file retains all finite grid outputs, not only successes. The
verifier imports no generator or repository module and reconstructs paths,
CRT sources and finite itinerary classes differently. Same-author independent
implementations are not independent mathematical review.

## Evidence summary and boundary

The former 24,576-input grid now has 14,193 mergers and 10,383 explicit
OUTSIDE_RETURN outcomes: 3,086 additional mergers and all 11,107 old mergers
retained. There are 711 new variable-length family rows, plus 108 examples
from the two periodic-centre instances. These are certificate classifications,
not a convergence census or a measure of the fraction of Collatz solved.

See the [actual execution receipt](../../../reports/astra-exit-merging-04/validation.json)
and [experiment contract](../../../experiments/X-AEM-004-shadow-switching/README.md).
No complete-checkout root validation, external Lean build, CI run, or
independent mathematical acceptance is claimed for this continuation.
