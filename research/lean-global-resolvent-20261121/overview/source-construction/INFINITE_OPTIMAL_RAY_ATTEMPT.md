# The infinite optimal-ray attack: fixed-source approximation and its exact tail

Date: 23 November 2026. **Attempted closure; no escape exclusion obtained.**

This continuation attacks the actual infinite pressure-optimal ray, rather
than trying again to deduce balanced finite words. Its positive content is
an exact calculation of the simultaneous-approximation product for one
fixed ordinary source and one fixed real limit. The calculation supplies no
strict Diophantine saving. No Lean wrapper or new global theorem is claimed.

## 1. Keep the two maximizing domains separate

Write `U(n)=(3n+1)/2^a(n)` on positive odd integers. For an escaping
eventual-meeting component, the supplied product construction gives

\[
\Lambda(n)=\prod_{j\ge0}\frac{3U^j(n)}{3U^j(n)+1}>0,
\qquad r(n)=\Lambda(n)/n,
\qquad 2^{a(n)}r(n)=3r(Un).
\tag{1}
\]

PR182 selects a least maximum over the **unit** component. Fresh PR180
instead selects a least maximum over **all positive odd** component members.
Call these `m_unit` and `m_all`; they need not coincide. The enlarged
maximum has residue 3 or 7 modulo 12, and the first case is a ternary leaf.
The harmonic two-sided path law in PR180's `BOUNDARY_DESCENT.md` remains on
the unit component. Its positive minimum atom at the unit maximum cannot
be assigned to an enlarged maximum that is a ternary leaf: a positive odd
multiple of three has no odd predecessors, and hence cannot carry positive
mass in that two-sided harmonic flow.

The following arithmetic discussion works with either domain, provided its
competitors retain the chosen domain. In the enlarged domain, every actual
odd source is an admissible competitor. Put `m=m_all` there.

At the selected root all nonempty forward prefixes have `2^A<3^k`. At
every subsequent target, the original path maximizes the coefficient among
every actual incoming path. These are the inherited pressure identities;
we do not count their restatement as a new closing result.

## 2. The coherent scale has a fixed real correction series

Fix any one escaping positive odd source `m`, not necessarily a maximizer.
Let `q_j=U^j(m)`, `a_j=v2(3q_j+1)`, `A_0=0`, and
`A_k=sum_(j<k) a_j`. Define

\[
\gamma_k=3^k/2^{A_k},\qquad
C_k=\sum_{j<k}3^{k-1-j}2^{A_j},\qquad
S_k=C_k/3^k=\sum_{j<k}\frac{2^{A_j}}{3^{j+1}}.
\tag{2}
\]

The actual finite identity is

\[
2^{A_k}q_k=3^k m+C_k,
\qquad q_k/\gamma_k=m+S_k.
\tag{3}
\]

The finite correction product satisfies
`Lambda_k(m)=gamma_k*m/q_k`, so its supplied positive limit gives

\[
S_k\uparrow S(m):=\frac{m}{\Lambda(m)}-m<\infty,
\qquad h(m):=1/r(m)=m+S(m).
\tag{4}
\]

Every gap is at least one. Therefore `A_j>=j`, and termwise comparison
with the geometric series gives

\[
S(m)\ge\sum_{j\ge0}\frac{2^j}{3^{j+1}}=1.
\tag{5}
\]

The same holds for every escaping tail `q_k`. Splitting the unchanged
series at the actual odd clock `k` gives the **exact** tail identity

\[
\boxed{S(m)-S_k=\frac{2^{A_k}}{3^k}S(q_k).}
\tag{6}
\]

In particular the real remainder is not a freely improvable error term.
It contains the whole later correction with a lower bound of one after
normalization. Also `S_k -> -m` in the 2-adic topology: by (3), its error
is `2^A_k*q_k/3^k`, whose binary valuation is exactly `A_k` because `q_k`
is odd. Here `A_k>=k` tends to infinity. No irrationality or algebraicity
of the real value `S(m)` has been established.

The pressure optimum makes `h(m)` the smallest coherent scale in its
chosen ordinary component. It does not change (6).

## 3. The fixed-form Subspace-Theorem test has product at least one

This was a deliberate attempt to remove the moving-coefficient problem
of the earlier inverse-cylinder argument. The source `m` and the real
number `S=S(m)` are now fixed while `k` grows. At the primitive integer
vector `(X,Y)=(3^k,C_k)`, test the pairs of linear forms

\[
\begin{array}{c|c}
\text{place}&\text{forms}\\ \hline
\infty&(X,\ SX-Y)\\
2&(X,\ mX+Y)\\
3&(X,\ Y).
\end{array}
\tag{7}
\]

For `k>=1`, the last term of `C_k` is `2^A_(k-1)`, so `3` does not
divide `C_k` and the vector is primitive. Equations (3) and (6) give

\[
|X(SX-Y)|_\infty=3^k2^{A_k}S(q_k),
\]
\[
|X(mX+Y)|_2=2^{-A_k},
\qquad |XY|_3=3^{-k}.
\]

Consequently the complete, unnormalized product is

\[
\boxed{
|X(SX-Y)|_\infty\,|X(mX+Y)|_2\,|XY|_3
=S(q_k)\ge1.}
\tag{8}
\]

