# Direct attempt to eliminate the canonical escape charge

Date: 2026-11-22. **Outcome: no vanishing of the canonical escape
coefficient was proved in this pass.** This is a record of a direct
arithmetic contraction attempt on the actual terminal measure. It is
not presented as another advance toward closure.

The target was the already identified positive coefficient

\[
b_\infty=\sum_{\mathcal C\ {\rm escaping}}
             \frac{D_{\mathcal C}^{\,2}}{C_{\mathcal C}},
\qquad D_{\mathcal C}=\sum_{n\in\mathcal C}d(n).
\]

All the statements below retain the source qualifications of the
ordinary harmonic construction. The arithmetic calculations are written
mathematics; no new Lean theorem is claimed.

## 1. Directly used current sources

| Source | Exact head | Material used |
|---|---|---|
| Own PR175 | 728389c2ad4796853948250a90188b0697483d92 | Exact boundary coefficient and canonical charge from LITERATURE_DIRICHLET_BOUNDARY.md. |
| PR185 | 53f01ca5b443ef57ef2160b4996dbb2cc87f7395 | CONTACT_RETURN_FINITE_REFERENCE.md and CONTACT_EXIT_ACCOUNTING.md in research/multiple-attacks-20261122/: contact comparison, original-source return map, terminal mass. |
| PR180 | ab3973099f0d285bbe88972382ad599bb02cd460 | ORDINARY_BOUNDARY.md and CONTACT_CLOCK.md in research/lean-joint-20261122/: actual first-contact laws, full-source limits, exact reset clock, and a short noncontact parent at every root. |
| PR176 | 31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6 | SPARSE_BOUNDARY_MASS.md and ALL_DEPTH_FIRST_CROSSING.md under research/lean-global-resolvent-20261121/overview/profound/: the actual crossing-source estimate with its arriving canonical weights retained. |

The entire strict-Green correction and finite contact reference were
examined for a possible missing contraction. The first preserves the
positive terminal sector; the second kills last-contact exits without
deciding their ordinary fate. Neither was substituted for the estimate
attempted here.

## 2. Work on the actual escaping terminal measure

Fix one hypothetical escaping ordinary component \(\mathcal C\). Let

\[
C=\lim_{j\to\infty}\nu(U^jp)>0,\qquad
D=\sum_{n\in\mathcal C}d(n)>0,\qquad F=D/C,
\]

where \(p\) is any member of the component. In this note \(C,D,F\)
refer to this one component, not to global sums.

Use the fixed contact section
\(\mathcal A=\{x:V(x)\le2\}\). Let \(\Lambda\) be the contacts in
\(\mathcal C\) with no strictly later forward contact. The pinned
ordinary first-contact theorem gives

\[
\eta(y)=\nu(y)\mathbf1_\Lambda(y),\qquad
\sum_y\eta(y)=C.
\tag{1}
\]

The actual inverse first-contact distribution from \(q\) is denoted
\(\mu_q\). For a last contact \(x\), its successor \(Ux\) is noncontact
and has no later contact, so the reset kernel is

\[
Q(x,y)=\mu_{Ux}(y),\qquad x,y\in\Lambda.
\tag{2}
\]

Its rows sum to one. The original contact-clock theorem proves that
repeated resets drift to decreasing integer clock; it does not make
\(\eta\) stationary.

## 3. Exact density after one reset

For a noncontact root \(q\) in this component, put

\[
\beta(q)=\frac1{\nu(q)}
       \sum_{\substack{x\in\mathcal A\\Ux=q}}\nu(x).
\tag{3}
\]

Every contact parent of a point with no future contacts is itself a
last contact. For a fixed \(y\in\Lambda\), let \(q_t=U^t y\).
A reset from \(x\) reaches \(y\) precisely when \(Ux=q_t\) for some
\(t\ge1\). The actual inverse path is unique and its mass is
\(\nu(y)/\nu(q_t)\). Since there is no intervening contact after \(y\),
it is a genuine first-contact path. Nonnegative summation therefore
gives the exact density

\[
(Q_*\eta)(y)=\nu(y)H(y),
\qquad
H(y)=\sum_{t\ge1}\beta(q_t).
\tag{4}
\]

In particular the incoming masses have not been replaced by fresh
reciprocal-height samples. Since \(Q\) is Markov and \(\eta\) is finite,

\[
\boxed{\sum_{y\in\Lambda}\nu(y)H(y)=C.}
\tag{5}
\]

