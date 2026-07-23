# Global counterexample cartography — pass 5

**Cutoff:** `2026-07-23T05:05:04Z`  
**Jerusalem cutoff:** `2026-07-23T08:05:04+03:00`  
**Prior cutoff:** `2026-07-22T21:54:16Z`  
**Exact provenance:** [`ANALYSIS_SNAPSHOT_PASS_5.md`](ANALYSIS_SNAPSHOT_PASS_5.md)

## Executive update

The repository has changed category. Its strongest constructive work is no longer best described as several unrelated symbolic schedules. Four major lanes now share one exact **ordinary multiplicative-refund machine**:

```text
q=rho_s+2^E ell
 ->
q'=sigma_s+M_s ell.
```

The finite state `s` and ordinary quotient `q` determine the physical block and next type. When `M_s` dominates the dyadic radix, every noncanonical lift refunds the most-significant boundary. The sole unresolved theorem is whether one finite ordinary root meets the changing exact cylinders forever.

In parallel, the positive-cycle work has become a genuine funnel. Length, defect support, fixed pulse cones, factorwise quotient lifting, block carries, commutators, and full-denominator replay now constrain one another. A new exact bridge shows that, conditional on the proposed no-cycle-through-50,000 theorem, every surviving cycle needs at least **17,397 valuations different from two**.

No unconditional counterexample was found.

## 1. Four ordinary refund machines

### 1.1 Fixed six-branch chart — PR #45

PR #45 has a fixed chart with

```text
M=2^19=524288,
N=9^6=531441,
Delta=N-M=7153.
```

For six finite branch states, a current quotient `q` is legal exactly when

```text
r=[Delta q+e_i]_M
```

is one of six source digits `d_j`. The next quotient is

```text
q'=q+(Delta q+e_i-d_j)/M.
```

Every legal transition strictly increases `q`. The physical state is

```text
h=Mq+d_i,
n=-5+2h.
```

One finite `(i_0,q_0)` defined forever is therefore a complete positive unbounded Collatz orbit. This is the smallest current fixed-scale machine and becomes `ACL-P043`.

PR #45 further places it in an infinite family of fixed-weight fibers with length `L`, pulse count `b`, radix `2^(3L+b)`, odd multiplier `9^L`, and `binom(L,b)` exact branches. The six-branch chart is the first supercritical member, not an isolated curiosity.

### 1.2 Negative-three changing-run machine — PR #51

The complete negative-three block chart is

```text
A: z=8q    ->9q,
B: z=1+16q ->1+9q,
n=6z-5.
```

The pass-4 chart

```text
x ->9x/8 or (9x+1)/16,
n=42x-5
```

is exactly the invariant subchart `z=7x`. Its derivation and depth-31 frontier remain correct, but it is no longer the whole PR #51 architecture.

The stronger state comes from maximal runs. Immediately after `B`, write

```text
z=2^(3r)u,
u odd,
9^r u=1 mod16.
```

Then

```text
A^rB: z ->(9^(r+1)u+7)/16.
```

Two successive run labels determine one exact changing dyadic cylinder in an ordinary quotient. A third run gives an affine edge with multiplier `9^(r+1)`. The physical macro is strictly increasing for every emitted run `r>=5`, by the exact comparison

```text
9^6>2^19.
```

Thus `ACL-P042` is one finite `(r_0,r_1,k_0)` whose decoder remains defined forever and emits only runs at least five.

PR #51 also provides explicit reset highways

```text
z_m=(2^(m+4)-7)/9,
m=0 mod6,
```

with arbitrarily long exact finite prefixes. They prove unbounded finite survival depth, not an infinite root.

### 1.3 Intrinsic changing-height core — PR #49

PR #49 now strips away the connector coordinates completely. The runtime state is

```text
(t,gamma,i,C),
gamma in {1,2,3},
i in {0,1,2,3},
gcd(C,6)=1.
```

Set

```text
G=7(t+1)+gamma-beta_i,
D=11(t+17)-i,
X=3^G C+1.
```

