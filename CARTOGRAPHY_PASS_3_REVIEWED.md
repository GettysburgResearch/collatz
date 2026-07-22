# Global counterexample cartography — reviewed pass 3 replacement

**Final cutoff:** 2026-07-22 20:46:30 UTC  
**Previous published cutoff:** 2026-07-22 20:10:33 UTC  
**Exact provenance:** [`ANALYSIS_SNAPSHOT_PASS_3R.md`](ANALYSIS_SNAPSHOT_PASS_3R.md)  
**Quality audit:** [`PASS_3_QUALITY_AUDIT.md`](PASS_3_QUALITY_AUDIT.md)

## Executive correction

The first pass-3 publication was mathematically useful but not audit-grade. This replacement:

1. freezes exact source SHAs through PR #49;
2. integrates PR #44's successful frozen-source review of PR #33;
3. incorporates PR #48's independent review of PR #45 and its explicit non-reproduction boundary for PR #42 `T-8602`;
4. replaces the old 256-stage refund target by PR #49's width-one deterministic decoder;
5. incorporates PR #34 wave 25 and PR #19 iteration 8;
6. retires duplicate atom `ACL-P038` in favor of canonical `ACL-P036`;
7. records that permanent cross-cycle phase 1 is shifted ordinary Collatz.

No unconditional counterexample was found.

## 1. Frozen corrected phase-34 class: independently verified negative result

PR #44 independently reconstructed PR #33 at

```text
PR #33: c9d62bce3e93f5785f72e4520bc576863d9379eb
PR #3 interface: f274dfeee3c9c391c48e58d8b57cb9f1759236f8
```

and returned `PASSED` for

```text
L-9704 -> L-9705 -> L-9706 -> T-9705.
```

The frozen corrected 256-transition doubling-scale phase-`-34` class has no signed ordinary completion. This is green at the frozen-source confidence level; native-ledger integration remains pending.

The result does not cover linear-height refund, cross-cycle handoffs, adaptive/growing-rank stages, or persistent degeneracy. Room/seam search inside the frozen class is no longer a constructive counterexample path.

## 2. Positive cycles: shortest certificate, stronger support floor

A positive cycle remains logically closest to a disproof because the final certificate is finite.

### Bounded packets

PR #42's source packet reports all admissible cycle windows through 27 accelerated odd terms, with `802,459,998,516` compositions and zero modular matches, plus `35,548,596,168,868` words in two `(41,65)` low-complexity families with zero matches. PR #48 found the finite-window/MITM logic coherent but did **not** execute the full census, so the global status remains source `PROPOSED` plus exact source computation—not independently reproduced.

PR #13 proposes exclusion of odd-state length 184. PR #34 wave 25 further proposes that every nontrivial positive cycle has at least seven valuations different from two: the exact five- and six-defect frontiers are empty.

### Critical-scale compiler

PR #48 independently passes PR #45's frozen compiler, block-replacement formula, and rejected trillion-symbol near-candidate. The compiler is therefore green at its frozen source; the positive equality remains open.

The live finite target is still

```text
C(w)=n(2^A-3^k)
```

for the entire denominator, followed by exact valuation replay. Proper-factor divisibility and near-integer intervals do not count.

### Cross-prime state

PR #34 `L-9914` gives a lossless factorwise compiler: compatible prime-power excess paths reconstruct at most one monotone word in the strict full-order window, and local periodic aliases must collectively span the full primitive period. This turns cross-prime compatibility into the correct finite state, but constructs no compatible full-factor tuple.

## 3. Distributed negative-cycle pulses: exact reduction sharpened

PR #47 proves the one-pulse reduction and reports 720,000 reduced candidates with only the trivial cycle.

PR #34 wave 25 gives the exact arbitrary-pulse form. For a negative cycle with states `z_i`, prefix exponents `A_i`, pulses `delta_i`, cumulative `Delta_i`, and

```text
b_i=-(3z_i+1)>0,
D_delta=2^(B+Delta)-3^N,
```

one has

```text
C_delta=z_0 D_delta+R_delta,
R_delta=sum_i b_i(2^delta_i-1)2^(A_i+Delta_i)3^(N-i-1).
```

Therefore:

```text
integrality  <=>  D_delta | R_delta,
positivity   <=>  z_0+R_delta/D_delta>0.
```

For two pulses at `i<j` with fixed total `T`, the remainder is

```text
R=U_j 2^T+(U_i-U_j)2^delta-U_i,
U_t=b_t2^A_t3^(N-t-1),
```

so the exact two-pulse search reduces to one exponential congruence modulo the full denominator. No hit is known. An independent two-pulse agent is active.

The research target is `ACL-P037`: critical-scale full-factor compatibility, not low repetition controls.

## 4. Linear-height quotient refund: now a deterministic expanding decoder

This lane advanced materially during the audit.

### Width one is atomic

PR #49 proposes exact fixed-width exponents

```text
A_L(B)=7L(B+1)+56L(L-1),
E_L(B)=11L(B+1)+88L(L+1),
```

and refund whenever

```text
5B>9288L+9363.
```

The least qualifying multiples of 16 include

