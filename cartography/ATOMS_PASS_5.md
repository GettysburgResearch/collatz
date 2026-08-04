# Atomic counterexample problems — pass 5

These are the new or materially sharpened standalone handoffs from the fifth cartography pass. They are cartography formulations unless explicitly marked otherwise.

## Existing-atom updates

### `ACL-P036` — Intrinsic changing-height core survivor

Replace the pass-4 complement-counter description by PR #49's intrinsic runtime state

```text
(t,gamma,i,C),
gamma in {1,2,3},
i in {0,1,2,3},
gcd(C,6)=1.
```

One physical integer recovers the state. Every defined step has exact physical replay, unique next type, primitive-core growth exceeding 170 bits, adjacent coprimality, and required fresh-prime turnover.

At the complete top boundary, the current quotient has four legal residue cylinders modulo

```text
2^(11(t+33)),
```

with two ternary lifts each. Noncanonical lifts eventually more than double; canonical runs have uniformly bounded length and cannot absorb an infinite orbit.

**Positive certificate.** Give one explicit physical integer whose intrinsic decoder is defined forever.

**Full-conjecture implication.** Its shortcut-Collatz orbit is positive and unbounded.

### `ACL-N076` — Intrinsic-core residue recurrence decision

Prove one of:

1. every ordinary intrinsic state eventually misses all four complete next cylinders;
2. the forced fresh-prime and coprime-core renewal is incompatible with all-time residue landing;
3. the canonical/noncanonical dichotomy yields a ranking or completion-height contradiction;
4. one state survives forever, in which case publish `ACL-P036`.

A proof must use the changing most-significant boundary, not a fixed-modulus lasso.

### `ACL-P040` — Divisible-seven negative-three subchart survivor

The pass-4 map remains exact:

```text
G(x)=9x/8        if x=0 mod8,
G(x)=(9x+1)/16  if x=7 mod16,
n=42x-5.
```

It is now classified as the invariant subchart `z=7x` of PR #51's full negative-three chart. It remains a complete positive atom, but the broader run-core atom below has greater architectural reach.

### `ACL-N080` — H renewal-counter decision

Replace the earlier qualitative delayed-novelty formulation by PR #19 iteration 11's exact renewal state. A positive H witness is one finite

```text
(a_0,R_0,b_0,k_0)
```

whose deterministic type/counter decoder is defined forever. A stronger witness eventually uses only refund edges. The negative alternative proves every ordinary renewal counter exits.

---

## `ACL-P042` — Negative-three run-five highway survivor

**Statement.** In PR #51's full chart

```text
A: z=8q    ->9q,
B: z=1+16q ->1+9q,
n=6z-5,
```

use maximal-run normalization after each `B` edge. Construct one explicit finite quotient state

```text
(r_0,r_1,k_0)
```

whose deterministic changing-modulus decoder is defined forever and emits

```text
r_j>=5
```

at every later macro.

Every such macro strictly increases the physical state by the exact inequality `9^6>2^19`.

**Full-conjecture implication.** The reconstructed positive Collatz orbit is unbounded.

**Required proof object.** Explicit root state, exact changing-modulus invariant, every emitted run, physical block replay, and an independent verifier. A reset highway of arbitrary finite length does not count.

---

## `ACL-P043` — Fixed six-branch quotient survivor

**Statement.** For PR #45's six-branch fixed chart with

```text
M=2^19,
N=9^6,
Delta=N-M,
```

find one finite state `(i_0,q_0)` whose deterministic partial map

```text
r=[Delta q+e_i]_M,
r=d_j,
q'=q+(Delta q+e_i-d_j)/M
```

is defined forever.

Every legal transition has `q'>q`; the physical initialization is

```text
h=Mq_0+d_(i_0),
n_0=-5+2h.
```

**Full-conjecture implication.** The physical orbit is a positive unbounded Collatz orbit.

**Why atomic.** It is the smallest current fixed-scale counterexample machine: six control states, one integer counter, one modulus, and strict growth with no threshold.

---

## `ACL-P044` — Causal 176-bit selector/refund coupling