A step is defined exactly when the prescribed power of two divides `X` and one six-bit physical output gate holds. The gate determines the next type uniquely. The associated physical integer is

```text
n=2^(11t+5+i)3^gamma C-34.
```

Every defined step is an exact physical Collatz connector. The primitive core is replaced by a coprime core more than 170 bits larger, and every hypothetical infinite orbit must create globally new odd primes infinitely often.

At the complete top boundary, every current state has four binary continuation cylinders and two ternary lifts per cylinder. The common modulus is

```text
H_t=2^(11(t+33)).
```

Since `t` increases by 16, the modulus gains exactly 176 bits per connector. Each edge has

```text
m=rho+H_t ell
 ->
m'=sigma+3^G ell.
```

The new pass-5 facts sharply reduce the apparent canonical escape:

1. from height 3776, every noncanonical `ell>=1` gives `m'>2m`;
2. two consecutive canonical lifts force a long zero most-significant block in the next exact residue over an explicit height range;
3. no path has 471 consecutive canonical lifts after height 3760;
4. eventually no path has 234 consecutive canonical lifts;
5. hence every hypothetical infinite path uses genuinely refunded lifts with positive lower density at least `1/471`, eventually `1/234`.

The remaining gap is now exactly residue recurrence: can one intrinsic core land in one of the four legal changing cylinders forever? This remains `ACL-P036` / `ACL-N076`.

### 1.4 H renewal counter — PR #19 iteration 11

H now has the same architecture. A renewal type is

```text
tau=(a,R,b).
```

Every positive bridge of that type is one ordinary counter progression

```text
X=x_tau+M_tau k.
```

For a next type `sigma=(b,S,c)`, exact stitching gives

```text
k=eta_(tau,sigma)+2^(3S+2c)t
 ->
k'=zeta_(tau,sigma)+3^(2R+a)t.
```

The next type is recovered from exact valuations. One finite `(a_0,R_0,b_0,k_0)` defined forever reconstructs a positive infinite H orbit and therefore a Collatz counterexample.

The domains of all possible next types are disjoint and satisfy the exact Kraft law

```text
sum_(S,c>=1)2^(-(3S+2c))=1/21.
```

Thus a specified `h`-renewal path has exact relative Haar measure `21^(-h)`. This quantifies thinness but does not prove emptiness.

A refund edge satisfies

```text
3^(2R+a)>=2^(3S+2c),
zeta>=eta,
```

which makes every ordinary point nondecreasing in the counter. The finite audit already contains 353,835 refund edges, 42 refund self-loops, 34 refund SCCs, and one SCC of size 594. These are genuine positive engine data but not ordinary witnesses. The longest frozen canonical-root refund chain has four transitions and then exits.

This exact positive target is now `ACL-P045`; the positive-or-negative decision is the sharpened `ACL-N080`.

## 2. The common top-boundary theorem

The four machines have different coordinates but the same unresolved object:

```text
finite exact control
+ one ordinary unbounded quotient
+ changing complete dyadic cylinder
+ odd multiplicative refund
+ exact physical replay.
```

This is not the additive one-counter architecture excluded by PR #34. The modulus changes, quotient division is nonlinear, and the most-significant boundary is part of the state.

The shared theorem target `ACL-N085` is:

1. construct one ordinary root in any machine and prove all-time domain recurrence; or
2. prove a completion-height, prime-renewal, or ranking theorem forcing every ordinary root to exit.

A fixed-modulus lasso, finite SCC, periodic type word, positive-density cylinder family, or abstract `Z_2` point is insufficient.

See [`cartography/ORDINARY_REFUND_MACHINES.md`](cartography/ORDINARY_REFUND_MACHINES.md).

## 3. The 176-bit selector connection

PR #3 independently reaches the same scale from the symbolic side. A width-one linear connector consumes exactly one new 176-bit moving top block. Its conditional correlated-selector theorem constructs complete dyadic projection through `b` bits if a family of full-offset gadgets exists with linear length.

At `b=176`, such a gadget would expose all `2^176` possible next top blocks—the exact increment in PR #49's complete modulus.

The missing coupling is causal:

```text
current intrinsic core
 -> choose one legal 176-bit next block
 -> physical selector gadget
 -> same intrinsic core interface at height t+16.
```

If the selector can force a noncanonical legal block at every stage, PR #49's refund and canonical-run theorems already supply the growth side. This becomes `ACL-P044`.

The branch currently has exact selector gadgets only through `b=6`; no `b=176` construction or all-time orientation theorem is claimed.

## 4. The positive-cycle funnel

### 4.1 Length floor

PR #45 proposes a computer-assisted exact theorem excluding every nontrivial positive accelerated cycle with at most 50,000 odd states. The packet uses the exact product identity to bound the minimum state by `1,447,682,232`, then exhaustively proves first drop below the start for every odd input in the required range.

This is proposed and has no independent repository review at its current source.

### 4.2 Sparse-support layers

The centered coordinate

```text
E_w=C_w-(2^A-3^k)
```

deletes every valuation `2`. Current layers are:

```text
PR #34: proposed complete support 5 and 6;
PR #47: proposed exact support 7 through 11;
PR #42: proposed support 7 through 15;
PR #42 X-8610: complete source-exact support 16, zero formal matches;
PR #42 X-8611: complete source-exact support 17, zero formal matches.
```

The support-16 and support-17 computations retain exact cyclic necklace representatives, enumerate every compatible gap vector and product-window cell, and replay every formal match. They remain source-exact computations pending an independent implementation.

### 4.3 New length-support bridge

Let `s` be the number of valuations different from two. Write `R=k-s`, let `B` be their sum, and note

```text
A=B+2R>=2k-s.
```

The least-state product window is

```text
2^A 7^k<=22^k.
```

Therefore every positive cycle satisfies

```text
14^k<=11^k 2^s.
```

Conditional on the proposed `k>=50001` floor, exact integer arithmetic gives

```text
11^50001 2^17396 <14^50001
                       <=11^50001 2^17397.
```

Hence the combined proposed chain forces

```text
s>=17397.
```

This is a major global reclassification. Support 16 or 18 may be the next open layer inside one sparse-support computation, but it is not the first globally feasible counterexample region if the 50,000-state theorem survives review.

The exact bridge and checker are in [`cartography/CYCLE_FEASIBLE_REGION.md`](cartography/CYCLE_FEASIBLE_REGION.md).

### 4.4 Fixed pulse cones are finite

PR #53 extends PR #51's two-pulse eliminants to arbitrary fixed finite support on one fixed negative-cycle word. Treating the pulse numerator and denominator as linear Laurent polynomials in each pulse variable gives a reduced Sylvester resultant

```text
E_i=U S_i H_i^-+Q H_i^+.
```

It proves

```text
D|H <=>D|E_i,
v_2(E_i)=A_(p_i+1),
E_i!=0,
```

and an explicit cap on every pulse coordinate. Therefore the entire coordinatewise upward pulse cone of one fixed negative-cycle word contains only finitely many possible positive-cycle divisibility hits.

This closes an important hidden resonance possibility. A viable pulse construction must now vary repetition length, baseline word, support architecture, or macro-block grammar rather than merely increasing pulse sizes in one fixed cone. This is `ACL-N083`.

### 4.5 Compiler convergence

The finite-cycle tools now form one coherent stack:

```text
PR #45 / PR #50:
  critical mechanical or fixed-weight straight-line program;

PR #50:
  correct quotient-Hensel digit at each newly added prime power;

PR #47 / PR #45:
  normalized centered half-join and exact block-carry decoder;

PR #47 / PR #53:
  commutator and sparse-resultant elimination of fixed subfamilies;

PR #34:
  lossless cross-prime excess-path compatibility;

final gate:
  C(w)=n(2^A-3^k) for the entire denominator
  plus exact physical replay.
```

PR #50's chart-to-mechanical bridge is especially useful: a chart symbol maps to the valuation pair `(2-e,2)`, preserving the same denominator parameters as the critical mechanical cycle. It also records the correct lifting datum

```text
(C/p^d)(D/p^d)^(-1) mod p^e,
```

rather than the numerator residue alone.

