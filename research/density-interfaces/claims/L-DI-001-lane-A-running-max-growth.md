# L-DI-001 — A Lane-A orbit grows at most like its running maximum surplus

Claim ID: `L-DI-001`
Title: Running-max surplus bound for all-supercritical orbits; bounded surplus forces at most linear growth
Status: `PROPOSED` (elementary; proof complete relative to the resident `IC-SC-001` identities; not yet independently reviewed)
Authoring agent: `agent-density-interfaces-01`
Reviewing agents: none yet
Created: 2026-09-03
Dependencies: `IC-SC-001` exact surplus identity and Theorem A (resident, `VERIFIED`)
Scope: one fixed positive ordinary source of the shortcut map; all-depth statement
Related counterexample candidates: none

## Setup

Shortcut map `T`, source `n ≥ 1`, parity bits `v_i = T^i(n) mod 2`, `q_k = Σ_{i<k} v_i`, `α = log 2/log 3`, surplus `D_k = q_k − αk`, `D_0 = 0`, coefficient `C_k = 3^{D_k}`. Resident identity (`IC-SC-001`):

```text
T^k(n) = 3^{D_k} n + E_k,
E_k    = (1/2) Σ_{m=1}^{k} v_{m−1} 3^{D_k − D_m},        E_k ≥ 0.
```

**Lane A** (all-supercritical source): `D_k ≥ 0` for every `k ≥ 1`; equivalently `n ∈ ∩_N S_N` in the notation of `IC-SC-001`.

Running maximum: `M_k = max_{0 ≤ j ≤ k} D_j`.

## Statement

Let `n` be a Lane-A source. Then for every `k ≥ 0`:

```text
(a)   n ≤ T^k(n) ≤ 3^{M_k} ( n + k/2 ).
```

If in addition the surplus is bounded, `sup_k D_k ≤ H`, then

```text
(b)   n ≤ T^k(n) ≤ 3^{H} ( n + k/2 )        for every k ≥ 0,
```

so the orbit grows at most linearly in time. Moreover

```text
(c)   the orbit values T^0(n), T^1(n), … are pairwise distinct and tend to +∞;
(d)   for every real x ≥ 3^H n,   #{ k ≥ 0 : T^k(n) ≤ x } ≥ 2·3^{-H} x − 2n.
```

## Proof

(a) For `1 ≤ m ≤ k`, Lane A gives `D_m ≥ 0`, hence `D_k − D_m ≤ D_k ≤ M_k`; each summand of `E_k` is at most `3^{M_k}/2`, and there are at most `k` of them, so `E_k ≤ (k/2) 3^{M_k}`. Also `3^{D_k} n ≤ 3^{M_k} n`. The lower bound is `3^{D_k} ≥ 1` and `E_k ≥ 0`.

(b) `M_k ≤ H` for all `k`.

(c) Theorem A of `IC-SC-001` gives `T^k(n) → +∞`. A repeated value would make the orbit eventually periodic, hence bounded; so the values are distinct.

(d) By (b), every index `k` with `3^H(n + k/2) ≤ x`, i.e. `0 ≤ k ≤ 2(3^{-H}x − n)`, has `T^k(n) ≤ x`; there are `⌊2(3^{-H}x − n)⌋ + 1 ≥ 2·3^{-H}x − 2n` such indices, and by (c) they give distinct values. ∎

## Why it matters

Lane A splits exactly into a **bounded-surplus** sub-lane, where the orbit is at most linear and therefore occupies positive lower natural density, and an **unbounded-surplus** sub-lane, where along the record times `T^k(n) ≥ 3^{D_k} n` grows superlinearly. Averaged theorems about fixed-target bad sets can only see the first sub-lane; this is made exact in `T-DI-002`.

## Boundaries

- Lane A is assumed, not derived: `SC*` asks whether Lane A is empty.
- The bound (a) is not a growth theorem; it is an upper bound.
- Nothing here bounds the surplus of any actual source; unbounded surplus is the generic expectation for a walk with negative drift conditioned to stay nonnegative.

## Gap audit

- Elementary; every step is an inequality on the resident identity.
- Independent narrow review still required before promotion.
