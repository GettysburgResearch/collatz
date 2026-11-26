# Independent review of the closing, population and geometric arguments

The wall-work contributor independently checked the following written arguments on 26 November 2026. SHA-256 identifies the reviewed bytes. The common project baseline was PR197 at `f74d2144275c3e1f9148b0b2997fecc7931ae7f5`.

| Reviewed file | SHA-256 |
|---|---|
| `critical/FORCED_CLOSINGS.md` | `9f61ef7fdb4f20ed9d204b232ee55520510547c07698cef97057fc776930d8bb` |
| `critical/FINITE_RECORD_POPULATION.md` | `78004a67b99ff3c2706e138660b39aca2ddc9a36b31c72f13a01f4d8326836c5` |
| `critical/FIRST_ATTACHMENT_CLOCK.md` | `cc775e321cb99e98598aae72bbaf142067b8ca6227e3d85d413a7f5570228e38` |
| `critical/PRECISION.md` | `a25080546a0c3a65b907532143e5cdd3fdbeb1ae7f762aca4402f0a6b38b79ff` |
| `adelic/GEOMETRIC_SLICES.md` | `e916a32b7da760183d54e0a25c3df3ebe5f331a0ca753332d7fb2a66c21f5d08` |
| `adelic/check_geometric.py` | `2d1cba6ed74b197001873cf02c5d2c9cd0235a28cf77042c00278e5f7ef4eacf` |

## Forced closings and finite population

The same-center hypothesis is used for the ternary past and dyadic future data. I checked the integer displacements, fixed-place product and carries against the stated precisions. The inequality $2\delta+1-\rho<\theta$ suffices to make each of the nearby labels on its own side agree. Rotation to a common chronological phase preserves the candidate least odd/shortcut period. At a coefficient record the slope satisfies $2^s<3^b$ and the allowed carry is bounded by $(9/2)^b$. The suggested small-denominator product and the spacing on $K-1$ therefore give the claimed bounded number of qualifying closings under the paper's hypotheses.

For the finite population I checked the reverse script, positivity and integrality of the reconstructed centers, cyclic indexing at the endpoint of a rotated suffix, and the choice of the unique odd lift of each residue in $[3^n,3^{n+1})$. The bounded multiplicity of carries in a fixed residue and the final exponent $1-\theta+2\delta+1-\rho<0.94$ are compatible. The starting integer varies with the approximating word. A fixed-root conclusion would require an additional argument. I found no mathematical defect in the stated conclusions.

## First physical attachment

I independently checked the first-attachment clock argument, including the final ascent phase $u=j$ and a visitor with $n=0$. The target $Y_u$ has a unique odd predecessor $(2Y_u-1)/3=Y_{u-1}$ even when the target itself is even. First contact with the entire indicated prefix therefore forces arrival by an even step. After subtracting the first $k$ terms of the positive carry sum, the denominator divides $3^{\max(B,i_{k-1}+d)}$, since each removed term has denominator $3^{d-r+i_r}$. The remaining positive rational is at least the reciprocal of that power and strictly below $(2/3)^{i_k}$. The inequality $(3/2)^3>3$ gives the stated iteration. It also gives $d<3B$ and the resulting $t\le3^{6B}$. I found no mathematical defect. Existence of a smaller visitor remains outside the conclusion.

## Geometric slices

I checked the affine two-arm $O(1/\sqrt h)$ estimate against its pinned repository source and the period-to-exceptional-count conversion on arbitrarily translated intervals. For odd bases the low-precision change in $P_{j-42}$ has valuation $3+c+v_2(t'-t)$. In the near-minus-one case normalizing by $p+3$ removes the base-dependent valuation. The residual valuation is $1+v_2(t'-t)$, with at most one further binary digit from the parity of the number of laps. The 389-step synchronized anchors have compensated grades 31 and zero.

For the negative terminal the lower 62-step anchor contributes $3^5$. The following laps and last odd step give $2+3^{r-24}u$ against $1+3^{r+13}u$, so the relative multiplier is exactly $3^{37}$. I checked the sign and leading factor of the binomial series for the stabilized unit. The even-base split has bounded valuation after squaring an element congruent to three modulo eight. When the remaining rotation is near plus or minus one, the two terminal certificates handle both signs. Discarding the initial $O(h+H_-)$ exponents is uniform in the base and interval. The implicit absolute constant can depend on the fixed 334711-bit precision.

I independently reran the supplied exact checker. It verified all 164 terminal blocks, the first merger at clock 334711, odd counts 167282 and 167319, three signed anchor profiles, and the 2957-bit unit control. The general geometric interval estimate remains a written theorem using the pinned affine estimate. [Affine estimate at the inspected revision](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

This review was independent of the authors of those two packets. The wall constructions and their Lean audit are the reviewer's own work and are documented in `WALL_RESULTS.md`.
