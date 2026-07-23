# Global Collatz counterexample map

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36](https://github.com/gfreund123/collatz/issues/36)  
**Repository:** `gfreund123/collatz`  
**Reviewed snapshot:** [`ANALYSIS_SNAPSHOT_PASS_5.md`](ANALYSIS_SNAPSHOT_PASS_5.md)  
**Current delta:** [`CARTOGRAPHY_PASS_5.md`](CARTOGRAPHY_PASS_5.md)  
**Atomic handoffs:** [`ATOMIC_COUNTEREXAMPLE_LEMMAS.md`](ATOMIC_COUNTEREXAMPLE_LEMMAS.md)  
**Graph source:** [`docs/global-counterexample-map.mmd`](docs/global-counterexample-map.mmd)

## Scope and confidence vocabulary

For the shortcut map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

a full disproof is an explicit positive nontrivial cycle, an explicit positive orbit avoiding `1` forever, or a rigorously equivalent witness such as a third functional-graph component or coverage deficit.

| Color | Meaning |
|---|---|
| Green | proved or independently verified at one exact frozen source |
| Blue | source-inspected external theorem with native hypotheses audited |
| Orange | native proposed theorem or exact algebraic interface |
| Yellow | exact finite/source computation |
| Red | refuted, closed mechanism, or secret reduction |
| Grey | open construction or missing implication |

There is **no unconditional counterexample** in this snapshot.

## 1. The repository now has two global funnels

### Positive-cycle funnel

The cycle program is no longer a collection of unrelated searches. Its current layers are:

```text
cycle length and minimum-state bounds
 -> defect-support feasible region
 -> compressed block/carry or mechanical compiler
 -> fixed-cone / commutator eliminants
 -> prime-power compatibility
 -> entire denominator equality
 -> exact valuation replay.
```

The decisive object remains

\[
C(w)=n(2^A-3^k),
\]

for the **entire** denominator, followed by exact replay. Proper-factor hits, near integers, unreplayed carry edges, and bounded grammars are not certificates.

### Ordinary-divergence funnel

Four strong lanes now have one common state architecture:

\[
q=\rho_s+2^{E_s}\ell
\quad\longmapsto\quad
q'=\sigma_s+M_s\ell.
\]

A finite exact control state `s` and one ordinary quotient determine the physical block and next type. When the odd multiplier `M_s` refunds more information than the next dyadic radix consumes, every noncanonical lift grows. The remaining theorem is ordinary most-significant-boundary recurrence: find one finite root that belongs to the exact changing cylinder forever.

See [`cartography/ORDINARY_REFUND_MACHINES.md`](cartography/ORDINARY_REFUND_MACHINES.md).

## 2. Four ordinary multiplicative-refund machines

### PR #45: fixed six-branch chart

The exact chart has radix

```text
M=2^19,
N=9^6,
N-M=7153.
```

Its state is `(i,q)`. One residue test chooses the unique next branch and every legal transition strictly increases `q`. The physical embedding is explicit. One positive state defined forever would be an unconditional Collatz counterexample.

This is the smallest **fixed-scale** refund machine in the repository.

### PR #51: negative-three changing-run highway

The full ordinary chart is

```text
A: z=8q    ->9q,
B: z=1+16q ->1+9q,
physical n=6z-5.
```

The pass-4 map

```text
x -> 9x/8       or (9x+1)/16,
n=42x-5
```

remains exact, but is now correctly classified as the invariant subchart `z=7x` of the larger system.

The stronger state is the maximal-run quotient `(r,s,k)`. The run labels are outputs of a deterministic changing-modulus map. Every emitted run `r>=5` strictly increases the physical chart state by `9^6>2^19`. One forever-defined state whose emitted runs all remain at least five is a complete counterexample.

### PR #49: intrinsic changing-height core

The runtime state is

```text
(t,gamma,i,C),
gamma in {1,2,3},
i in {0,1,2,3},
gcd(C,6)=1.
```

It is recoverable from one physical integer

```text
n=2^(11t+5+i) 3^gamma C-34.
```

At every finite state there are exactly eight ordinary source cylinders. The decoder checks one high binary divisibility and one six-bit output cell; the next type is unique. Each legal connector replaces the prime-to-six core by a coprime core more than 170 bits larger.

The complete top-boundary modulus grows by exactly 176 bits per connector. Noncanonical lifts eventually more than double. Canonical lifts cannot absorb the architecture indefinitely: after height `3760` there are no 471 consecutive canonical lifts, and eventually no 234. Hence any hypothetical infinite path uses genuinely refunded top lifts with positive lower density.

Such a path must also introduce infinitely many globally new odd primes. This is the strongest changing-scale constructive lane, but existence is still open.

### PR #19: H renewal counter

Iteration 11 gives a deterministic renewal state

```text
(a,R,b,k).
```

For a transition from renewal type `tau` to `sigma`, one exact edge is

```text
k=eta_(tau,sigma)+2^q t
 ->
k'=zeta_(tau,sigma)+3^g t.
```

One finite tuple defined forever reconstructs a positive H orbit and therefore a Collatz counterexample. The edge domains satisfy the exact Kraft law

\[
\sum_{S,c\ge1}2^{-(3S+2c)}=\frac1{21};
\]

a specified `h`-renewal type path has relative Haar measure `21^{-h}`.

The finite refund graph already contains 353,835 refund edges, 42 refund self-loops, 34 refund SCCs, and one SCC of size 594. These are genuine engine data, but an SCC or periodic type path is not an ordinary root.

## 3. The exact 176-bit selector connection

PR #3 proves that one width-one linear connector consumes one new 176-bit top block. Its conditional correlated selector gadget projects onto all `b` output bits when its stated rank hypotheses hold; the unproved endpoint is exactly `b=176`.

PR #49 independently shows that the next complete top-boundary modulus gains exactly 176 bits per connector.

Thus the two branches meet at the same arithmetic scale:

```text
PR #3: expose/steer the next 176-bit block;
PR #49: consume that 176-bit block in the intrinsic physical decoder.
```

The missing theorem is causal orientation: derive the selector input from the current intrinsic core alone, force a legal next source cylinder, and prove ordinary top closure for all time. This is `ACL-P044`.

## 4. Positive-cycle feasible region

### Current source layers

- PR #45 proposes no nontrivial positive cycle through `50,000` accelerated odd states.
- PRs #13 and #50 propose exact exclusions at lengths 184 and 185.
- PR #47 proposes complete centered-support exclusions through 11 non-`2` valuations.
- PR #42 proposes support layers through 15 and records exact source computations with zero formal matches at supports 16 and 17.
- PR #53 proves that every fixed negative-cycle word has only finitely many possible hits in its entire coordinatewise upward pulse cone.

All these theorem-level claims retain their source status.

### New exact length-support bridge

Let

```text
k = odd-state length,
s = number of valuations different from 2,
R = k-s,
B = sum of the s non-neutral valuations.
```

Then

\[
A=B+2R\ge2k-s.
\]

The elementary least-state window for a nontrivial cycle gives

\[
2^A7^k\le22^k.
\]

Therefore every cycle satisfies

\[
\boxed{14^k\le11^k2^s.}
\]

Conditional on the proposed `k>=50001` floor, exact integer comparison gives

\[
11^{50001}2^{17396}<14^{50001}
\le11^{50001}2^{17397}.
\]

Hence

\[
\boxed{s\ge17397.}
\]

This does not make the support-16/17 computations incorrect; it relocates them as method-validation packets rather than candidates in the globally feasible region, conditional on the length theorem. See [`cartography/CYCLE_FEASIBLE_REGION.md`](cartography/CYCLE_FEASIBLE_REGION.md).

### Compiler convergence

The most complete constructive cycle route now combines:

```text
PR #45 block residue/carry decoding
 + PR #50 correct quotient-Hensel lifting
 + PR #47 normalized half-join and commutator sieves
 + PR #34 prime-power excess paths
 + PR #53 sparse-resultant fixed-cone caps
 -> full-denominator equality
 -> exact physical replay.
```

This is `ACL-N086`: either produce one full compatible circuit, or identify the first exact interface that cannot be made simultaneously compatible.

## 5. Closed or sharply narrowed mechanisms

| Mechanism | Standing | Consequence |
|---|---|---|
| frozen corrected 256-transition doubling class | independently excluded at frozen source | stop searching words/seams inside that class |
| fixed-modulus centered lasso | completion ghost | retain a true top boundary |
| finite control + zero-tested additive counter | proposed ultimately periodic | use nonlinear/changing-modulus or richer memory |
| permanent cross-cycle phase 1 | shifted ordinary Collatz | prove repeated exits/returns or a finite return |
| bare congruence sanctuary | independently reviewed proposed no-go | use genuine word-boundary memory |
| H `10/30` compiler | proposed physical descent/bounded multiplier | use refund edges or a new macro family |
| one fixed pulse support with unbounded pulse heights | finitely capped by PR #53 | vary repetition/baseline/support architecture |
| ambient cone or approximate spectrum | no witness extraction | produce an exact third component |

## 6. Remaining independent routes

### Centered `64 -> 81`

The exact forced tail

\[
64B'=81B+e-e'
\]

still requires a nonlinear/changing-modulus most-significant-boundary machine. The new common refund form suggests the correct abstraction, but no complete intrinsic quotient reduction has yet been published.

### Cross-cycle handoff

Issue #39 remains outside the frozen PR #33 class. Permanent phase 1 is a secret reduction to ordinary Collatz. A real result must prove repeated multi-phase return, a finite positive return, or a multi-phase invariant.

### Sanctuary and equivalent witnesses

A regular sanctuary remains a finite certificate only if its DFA retains canonical word-boundary information. Coverage, solution-cone, and spectral criteria remain exact but lack faithful third-component extraction.

## 7. Priorities

### By logical distance

1. **Full-denominator positive cycle.**
2. **Boundary-memory sanctuary DFA.**
3. **Forever-defined fixed six-branch chart state.**
4. **Forever-defined negative-three run-five highway.**
5. **Forever-defined PR #49 intrinsic core.**
6. **Forever-defined H renewal counter.**
7. **Centered nonlinear top-boundary seed.**
8. **Multi-phase cross-cycle return.**
9. **Exact third-component witness.**

### By architectural leverage

1. **Common multiplicative-refund top-boundary theorem** across PRs #19/#45/#49/#51.
2. **Causal 176-bit selector/refund coupling** between PR #3 and PR #49.
3. **Global cycle feasible-region audit and full-denominator compiler convergence.**
4. **PR #49 intrinsic core residue recurrence and fresh-prime generation.**
5. **Negative-three run-core top-boundary invariant.**
6. **H refund-SCC to ordinary-root extraction.**
7. **Centered intrinsic quotient reformulation.**

## Bottom line

The repository has not produced a counterexample, but the full-objective frontier is now much sharper:

```text
four exact deterministic ordinary refund machines;
one shared most-significant-boundary recurrence problem;
one exact 176-bit selector interface;
a proposed cycle length floor above 50,000;
conditional defect support at least 17,397;
fixed pulse cones finitely capped;
and a converging full-denominator compiler stack.
```

The most valuable next theorem is no longer “find a clever symbolic schedule.” It is one of:

1. a causal ordinary top-boundary invariant for one multiplicative-refund machine; or
2. one exact full-denominator cycle circuit with complete replay.
