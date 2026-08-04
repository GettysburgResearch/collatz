# Session report — nine-B synchronizer and centered high-block quotient

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`  
**Date:** 2026-07-23  
**Starting hypothesis:** a remote finite-support or arithmetic-dynamics representation might turn the verified run-core growth gate into a smaller ordinary invariant problem.

## Repository state read

The continuation used the live branch-local state through:

- PR #38 cartography pass 5;
- PR #51 `O-8001`, `L-8002`, `L-8004`, `L-8005`, `T-8002`, `T-8003`;
- PR #48's independent reconstruction and its refutation of eventually affine positive-slope run schedules;
- PR #49's intrinsic changing-boundary comparison;
- PR #47's new exact commutator interfaces.

The relevant verified positive target is not “every run at least five.” It is the weaker exact condition that every nine-run block have total at least `44`.

## Approaches attempted

### 1. Zero-carry quotient atoms

The exact run-core quotient contains isolated zero-carry triples. The cleanest is

```text
(r,s,t)=(0,5,0):
k=16*ell  ->  k+=9*ell.
```

I enumerated the corresponding exact triples. They do not close under iteration: no compatible next zero-lift edge was found in the declared ranges, and the construction drains rather than regenerates the ordinary top boundary.

**Status:** useful local algebra; not a construction.

### 2. Prescribed high schedules

The verified refund cone supports high nonlinear schedules, but PR #48 proves every eventually affine positive-slope schedule selects an irrational core. Canonical representatives of bounded `{64,65}` branch words were reconstructed exactly; none survived one unsolicited additional synchronized block in the bounded search.

**Status:** bounded negative evidence only.

### 3. Nine-B synchronization

A high run followed by eight zero runs uses exactly nine `B` edges. Centering `B` at its fixed point gives

```text
B^9(p)=1+(9/16)^9*(p-1).
```

Writing

```text
p=1+16^9 W
```

turns the entire block into the ordinary partial map

```text
F_s(W)
 = [9^s(1+9^9 W)-2^(3s)]/2^(3s+36).
```

This is `L-8251`.

### 4. Maximal common odd boundary residue

The synchronized map has the branch-independent modulus

```text
D9=16^9-9^9
  =68,332,056,247
  =7*13*19*37*163*6553.
```

The unique common inverse residue is

```text
omega=37,933,813,917 mod D9.
```

It simultaneously satisfies

```text
9^9*omega+1 =0 mod D9,
16^9*omega+1=0 mod D9.
```

Every defined branch preserves `W=omega mod D9`.

An exact two-consecutive-branch argument shows prime-to-six maximality: any common fixed-residue modulus coprime to `6` for two consecutive labels divides `D9`.

**Status:** `L-8251`, `PROPOSED`.

### 5. Centered positive quotient

Write

```text
W=omega+D9*X.
```

The branch becomes

```text
2^(3s+36) X'
 =9^(s+9)X+T_s,
T_s=9^s*a-8^s*b,
a=215,072,362,
b=38,148,886,279.
```

Both thresholds turn favorable at exactly `s=44`:

```text
9^(s+9)>2^(3s+36),
T_s>0.
```

Therefore every defined branch with `s>=44` and `X>=0` satisfies

```text
X'>X.
```

The exact branch cylinder and two-label quotient law are

```text
X=xi_s+2^(3s+36)k,

k=rho_(s,t)+2^(3t+36)ell,
k'=sigma_(s,t)+9^(s+9)ell.
```

This removes the fixed prime-to-six modulus, divisible-seven condition, and nine-run resource counter from the live state. Only the dyadic ordinary top boundary remains.

**Status:** `L-8252`, `PROPOSED`.

## New results

### `L-8251`

- exact physical `A^r B^9 A^s` synchronizer;
- one ordinary boundary coordinate `W`;
- maximal common prime-to-six invariant `D9`;
- explicit finite acceptance gate back to a positive Collatz integer.

### `L-8252`

- exact centered coordinate `X`;
- positive toll and multiplicative surplus for every `s>=44`;
- pointwise strict growth;
- one dyadic branch residue per high label;
- exact changing-modulus quotient-refund law.

### `X-8251`

Two separately written standard-library implementations reproduce:

```text
centered branch instances:       1,649
raw/centered agreements:         1,649
invariant-residue checks:        1,649
physical high-block replays:       650
quotient-pair identities:        5,110
pointwise high-growth checks:       901
zero-carry pairs in 44..80:          0
```

Transcript:

```text
62a6db9a403326384e207dddd9a7a135a0f9c03eb7a7cb92d6f26c18c0914908
```

Both local commands completed successfully.

## Candidate counterexamples

None.

No positive integer was found whose centered orbit is defined forever. No `K-####` file is created.

