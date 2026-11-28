# The actual stationary selector can be negatively correlated with low grade

Date: 2026-11-28. **A finite exact counterexample to an all-scale
positive-association closure.** This uses the native Collatz map and the
genuine fair stationary real/ternary seed. It does not modify either law,
and does not refute the asymptotic lower bound in
[CRITICAL_GRADE_TAIL.md](CRITICAL_GRADE_TAIL.md).

The new one-copy sufficient estimate asks for a fair binomial lower tail
after conditioning on a rare ordinary selector. It is natural to try a
positive-correlation inequality between that selector and low odd grade.
Such an inequality is false at some actual median clocks. Only a more
specific asymptotic argument can remain viable.

## 1. Exact parameters and native count

Take

\[
X=100000,\qquad h=80=\left\lfloor\frac{2\log X}{\log(4/3)}\right\rfloor,
\qquad b=35=\lfloor h/2-\sqrt h/2\rfloor.
\tag{1}
\]

The clock identity follows from the two integer comparisons
\(4^{80}\le X^2 3^{80}\) and \(X^2 3^{81}<4^{81}\). The grade
identity is \(\lfloor40-\sqrt{20}\rfloor=35\), certified by
\(4^2<20\le5^2\).

Two exact integer replays give

\[
\#\{1\le n\le100000:a_{80}(n)\le35\}=12850.
\tag{2}
\]

The first iterates every source separately. The second propagates the
population of pairs `(native state, accumulated odd count)` and merges
identical pairs, preserving total multiplicity at each of the eighty
steps. They give the same count. This is a bounded computation; no claim
about all sources or all clocks follows from it.

## 2. The fair stationary transfer makes the sign rigorous

Let \(K=K_{80,100000}\) be the one-copy selector in (18) of the linked
critical-grade note. Under the fair stationary driving law,
\(\Pr(K=1)=X/2^h=:s\) exactly and
\(A_h\sim\operatorname{Bin}(h,1/2)\) without conditioning.

The full grade-and-endpoint stationary transfer gives

\[
\left|\Pr(A_h\le35\mid K=1)-\frac{12850}{100000}\right|
\le\frac{\mathbb E\min(R_0,X)}X
\le X^{-3/4}\mathbb ER_0^{3/4}.
\tag{3}
\]

The nonnegative affine-series estimate for the genuine fair stationary
seed gives

\[
\mathbb ER_0^{3/4}\le
\frac1{2^{7/4}-1-3^{3/4}}<\frac{25}2.
\tag{4}
\]

This bound can be checked without evaluating an irrational number:

\[
(84/25)^4<2^7,\qquad (57/25)^4>3^3,
\]

so the denominator in (4) exceeds
\(84/25-1-57/25=2/25\). Also \(5000^4<X^3\), hence
\(X^{3/4}>5000\). Equations (3)--(4) therefore imply the strict bound

\[
\Pr(A_h\le35\mid K=1)<0.1285+0.0025=0.131.
\tag{5}
\]

In contrast, the exact unconditional binomial probability is

\[
\Pr(A_h\le35)=
\frac{94993334918070245839239}{604462909807314587353088}
>0.157.
\tag{6}
\]

Combining (5)--(6) proves a strict negative covariance for the actual
stationary law:

\[
\boxed{
\operatorname{Cov}(\mathbf1_{K=1},\mathbf1_{A_h\le35})
<-0.026\,\Pr(K=1).}
\tag{7}
\]

Thus a universal inequality
\(\Pr(K=1,A_h\le b)\ge\Pr(K=1)\Pr(A_h\le b)\), even restricted to
the displayed genuine critical clock and its one-standard-deviation
lower-grade threshold, is false.

The lower-tail theorem concerns the limit as \(X\to\infty\) and
permits finite-cutoff error. Under full Collatz its relative covariance
would tend to zero. Equation (7) does not contradict that possible
limit, and does not obstruct an asymptotic positive lower estimate with
a vanishing error. It only rules out applying an all-scale association
theorem directly to these exact observables.

The last admitted lattice value at this finite cutoff is
\(W=-\sqrt5/2\), about \(-1.118\), even though it is selected by
flooring the threshold for \(z=1\). A comparison with a Gaussian at
finite \(h\) is sensitive to that lattice rounding and to continuity
corrections. The counterexample compares with the **exact finite
binomial law**, as an association claim requires; it is not evidence
against the Gaussian asymptotic target.

## 3. Reproduction and scope

Run

```sh
python -X utf8 -B research/astra-collision-factor-bridge-20261128/arithmetic/check_stationary_grade_anticorrelation.py --receipt reports/astra-collision-factor-bridge-20261128/arithmetic/stationary-grade-anticorrelation.json
```

The runner checks both counts, the exact clock and grade thresholds,
the rational fourth-power bounds, and the exact binomial fraction.
Every check remains active under `python -O`; there are no floating-point
comparisons. The source hash and completed receipt are retained. These
are finite arithmetic checks. The stationary coupling and fractional
moment arguments in (3)--(4) are written proofs from
[CONDUCTOR_AND_STATIONARY_TRANSFER.md](../factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md)
and [STATIONARY_COLLISION_CONSUMER.md](../factoring/STATIONARY_COLLISION_CONSUMER.md),
not new Lean probability formalizations.
