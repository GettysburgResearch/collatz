# Global counterexample cartography — pass 4

**Cutoff:** `2026-07-22T21:54:16Z`  
**Prior reviewed cutoff:** `2026-07-22T20:46:30Z`  
**Exact provenance:** [`ANALYSIS_SNAPSHOT_PASS_4.md`](ANALYSIS_SNAPSHOT_PASS_4.md)

## Executive update

The fourth pass changes the constructive map in seven important ways.

1. PR #49 reduces the linear-refund lane to one deterministic partial map on the finite ordinary state `(t,i,k)`; every obligation except infinite definedness is proposed solved.
2. PR #49 further makes that state intrinsically recoverable from one physical integer and proves a fresh-prime necessity for every hypothetical infinite path.
3. PR #51 gives complete finite caps on all two-pulse sizes for each fixed negative-cycle packet and exposes a very small exact ordinary block chart.
4. The negative-three block chart contains a previously unrecorded invariant `h=21x` section with the fixed `9/(8,16)` map; one all-time positive path would be a full Collatz counterexample.
5. PR #45 and PR #47 supply complementary block-carry and commutator interfaces that can be combined with PR #34's cross-prime compiler into a critical mixed-drift cycle circuit.
6. PR #47 proposes an exact seven-defect exclusion, raising the proposed positive-cycle support floor from seven to eight non-`2` valuations.
7. H iteration 9 closes the adaptive `10/30` compiler at proposed level and identifies a general physical-macro gate: abstract tail freedom is irrelevant unless zero-carry macros are nondescending and their multiplier escapes.

No unconditional counterexample was found.

## 1. Linear refund: the state is now only `(t,i,k)`

PR #49 `L-8503` uses the Bezout data

```text
N=3^(7(t+1)),
M=2^(11(t+17)),
Nr=1+Mc
```

and the complement coordinate

```text
W_(t,i)(k)=b_i(M-r)+Mk,
W^+_(t,i)(k)=b_i(N-c)+Nk.
```

They satisfy

```text
M W^+=N W+b_i,
W mod64=p_i.
```

The low six bits of `k` select at most one target type. Complete continuation to height `t+16` is one residue class modulo the next power-of-two radix. Thus the target type and connector edge are outputs of the current ordinary counter rather than externally supplied directive data.

`T-8504` packages this as a deterministic partial map

```text
F(t,i,k)=(t+16,j,k').
```

For `t>=3744` and `k>=256`, every legal transition satisfies

```text
k'>=2k.
```

The physical start is explicit:

```text
n_0=2^(11(t_0+1))
    [b_(i_0)(M_0-r_0)+M_0k_0]/64
    -34.
```

Therefore a single finite state whose map is defined forever already proves exact physical replay, positivity, and unboundedness.

The full positive target is now exactly:

```text
find (t_0,i_0,k_0),
t_0>=3744,
k_0>=256,
whose deterministic map is defined forever.
```

This is a much smaller statement than the earlier 256-stage word-selection problem. It remains an ordinary top-boundary problem, not a residue-only search: each local domain is a very thin full residue condition at a changing modulus, and zero-dimensional completion pressure does not prove emptiness.

### One physical integer is the entire state

PR #49 `L-8504` places the consecutive boundary words in a determinant-one basis. The physical boundary integer satisfies

```text
v_2(n+34)=11t+5+i,
```

so its valuation modulo `176` recovers the current type `i`, then the exact height `t`; the odd boundary word recovers `k`. A counterexample verifier can therefore begin with a single written integer `n_0`, reconstruct `(t_0,i_0,k_0)`, and iterate the deterministic map. There is no hidden external marker or future directive.

### Any survivor must manufacture fresh primes forever

PR #49 `T-8505` proposes a sharp arithmetic necessity. Every boundary word has an odd prime divisor at least `5`, no such prime divides two adjacent words, and Evertse finiteness excludes eventual support on any fixed finite prime set. Hence an infinite refund path must introduce infinitely many globally new odd primes into `n_j+34`.

