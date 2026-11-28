# A half-density colour survives the actual precritical Collatz trajectory

**Status: PROPOSED written theorem.** The construction gives an explicit mathematical obstruction to promoting finite-scale, original-source colour agreement to component invariance. It uses genuine positive shortcut orbits. No assertion of a nontrivial component is made.

Write \(T(x)=x/2\) for even \(x\), \(T(x)=(3x+1)/2\) for odd \(x\), and \(u(x)=x/2^{v_2(x)}\). Here \(\log\) is natural and \(\log_2\) is base two. Put \(L(x)=\log\log\log x\) at sufficiently large \(x\). For any fixed cutoff \(M\), there is a binary colouring \(c\) of all positive integers with the following properties.

1. It has natural density \(1/2\), satisfies \(c(2x)=c(x)\) exactly, and vanishes whenever \(u(x)\le M\).
2. For each fixed positive rational \(a\) and fixed real \(b\), the fraction of \(X\le n<2X\) with \(c(n)\ne c(\lfloor an+b\rfloor)\) is
   \[
      O_{a,b,M}\!\left(\frac1{(\log X)(\log\log X)\sqrt{L(X)}}\right).                 \tag{1}
   \]
   The same estimate applies to one genuine shortcut step by splitting by parity. It applies to dyadic siblings by the two affine comparisons. It is not a summable bound when sampled at \(X=2^k\).
3. For every fixed \(A>0\) and \(0<\theta<1\), outside a set of starting integers of natural density zero, **simultaneously for every** \(0\le t\le(\log n)^A\) one has
   \[
      \min_{0\le i\le t}u(T^i n)\ \ge Y_n:=\exp((\log n)^\theta)
      \quad\Longrightarrow\quad c(T^t n)=c(n).                                                   \tag{2}
   \]
   The argument uses no distributional assumption about an endpoint.
4. Let \(d=\log(2/\sqrt3)\). For each fixed \(0<\varepsilon<1\), a set of natural density one has constant colour on its whole actual trajectory up to \((1-\varepsilon)\log n/d\). This corollary uses Inselmann's macroscopic theorem.
5. Given \(\eta>0\), one can choose a fixed \(M\) so that the set of positive original sources which *eventually encounter a genuine colour change* has lower natural density at least \(1/2-\eta\). Only this conclusion uses the external tightness of the ordinary orbit minimum.

Thus large-scale constancy survives on the same original trajectories over the entire strictly precritical time range, even when a positive mass eventually crosses an edge where the colour changes. Exact invariance on odd edges remains an additional arithmetic condition. The example complements the summable-sibling rigidity theorem for eventually invariant colourings. It does not show that an *exactly* invariant nonconstant plus-map colour can attain (1).

## Two frequencies, with the correct density at every intermediate mixture

Let \(p_i\) enumerate the primes, \(Q_j=\lceil\exp(\exp(3(j+4)^2))\rceil\) for \(j\ge1\), and \(k_0=1\). By simultaneous Dirichlet approximation choose \(1\le m\le Q_j^j\) such that
\[
 k_j=m Q_j k_{j-1},\qquad \|k_j\log_2 p_i\|_{\mathbb R/\mathbb Z}\le Q_j^{-1}\quad(i\le j).
\]
Indeed apply the usual box pigeonhole to multiples of \(Q_j k_{j-1}(\log_2 p_i)_{i\le j}\). Any admissible choice works. We have \(k_{j-1}\mid k_j\), \(k_j\ge Q_j\), and \(\log k_j\le\sum_{i\le j}(i+1)\log Q_i\). In particular when \(j^2\le L(X)<(j+1)^2\), for each \(i=j+O(1)\) and fixed \(C>0\),
\[
 k_i^{-1}+Q_i^{-1}=o((\log X)^{-C}),\qquad
 \log k_i\le (\log\log X)^{O(1)}.                                             \tag{3}
\]
The first inequality follows since \(\log\log X<\exp((j+1)^2)\) while \(\log Q_i\ge\exp(3(i+4)^2)\). The fixed displacement in the index may have either sign.

For \(w\ge1\), let \(j=\lfloor\sqrt w\rfloor\), \(s=(w-j^2)/(2j+1)\), and \(B(z)=\mathbf1_{\{z\}<1/2}\), where braces denote fractional part. Define the period-one function
\[
 F(w,z)=\begin{cases}
 B(k_{j+1}z),&\{2k_{j+1}z\}<s,\\
 B(k_jz),&\text{otherwise}.
 \end{cases}                                                                  \tag{4}
\]
Both bit functions on the right are constant on the grid cells of length \(1/(2k_{j+1})\). The first branch occupies fraction \(s\) of every grid cell. On every complete period of length \(1/k_j\) each bit function has mean \(1/2\), so (4) has mean exactly \(1/2\) for *every* \(s\). At a stage change the former stage tends in measure to its fine bit, which is exactly the new coarse bit. Define
\[
                 c(n)=F(L(u(n)),\log_2 n)                                      \tag{5}
\]
once \(u(n)>M\) and \(L(u(n))\ge1\), and set it to zero otherwise. Since all frequencies are integral, removing or restoring powers of two in the second coordinate is immaterial. This proves the exact doubling identity.

