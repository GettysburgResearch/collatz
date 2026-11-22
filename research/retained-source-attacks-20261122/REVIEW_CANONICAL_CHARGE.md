# Independent review: nonlinear canonical charge

Date: 2026-11-22. Reviewer: sibling-mass research lane.

**Verdict: VERIFIED within the explicitly source-qualified inputs.**
The entropy identities, whole ordinary-path law, physical boundary
family, and positive pole residue are valid at the reviewed bytes.
They do not prove absence of an escaping component.

Reviewed file: `CANONICAL_CHARGE.md`.

Reviewed SHA256:
`979d6be5c4345489c3a71b1e1696ce60bb675d9000bc0800a6cb4ec04557566c`.

The reconstruction below was performed from the statements and actual
algebra, rather than from the author's conclusion. The prior existence
of the canonical functions and the quantitative ordinary path-count
bound remain imported assumptions with their original qualifications.

## 1. Maps, row normalization and the entropy sign

The domain contains the positive odd ternary units which are not
themselves periodic. It permits a vertex whose future is eventually
periodic; killing occurs when the trajectory first reaches a periodic
vertex. On the escaping component used in the new calculations there
is no killing, and every parent remains in that same component.

I checked normalization directly. `L nu=nu` makes `K` a probability
row, and `h=L(lambda h)` makes `K_h` a probability row. With
`u=lambda h/nu`, one has

\[
 Ku(q)=\frac{h(q)}{\nu(q)}=\frac{u(q)}{\lambda(q)},\qquad
 \frac{K_h(q,n)}{K(q,n)}=
       \lambda(q)\frac{u(n)}{u(q)}.
\]

The bounds `3 delta/4 <= u <= 1` make both the likelihood ratio and
its reciprocal uniformly finite. Thus the countable row logarithm is
absolutely integrable. Substitution gives precisely

\[
 D_{\rm KL}(K(q,\cdot)\Vert K_h(q,\cdot))
   =(I-K)\log u(q)-\log\lambda(q)
   =\log Ku(q)-K\log u(q).
\]

In particular the entropy orientation and the sign of the boundary
term in equations (9)--(10) are correct.

## 2. Infinite signed summation and the two clock ends

The imported absolute edge variation of `R` controls that of `log u`
by the Lipschitz constant `4/(3 delta)`. Reindexing incoming edges is
then an absolutely convergent calculation, not a cancellation of two
infinite integrals of a bounded function against an infinite measure.

Each synchronous level has mass `c_E`. Averaging `K psi` over level
`r` gives the average of `psi` over level `r-1`, because each parent
has one forward image and `L nu=nu`. The negative-clock endpoint is
zero: the cumulative source formula gives `Rbar_r -> 0`, and
`abs(log(1-R)) <= R/(3 delta/4)`. At the positive-clock endpoint,
one fixed forward ray captures a fraction `nu(q_r)/c_E -> 1` of
the level's mass. Boundedness of `log u` therefore gives the limit
`log(1-F_E)` for the entire level average.

These facts license the finite-level telescope followed by exhaustion.
The result is `c_E log(1-F_E)`, with no residual clock source omitted.
Also `d(n) >= delta nu(n)/(4n)` and `log(1+1/(3n)) <= 1/(3n)`
give the stated finite bound for `H_E`. Equations (10)--(11) follow.
Since `1-F_E >= 3 delta/4`, their logarithm is well defined.

## 3. Ordinary whole-path probability and physical normalization

I reconstructed the path law from finite intervals. At any leftmost
clock, assign mass `nu(n)/c_E` to its state and follow the actual
forward map through the interval. Summing one earlier clock produces
the next distribution by `L nu=nu`. These interval laws are consistent
and have total mass one, so they define the stated two-sided law.
Its backwards conditional law is exactly `K`.

A vertex has one specified clock and can occur only there. Thus the
probability that a path contains `n` is exactly `nu(n)/c_E`; there
is no extra sum over possible visit times. Each finite interval is an
actual retained simple forward path. The source-qualified count bound
extends to all clocks by increasing finite intervals, yielding both
`sum 1/Q_r <= 200` and the uniform height tail. This does not
identify a complete inverse ray with the forward orbit of one
ordinary starting integer.

For real `z>=0`, the product in (16) is well defined and is bounded
below by `exp(-200 z/3)`. Its exponential-variable representation is
legitimate because the conditional total mean is at most `200/3`.
The mixture is therefore completely monotone. This representation
leaves the actual integer-path law unchanged.

The root in (17) must be excluded from the inverse product, as it is
in the reviewed text. Conditioning the whole-path law at level `k`
then gives

\[
 h_z(q_k)/c_E=
 \mathbb E\left[1_{\{Q_k=q_k\}}
                 \prod_{r<k}\lambda_z(Q_r)\right].
\]

The omitted event has probability tending to zero and the partial
products are bounded, which proves (18). The final text also gives
a pointwise proof of `h_1=h`: `nu-h=sum_(j>=1)L^j d` implies
`T^k(nu-h) <= sum_(j>=k+1)L^j d -> 0`. This avoids requiring an
unstated Banach-space membership for the reference.

Differentiation at zero is justified by the uniform reciprocal sum.
Using the exact vertex inclusion probabilities gives (20). For the
whole-path tilt in (20a), its density is the product divided by its
positive expectation. The expected negative logarithm is `H_E/c_E`,
so the displayed equality with the finite row-entropy budget is also
correct.

## 4. Complex continuation and the least-state residue

Let `m=min E`. The absence of repeated states means the factor
`3m/(3m+z)` occurs either zero or one time in each path product.
Every other odd state is at least `m+2`. This gives the exact split
(21) into an analytic term and one possible simple pole.

On compact subsets of `Re z>-3m`, finitely many small factors have
denominators bounded away from zero. For the remaining factors,
the logarithmic tail is bounded by a constant times `sum 1/n`.
The height-tail bound makes the product convergence uniform over all
sampled paths. The same estimates on `abs(z+3m)<3`, after deleting
the `m` factor, establish holomorphy of both `A_E` and `C_E` there.
Finite-height truncations involve finitely many possible states, so
their expectations are finite sums of holomorphic products. Uniform
convergence justifies passage to the expected infinite product.

At `z=-3m` each remaining factor is `n/(n-m)>1`. The event of
visiting `m` has probability `nu(m)/c_E`, so the residue is at least
`3m nu(m)>0`. Its finiteness follows from

\[
 -\log(1-m/n)\le\frac{m}{n-m}
 \le\frac{m(m+2)}{2n}\quad(n\ge m+2),
\]

and the reciprocal sum bound. Hence this is a genuine nonremovable
simple pole of the continuation of the original positive-parameter
function, not a pole of an unrelated formal expression. The distinction
from the upstream entire linear deformation is necessary and correctly
retained.

## 5. Scope of this review

The exact pinned upstream files were inspected for their definitions,
variation theorem, occupation bound and harmonic correspondence. Their
full earlier analytic proofs were not re-audited, and no Lean replay
is claimed for this infinite argument. The root's separately authored
`ANALYTIC_PARAMETER.md`, linked near the end of the reviewed note, is
outside this review.

The two clarifications requested during reconstruction—the pointwise
`h_1=h` proof and explicit continuation from `Re z>-3m`—are present
in the SHA256 bound above. No remaining correction was required.
This verdict does not extend to later source bytes, sibling-current
estimates, other components, or a full Collatz proof.
