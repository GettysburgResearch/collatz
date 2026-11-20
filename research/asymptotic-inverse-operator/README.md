# The strong limit of the canonical inverse operator

**PROPOSED, source-qualified.** This packet specializes established
weighted-shift theory to the ordinary inverse kernel in PR #145.
It does not prove that escaping Collatz orbits are absent.

For the positive harmonic trace $H$, let

$$m(x)=H(x)/x,\qquad
P(t,x)=\mathbf1_{Ux=t}\frac{(3/2^{v_2(3x+1)})H(x)}{H(t)}.$$

The operator acts on $\ell^2(m)$. Its adjoint is
$P^*f(x)=\frac{3x}{3x+1}f(Ux)$, and the positive contractions
$(P^*)^nP^n$ have a strong limit $A$.

Under the stated arithmetic inputs, the note computes $A$ explicitly.
It vanishes on periodic basins. Each synchronous level of an escaping
component contributes one rank-one block, and the block eigenvalues
approach one along the forward spine. Therefore

$$A\text{ compact}\iff A=0
\iff\text{every positive ordinary orbit is eventually periodic}.$$

This does not exclude a nontrivial positive cycle.
Compactness of $A$ is not established.

There is an exact limit on finite-time norm approaches. For every finite
time $n$ and finite physical cutoff $M$, with $Q_M$ the projection onto
states at most $M$,

$$\|P^n\|_{\rm ess}=\|P^n(I-Q_M)\|
=\|(I-Q_M)P^n\|=1.$$

These equalities hold even if all ordinary orbits reach 1. Thus those
finite-time norms cannot prove the missing compactness.
The ordinary harmonic trace and reciprocal summability are imported
from the frozen PR #145 packet; the operator deductions retain that
source qualification.

- [Full block computation, tail identities, inputs and prior theory](ASYMPTOTIC_OPERATOR.md).
- [Two exact rational shifts with opposite asymptotic limits](SHIFT_CONTROLS.md).
- [Standard-library exact replay](verify_operator_controls.py).
- [Investigation report](../../reports/2026-11-20-forward-closure/README.md).

The general rank-one block mechanism is credited to Gehér's work on
weighted shifts. The contribution here identifies the arithmetic
quantities and proves the explicit Collatz tail estimates.

Run from the repository root:

    python -X utf8 -B research/asymptotic-inverse-operator/verify_operator_controls.py