This is not an existence theorem. It does rule out fixed-`S` invariants and shows what a positive definedness proof must accomplish: generate the exact changing-modulus address **and** fresh arithmetic support forever.

## 2. Two-pulse negative-cycle families are finite packet by packet

PR #51 rotates two pulse positions so the first is at zero and the second is at the shorter cyclic gap `g`. For a repeated negative cycle, it defines

```text
D=UXM-Q,
R=X(beta M+gamma)-alpha
```

and proves the full numerator split

```text
C'=z_0D+2^a_0 3^(N-g-1)R.
```

Hence

```text
D|C' <=> D|R.
```

The eliminants

```text
K(M)=Q(beta M+gamma)-UM alpha,
J(X)=U(X gamma-alpha)+beta Q
```

satisfy

```text
D|R <=> D|K(M) <=> D|J(X).
```

`K` is odd and nonzero. `J` is nonzero because its two terms have distinct `2`-adic orders. Consequently every fixed repetition/rotation/gap has explicit finite caps on **all** positive pulse sizes, not merely the first few threshold increments.

The exact frozen scans report:

```text
all-size two-pulse candidates:     16,445,391
bounded three/four-pulse candidates:24,192,960
nontrivial exact cycles:                    0
```

The only two-pulse hit is the trivial `(1,2)^2 -> (2,2)^2`, `n=1`.

This does not close distributed pulses globally. It does remove a hidden concern: there is no unbounded pulse-size resonance inside one fixed two-pulse packet. A successful pulse construction must vary repetition, gap, support size, or macro-block type at the critical global scale and still satisfy every prime-power factor of the full denominator.

## 3. New direct divergent lane: the `9/(8,16)` pulse chart

PR #51 `O-8001` gives the exact negative-three block chart

```text
h=8q       -> 9q,
h=3+16q    -> 3+9q,
n=-5+2h.
```

The multiple-of-21 section is invariant. Put

```text
h=21x.
```

Then the chart becomes

```text
G(x)=9x/8        if x == 0 mod 8,
G(x)=(9x+1)/16  if x == 7 mod 16,
undefined       otherwise,
```

with physical state

```text
n=42x-5.
```

The two branches replay exactly the accelerated valuation blocks

```text
A=(1,2),
B=(2,2).
```

The trivial physical cycle is absent from positive integral `x`, because `n=1` would require `x=1/7`.

Therefore:

```text
one positive x_0 whose G-orbit is defined forever
 -> one ordinary positive Collatz counterexample.
```

A repeat gives a nontrivial cycle. A nonrepeating infinite positive integer orbit is unbounded.

Every finite binary word is realizable by one residue class modulo its accumulated dyadic denominator. Thus this chart is not solved by deeper finite search; it has the familiar ordinary-section boundary in the smallest arithmetic form currently present in the repository.

### Exact depth-31 minimum

An original exact C++ cylinder enumerator exhausts every `4,294,967,294` finite prefix word at depths `1..31`. It finds

```text
least x surviving 31 blocks:
24643395416689283212736;

physical n=42x-5:
1035022607500949894934907.
```

This state survives exactly 31 chart blocks and then exits; every smaller positive `x` exits sooner. A separately written Python verifier independently reproduces all minima through depth 20 and replays the full frozen depth-31 physical trajectory. The full depth-31 minimum is exact finite evidence, not an infinite extrapolation.

### H-style renewal form

A positive finite integer cannot follow `A` forever, so any positive all-time path has infinitely many `B` blocks. Group from one `B` to the next, with `r` intervening `A` blocks, and set `p=16x`. Then

```text
p_next=[3^(2r+2)/2^(3r+4)]p+1.
```

This is a toll-one renewal exactly analogous to H, with multiplier

```text
a_r^pulse=(3/4)a_r^H
```