This integrated offense is `ACL-N086`; a positive output is the existing full-cycle atoms `ACL-P039` or `ACL-P041`.

## 5. H macro barriers remain relevant

Iterations 10 and 11 complement one another.

Iteration 10 proves that a finite macro family with only polynomial suffix-multiplier growth must have exponent at least

```text
1/log_2(plastic_constant)-1=1.464965255...
```

and that a finite directed macro grammar with no positive multiplier cycle cannot support a nonperiodic positive orbit. It also supplies an exact critical deficit law and a quantitative, though weak, fresh-prime lower rate.

Iteration 11 supplies the actual positive engine class—refund edges and refund SCCs—while preserving the ordinary-section firewall. A viable H construction must exploit positive multiplier cycles or unbounded macro state **and** exhibit one ordinary renewal counter.

## 6. Centered, cross-cycle, sanctuary, and equivalent routes

### Centered 64-to-81

The independently reviewed centered equivalence/cylinder/recurrence platform remains intact. Fixed-modulus PDR is exactly the completion ghost. Finite control plus one zero-tested additive counter is proposed periodic. The open certificate still needs nonlinear or changing-modulus top-boundary access.

The new refund-machine synthesis suggests recasting the centered forced tail in the common affine-cylinder form, with the actual most-significant quotient retained. No such complete reduction has yet been published.

### Cross-cycle handoff

Issue #39's scale-22 physical handoff remains outside the frozen corrected class. Permanent phase 1 remains conjugate to ordinary Collatz and is not a new amplifier. No new repeated multi-phase return theorem or explicit finite return was present at the cutoff.

### Sanctuary

The no-bare-congruence-sanctuary theorem remains independently passed at its frozen source. A sanctuary needs genuine word-boundary memory. The regular-language program remains a finite certificate route but has not produced an invariant language.

### Equivalent witnesses

Coverage deficit, solution-cone third rays, and point-spectrum support remain exact equivalent routes. The extraction theorem converting analytic data into a third functional-graph component remains missing.

## 7. Revised priorities

### By logical distance to a disproof

1. **Full-denominator positive cycle** — finite equality and replay.
2. **Boundary-memory sanctuary DFA** — finite closure certificate.
3. **Fixed six-branch quotient survivor** — smallest deterministic growing ordinary machine.
4. **Negative-three run-five highway survivor** — changing-run machine with physical growth automatic.
5. **PR #49 intrinsic changing-height core survivor** — strongest arithmetic structure and canonical-run control.
6. **H forever-defined renewal counter** — exact one-counter normal form and refund graph.
7. **Divisible-seven `9/(8,16)` subchart survivor** — still exact, now recognized as a restricted PR #51 lane.
8. **Centered nonlinear top-boundary survivor**.
9. **Multi-phase cross-cycle return**.
10. **Exact third-component witness**.

### By architectural leverage

1. **Common multiplicative-refund top-boundary theorem** across PRs #19/#45/#49/#51.
2. **PR #49 residue recurrence plus 176-bit selector coupling**.
3. **Global cycle feasible-region review and compiler convergence**.
4. **PR #45 fixed six-branch and fixed-weight chart family**.
5. **PR #51 changing-run quotient and reset-highway recurrence**.
6. **H refund SCC to ordinary-root extraction**.
7. **Centered conversion to a true changing-boundary quotient machine**.
8. **Cross-cycle repeated-return invariant**.

## Bottom line

The fifth pass finds no counterexample, but it clarifies the global problem much more sharply than a list of branch results.

The divergent-orbit frontier is now:

```text
four exact deterministic ordinary refund machines,
one shared most-significant-boundary problem.
```

The finite-cycle frontier is now:

```text
k beyond 50,000,
conditional defect support at least 17,397,
no fixed pulse-cone resonance,
full factorwise quotient lifting and exact replay still required.
```

The best chance of a breakthrough is no longer a deeper blind cylinder search. It is either:

1. a causal top-boundary invariant for one multiplicative-refund machine; or
2. a full-denominator circuit operating inside the actual large-length/high-support feasible region.
