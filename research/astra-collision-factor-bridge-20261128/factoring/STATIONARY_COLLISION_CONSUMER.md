# A uniform stationary transfer of the entire collision law

Date: 2026-11-28. **Exact finite transfer and a sufficient stationary
two-copy estimate for the one-eighth question.** The final relative
small-cell estimate is not proved here.

The single-bin stationary replacement in
[CONDUCTOR_AND_STATIONARY_TRANSFER.md](CONDUCTOR_AND_STATIONARY_TRANSFER.md)
has a stronger consequence: all endpoint and grade bins can be transferred
at once, with no error proportional to the number of targets. This gives a
direct consumer for the finite collision energy and its critical-clock
limit. It also removes a sum over target labels from the two-copy observable.

## 1. The full empirical law is a shifted-window pushforward

Let \(T\) be the native shortcut map and let \(a_h(n)\) be the number of
odd branches among its first \(h\) steps. For an integer \(X\ge1\), define

\[
\mathsf P_{h,X}
=\frac1X\sum_{n=1}^X\delta_{(a_h(n),T^h(n))}.
\tag{1}
\]

For any real seed \(r\ge0\), let \(k=\lfloor r\rfloor\) and define

\[
\mathsf P^{(r)}_{h,X}
=\frac1X\sum_{n=k+1}^{k+X}\delta_{(a_h(n),T^h(n))}.
\tag{2}
\]

The unshifted and shifted source windows share at least
\(X-\min(k,X)\) integer points. Matching these points gives a coupling
before applying the deterministic map \(n\mapsto(a_h(n),T^h(n))\).
Consequently, with total variation defined as the supremum over events,

\[
\boxed{
\|\mathsf P^{(r)}_{h,X}-\mathsf P_{h,X}\|_{\rm TV}
\le\frac{\min(\lfloor r\rfloor,X)}X
\le\frac{\min(r,X)}X.}
\tag{3}
\]

Equivalently, the finite integer-window theorem can be applied to the one
membership indicator for the preimage of **any union of endpoint/grade
bins**. The same constant works for every such union. Summing separate
one-bin bounds is unnecessary and would lose this fact.

Let \((R_0,Z_0)\in[0,\infty)\times\mathbb Z_3\) be an independent joint
seed. On a word of grade \(a\), the final ternary coordinate is independent
of \(Z_0\) modulo \(3^a\), and its real coordinate shifts by
\(3^a2^{-h}R_0\). The full-conductor ordinary selector therefore produces
exactly the shifted source window in (2). After averaging the seed,

\[
\mathsf Q_{h,X}=\mathbb E\mathsf P^{(R_0)}_{h,X}
\]

is a probability measure and satisfies

\[
\boxed{
\|\mathsf Q_{h,X}-\mathsf P_{h,X}\|_{\rm TV}
\le d_X:=\frac{\mathbb E\min(R_0,X)}X.}
\tag{4}
\]

All statements are uniform in \(h\). The seed may be stationary or not;
its two coordinates must be driven by the same future word. The finite
word identities and positivity argument are proved in the linked notes.

## 2. Maximal atoms and collision energy transfer without a target loss

Let \(P_{h,X}\) and \(Q_{h,X}\) denote the endpoint marginals of (1) and
(4). Then

\[
\left|\sup_y P_{h,X}(y)-\sup_y Q_{h,X}(y)\right|\le d_X.
\tag{5}
\]

For a discrete probability measure \(\lambda\), write
\(\mathcal C(\lambda)=\sum_y\lambda(y)^2\). Two independent copies of
a coupling with mismatch probability at most \(d_X\) show that the event
of equal endpoints can change only when at least one copy mismatches.
Thus

\[
\boxed{
|\mathcal C(P_{h,X})-\mathcal C(Q_{h,X})|\le2d_X.}
\tag{6}
\]

For a stationary seed of odd-bit bias \(p<1/2\),
\(\mathbb ER_0=p/(1-2p)\). In particular \(p=1/8\) gives

\[
\|\mathsf Q_{h,X}-\mathsf P_{h,X}\|_{\rm TV}\le\frac1{6X},
\qquad
|\mathcal C(P_{h,X})-\mathcal C(Q_{h,X})|\le\frac1{3X}.
\tag{7}
\]

