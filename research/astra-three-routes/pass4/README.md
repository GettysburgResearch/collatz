# Fourth pass: a constructive moving-ghost rank links all three routes

Agent: `astra-three-routes-04` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: `7d0397c92879545609aa4097f89f5497cd53026d`, PR #92.

**All theorem-level claims are PROPOSED pending independent review. No complete
Collatz proof, universal SC result, cycle exclusion, or fixed-floor survivor
bound is claimed. All three routes remain active.** Earlier proof and
experiment bodies remain unchanged.

This pass is constructive, rather than another enlargement of the excluded
finite-feature class. The useful connection is one common integer rank built
from infinitely many block-adapted ranks, yet exactly computable from at most
four entries. The extra entry has an unbounded input-dependent index. Long
periodic corridors now have total exit formulas and exact integrated costs.
The full inverse fan isolates one resonant odd branch per endpoint. What is
still missing is a global way to pay for changes of mode or to cover all
residuals by lower-rank merging diagrams.

## The shared object

For a>=0 let

    w_a=1^a0,
    z_a(n)=3^a(n+1)-2^a(2n+1),
    R_a(n)=z_a(n)^2/3^v3(z_a(n)),
    R_*(n)=min_(a>=0) R_a(n).

A zero z has rank zero. For positive sources this occurs only at n=1,a=1.
The infinite minimum is exactly

    R_*(n)=min(R_0(n),R_1(n),R_2(n),R_h(n)),
    h=v3(2n+1),

where the last entry is needed only for h>=3. Also n-1<=R_*(n)<=n^2.

For n>1 take the active a=0 for even n and a=v2(n+1) for odd n. Its maximal
legal repeated corridor has

    k=floor(v2(z_a(n))/(a+1)) >= 1,
    A(n)=g_a^k(n), g_a(n)=(3^a n+3^a-2^a)/2^(a+1).

A is a total ordinary acceleration; it does not mean "search until descent".
On an aligned source with R_a(n)=R_*(n), it gives

    R_*(A(n)) <= [3^a/4^(a+1)]^k R_*(n) <= R_*(n)/4.

For every a>=2 and k>=1, a proved CRT family supplies such ordinary sources,
with arbitrarily high ternary precision. Their numbers increase while the
SAME proper integer rank decreases. No finite truncation of the rank dictionary
works for every source in these families.

## Read the three routes

| Route | Result this pass | Remaining full-closure gap |
|---|---|---|
| [3. Moving common rank](MOVING_GHOST_RANK.md) | Exact maximal corridors; infinite-to-four-entry collapse; all-parameter uphill common-rank drops | R_* increases on some mode switches; a complete compatible repayment rule is missing |
| [2. Resonant source fan](RESONANT_SOURCE_FAN.md) | Complete inverse acceleration, one deep odd column, exact rank fibers, lower-rank normalizer, all-height backward power family | The one-edge residual is nonempty; further merging diagrams need a proved complete cover |
| [1. Renewal mass](RENEWAL_MASS.md) | Exact all-source/all-residence corridor sum; summation over the infinite dictionary; safe-state resolvent with rigorous whole-source tail | No bound is proved for repeated returns between unsafe states or their transported density |

The order starts with definitions, not a narrowing of the research portfolio.

## Two concrete positive certificates and an essential negative control

    577363 -> A(577363)=649534,
    R_*: 50808384 -> 7144929.

The value rises and the common integer rank falls. This belongs to an
all-parameter family, not a lone numerical observation.

    81 -> 122 -> 61 -> 92 -> 46,
    R_*(81)=81 < R_*(46)=225.

Thus the numerically larger merging ancestor 81 gives a backward rank reduction
for 46. An all-height family uses x=3^e for every e=4 mod 8.

    7 -> A(7)=13, R_*: 12 -> 36.

This REFUTES unconditional forward monotonicity of the candidate. The successful
families cannot be silently applied after an uncontrolled mode switch.

## Exact evidence, not extrapolation

The new generator and separately written verifier agree on:

- 16383 ordinary sources and 44933 raw shortcut replay steps;
- 10930 distinct sampled rank fibers;
- 88 CRT family triples and 16 all-height backward-family samples;
- complete inverse lists for endpoints 2..128, capped at source 8192, with 504 edges;
- exact one-edge classification through source 16384: 13458 forward drops,
  510 additional inverse drops, 2415 unresolved residual labels;
- four complete-source/all-residence occupation intervals and 576 ordinary lifts;
- quarter-drop normalization: 128 starts reach 1 and 16255 stop at an unsafe
  input in the finite pilot; this is not a complete convergence algorithm.

Eight resealed corrupt reports are rejected. Both implementations have the same
author: implementation independence is not independent mathematical acceptance.
The all-parameter and all-residence statements rest on the accompanying proofs.

From the repository root:

```bash
python -B experiments/X-ASTRA3-004-moving-ghost/run.py \
  --check experiments/X-ASTRA3-004-moving-ghost/results/canonical.json
python -B experiments/X-ASTRA3-004-moving-ghost/verify.py \
  experiments/X-ASTRA3-004-moving-ghost/results/canonical.json --self-test
```

Semantic SHA-256:

    7ac43379cc79e1cd550a77a72d8587b0e7d9b5cd45ed2bbf10895e16667b9710

[Sources, claim boundaries, and review targets](SOURCES_AND_REVIEW.md) record
how this differs from the preceding packets and from PR #90/#91. No broad
external novelty claim is made. No external large certificate or Lean build,
old inverse-cone experiment, full-repository validator, or workflow was run.
