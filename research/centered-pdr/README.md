# Centered forced-tail modular/PDR program

**Agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Branch:** `agent/gpt56-pdr-01/40-centered-forced-tail-pdr`  
**Frozen centered source:** PR #16 at `87478352e65c7b816dfc8b3b30894b71fb50f662`  
**Status:** exact native packet; theorem-level claims `PROPOSED` pending independent review; no counterexample claimed

## Purpose

This packet continues the centered ordinary-section work after the independent reconstruction in draft review PR #37. It compiles eventual-zero nearest-integer blocks into an exact integer transition system and asks a deliberately proof-carrying question:

> Can a modular/PDR certificate distinguish one finite ordinary integer from the many compatible `2`-adic completion points?

The first answer is negative but exact. At every fixed dyadic precision, the greatest modular safety kernel is the full binary de Bruijn graph of itinerary cylinders. Its cycles are periodic `2`-adic ghosts, not positive ordinary witnesses. A successful next abstraction must retain the moving top boundary or an equivalent height/carry obligation.

## Frozen centered equations

Once appended blocks are zero, nearest integers satisfy

```text
64 B' = 81 B + e - e'.
```

The partial transition table is

```text
(B mod 64,e)=(0,0)  -> e'=0
(B mod 64,e)=(49,0) -> e'=1
(B mod 64,e)=(0,1)  -> e'=1
(B mod 64,e)=(15,1) -> e'=0.
```

The multiplier `81=64+17` yields a base-64 sequential transducer with post-initial carry in `{0,...,17}`.

## Main result

For precision `64^d`, define an existential edge by choosing one additional base-64 block before taking the exact transition. `T-8701` proves that the greatest infinite-path kernel is

```text
binary words e_0...e_d
  <-> unique d-step cylinder residue R_d(e_0...e_d),
```

with edges given by shift-and-append. Hence the kernel has `2^(d+1)` states and is exactly a de Bruijn graph.

`R-8701` proves that its periodic lassos are nonordinary except for the two trivial constant controls, both of which select nearest integer zero.

## Exact height renewal

`L-8702` adds the missing first top-boundary coordinate without claiming
all-time closure. For a positive legal path beginning in

```text
H/64 <= B_0 < H,
```

either a forbidden low residue terminates the path or its first crossing
`H <= B_t < 64H` occurs by `t<=18`. For each binary itinerary, the initial
integer is written exactly as `B_0=r+64^t Q`; all first-crossing conditions
reduce to one half-open rational interval for the integer `Q`.

`X-8703` streams all `1,048,572` words through depth 18 at `H=64^18`,
stores aggregate digests and selected boundary certificates, and is
independently reconstructed by a verifier that imports no builder code.
These canonical counts are finite computation. The iterated affine identity,
interval formula, deterministic partition of crossing survivors, and
18-step bound have a separate elementary proof in `L-8702`, whose status
remains `PROPOSED` pending review.

## Positive construction boundary

Any positive infinite path is strictly increasing and therefore divergent. A genuine constructive certificate must nevertheless supply:

1. one explicit finite `B_0>0`;
2. an all-time legality proof for the exact integer transition;
3. canonical top-boundary closure, not an infinite `2`-adic word;
4. the independently replayed issue-#4 chart translation.

No such seed was found or claimed in this session.

## Files

1. `claims/D-8701-centered-forced-tail-system.md`
2. `claims/L-8701-monotonicity-invariant-carry.md`
3. `claims/T-8701-fixed-precision-pdr-kernel.md`
4. `claims/R-8701-fixed-modulus-pdr-ghosts.md`
5. `claims/Q-8701-height-augmented-pdr.md`
6. `claims/L-8702-centered-height-renewal.md`
7. `CLAIM_INVENTORY.md`
8. `../../experiments/X-8701-centered-pdr/`
9. `../../experiments/X-8703-centered-height-renewal/`

## Cross-program boundary

- PR #37 independently verifies the centered recurrence and repairs the false unrestricted complexity screen.
- PR #33 closes a different frozen corrected-stage architecture at proposed-proof level; its independent audit is recorded separately under `reports/gpt56-pdr-01/` and `X-8702`.
- Issue #39 owns the first cross-cycle constructive handoff and is not duplicated here.
- No root ledger is edited by this packet.
