# Atomic counterexample problems — reviewed pass 3

These are the canonical pass-3 handoffs after quality review. They are open formulations unless explicitly marked `RESOLVED`.

## Identifier reconciliation

A pre-pass repository comment reserved:

```text
ACL-P036 = linear-height quotient-refund invariant.
```

The first pass-3 publication mistakenly duplicated that target as `ACL-P038`. The canonical ID is `ACL-P036`. `ACL-P038` is retired and must not be cited as a distinct problem.

## ACL-P036 — Linear-height quotient-refund invariant

**Statement.** In the issue-#43 linear schedule, construct exact sets `K_B` and a causal rule satisfying

```text
(B,Y) in K_B
 -> choose one physically overlapping stage word and exact lift k
 -> (B+4096,Y_next) in K_(B+4096),
Y_next>Y>0.
```

The rule may use finite control and one unbounded quotient/carry. It may not inspect future cylinder digits.

The proof must certify the next canonical most-significant boundary from only the current state, quotient/carry, and chosen word.

Give one explicit ordinary initialization and prove every local shortcut-Collatz transition, positivity, and unboundedness.

**Full-conjecture implication.** The physical stage replay gives an explicit divergent positive Collatz orbit.

---

## ACL-P037 — Critical-scale distributed-pulse cycle certificate

**Statement.** Let `u` be the exact accelerated valuation word of a known negative cycle, repeat it in a compressed representation, and insert pulse increments at finitely or compactly described positions.

For the resulting length `N`, prefix exponents `A_j`, and pulse sums

```text
Delta_j=sum_(i<j)delta_i,
Delta=sum_i delta_i,
```

prove the complete equality

```text
sum_(j=0)^(N-1)3^(N-1-j)2^(A_j+Delta_j)
 = n(2^(A_N+Delta)-3^N)
```

for one positive odd integer `n`, then replay every exact valuation and the return.

**Critical-scale requirement.** The pair `(N,A_N+Delta)` must satisfy the current published/computational cycle bounds and critical continued-fraction gate. Low repetition counts are controls, not frontier candidates.

**Required proof object.** Pulse grammar, compressed affine summaries, factorization or full-denominator circuit, exact equality, reconstructed seed, and independent replay.

**Full-conjecture implication.** A nontrivial positive cycle disproves Collatz.

---

## ACL-N074 — `(8,13)` prime-233 packet

**Status:** `RESOLVED NEGATIVELY`.

The 792 positive compositions of 13 into eight parts have no cycle numerator divisible by

```text
233 | 2^13-3^8.
```

This remains verifier infrastructure, not an open frontier atom.

---

## ACL-N075 — Pulse-circuit essential-rank and cross-prime decision

**Statement.** For a frozen negative primitive cycle and specified pulse grammar, prove one of:

1. the full-denominator condition reduces to bounded essential rank and admits a complete modular exclusion;
2. the essential rank grows, and an exact factorwise state couples the prefix-discrepancy walk to every prime-power order of `2^A-3^N`;
3. a critical-scale pulse circuit satisfies the full equality and yields `ACL-P037`.

A one-prime, proper-factor, or global-order reduction is insufficient.

---

## ACL-N076 — Quotient-refund causal top-boundary decision

**Statement.** Freeze a finite stage-word subalphabet in the linear-height refund architecture. Prove that every compatible infinite quotient selection either:

1. needs future information not computable from current finite control plus quotient;
2. selects a nonordinary rational-base completion;
3. decomposes into bounded excluded leaves;
4. or admits the causal top-boundary invariant of `ACL-P036`.

Case 4 must be published as the positive atom rather than described as a negative classification.

---

## ACL-N077 — Height-augmented centered forced-tail decision

**Statement.** For

```text
64B'=81B+e-e',
```

construct a sound one-counter abstraction retaining:

```text
finite control,
previous digit/sign,
carry in {0,...,17},
canonical most-significant boundary,
finite-support or carry-flush closure.
```

Prove one of:

1. an explicit positive `B_0` is legal forever;
2. every canonical finite word reaches a finite trap or violates top-boundary closure.

**Boundary.** Fixed-modulus lassos are excluded by PR #44 and do not count.

---

## ACL-N078 — Frozen corrected-stage review integration

**Statement.** Integrate PR #44's successful frozen-source review into the PR #33 claim ledger without extending its scope. Record exact source commits and distinguish:

- frozen corrected doubling-scale class;
- linear-height quotient refund;
- cross-cycle handoffs;
- adaptive or growing-rank systems.

**Use.** Prevents continued counterexample search inside an independently excluded class while preserving legitimate escape architectures.

---

## ACL-P039 — Full-denominator critical mechanical cycle circuit

**Statement.** Starting from a compressed critical-scale mechanical valuation word and finite block-replacement circuit, solve

```text
C(w)=n(2^A-3^k)
```

for one positive odd integer `n`, not only modulo selected factors.

Prove primitive-necklace normalization, exact valuation admissibility, positivity, and return.

**Required innovation.** Full-denominator lifting, common-content identity, or quotient-guided replacement. A near-integer interval or large proper divisor is insufficient.

**Full-conjecture implication.** The finite certificate is a nontrivial positive cycle.

---

## ACL-N079 — Cross-cycle phase-1 secret-reduction decision

**Statement.** Starting from issue #39's exact handoff, prove one of:

1. infinitely many physically exact returns from phase 1 to a nontrivial negative-cycle phase with a net-positive resource potential;
2. a finite positive nontrivial return before permanent phase 1;
3. every possible continuation is eventually permanent phase 1 or otherwise reduces to the original Collatz problem without new structure.

A permanent phase-1 tail is not a construction result because it is conjugate to

```text
q -> T(q-1)+1.
```

---

## ACL-N080 — H delayed-novelty versus reset-renewal decision

**Statement.** Combine PR #19 iteration-8 entropy and prefix-return barriers with the iteration-7 prime firewall and endpoint-product equations. Prove one of:

1. every finite-alphabet ordinary H survivor violates the required entropy/capital/return inequalities;
2. every unbounded-letter reset-renewal ray enters a subcritical endpoint-product trap;
3. one explicit positive seed supplies delayed novelty, fresh primes, eventual carry stabilization, and all-time positivity.

**Implication.** Cases 1–2 close H; case 3 gives a Collatz counterexample through the H embedding.