## Sampling and freezing the scale

For fixed \(0<c_0<c_1\), an interval or bounded union of intervals \(I\) on the unit circle, and one progression modulo \(h\), the count of \(c_0X\le n<c_1X\) in that progression satisfying \(\{k\log_2 n\}\in I\), divided by \(X\), is at most
\[
                O_{c_0,c_1}\big((|I|+1/k)/h+k/X\big).                         \tag{6}
\]
The constant depends also on the fixed number of intervals. In log coordinates the bounded smooth weight has size \(O(X)\), and at most two end periods are incomplete. Returning to integers in one progression costs at most one per interval, of which there are \(O(k)\). For an arbitrary frozen profile (4), integrate its zero-mean part period by period against the log-coordinate weight. The weight varies by \(O(X/k_j)\) per coarse period, so the difference from half the interval length is \(O(X/k_j)\). Returning to all integers costs \(O(k_{j+1})\) because that bounds the number of constant pieces on the sample interval.

Set \(w_0=L(X)\), \(j=\lfloor\sqrt{w_0}\rfloor\), and \(R_X=1/[(\log X)(\log\log X)j]\). Uniformly on every such fixed proportional interval, replacing (5) by \(F(w_0,\log_2 n)\) costs \(O(R_X X)\) exceptional integers. Here are the quantitative details. Discard \(v_2(n)>V=\lceil 4\log_2\log X\rceil\), at cost \(O(X2^{-V}+1)\). With \(v_2(n)=v\le V\), the mean value theorem gives
\[
 |L(u(n))-w_0|=O((1+v)/[(\log X)(\log\log X)]).
\]
Within one stage a change in (4) requires its fine gate variable to be within \(O((1+v)R_X)\) of the frozen threshold. If a stage boundary intervenes both profiles coincide with its shared bit except when a neighboring gate is within that distance of its endpoint \(0\) modulo one. There is at most one such boundary. Apply (6) to the single residue class \(2^v\bmod 2^{v+1}\) and at most two gates, then sum over \(v\le V\). The main sum is \(O(R_X\sum_v2^{-v}(1+v))\); the errors are negligible by (3), since \(V=O(\log\log X)\) and every frequency used is \(X^{o(1)}\). The small-core exceptions have already been discarded at large \(X\).

The frozen half-mean now gives half-density on all fixed proportional intervals. In particular it gives natural density by a dyadic tail decomposition. For \(m=\lfloor an+b\rfloor\) in (1), freeze both colours at the same \(w_0\) by this estimate; the integer map \(n\mapsto m\) has bounded multiplicity. Write \(a\) as a fixed product of signed prime powers. By (3) and the simultaneous approximation, at each relevant frequency \(k_i\),
\[
 \|k_i(\log_2 m-\log_2 n)\|
      \le O_a(Q_i^{-1})+O_{a,b}(k_i/X)=o(R_X).
\]
A disagreement of the frozen profiles places one of at most three circle coordinates of \(n\) within \(o(R_X)\) of a discontinuity (including the wrap of the gate). Equation (6) proves (1). The parity split uses respectively \(a=1/2,b=0\) and \(a=3/2,b=1/2\). For dyadic siblings compare the two maps \(2n,2n+1\) with \(n\).

## Simultaneous control of the actual orbit

For the true trajectory write \(x_i=T^i n\) and let \(q_t\) count odd departures up to time \(t\). The [locally compiled Lean certificate](OrdinaryPhaseBound.lean) bounds the finite multiplicative ratio between 1 and \((1+1/(3H))^t\) above a positive integer departure floor \(H\). The exact multiplicative identity gives
\[
 \log_2 x_t-\log_2 n=q_t\log_2 3-t+
 \sum_{\substack{i<t\\x_i\ {\mathrm{odd}}}}\log_2(1+1/(3x_i)).                   \tag{7}
\]
Suppose the hypotheses of (2) hold at time \(t\). Every summand is at most \(1/(3Y_n\log 2)\). We have \(\log x_t\le \log n+t\log 2\), using \(T(x)\le2x\) for positive \(x\). Thus, for \(n\in[X,2X)\), both \(L(u(x_t))\) and \(L(u(n))\) are within a fixed constant of \(w_0=L(X)\): throughout the permitted range the log-height lies between \((\log n)^\theta\) and \((\log n)^{C_A}\) for a fixed \(C_A>\max(1,A)\). These inequalities also hold for the odd parts using the stated minimum. For all sufficiently large \(X\), that fixed interval in the \(w\)-coordinate meets at most two stages. For *every* frequency \(k_i\) in those stages, (7) gives
\[
  \|k_i(\log_2 x_t-\log_2 n)\|
    \le (\log n)^A\left(Q_i^{-1}+k_i/(3Y_n\log 2)\right)=o(1).               \tag{8}
\]
The last bound is uniform in permitted \(n,t\), by (3) and \(\log Y_n=(\log n)^\theta\).

