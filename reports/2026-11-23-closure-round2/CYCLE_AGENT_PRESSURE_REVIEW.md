# Independent scoped review of the pressure-pole closing attempt

Date: 2026-11-23. Reviewer: cycle-cancellation research lane.

**Verdict: VERIFIED at the level of the written deductions and explicitly
retained dependencies below. Escape exclusion remains OPEN.** No Lean
verification of the infinite measure statements is claimed.

Reviewed source:
`research/closure-round2-20261123/ESCAPE_CLOSURE.md`, SHA-256
`607228e47b1370435747e1843c3ed7b572ffcf3ef834647c18a1ca98575c57bf`.
This review does not extend to later bytes. The reviewer did not author
this pressure note or supply its ordinary-measure identity. The reviewer
is the author of the separate cycle-cancellation files; this report is
not an independent review of those files.

## 1. Exact measures and the ordinary Riesz decomposition

At an ordinary root q, every legal inverse child n is positive, odd,
prime to three, and satisfies U(n)=q with its exact valuation exponent.
Conversely each n has just one ordinary parent root U(n). Therefore its
coefficient in sigma_s P_s is exactly

`U(n)^(-s) (3/2^a(n))^s = n^(-s) lambda(n)^s`.

Iterating gives the displayed atom density `Lambda_k(n)^s`; it decreases
between zero and one. For `sigma_s(f)<infinity`, this provides the stated
domination for passing to the limit in the finite telescope. Hence (7)
is the exact Riesz-type decomposition

`sigma_s(f) = sum_k d_s(P_s^k f) + mu_infinity,s(f)`.

The residual measure is not lost or replaced by Haar. The identity
`Lambda_infinity(n)=lambda(n)Lambda_infinity(U(n))` also proves its
invariance directly on atoms. Eventual cycles have product zero; the
positive product on escape is the explicitly pinned prior input. Since
the state set is countable, its partition into escaping components gives
the stated coefficient-one component sum.

## 2. Rational and countable pole integrability

For b prime to three, `|n-a/b|_3^(-beta)` equals
`3^(beta v_3(bn-a))`. The excluded ordinary pole condition ensures the
integer `bn-a` is nonzero. Its ordinary absolute value bounds its
3-primary part and is at most `(b+|a|)n`. This proves (8) when
`0<beta<s-1`, including the displayed dependence on both heights.
The restricted component version may admit a pole outside that component;
it does not establish the global sigma_s statement for such a pole.

For a countable family, the weighted condition
`sum_i c_i(|a_i|+b_i)^beta<infinity` really does imply both the pointwise
ordinary bound and the summable majorant in (10). The note does not infer
integrability of the sum merely from the individual terms. The same
condition implies `sum_i c_i<infinity`, as each height is at least one.
All changes of order have nonnegative summands.

## 3. Green function, including periodic roots

For a nonperiodic q, a fixed ancestor n can reach q at only one depth;
two hits would make q periodic. The exact path product is
`(q/n)^s Lambda(n,q)^s`, giving (13).

If q has least odd period r, a source's hits are precisely its first hit
followed by r-step laps. Each lap multiplies the path weight by
`c_q^s`, where `0<c_q<1`. The sum is therefore geometric with denominator
`1-c_q^s`, yielding (14) without classifying positive cycles. The known
fixed odd point q=1 has exactly this factor with `c_q=3/4`.

The loss-measure integral (12) follows directly from (7) and Tonelli.
It also independently implies pointwise finiteness at every ordinary
root because every such atom has strictly positive d_s mass.

For unit-Haar measure, shell masses are `1/2` at valuation zero and
`3^(-j)` at valuation j>=1. These give the stated `J_beta`; a nonunit
pole permitted by the denominator condition has integral one. Thus
(15) follows from `m P_s=rho(s)m` and the geometric time sum. Its
measure is explicitly different from the retained atomic measure.

## 4. Parameter window and the closing boundary

Near -1, `I_1(q)+1=2(q+1)/3`, so the pole contributes the factor
`3^(-beta)`. The inequalities
`s log_3(3/2)<beta<s-1` are simultaneously feasible exactly when
`s>log_2(3)`. Intersecting with `s<2` gives the claimed Haar-contracting
window. PR175 uses operator exponent `delta=1-p` in `(0,1)`, whose Haar
multiplier exceeds one; the new exponent is in `(1,2)`. Its mean
obstruction therefore does not transfer to the new window. Its
finite-pole propagation obstruction does transfer. For example,
`-1 -> -1/4 -> 1/8` gives a positive nonintegral propagated dyadic pole.

Finally invariance gives `mu_E(P_s^k f)=mu_E(f)>0`, so Tonelli forces
`mu_E(G_s f)=infinity`. The retained-source calculation in Section 6
reproduces that divergence before any interchange: the same positive
quantity survives at every distinct forward endpoint. Under d_s it
instead telescopes to the stated finite loss. These facts are compatible
with finite total mass and pointwise finite Green values. Neither loss
nor Haar budgets prove the required same-law collision upper bound.

## 5. Source inspection and limits

The following exact source texts were fetched and inspected for the
claims used here:

| Source | Frozen commit and Git blob | Checked role |
|---|---|---|
| PR177, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md` | Commit `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`; blob `314fce3965adf36775fac9b5f2097c0181e830de` | Ordinary operator, elementary positive-product input, Haar multiplier, atomic invariance, and same-source Green boundary. |
| PR175, `research/lean-global-closure-20261121/risk23/TERNARY_POLE_BARRIER_ATTEMPT.md` | Commit `8870528daa6a13cc941d602e578e35c8bfa4bf4f`; blob `629bd0f0d1b7993e90cfa6cb20a5e98facbd22ff` | Exact exponent range and Haar obstruction, finite-pole propagation, ordinary-only limitation. |
| PR185, `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md` | Commit `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`; blob `803d6ba2a3827c6ef94cb31fb838e3d416b92090` | The critical collision upper target concerns the specified ordinary inverse endpoint laws. This is not a full review of that separate paper. |

No mathematical correction to the reviewed pressure note is requested.
The positive-product input remains source-qualified, and the infinite
operator arguments remain written proofs. This review certifies neither
a new external-literature theorem nor escape or full Collatz closure.
