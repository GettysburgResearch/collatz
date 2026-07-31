# Session report — all-length mechanical closure and growing-support barrier

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**PR:** #81  
**Date:** 2026-07-31

## Objective

Continue the direct attack on the two remaining coefficient-stopping boxes
without introducing a new encoding:

```text
Box 1:
  exclude an ordinary all-time-supercritical orbit;

Box 2:
  force canonical descent at every nontrivial first crossing.
```

The unrestricted boxes are not proved in this pass.

## Cross-branch input

The pass read the newest PR #80 and PR #82 packets.

PR #82 supplied:

- the exact repeated-factor/gap barrier `T-6604`;
- quantitative mechanical loss `T-6605`;
- swap-budget recurrence `T-6606`;
- wrap-only defect transport `T-6607`;
- corridor recurrence `T-6608`;
- fixed-length short full-denominator classification `T-6609`;
- the Rhin square-root swap floor and bank--displacement uncertainty.

PR #80 supplied the distinct-odd-source product bound and stronger
all-supercritical mean-surplus pressure.

No source claim was silently promoted.

## New result 1 — the mechanical premise is closed at all lengths

`T-6806` combines:

```text
upper-mechanical bank < 1;
Sturmian factor complexity <= L+1;
dyadic separation of repeated factors;
Rhin lambda >= j^(-13.3);
an exact finite canonical replay through j=372;
a three-residue integer induction beginning at 373.
```

Result:

```text
j=2:
  word 10, trivial root=endpoint=1;

every valid j>2:
  the upper-mechanical canonical source descends,
  unless the finite segment already contains a nontrivial positive cycle.
```

Consequently every acyclic nontrivial Box-2 failure is now a
**nonmechanical modulus wrap**.  This discharges the mechanical hypothesis in
PR #82's wrap-only classification.

## New result 2 — exact finite certificate

`X-6801` contains two independent implementations.

```text
finite range                    j < 373
valid mechanical rows              234
nontrivial failures                   0
analytic induction bases       373,374,375
semantic digest
5d88f47548ca6716b7c10cf839dc7d65eb6efdff748b35cca9d709aa36771d2e
```

The generator uses modular inversion.  The verifier uses one-bit canonical
rectangle lifting and imports no generator code.

## New result 3 — bank area

For the prefix-excess path above the mechanical word,

```text
I = exact adjacent-swap area;
H = maximum integer prefix excess;
B = coefficient bank;
R = number of displaced odd positions.
```

`L-6808` proves

```text
I >= H^2;
B < H+1 <= sqrt(I)+1;
H <= R.
```

For a canonical no-descent target failure, every individual displacement also
satisfies

```text
h_i < 1+log_2(j)+(B+1)log_2(3).
```

## New result 4 — stronger asymptotic barriers

Combining `L-6808` with PR #82's source-qualified return uncertainty gives:

```text
T-6807:
  liminf I/j^(2/3) >= (alpha/2)^(2/3)
                   = 0.463412...;

T-6808:
  liminf R/j^(1/3) >= (alpha^2/2)^(1/3)
                   = 0.583862....
```

Thus the remaining acyclic Box-2 obstruction is forced simultaneously into:

```text
a nonmechanical wrapped displacement;
at least two-thirds-scale integrated distance;
at least cube-root growing displaced support;
one of fewer than j/2 complete-denominator defect levels.
```

## Box 1 status

The PR #80 product/packing theorem strengthens the necessary surplus profile
of an ordinary all-supercritical path.  It still does not move the canonical
source coordinate.  No new physical-growth consequence was misrepresented
as ordinary extraction.

The exact unresolved statement remains

```text
min_{w in W_N^sup} r_w -> infinity.
```

## Box 2 status

The mechanical and no-wrap sectors are closed, modulo a positive cycle.
The exact remaining theorem is a complete-denominator avoidance statement for
the growing-support wrap language classified in PR #82 `T-6609`.

## Honest boundary

No proof of CST, no proof of absence of positive cycles, no proof of Box 1,
and no proof of Collatz is claimed.
