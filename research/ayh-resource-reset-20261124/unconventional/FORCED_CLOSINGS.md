# Polynomial reduced denominators forced by two local words

**Status.** Proposed written theorem. Its inputs are the two-variable fixed-place theorem in [PRECISION.md](PRECISION.md) and finite shortcut-word arithmetic. The latter has a Lean companion.

Let \(q\) be an ordinary positive odd state on a trajectory. Close its actual preceding \(b\ge1\) odd gaps by periodic repetition of that finite word. Let \(\zeta_-\) be the rational fixed phase of this past block at the boundary \(q\). Independently, close its actual following \(h\ge1\) shortcut bits by periodic repetition, with rational fixed phase \(\zeta_+\) at the same boundary. Both fixed points are unique. Write \(d_\pm\) for their positive reduced denominators.

Put \(\rho=\log_3 2\). For \(0<\theta\le1\), take \(b=\lfloor\theta\log_3 q\rfloor\) preceding odd gaps and \(h=\lfloor\theta\log_2 q\rfloor\) following bits. Along any sequence \(q\to\infty\) of physical centers with this many past odd gaps,
\[
 \liminf_{q\to\infty}\frac{\log\operatorname{lcm}(d_-,d_+)}{\log q}
 \ \ge\
 \max\left(0,\frac{(1+\rho)\theta-1}{2}\right).                  \tag{1}
\]
In particular at \(\theta=1\), at least one of the two actual closing denominators satisfies
\[
 \max(d_-,d_+)\ge q^{\rho/4-o(1)},\qquad \rho/4=0.157732438\ldots.       \tag{2}
\]
Each prime's forced precision reaches only \(\theta\log q+O(1)\). Formula (1) already gives a positive exponent when \(1/(1+\rho)<\theta<1\), where both single-prime precisions fall below the height of the ordinary integer.

Every sufficiently large odd state of a single positive escape has enough past. In fact after \(n\) odd steps from \(a\), one has \(q_n+1\le(3/2)^n(a+1)\), hence \(\lfloor\log_3 q_n\rfloor\le n\) eventually. Thus every sufficiently large strict record of that same orbit satisfies the theorem. Periodic paths and changing ordinary sources are also admissible whenever the indicated past is available. No assumption about rationality of a limiting record enters (1).

## Forced local agreements

The affine map of a physical word \(w\) of \(s\) shortcut bits and \(p\) ones is \(F_w(X)=(3^pX+C_w)/2^s\). Its unique rational fixed point is
\[
 \zeta_w=C_w/(2^s-3^p).
\]
All words here have a positive odd count, so the reduced denominator is prime to six. For actual starting and terminal states \(u,v=F_w(u)\),
\[
 2^s(v-\zeta_w)=3^p(u-\zeta_w).
\]
Both displacements are integral locally at two and three. Therefore \(u-\zeta_w\in2^s\mathbb Z_2\) and \(v-\zeta_w\in3^p\mathbb Z_3\). At the shared physical center \(q\), the past supplies the ternary match of order \(b\) and the future supplies the dyadic match of order \(h\). These are exact facts for the two chosen words.

## Real size of a closed phase

For a nonempty word with \(p\) ones at bit positions \(0\le i_1<\cdots<i_p<s\),
\[
 C_w=\sum_{j=1}^p3^{p-j}2^{i_j}
 \le 2^{s-p}(3^p-2^p),
\]
since \(i_j\le s-p+j-1\). Let \(H=\max(2^s,3^p)\) and \(D=|2^s-3^p|\ge1\). For every \(\epsilon>0\), the two-variable estimate (3) of [PRECISION.md](PRECISION.md), applied to \(U=2^s,V=3^p\), yields \(D\gg_\epsilon H^{1-\epsilon}\). Indeed the corresponding prime parts are already \(2^s,3^p\), and \(1+D\le2D\). At any clock with \(\min(2^s,3^p)\le H/2\) we additionally have \(D\ge H/2\) directly. Thus
\[
 |\zeta_w|\le
 \min\bigl(2^{s-p},(3/2)^p\bigr)
 \begin{cases}2,&\min(2^s,3^p)\le H/2,\\
 O_\epsilon(H^\epsilon),&\min(2^s,3^p)>H/2.
 \end{cases}                                                     \tag{3}
\]
In the second case \(s\log2=p\log3+O(1)\). Since \(\min(s\log2-p\log2,p\log(3/2))\le (1-\rho)s\log2\) for every \(p\), (3) implies both uniform estimates
\[
 \log(1+|\zeta_w|)\le (1-\rho+o(1))\,p\log3 \qquad(p\to\infty),
\]
\[
 \log(1+|\zeta_w|)\le (1-\rho+o(1))\,s\log2 \qquad(s\to\infty).
\]
The first is uniform in \(s\), and the second is uniform in \(p\). In particular \(M=\max(1,|\zeta_-|,|\zeta_+|)\le q^{(1-\rho)\theta+o(1)}\). Hence both rational labels differ from the integer \(q\) for all sufficiently large centers, even on a periodic trajectory.

