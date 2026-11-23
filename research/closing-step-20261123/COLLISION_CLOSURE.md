# Complete-carry entropy and squared-word collision transport

Date: 2026-11-23. Author: source-collision lane.

**Status: written arithmetic/probability theorems, with exact source and law
boundaries. The same-source escape contradiction and Collatz remain OPEN.**
This attack controls ambiguity in the actual ternary endpoint code by retaining
the complete carry. It proves an entropy-rate theorem for every stationary
integrable gap process, a weighted collision inequality for arbitrary actual
word laws, and an exact Renyi-2 exponent for the geometric equality branch
already isolated in PR180.

The natural geometric-2 model also admits a polynomial finite collision bound.
It is a distinct law: the mean-gap bound of an escaping ordinary stationary
limit is at most \(\ell=\log_2 3<2\). No geometric-2 model is substituted for
that actual limit or for a fixed ordinary-root conditional boundary.

## 1. Exact sources and chronological convention

| Frozen source | Use and retained boundary |
|---|---|
| PR180, `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 3--7 | Actual stationary backward-gap lift, finite-entropy bound, and maximum-Shannon iid equality branch. The existence of a stationary lift of an ordinary time limit is reused. |
| Same head, `research/profound-step-20261123/STATIONARY_REAL.md`, Sections 2--4 | Exact conditional drift and correction budget; the relation to the new carry budget is explained below. |
| PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md`, Sections 2--4 | Complete carry decoding and the exact quotient-channel injection. No bound on aggregation over source boxes is imported. |
| PR182, `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`, `research/literature-round4-20261123/ACTUAL_LAW_RIGIDITY.md`, Sections 3--8 | Finite ordinary periodic shadows, their source-height payment, and the explicit failure of local-statistics-only collision transfer. |
| PR178, `c91b80a3156e640ad471cf30c47721145ae21eb1`, `research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md`, Sections 4--6 | Quantitative same-source inverse/time-law comparison; its arithmetic collision term remains open. |

Let \(G_j\), \(j\in\mathbb Z\), be a stationary process of positive integer
gaps, with
\[
 b=\mathbb EG_0<\infty,\qquad
 \bar g=\mathbb E[G_0\mid\mathcal I],\qquad \ell=\log_2 3.
 \tag{1}
\]
Here \(\mathcal I\) is the invariant sigma-algebra. Independence, ergodicity,
bounded gaps, and reversibility are not assumed.

For a **chronological** length-\(m\) word \(w=(g_1,\ldots,g_m)\), put
\[
 a_i=\sum_{j=1}^i g_j,\quad a_0=0,\quad A=a_m,\quad Q=3^m,
 \qquad
 C(w)=\sum_{i=0}^{m-1}3^{m-1-i}2^{a_i},
 \qquad K(w)=\left\lfloor C(w)/Q\right\rfloor.
 \tag{2}
\]
Its endpoint code is
\[
 r_m(w)=2^{-A}C(w)\pmod{Q}.                              \tag{3}
\]
An actual ordinary segment from \(p\) to \(q\) has
\[
 2^Aq=3^m p+C(w),
\]
so (3) is literally \(q\bmod Q\).

Let \(P_m\) be the law of the chronological window
\((G_{-m+1},\ldots,G_0)\). The consistent endpoint laws define the ternary
series factor
\[
 Z_3=\sum_{i\ge1}3^{i-1}2^{-(G_0+G_{-1}+\cdots+G_{-i+1})}
      \ \in\mathbb Z_3^\times,\qquad \rho=\mathcal L(Z_3).
 \tag{4}
\]
Thus \((r_m)_*P_m=\rho\bmod3^m\). Stationarity says that the chronological
window has the same law as \((G_1,\ldots,G_m)\); this is the orientation
used when estimating the prefix sums below. It does not assert that a
process equals its time reversal.

