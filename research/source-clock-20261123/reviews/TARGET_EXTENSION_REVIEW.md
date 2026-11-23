# Independent review: deterministic-scale information extension

Reviewer lane: target descent. Date: 2026-11-23.

**Verdict: PASS within the stated source-qualified scope.** The extension
proves a strictly positive lower Shannon information dimension for the
specified actual real boundary law, with the displayed coefficient. Its
transfer to each fixed absolutely continuous path reweighting and to the
countable ordinary component mixture is valid. No lower local dimension or
collision upper bound follows from this review.

## Frozen artifacts and scope

| Artifact | SHA-256 |
|---|---|
| `research/source-clock-20261123/EXTENSIONS.md` | `0681b6a52408ee704f584110381ed5a259fb6d4a65d238631549069010b32b1b` |
| `research/source-clock-20261123/BOUNDARY_OVERLAP.md` | `086640abba47b80e1c6d9baee8b2e6bb003e8fd320fe5afb2cd202e7b10838c4` |

The companion boundary argument was independently reviewed in
`TARGET_BOUNDARY_REVIEW.md`. For the additional selection citation I read
PR #175, `8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`,
Section 5, equation (16). It supplies the stated full-path-functional
correlation implication under its own source qualifications. It does not
assert convergence in probability or almost surely of the sample-path
Cesaro averages. The extension does not need such an assertion.

The clock-tail calculation was independently derived by this reviewer and
then integrated by the boundary owner. The entropy extension and final
absolutely continuous transfer were checked against the frozen text. The
infinite assertions remain written deductions, not Lean declarations.

## 1. Clock tail and expectation-to-probability conversion

For total valuation `A`, the number of legal depth-`r` inverse words is at
most `binom(A-1,r-1)`. On the low-profile event each retains its original
cylinder mass at most `(B/F(q))*3^r*2^(-A)`. The identity

\[
\sum_{A\ge r}\binom{A-1}{r-1}(3/4)^A=3^r
\]

therefore gives exactly

\[
\mathsf P_q\{F(X_r)\le B,A_r\ge6r\}
\le\frac B{F(q)}9^r(2/3)^{6r}
=\frac B{F(q)}(64/81)^r.
\]

This bound is correctly restricted to low-profile endpoints.

Reducing the admissible positive floor to `alpha <= 1` makes
`0 < theta < 1` explicit. The unconditional selection identity yields
`liminf E L_N/N >= theta`. For `b=theta/2`, the elementary inequality
`E L_N/N <= b+(1-b)P(L_N>=bN)` gives precisely
`liminf P(E_N) >= p_* = theta/(2-theta)`. No pathwise lower-frequency
conclusion is inserted.

On `E_N`, the latest low-profile time `r<N` has
`L_r=L_N-1 >= bN-1`. Hence `r >= bN-1`, and eventually `r >= bN/2`.
The multiplier bound gives `a_r <= C_q exp(-kappa*b*N)` with exactly
the displayed `C_q`. The union of the exceptional clock events for these
possible `r` has exponentially vanishing probability.

## 2. Deterministic scales and the entropy coefficient

Outside the clock exception, `A_r<6r` implies
`a_r >= (3/64)^r >= (3/64)^N`. Combining this with the multiplier upper
bound and `D>=1` gives both sides of (E8). The lower side is essential:
it provides a deterministic fine radius contained in the randomly selected
good shadow radius.

For each possible depth, summing the heavy-cell bound over all totals with
`a_r <= C_q exp(-beta*N)` is a geometric sum. Summing over fewer than `N`
possible depths yields exactly (E10), including its factor `N`. For each
fixed `s<1`, that error still tends to zero exponentially up to a polynomial
factor. The bound is for the full reference ball mass, not only the
restricted cylinder measure.

The dyadic level

\[
k_N=\lceil\rho\log_2(64/3)N\rceil
\]

has cell diameter at most the deterministic radius in (E11). Therefore a
set of lower limiting mass at least `p_*` has cell information at least
`s*rho*beta*N-O_q(1)`. All other cell information is nonnegative.
Taking expectations and dividing by `k_N log 2` proves the claimed lower
bound along `k_N`.

There is no subsequence gap in the final liminf: `rho=1/40` gives
`0<rho*log_2(64/3)<1`, so `k_N` is unbounded and increases by zero or one.
It visits every sufficiently large integer. The coefficient after
`s` increases to one is

\[
\frac{p_*\beta}{\log(64/3)}
=\frac{\kappa\theta^2}{2(2-\theta)\log(64/3)},
\]

as stated. The root-dependent finite prefactors vanish after division by
the resolution; the onset need not be uniform in the root.

## 3. Fixed absolutely continuous reweighting

For a fixed probability `Q=wP`, the full-event selection identity first
extends to bounded simple functions. Truncating the nonnegative integrable
density `w` incurs error at most
`(2/alpha) E_P(w-min(w,m))`, uniformly in the averaging horizon. This
establishes (E13) and preserves the same `theta` and `p_*` under `Q`.

If exceptional sets `A_N` have `P(A_N)->0`, then `Q(A_N)->0` by absolute
continuity of the finite integral. For example,

\[
Q(A_N)\le mP(A_N)+E_P[w\mathbf1_{w>m}],
\]

followed first by `N->infinity` and then `m->infinity`, proves the needed
transfer without any bounded-density assumption. The geometric bounds may
lose their exponential rate after this change of law, but only their
vanishing is used in the entropy limit.

The arbitrary fixed reference measure allowed by the heavy-cell estimate
can be chosen to be the real marginal of this `Q`. Thus the entropy is
computed under the reweighted law itself. The same `d_B` follows. The word
“fixed” is necessary: this argument does not permit a sequence of densities
chosen separately at each resolution.

## 4. Affine coordinates and countable component mixtures

Fixed nonzero affine coordinate changes alter matching partition levels
by a constant and produce bounded cell-intersection multiplicity. They
therefore preserve the information dimension used here.

For a finite collection of clock-zero roots, entropy concavity bounds the
component entropy below by the sum of the weighted conditional entropies.
The residual mixture contributes nonnegative entropy and can be discarded
for this lower bound. Taking the resolution liminf for the finite sum
gives its total weight times the root-uniform `d_B`. Increasing the finite
collection until its weight tends to one proves (E15). This order of
limits avoids assuming any root-uniform convergence onset.

The source comparisons used to identify the conditional ordinary, critical,
and trace laws remain explicit. No convenient replacement of the component
law is used in this transfer.

## 5. Central-target boundary

The conclusion is an all-scale lower bound on mean real information. It
does not furnish the same-clock ternary collision upper bound of PR185.
The explicit density in `COLLISION_TRANSFER.md` has exact local dimension
one and Shannon information dimension one, yet retains collision at least
`c*sqrt(m)*3^(-theta*m)`. Thus even a larger coefficient in the present
information-dimension theorem would require an additional concentration
argument before it could settle that collision target.
