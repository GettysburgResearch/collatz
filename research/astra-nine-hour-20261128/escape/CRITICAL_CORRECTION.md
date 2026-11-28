# The accumulated affine correction at one critical shortcut clock

**PROPOSED, source-qualified written theorem.** Use the ordinary positive shortcut map, with an even input sent to half itself and an odd input sent to \((3n+1)/2\). Let \(F_j(n)\) count the odd departures through its first \(j\) steps. Write \(D=\log(4/3)\), \(\mu=2/D\), \(\sigma^2=2(\log3)^2/D^3\), with natural logarithms. For every fixed real \(u\) and a source uniformly chosen from \(1,\ldots,X\), take
\[
 b_X=\sigma\sqrt{\log X},\qquad
 t=\lfloor\mu\log X+u b_X\rfloor,\qquad
 E_t(n)=\log\frac{2^tT^t(n)}{3^{F_t(n)}n}.
\]
Only positive \(t\) at sufficiently large \(X\) matter. The argument of the logarithm is an exactly computable positive rational. Let \(G\) be standard normal. Under the two external population inputs specified below,
\[
             E_t(n)/b_X \quad\Longrightarrow\quad A(u-G)_+.                 \tag{1}
\]
Here \(A\) is independent of \(G\). Its distribution gives each eventual positive cycle its natural population mass, at the value \(A_C=\log2-(q_C/P_C)\log3\), where \(P_C,q_C\) are its shortcut period and odd count. All escaping sources contribute at \(A=0\). The theorem includes any number of components, either bounded or escaping. The proof leaves the component masses undetermined. It does not assume that an escaping orbit has a limiting odd frequency.

For the known cycle \(1,2\), \(A_1=D/2\). Every possible nontrivial cycle has \(0<A_C\le\log(10/9)<D/2\). Thus one bounded statistic at this single critical clock suffices to distinguish universal convergence under the additional fixed-target positivity input. For **any** fixed \(s>0\), put \(B_u(v)=\mathbb E[\exp(-v(u-G)_+)]\). Then
\[
 \lim_{X\to\infty}\frac1X\sum_{n\le X}
      \exp(-sE_t(n)/b_X)=\mathbb E[B_u(sA)]
      \ \ge B_u(sD/2).                                                       \tag{2}
\]
Equality in (2) is equivalent to universal convergence. No equality, or contrary strict inequality, is proved here. The conclusion also applies at \(u=0\) and at each fixed negative \(u\). At negative \(u\) the early arrivals have small but strictly positive limiting probability.

## Population inputs and their scope

