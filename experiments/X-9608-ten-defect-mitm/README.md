# X-9608 — Exact ten-defect normalized meet-in-the-middle certificate

**Experiment ID:** `X-9608`  
**Status:** exact finite computation supporting proposed `L-9605` and `T-9604`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23

## Purpose

This packet checks the complete finite remainder of `T-9604`: positive accelerated cycle words having exactly ten valuations different from `2`.

The theorem first classifies the residual exceptional-letter languages and proves a finite neutral-gap cutoff. Direct expansion of the remaining family would contain more than 1.6 billion largest-gap-normalized words. `L-9605` replaces that expansion by an exact normalized half-join.

This is a cycle-exclusion packet. It does not produce a positive cycle, divergent orbit, or Collatz counterexample.

## Exact join

For a centered word split `w=uv`,

```text
E_w = 3^(k_v) E_u + 2^(A_u) E_v.
```

Writing

```text
D=2^(A_u+A_v)-3^(k_u+k_v),
```

and using the invertibility of `2` and `3` modulo `D`,

```text
D | E_w
iff
E_u*2^(-A_u) + E_v*3^(-k_v) == 0 mod D.
```

`run.cpp` uses a `5+5` exceptional-block split. It indexes left normalized residues by exceptional multiset and neutral-gap sum and probes them with the complementary right state.

`verify.cpp` is independently written and uses a `4+6` split. It therefore generates different half-pattern and gap collections while testing the same exact full-word condition.

## Coverage

Residual languages:

```text
1^10
1^9,3
1^9,4
1^9,5
1^9,6
1^9,7
1^8,3,3
1^8,3,4
1^8,3,5
1^8,4,4
1^7,3,3,3
```

Frozen totals:

```text
finite (type,R) rows             184
full candidates represented       1,623,353,430
5+5 left states                       25,881,900
5+5 right states                       7,879,043
formal divisor hits                            0
nontrivial cycle hits                          0
```

Candidate cardinalities are computed exactly from complementary half-multiset and half-gap counts. They agree with the independently generated `4+6` packet.

## Replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9608-ten-defect-mitm/run.cpp \
  -o /tmp/x9608

/tmp/x9608 > /tmp/x9608.json

diff -u \
  experiments/X-9608-ten-defect-mitm/results/canonical.json \
  /tmp/x9608.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9608-ten-defect-mitm/verify.cpp \
  -o /tmp/x9608-verify

/tmp/x9608-verify
```

## Frozen digests

```text
run.cpp authoring SHA-256
2f07ed7ae0467f89b844087d893df79ec2cd6dba4e71e5429c5dfcd8545f1d07

verify.cpp authoring SHA-256
7fbe8b49ce45eaf66f3867597e38b9bb88a47438438bf28dc4a206f1b5994a3a

canonical.json SHA-256
7daad798a10f6c68db81064a5014f0214392be3d422b58771ab5b6a7b8d82545

5+5 row/state FNV-1a-64
776c0a3b4ace3abc

split-independent candidate FNV-1a-64
8b0ed2d5d2377bda
```

The source hashes record the authoring files used for the frozen run. Repository or CI replay is still requested; the row digests bind the mathematical packet independently of source formatting.

In the authoring environment, the `5+5` run took approximately `5.1` seconds and the independent `4+6` verifier approximately `5.4` seconds. These timings are informational only.

## Boundary

- The packet covers exactly ten non-`2` valuations with arbitrary neutral gaps.
- Original high valuation magnitudes are unbounded; the theorem's monotone lowering classifies them into the displayed residual types.
- Eleven or more non-neutral valuations are outside this packet.
- No failed join, modular residue, or large covered cardinality is evidence that a counterexample exists.