The proposed closure was to prove a strictly smaller total by genuine
arithmetic estimates on the right-hand side of (4).

## 4. The arithmetic bounds obtained

On the contact set, the imported comparison is

\[
\frac{\gamma}{x}\le\nu(x)\le\frac2{\delta x},
\qquad \delta=e^{-200/3},\quad\gamma>0.
\tag{6}
\]

Every odd inverse parent is \(x=(2^e q-1)/3\). As
\(1/x\le6/(2^e q)\), summing all exponents, including illegal ones
only in this upper bound, yields

\[
\boxed{\beta(q)\le\frac{12}{\delta q\nu(q)}.}
\tag{7}
\]

There is also a strictly positive noncontact deficit at every root.
The explicit residue lift in CONTACT_CLOCK.md produces a parent
\(p\equiv17\pmod{54}\) with exact exponent at most 54,
\(p<2^{54}q/3\), and \(V(p)\ge9/4>2\). Hence, with
\(a=3\gamma/2^{54}>0\),

\[
\boxed{\beta(q)\le1-\frac{a}{q\nu(q)}.}
\tag{8}
\]

This strict inequality is an actual arithmetic statement. It does not
imply a strict bound after summing over all possible reset depths.

For \(t\ge2\), the spine parent \(q_{t-1}\) is noncontact. Therefore

\[
\beta(q_t)\le
\frac{\nu(q_t)-\nu(q_{t-1})}{\nu(q_t)}.
\tag{9}
\]

Using \((b-a)/b\le\log(b/a)\) for \(0<a\le b\), and keeping the
first-step deficit (8), gives

\[
\boxed{
H(y)\le
1-\frac{a}{q_1\nu(q_1)}
  +\log\frac{C}{\nu(q_1)}.}
\tag{10}
\]

Thus the unwanted accumulated term is the actual remaining
harmonic-capacity growth after the first step. It is not an independent
word count and cannot be removed by summing a one-step loss repeatedly.

The alternative reciprocal-path estimate also does not give the needed
strictness. If \(m_y=\min_{t\ge1}q_t\), then the retained orbit-count
bound gives

\[
\sum_{t\ge1}\frac1{q_t}\le200m_y^{-1/40},
\qquad
H(y)\le\frac{2400}{\delta\nu(y)}m_y^{-1/40}.
\tag{11}
\]

The displayed upper bound in (11) cannot even be made less than one
by increasing the contact height. Indeed (6) implies
\(1/(\delta\nu(y))\ge y/2\), while
\(m_y\le U(y)\le(3y+1)/2\le2y\). Its right-hand side is therefore
at least

\[
1200\,2^{-1/40}y^{39/40}>1.
\tag{12}
\]

This calculation rules out a purported strict contraction from this
particular arithmetic bound; it does not rule out a sharper bound.

Integrating (10) against the actual terminal measure and using (5)
gives only

\[
a\sum_{y\in\Lambda}
\frac{\nu(y)}{Uy\,\nu(Uy)}
\le
\sum_{y\in\Lambda}\nu(y)
       \log\frac{C}{\nu(Uy)}.
\tag{13}
\]

The left side is finite since \(q\nu(q)\ge\gamma\). The right side
can be an extended nonnegative sum. No available estimate reverses
this inequality or bounds the remaining capacity-growth term below the
first-step deficit. Even proving the right side finite would not supply
the required strict inequality.

## 5. Retaining the canonical charge does not introduce a new height weight

The attempt also tested whether the special canonical source \(d\),
rather than an arbitrary initial measure, changes the density in (4).
It does not.

For a fixed original source \(p\in\mathcal C\), its mass \(d(p)\)
after \(k\) forward steps is still \(d(p)\), at \(q_k=U^kp\).
After its last contact, the first-contact law at \(q_k\) is exactly
\(\eta\) restricted to the last-contact ancestors of \(q_k\), divided
by \(\nu(q_k)\). Those ancestor sets increase to \(\Lambda\), and
\(\nu(q_k)\to C\). Consequently the reset laws converge in total
variation to \(\eta/C\).

Summing over the unchanged original charges is legitimate because
\(\sum_{\mathcal C}d=D<\infty\). It gives the canonical limiting measure

\[
\lim_{k\to\infty}\Pi L^k(d\mathbf1_\mathcal C)
=\frac DC\,\eta=F\eta.
\tag{14}
\]

There is no factor \(1/U^kp\) or \(1/y\) newly attached to this
transported original mass. Such a factor would reset the source and
would no longer compute (14).