The primary theorem inspected is Evertse's presentation of the p-adic
Subspace Theorem, Theorem 1.1 and its two-dimensional application on
pages 2--3. With two forms in two variables, a strict negative power of
height is required. Also the forms must have algebraic coefficients.
Our real coefficient has not been proved algebraic; even granting that
additional premise would not make (8) satisfy the strict saving.

Thus this particular fixed-source route stops at an exact identity, not
at an unestimated logarithmic loss. Increasing the approximation clock,
using the root's maximum property, or substituting an orbit-count bound
does not remove the positive tail factor in (8). A different approximation
would have to cancel information from that tail while retaining the same
ordinary source and complete binary congruence.

The earlier checkpoint-14 inverse-cylinder product is explicitly credited:
it equals an ordinary endpoint at least one, and moving forward roots
also change its forms. Equation (8) is the forward, fixed-source test
using the convergent real correction; it is not evidence of a new global
Diophantine obstruction theorem.

## 4. Negative-cycle optimization has a precise moving-anchor issue

A second attempt uses the negative rational cycle supplied by each actual
supercritical prefix. When `2^A_k<3^k`, put

\[
\xi_k=-\frac{C_k}{3^k-2^{A_k}}<0.
\tag{9}
\]

This is the fixed point of the affine word of that prefix. Its denominator
is prime to three, and its ternary residue agrees with the actual endpoint:

\[
\boxed{q_k\equiv\xi_k\pmod{3^k}.}
\tag{10}
\]

Indeed both are congruent to `C_k*2^(-A_k)` modulo `3^k`. The given word
also has exact rational branch legality: every cyclic phase is a negative
odd carry divided by the same positive odd denominator, so the next phase
is 2-adically odd and each displayed division exponent is exact. It
therefore provides a concrete rational negative anchor for a depth-`k`
inverse comparison. Moreover `gamma_k -> infinity` on the escaping orbit,
so `xi_k -> -S(m)` in the real topology. This is a useful exact connection
between the pressure ray and negative rational cycles, but the anchor
itself generally changes with `k`.

The primary research note *Bounded terminal words and eventual exact minima
in Collatz inverse trees* proves a finite terminal description for targets
approaching **one fixed** negative rational cycle through a specified
original ternary depth. Its constants depend on that anchor's denominator,
period and cycle numerators; inverse depth beyond the supplied depth is
excluded from its correspondence. Its statement and setup were inspected;
no independent reconstruction of its complete proof is claimed here.

Applied to (9), those parameters can vary with `k`. Real convergence of
the anchors does not bound their denominators or periods. No uniform
estimate was obtained that places the actual depth `k` beyond the theorem's
anchor-dependent onset. Nor does a depth-`k` optimization automatically
give a legal longer inverse path from the same ordinary endpoint. These
are the first unsupported steps in that attempted application.

## 5. What an actual pressure-improving repair must supply

At target `q_k`, a competing actual word with odd length `l`, total gap
`B`, complete carry `D`, and positive odd source `n` must satisfy

\[
2^Bq_k=3^l n+D.
\tag{11}
\]

It defeats the selected maximum only if

\[
3^l2^{A_k}>3^k2^B.
\tag{12}
\]

For equality of coefficients, unique factorization forces `l=k,B=A_k`;
leastness of the maximizing source then requires `n>=m`. A larger
congruent carry producing `0<n<m` would defeat that tie. Fresh PR180's
same-clock repair theorem shows that a nontrivial repair starting after
`i` odd steps must span a window of length `L` satisfying
`2^(i+L)<3^(L-1)`. It constructs no such window.

There is also a bounded-source requirement hidden by coefficient-only
search: any strictly better ancestor has
`h(n)=1/r(n)<h(m)`, and (5) gives `n+1<=h(n)`. Hence

\[
\boxed{n<h(m)-1.}
\tag{13}
\]

The original component's floor and product estimate bound `h(m)` in
terms of that floor. Arbitrarily large congruence solutions therefore
cannot defeat the optimum merely by existing. Appending the same actual
suffix to two already coalesced paths also preserves their coefficient
ratio exactly; it cannot turn a previously losing candidate into a gain.

I did not construct a path meeting (11)--(12), or a positive smaller
source in the equal-coefficient case, for every infinite optimal ray.
The fixed-source adelic product and the changing negative-cycle anchors
do not supply it. Nontrivial positive cycles are outside the escaping
product premise throughout this note.

## Evidence and sources

The exact source versions and hashes are in `SOURCES.json`. The small
companion program checks only finite identities: affine carries, the
exact binary valuation, the shifted tail identity, the product in (8)
with a finite later tail, and the rational anchor congruence. It uses
ordinary known finite orbit segments. It does not manufacture an escaping
orbit, verify the infinite product input, or claim a universal comparison.

Primary sources inspected:

- J.-H. Evertse, *The p-adic Subspace Theorem* (May 2011), Theorem 1.1
  and the two-variable application: <https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf>.
- Lyapunov Weaver, *Bounded terminal words and eventual exact minima in
  Collatz inverse trees*, v1, 6 November 2026, Theorem 1 and its setup:
  <https://rstation.ai/problems/collatz/papers/108>.

Full Collatz, infinite-ray exclusion, and the pressure-improving repair
remain open in this attack.
