# Adaptive smaller companions and asynchronous source merging

**PROPOSED pending independent mathematical review. No complete Collatz proof.**
Continuation of #123 (`bf0696f888442c82a4c6cdc1df36becf8550295a`), programme #121.

The new main theorem removes the previous second-exit restriction rather
than merely adding a longer favorable itinerary. For a given source

    n=8^k u-5, k>=1, u positive odd,
    16 | 9^k u+1,

it gives

    T^(3k+4)(n)=T^(3k+2)((3n-5)/4), 0<(3n-5)/4<3n/4.

EVERY input in #122/#123's old h>=1 entry domain is covered, including failed
second exits, failed return entries, and the 3003/999 synchronization control.
The new companion for 3003 is 2251: T^10(3003)=T^8(2251)=713.
The additional old h=0 class is covered too. A weaker target factor can yield
a substantially broader, shorter certificate. The old one-third results are
not refuted and their stronger factor is not asserted for the new companion.

For every guarded k>=15 the entire displayed forward arm stays above n.
Infinitely many such inputs are divisible by 3, with no smaller pure ancestor
at any depth. Thus this remains genuine two-sided, original-root descent.

## More than the direct rule

A proved three-companion selector, choosing (3n-5)/4, (3n-25)/8, or (n-35)/8,
handles seven of the eight odd seed residues modulo16 by an explicitly finite
path to a merger OR the earlier reusable pair (9C+2,C). Variable odd-run
lengths are read from the input. The remaining seed class and failed return
guards are retained. Reaching a return pair is not a successful certificate.

Every finite old hard-return itinerary now lifts from the NEW old-h=-1 entry
class, not just the former entry region. Arbitrarily many expanding returns
are still allowed, with original source order and independent clocks intact.

A clock-rigidity lemma explains why simply allowing nonzero fixed clock offsets
with the old affine companions could not yield uniform affine-word families:
the clock difference is fixed by the 2-adic valuation of the source slopes.
Changing the companion is a mathematical change, not a presentation trick.

Read [the complete proof](PROOF.md), especially Sections 3, 5 and 7, and
[sources and limitations](SOURCES_AND_LIMITS.md). New claims AAC-001--006 have
not been independently reviewed or formalized.

## Run on a source

From the repository root:

```sh
python -B experiments/X-AEM-003-adaptive-companions/run.py --source 3003
```

A bounded call returns a physical merger, an outside-domain/return result,
or budget exhaustion; it never calls an unfinished computation a proof.
`--budget` controls the number of subsequent hard-return stages.

## Replay the finite evidence

```sh
python -B experiments/X-AEM-003-adaptive-companions/run.py --check experiments/X-AEM-003-adaptive-companions/results/canonical.json
python -B experiments/X-AEM-003-adaptive-companions/verify.py experiments/X-AEM-003-adaptive-companions/results/canonical.json --self-test
python -O -B experiments/X-AEM-003-adaptive-companions/verify.py experiments/X-AEM-003-adaptive-companions/results/canonical.json --self-test
```

`run.py --full PATH` writes every deterministic row, including failures.
The corpus has 1,115 family rows, 108 direct no-descent cases, and all 24,576
inputs k=1..6, odd u<8192. There are 11,107 local mergers, 10,397 unresolved
return exits, and 3,072 outside-seed outputs. These are not convergence counts.
All 1,536 old-entry inputs in this grid have the new direct certificate;
the all-input inclusion is proved algebraically, not inferred from this count.

The verifier uses actual raw trajectories rather than the generator's word
concatenation, forward rather than reverse return cylinders, and CRT in v
rather than u. It also checks 257 symbolic cylinders, rejecting 18 resealed
corruptions and five direct bad witnesses. Same-author implementation
diversity is not independent mathematical acceptance.