## Denominator estimate

Set \(d=\operatorname{lcm}(d_-,d_+)\), \(U=d(q-\zeta_+)\), \(V=d(q-\zeta_-)\), and \(H_0=\max(|U|,|V|)\). These are nonzero signed integers with \(H_0\le d(q+M)\). Their prime parts satisfy \([U]_2[V]_3\ge 2^h3^b\), because \(d\) is prime to six. Furthermore \(1+|U-V|\le 3dM\). The disjoint-prime estimate (3) of [PRECISION.md](PRECISION.md) therefore gives
\[
 2^h3^b\ll_\epsilon d^{2+\epsilon}(q+M)^{1+\epsilon}M.
\]
Take logarithms and divide by \(\log q\). The left side has ratio \(2\theta+o(1)\), while \(M=q^{(1-\rho)\theta+o(1)}\) as an upper bound and \(q+M=q^{1+o(1)}\). Taking the lower limit and then sending \(\epsilon\downarrow0\) gives (1). Since \(d\le d_-d_+\le\max(d_-,d_+)^2\), (2) follows.

If the two labels coincide, they have the same denominator \(d\) and ordinary divisibility directly gives \(2^h3^b\le d|q-\zeta_\pm|\), which strengthens the conclusion in this case.

## All but a bounded number of closings on one side of every large coefficient record

Take a single positive odd trajectory with total clock \(S_n\) after \(n\) odd transitions. At a strict upper record of \(3^n/2^{S_n}\), every nonempty suffix of \(b\le n\) preceding odd gaps has physical clock \(s\) satisfying \(2^s<3^b\). This section uses this coefficient-record property.

Fix \(1/2<\theta<1\) and \(0<\delta<(\theta-(1-\rho))/2\). At a coefficient record of height \(q\), inspect every past odd clock \(b\in[\theta\log_3 q,\log_3 q]\) and every future shortcut clock \(h\in[\theta\log_2 q,\log_2 q]\), taking only integer clocks. Suppose the full range of past clocks is available, as holds eventually on every single escaping trajectory. Let \(k_-\) and \(k_+\) count the closings with reduced denominator at most \(q^\delta\) on the respective sides. Then for all sufficiently large \(q\),
\[
 \min(k_-,k_+)\le
 1+\left\lfloor
 2\bigl(\log_3(9/2)+\log_2 3\bigr)\frac{1-\theta}{2\theta-1}
 \right\rfloor.                                                    \tag{4}
\]
For example \(\theta=9/10,\delta=13/50\) gives at most **one** such closing on one of the two sides. The side may depend on the record. It has order \(\log q\) distinct consecutive closing clocks, each using its own actual word.

**Coinciding small phases on a given side.** Throughout these ranges (3) bounds all real phase magnitudes by \(q^{1-\rho+o(1)}\). Two small-denominator phases on the same side both agree with \(q\) at their shared prime to depth at least \(\theta\log q\) in natural-log units. Their cross-multiplied numerator difference, an integer, is therefore divisible by a prime power at least \(q^\theta\). Its absolute size is at most \(2q^{2\delta+1-\rho+o(1)}<q^\theta\) eventually. Hence every small-denominator phase on the past side equals a single rational \(\xi_-\), and likewise on the future side there is only \(\xi_+\).

**Least periods.** A fixed rational phase of a shortcut word executes that word under the actual signed rational parity rule in \(\mathbb Z_2\). Indeed write its numerator over its odd denominator. Applying the latter \(s-j\) prescribed branches to the \(j\)-th intermediate value gives its final 2-integral fixed phase. Inverting one branch from a 2-integral value gives \(2y\) for a zero or \((2y-1)/3\) for a one, respectively an even or odd 2-integral value. Iterating backwards proves physical legality at every step. In a word between odd endpoints the compressed divisions are therefore the actual exact positive gaps.

