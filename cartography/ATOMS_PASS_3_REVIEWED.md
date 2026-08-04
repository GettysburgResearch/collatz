# Atomic counterexample problems — reviewed pass 3

These are the canonical pass-3 handoffs after final live refresh. They are open formulations unless explicitly marked `RESOLVED`.

## Identifier reconciliation

The canonical linear-height refund atom is `ACL-P036`. The earlier duplicate `ACL-P038` is retired.

## ACL-P036 — Forever-defined width-one refund decoder

**Statement.** Use PR #49's exact width-one connector state

```text
(t,i,j,z),
t>=3744,
z>=1,
```

and its deterministic decoder. Exhibit one explicit finite tuple and an inductive ordinary invariant proving that the decoder is defined at every future connector.

The proof must verify:

1. the exact divisibility and four-cell membership test at every step;
2. canonical most-significant/top-boundary closure without future cylinder data;
3. the explicit physical initialization from PR #49;
4. every shortcut-Collatz connector replay.

PR #49 then supplies unique next type, positivity, and `z'>=2z` automatically.

**Full-conjecture implication.** The explicit physical orbit is positive and unbounded, so Collatz is false.

---

## ACL-P037 — Critical-scale distributed-pulse cycle certificate

**Statement.** Start with a known negative cycle, states `z_i`, prefix exponents `A_i`, and a compressed pulse grammar `delta_i>=0`. Put

```text
Delta_i=sum_(t<i)delta_t,
D_delta=2^(B+Delta)-3^N,
b_i=-(3z_i+1)>0,
R_delta=sum_i b_i(2^delta_i-1)2^(A_i+Delta_i)3^(N-i-1).
```

Prove

```text
D_delta | R_delta,
n=z_0+R_delta/D_delta>0,
```

then replay every exact valuation and the return.

For two pulses of fixed total `T`, use the exact one-variable form

```text
R=U_j2^T+(U_i-U_j)2^delta-U_i.
```

**Critical-scale requirement.** The total shape must satisfy current cycle height/continued-fraction constraints. Low repetition ranges are controls.

**Full-conjecture implication.** The finite certificate is a nontrivial positive cycle.

---

## ACL-N074 — `(8,13)` prime-233 packet

**Status:** `RESOLVED NEGATIVELY`.

The 792 positive compositions fail the necessary divisor `233 | 2^13-3^8` test.

---

## ACL-N075 — Cross-prime pulse compatibility decision

**Statement.** Combine PR #34's lossless prime-power excess-path compiler with the distributed-pulse remainder. Prove one of:

1. no compatible full-factor pulse path exists for the frozen grammar;
2. one compatible path reconstructs a unique critical-scale word and yields `ACL-P037`;
3. the grammar needs a strictly richer unbounded cross-prime state, explicitly identified.

One-prime, proper-factor, or global-order aliasing is insufficient.

---

## ACL-N076 — Refund decoder infinite-definedness dichotomy

**Statement.** For PR #49's deterministic map, prove one of:

1. one explicit finite residual remains in the decoder domain forever, yielding `ACL-P036`;
2. every ordinary residual eventually fails the divisibility or four-cell test;
3. every infinite completion is nonordinary by a quantified top-boundary/stabilization theorem.

Incorporate PR #48's cylinder sparsity and PR #34 `L-9915`: finite control plus one zero-tested additive counter is not enough. A positive invariant may use the exact nonlinear inverse-carry recurrence, changing modulus, stack, or richer unbounded state.

---

## ACL-N077 — Height-augmented centered forced-tail decision

**Statement.** For

```text
64B'=81B+e-e',
```

construct a sound ordinary machine retaining bounded carry and canonical top closure. It must lie outside PR #34 `L-9915`'s additive one-counter class.

Prove either:

1. one explicit positive `B_0` is legal forever;
2. every canonical finite word reaches a finite trap or violates top-boundary closure.

Fixed-modulus lassos do not count.

---

## ACL-N078 — Frozen corrected-stage review integration

Integrate PR #44's successful review into PR #33 without extending scope. Preserve the distinction among the frozen doubling class, width-one linear refund, cross-cycle handoffs, and adaptive/growing-rank systems.

---

## ACL-P039 — Full-denominator critical mechanical cycle circuit

Starting from PR #45's independently reviewed compiler, solve

```text
C(w)=n(2^A-3^k)
```

for the entire denominator and one positive odd `n`. Use PR #34's seven-non-`2` support floor and lossless cross-prime compiler. Prove primitive normalization, exact valuations, positivity, and return.

---

## ACL-N079 — Cross-cycle phase-1 secret-reduction decision

Starting from issue #39, prove repeated physically exact returns from phase 1 to nontrivial phases with net-positive resource, or a finite positive return before permanent phase 1, or a theorem that every continuation reduces to shifted ordinary Collatz.

---

## ACL-N080 — H delayed-novelty versus reset-renewal decision

Combine PR #19 iteration-8 entropy/return barriers with the prime firewall and endpoint-product equations. Prove finite-alphabet extinction, reset-renewal extinction, or one explicit positive H survivor with delayed novelty, fresh primes, and ordinary stabilization.