**Statement.** Prove PR #3's conditional correlated selector at `b=176`, and orient it causally inside the width-one phase-`-34` connector so that the current ordinary intrinsic state selects one legal next 176-bit top block without consulting future cylinder digits.

The coupled gadget must:

1. expose every required 176-bit next-block value;
2. preserve exact physical overlap into PR #49's intrinsic core interface;
3. force a noncanonical refunded lift or otherwise certify the selected canonical case;
4. return to the same finite-state-plus-one-counter form;
5. start from one explicit positive integer.

**Full-conjecture implication.** Repeated causal selection yields `ACL-P036` and an unbounded positive Collatz orbit.

**Boundary.** A complete projection code without causal orientation, or one finite selected block, is insufficient.

---

## `ACL-P045` — H forever-defined renewal counter

**Statement.** Using PR #19 iteration 11, exhibit one explicit

```text
(a_0,R_0,b_0,k_0),
a_0,R_0,b_0>=1,
k_0>=0,
```

whose exact deterministic transition

```text
k=eta_(tau,sigma)+2^(3S+2c)t
 ->
k'=zeta_(tau,sigma)+3^(2R+a)t
```

is defined at every future renewal.

A stronger certificate proves that all sufficiently late edges are refund edges and strict refund occurs infinitely often.

**Full-conjecture implication.** PR #19 reconstructs a positive infinite H orbit and hence a positive Collatz orbit avoiding `1`.

**Boundary.** A refund SCC, periodic type lasso, `21^{-h}` cylinder estimate, or long finite counter path is not a witness.

---

## `ACL-N083` — Fixed pulse cone versus growing architecture

**Statement.** Reconstruct PR #53's sparse-resultant theorem and decide the remaining negative-cycle pulse frontier:

1. every fixed word and fixed support has explicit finite coordinate caps;
2. prove a uniform repetition-length bound or a finite union theorem, thereby closing the entire known-negative-cycle upward-pulse lane; or
3. construct a genuinely growing baseline/support/macro architecture that escapes fixed-cone finiteness and satisfies the full denominator.

A pulse-size search inside one fixed cone is no longer a frontier computation.

---

## `ACL-N084` — Global positive-cycle feasible-region audit

**Statement.** Independently reconstruct:

1. PR #45's proposed exclusion through 50,000 odd states;
2. the elementary product window `2^A 7^k<=22^k`;
3. the identity `A=B+2(k-s)` with `B>=s`;
4. the derived inequality
   ```text
   14^k<=11^k 2^s.
   ```

Return one exact verdict on the conditional region

```text
k>=50001,
s>=17397.
```

The exact threshold certificate is in `cartography/check_cycle_feasible_region.py`.

**Use.** Distinguishes a method-local first open support cell from the globally feasible counterexample region.

---

## `ACL-N085` — Common multiplicative-refund top-boundary theorem

**Statement.** For one or more of the exact machines

```text
q=rho_s+2^E ell
 ->
q'=sigma_s+M_s ell,
```

covering PR #45's fixed chart, PR #51's run core, PR #49's height core, and PR #19's H renewal counter, prove one of:

1. an explicit ordinary root remains in the changing domain forever;
2. a shared completion-height, prime-renewal, or ranking theorem forces every ordinary root to exit.

The theorem must retain the actual most-significant quotient and exact physical replay.

**Use.** Prevents four teams from separately rediscovering the same ordinary-section obstruction under different coordinates.

---

## `ACL-N086` — Full-denominator compiler convergence

**Statement.** Assemble and audit the current finite-cycle compiler stack:

```text
critical mechanical or fixed-weight SLP
 -> quotient-Hensel digit at every prime power
 -> normalized centered half-join / block carry decoder
 -> commutator and sparse-resultant elimination of fixed subfamilies
 -> lossless cross-prime compatibility
 -> full exponential-circuit equality
 -> physical replay.
```

Prove one of:

1. one closed circuit satisfies the complete denominator and gives a positive cycle;
2. a named finite grammar is exhaustively excluded;
3. a structural theorem closes an entire compiler class without reducing to the original divisibility equation.

Proper-factor cancellation, a near-integer quotient, or an unreplayed carry cycle does not count.