Write
\[
 H_m=H(P_m),\quad h=\lim_{m\to\infty}H_m/m,\quad
 J_m=H(\rho\bmod3^m),\quad
 \mathcal C_m=\sum_{r\bmod3^m}\rho(r+3^m\mathbb Z_3)^2.
 \tag{5}
\]
Entropy uses natural logarithms. Finite mean gives \(H(G_0)<\infty\) by
comparison with a geometric law. Hence \(H_m\le mH(G_0)<\infty\);
subadditivity supplies the finite entropy rate \(h\).

## 2. The exact information lost by the endpoint code

The map
\[
 w\longmapsto\bigl(A(w),K(w),r_m(w)\bigr)                 \tag{6}
\]
is injective. Indeed \(A\) and \(r_m\) determine \(C\bmod3^m\), while \(K\)
determines its quotient, so they determine the complete \(C\). For \(m>1\),
\[
 C=3^{m-1}+2^{g_1}C(g_2,\ldots,g_m)
\]
has an odd remaining carry. Thus \(g_1=v_2(C-3^{m-1})\), and recursive
decoding determines the first \(m-1\) gaps. The specified total \(A\)
determines the last gap. For \(m=1\), the total already determines the word.

Consequently the chain rule gives the **exact** identity
\[
 \boxed{
 H_m-J_m=H(A_m,K_m\mid r_m)\le H(A_m)+H(K_m).}
 \tag{7}
\]
This is an identity for the actual word probability. Repeated occurrences
of the same word retain their combined probability. No uniform law on words
or ordinary sources is introduced.

Since \(\mathbb EA_m=mb\), the entropy bound for a nonnegative integer with
that mean gives
\[
 H(A_m)\le (mb+1)\log(mb+1)-mb\log(mb)\le\log(mb+1)+1.
 \tag{8}
\]

The carry entropy is controlled by its logarithm. For every \(t>1\), compare
its law with
\[
 q_t(k)=\frac{(k+1)^{-t}}{\zeta(t)},\qquad k\ge0,
 \quad \zeta(t)=\sum_{k\ge0}(k+1)^{-t}.
\]
The entropy/cross-entropy inequality gives
\[
 \boxed{H(K_m)\le t\,\mathbb E\log(K_m+1)+\log\zeta(t).}  \tag{9}
\]
All terms are finite by the next section. The series \(\zeta(t)\) here is
only a convergent positive reference distribution; no zeta-function
hypothesis is involved.

## 3. The carry ambiguity has exactly the positive drift budget

For the forward chronological block with the same distribution, set
\[
 D_j=G_j\log2-\log3,\qquad S_i=\sum_{j=1}^iD_j,\qquad
 M_m=\max_{0\le i<m}S_i.
\]
The initial term \(S_0=0\) is included. Formula (2) becomes
\[
 \frac{C}{3^m}=\frac13\sum_{i=0}^{m-1}e^{S_i}.
\]
Since \(C/3^m<K+1\le1+C/3^m\),
\[
 \boxed{
 M_m-\log3<\log(K_m+1)\le M_m+\log(m+1).}
 \tag{10}
\]

Birkhoff's theorem gives \(S_i/i\to d\) almost surely, where
\[
 d=\bar g\log2-\log3.
\]
The elementary maximum-of-partial-sums consequence is
\[
 M_m/m\longrightarrow d_+ \quad\text{almost surely}.     \tag{11}
\]
For each sample path this follows by separating finitely many initial
indices, then using \((d-\varepsilon)i\le S_i\le(d+\varepsilon)i\)
on the remaining indices.

The convergence also holds in \(L^1\). Here is the needed integrability
argument. The averages \(A_m/m\) are uniformly integrable: writing
\(G=G\mathbf1_{G\le L}+G\mathbf1_{G>L}\), their bounded part is at most
\(L\), while the remaining part has expectation
\(\mathbb E[G\mathbf1_{G>L}]\), uniformly in \(m\). For a threshold at
least \(2L\), the tail expectation of the full average is at most twice
this latter expectation. Let \(L\to\infty\).
Because
\[
 0\le M_m/m\le(\log2)A_m/m,
\]
the maxima are uniformly integrable too. This proves the \(L^1\)
assertion without assuming a second moment or independence.

