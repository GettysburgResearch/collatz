# Attempt to turn adelic mixing into a same-orbit entropy contradiction

**Status: unsuccessful direct closing attempt. No new global theorem, Lean
declaration, or improvement to the occupation rate is claimed.**

The target was the actual escaped orbit, using the new all-depth inverse
comparison, rather than an unrelated stationary random-gap law. This note
records the specific high-variance application tested and its first missing
inference. It is not a new literature catalogue.

## Exact input

Fix one hypothetical escaping positive odd unit orbit `q_j`. Under the
repo's qualified ordinary harmonic construction, `v_j=nu(q_j)` increases
to `C>0`. The canonical inverse kernel is

`K(q,x)=nu(x)/nu(q)` on actual edges `Ux=q`.

PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`,
`research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, proves
that the endpoint law after `r` inverse steps from the average of
`q_r,...,q_(r+M)` differs in total variation from the average of
`q_0,...,q_M` by at most

`1 - sum_(j=0)^M v_j / (C(M+1))`,

uniformly over **every** inverse depth `r`. Thus a lower entropy bound for
these precise moving laws would contradict the actual time-law entropy
ceiling `H_2(log_3 2)<1`.

PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`,
`research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md`,
also shows that the actual normalized real fibres approach a common
probability `mu_infinity`, uniformly over future source positions. Their
ordinary trace is available at ternary precision **j+r+1**, retaining the
original source clock. The same PR's phase note proves uniform leading-phase
discrepancy for distinct actual orbit segments. Its power rate is stronger
than checkpoint 13's fixed-run occupation rate; no rate refinement was
pursued here.

## The proposed mechanism

For the joint stationary real/ternary affine law, the fair shortcut maps

`f_0(x)=x/2`, `f_1(x)=(3x+1)/2`

both have product-Haar Jacobian `1/2`. Project to the compact quotient

`X = (R x Q_3) / diagonal Z[1/3]`.

Writing `T_a` for multiplication by `a` on this quotient, stationarity
implies the exact relation

`(T_2)_* mu = (mu + (T_3)_* mu)/2`.

The proposed argument was to combine this commuting-action relation and
dyadic equidistribution with the actual normalized fibre stabilization,
then obtain nondegenerate compact canonical inverse rows for the same
escaped time law. This would be enough: the stationary canonical entropy
identity in PR178 would force a mean valuation strictly above `log_2 3`,
contradicting the actual positive-orbit mean bound.

The quotient relation and dyadic mixing are **already present** in the
source-qualified manuscript *Geometry, integer fibres, and dyadic
equidistribution of the joint Collatz affine law*, v2, 22 October 2026,
Section 10.6. They are not new claims of this attempt. The manuscript was
read directly at <https://rstation.ai/problems/collatz/papers/19>.

Its exact binomial identity turns iterates of `T_2` into averages of powers
of `T_3`. Its displayed rates concern the unconditioned joint stationary
law. In particular it states dyadic convergence to Haar, a finite-partition
entropy bound, and a Wasserstein bound of order
`sqrt(log(n+2)) / (n+1)^(1/4)`. Its joint law is explicitly singular despite
full dimension, so neither product-Haar Jacobians nor maximal dimension can
be promoted to a finite continuous density.

## The quantitative point where the application stops

The moving actual fibres condition on

`z = q_j mod 3^(j+r+1)`

and retain real height of order `q_j`. Their source probability is not a
fixed positive-probability event in the unconditioned affine law. The trace
normalization multiplies its joint cylinder mass by `3^(j+r+1)` and then
compares it to a quantity of order `q_j`.

Even a total-variation error `epsilon` for unconditioned measures would
give a conditional error of order `epsilon / P(A)` on an event `A`, rather
than `epsilon`; a Wasserstein error by itself does not even control a
shrinking ternary cylinder indicator. The cited dyadic mixing result gives
neither the required conditional error nor uniformity at these moving
ordinary centres. Sending the dyadic mixing time arbitrarily far forward
also changes the law: the exact all-depth comparison applies to **inverse
Collatz windows** and does not identify dyadic pushforwards of the joint
affine measure with those windows.

There is a particularly concrete arithmetic feature one might exploit in
a future proof. Since `q_j+1 <= (3/2)^j(q_0+1)`, the ordinary integer centre
has at most

`j log_3(3/2) + O_(q_0)(1)`

ternary digits. At resolution `j+r+1`, a long high-digit zero tail remains.
Thus a useful replacement for generic almost-everywhere mixing would be
a **pointwise conditional estimate at ordinary rational centres of this
height**, with the retained real-height window and adequate constants.
No such theorem was derived from the cited boundary identification,
full-dimension statement, dyadic mixing, or leading-phase discrepancy.

The leading-phase theorem concerns the real logarithm of the same orbit
values and supplies no additional multiplication-by-two invariance of
their ternary time law. Adding that invariance would be an unsupported
step. No arbitrary compact control or changed-source family is offered as
a replacement proof.

## Outcome

The all-depth inverse comparison repairs the original change-of-law issue
for its precisely specified windows. It does not make every operation on
the ambient joint affine law available for those windows. The attempted
adelic mixing closure stops at a uniform conditional estimate for moving
ordinary integer fibres. This checkpoint therefore contributes no positive
closing estimate from this lane. The existing compact canonical-kernel
criterion remains a possible target, not an established consequence.

The external manuscript's analytic dependencies remain source-qualified;
they were read for applicability and were not independently re-proved or
installed as Lean axioms.

## Further direct test: the simultaneous Diophantine product

A second attempt used the actual finite cylinder rather than ambient
mixing. For an inverse prefix of length `n` from a positive odd unit `q`
to a positive odd unit `x`, put

`S_i = e_1 + ... + e_i`, `D = 2^(S_n)`, and
`B = sum_(i=1)^n 3^(i-1) 2^(S_n-S_i)`.

The exact relation is `qD-B=3^n x`. The last summand makes `B` odd,
so `(D,B)` is primitive. For a **fixed** `q`, test the two independent
linear forms `(X,qX-Y)` at the real and ternary places and `(X,Y)` at
the binary place. Their unnormalized all-place product at `(D,B)` is

\[
\begin{aligned}
 |D(qD-B)|_\infty\,|DB|_2\,|D(qD-B)|_3
 &=D(3^n x)\,D^{-1}\,3^{-n}\\
 &=x\ge1.
\end{aligned}
\]

The exact ternary factor uses `3` not dividing the retained endpoint `x`.
Thus these forms give no negative power of height. For the original
reversed prefix from `q_j` back to `p`, the numerical product is exactly
`p` at every `j`. In that growing-source family there is an additional
problem **before** testing the product threshold: `q=q_j` varies, so the
forms are not a fixed collection to which the standard theorem applies.
Putting this moving coefficient into a larger system does not by itself
help; the relation `B+p3^j-q_j2^(S_j)=0` is already a moving hyperplane.

The precise primary theorem checked was Jan-Hendrik Evertse,
[*The p-adic Subspace Theorem*](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf),
May 2011, Theorem 1.1 and its two-variable application on pages 2--3.
For two forms in two variables its hypothesis requires an upper bound
`C H^(-epsilon)` with `epsilon>0`, for fixed algebraic forms. Neither
the fixed-root product above nor the moving-source family supplies it.

No independent endpoint-only form of bounded dimension was found. Here
`B` has `n` summands, while the earlier sparse-return application obtains
bounded dimension from a separately assumed bound on endpoint binary
complexity. The ordinary high ternary zero tail does not provide that
bound. This calculation audits the attempted application; it is not a
new convergence estimate or cycle-exclusion theorem.
