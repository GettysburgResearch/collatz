# Session report — independent supercritical audit and strengthening

Agent: `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
Issue: `#75`  
Branch: `agent/gpt56-positive-review-01/75-verify-supercritical`  
Base: `agent/gpt56-positive-01/75-positive-coefficient-gate`  
Date: 2026-07-29

## Starting hypothesis

The source claim `T-6708` was produced by a lower-reasoning model and required a clean independent reconstruction. The review was instructed not to rely on the authoring model's confidence and to continue only after checking the exact recurrence, exponent algebra, quantifiers, case split, and tail consequences.

## Approaches attempted

1. Re-derived the shortcut recurrence from one step.
2. Proved the finite affine formula by induction rather than accepting the source normalization.
3. Recomputed the logarithmic-surplus identity term by term.
4. Audited both cases in `T-6708` and the shifted-tail corollary.
5. Tried to refute the theorem with long safe parity excursions of the form `1^r0^s`.
6. Distinguished depthwise minimizing words from one nested infinite path.
7. Investigated the source's admitted gap between an unbounded subsequence and full divergence.
8. Proved a low-band renewal lemma that closes that gap.

## Verification result

### `T-6708`

**Verdict: PASSED.**

The exact formula is

```text
T^k(n)
 = (3^q_k / 2^k) n
 + sum_(m=1)^k v_(m-1) 3^(q_k-q_m) / 2^(k-m+1).
```

With

```text
alpha = log(2)/log(3),
D_k = q_k-alpha*k,
```

this gives

```text
E_k = (1/2) sum_(m=1)^k v_(m-1) 3^(D_k-D_m).
```

If `D_k` is unbounded, the multiplicative term gives an unbounded subsequence. If `0<=D_k<=B`, every odd contribution is at least `1/(2*3^B)` and `q_k>=alpha*k`, so the whole orbit tends to infinity at least linearly. No gap was found.

The source's formal tail corollary is also correct. One wording phrase is ambiguous: what is proved is that every starting time of a bounded infinite orbit admits at least one later subcritical block, not necessarily infinitely many subcritical lengths from each fixed start.

## New result

### `T-6709` — all-time supercriticality forces full divergence

The original proof established only unboundedness when `D_k` itself is unbounded. The new theorem proves

```text
3^q_k / 2^k >= 1 for every k
    ->
T^k(n) -> +infinity.
```

The key low-band lemma is:

```text
if D_k < H infinitely often,
then odd endpoints with D_m < H+(1-alpha)
occur infinitely often.
```

Otherwise, after the last such endpoint, any later visit below `H` would have to be followed eventually by an odd step while still below `H`, creating another forbidden low endpoint; an infinite run of evens would instead force `D` negative.

At a later time with `D_k<H`, every prior low-band odd endpoint contributes at least

```text
1 / (2*3^(H+1-alpha))
```

to the exact affine remainder. Repeated low returns therefore raise the low values without bound. If low returns stop, the multiplicative term stays above `3^H n`. Splitting on these alternatives for every target height proves full divergence.

## Candidate counterexamples

None.

## Failed or nondecisive approaches

- Finite words `1^r0^s` can finish at modest values after very high excursions. They do not refute `T-6709`, because choosing a new minimizing word at every depth is not one nested infinite path. Along one fixed path, repeated returns accumulate low-band odd contributions.
- The new theorem classifies the dynamics of an ordinary all-time-supercritical path but does not exclude its ordinary realization.
- No uniform divergence rate follows from the proof; low-band renewals can be sparse.

## Potential errors and review targets

1. Check the indexing in the exact affine sum independently.
2. Check that the first future odd step after a low visit ends below `H+1-alpha`.
3. Check the quantifier order: fix the target `M`, then choose `H`, then choose the eventual time `K`.
4. Keep divergence of an assumed ordinary realization distinct from proof that such a realization exists.
5. Do not promote `T-6709` without another independent review.

## Files changed

- `research/positive-coefficient-gate/reviews/T-6708-independent-review.md`
- `research/positive-coefficient-gate/T-6709-supercritical-implies-divergence.md`
- this report

## Claims affected

- independent verdict `PASSED` for source claim `T-6708`;
- new proposed strengthening `T-6709`;
- no source status changed automatically.

## Recommended next actions

1. Independently review `T-6709`.
2. Replace strategic references to an “unbounded” `tau=infinity` branch with the stronger “divergent to +infinity” description once reviewed.
3. Attack ordinary realization directly through constrained residue-cylinder least roots.
4. Keep the delayed-crossing Farey lane separate; `T-6709` does not improve the finite crossing denominator by itself.

## Organizational improvement idea

Independent reviews should freeze the exact source blob and use a separate branch, as done here. A later stronger theorem should receive a new claim ID rather than silently rewriting the statement that was reviewed.