It follows from (10) that
\[
 \boxed{
 \lim_{m\to\infty}\frac{\mathbb E\log(K_m+1)}m
 =\mathbb E[(\bar g\log2-\log3)_+]=:\mathfrak d.}
 \tag{12}
\]
This is the same positive conditional-drift budget that the previous real
stationary-series note identifies as \(\mathbb Eh(R_\infty)\). The
probability and the chronological/reflected conventions remain those
specified in (1)--(4).

**Theorem 1 (complete-carry entropy bound).**
For every stationary positive-gap process satisfying (1),
\[
 \boxed{
 \max(0,h-\mathfrak d)
 \le\liminf_m\frac{J_m}{m}
 \le\limsup_m\frac{J_m}{m}
 \le\min(h,\log3).}
 \tag{13}
\]
In particular, if \(\bar g\le\ell\) almost surely, then
\[
 \boxed{
 H(P_m)-H(\rho\bmod3^m)=o(m),\qquad
 \lim_m\frac{H(\rho\bmod3^m)}{m\log3}=\frac h{\log3}.}
 \tag{14}
\]

**Proof.** Combine (7)--(9) and (12), first for fixed \(t>1\), and then
let \(t\downarrow1\). The upper bounds follow because the endpoint is a
factor of the word and has at most \(3^m\) values. If \(\mathfrak d=0\),
(7)--(12) give the stated \(o(m)\) loss. \(\square\)

For an actual escaping-orbit stationary limit, the inherited bound is only
\(\mathbb EG_0\le\ell\). That global inequality does not imply
\(\bar g\le\ell\) on every invariant component. Formula (13) is valid
without that additional condition; formula (14) is valid on any invariant
restriction where the componentwise inequality holds. In particular it
applies to the conditionally critical branch from the preceding packet.

## 4. A weighted collision inequality retaining every carry channel

The Shannon argument alone does not control collision entropy. For that
purpose there is a different finite inequality.

**Lemma 2 (weighted injection).** Let \(I\) be a finite set of objects, with
box labels \(B(i)\), residue labels \(r(i)\), and nonnegative weights \(w_i\).
Assume \(i\mapsto(B(i),r(i))\) is injective. Give every box a positive penalty
\(L_B\). Then
\[
 \boxed{
 \sum_a\left(\sum_{i:r(i)=a}w_i\right)^2
 \le\left(\sum_B L_B^{-1}\right)
       \sum_i L_{B(i)}w_i^2.}
 \tag{15}
\]

**Proof.** For a fixed residue, apply weighted Cauchy:
\[
 \left(\sum_{i:r(i)=a}w_i\right)^2
 \le
 \left(\sum_{i:r(i)=a}L_{B(i)}^{-1}\right)
 \left(\sum_{i:r(i)=a}L_{B(i)}w_i^2\right).
\]
The injectivity hypothesis ensures that each box occurs at most once in
the first sum, which is therefore at most \(\sum_BL_B^{-1}\).
Sum the second factor over all residues. \(\square\)

The same assertion holds for countably many objects and boxes when the
displayed quantities are finite, by monotone convergence through finite
subsets. In particular it applies to all positive length-\(m\) gap words,
using the injection (6), without bounding the gap alphabet.

Let
\[
 Z_m=\sum_wP_m(w)^2>0,\qquad
 \widetilde P_m(w)=P_m(w)^2/Z_m.                         \tag{16}
\]
The probability \(\widetilde P_m\) is the **squared-word tilt** of the
supplied law. It is not asserted to be stationary as \(m\) varies.

For any positive penalties \(L_{a,k}\) with finite reciprocal sum,
\[
 \boxed{
 Z_m\le\mathcal C_m
 \le Z_m\left(\sum_{a,k\ge0}L_{a,k}^{-1}\right)
       \mathbb E_{\widetilde P_m}L_{A_m,K_m}.}
 \tag{17}
\]
The lower bound holds because grouping words into residues adds
nonnegative cross terms. The upper bound is (15).

