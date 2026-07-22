# Integer-first counterexample offense

**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Draft PR:** #47

## Acceptance standard

A positive result must provide one ordinary positive integer and prove, with exact standard-map replay, either:

1. a nontrivial positive cycle; or
2. an infinite orbit that never reaches `1`.

The following are not candidates:

- a long finite prefix;
- a compatible inverse limit in `Z_2`;
- a real shadow;
- approximate divisibility;
- a modular lasso without an ordinary top boundary;
- a control-map orbit without an exact `3x+1` embedding.

## 1. Negative-cycle perturbation program

### Single pulse — `L-9601`, `X-9601`

Repeating a rotated negative cycle and increasing one valuation reduces to

\[
2^{Ar+\delta}-3^{kr}
\mid
(2^\delta-1)(3z+1).
\]

The exact scan checks `720,000` reduced cases through `20,000` repetitions and finds only the trivial `n=1` cycle.

### Distributed pulses — `L-9602`, `X-9602`

Arbitrary extra valuations produce an exact weighted subset sum. Distinct unit pulses satisfy

\[
H(P)=\sum_t2^{t-1}W_{p_t}.
\]

A cyclic half-balance theorem gives a complete meet-in-the-middle cover. The frozen range represents `508,127,577,642` raw labeled pulse words and contains no nontrivial hit.

### Two supports — `L-9603`, `X-9603`

Two pulse supports reduce to a bounded discrete logarithm after an exact gcd sieve. The frozen packet checks `59,385,744` pulse splits and finds no nontrivial hit.

### Two macro-blocks — `L-9604`, `X-9604`

For two compressed affine blocks, the commutator

\[
\Omega(u,v)
=(q_u-p_u)C_v-(q_v-p_v)C_u
\]

controls every `u^m v^n` candidate. Once the cycle denominator exceeds `G_m|\Omega|`, all later `n` are eliminated. The frozen packet contains zero cycle hits.

## 2. Centered non-neutral support program

For every accelerated word,

\[
E_w=C_w-(2^A-3^k)
=
\sum_j3^{k-1-j}2^{A_j}(4-2^{a_j}).
\]

Valuation `2` is exactly neutral. A nontrivial positive cycle must satisfy

\[
D_w\mid E_w,
\qquad
E_w\ge2D_w>0.
\]

PR #34 independently developed the first centered support layers. This branch reconstructs the interface and adds:

| claim | excluded support | exact finite packet |
|:---|:---|:---|
| `T-9601` / `X-9605` | exactly 7 non-`2` valuations | 49,471 normalized candidates |
| `T-9602` / `X-9606` | exactly 8 | 3,880,002 candidates |
| `T-9603` / `X-9607` | exactly 9 | 98,203,183 candidates |
| `T-9604` / `X-9608` | exactly 10 | 1,623,353,430 candidates represented by MITM |

Every packet has zero formal divisor hits.

`L-9605` supplies the scalable exact join. For a split `w=uv`,

\[
D_w\mid E_w
\iff
E_u2^{-A_u}+E_v3^{-k_v}\equiv0\pmod{D_w}.
\]

`X-9608` is independently checked with `5+5` and `4+6` splits.

Subject to independent reconstruction of all proposed centered layers, every nontrivial positive cycle would require at least **eleven** valuations different from `2`.

## 3. Constructive pivot: quotient refund

The cycle exclusions are useful, but the branch’s positive target remains an unconditional ordinary witness.

Issue #43 / PR #48 proves a sharp conditional fact for the linear-height phase-34 architecture: once one coherent ordinary path has a positive lift quotient beyond the exact threshold, that quotient at least doubles at every stage. Growth is therefore no longer the missing theorem.

The sole constructive wall is now:

```text
one explicit ordinary initialization
+ causal stage-word selection
+ exact local connector replay
+ canonical most-significant carry flush.
```

A successful invariant there immediately yields an unbounded physical induced orbit. Pairwise quotient lifts, compactness, or future-digit selection do not suffice.

## Collaborator handoffs

All exact cycle packets are posted to issue #9 and PR #34. The phase-1 boundary of issue #39 is recorded explicitly: a permanent phase-1 tail is the original shortcut Collatz map shifted by one, not an extra amplifier.

## Status

No unconditional Collatz counterexample has been found. No `K-####` identifier is assigned. Every finite negative packet and reusable exact reduction is shared rather than kept private.