Consequently each future small clock is a literal multiple of the least shortcut period \(t_+\) of \(\xi_+\). Each past small clock is a multiple of the least *odd* period \(t_-\) of \(\xi_-\), since each associated chronological word is executed from \(\xi_-\) back to that same phase. Anchoring at either end of the closed word describes the same phase. If both counts are at least some \(K\ge2\), distinct such multiples in the two clock intervals imply
\[
 t_-\le\frac{(1-\theta)\log_3 q}{K-1},\qquad
 t_+\le\frac{(1-\theta)\log_2 q}{K-1}.                           \tag{5}
\]

For a reduced rational \(a/d\) write \(H(a/d)=\max(|a|,d)\). Any future least word of \(t_+\) shortcuts has carry and raw denominator at most \(3^{t_+}\), so \(H(\xi_+)\le3^{t_+}\). A selected past word is a repetition of the least odd cycle word of length \(t_-\). Its full clock satisfies \(2^s<3^b\), so the clock \(s_-\) of a single least lap satisfies \(2^{s_-}<3^{t_-}\). The carry envelope gives \(C<(9/2)^{t_-}\), and the raw denominator has absolute value at most \(3^{t_-}\). Thus \(H(\xi_-)\le(9/2)^{t_-}\).

**Combined lower height.** Set \(W=H(\xi_-)H(\xi_+)\), write \(\xi_\pm=a_\pm/d_\pm\) in reduced form, and multiply both displacements at \(q\) by \(d_-d_+\). The resulting integers \(U,V\) have maximum absolute value at most \(2(q+1)W\). Their difference has absolute value at most \(2W\), since it is the cross difference of the two rationals. The same two local matches at clocks at least \(\theta\log q\) apiece yield, by (3) of [PRECISION.md](PRECISION.md),
\[
 q^{2\theta}\ll_\epsilon (q+1)^{1+\epsilon} W^{2+\epsilon}.
\]
Any sequence of such records therefore satisfies
\[
 \liminf\frac{\log W}{\log q}\ \ge\ \frac{2\theta-1}{2}.
\]
The upper bounds from (5) give
\[
 \frac{\log W}{\log q}\le
 \bigl(\log_3(9/2)+\log_2 3\bigr)\frac{1-\theta}{K-1}.
\]
Choose \(K=2+\lfloor 2(\log_3(9/2)+\log_2 3)(1-\theta)/(2\theta-1)\rfloor\). These two bounds contradict each other if both counts reach \(K\) at arbitrarily large coefficient records. This proves (4). The existence threshold is ineffective.

## Scope

This theorem forces the denominators of the particular preceding and following local closings to share a polynomial lower bound. The number and position of these windows depend on the physical height \(q\). Previous single-source results concern the full sequence of initial-prefix closings from one fixed source. Previous cyclic two-sided packing compares equal past and future words at different phases of a prescribed rational cycle. The local comparison uses two independent rational closings at one varying integer. The contemporaneous PR193 packet already proves the general moving-rational-center inequality and the exact agreement after repeated words. Its estimate also implies the central height input in (4). The conclusions here use the uniformly controlled real size of the specific closings at logarithmic depths and the coefficient-record least-period argument. [PR193 moving centers](https://github.com/GettysburgResearch/collatz/blob/5cf2ea9dda23470b600a72a2fab20d929f668e5d/research/astra-unconventional-20261126/arithmetic/MOVING_CENTERS.md) [Fixed-source prefix results, 881f940d](https://github.com/GettysburgResearch/collatz/blob/881f940d4278a3409789c7d315d24a3ff2382d15/research/astra-global-closure-20261124/round6/arithmetic/README.md) · [Two-sided packing, 1be1e814](https://github.com/GettysburgResearch/collatz/blob/1be1e81427cb5cfc182fb2a4e63dbbf8baa33fbe/research/two-sided-cycle-packing-20261124/README.md)

The proof allows both denominators to be large, including on every late window of a hypothetical escape. An independent upper bound on their simultaneous size would be needed to exclude such an orbit. The present lower bound applies pointwise without producing that upper bound.