For example, for \(s,t>1\),
\[
 \boxed{
 \mathcal C_m
 \le Z_m\,\zeta(s)\zeta(t)\,
 \mathbb E_{\widetilde P_m}(A_m+1)^s(K_m+1)^t.}
 \tag{18}
\]
All cross-channel collisions are retained in the weighted Cauchy estimate.
This is not a sum of the separate channel collision energies.

These formulas also hold for an empirical law of actual past words on
one finite ordinary orbit segment. Each repeated word has its full
empirical mass in \(P_m\), so its squared repeated-occurrence mass remains
in \(Z_m\). The endpoint law is the pushforward of the retained actual
windows. Any omitted initial endpoints or inverse-law remainder must
still be restored with their actual masses, as in the frozen source
consumer; they are not included in (17) by an unstated normalization.

## 5. Exact Renyi-2 exponent for geometric gaps of mean below two

Now assume the supplied stationary law really is iid geometric with mean
\(1<b<2\):
\[
 p_b(g)=b^{-1}(1-b^{-1})^{g-1},\qquad g\ge1.
\]
This assumption is legitimate for the maximum-Shannon equality branch in
PR180, where \(b=\ell\). It is not inferred merely from an approximate
finite collection of local block frequencies.

Direct summation gives
\[
 Z_m=(2b-1)^{-m},\qquad
 \widetilde P_m=\gamma_\beta^{\otimes m},\qquad
 \boxed{\beta=\frac{b^2}{2b-1}<\frac43.}                 \tag{19}
\]
Thus the collision-weighted gap process has a different mean from the
original process. This change of measure is exact, not a replacement
for the original endpoint law.

Under that tilt let \(Y=2^G/3\). For \(u>0\) with
\((1-\beta^{-1})2^u<1\),
\[
 \mathbb EY^u
 =\frac{(2/3)^u}{\beta-(\beta-1)2^u}=:\lambda(u).
 \tag{20}
\]
Since
\[
 \lambda(1)=\frac{2/3}{2-\beta}<1,
\]
there is a fixed \(u>1\) such that \(\lambda(u)<1\).
Independence and Minkowski's inequality give
\[
 \left\|C/3^m\right\|_{L^u(\widetilde P_m)}
 \le\frac13\sum_{i=0}^{m-1}\lambda(u)^{i/u}
 \le\frac1{3(1-\lambda(u)^{1/u})}.
 \tag{21}
\]
Consequently \(\sup_m\mathbb E_{\widetilde P_m}(K_m+1)^u<\infty\).
This is the uniform carry moment unavailable from a first-moment
stationary drift bound alone.

Choose \(1<t<u\), and use
\[
 L_{a,k}
 =\left(1+\frac{|a-m\beta|}{\sqrt m}\right)^2(k+1)^t.
 \tag{22}
\]
A decreasing-integral comparison on the two sides of \(m\beta\) gives
\[
 \sum_{a\ge0}
 \left(1+\frac{|a-m\beta|}{\sqrt m}\right)^{-2}
 \le2+2\sqrt m\le4\sqrt m.                              \tag{23}
\]
The sum over \(k\) is \(\zeta(t)\).

For every fixed finite \(v>0\), the iid geometric sum satisfies
\[
 \sup_m\mathbb E\left|
 \frac{A_m-m\beta}{\sqrt m}\right|^v<\infty.             \tag{24}
\]
An elementary justification is to choose an even integer \(2r\ge v\)
and expand the \(2r\)-th moment of the centered sum. Any term containing
an index exactly once has expectation zero by independence and centering.
All remaining terms involve at most \(r\) distinct indices, so the
moment is \(O_{\beta,r}(m^r)\). All required single-gap moments are finite.
The lower moments follow by the moment inequality.

