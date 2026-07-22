# Quality audit of cartography pass 3

**Agent:** `gpt56-cartographer-01`  
**Audit date:** 2026-07-22  
**Audited head:** `7c9afd20c2db60d95a74fc69a422d2b1bedeca60`  
**Disposition:** **superseded for current-state use** by the reviewed replacement pass

## Verdict

The mathematical core of pass 3 was mostly sound, but the pass was not audit-grade as a repository cartography update. It should not remain the current integrated map without correction.

The replacement preserves the valid mathematics, repairs provenance and status wording, reconciles atom identifiers, incorporates omitted source developments, and updates the primary map, crosswalk, diagram, and PR description.

## What passed re-audit

### PR #44 / PR #33 status

PR #44 really does contain a claim-by-claim independent reconstruction of PR #33 at frozen source `c9d62bce3e93f5785f72e4520bc576863d9379eb`. Its matrix marks `T-9705` `PASSED` within the exact corrected 256-transition phase-`-34` class and explicitly says integration is still pending.

Correct global wording is therefore:

```text
independently verified at the frozen source;
native-ledger integration pending;
no implication outside the frozen class.
```

### Centered PDR boundary

The pass correctly reported the exact forced-tail recurrence

```text
64 B' = 81 B + e - e'
```

and PR #44's fixed-modulus result: the recurrent modular kernel is the finite cylinder/de Bruijn graph and every modular lasso is a periodic completion ghost. A sound ordinary certificate needs a most-significant boundary, finite-support or carry-flush proof, or an unbounded height/length coordinate.

### Cycle packets

The reported source values match the source branches:

- PR #42 covers every admissible positive-cycle window through 27 accelerated odd terms by exact meet-in-the-middle and records zero modular matches;
- PR #42's `(41,65)` low-complexity families contain `35,548,596,168,868` valuation words and have zero modular matches;
- PR #45's compressed critical-scale word and 43-swap construction are rejected by a directed interval with margin greater than `0.00247`;
- PR #47's one-pulse scan covers 720,000 reduced candidates and finds only the trivial cycle.

### Distributed-pulse algebra

The synthesis in pass 3 is algebraically correct after independent re-derivation.

For a base word of length `N`, prefix exponents `A_j`, and pulse increments `delta_i`, let

```text
Delta_j = sum_(i<j) delta_i,
Delta   = sum_i delta_i.
```

The pulsed word has exact affine constant

```text
C_delta
 = sum_(j=0)^(N-1) 3^(N-1-j) 2^(A_j+Delta_j)
```

and denominator

```text
D_delta=2^(A_N+Delta)-3^N.
```

Increasing valuation `a_i` by `delta` changes the current affine constant by

```text
(2^delta-1)
 * sum_(j=i+1)^(N-1) 3^(N-1-j)2^(A_j),
```

with the suffix evaluated after earlier pulses. The positive-cycle condition remains the full equality `C_delta=nD_delta` plus exact replay.

The correction adds the missing qualification: a serious cycle offense must operate at the current critical continued-fraction/verified-height scale. Small repetition counts are controls, not frontier candidates.

## What failed quality review

### 1. Source provenance was incomplete

`ANALYSIS_SNAPSHOT_PASS_3.md` used phrases such as “current open head at cutoff” for PRs #13, #19, #34, #45, and #47 instead of freezing exact SHAs. That defeats the purpose of an immutable snapshot in a rapidly moving repository.

### 2. The primary map was not actually updated

Pass 3 added a delta file but left all of the following at the pass-2 state:

- `GLOBAL_COUNTEREXAMPLE_MAP.md`;
- `cartography/CROSSWALK_AND_PRIORITIES.md`;
- `docs/global-counterexample-map.mmd`;
- `docs/global-counterexample-map.dot`;
- the draft PR body.

The pass claimed that status changes had been propagated, but the main graph still colored PR #33 only as proposed.

### 3. Atom numbering was inconsistent

A pre-pass comment reserved

```text
ACL-P036 = linear-height quotient-refund invariant.
```

Pass 3 then created the same target again as `ACL-P038`. The reviewed replacement restores `ACL-P036` as canonical and retires `ACL-P038` as a mistaken duplicate alias.

### 4. A load-bearing cross-cycle reduction was omitted

Issue #39 records that the phase-1 state satisfies

```text
(q,1) -> (T(q-1)+1,1).
```

A permanent phase-1 tail is therefore exactly the original shortcut Collatz problem in a shifted coordinate, not a new amplifier. The viable cross-cycle target must prove repeated exits/returns among several phase families, a finite positive return before the reduction, or a genuine multi-phase invariant.

### 5. Priority language conflated novelty with logical distance

The quotient-refund architecture is the strongest new divergent-orbit architecture, but a positive cycle remains the shortest logical certificate because it is finite. The replacement gives two separate rankings:

- distance to a disproof;
- architectural research leverage.

### 6. H moved materially immediately after the cutoff

Current PR #19 advanced from the finite search summarized in pass 3 to iteration 8:

- proposed exclusion of every positive H block cycle through `2,479,700,524` blocks;
- proposed factor-entropy/capital lower bounds;
- proposed prefix-return barriers, including exclusion of `{2,3}` templates with return constant at most 84.

The reviewed replacement includes this current state.

## Replacement rule

For current research decisions, use:

1. `ANALYSIS_SNAPSHOT_PASS_3R.md`;
2. `CARTOGRAPHY_PASS_3_REVIEWED.md`;
3. the revised `GLOBAL_COUNTEREXAMPLE_MAP.md`;
4. `cartography/ATOMS_PASS_3_REVIEWED.md`;
5. the revised crosswalk and graph sources.

The original pass-3 files remain as historical evidence of what was published, but are superseded for current-state cartography.
