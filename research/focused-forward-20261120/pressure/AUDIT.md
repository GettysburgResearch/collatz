# Independent pressure-packet reconstruction

This is a content-level audit during preparation of the additive packet.
The exact reviewed bytes are pinned by the SHA-256 and Git blob digests in
[audit-snapshot.json](audit-snapshot.json); the parent publication report
must supply the full new commit SHA. The prior repository head was
`6ff18e4f63be8f3bece76215fcfe44d83b001d7f`.

The definition and closure distinction imported from PR149 were checked at
the full head `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`, specifically
`research/forward-inverse-defect/PROOF.md` (all-action potential) and
`research/forward-inverse-defect/CLOSURE_BOUNDARY.md` (basin restriction and
the additional root condition). This audit does not promote neighboring
claims at that head.

## Mathematical reconstruction

| Claim in `PROOF.md` | Narrow verdict | Reconstruction |
|---|---|---|
| H1 | VERIFIED at the pinned text | Positive score gives `5A<=8k-1`. Positivity of the affine correction gives `3^k m<2^A`, hence `2*243^N*m^5<256^N` for every `k<=N`. The integer strict cutoff is correct. Reversing a legal word gives the unique actual forward path; visits after the first hit of `1` are exponent-two root loops of score `-2`. The maximum therefore reduces exactly to first-hit paths in the stated finite interval. |
| H2 | VERIFIED at the pinned text | Concatenate the reversed first-hit path to any inverse word from the source. Both score and horizon add. The surviving horizon is exactly `L-h`, not `L`. |
| H3 | VERIFIED at the pinned text | Before the first hit of `1`, odd unit states are distinct. Their increasing rearrangement has `j`th member at least `3j+1`. This bounds the logarithm of the exact product correction by `(1+ln h)/9`; substitution and one bootstrap of `log h` give the stated coefficients. The statement concerns the terminating basin only. |
| O1 | VERIFIED at the pinned text | The even-`k` inverse-one word has legal unit endpoints; parity of `k` is essential. The two ordering comparisons, geometric sum of decreasing even parameters, and least permitted one-step upper ancestor yield exactly `d>=8/log_2(3)-5`. No conclusion assumes typical ternary points represent a fixed ordinary integer. |
| O1-local | VERIFIED at the pinned text | The lower comparison has ratio below `10` once the reduced even parameter is at least `2`. The permitted predecessor exponent has gap `2` or `4`; odd integer slack gives `u_(a')<=n_k-2`, hence `u_a<16n_k`. Thus the same proof uses only local height ratios at most `16`. |
| O2 | VERIFIED at the pinned text | Iterating exactly `12` times uses one common `D_16(X)`, with a bounded parameter-rounding error. A largest even `k` satisfying `32*3^k<=X` ensures all comparison points lie below `X` and `k log_2(3)=log_2 X+O(1)`. The coefficient is positive by the stated exact rational bound. The claim is a liminf lower bound, distinct from O1-local's larger limsup coefficient. |
| `W(1)<infinity` or Collatz | OPEN | Finite maxima and necessary oscillations do not give a uniform bound as the candidate height grows, and root finiteness would not itself establish membership of every component in the basin of `1`. |

These are elementary written-proof reconstructions, not proof-assistant
certification. Their verdicts apply only to the pinned statements and
hypotheses.

## Integer implementation audit

The C++ program was read independently of the Python controller.

- A nonzero cache entry records an exact first-hit depth plus one and the
  exact total division exponent. The only initial entry is the root with
  depth zero. Each subsequent entry is obtained by prepending actual odd
  edges to an already verified first-hit tail.
- A path with no known tail after the horizon is excluded. If a known tail
  is encountered but its complete depth exceeds the horizon, that source
  is also excluded. It is permissible to cache that longer exact path;
  later sources are still compared against their own total depth.
- `unsigned __int128` is used for ordinary states. The multiplication
  guard checks `n<=(max128-1)/3` before evaluating `3*n+1`. The valuation
  routine handles both 64-bit halves and rejects a zero input.
- Depth and exponent totals are packed only after checking that each fits
  its 32-bit field. The resulting score arithmetic fits signed 64-bit
  integers under these explicit checks. Cache indices are used only for
  odd values at most the checked cutoff. No unproved convergence is needed
  for the bounded procedure to terminate.

The reviewer compiled the current C++ source with GCC using `-std=c++17
-O3 -Wall -Wextra -Wconversion -pedantic`. The sole diagnostic was the
expected portability warning for the GNU `unsigned __int128` extension.
The binary SHA-256 was
`74899d1cce9580e3b324ca43f9ce5ee6aa50cb2d52bd6b294149ac8732b4bc90`,
exactly matching the binary hash in both large saved receipts.

## Checks actually executed in this review

1. The independent uncached arbitrary-integer replay at horizon `1,000`,
   with inverse-tree controls at horizons `0`, `1`, `10`, `20`, `30`, and
   `40`, reproduced the saved Python receipt.
2. A newly compiled C++ replay at horizon `1,000` returned the same `9,759`
   candidate outcomes and root maximum `0`; its maximum first-hit odd depth
   was `113` and maximum division sum was `194`.
3. The separate `check_review.py` direct valuation-loop implementation
   matched nine C++ result fields on `54` cutoff/horizon combinations,
   totaling `3,420` candidate cases. It explicitly includes zero horizon
   and sources which have not hit within their horizons.
4. That same independent checker replayed `10,100` legal inverse-one
   letters and `199` bounded-ratio comparisons from O1-local, and checked
   the rational positivity bound for O2.

The review did **not** rerun horizon `1,500` or `2,000`. Their original
receipts were inspected, their exact height cutoffs independently checked,
and their executable digest matched the fresh build. The large computations
remain originating-run evidence, with the smaller independent implementation
providing a separate bounded cross-check. The integration report should
distinguish these events from the full repository validator.