To match the energy coefficient itself, the component's finite measure
\(F^2\eta\) has total mass \(D^2/C\). Since the reset stays in the
same component, (4)–(5) give

\[
Q_*(F^2\eta)(y)=F^2\nu(y)H(y),
\qquad
\sum_y Q_*(F^2\eta)(y)=D^2/C.
\tag{15}
\]

Thus the canonical factor is constant throughout this component and
does not suppress the compensating terminal-contact influx. The exact
calculation leaves the positive boundary coefficient intact.

## 6. The uniform density floor and a direct optional-stopping test

A final attempt tested whether the stationary normalization supplies a
uniform positive payoff that forces contact within the available finite
mixing horizon. Its exact status matters.

The additional frozen source is PR180 at
bfba8feaefb3d0910456cdd92d2afcf9e8785b4d,
research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md, equations
(E2)--(E4). Write \(\mu=\chi^{-1}>0\). That source gives
\(D\ge\mu g\) almost everywhere and identifies the canonically defined
finite density \(D_j\) with the conditional average of \(D\) on
each residue cylinder modulo \(3^j\). Every unit cylinder lies entirely
in the unit set. Averaging therefore proves the actual pointwise bound

\[
\boxed{D_j(x)\ge\chi^{-1}
\quad\text{for every ternary unit }x\text{ and every }j\ge1.}
\tag{16}
\]

This assertion is not restricted to almost every ordinary integer.
It does not assert a pointwise ordinary limit for \(D_j\).

Use the actual critical inverse law \(K_G\), and let
\(\tau_M^0\) be first entrance into \(\{V\le M\}\). The
positive-horizon martingale in PR185's STOPPED_MIXING_INTERFACE.md is

\[
Z_k^{(t)}=\frac{D_{t-k}(X_k)}{G(X_k)},\qquad 0\le k\le t-1.
\]

For integers \(t\ge s+1\), stop at \(\tau_M^0\wedge s\).
On \(\{\tau_M^0\le s\}\), the remaining horizon is positive,
so (16) applies; also \(G(X_\tau)\le V(X_\tau)\le M\).
The exact bounded optional-stopping identity consequently gives

\[
\frac{D_t(q)}{G(q)}
\ge\frac1{\chi M}\Pr_q^G(\tau_M^0\le s),
\qquad
\boxed{\Pr_q^G(\tau_M^0\le s)
\le\chi M\,\frac{D_t(q)}{G(q)}.}
\tag{17}
\]

The direction is decisive: small finite-horizon density gives an
**upper bound on early entrance**, hence a lower bound on its tail.
It does not force quick entrance. The displayed calculation is fully
consistent with almost-sure entrance at an unbounded later time.

One also cannot combine a fixed contact atom's positive hitting
probability with a finite-horizon estimate whose predecessor-floor
hypothesis excludes that very atom. If a fixed last contact \(y\)
lies \(\ell\) inverse steps behind the tested root, its contact
probability becomes available at depth \(\ell\). At that depth
the true predecessor floor is at most \(y\). A moving floor
\(b>y\) has already failed. Before that depth the atom gives no
positive lower bound for the event in (17).

Thus the normalization does supply the uniform lower bound requested
in this test, but its valid optional-stopping consequence points toward
delayed entrance, and the attempted opposing finite-floor estimate
has incompatible hypotheses once the old source is included.

## 7. The first unsupported step and the result of this pass

The missing arithmetic step in this attempted proof is control of
\(\log(C/\nu(Uy))\), or of the finer contact-only increments in (4),
strong enough to outweigh the explicit first-step noncontact deficit
after integration with the unchanged canonical boundary measure.

The new all-depth first-crossing estimate controls coefficients at
distinct crossing integers. On the hypothetical escaping spine its
arrival factor \(G(n)\) is at least a fixed positive multiple of the
crossing height. Substituting that unweighted crossing estimate into
(10) or (13) would discard the same arriving mass that defines \(C\).
The finite contact reference does not control this later capacity
growth either: its killed last-contact exits are precisely the states
being retained in (1).

Accordingly, this pass did not prove a canonical-specific strict
inequality and did not improve the bound to \(o(1/N)\). Equations
(4), (7)–(13), (14)–(15), and (16)–(17) specify what was actually calculated and
where the direct charge-elimination attempt stopped. No generic
countermodel, new reformulation, or finite verification is offered as
a substitute for the missing vanishing proof.