For the fair stationary seed, Section 6 of the companion note proves
\(\mathbb E\min(R_0,X)\le eC_0\log X\) for \(X\ge e^2\), with the
explicit absolute constant \(C_0\) given there. Hence

\[
|\mathcal C(P_{h,X})-\mathcal C(Q_{h,X})|
\le\frac{2eC_0\log X}{X}.
\tag{8}
\]

In particular the true finite collision energy and either stationary-seeded
version have the **same limit along every choice of clocks \(h=h(X)\)**,
whenever one of those limits exists. Their liminf and limsup also agree
without an existence assumption. This applies to the critical clock used
in the project's one-eighth criterion.

## 3. The exact stationary trace, with every grade weight retained

Take the seed to be stationary for odd-bit bias \(p\), and drive its future
with the same bias. Let \((R_h,Z_h)\) be its final joint state and \(A_h\)
the future grade. The marginal \((R_h,Z_h)\) is stationary; its correlation
with \(A_h\) remains part of the observable.

Write

\[
c_{h,a}=p^a(1-p)^{h-a},\quad q_a=3^a,\quad
L_a=q_a2^{-h}X,
\]

and

\[
H_y(R,Z,a)=
\mathbf1_{Z\equiv y\ (q_a)}
\mathbf1_{0<y-R\le L_a}.
\tag{9}
\]

The endpoint law in (4) is exactly

\[
\boxed{
Q_{h,X}(y)=\frac1X
\mathbb E_p\left[c_{h,A_h}^{-1}H_y(R_h,Z_h,A_h)\right].}
\tag{10}
\]

To verify this, condition on the future word. Its probability is
\(c_{h,a}\), which cancels the displayed reciprocal. The remaining sum is
the shifted-window count from Section 1. In particular, summing (10) over
all positive integers \(y\) gives 1 exactly; no asymptotic normalization is
being assumed.

For two independent stationary paths, use primes to denote the second
copy and put

