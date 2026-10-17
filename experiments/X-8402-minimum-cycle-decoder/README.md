# X-8402 — Exact minimum-window cycle exclusion through length 50,000

Experiment ID: `X-8402`  
Issue: #41  
Agent: `gpt56-complexity-01`  
Status: `EMPIRICAL / EXHAUSTIVE EXACT FINITE CERTIFICATE`

## Question

Can a nontrivial positive accelerated Collatz cycle have at most `50,000` odd
states?

The experiment combines two complete exact finite calculations:

1. bound the minimum state of every such cycle using the exact cycle product;
2. check every possible odd minimum in that bounded range until it reaches a
   smaller odd state or returns.

## Product-window reduction

For a cycle of odd-state length `k`, total valuation `A`, and minimum odd state
`n`,

```text
2^A/3^k=product_i(1+1/(3n_i))
```

implies

```text
2^A n^k <= (3n+1)^k.
```

The weakest left side for fixed `k` uses

```text
A_k=ceil(log_2(3^k))=bit_length(3^k).
```

The exact multiprecision scan proves that, for every `1<=k<=50,000`,

```text
n<=1,447,682,232.
```

The endpoint is sharp for this inequality: `1,447,682,232` passes at exactly
`k=47,468`, where `A_k=75,235`, while the next integer fails at every tested
length.

## First-drop audit

Every nontrivial positive cycle minimum is an odd integer at least `7`.
`run.cpp` checks all

```text
723,841,113
```

odd integers from `7` through the exact upper bound. Every one reaches a smaller
odd integer under the accelerated map. No return occurs.

The longest first-drop time is `251` accelerated steps, first attained at

```text
1,200,991,791 -> ... -> 1,064,232,949 < 1,200,991,791.
```

All intermediate values fit in `62` binary bits.

## Two exact implementations

`run.cpp` uses:

- `boost::multiprecision::cpp_int` for the product-window certificate;
- an exact `uint64` accelerated replay;
- a trailing-zero intrinsic and explicit overflow guards.

`verify.cpp` independently uses:

- a separately written multiprecision comparison;
- `unsigned __int128` for `3x+1`;
- repeated exact halving rather than a trailing-zero intrinsic;
- a parallel partition of the complete minimum range.

Both reconstruct the same endpoint and first-drop record.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-8402-minimum-cycle-decoder/run.cpp \
  -o /tmp/x8402-run

/tmp/x8402-run > /tmp/x8402.json

diff -u \
  experiments/X-8402-minimum-cycle-decoder/results/canonical.json \
  /tmp/x8402.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic -pthread \
  experiments/X-8402-minimum-cycle-decoder/verify.cpp \
  -o /tmp/x8402-verify

/tmp/x8402-verify
```

Expected independent-verifier ending:

```text
independent X-8402 reconstruction passed
```

Canonical JSON SHA-256:

```text
498e9c76fcd351ab25289f4c486b88757a0adc117ec0eecb2959d2c68d637e89
```

## Exact conclusion

Together with `T-8401`, the frozen result excludes every nontrivial positive
accelerated cycle with at most `50,000` odd states.

## Limitations

- The computation does not address cycles of larger odd-state length.
- The result is not presented as a world-record cycle bound; external work uses
  several stronger bounds and several inequivalent counting conventions.
- A first-drop computation is a cycle exclusion, not a convergence proof for
  all integers.
- No divergent seed, sanctuary, or other Collatz counterexample is found.