Define a bad subset of the original shell as follows. Exclude the \(o(1)\)-neighborhood from (8) around the discontinuities of the bit functions at each of the finitely many relevant frequencies. If there is one stage, also exclude its gate near its frozen threshold and its wrap, to width \(O(1/j)+o(1)\). If there are two stages, exclude both gates within that width of the stage endpoint, including its wrap. In the latter case both profiles agree with the shared boundary bit outside this exception because the allowed range of \(w\) stays within a fixed distance of the boundary. The exceptional measure is \(o(X)\) by (6). Every permitted original source outside it gives the same bit decision at both endpoints and at **every** permissible date by (8). This proves (2) without adding per-date errors. The dyadic tail argument again gives the asserted natural density.

## Where the colour really breaks

Inselmann's Theorem 1.3 yields, simultaneously at integer times \(i\le (\log n)/d\), on a density-one set for each fixed \(\delta>0\),
\[
                 \log x_i=\log n-di+O(\delta\log n).
\]
One may take the error bound \(\delta\log n\) by choosing \(\lambda=1-di/\log n\) in the theorem; the equivalent uniform bound is also its Theorem 1.1. Fix \(\varepsilon>0\) and take \(\delta\) sufficiently small relative to it. Then \(x_i\ge n^{\varepsilon/2}\) up to \((1-\varepsilon)\log n/d\). Choose a small fixed \(h>0\) with \(h<\varepsilon/(2d)\) and \(h\log 2<\varepsilon/4\), and shrink \(\delta\) further so \(h(\log2-d)>3\delta\). If \(v_2(x_i)\ge\lfloor h\log n\rfloor\), that many subsequent pure halvings contradict the uniform profile at their two endpoints: the difference between their logarithmic slopes is \(\log2-d>0\). These endpoints still lie within the theorem's time range. Consequently \(u(x_i)\ge n^{\varepsilon/4}\) at every displayed early date. Apply (2) with any \(\theta<1\) and \(A=2\). [Inselmann, Theorems 1.1 and 1.3](https://arxiv.org/html/2402.03276v3)

The natural-density tightness input says that for each \(\eta>0\) one may choose a fixed \(M\) such that at least \(1-\eta\) in lower natural density eventually hit \([1,M]\). The cited fixed-target specialization gives this, and intermediate raw even steps cannot remove a smaller odd part. All such destinations have colour zero. Since the marked sources have density \(1/2\), at least \(1/2-\eta\) in lower natural density start marked and reach an unmarked destination, which requires a true colour change on the way. Both analytic inputs in these two paragraphs are source-qualified. [Mazur fixed-height theorem dossier](../../external/mazur-2026/natural-density-log-time.md)

The precritical agreement considered in isolation has a simpler antecedent: the indicator of ever visiting 5 is exactly invariant on every edge except the single departure from 5, and both colours have positive lower density. Paper 212 proves this, and gives branch-specific disagreement upper bounds of order \((\log X)^{-1/2}\). No general rational-dilation agreement or half-density follows from that example. The new obstruction is their simultaneous realization here, with rate (1), along actual paths.

McNamara's stable-set construction already uses changing archimedean characters approximating prescribed prime phases, with a moving gate. That is the origin of the frequency method. The earlier paper arranges a disappearing pattern of three consecutive marked integers. Here the nested half-density interpolation, near-harmonic one-step error and uniform ordinary-path conclusion serve a different purpose. Lean Assurance Lab's summable-sibling result uses eventual exact Collatz invariance and summability to obtain a strong limiting profile invariant under doubling and tripling. The present colour has infinitely many actual defects and gives no counterexample to that theorem. [McNamara, §§1–2](https://arxiv.org/abs/2312.08544) · [Lean Assurance Lab, Paper 212, “Density from dyadic siblings”](https://rstation.ai/problems/collatz/papers/212/v1)

**First open step.** A positive full-proof route through component colours must exploit exact odd-edge propagation, quantitative information about genuine visits to small heights, or another condition excluding this construction. The affine and path agreement estimates quantified above do not provide that exclusion by themselves.