\[
J_h=\sum_{y\ge1}
H_y(R_h,Z_h,A_h)H_y(R'_h,Z'_h,A'_h).
\tag{11}
\]

Tonelli and independence give the exact collision formula

\[
\boxed{
\mathcal C(Q_{h,X})=
\frac1{X^2}\mathbb E_p
\left[\frac{J_h}{c_{h,A_h}c_{h,A'_h}}\right].}
\tag{12}
\]

For \(p=1/8\), the two reciprocal grade factors are
\(8^h/7^{h-A_h}\) and \(8^h/7^{h-A'_h}\). Dropping them would change the
measure and would invalidate the transfer.

## 4. The target sum is one explicit arithmetic intersection

There is no need to enumerate all \(y\) in (11). Given the two grades
\(a,a'\), let \(r_a\) and \(r'_{a'}\) be the least nonnegative integer
representatives of \(Z_h\bmod3^a\) and \(Z'_h\bmod3^{a'}\).
The two congruences are compatible exactly when

\[
r_a\equiv r'_{a'}\pmod{3^{\min(a,a')}}.
\tag{13}
\]

If they are compatible, put \(q=3^{\max(a,a')}\) and let \(r\) be the
representative coming from the larger modulus. Also put

\[
\ell=\max(R_h,R'_h),\qquad
u=\min(R_h+L_a,R'_h+L_{a'}).
\tag{14}
\]

Both real coordinates are nonnegative. Consequently the positive endpoint
condition is automatic on \((\ell,u]\), and

\[
\boxed{
J_h=\max\left(0,
\left\lfloor\frac{u-r}{q}\right\rfloor
-\left\lfloor\frac{\ell-r}{q}\right\rfloor\right)}
\tag{15}
\]

when (13) holds; otherwise \(J_h=0\). Thus the two-copy observable needs
only the jointly selected real interval and two finite ternary residues.
The formulas also cover grade zero, where the modulus is 1.

If \(X\le2^h\), the intersection interval has length at most \(q\), so
\(J_h\in\{0,1\}\). A half-open interval of length exactly \(q\) still
contains at most one point of the residue class. This includes the entire
critical regime beyond the initial binary-information horizon.

## 5. A constant-weight fair stationary version of the one-eighth problem

For \(p=1/2\), all word probabilities equal \(2^{-h}\), so (12) becomes

\[
\mathcal C(Q_{h,X})=\frac{4^h}{X^2}\mathbb EJ_h.
\tag{16}
\]

When \(X\le2^h\), this is
\(4^hX^{-2}\Pr(J_h=1)\). Combining with (8),

\[
\boxed{
\left|\mathcal C(P_{h,X})-
\frac{4^h}{X^2}\Pr(J_h=1)\right|
\le\frac{2eC_0\log X}{X}.}
\tag{17}
\]

This is a uniform all-clock identity with an explicit vanishing error. For
the chosen critical clocks, a sufficient stationary estimate for the desired
lower bound is therefore

\[
\Pr(J_h=1)\ge
\left(\frac18-o(1)\right)\frac{X^2}{4^h}.
\tag{18}
\]

The exact clock match is the one in the prior source-qualified
[synchronous phase theorem](../../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md),
pinned at Collatz commit `504d29d399efa941a62006d1ea4635385ce6bb5f`:

\[
h_X=\left\lfloor\frac{2\log X}{\log(4/3)}\right\rfloor,
\qquad
h_X(u)=\frac{2\log X}{\log(4/3)}
+\sqrt{\frac{2(\log3)^2}{\log^3(4/3)}}\,u\sqrt{\log X}
+o(\sqrt{\log X}),
\tag{18a}
\]

with integer rounding and natural logarithms. Its statistic is exactly
\(\Pr(T^{h_X}n=T^{h_X}n')=\mathcal C(P_{h_X,X})\) for two independent
uniform ordinary starts. No Cesàro averaging, stopping-time substitution, or
conversion to an accelerated odd-only clock is needed. The prior theorem
imports the named Leen clock/minimum laws and positive-predecessor result;
those analytic developments are not rebuilt in this note.

At the median date, the requested probability in (18) has order
\(X^{\,2-4\log2/\log(4/3)}\), up to the bounded factor from rounding the
clock. The negative exponent has magnitude approximately \(7.6377\).
This makes the required **relative** precision concrete.

If the project's previously established upper bound \(1/8\) is supplied
at those clocks, (18) would give equality there. This note does not reprove
that upper bound or the separate theorem converting maximal critical
collision to full Collatz.

The required precision in (18) is **relative to the small probability**
\(X^2/4^h\). An absolute mixing error tending to zero is not sufficient.
The grades in (13)–(15) still belong to the same paths as the real and
ternary endpoints; they cannot be replaced by independent binomial draws.

As a normalization check, for one fair stationary path let
\(K_h=\sum_{y\ge1}H_y(R_h,Z_h,A_h)\). Equation (10) gives
\(\mathbb EK_h=X/2^h\). When \(X\le2^h\), \(K_h\) is an indicator, so

\[
\Pr(K_h=1)=X/2^h
\tag{19}
\]

**exactly**. The missing assertion is the endpoint coincidence law after
both rare selectors fire, not the one-copy normalization.

## 6. What is new in the consumer, and what remains unproved

The stationary replacement has no accumulation of errors over endpoint
labels, over grades, or over clock length. It transfers the entire empirical
law and hence the actual quadratic collision statistic. The two-copy label
sum reduces to the explicit compatible-residue interval test (13)–(15).
This is a concrete place for a new uniform stationary, primary, or weighted
arithmetic estimate to enter the full-proof route.

No inspected factoring result supplies the relative estimate (18).
The sparse determinant and weighted discrete-log numerator in the companion
note remain relevant, but neither an ordinary spectral gap nor a coarse
stationary marginal controls this same-path, shrinking full-cylinder event.

The finite integer-window inequality is certified by
[StationaryWindow.lean](StationaryWindow.lean), with the fresh three-root
[receipt](../../../reports/astra-collision-factor-bridge-20261128/factoring/stationary-window-lean-receipt.json).
The coupling, stationary construction, and two-copy analytic reduction here
are written proofs, not separately formalized probability theory.
