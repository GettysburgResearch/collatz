# Independent review of FB-001 through FB-004

Reviewer: the separate `independent_attack` research agent.
Date: 20 November 2026.

**Verdict: VERIFIED within the exact written scope below.** This is a
reconstruction of the elementary mathematical arguments and an execution
of the finite checker. It is not a formal proof-assistant verification,
nor an extension to positive-grade minima or unknown convergent sources.

## Exact reviewed contents

The reviewed files are in `research/forward-bridge-20261120/`:

| File | SHA-256 |
| --- | --- |
| `PROOF.md` | `ec6d5c2bc329fb9affa3af3731e847b44d233b437dd7be8c269e53af931fd273` |
| `check.py` | `36644e86b137b0e67f9e9d935864060d3b2f687d494918be5e75209c1d397513` |
| `README.md` | `d2ef4a20d636d00da57c8d3786bdb220d34c23ef29957a0b12b4765fc0610425` |

The proof and checker hashes were computed immediately before and after
the execution recorded below and confirmed unchanged. The source PR146
is frozen in the packet at
`92820dd336b010215eb8a6eb4878a31b58a67656`; PR145's preceding branch-count
discussion is pinned at `dd245a712f985909f541590e3f6c179b7ba011e4`.

## Reconstructed arguments

**FB-001: common-clock balanced mergers and grade minima.** Splitting a
first-arrival path gives `g(n)=2s_h(n)-h+g(T^h(n))`; each additional
trivial-cycle lap contributes one odd input and two steps, so the
identity persists after arrival. Equal grades imply equal first-arrival
parities, hence the same cycle phase at every sufficiently large common
clock. The invariant then forces the same odd count. Conversely a common
endpoint with equal odd counts gives equal grades. A smaller source
sharing a finite endpoint with a known convergent source is itself
convergent, so initially unknown smaller sources do not evade the
grade-minimum characterization of permanent representatives.

**FB-002: the sharp product gap.** Multiplication of the exact step
ratios gives `n*2^g(n)=product 4z/(3z+1)` over odd inputs before the
first visit to 1. The last odd input must satisfy `3z+1=2^a`, with
even `a>=4`, hence `z>=5`. Every factor exceeds one, and the last
factor is at least `5/4`. Equality requires exactly one odd input,
equal to 5, giving precisely the sources `5*2^j`.

**FB-003: the complete nonpositive-grade sector.** The product bound
attains the grade `-2m` minimum at `4^m`. For an odd grade at most
`-3`, the corresponding power of two is `2 mod 3`, so it is excluded
from the source class. The sharp nonpower bound is then attained by
`10*4^m`. Grade `-1` has minimum 7 because its stated path has five
odd inputs and 11 steps, while the only smaller `1 mod 3` sources
are 1 and 4, with different grades. These cases exhaust `g<=0`.

**FB-004: all upper-bit obligations in that sector.** I checked the
eligibility cutoffs and every displayed affine-prefix identity. Row 1
produces exactly the stated shifted powers `3^a+1` and `3^a+2` in their
respective exponent ranges, making their convergence necessary. Initial
halving reduces the two infinite representative families to row-1 arms
or to `5+3*2^ell`. The four-step path from 5 and the eleven-step path
from 7 give the claimed higher-arm reductions. The finite exceptional
arms are separately replayed. This proves the conditional equivalence
without claiming convergence of either shifted-power family.

No mathematical gap was found in these four elementary arguments.

## Execution scope

Executed successfully at the hashes above:

```sh
python -X utf8 -B research/forward-bridge-20261120/check.py
```

Exit status: `0`; returned status: `PASS`.

| Check | Actual count |
| --- | ---: |
| Bounded first arrivals | 25,000 |
| Common-clock balanced comparisons | 178 |
| Exact product checks | 2,048 |
| Classified nonpositive-grade sources congruent to 1 modulo 3 | 4,857 |
| Distinct observed grades | 43 |
| High-bit affine identities | 410 |
| Finite exceptional upper arms | 12 |
| Negative controls | 2 |

The mathematical all-family statements are supported by the written
proofs, not inferred from these bounded counts. This review does not
cover later file revisions, different definitions of the prefix filter,
the positive-grade sector, or a claimed complete Collatz merger selector.
