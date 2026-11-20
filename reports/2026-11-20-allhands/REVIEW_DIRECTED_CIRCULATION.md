# Scoped independent reconstruction of the directed circulation theorem

Reviewer: `closure_directed`, independently of the authoring agent.

Reviewed text: `DIRECTED_BOUNDARY_CIRCULATION.md`, SHA256
`23e0fb30ca213fbac8aa1a6a948b323bebd2c192e6422eceed5a0d643fb220a6`.
The checker hash was recorded as
`8e2b7ca383655a4bf60cb22584ca38812402d0d1b7b3d3f1ba6293e5ef037e33`,
but this review does not claim an independent execution or complete code audit.

The source path construction was independently read in PR146,
`6863d298187af8b2619efbf78cc4b0aa8e627393`,
`research/upper-bit-mergers/DIRECTED_TRIPLING.md`.

## Verdict

**VERIFIED at the stated written-proof scope:** DC1, its extension to arbitrary moderate positive weights, and the clipping argument in DC3. The corollaries invoking the analytic coercivity and predecessor theorems remain qualified by precisely those source inputs; this review does not independently reprove them.

## Return path and incoming multiplicity

For x divisible by 3^5, the chosen high return has at most two neighbor crossings of eight ordinary edges each, seven exponent descents of eleven edges each, and six simple triplings. Thus 16+77+6=99 is valid. In an exponent descent from i to i−1 the unique tripling source is `8*3^(i−3)*v−1`. The allowed exponents range from b+1 through a, so its index is between zero and six. The two strings of simple triplings use disjoint exponent ranges: the initial range starts at six, and the final range ends at four. No label slot is repeated within one high return.

For x=3^j u, j≤4, the low return length is bounded by

`(a−j−1) + 18 + a + 99 + a + j = 3a+116`.

The CRT exponent search has maximum at most `4+486*64=31108`, so the stated A=31110 is valid. The displayed L=3A+120 is a valid integer overestimate. Every elementary positive edge changes height by a factor in [1/3,3], giving the advertised H after including the initial value 3x.

The label count is

`17 + 5*(A+1) + 5*A*17 = 90A+22`.

The first seventeen labels are for the original high case. Each of the five low valuation strata has its direct simple-power labels and one high-return list for each possible a. Distinct labels can produce the same integer, which is why they must retain multiplicity. However, each fixed affine label is injective in x on its actual domain, and each slot occurs at most once for a given return. Thus at most M incoming occurrences contribute to a fixed y. Negative affine intercepts cause no issue because positivity is imposed on the actual path domain, and the height estimate comes from the positive path itself.

## Ordering the summability argument

The finite cycle identity holds for every invariant real f because ordinary edges contribute zero and the allowed tripling edges carry the exact signed differences. The two positive inequalities hold pointwise without convergence assumptions. Tonelli applies to each nonnegative double sum, and moderate-weight comparability plus the incoming multiplicity gives both one-sided estimates.

Finiteness of either original weighted oriented moment therefore forces finiteness of the other. Only after this step does the argument sum the signed cycle identity. The double series of absolute differences is bounded by M K_omega times the original absolute moment, so the reordering is legitimate. No cancellation of infinite quantities is used. The same incoming multiplicity proves the claimed pointwise two-sided comparison of pi_omega and omega.

The common weight depends solely on the deterministic chosen returns and omega. It is not chosen after seeing f or a component cut. A positive circulation by itself does not exclude more than one component; the paper preserves this limit.

## Functional extensions

For DC3, clipping to [a,b] is monotone and 1-Lipschitz. Consequently neither oriented defect can increase under clipping. The bounded-label result therefore applies to every clipped label. If the original real f took two distinct values, clipping between those values would preserve their difference, contradicting constancy of the clipped label. This establishes the extension without assuming f is bounded or summable.

The predecessor counting input `A_C(X)≥c_C X^beta` at all sufficiently large X implies divergence of the critical component series by partial summation. It is essential that this is the source input at that scope; merely a sequence of isolated count lower bounds would need a separate argument. The paper attributes the input rather than claiming its reproof.

No result reviewed here proves the arithmetic moment upper bound needed to eliminate a cut. The exact circulation and the existing permanent-failure upper bound can both hold for a nonempty hypothetical boundary.
