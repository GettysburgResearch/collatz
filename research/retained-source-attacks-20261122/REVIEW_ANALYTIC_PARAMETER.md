# Independent review: the analytic parameter attempt

Reviewer: `/root/canonical_charge`. Date: 2026-11-22.

**Verdict: VERIFIED WITH FIXES, at the written deduction level, conditional
on the explicitly pinned ordinary path-count and strict-resolvent inputs.**
The final reviewed version incorporates the one subset-count correction
identified below. No escape-exclusion theorem or analytic Lean formalization
is approved by this review.

## Frozen files

| File | SHA256 |
|---|---|
| `ANALYTIC_PARAMETER.md` | `c4d81e33b76a2b92901365c11325aa90c1777939711c03fd833d2d91f84bad22` |
| `lean/SurvivalCurvature.lean` | `f667a8b1292126ec77ce3889ab432dae22655b1595e1a82e5da02d426bec80d0` |
| `lean/SurvivalAudit.lean` | `81aaf69137c451cacac7991f51e98c5b854137892d4df7b98e2850615d704d04` |

These are paths relative to this packet. The Lean review here concerns the
statement and finite algebra. Compiler execution and axiom-output evidence
belong to the separate root replay receipt; this reviewer did not run a second
compiler replay.

## Reconstruction

1. **Laplace rigidity.** For a finite positive representing measure, all
   positive-parameter derivatives exist. Continuity of an assumed entire
   extension at zero and monotone convergence identify every moment as finite.
   Its Taylor expansion at a negative real argument has nonnegative terms,
   so Tonelli identifies it with the exponential moment. Any positive measure
   above a fixed positive holding time forces ordinary exponential growth.
   This contradicts the displayed order-below-one majorant. No inaccessible
   proof of Bernstein's representation theorem is needed for this implication.

2. **Uniform actual-path product.** Independently integrating each
   `log(1+t/(3n))` gives `t/[u(3u+t)]` above its ordinary state. With
   `a=t/3`, the count estimate bounds the integral by
   `5 a^theta int_0^infinity v^(theta-1)/(1+v) dv`. Splitting at one gives
   `1/theta+1/(1-theta)=1/[theta(1-theta)]`. The bound is uniform in the
   original path and every interior subset. In the initial draft an equality
   used the full-path counting function for a subset; it has been corrected
   to an inequality in the frozen file.

3. **Operator column estimate.** The positive majorant of the off-diagonal
   kernel is `|z| exp(B_theta |z|^theta)` times precisely the old strict
   positive kernel `K`. The source factor, endpoint exclusion, weighted
   input/output space, and killed domain are unchanged. Hence the stated
   norm bound follows from `||K||<=A_s`; it does not rely on raw transport
   being bounded. Its logarithmic growth gives entire order at most theta.

4. **Same-source curvature.** For a finite product, its value, first
   derivative and second derivative at zero are respectively
   `1`, `-sum w`, and `(sum w)^2-sum w^2`. Consequently its moment
   determinant is exactly `-sum w^2`. Positive ordinary weights make this
   strictly negative for a nonempty path. Absolute summability of weights
   licenses local uniform product convergence and these derivative limits.
   Cauchy--Schwarz for a positive Laplace measure gives the opposite sign.
   Thus the intended positive representation fails on the same original
   escaping atom, not merely on an unrelated test function.

5. **Physical rational family.** The exponential holding-time construction
   uses the original fixed Collatz states and their exact rates. Finite mean
   of the nonnegative total gives almost sure finiteness. At the least state,
   the one matching factor has a simple pole; the product of all other
   factors is positive and finite. No cancellation is possible for this
   single path. The companion component-mixture pole was independently
   derived in `CANONICAL_CHARGE.md`; this review does not count that
   self-authored companion as an independent review of itself.

6. **Finite Lean interface.** `survival` is literally the product
   `(1-C w*X)` and both public statements express the preceding polynomial
   computation. The ordinary theorem quantifies over all natural states,
   which is stronger than merely positive ordinary states and valid since
   `1/(3n+1)>0` also at zero. No Collatz orbit hypothesis or convergence
   statement is smuggled into either declaration. The independent audit
   file requests exactly these two declarations.

## Limits of this review

The path occupation input and the preexisting strict resolvent remain
source-qualified; their upstream proof histories were not repeated. The
brief literature discussion about alternative entropy classifications in
Section 5 was not used in the checked mathematics, and those external
classifications were not independently audited here. The result is the
sharper entire growth bound plus a precise failed final identification.
It is not a proof that the canonical escape coefficient vanishes.