Hölder, with exponents \(u/(u-t)\) and \(u/t\), combines (21) and
(24) to give
\[
 \sup_m\mathbb E_{\widetilde P_m}L_{A_m,K_m}<\infty.
\]
Equations (17), (19), and (23) prove:

**Theorem 3 (exact geometric collision rate).**
For each \(1<b<2\) there is \(C_b<\infty\) such that for all \(m\ge1\),
\[
 \boxed{
 (2b-1)^{-m}\le\mathcal C_m
 \le C_b\sqrt m\,(2b-1)^{-m}.}
 \tag{25}
\]
In particular,
\[
 \boxed{
 \lim_{m\to\infty}\frac{-\log\mathcal C_m}{m\log3}
 =\frac{\log(2b-1)}{\log3}.}
 \tag{26}
\]

At the actual maximum-Shannon equality value \(b=\ell\), Theorem 1 and
Theorem 3 identify **both** endpoint entropy rates:
\[
 \boxed{
 \lim_m\frac{H(\rho\bmod3^m)}{m\log3}
 =\frac{\Phi(\ell)}{\log3}=0.9499555\ldots,\qquad
 \lim_m\frac{-\log\mathcal C_m}{m\log3}
 =\frac{\log(2\ell-1)}{\log3}=0.7051555\ldots.}
 \tag{27}
\]
The exact formulas, rather than the displayed rounded decimals, define
the constants.

This is an upper collision bound for the **same** limit in that equality
branch, with its exact smaller exponent. It does not contradict the
previous strict collision lower bound and does not reach the larger
critical exponent \(\Phi(\ell)\). In fact (25) shows that reaching that
larger exponent on this branch would require excluding the branch by
additional ordinary-source information.

## 6. The geometric-2 endpoint has a polynomial full-dimension bound

For the natural iid law \(p_2(g)=2^{-g}\), (19) becomes
\[
 Z_m=3^{-m},\qquad \beta=4/3,\qquad \lambda(1)=1.
\]
There is no uniform first carry moment: the expected normalized carry
is exactly \(m/3\). Nevertheless a small moving moment yields a
polynomial bound, without importing a Fourier-mixing theorem.

For \(m\ge2\), choose
\[
 u=1+\frac1m,\quad t=1+\frac1{2m},\quad
 p=\frac{u}{u-t}=2m+2,\quad r=2p=4m+4.
 \tag{28}
\]
The tilted law is still iid geometric with mean \(4/3\). On
\(1\le u\le3/2\), formula (20) is smooth, positive, and satisfies
\(\lambda(1)=1\). A fixed constant \(c\) therefore gives
\[
 \lambda(u)\le e^{c(u-1)},\qquad
 \left\|K_m+1\right\|_u
 \le1+\frac13\sum_{i<m}\lambda(u)^{i/u}\le C m.
 \tag{29}
\]
The constants are independent of \(m\). For example, the logarithmic
derivative of \(3(2/3)^u/(4-2^u)\) is bounded on this closed interval.

For the same tilted total clock,
\(\mathbb E2^{A_m}=3^m\). The elementary bound
\(x^r\le(r/(e\log2))^r\,2^x\), \(x\ge0\), yields
\[
 \|A_m+1\|_r
 \le\frac r{e\log2}(2\cdot3^m)^{1/r}
 \le C' m.                                             \tag{30}
\]
Use the uncentered penalties
\(L_{a,k}=(a+1)^2(k+1)^t\).
Hölder with exponents \(p\) and \(u/t\) now gives
\[
 \mathbb E_{\widetilde P_m}(A_m+1)^2(K_m+1)^t
 \le\|A_m+1\|_{2p}^2\|K_m+1\|_u^t
 \le C''m^3,                                           \tag{31}
\]
since \(m^{1/(2m)}\) is uniformly bounded.
Also \(\zeta(t)\le1+(t-1)^{-1}\le3m\), and \(\zeta(2)\) is fixed.

