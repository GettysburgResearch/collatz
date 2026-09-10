# Session report — supercritical branch

Agent: `gpt56-positive-01`  
Issue: `#75`  
Branch: `agent/gpt56-positive-01/75-positive-coefficient-gate`  
Date: 2026-07-29

## Starting hypothesis

The remaining `tau=infinity` branch might admit a direct contradiction from coefficient density, no descent, and ordinary extraction.

## Approaches attempted

1. Tested whether the all-prefix inequality `3^q_k >= 2^k` conflicts directly with the Angeltveit `485/306` ballot barrier. It does not: coefficient supercriticality is slightly stronger and is compatible at the word level.
2. Tested whether no descent supplies additional endpoint inequalities in this branch. It does not: `C_k >= 1` and positivity already imply `T^k(n) >= n`.
3. Searched current verification sources for an unconditional `2^75` floor. The current authoritative Barina project still records `2^71`; no certified `2^75` result was located.
4. Rewrote the exact affine remainder in terms of the logarithmic surplus `D_k=q_k-alpha k`.

## New result

### `T-6708` — all-time coefficient supercriticality forces unboundedness

For an ordinary positive orbit, if

```text
3^q_k / 2^k >= 1
```

for every prefix, then the orbit is unbounded.

The exact identity

```text
E_k = (1/2) sum_{m<=k} v_{m-1} 3^(D_k-D_m)
```

produces an exhaustive proof.

- If `D_k` is unbounded, the multiplicative term `3^D_k n` is unbounded.
- If `0 <= D_k <= B`, every odd contribution is at least `1/(2*3^B)`, while `q_k >= alpha k`, giving
  ```text
  T^k(n) >= alpha*k/(2*3^B) -> infinity.
  ```

Thus the opaque `tau=infinity` branch is necessarily an unbounded-orbit branch. It cannot contain a bounded nonperiodic orbit or a positive cycle.

## Candidate counterexamples

None.

## Failed approaches

- Density alone does not exclude an ordinary survivor.
- No descent is automatic while the coefficient is supercritical and contributes no further restriction.
- The next Farey candidate requires a verification floor near `2^75`; no current authoritative unconditional floor at that level was found.

## Potential errors

The theorem distinguishes unboundedness from convergence to infinity. When `D_k` is unbounded, only an unbounded subsequence is proved. When `D_k` is bounded, the entire orbit tends to infinity at least linearly.

## Files changed

- `research/positive-coefficient-gate/T-6708-supercritical-implies-unbounded.md`
- this report

## Claims affected

- added `T-6708` as `PROPOSED`;
- no prior claim status changed.

## Recommended next actions

1. Independently reconstruct the surplus identity and the bounded/unbounded split.
2. Import every sound exclusion of unbounded ordinary paths into the supercritical cylinder tree.
3. Prove divergence of the least ordinary roots in the survivor unions; do not replace ordinary extraction with symbolic density.
4. In parallel, pursue a certified `2^75` computation or sharpen the next mechanical remainder bound enough to use the current floor.

## Organizational improvement ideas

The positive program should maintain two separate ledgers:

```text
U-lane: all-time supercritical ordinary paths (now necessarily unbounded)
F-lane: finite first coefficient crossing candidates
```

This prevents bounded-cycle arguments from being mixed with the genuinely unbounded `tau=infinity` branch.
