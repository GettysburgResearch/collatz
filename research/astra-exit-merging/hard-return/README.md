# Hard exits can return to the same paired comparison

**PROPOSED pending independent mathematical review. No complete Collatz proof.**
Continuation of [PR #122](https://github.com/GettysburgResearch/collatz/pull/122)
and [strategy #121](https://github.com/GettysburgResearch/collatz/issues/121).
Parent frozen at `65c91ecea97d9ebf931eb1d9284b7950182a298e`.

Read [the proof](PROOF.md), then [sources and evidence limits](SOURCES_AND_LIMITS.md).

## What changed

The parent's good second-exit condition is not assumed here: this packet starts
on its complementary hard exit. The original source and its smaller companion
reach the pair `(9C+2,C)`. For `C=2^(r+1)b-2`, r>=3, b positive odd:

- If `3^r b=1 mod4`, the pair merges after r+3 shortcut steps each.
- If `3^r b=3 mod4`, it becomes `(D,9D+2)`, where `D=(3^(r-1)b-1)/4`.

The arms swap, but the comparison form survives. This one rule composes over
arbitrarily many changing hard labels. A complete cylinder compiler realizes
every finite list of hard labels followed by a merging label. Labels r>=8
make D increase; those expanding returns are handled without asserting that
D is a decreasing rank.

Lifted back to a guarded original `n=8^k u-5` divisible by three, the result is

    T^L(n)=T^L(n/3-2),  0<n/3-2<n/3,
    L=3k+h+6+sum_i(ri+3).

Both k and h, the number of stages, and every label are unbounded. A sufficient
explicit k threshold proves no forward descent on the entire n-arm; divisibility
by three forbids a smaller pure ancestor. All-input statements WITH guards and
CRT non-vacuity constructions are kept distinct.

## Concrete new example

    n=142532741427, x=47510913807,
    labels 9 (hard, growing), 5 (hard), 3 (merge),
    T^36(n)=T^36(x)=803558279.

A k=82 version of the same changing-label pattern merges at 279 equal shortcut
steps without EVER going below its original n on the displayed n-arm. The
canonical artifact contains its exact integers, words and minimum.

## A discovered failure to retain

`n=3003` and the fixed proposed equal-clock partner `x=999` first reach 1 at
29 and 34 shortcut steps. Their eventual raw-cycle phases differ, so they
NEVER meet at equal times. They do meet at unequal times. This rejects a
universal fixed-partner synchronous closure, not Collatz or other partners.

Outside-language exits and infinite hard-return itineraries remain unresolved.
This does not cover all sources congruent to 7 modulo 32. A bounded selector
retains OUTSIDE_LANGUAGE and BUDGET_EXHAUSTED rather than certifying them.

## Replay

From the repository root:

```sh
python -B experiments/X-AEM-002-hard-return/run.py --check experiments/X-AEM-002-hard-return/results/canonical.json
python -B experiments/X-AEM-002-hard-return/verify.py experiments/X-AEM-002-hard-return/results/canonical.json --self-test
python -O -B experiments/X-AEM-002-hard-return/verify.py experiments/X-AEM-002-hard-return/results/canonical.json --self-test
```

The generator supports `--full /path/to/full.json` for complete deterministic
case rows, including every unsuccessful ambient input. The committed compact
artifact contains exact digests and examples; it is not a substitute for the
written proof. The verifier uses a different CRT variable and a forward rather
than reverse cylinder compiler, and imports no generator or repository module.
