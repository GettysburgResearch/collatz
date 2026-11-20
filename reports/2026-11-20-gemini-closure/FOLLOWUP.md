# Direct attempts at the remaining global steps

**Collatz remains unresolved.** This follow-up continued the three global
attacks after publication of the initial audit. Its positive output is a
certified counterexample to iterating the initial drift estimate for one
explicit full-support input. It does not claim eventual absorption.

## Fixed-source transport

For the actual unsafe return operator, fix
`f0(u)=1/[u(u+1)]` on `U` and zero elsewhere. Put
`E_j=||H^j f0||_psi` and `D_j=E_(j+1)-E_j`. Integer interval arithmetic and
an analytic bound for all omitted original sources certify

\[
-0.209006853156\le D_0\le-0.188077839702,
\]

\[
0.000132428698\le D_9\le0.000217170924.
\]

Thus negative seed drift cannot simply be re-applied after actual transport,
even for this particular unchanged full-support input. Source 27 supplies the
exact unsafe-return path
`27,31,121,91,103,175,445,334,167,319,1822`; accumulated mass at 319 is more
than 179 times its initial seed mass by return nine.

The omitted sources above `N` contribute only `O(1)` to the `N`-return
Cesaro energy. The remaining long-time term is the finite triangular array
of actual histories from starts at most `N`. Its required
`o(log log N)` bound is still open. The detailed note also proves that the
log-log rank gauge differs by at most `log 2` from the corresponding ordinary
height gauge, so this target has not gained an unstated arithmetic hypothesis.

See [the proof and exact certificate](../../research/gemini-global-closure-20261120/FIXED_SOURCE_DRIFT.md).
The computation certifies two whole-source signs. It does not extrapolate
them to later return times or rule out a different correction to the gauge.

## Arbitrary-period cycles

The attempted product of active component-rank contractions and mode-switch
factors has exact cancellation. For a nonabsorbing `A`-cycle `n_i>1`, with
indices taken cyclically, module lengths `L_i=(a_i+1)k_i`, and odd counts
`Q_i=a_i k_i`, the switch product reduces to

\[
\prod_i\left|
\frac{z_{a_{i+1}}(n_{i+1})}{z_{a_i}(n_{i+1})}
\right|=\frac{2^{\sum_iL_i}}{3^{\sum_iQ_i}}.
\]

This already follows from the affine module identities. Multiplying the
ternary valuation gains therefore does not furnish a contradictory cycle
drift. For a primitive positive cycle word the unexcluded ordinary condition
remains the full divisibility
`2^L-3^Q | C_w`, with positive denominator.

The reconstructed positive rational local models are already subsumed by
PR149's stronger
[`RATIONAL_CYCLES.md`](https://github.com/GettysburgResearch/collatz/blob/92c0129e794dde3ec55ceec470a12d51ba3f7e2f/research/forward-inverse-defect/RATIONAL_CYCLES.md).
They are not republished as a new result. Such rational models do not refute
integer-specific height bounds; the attempt did not turn those bounds into
an arbitrary-period exclusion.

## Adaptive smaller-source mergers

Keep an ordinary source `n` fixed and let `y=T^i(n)`. For a candidate parity
word `w` of length `j`, with `p` odd positions `t_1<...<t_p` numbered from
zero, put `C_w=sum_(l=1)^p 3^(p-l)2^(t_l)`. A smaller positive companion
following that word exists exactly when the same coefficient satisfies

\[
2^j y-3^pn<C_w<2^jy,
\qquad C_w\equiv2^jy\pmod{3^p}.
\]

Indeed its start must be `(2^j y-C_w)/3^p`; the strict inequalities give
`0<m<n`, and the integral start belongs to the word's unique legal binary
parity cylinder. The missing selection argument must control this real
interval and ternary congruence simultaneously for the unchanged source.
An inverse compiler's congruence control alone does not establish the
required ordinary-size bound.

The signed `-1` shadow supplies finite necessary clock costs. Those costs
do not prove an indefinitely decreasing selector rank. The stabilized
`kappa` invariant is defined using a known hit of 1, so using it for an
arbitrary unknown source requires an independent totality argument. No
such argument was obtained, and no additional finite leaf census is offered
as a replacement.
