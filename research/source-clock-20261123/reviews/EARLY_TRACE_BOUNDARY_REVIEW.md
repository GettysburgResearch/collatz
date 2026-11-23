# Independent reconstruction of the actual boundary dimension argument

Date: 2026-11-23. Reviewer lane: `early_trace`.

## Frozen object and verdict

The reviewed object is the uncommitted draft
`research/source-clock-20261123/BOUNDARY_OVERLAP.md`, Sections 2--6, based on
PR180 commit `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`, with exact content
SHA256

```
086640abba47b80e1c6d9baee8b2e6bb003e8fd320fe5afb2cd202e7b10838c4
```

**Verdict: VERIFIED as a deduction from the explicitly supplied,
source-qualified inputs.** I reconstructed the cone-floor implication,
endpoint subsequence, actual-law overlap count, infinite valuation-clock
sum, arbitrary-reference transfer, and separate nonatomicity argument.
No mathematical correction was required in these sections at this hash.
This verdict does not validate the imported trace construction, positive
floor, selection theorem, or distinct-path reciprocal estimate. It is not
a Lean verification and does not establish escape or cycle exclusion.

The qualification is substantive: if any retained analytic input fails,
the conclusions do not follow from this review alone. A later source hash
requires a separate review boundary.

## 1. The low-profile cone and its real shadow

For a legal finite path from an ancestor `u` to `n`, let `omega` be its
actual multiplier. Iterated positive harmonicity gives
`F(n) >= omega F(u) >= alpha omega`. The reciprocal estimate gives
`omega u/n >= delta`. Thus `F(n) <= B` implies
`u >= alpha delta n/B` for **every** ancestor. This is a whole-cone
statement; it does not infer a floor from a likely sampled continuation.

For any continuation of a retained low-profile endpoint `n = X_r`, all
continued states are at least `c_B n`. Its remaining lambda product is
at least `exp(-C_0(c_B n)^(-rho))`. The exact affine identity then gives

\[
R-R_r\le C_0c_B^{-\rho}a_rn^{1-\rho}
       \le C_0c_B^{-\rho}q^{1-\rho}a_r^\rho.
\]

The last inequality is `a_r n <= q`, with the exponent retained; it does
not replace `n` by its expectation. If the reciprocal estimate is stated
only at integer thresholds at least one, its use at `c_B n` follows by
rounding up when this threshold exceeds one, and by the threshold-one
bound otherwise. The displayed shadow remains valid in both cases.

## 2. The endpoint subsequence uses only upper return frequency

The full-event selection input implies `limsup L_N/N >= theta_B` almost
surely. To check the quantifier, on an event where this limsup is below
`theta_B` by a fixed positive margin, the pointwise bound
`g <= 2/B + (2/alpha-2/B) 1_(F<=B)` makes the limsup of the averages of
`g` strictly less than one. Reverse Fatou contradicts the selection
identity on that same full-path event. Taking countably many margins is
legitimate. This yields no lower return frequency.

The three integral parents with exponents `e_0, e_0+2, e_0+4` have all
three ternary residues: modulo nine, `4^j = 1+3j`. Therefore two distinct
unit parents have exponent at most six. At a low-profile node their
probabilities are at least `p_B = 3 alpha/(64B)`. Every selected edge has
probability at most `1-p_B`, including an edge outside this pair.
Telescoping hence gives `a_r <= (F(q)/alpha) exp(-kappa_B L_r)`.

For each large `N` with `L_N >= theta_B N/2`, let `r<N` be its last
low-profile time. Then `L_r=L_N-1`, `r` tends to infinity, and eventually
`L_r >= theta_B r/4`. This proves the exponential-multiplier subsequence
with low-profile **endpoints**, without strengthening limsup frequency.

## 3. Same-total counting retains the original probabilities

At fixed actual depth `r` and valuation total `A`, write
`a=3^r 2^(-A)` and `t=D a^rho`. Distinct words have distinct odd
endpoints, because the deterministic forward path recovers the word.
Their offsets `q-a n` are consequently separated by at least `2a`.
Any boundary point in a cell of length `t` comes from an offset in an
interval of length `2t`, hence from at most `t/a+1` retained prefixes.
Each prefix has its unconditioned canonical mass at most `Ba/F(q)`.
For `a<=1`, `t>=a`, so the cell's restricted mass is at most
`2Bt/F(q)`, as in (17).

