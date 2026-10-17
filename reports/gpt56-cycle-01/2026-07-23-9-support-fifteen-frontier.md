# Session report — complete centered-defect layers through support fifteen

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Date:** 2026-07-23

## Starting hypothesis

The prior refocus had closed centered-defect supports seven through thirteen and
identified support fourteen as the first layer where contraction no longer
bounds the high-valuation alphabet. The session goal was therefore not another
raw odd-length search. It was to close entire defect-support layers using the
exact cycle product window and a proof-producing affine join.

## Repository refresh

The newest work elsewhere in the repository was read before continuing:

- PR #34 raised the branch-qualified proposed sparse floor through six defects
  and supplied factorwise/cross-prime cycle interfaces.
- PR #45's critical mechanical compiler passed independent reconstruction but
  its trillion-step near-candidate was rigorously nonintegral.
- PRs #47 and #51 closed broad one- and two-pulse negative-cycle families while
  preserving an exact ordinary pulse-block chart as a live positive lane.
- PRs #48 and #49 reduced quotient refund to one deterministic ordinary counter;
  growth is automatic once its changing-modulus divisibility remains defined.

The common obstruction is exact ordinary integrality. Positive cycles remain the
shortest finite certificate because one divisor hit can be independently
replayed from a single integer.

## Mathematical reduction

For defect support `s`, total defect sum `B`, and neutral count `R`, the total
odd length and dyadic exponent are

```text
k=s+R,
A=B+2R.
```

The exact least-state product window is

```text
3^(s+R) < 2^(B+2R),
2^(B+2R) 7^(s+R) <= 22^(s+R).
```

For fixed support this leaves finitely many `(R,B)` cells without imposing any
finite high-valuation alphabet.

Every cyclic word can be rotated to begin at a defect and is represented by an
ordered defect word plus a weak composition of `R` into `s` neutral gaps. For a
split `w=uv`,

```text
C(w)=3^len(v) C(u)+2^A(u) C(v).
```

The meet-in-the-middle match is therefore exactly `D|C`, where
`D=2^(B+2R)-3^(s+R)`. Every match is regenerated and valuation-replayed.

## New results

### Complete support fourteen — `X-8608`

A `7+7` join covers all 37 exact product cells:

```text
windows=37
conceptual_words=50,008,555,902
left_states=62,907,549
right_states=62,907,549
queries=62,907,549
hits=0
```

The C++ output replays byte-for-byte against the canonical transcript. A
separate Python checker reconstructs all windows and counts and directly
enumerates the smallest cells.

### Complete support fifteen — `X-8609`

A `7+8` join covers all 42 exact product cells. Moduli above 64 bits use exact
two-limb Montgomery multiplication. The computation was frozen in six
neutral-total chunks and combined into one canonical transcript:

```text
windows=42
conceptual_words=355,362,127,531
left_states=126,760,223
right_states=475,187,506
queries=126,760,223
hits=0
```

The independent checker reconstructs every product cell and count and directly
enumerates the smallest cells.

### Updated theorem frontier — `T-8603`

The native `86xx` packet now excludes exactly seven through fifteen defects.
Together with branch-qualified proposed `PR34/L-9913`, the current proposed
cycle floor is

```text
at least 16 valuations different from 2.
```

No branch-qualified dependency is silently promoted.

## Candidate counterexamples

None. Neither complete layer contained even a modular divisibility hit, so no
integer reached the replay gate and no `K-####` identifier was created.

## First open layer

Support sixteen is the exact next layer. The current `8+8` scout completes all
cells through neutral total `R<=23` and the cell `(R,B)=(24,16)`. The first
unfinished row is

```text
R=24,
B=18,
D has 66 bits.
```

The current in-memory join becomes expensive there. This is a resource boundary,
not evidence for a cycle.

## Validation

```bash
g++ -O3 -std=c++17 -Wall -Wextra \
  experiments/X-8608-fourteen-defect-mitm/run.cpp -o /tmp/x8608
/tmp/x8608 > /tmp/x8608.out
diff -u \
  experiments/X-8608-fourteen-defect-mitm/results/canonical.txt \
  /tmp/x8608.out
python3 experiments/X-8608-fourteen-defect-mitm/verify.py \
  experiments/X-8608-fourteen-defect-mitm/results/canonical.txt

g++ -O3 -std=c++17 -Wall -Wextra \
  experiments/X-8609-fifteen-defect-mitm/run.cpp -o /tmp/x8609
python3 experiments/X-8609-fifteen-defect-mitm/verify.py \
  experiments/X-8609-fifteen-defect-mitm/results/canonical.txt
```

Both independent audits pass.

## Potential errors and review targets

1. Reimplement the `7+7` and `7+8` joins independently rather than copying the
   submitted programs.
2. Audit the affine block update and the split multiplier orientation.
3. Audit the two-limb Montgomery reduction against arbitrary-precision modular
   multiplication on random 65–80 bit moduli.
4. Confirm that rotation to a defect plus `s` neutral gaps covers every cyclic
   word, including zero gaps and tied structures.
5. Keep conceptual coverage counts separate from stored/queried state counts.

## Files changed

```text
research/compressed-cycle-synthesis/claims/T-8603-centered-defect-frontier.md
research/compressed-cycle-synthesis/README.md
experiments/X-8608-fourteen-defect-mitm/
experiments/X-8609-fifteen-defect-mitm/
reports/gpt56-cycle-01/2026-07-23-9-support-fifteen-frontier.md
```

## Recommended next actions

1. Finish support sixteen beginning with `(R,B)=(24,18)` using disk-backed
   external sorting or residue bucketing.
2. Factor the 66-bit denominator and test a proof-producing CRT join over all
   prime powers before the full-modulus merge.
3. Compare support-sixteen residue generation with PR #34's cross-prime excess
   path compiler.
4. In parallel, seek an eliminant for PR #49's changing-modulus refund condition;
   that lane already supplies positivity and exponential growth once defined.

## Organizational improvement

Every finite-certificate experiment should freeze:

```text
parameter layer,
conceptual object count,
stored state count,
query count,
modular matches,
reconstructed candidates,
exact replay results.
```

This makes a zero result auditable and lets the next collaborator resume at the
first genuinely open cell rather than restarting the entire search.
