# Session report — intrinsic refund marker and prime turnover

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Branch:** `agent/gpt56-cylinder-01/43-linear-quotient-refund`  
**Date:** 2026-07-23

## Starting hypothesis

The deterministic complement-counter map of `T-8504` had already reduced a complete counterexample to one finite state whose next-scale divisibility remains defined forever. The next goal was to remove any remaining trusted metadata and identify an arithmetic invariant strong enough to constrain or generate the missing top boundary.

## Repository and collaborator inputs read

- independent issue-#43 packet PR #48: growth after coherence, cylinder firewall, and stage-word residue sparsity;
- PR #44: fixed-modulus PDR graphs are periodic `2`-adic ghosts unless a canonical top boundary is retained;
- PR #51 `O-8001`: exact negative-three-cycle and negative-eleven-cycle one-counter charts;
- issue #43 cartography update: canonical positive atom `ACL-P036` and negative atom `ACL-N076`;
- PR #34 `L-9915`: fixed-residue additive one-counter controllers are eventually periodic.

These inputs confirm that further low-residue or prefix search is not the right load-bearing step. The state must retain exact most-significant closure and genuinely unbounded arithmetic information.

## Approaches attempted

1. Re-expressed the complement quotient in terms of the two consecutive ordinary boundary words rather than the connector inverse variables.
2. Searched for a determinant or adjacent-word invariant that makes the top coordinate intrinsic.
3. Compared the resulting system with the two-branch negative-three-cycle chart.
4. Audited whether a finite prime library or fixed `S`-unit schema could support an infinite refunded path.
5. Built an independent exact checker for the new elementary identities.

## New mathematical results

### `L-8504` — unimodular physical marker

With

```text
d=M-r,
e=N-c,
```

the complement matrix is

```text
[[M,d],[N,e]] in SL_2(Z).
```

For one local state,

```text
(W,U)^T = [[M,d],[N,e]] (k,b_i)^T.
```

Hence

```text
k=eW-dU,
b_i=MU-NW.
```

The cone edges `N/M` and `e/d` are neighboring Farey fractions. The abstract counter is therefore an intrinsic lattice coordinate, not hidden connector metadata.

The physical boundary integer

```text
n=2^(11(t+1))*W/64-34
```

satisfies

```text
v_2(n+34)=11t+5+i.
```

Because `16|t`, the valuation modulo `176` recovers the type, then the full height, and the odd boundary word recovers `k`. A final verifier can begin with one written integer rather than a trusted marked tuple.

### `T-8505` — fresh-prime turnover

Every boundary word has residue `5,30,20,56 mod64`; none is `{2,3}`-smooth. Thus every boundary carries a prime at least five.

The local equation gives

```text
gcd(W_n,W_(n+1)) | b_(i_n),
```

so no prime at least five persists across adjacent boundaries.

If all late boundary words used one finite prime set, the local equations would give infinitely many distinct primitive nondegenerate three-term `S`-unit zero sums. Evertse 1984 Corollary 1 with `d=0` makes that impossible. Therefore every fixed finite prime set is escaped infinitely often, and infinitely many globally new odd primes divide the physical shifts `n_n+34`.

## Exact experiment

Added `X-8503-unimodular-physical-marker` with separately written derivation and checker.

Frozen derivation:

```text
unimodular rows:              4
exact connector cases:        192
intrinsic marker cases:       192
adjacent gcd cases:           192
projective valuation rows:    64
smooth residue obstructions:  4
semantic digest:
320b667d3c82007624e7bb3ccbb3738aa31503afea3718058f9e23613b7940df
```

Independent checker:

```text
exact connector cases:      32
intrinsic marker cases:     32
adjacent gcd cases:         32
smooth residue gates:       4
all independent checks passed
```

The experiment validates only the elementary gates. It does not prove the external Evertse theorem or construct an infinite path.

## Candidate counterexamples

None. No `K-85xx` identifier was created.

## Failed or closed approaches

- A fixed-modulus residue lasso remains a completion ghost by PR #44.
- A finite controller observing only fixed residues of an additive counter is closed by PR #34 `L-9915`.
- A fixed finite-prime multiplicative library is now closed by `T-8505`.
- The smaller PR #51 chart supplies no known top-boundary closure theorem transferable to the refund map.

## Exact remaining gap

Construct one finite ordinary physical integer whose intrinsic state under `L-8504` remains in the domain of `T-8504` forever. The invariant must:

1. preserve the moving next-scale divisibility;
2. carry canonical most-significant closure;
3. remain causal and finite at initialization;
4. generate the infinitely renewing odd-prime content forced by `T-8505`.

Growth, positivity, physical replay, type selection, and verification metadata are no longer separate gaps.

## Files changed

- `research/quotient-refund/claims/L-8504-unimodular-physical-marker.md`
- `research/quotient-refund/claims/T-8505-fresh-prime-turnover.md`
- `experiments/X-8503-unimodular-physical-marker/`
- updated packet README, inventory, interface map, gap audit, and `Q-8501`.

## Claims affected

- added `L-8504`, `T-8505`, `X-8503`;
- sharpened `Q-8501` to a single-physical-integer certificate and a fresh-prime-generating safety invariant.

## Recommended next actions

1. Express the next-scale top-boundary test in the intrinsic `SL_2(Z)` coordinates and seek a scale-renormalization law for the Farey-cone distance `k`.
2. Test whether PR #3's ordinary quadratic bulk can generate the exact moving top coordinate, not only low bits.
3. Use the negative-three-cycle chart as a minimal regression system for any proposed top-boundary PDR invariant.
4. Request independent reconstruction of `L-8504` and the Evertse specialization in `T-8505`.

## Organizational improvement

Counterexample certificates should distinguish:

```text
trusted metadata,
intrinsic physical markers,
abstract low residues,
canonical top-boundary state,
prime-renewal obligations.
```

A claim should state which of these are reconstructed from the written integer and which remain assumptions.
