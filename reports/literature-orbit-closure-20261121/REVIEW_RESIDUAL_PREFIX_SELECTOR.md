# Independent source review: residual prefix and all-clock selector

**Review type:** mathematical and source-level review only. No compilation, finite search replay, or edits to the reviewed files were performed. This review does not replace the author's strict Lean build and axiom-audit receipts.

## Exact reviewed snapshot

Files are in `collatz_work/literature_rewriting/`.

| File | SHA-256 |
|---|---|
| `ResidualPrefixErasure.lean` | `b4d8ae889c458ee26c3ea8d3c362290c465a725f024d53e1f3978290c6661a9c` |
| `ResidualPhaseSelector.lean` | `f5849eb6bc7cb4935f2df66e734b08e4372b92093a7aa2480a3e8ed16078528c` |
| `RESIDUAL_PREFIX_ROUTE.md` | `62b3fd95fa11777422c739aa9f7ffcde0015e238868913971c448f455454c499` |

The imported eight-clock diamond and its eighth-source erasure theorem were also read in `collatz_work/literature_symbolic/LongDiamondErasure.lean`. The bounded phase classifier `residual_phase_analysis.py` was inspected as source, without execution.

## Findings

**No blocking mathematical or scope issue was found at this snapshot.**

1. **Physical normalization and clocks.** The prefix is the ordinary shortcut orbit
   `T^7(128z+27)=729z+161`, with six odd inputs. If `729z+162=2^k u`, the imported eighth-source diamond gives `8x+7=T^7n`, hence exactly `1024x=729n+29`. Its merger clocks compose to `T^(k+5)x=T^(k+15)n`. All paths use the repository's ordinary `step` and `orbit`; no multiplication in an unrestricted semigroup is substituted for an orbit identity.

2. **Generic source comparison.** The scale identity is `2^r(x+1)=3^p z+c+1`. The entire-progression conditions `3^p<=2^(h+r)` and `c+1<2^r(b+1)` imply the required strict comparison after multiplying `x+1<n+1` by `2^r`. The eventual version uses the integer slope gap of at least one and `z>=c+2`, yielding the stronger intermediate inequality `3^p z+c+1<2^(h+r)z`. The bridge lemmas explicitly retain `0<r<k`, `u>0`, the actual prefix endpoint, and the synchronous diamond as hypotheses. No universal diamond selector is hidden in the generic theorem.

3. **Exact CRT selector for every k.** The constants satisfy `6400=(1,0)` and `14337=(0,1)` modulo `(81,256)`, with product modulus 20736. The powers `2^(53k+1)` and `3^(63(k+1))` supply the needed inverses because `2^54=1 mod81` and `3^64=1 mod256`. Thus the selected `w` satisfies `2^k w=2 mod81` and `3^(k+1)w=147 mod256`. The first forces positivity; the second forces oddness. With `u=81w` and `z=9 floor(2^k w/81)`, the exact integer division gives `729z+162=2^ku`. These statements hold for all natural k; the physical residual-family conclusion explicitly restricts to k>=6.

4. **Residual cell and complete progressions.** Every selected `n=128z+27` is divisible by 9. The endpoint gives `729n=2^(k+7)u-1053`, so k>=6 yields `n=1819 mod8192`, hence `n=34587 mod73728`. Increasing t by one increases n by `M_k=9*2^(k+15)=73728*2^(k+2)`. The strict positive canonical-base bounds establish a complete positive residue progression, rather than a truncated progression with small omitted terms.

5. **No descent and all-k disjointness.** The seven displayed prefix states after time zero exceed the original source. The subsequent k odd steps increase from the prefix endpoint. Therefore `n<=T^i n` holds through i=k+7, and through i=13 when k>=6. Because u is odd, `v_2(T^7n+1)=k` exactly; different k therefore produce disjoint source progressions. The note correctly avoids upgrading this to no descent through an arbitrary binary-logarithmic horizon.

6. **Exact relative density 1/128.** The kth progression has relative density `2^(-(k+2))` inside the one ambient cell. Their disjoint finite sums tend to 1/128. The countable-union upper bound is justified: write an arbitrary member of that ambient cell as `n=34587+73728 ell`. Then `z=270+576 ell`, and

   `T^7 n+1=729z+162=64(3078+6561 ell)`.

   Since 6561 is odd, for K>=6 the condition `2^K | T^7n+1` has relative density exactly `2^(-(K-6))`. It contains every selected progression with k>=K and its density tends to zero. This establishes the claimed natural density without an unjustified countable-additivity step. The note correctly identifies the density argument as written mathematics, not a Lean density theorem.

7. **Finite endpoint catalogue and its limitation.** The phase classifier checks equality at the representative and equality of affine slopes, the two conditions needed for an entire binary cylinder. Its reported bounded classification is explicitly a Python result, while the useful r=3 diamond is imported from Lean. The all-even obstruction is valid for synchronous pure dyadic cylinder erasures: an endpoint `W=1 mod2^H` is all-even at the catalogued clocks; slope equality forces p=r, while the other endpoint is initially even, so its odd positions satisfy `i_j>=j`. Thus its carry is at least `2(3^r-2^r)>3^r-1` for r>=2, contradicting the required carry. The note limits this obstruction to that architecture and leaves unbounded endpoint clocks and other affine partner rules open.

8. **Induction scope.** `basin_by_smaller_induction` explicitly requires the basin statement for every smaller positive source. It transfers that statement through a proven common future. It does not require the partner to belong to the selected family, and it does not present the 1/128 partial coverage as convergence of the entire residual cell or of all positive integers.

## Minor wording precision

In the natural-density tail paragraph, replace **“for any K”** by **“for any K>=6”**. The displayed relative-density formula `2^(-(K-6))` is intended in that range. This is a wording qualification, not a gap in the limiting argument, which only uses arbitrarily large K.

No other correction is requested by this review.
