# Atomic counterexample problems — pass 3

These are new standalone handoffs from the third cartography pass. They are open formulations, not proved claims.

## ACL-P037 — Distributed-pulse negative-cycle certificate

**Statement.** Let `u` be an exact accelerated valuation word of a known negative Collatz cycle, repeat it `r` times, and choose finitely many pulse increments `delta_i>=1` at specified valuation positions. With `N`, `A_j`, `Delta_j`, and `Delta` as in `CARTOGRAPHY_PASS_3.md`, prove

```text
C_delta = n(2^(A*r+Delta)-3^N)
```

for one positive odd integer `n`, then replay every exact valuation and the return.

**Implication.** The resulting finite certificate is a nontrivial positive Collatz cycle.

**Required proof object.** Pulse list, compressed affine summaries, exact full-denominator equality, reconstructed seed, and independent physical replay.

**Boundary.** Divisibility by a proper factor, a near-integer quotient, or a single-pulse hit is insufficient.

---

## ACL-N075 — Distributed-pulse bounded-rank reduction

**Statement.** For a frozen negative primitive cycle and a specified pulse grammar, prove either:

1. every pulse circuit compresses to bounded essential rank and admits a complete modular exclusion; or
2. the essential pulse rank grows, and provide the exact meet-in-the-middle state needed to search it without expanding the repeated word.

**Use.** Prevents brute-force scans over pulse locations that secretly repeat the one-pulse obstruction.

---

## ACL-P038 — Linear-height quotient-refund invariant

**Statement.** In the issue-#43 linear schedule, construct sets `K_B` and a causal finite rule satisfying

```text
(B,Y) in K_B
 -> choose a physically overlapping stage word and exact lift k
 -> (B+4096,Y_next) in K_(B+4096),
Y_next>Y>0.
```

The rule may use finite control and one unbounded quotient/carry but may not inspect future cylinder digits.

Give one explicit ordinary initialization and prove every local Collatz transition, positivity, and unboundedness.

**Implication.** Supplies an explicit divergent positive Collatz orbit.

---

## ACL-N076 — Quotient-refund causality obstruction

**Statement.** Freeze a finite stage-word subalphabet in the linear-height refund architecture. Prove that every infinite compatible quotient selection either:

1. requires unbounded future information not computable from current finite control plus quotient;
2. collapses to a nonordinary rational-base completion; or
3. admits a causal top-boundary invariant.

In case 3, output the invariant as `ACL-P038` rather than treating this as a negative result.

---

## ACL-N077 — Height-augmented centered forced-tail decision

**Statement.** For the exact partial map

```text
64B'=81B+e-e',
```

construct a sound one-counter abstraction retaining finite control, carry in `{0,...,17}`, a canonical most-significant boundary, and finite-support closure. Prove one of:

1. an explicit positive seed is legal forever; or
2. every canonical finite word reaches a finite trap or violates top-boundary closure.

**Boundary.** Fixed-modulus lassos are excluded by PR #44 and do not count.

---

## ACL-N078 — Frozen corrected-stage integration

**Statement.** Reconcile PR #44's independent `PASSED` review with the native PR #33 ledger, including exact source commits, theorem status, and the distinction between:

- the frozen corrected 256-transition architecture;
- linear-height refund schedules;
- cross-cycle handoffs;
- adaptive/growing-rank constructions.

**Implication.** Prevents further counterexample searches inside a class already independently excluded while preserving every legitimate escape lane.

---

## ACL-P039 — Full-denominator mechanical cycle circuit

**Statement.** Starting from a compressed critical-scale mechanical valuation word and a finite block-replacement circuit, solve the complete equality

```text
C(w)=n(2^A-3^k)
```

for one positive odd integer `n`, not merely modulo selected factors. Prove exact valuation admissibility and return.

**Implication.** Gives a finite nontrivial positive cycle certificate.

**Required innovation.** A full-denominator lifting method, common-content identity, or exact quotient-guided replacement rule; partial modular joins alone are insufficient.
