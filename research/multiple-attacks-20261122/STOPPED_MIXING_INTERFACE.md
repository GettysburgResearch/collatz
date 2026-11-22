# The exact stopped mixing estimate needed at contact returns

**Status:** proposed global interface, with a proved Haar maximal estimate
and an exact remaining change-of-measure obstruction. The stopped trace
estimate below is **OPEN** and is not an input to the proved contact
contraction. No Collatz closure is inferred from it.

## 1. Law, stopping times, and normalized payoff

Keep the nonperiodic positive odd-unit domain and all source qualifications
in `CONTACT_RETURN_FINITE_REFERENCE.md`. Fix \(M>1\) and let
\(C_M=\{V\le M\}\). The critical harmonic inverse law has kernel

\[
\mathcal K_G(q,x)=\mathbf1_{U(x)=q}\frac{\omega(q,x)G(x)}{G(q)},
\qquad \omega(q,x)=3/2^{v_2(3x+1)}.
\tag{1}
\]

Use its actual path \(X_0=q,X_1,\ldots\), and define

\[
\tau_M^0=\inf\{k\ge0:X_k\in C_M\},\qquad
\tau_M^+=\inf\{k\ge1:X_k\in C_M\}.
\tag{2}
\]

Both are almost surely finite by the pinned entrance theorem and the
Markov property. The ordinary harmonic law \(\mathcal K_\nu\) is
equivalent on the same complete physical paths; its Radon--Nikodym
derivative is between \(\delta\) and \(\delta^{-1}\). Thus an estimate
for any nonnegative stopped payoff transfers between these two actual
laws with a fixed factor. Neither is replaced by independent geometric
valuation letters.

Let \(D_t=P^t1\), \(t\ge1\). For any actual first-contact word from
\(q\) to \(x\), the critical probability is
\(\omega_wG(x)/G(q)\). Consequently the exact stopped residue error is

\[
\frac1{G(q)}\sum_{w\in\mathcal H_M(q)}
\omega_w|D_t(x_w)-D_m(x_w)|
=\mathbb E_q^G\!\left[
\frac{|D_t(X_\tau)-D_m(X_\tau)|}{G(X_\tau)}\right].
\tag{3}
\]

Choose \(\mathcal H_M\) and \(\tau\) consistently as first entrance
or strict first return. The source words and their actual endpoints stay
inside the sum.

The denominator in (3) is essential. At contact endpoints,
\(|D_t-D_m|/x\le4M/x\), but normalizing by the harmonic flow changes
this to \(|D_t-D_m|/(x\nu(x))\), which is comparable to the payoff in
(3). Since \(\gamma\le x\nu(x)\le M/\delta\), the small reciprocal
height has disappeared. An endpoint bound of order \(1/x\) cannot be
substituted for a small normalized Doob error.

## 2. A maximal version that would pay adaptive endpoint errors

The finite densities extend canonically as cylinder functions on
\(\mathbb Z_3\). For \(m\ge1\), define the bounded measurable function

\[
F_{m,M}(z)=\min\left(4M,
\sup_{t\ge m}|D_t(z)-D_m(z)|\right).
\tag{4}
\]

At every ordinary \(x\in C_M\), the source bound \(D_t(x)\le2V(x)\)
shows that clipping does nothing. Let \(\alpha>0\) be fixed and small,
and put

\[
m(q)=\max(1,\lfloor\alpha\log(2+q)\rfloor).
\]

Here is one precise next estimate, stated separately from the proved work.

**OPEN stopped return estimate.** For every \(A>1\), fixed \(M>1\),
and fixed \(\alpha>0\) in a specified admissible range, there exist
\(C_{A,M,\alpha}<\infty\) and \(Q_{A,M,\alpha}\) such that every
ordinary \(q\in C_M\) with \(q\ge Q_{A,M,\alpha}\) satisfies

\[
\boxed{
\mathbb E_q^G\!\left[
\frac{F_{m(q),M}(X_{\tau_M^+})}{G(X_{\tau_M^+})}\right]
\le C_{A,M,\alpha}\,m(q)^{-A}.
}\tag{SM+}
\]

All constants must be independent of the root, the realized return
duration, and every precision \(t\ge m(q)\). The supremum in (4)
allows the fine precision to be chosen adaptively; a claim only for one
fixed \(t\) does not automatically provide that version.

If (SM+) were proved, the strong Markov property and the contact-height
theorem would pay the sum of these normalized errors over all returns.
Indeed, writing \(Y_j=X_{\tau_j}\) for successive inverse contacts,
\(Y_j\ge(\delta\gamma/M)\rho^{-j}Y_0\). The proved deterministic
bound \(\sum_j\log(2+Y_j)^{-A}<\infty\), uniform in the realized
chain, then bounds the sum of conditional expectations in (SM+).
Finitely many low-height exceptions have uniformly bounded payoff
\(4M/\gamma\). Nonnegative summation gives a finite expected total
endpoint error, and hence an almost surely finite total error. No
ordinary excursion duration is charged in this conditional deduction.

## 3. The actual-law optional-stopping identity

There is a useful optional-stopping argument on the correct inverse law.
For a fixed finite horizon \(t\), the process

\[
Z_k^{(t)}=\frac{D_{t-k}(X_k)}{G(X_k)},\qquad 0\le k\le t-1,
\tag{5}
\]