## Failed approaches

1. zero-carry triples do not form a regenerative high-resource cycle in the bounded exact search;
2. canonical representatives of tested bounded high words exit immediately after their prescribed prefix;
3. periodic high-block cycles through period three and labels `44..80` produced no positive integer cycle;
4. fixed/constant top-lift transitions were absent in the bounded high-range search;
5. eventually affine schedules are already excluded by PR #48.

These are not extrapolated beyond their exact scopes.

## Potential errors and audit points

1. Reconstruct the grouping convention: a high run plus eight zero runs contains nine `B` edges, and `F_s` additionally advances through the following `s` `A` edges to the next pre-`B` boundary.
2. Check maximality assumptions: the modulus is odd, coprime to `3`, and fixed by two consecutive branches.
3. Verify the exact threshold signs for both multiplier and toll.
4. Check that the physical initial core in `L-8251` is positive odd and that every grouped transition replays the normalized chart.
5. Keep pointwise growth separate from infinite definedness.

## Files changed

```text
research/outlier-bridges/claims/L-8251-nine-b-two-place-synchronizer.md
research/outlier-bridges/claims/L-8252-centered-high-block-expansion.md
research/outlier-bridges/SOURCE_LEDGER_SYNCHRONIZER.md
experiments/X-8251-nine-b-synchronizer/README.md
experiments/X-8251-nine-b-synchronizer/run.py
experiments/X-8251-nine-b-synchronizer/verify.py
experiments/X-8251-nine-b-synchronizer/results/canonical.json
reports/gpt56-outlier-01/2026-07-23-52-nine-b-synchronizer.md
```

## Claims affected

```text
L-8251  new, PROPOSED
L-8252  new, PROPOSED
X-8251  new, exact finite computation
```

No canonical root ledger is edited.

## Recommended next actions

1. Independently reconstruct `L-8251`, beginning with the physical grouping and maximality argument.
2. Independently reconstruct `L-8252`, especially the exact toll threshold.
3. Build a boundary-memory search directly on the centered branches
   ```text
   X=xi_s mod2^(3s+36)
   ```
   using a bounded nonlinear alphabet such as `{64,65}`.
4. Seek a finite regular language of ordinary binary top quotients closed under the exact pair law—not a prescribed infinite schedule.
5. Cross-map the centered machine to PR #12's regular-sanctuary verifier and PR #48's transported-stack formalism.
6. Use rational self-affine tile theory only as representation guidance; the required object is an ordinary finite-support intersection point.

## Organizational improvement idea

The repository now has several machines of the form

```text
x=xi_s+2^H k
 -> x'=c_s+M_s k.
```

Add a shared machine schema recording:

```text
physical decoder;
branch residue;
radix;
odd multiplier;
affine toll;
growth cone;
ordinary input criterion;
top-boundary criterion;
known completion ghosts.
```

A common verifier interface would allow sanctuary/PDR, transported-stack, and rational-tile experiments to be compared without rederiving semantics.

## Bottom line

The constructive target has been reduced again:

```text
before:
  exact run core
  + mod7 invariant
  + moving powers of 3
  + nine-run resource
  + dyadic top boundary
  + growth;

after:
  one nonnegative ordinary X
  + one high dyadic branch cylinder at every step.
```

Every defined high branch is already physical, positive, and expanding. Infinite ordinary definedness remains completely open.
