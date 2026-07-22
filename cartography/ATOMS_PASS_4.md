# Atomic counterexample problems — pass 4

These are the new or materially sharpened handoffs from the fourth cartography pass. They are cartography formulations unless explicitly marked otherwise.

## Existing-atom updates

### `ACL-P036` — forever-defined complement counter

Replace the older state `(t,i,j,z)` by PR #49's exact reduced state

```text
(t,i,k),
t>=3744,
k>=256.
```

The next type is an output of `k mod64`, not supplied control. Full continuation is one divisibility test, and every legal step satisfies `k'>=2k`. PR #49 `L-8504` makes this state recoverable from one physical integer `n`, so the certificate may begin from `n_0` alone. PR #49 `T-8505` adds the necessary condition that infinitely many globally new odd primes divide the boundary shifts. The sole positive obligation is one explicit physical state whose deterministic partial map is defined forever while satisfying that forced prime turnover.

### `ACL-N076` — complement-counter domain dichotomy

Prove one of:

1. every ordinary finite `(t,i,k)` eventually fails PR #49's exact next-scale divisibility test;
2. every infinite compatible completion is nonordinary by a quantified top-boundary theorem;
3. the mandatory fresh-prime turnover is incompatible with decoder definedness;
4. one physical integer is defined forever, in which case publish `ACL-P036`.

### `ACL-N080` — H delayed novelty / reset renewal

Add PR #19 iteration 9: the adaptive `10/30` zero-carry macros strictly descend, and their renormalized `3/1` Sturmian core has bounded multiplier and is nonphysical. A positive H construction must use a different macro family with zero carry, nondecrease, multiplier escape, exact cylinder closure, and one finite initialization.

---

## `ACL-P040` — Negative-three `9/(8,16)` pulse-chart survivor

**Statement.** Find one positive integer `x_0` for which the deterministic partial map

```text
G(x)=9x/8        if x == 0 mod 8,
G(x)=(9x+1)/16  if x == 7 mod 16
```

is defined for every future step, together with a finite inductive ordinary top-boundary proof.

The physical initialization is

```text
n_0=42x_0-5.
```

Every `G` step replays exactly one accelerated Collatz block, `(1,2)` or `(2,2)`. The trivial cycle is absent from positive integral `x`. A repeated `x` gives a nontrivial positive cycle; a nonrepeating infinite positive path is unbounded.

**Full-conjecture implication.** Either outcome is an unconditional Collatz counterexample.

**Required proof object.** Explicit `x_0`, exact all-time domain invariant, physical replay, and an independent checker. Arbitrary-depth binary cylinders or a `2`-adic completion do not count.

**Frozen finite baseline.** Exhaustive cylinder enumeration through depth `31` gives least root `x=24643395416689283212736`, physical `n=1035022607500949894934907`; it exits at the next block. Any positive proof must go beyond this finite frontier.

**Derivation.** See `cartography/PULSE_CHART_SYNTHESIS.md`.

---

## `ACL-N081` — Pulse-chart renewal decision and H transfer

**Statement.** Group the chart of `ACL-P040` from one `(2,2)` block to the next. With `r` intervening `(1,2)` blocks and `p=16x`, the exact renewal is

```text
p_next=[3^(2r+2)/2^(3r+4)]p+1.
```

Prove one of:

1. every positive ordinary renewal chain violates an exact completion-height, entropy/capital, prefix-return, fresh-prime, or endpoint-product condition;
2. one explicit renewal chain has exact zero carry, remains positive, and supplies the all-time chart witness of `ACL-P040`.

The critical mean is

```text
kappa_pulse=log(16/9)/log(9/8)=4.8849491923617...
```

so PR #19's H tools must be rederived with this shifted multiplier rather than copied formally.

**Use.** This is a fixed-small-arithmetic divergent-orbit lane, complementary to PR #49's changing-modulus refund decoder.

---

## `ACL-P041` — Critical mixed-drift block-carry cycle circuit

**Statement.** Construct a critical-scale accelerated valuation circuit by combining:

1. PR #45 `L-8404`: a fixed block shape has at most one word at each dyadic residue, giving an exact carry-edge decoder;
2. PR #47 `L-9604`: opposite-drift two-block runs obey an `n`-independent commutator divisibility sieve and finite repetition cutoff;
3. PR #34 `L-9914`: compatible prime-power excess paths reconstruct at most one monotone word and enforce the full denominator factorwise.

The output must be one closed carry path

```text
c_0=0 -> c_1 -> ... -> c_g=0
```

at one positive base state `n`, with every decoded block expanded and every exact valuation replayed.

**Full-conjecture implication.** The closed physical path is a nontrivial positive Collatz cycle.

**Boundary.** A graph containing only contracting blocks, one proper denominator factor, an unreplayed carry edge, or a bounded low-scale block library is insufficient.

---

## `ACL-N082` — Reconcile the sparse-support frontier through seven defects

**Statement.** Independently reconstruct the overlapping sparse-cycle claims:

- PR #34 proposes complete exclusion of exactly five and exactly six non-`2` valuations;
- PR #51 independently proposes five defects and supplies only a bounded six-defect scout;
- PR #47 `T-9601` proposes a complete exact finite exclusion of exactly seven non-neutral valuations.

Return one exact verdict:

1. all complete claims pass, so every nontrivial positive cycle requires at least eight valuations different from two;
2. the first incomplete or false sparse-support class is identified exactly and reduced to a finite determinant/bilinear/carry problem;
3. an exact divisor hit is found, in which case reconstruct and replay the positive cycle immediately.

**Use.** Separates a bounded scout from complete proposed theorems and prevents agents from reopening all sparse-support families when only one support level or class is genuinely unsettled.