1. For each fixed positive integer \(a\), let \(P(a)\) be its shortcut predecessor set and \(\tau_a\) the first shortcut arrival there. The fixed-target clock theorem gives natural density \(d_a\) and, for each real \(z\), the natural density \(d_a\Phi(z)\) of those \(n\in P(a)\) with \(\tau_a(n)\le\mu\log n+z\sigma\sqrt{\log n}\). This is Leen's every-target corollary, with the precise shortcut normalization transcribed in Weaver 179/v1, Appendix A.5, (A.8). We read that displayed formula. Leen's full source was not rebuilt or independently verified for this packet. No local Gaussian mass estimate, empirical moment convergence or functional Brownian theorem is used. [Published statement of (A.8)](https://rstation.ai/problems/collatz/papers/179/v1) · [Leen, Brownian motion in Collatz orbits](https://doi.org/10.5281/zenodo.23252395)
2. The minimum \(m(n)=\min_{j\ge0}T^j n\) is tight in natural sampling. For example, input 1 of PR211's variance proof, Mazur's July arbitrary-diverging-threshold theorem, has a quantitative first-passage form bounding the upper density of sources avoiding large fixed thresholds by a quantity tending to zero. This also follows from Wren 7 v3, Theorem 7, in the odd clock, then stripping initial twos. The odd minimum equals the shortcut minimum: every positive even site is followed by a smaller state, and deleting intermediate even steps between odds cannot delete the minimum. These are external inputs here. [Mazur source dossier](../../external/mazur-2026/natural-density-log-time.md) · [Wren 7, Theorem 7](https://rstation.ai/problems/collatz/papers/7)
3. Only the equivalence following (2) uses that a bad source, if any exists, has a positive-lower-density population of bad sources. Mazur's September positive-predecessor theorem supplies this: an odd step from a bad odd source gives a further bad unit modulo three, and one may choose a bad odd unit by stripping twos. Its ordinary and shortcut predecessor sets agree on hitting this odd target. The same input gives positive density at target one. [Mazur's theorem record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

## The minimum and its physical clock

Let \(C_m=\{n:m(n)=m\}\). Unless \(m\) is a minimum on its own forward orbit, this cell is empty. Otherwise
\[
 C_m=P(m)\setminus\bigcup_{j<m:\, j\in P(m)}P(j).                        \tag{3}
\]
For any source in \(P(m)\), a smaller site must occur strictly before its first \(m\), since the entire future of \(m\) stays above or at \(m\). If two basins in the finite union intersect, the two targets occur on the same forward orbit in temporal order, so one basin contains the other. Delete contained or duplicate sets to obtain a disjoint union. On each retained \(P(j)\),
\[
              \tau_m(n)=\tau_j(n)+\tau_m(j).
\]
The fixed added time leaves the Gaussian limit unchanged by continuity. Subtract the finitely many timed subpopulation counts from the one for \(m\). This proves that \(C_m\) has natural density \(p_m\), and its timed law at the first minimum has distribution function \(p_m\Phi(z)\). Modifying the center and scale from the individual \(n\) to \(X\) does not alter the limit for uniform \(n\le X\). Indeed \(\log(X/n)=O_P(1)\), since \(\Pr(n<Xe^{-K})\le e^{-K}\). Use fixed \(K\), sandwich the thresholds by \(z\pm\epsilon\), and then take the two limits. Minimum tightness gives \(\sum p_m=1\). Hence
\[
   \left(m(n),\frac{\tau_{m(n)}(n)-\mu\log X}{b_X}\right)
           \Longrightarrow (M,G),\qquad \Pr(M=m)=p_m,\quad M\perp G.   \tag{4}
\]
The joint minimum–clock theorem itself is prior work of Leen. The finite disjoint-basin deduction shows explicitly why the every-target input suffices. In particular it supplies hypothesis (G) of the earlier collision packet from that input and tightness. [Earlier conditional use at PR193's pinned tree](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-global-resolution-20261124/collision/README.md)

## The exact arithmetic after first attainment

The product of the actual one-step physical ratios gives
\[
 E_t(n)=\sum_{\substack{0\le i<t\\ T^i n\ { \rm odd}}}
          \log\left(1+\frac1{3T^i n}\right).                              \tag{5}
\]
Every departure strictly before first attainment of the global minimum is distinct. Otherwise future periodicity would prevent the later first attainment. On any simple segment of length \(k\), ordering its distinct positive integer sites bounds the sum in (5) by \(H_k/3\le(1+\log(1+k))/3\). This elementary bound suffices.

Fix a minimum \(m\). If its ordinary future escapes, every prefix is simple and the same bound applies forever. If it is bounded, follow its finite transient segment and then separate complete cycle laps from a final incomplete lap. For every \(k\), its correction is \(k A(m)+O_m(1)\), where \(A(m)=A_C\) on that cycle. Telescoping the true physical height around one lap gives the stated value of \(A_C\). It is positive since a cycle contains an odd departure. A nontrivial cycle has all sites at least three, so each summand per time is at most \(\log(10/9)\). The upper bound is strictly below \(\tfrac12\log(4/3)\) because \((10/9)^2<4/3\).

Put \(A(m)=0\) for an escaping minimum. Splitting at \(\tau=\tau_m(n)\) yields, uniformly over all sources with this specified minimum, for every \(t\),
\[
   \big| E_t(n)-A(m)(t-\tau)_+\big| \le O_m(1)+O(\log(2+t)).             \tag{6}
\]
This includes \(t<\tau\). Take finitely many \(m\) first using tightness, divide (6) by \(b_X\), then apply (4). The floor error costs \(O(1/b_X)\). This proves (1), in fact jointly with the actual minimum. Tightness also identifies the density of each union of minimum cells as its sum of \(p_m\): truncate at a fixed finite cutoff and then increase it. The bounded continuity of the exponential test proves (2). Strict decrease of \(B_u\) on nonnegative arguments follows from \(\Pr(G<u)>0\). If the bad density is \(\delta>0\), its contribution lifts the right hand side above the lower bound by at least
\[
      \delta\,[B_u(s\log(10/9))-B_u(sD/2)]>0 .
\]

The *limiting probability law* in (1) identifies the law of \(A\). For each positive integer \(k\) divide its \(k\)-th moment by the finite positive number \(\mathbb E[(u-G)_+^k]\). Independence gives \(\mathbb E A^k\), and the compact interval \([0,D/2]\) is moment-determinate. This does not pass unbounded moments through weak convergence of the finite-source samples. The escaped mass is the atom at zero of \(A\); cycles with identical odd fraction contribute to the same positive atom.

## Marking individual states

The same proof gives a vector-valued form. For a fixed finitely supported real function \(f\) on positive integers, put \(L_t(f)=\sum_{i<t} f(T^i n)\). On a simple path its absolute value is at most \(\sum_x |f(x)|\). On a bounded fixed future its asymptotic mean is the uniform cycle average \(\bar f_C=P_C^{-1}\sum_{x\in C}f(x)\); use zero on escapes. For any finite collection of such functions the normalized occupations converge jointly to \((u-G)_+(\bar f_C)_f\), with **one common** component and Gaussian variable. Choosing a state from a cycle separates it from every other cycle. No measurability or identification of an infinite path by a finite computation is required to evaluate the left hand side.

The formula concerns the critical time and actual visits. Leen supplies the Gaussian population input; the full-orbit minimum decomposition also appears in Weaver's microscopic occupation paper with *distinct points in a moving height band* as observable. Here the sampling clock is fixed first, visits count with multiplicity, and the scaled cumulative affine correction is computable for each positive original source. [Weaver, Paper 18, part C](https://rstation.ai/problems/collatz/papers/18) · [PR211 source-variance comparison](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/SOURCE_VARIANCE.md)

## The lower tail of the parity count at the same clock

The cutoff where a Gaussian parity estimate would decide Collatz can be specified by a single inequality. With \(t,b_X,u\) as above, define the standardized count \(Y_X=2(F_t-t/2)/\sqrt t\). For **every fixed pair \(v<u\)**,
\[
 \lim_{X\to\infty}\Pr(Y_X\le v)
   =\sum_{C\ { \rm cyclic}} d_C\,
          \Phi\bigl(u-(A_1/A_C)(u-v)\bigr).
                                                                        \tag{7}
\]
The sum contains the known cycle as well as any hypothetical cycles. No limit of the parity frequency on an escaping orbit is needed. No functional path limit is used.

Indeed the exact product gives
\[
  (F_t-t/2)\log3=\log T^t(n)-\log n+A_1 t-E_t(n).
\]
The relations \(A_1\mu=1\) and \(A_1\sigma/\log3=\sqrt\mu/2\) follow from the specified variance of the shortcut arrival clock. Thus after division by \(A_1 b_X\), the right hand side is
\[
       u+\frac{\log T^t(n)-E_t(n)}{A_1 b_X}+o_P(1).
\]
The variable on the left is \(Y_X\sqrt{t/(\mu\log X)}\), with a deterministic factor tending to one. This factor can equivalently be applied to each fixed test threshold.

Before first attainment of the minimum the correction is \(O(\log(2+t))\), while the endpoint is at least one. Hence these sources contribute zero limiting mass to any strict subthreshold \(v<u\). The same argument applies at every time in an escaping cell, since the entire physical trajectory is simple. In a fixed cyclic cell after the minimum, the endpoint is bounded uniformly by the maximum of the complete future of that fixed minimum. By (6) the test variable there differs by \(o_P(1)\) from
\[
     u-\frac{A_C}{A_1}\frac{(t-\tau)_+}{b_X}.
\]
At \(v<u\) the corresponding limiting event requires \(G\le u-(A_1/A_C)(u-v)<u\), so it automatically lies after first arrival and has a Gaussian-null boundary. Apply (4) cell by cell, truncate the minimum at a finite cutoff, and then remove the cutoff by tightness. This proves (7).

Write \(d_1\) for the basin density of the known cycle, and \(r=A_1/\log(10/9)>1\). The concrete choice \(u=0,v=-1\) gives
\[
 d_1\Phi(-1)\le\lim_X\Pr(Y_X\le-1)
      \le d_1\Phi(-1)+(1-d_1)\Phi(-r).
\]
Therefore, under fixed-target positivity, universal convergence is equivalent to this single lower-tail probability attaining \(\Phi(-1)\) at \(t=\lfloor2\log X/\log(4/3)\rfloor\). The packet does not establish that equality. The binomial parity distribution at \(t\le\log_2X\) does not evaluate this much later clock. Inselmann's Theorem 1.1 gives macroscopic height accuracy up to this later clock and does not evaluate its one-standard-deviation parity tail. [Inselmann, Theorem 1.1](https://arxiv.org/html/2402.03276v3)

There are two other observable consequences at each fixed \(u\). As \(v\uparrow u\), the right hand side of (7) tends to \(\Phi(u)\sum_{C\ { \rm cyclic}}d_C\). As \(v\to-\infty\), its ratio to \(\Phi(v)\) tends to \(d_1\): the combined contribution of all other cycles is bounded above by \(\Phi(u-r(u-v))=o(\Phi(v))\), by the elementary Gaussian tail bounds. Both are iterated limits with the source cutoff sent to infinity first.
