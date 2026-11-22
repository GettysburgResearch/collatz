# A canonical escape label linking the two analytic routes

**Status: independently reviewed written synthesis from the stated frozen
analytic inputs.** The review covers the new deductions; inherited inputs
retain their separate evidence level. This note joins
[the ordinary harmonic Green identities](HARMONIC_CAPTURE_BRIDGE.md) to
[polynomial-phase rigidity](INVARIANT_CORRELATION.md). Their exact
source-qualified analytic inputs remain in force. No regularity of the
new label is assumed as a theorem, and no new claim is included in the
Lean audit count.

The construction gives an explicit bounded invariant label which is
positive on every escaping component and zero on every eventually
periodic component. If this particular label admitted ordinary mean
approximation by polynomial-phase sums, escaping orbits would be excluded.
Nontrivial periodic cycles remain a separate obligation.

## 1. Ordinary harmonic data and escaping components

Use the accelerated odd map

\[
 U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

Let \(\mathcal N\) be the positive odd ternary units which are not
themselves periodic. It includes states that later enter a cycle; forward
transport is killed at its first periodic state. Retain the ordinary
functions and operator from the harmonic note:

\[
 (Lr)(q)=\sum_{n\in\mathcal N:U(n)=q}r(n),\quad
 h(q)=G(q)/q,\quad\lambda(q)=\frac{3q}{3q+1},\quad
 d(q)=(1-\lambda(q))h(q).
\]

The pinned inputs and the Green identity give

\[
 L\nu=\nu,\quad0<h\le\nu\le A<\infty,
 \qquad
 W(q)=\sum_{n\in\operatorname{Pred}(q)}d(n)
                 =\nu(q)-\lambda(q)h(q).
 \tag{1}
\]

Here \(\operatorname{Pred}(q)\) includes time zero and only this unit
domain. All these are actual ordinary point values.

Fix an escaping unit \(q\): its forward orbit never enters a periodic
state. Its ordinary unit component is

\[
 \mathcal C(q)=\{n\in\mathcal N:
       U^a(n)=U^b(q)\text{ for some }a,b\ge0\}.
\]

Every member escapes. Put \(q_k=U^k(q)\). These states are distinct,
so \(q_k\to\infty\) as ordinary integers. The predecessor sets increase
and exhaust the component:

\[
 \operatorname{Pred}(q_k)\subseteq\operatorname{Pred}(q_{k+1}),
 \qquad\bigcup_k\operatorname{Pred}(q_k)=\mathcal C(q).
 \tag{2}
\]

The harmonic equation includes the actual edge from \(q_k\) to
\(q_{k+1}\), so \(\nu(q_k)\le\nu(q_{k+1})\le A\). Therefore

\[
 C_{\mathcal C}=\lim_k\nu(q_k)\in(0,A],\qquad
 D_{\mathcal C}=\sum_{n\in\mathcal C}d(n)
               =\lim_k W(q_k)\in(0,C_{\mathcal C}].
 \tag{3}
\]

Positivity of \(D_{\mathcal C}\) follows already from \(d(q)>0\).
Finiteness follows from \(0\le W(q_k)\le\nu(q_k)\le A\).
Starting from another member of \(\mathcal C\) gives the same limits:
the forward orbits have a common future, and their tails are cofinal.

Let \(m_{\mathcal C}=\min\mathcal C\). This is the minimum of the
**whole unit component**, including all ancestors, not the minimum of a
later forward suffix. Each predecessor domain in (2) lies above it. The
pinned strengthened comparison therefore gives

\[
 h(q_k)\ge\delta_{m_{\mathcal C}}\nu(q_k),\qquad
 \delta_m=\exp\left(-\frac{200}{3}m^{-1/40}\right).
\]

Since \(\lambda(q_k)\to1\), (1)--(3) imply

\[
 \boxed{
 F_{\mathcal C}:=\frac{D_{\mathcal C}}{C_{\mathcal C}}
 =\lim_k\left(1-\frac{\lambda(q_k)h(q_k)}{\nu(q_k)}\right)
 \in(0,1-\delta_{m_{\mathcal C}}].}
 \tag{4}
\]

This is a canonical positive escape value built from the same ordinary
harmonic functions and immigration mass as the Green theorem. It is
constant on the ordinary component by construction.

## 2. Extension to every positive ordinary integer

On positive odd ternary units set \(F(q)=F_{\mathcal C(q)}\) when the
orbit escapes, and set \(F(q)=0\) when it eventually enters any periodic
orbit, including at time zero. Thus

\[
                      0\le F<1,\qquad F(Uq)=F(q).
\]

This is a mathematical definition, not a claim that deciding which case
holds is algorithmically available.

For any positive integer \(n\), let \(o(n)\) be its odd part and put

\[
 \rho(n)=
 \begin{cases}
 o(n),&3\nmid o(n),\\
 U(o(n)),&3\mid o(n).
 \end{cases}
 \qquad \widetilde F(n)=F(\rho(n)).
 \tag{5}
\]

In the second case, \(3o(n)+1\equiv1\pmod3\), so its odd part is a
ternary unit. Hence \(\rho(n)\) is the first odd ternary unit on the
actual shortcut orbit of \(n\). For an even source or an odd nonunit,
advancing one shortcut step leaves that first unit unchanged. For an odd
unit \(n\), the first unit after the step is \(U(n)\). Consequently

\[
 \boxed{\widetilde F(Tn)=\widetilde F(n)\quad(n\ge1).}
 \tag{6}
\]

This extension is zero on every eventually periodic ordinary orbit and
strictly positive on every escaping ordinary orbit. In particular
\(\widetilde F(1)=0\). For a deterministic map on positive integers,
a noneventually-periodic orbit is injective and tends to infinity; these
are exactly the escaping orbits meant here.

## 3. Polynomial rigidity for any bounded invariant label

There is no need to prove closure under discontinuous thresholding.
Let \(J:\mathbb N_{>0}\to\mathbb C\) be a bounded exact invariant
label. Suppose it takes two different values \(\alpha\ne\beta\).
Following actual iterates to odd ternary units gives representatives
\(a,b\) with \(J(a)=\alpha\), \(J(b)=\beta\).

The exact level indicators

\[
 A(n)=1_{J(n)=\alpha},\qquad B(n)=1_{J(n)=\beta}
\]

are invariant Boolean labels. All ordinary predecessors of \(a\) and
\(b\) have the corresponding values, so LOG supplies

\[
 \liminf_XL_X(A)\ge c_{\log}/a,\qquad
 \liminf_XL_X(B)\ge c_{\log}/b.
 \tag{7}
\]

Fix a finite polynomial-phase sum \(Q\), and use its compact environment
from `INVARIANT_CORRELATION.md`. Along a common subsequence of cutoffs,
the two ordinary empirical measures of \(A\) and \(B\) converge to
\(\delta_A H\) and \(\delta_B H\). The polynomial projection theorem
applies to both labels and to the continuous observables
\(|\alpha-Q|\), \(|\beta-Q|\). Pointwise,

\[
 |J-Q|\ge A|\alpha-Q|+B|\beta-Q|.
\]

Choose the original cutoff sequence to realize the lower logarithmic
error, and take the common further subsequence. By (7) and the triangle
inequality on the compact environment,

\[
 \begin{split}
 \liminf_XL_X|J-Q|
 &\ge\delta_A\int|\alpha-Q|\,dH
       +\delta_B\int|\beta-Q|\,dH\\
 &\ge|\alpha-\beta|\min(\delta_A,\delta_B)\\
 &\ge\boxed{|\alpha-\beta|
                   \min(c_{\log}/a,c_{\log}/b)>0.}
 \end{split}
 \tag{8}
\]

No mean for \(J\), its level indicators, or its squared modulus is
assumed. No polynomial approximation of the level indicators is assumed.
Only the already proved compact projection theorem for exact Boolean
labels is used.

Let \(\mathcal P\) again be the ordinary Besicovitch closure of finite
polynomial-phase sums. Partial summation and the triangle inequality
extend (8) to every bounded approximant in \(\mathcal P\). Therefore

\[
 \boxed{J\in\mathcal P\text{ and bounded exact invariance}
                         \ \Longrightarrow\ J\text{ is constant}.}
 \tag{9}
\]

The constant can be any complex value. The assertion is pointwise
constancy on all positive ordinary integers: two distinct actual values
would produce the positive gap (8).

## 4. Consequence for the canonical escape label

Apply (9) to the bounded label (5). Since \(\widetilde F(1)=0\),

\[
 \boxed{\widetilde F\in\mathcal P
       \quad\Longrightarrow\quad
       \widetilde F\equiv0
       \quad\Longrightarrow\quad
       \text{every positive ordinary orbit is eventually periodic}.}
 \tag{10}
\]

More quantitatively, if an escaping unit \(a\) existed, then
\(\widetilde F(a)=F_{\mathcal C(a)}>0\), and comparison with the
unit target 1 in (8) gives

\[
 \boxed{\liminf_XL_X|\widetilde F-Q|
       \ge \frac{c_{\log}}{a}F_{\mathcal C(a)}>0}
 \tag{11}
\]

for every fixed polynomial-phase sum \(Q\). The same positive bound
extends to its bounded Besicovitch closure.

This is a direct interface between the two positive lanes: the harmonic
construction specifies which bounded invariant function to approximate,
and polynomial rigidity states what such approximation would force.
The construction itself provides **no** proof of membership in
\(\mathcal P\), or of any ordinary mean approximation rate. The component
minimum bound in (4) is not uniform along a growing forward suffix: the
original component and all its ancestors remain present.

All eventually periodic components were assigned zero, including any
hypothetical nontrivial cycle. Therefore (10) excludes escapes only;
identifying every periodic cycle with the trivial cycle is still required
for full Collatz. Nothing in this synthesis changes that boundary or
upgrades the source-qualified analytic inputs to Lean theorems.