and critical mean

```text
kappa_pulse=log(16/9)/log(9/8)
           =4.8849491923617...
```

The strongest immediate research question is whether PR #19's cycle-minimum, entropy/capital, prefix-return, fresh-prime, renewal-height, and endpoint-product methods can be rebuilt for this simpler chart—or whether the chart supplies the first ordinary survivor.

The proof and finite interface checker are in:

- `cartography/PULSE_CHART_SYNTHESIS.md`;
- `cartography/check_pulse_chart.py`.

## 4. Cycle synthesis: three exact compilers now line up

### Ordered-jump frontier reaches length 185

PR #50 proposes exclusion of every positive accelerated cycle with exactly 185 odd states, conditional on the cited 92-local-minimum theorem.

A length-185 ascent/descent skeleton with 92 minima has one equal adjacent pair. Up to rotation there are only two families:

```text
AA: 1,1,b_0,1,b_1,...,1,b_91,
DD: 1,b_0,b_1,1,b_2,...,1,b_92.
```

Both admit an ordered-jump identity

```text
C(w)=C_0+sum_r 2^r S_(j_r)
```

with strictly separated suffix valuations. Each `(height,multiplier)` therefore has at most one decoded word. Finite scans through height 30 plus a reference-height stability induction propose exclusion of every larger height.

This advances the local-minimum frontier from 184 to 185, but it is not the global critical-height frontier and has no independent review yet. The constructive next packet is length 186.

### Block residue inversion

PR #45 `L-8404` proves that for fixed accelerated length and valuation total, one residue

```text
C_w mod2^A
```

decodes at most one positive valuation word. A candidate base state and boundary carry therefore select at most one block of each shape. Positive-drift block alphabets reduce to finite carry reachability, and a closed carry path followed by exact replay gives a cycle.

This replaces enumeration of enormous block alphabets by one exact residue inversion per carry and shape.

### Opposite-drift commutator sieve

PR #47 `L-9604` treats a negative-drift block `u` repeated `m` times followed by a positive-drift block `v` repeated `n` times. With commutator

```text
Omega=(q-p)d-(s-r)c,
```

the mixed denominator must satisfy

```text
D_(m,n) | G_m Omega.
```

Once `D_(m,n)>|G_m Omega|`, that `n` and every later `n` are impossible. Thus each fixed block pair and first repetition has an exact finite all-`n` search.

### Combined offense

Together with PR #34 `L-9914`, these form a coherent critical-scale architecture:

```text
block shape + carry
 -> unique decoded valuation block
 -> commutator cap on repeated opposite-drift runs
 -> compatible prime-power excess paths
 -> full-denominator equality
 -> exact physical replay.
```

This is `ACL-P041`. It is more general than a mechanical word with local swaps and more structured than raw composition enumeration.

## 5. Support floor reaches eight at proposed level

PR #34 proposes complete exclusions through exactly six valuations different from two. PR #51 independently proposes the five-defect case and supplies only a bounded six-defect scout.

At the final pass-4 cutoff, PR #47 `T-9601` adds a proposed exact finite certificate for exactly **seven** non-neutral valuations. Centering at the trivial fixed point removes every valuation `2`; a largest-neutral-gap reduction, contraction classification, finite residual rows, and independent source-side enumeration report zero divisor hits. Combined with the earlier proposed claims, every nontrivial positive cycle would require at least

```text
eight valuations different from 2.
```

This is a source-proposed support floor, not yet an independently reviewed global theorem. The status hierarchy must remain explicit:

```text
PR #34 L-9913: proposed complete six-defect exclusion;
PR #51 X-8004: bounded six-defect scout only;
PR #47 T-9601: proposed complete seven-defect exclusion.
```

`ACL-N082` is therefore broadened from a six-defect reconciliation into a **through-seven support-floor audit**. A review should reconstruct the first unsupported class, if any, rather than reopening all sparse-support families at once.