For **any fixed** reference probability `eta`, the enlarged closed cells
have overlap multiplicity at most four. At most `4t^(-s)` cells can have
enlarged `eta`-mass greater than `t^s`. Multiplication by the preceding
restricted-cell bound proves (18). In particular, no identity of `eta`
with the sampled boundary marginal was used. Atomic or singular reference
measures do not invalidate the counting argument.

## 4. Exact verification of the infinite clock sum (19)

Let

\[
 A_0(r)=\left\lceil\frac{r\log3+cr}{\log2}\right\rceil,
 \qquad v=\rho(1-s)>0.
\]

All retained totals satisfy `A>=A_0(r)`. Their contribution in (18) is
bounded by `8B D^(1-s)/F(q)` times

\[
 \sum_{A\ge A_0(r)}(3^r2^{-A})^v
 =\frac{(3^r2^{-A_0(r)})^v}{1-2^{-v}}
 \le\frac{e^{-crv}}{1-2^{-v}}.
\]

This is the displayed bound (19). It is summable in `r` and permits
arbitrarily large actual totals. There is no hidden assumption that
`A_r=O(r)`, no union bound with an infinite constant, and no replacement
of the original valuation clock by its mean.

Borel--Cantelli removes only finitely many bad depths for fixed `eta,s`.
The good-return subsequence is infinite, and its scales tend to zero.
Since division by `log t<0` reverses inequalities, the remaining
`eta(B(R,t)) <= t^s` gives the asserted limsup local dimension **at
least** `s`. Countably many rational `s<1` give (21). This controls a
limsup only; even very long gaps between good scales remain permitted.

## 5. Common-law transfer and the separate no-atom check

The general upper-local-dimension bound at almost every point of a bounded
real probability is valid: the total mass of dyadic cells lighter than
`2^(-k(1+epsilon))` is summable in `k`. The containing cell lies in the
ball of radius `2^(-k)`, and interpolation between consecutive radii
gives upper local dimension at most `1+epsilon` eventually.

For the component transfer, condition on a fixed clock-zero ordinary root
`q`. The exact coordinate relation is `R=q-chi(q)Z`, obtained by taking
the limit in the actual affine-prefix identity. In (21), choose the fixed
reference probability `(z -> q-chi(q)z)_* mu_E`. Bounded positive
equivalence of the conditional ordinary and trace path laws transfers the
almost-sure statement. A fixed nonzero affine factor does not change the
local dimension. There are countably many roots, so their exceptional
sets may be combined without a uniform estimate in `q`. This proves the
claim about the **original** common marginal `mu_E`; it does not rely on
dimension surviving a weak limit of different measures. Bounded positive
tilts then preserve local dimensions because their ball masses differ by
fixed multiplicative constants.

For Section 6, nonperiodicity ensures that each bounded integer can hit
the root at at most one depth; therefore the minimum depth-`r` endpoint
`H_r` tends to infinity. At fixed total, the number of low-profile shadows
containing one prescribed point is at most `D a^rho/(2a)+1`. Multiplying
by `Ba/F(q)` and summing the two geometric series over
`a<=q/H_r` gives (25), uniformly in the prescribed point. Applying the
full-event selection identity to `H={R=z}` then gives
`P(H) <= (2/B)P(H)`, hence zero. Merely positive upper return frequency
would not justify that final selection step; the draft uses the stronger
input correctly.

## 6. Source simplification and closure boundary

The selection input (7) is already a consequence of the pinned PR175
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`,
Section 5, equation (16). That result proves the stronger mean of absolute
full-path correlations. It can therefore supply the input without adding
a separate dependency on the wording of Paper 12. Its own trace and
analytic dependencies remain source-qualified. A mean of absolute
correlations is still not the expectation of the absolute sample-average
error, and does not supply lower return frequency.

The reviewed theorem is materially stronger than a support-dimension
claim: it proves nonatomicity and upper local dimension one for the
actual canonical real marginal. It does not give uniform concentration,
lower local dimension, or the same-clock ternary collision estimate.
In particular, the good real scales depend on the inverse path and its
valuation total. Neither (19) nor the arbitrary-reference formulation
identifies these scales with the ordinary-height trace depth or with the
retained moving ternary-time law. No direct escape-closing transfer was
found in this review.