```text
L=1:   B=3744,
L=256: B=477424.
```

Thus one connector—not a 256-transition stage—is the atomic constructive object.

### Causal connector compiler

PR #49 gives a finite ordinary inverse-carry recurrence and exact six-bit connector normal form. The state is

```text
(t, source type i, target type j, residual z).
```

The next connector is defined exactly when one large divisibility test and one four-cell membership test pass. The next type is unique. When defined,

```text
z'=(Nz+theta-eta')/M'.
```

For every multiple of 16 with `t>=3744`,

```text
z>=1 and legal  =>  z'>=2z.
```

Hence growth, positivity, and type selection are automatic once one finite residual has an infinitely defined decoder path. The physical initialization is explicit in PR #49.

### Independent parallel boundary

PR #48 proves that an already-coherent positive lift path doubles after a stronger two-stage threshold and quantifies the selector deficit: a fixed 256-word offers at most `2^512` next classes while the first next modulus has over 1.36 billion bits. It also proves that a fixed directive still selects one nested dyadic cylinder; refund does not erase ordinary stabilization.

The sole positive gap is now sharply stated:

> Find one finite tuple `(t_0,i_0,i_1,z_0)`, with `t_0>=3744` and `z_0>=1`, and an inductive invariant proving the deterministic decoder is defined forever.

This is canonical `ACL-P036`.

PR #49 also proposes zero-dimensional completion pressure and excludes eventually periodic type directives through minimal period 58. Thinness and periodic exclusion do not prove emptiness.

## 5. Centered forced tail: exact one-counter problem, additive subcase closed

PR #44 proves the exact forced-tail map

```text
64B'=81B+e-e',
```

with bounded carry, invariant `B+4e mod17`, and strict growth on positive legal states. Fixed-modulus PDR is exactly the periodic cylinder ghost.

PR #34 `L-9915` now closes a restricted next step: deterministic finite control plus one zero-tested additive counter, even with fixed residue observations and positive drift, emits an ultimately periodic output and cannot produce a positive centered tail.

A viable centered certificate must therefore use genuine top-boundary access, nonlinear/changing-modulus updates, a stack, or more than one effective unbounded register. The remaining positive target is still one explicit positive seed with canonical most-significant closure.

## 6. Cross-cycle handoff: phase 1 is a secret reduction

Issue #39's scale-22 cell and physical handoff remain exact finite evidence outside the frozen class. But in phase `v=1`, with `q=n+1`,

```text
(q,1) -> (T(q-1)+1,1).
```

A permanent phase-1 tail is exactly ordinary Collatz in a shifted coordinate. A genuine cross-cycle certificate must prove repeated exits/returns among nontrivial phases, a finite positive return before permanent phase 1, or a multi-phase invariant.

## 7. H: strong finite-cycle and structured-language barriers

PR #19 iteration 8 proposes no positive exact H block cycle through

```text
2,479,700,524 blocks.
```

It also proposes:

- a factor-entropy lower bound for finite-alphabet survivors with logarithmic capital;
- exclusion of zero-entropy finite-alphabet codes with logarithmic capital;
- an exact prefix-return versus capital inequality;
- exclusion of `{2,3}` templates with certified return constant at most 84.

A viable H witness must combine delayed novelty or positive entropy, sufficient capital/reset growth, infinitely many fresh bridge primes, eventual ordinary carry stabilization, and a positive all-time initialization.

## 8. Sanctuary and equivalent witnesses

PR #48 independently passes PR #42 `T-8601`: no nonempty forward-invariant union of complete residue classes can avoid the trivial cycle. A sanctuary must retain genuine canonical-word boundary memory.

Coverage deficit, solution-cone third rays, and spectral excess remain exact equivalent routes, but no current packet extracts the required third component.

## 9. Corrected priorities

### By logical distance

1. **Full-denominator positive cycle** — critical mechanical or distributed-pulse/cross-prime circuit.
2. **Regular sanctuary DFA** — finite closure with word-boundary memory.
3. **Forever-defined refund decoder** — PR #49 makes growth and positivity automatic.
4. **Centered height/top-boundary seed** — additive one-counter subcase is closed.
5. **Multi-phase cross-cycle return** — avoid permanent phase-1 reduction.
6. **Positive H survivor** — delayed novelty/reset renewal required.
7. **Equivalent third-component witness**.

### By architectural leverage

1. **PR #49 refund decoder infinite-definedness**
2. **PR #45 full-denominator critical compiler**
3. **PR #34/issue #46 cross-prime distributed pulses**
4. **PR #44 centered nonlinear top-boundary machine**
5. **PR #19 delayed-novelty/reset-renewal frontier**
6. **Issue #39 repeated multi-phase regeneration**

## Bottom line

The replacement finds no unconditional counterexample.

It does reveal a significantly sharper positive path than the flawed pass reported:

```text
PR #49 already supplies an exact deterministic physical decoder,
unique next type, positivity, and exponential residual growth.
```

The entire divergent-orbit obligation has collapsed to one question: can one finite ordinary residual remain in the decoder domain forever? That is now the strongest explicit constructive target in the repository.