## 6. H iteration 9 closes the `10/30` compiler

PR #19 `L-9524` gives a physical macro test. If a contracting macro has canonical input above its real fixed point, every zero-carry use strictly lowers the positive endpoint. A finite family of such macros cannot occur forever.

For the adaptive compiler suffixes:

```text
f_10(Y)=(81Y+56)/128,       Y>=72,
f_30(Y)=(6561Y+3584)/8192, Y>=4608,
```

both macros strictly descend on the physical zero-carry slice.

Removing the terminal zeros leaves the aperiodic `3/1` irrational-rotation core. Its cumulative multiplier is bounded. Were it an exact positive orbit, the toll identity would give `p_n=Theta(n)` and divergent harmonic mass, contradicting the prior H survivor constraints.

Thus:

```text
abstract 2-adic tail surjectivity
!= physical ordinary counterexample freedom.
```

A live H construction now needs a different macro family satisfying all of:

```text
zero ordinary carry,
integer nondecrease,
cumulative multiplier escape,
exact cylinder closure,
one positive finite initialization.
```

The pulse-chart renewal in Section 3 is a natural new test bed for these methods, although its coefficients and critical mean differ and must be audited natively.

## 7. Updated global split

### Finite certificates

The shortest logical routes remain:

1. full-denominator positive cycle;
2. boundary-memory sanctuary DFA.

### Small deterministic ordinary charts

Two explicit partial maps now dominate the divergent-orbit side:

1. PR #49's changing-modulus complement counter `(t,i,k)`;
2. the fixed `9/(8,16)` pulse chart `G(x)`.

Each has one ordinary integer state, no external future directive, exact physical replay, and one missing all-time domain theorem. Their arithmetic difficulties are different enough to justify parallel work.

### Secret reductions and closed templates

The following do not themselves create a counterexample:

- fixed-modulus centered lassos;
- permanent cross-cycle phase 1;
- H's `10/30` compiler;
- additive zero-tested one-counter output controllers;
- bounded two-pulse packets;
- proper-factor or near-integer cycle hits.

## 8. Corrected priorities

### By logical distance

1. **Full-denominator positive cycle** — use the mixed-drift carry/cross-prime circuit or critical mechanical compiler; any witness must now carry at least eight non-`2` valuations if the proposed support chain survives review.
2. **Boundary-memory sanctuary DFA.**
3. **Forever-defined fixed pulse chart** — `ACL-P040`.
4. **Forever-defined PR #49 complement counter** — `ACL-P036`.
5. **Centered nonlinear top-boundary seed.**
6. **Multi-phase cross-cycle return.**
7. **Positive H survivor outside `10/30`.**
8. **Equivalent third-component witness.**

The pulse chart is placed ahead of refund by logical simplicity, not by evidence that a survivor exists.

### By architectural leverage

1. **PR #49 complement-counter infinite definedness.**
2. **Negative-three `9/(8,16)` pulse chart and H transfer.**
3. **Critical mixed-drift block-carry cycle circuit.**
4. **PR #45 full-denominator mechanical circuit.**
5. **Centered nonlinear/changing-modulus top-boundary machine.**
6. **H physical expanding macro search.**
7. **Cross-cycle repeated phase return.**

## Bottom line

No unconditional counterexample appears in this pass.

The positive frontier is nevertheless more concrete than before. The repository now contains two tiny deterministic ordinary-state questions whose positive resolution immediately settles the full objective:

```text
PR #49:
  one physical integer n whose intrinsic (t,i,k) marker
  remains in the changing-modulus decoder forever
  while generating infinitely many fresh odd primes;

pulse chart:
  one x>0 whose fixed map
  x -> 9x/8 or (9x+1)/16
  is defined forever.
```

The second chart is a newly exposed exact bridge between negative-cycle pulse constructions and H-style renewal analysis. It is the main original synthesis of this pass.