is a martingale under (1) through these positive remaining horizons.
Its conditional expectation applies \(P\) to \(D_j\) with \(j\ge1\),
which vanishes at nonunit parents. The Doob kernel therefore retains
exactly the contributing terms. This argument does not include the last
step to \(D_0=1\), whose nonunit terms need not vanish. The imported
bounds \(D_j\le2V\le4\chi G\) for \(j\ge1\) place all displayed
values in \([0,4\chi]\). Here the exact input for \(\chi\) is
PR185 `7889fc680f5ee22237732eccc172b1699ef565da`,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
Section 3, equations (20)--(21), SHA256
`34340b2dafc1b37cf07ab2a401cccf2f7481af8dc6265ba521e4cce4a154454b`.
It retains that source's every-ordinary-point comparison with PR180's
normalization \(\chi=(\operatorname{ess\,inf}D)^{-1}\).

Take either stopping time in (2), integers \(t\ge s\ge m\ge1\),
and stop the two martingales at \(\tau\wedge(s-m)\). On
\(\tau\le s-m\), both remaining density horizons are at least \(m\),
and their difference is bounded by twice (4). On the complement, both
normalized values lie in \([0,4\chi]\). Consequently

\[
\boxed{
\frac{|D_t(q)-D_s(q)|}{G(q)}
\le2\,\mathbb E_q^G\!\left[
\frac{F_{m,M}(X_\tau)}{G(X_\tau)}\right]
+4\chi\,\Pr_q^G(\tau>s-m).
}\tag{6}
\]

This comparison removes the full-prefix counting factor and exhibits
the exact remaining ordinary-time tail. For each fixed root that tail
vanishes as \(s\to\infty\). It need not vanish uniformly when the
root and the allowed clock move together. Thus (SM+) would pay the first
term; it would not discard the second term at the polylogarithmic
clocks needed by the finite-certificate argument.

## 4. The maximal estimate that really follows from marginal mixing

Let \(\mu\) be Haar probability on \(\mathbb Z_3\). The exact density
consistency makes \(D_t\) a nonnegative martingale in the ternary
cylinder filtration. Tao's marginal estimate, in the repository's
normalization, is

\[
\|D_t-D_m\|_{L^1(\mu)}\le C_Bm^{-B}\qquad(t\ge m).
\tag{7}
\]

It gives an \(L^1\) limit \(D_\infty\), with the same bound against
\(D_m\). Doob's weak \((1,1)\) inequality applied to the martingale
\(D_t-D_m=\mathbb E[D_\infty-D_m\mid\mathcal F_t]\) yields

\[
\mu\!\left\{\sup_{t\ge m}|D_t-D_m|>u\right\}
\le\min(1,C_Bm^{-B}/u).
\tag{8}
\]

Writing \(\epsilon=C_Bm^{-B}\), integration of this tail up to \(4M\)
gives, when \(\epsilon\le4M\),

\[
\|F_{m,M}\|_{L^1(\mu)}
\le\epsilon\bigl(1+\log(4M/\epsilon)\bigr).
\tag{9}
\]

Choose a larger fixed \(B\) than the desired exponent. Thus for every
fixed \(A>0\),

\[
\boxed{\|F_{m,M}\|_{L^1(\mu)}\le C_{A,M}m^{-A}.}
\tag{10}
\]

This is a genuine maximal improvement of the marginal input, but its
measure is still Haar. Formula (10) is not (SM+).

The primary input is Tao, *Almost all orbits of the Collatz map attain
almost bounded values*, Proposition 1.14, consistency (1.23), and
(1.26)--(1.27), in the [corrected author version v7](https://arxiv.org/html/1909.03562v7).
His first-passage Proposition 1.11 uses logarithmically distributed
starting integers; it is not a statement for the stopped ordinary
harmonic inverse law in (1).

## 5. Why generic optional stopping does not transfer (10)

The law of \(X_{\tau_M^+}\) is a probability on actual positive
integers, so it is countably atomic when embedded in \(\mathbb Z_3\).
Haar gives that countable set mass zero. An individual retained source
atom of mass \(p>0\) at \(x\) belongs to a residue cylinder of Haar
mass \(3^{-t}\) at every precision \(t\). The density of the stopped
law on that cylinder is therefore at least \(p3^t\).

Consequently no uniformly bounded density relative to all finite Haar
quotients, and no precision-independent \(L^1(\mu)\) trace operator,
can justify (SM+) for arbitrary test functions. The special maximal
error \(F_{m,M}\) may obey a stronger correlation estimate, but that
requires a new arithmetic argument. The actual inverse path filtration
also differs from the ternary precision filtration used in (8). Optional
stopping cannot change either the probability law or the filtration for
free.

## 6. Initial entrance and the terminal boundary

Starting from an arbitrary marked root \(q\notin C_M\) requires its
own first-entrance estimate. A direct analogue would be (SM+) with
\(\tau_M^0\) and every such ordinary root in place of the contact-root
quantifier; if only least-component roots or roots with an inverse-basin
floor are covered, that restriction must be explicit. Contact return
contraction begins only after this entrance and supplies no bound on its
duration or on its residue correlation.

Even a successful endpoint error estimate must be used inside a complete
source-preserving telescoping argument. It does not itself remove the
last-contact source measure \(\eta\). PR176 shows that an escaping
component would give a nonzero finite \(\eta\), while its moving-root
first-entrance laws converge in total variation to the fixed atomic law
\(\eta/C\). Its original sources have no subsequent forward contact,
so no estimate involving only strict contact returns charges their final
escaping excursions.

The next arithmetic target is therefore the stopped correlation in
(SM+), together with its correctly scoped initial entrance and an
explicit way to control the terminal \(\eta\) sector. The Haar maximal
bound (10) and the contact logarithmic budget identify exactly which
parts are paid; they do not supply those remaining statements.