**Theorem 4 (critical tilted-carry bound).**
For an absolute finite constant \(C\), all \(m\ge1\) satisfy
\[
 \boxed{
 3^{-m}\le\mathcal C_m\le C m^4\,3^{-m}.}
 \tag{32}
\]
The case \(m=1\) is absorbed by increasing \(C\). Thus this ternary
marginal has Renyi-2 dimension one. Its Shannon dimension is also one:
Theorem 1 gives the lower rate
\[
 2\log2-(2\log2-\log3)=\log3,
\]
and the finite alphabet gives the matching upper rate.

This says that the \(L^2\) norm squared of the depth-\(m\) density relative
to ternary Haar is at most \(Cm^4\). It does **not** give a bounded
\(L^2\) norm, absolute continuity, a Rajchman real marginal, or pointwise
regularity of the conditional real law at a specified ordinary ternary
root. A countable set of ordinary roots is Haar-null; a generic
disintegration assertion cannot select those fibres.

## 7. What happened to the direct fixed-source shadow attack

The new PR182 construction keeps the complete periodic shadow identity
\[
 2^{a_j}(\Delta q_j+b_j)=3^j(\Delta p+b_0),
 \qquad
 \Delta=3^d-2^{A_v}>0,
\]
so an actual segment following that template has the necessary payment
\[
 2^{a_T}\le\Delta p+b_0.                                \tag{33}
\]
For one fixed ordinary \(p\) and one fixed template, this forbids
arbitrarily long tracking. But residue collision does not identify a
repeated word, and repeated words at widely separated times do not
supply a long consecutive periodic segment. These two failed
inferences were checked against the explicit earlier same-source
nonidentical-word collision and the new periodic finite controls.

The present result avoids those inferences by decoding the **whole**
carry instead. The entropy identity (7) accounts for its complete
ambiguity, and (17) measures the exact extra collision cost under the
squared-word law. Neither asserts that every large collision forces
the periodic template in (33).

For the original finite empirical law, the quantity still needing
control is
\[
 Z_m\,\mathbb E_{\widetilde P_m}L_{A_m,K_m},
\]
with the actual repeated-word weights, plus the stated omitted mass.
For a general actual stationary limit, \(\widetilde P_m\) need not form
a stationary or independent family. The first-moment proof of (12)
under \(P_m\) does not transfer to that tilted family. The exact iid
branch is the case where the new tilt can be evaluated, leading to
(25)--(27).

Thus the attack has supplied an arithmetic entropy bridge and exact
iid collision exponents, but it has not obtained the critical
same-source upper estimate or excluded an escaping ordinary input.
No finite-source realization or generic geometric law is promoted
to that missing conclusion.

## 8. Primary literature inspected and use

The deductions above are self-contained apart from standard entropy,
ergodic, and probability inequalities. No historical novelty claim is
made for a general entropy method or a previously studied geometric
Syracuse law.

- M. Hochman, *On self-similar sets with overlaps and inverse theorems
  for entropy*, Annals of Mathematics 180 (2014), Theorem 2.7 and the
  self-similar setup:
  https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n2-p07-p.pdf .
  The inspected inverse theorem concerns a convolution of probability
  laws. A decomposition of actual endpoint labels into dependent
  summands does not supply that convolution. The proof here instead
  uses exact carry decoding and weighted Cauchy.

- S. Eberhard and P. P. Varju, *Mixing time of the
  Chung--Diaconis--Graham random process*, Theorem 1.1:
  https://arxiv.org/html/2003.08117v2 .
  Its innovations are iid and its sharp mixing conclusion covers
  almost all admissible moduli. It is not applied to the actual
  Collatz time process or automatically to the sparse sequence
  \(3^m\). The all-\(m\) estimates (25) and (32) above come from the
  supplied geometric law and the actual integer carry formula.

The formula for the geometric-2 marginal belongs to the Syracuse
random-variable framework. The present bound does not assert a new
uniform-mixing theorem for that framework, and no unreviewed recent
manuscript is a premise of (13)--(32).
