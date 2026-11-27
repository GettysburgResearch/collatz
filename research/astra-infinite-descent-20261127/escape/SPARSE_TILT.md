# Pointwise sparse inverse mass and fixed physical clocks

The estimates below are written proofs for actual positive integer Collatz paths. The finite residue identities, bounds on the three frequency regions, depth exponents and physical first-hit projection have been separately reviewed in this research pass. The parameter \(p\downarrow0\) assigns long inverse halving gaps high probability. All errors are uniform in the positive odd target \(y\) with \(3\nmid y\). The pointwise mass estimate holds through explicit quasi-polynomial depth. The fixed-clock theorem below also reaches a smaller quasi-polynomial horizon, which includes grades far above the elementary square-root range.

## The actual kernel and its mass

Use the shortcut map \(T(2x)=x,\ T(2x+1)=3x+2\). Let \(U_k=(\mathbb Z/3^k\mathbb Z)^\times\), \(k\ge1\), with uniform probability. Extend these means to locally constant functions on \(U=\mathbb Z_3^\times\). Put \(q=1-p\), with \(0<p<1\), and
\[
 I_e(y)=(2^e y-1)/3,\qquad
 A_pf(y)=3\sum_{\substack{e\ge1\\2^e y\bmod9\in\{4,7\}}}
               p q^{e-1} f(I_e(y)).
\]
For an odd ordinary target every accepted edge has positive odd source prime to three, runs to \(y\) in exactly \(e\) shortcut steps, and makes exactly one odd departure. Conversely every such consecutive odd-state edge occurs. Thus \(A_p^d1(y)\) is \(3^d\) times the independent geometric weight of exactly the legal length-\(d\) inverse words through positive odd units. The factor \(3^d\) normalizes the mean. The estimates do not discard visits below a positive floor and do not give an estimate for a prescribed forward path.

For a function \(f\) on \(U_k\), \(A_pf\) lives on \(U_{k+1}\). For any fixed \(e\), multiplication by \(2^e\) permutes \(U_{k+1}\), and the accepted residues are exactly \(1+3x\) as \(x\) ranges through \(U_k\). Thus \(A_p\) preserves the normalized mean. For fixed \(y\), as \(e\) ranges through one period \(b=2\cdot3^k\), the same accepted \(x\)'s occur exactly once. Indeed 2 generates \(U_{k+1}\): \(v_3(4^{3^j}-1)=j+1\) by induction from \((1+3^h u)^3-1\), with \(3\nmid u\), and odd powers of 2 are \(2\bmod3\). This proves the required order.

Write \(P f=\operatorname{mean}(f)\) as a constant. For \(bp\le1/2\), the geometric probability at \(r\bmod b,\ 1\le r\le b\), divided by \(1/b\), lies between \(1-bp\) and \((1-bp)^{-1}\). This follows by dividing \(q^{r-1}\) by the average of \(1,q,\ldots,q^{b-1}\). Since precisely a third of the residues are accepted,
\[
  \|(A_p-P)f\|_\infty\le 2bp\|f\|_\infty. \tag{1}
\]

Put \(g_j=A_p^j1-A_p^{j-1}1\). Each \(g_j\) has mean zero and level at most \(j+1\). Even though \(1\) has nonzero mean, \(g_1=(A_p-P)1\). Induction using (1) gives
\[
 b_j:=\|g_j\|_\infty\le (4p)^j3^{j(j+1)/2}
\quad(2p3^j\le1/2).
\]
Take \(K=\lfloor\log_3(1/(8p))\rfloor\) for \(p\) sufficiently small. Each successive displayed bound has ratio at most \(1/2\) up to \(K\). Consequently \(h=A_p^{K-1}1\) satisfies \(\|h-1\|_\infty\le24p\). Put \(\eta=(4p)^K3^{K(K+1)/2}/(1-24p)\). Since \(A_ph=h+g_K\), positivity gives for \(d\ge K-1\)
\[
 (1-\eta)^{d-K+1}h\le A_p^d1\le(1+\eta)^{d-K+1}h. \tag{2}
\]
For every \(c<1/(2\log3)\), \(\log\eta=-(\log(1/p))^2/(2\log3)+O(\log(1/p))\), hence
\[
 \sup_{\substack{1\le d\le\exp(c\log^2(1/p))\\y\in U}}
   |A_p^d1(y)-1-c_y p|=O_c(p^2). \tag{3}
\]
For \(d<K-1\), directly telescope the \(g_j\)'s. For larger \(d\), (2) changes \(h\) by \(o(p^a)\) for every fixed \(a\). The terms from \(g_2\) onward total \(O(p^2)\). If the two allowed residues in \(1,\ldots,6\) are \(a,b\), then \(A_p1=3(q^{a-1}+q^{b-1})/(1+q+\cdots+q^5)\), yielding \(c_y=(7-a-b)/2\).

| \(y\bmod9\) | 1 | 2 | 4 | 5 | 7 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(c_y\) | \(1/2\) | \(3/2\) | \(-1/2\) | \(-1/2\) | \(-3/2\) | \(1/2\) |

The joint depth and parameter restriction matters. When \(p>1/3\), take the ordinary odd target \(y_d=2\cdot3^{d+1}-1\). Its first \(d\) inverse letters can all equal 1. Indeed the successive states are \(2^{i+1}3^{d+1-i}-1\), \(0\le i\le d\). They are positive odd units and contribute \((3p)^d\). This rules out a uniform bounded first moment at the fair law \(p=1/2\). Both the target and the starting integer move in this construction.

## A pointwise local limit for the total inverse clock

Let \(a_{d,m}(y)\) count legal words of exactly \(d\) gaps with total \(m\), and put
\[
 W_{d,m}(p,y)=3^d p^d q^{m-d}a_{d,m}(y)
\]
for \(m\ge d\), and zero otherwise. Let \(G_d\) denote a sum of \(d\) independent positive geometric variables of parameter \(p\). For every fixed \(A>0\), as \(p\downarrow0,\ d\to\infty,\ d\le p^{-A}\),
\[
 \sup_{m\in\mathbb Z,\ y\in U}
 \left|W_{d,m}(p,y)-\Pr(G_d=m)\right|=o_A(p/\sqrt d). \tag{4}
\]
In particular, the physical odd-source count at \(p=d/m\) is
\[
 a_{d,m}(y)=(1+o_A(1))\,3^{-d}{m-1\choose d-1}. \tag{5}
\]
The mass in (4) includes actual paths whenever the target is ordinary. Constants for each fixed \(A\) may depend on \(A\).

To prove (4), insert \(e^{ite}\) in each summand of \(A_p\), obtaining \(B_t\). Its \(d\)th power at \(1\) is the Fourier transform of \(W_{d,m}\). Let \(\phi(t)=p e^{it}/(1-qe^{it})\). Select a fixed integer \(K>8A+20\), and restrict to \(d\ge K\), possible in this limit. For \(k\le d\), positivity and (3) give \(\|B_t^k f\|_\infty\le2\|f\|_\infty\) through domination by \(A_p^k|f|\).

Use the grid of \(B=2\cdot3^K\) roots on the frequency circle, and distance \(\tau=\sqrt p\). Off the \(\tau\)-neighborhood of all roots, a level-\(j\) input, \(1\le j\le K\), satisfies
\[
 \|B_t f\|_\infty\le C_K\sqrt p\,\|f\|_\infty.
\]
To see this, sum over one exponent period \(b=2\cdot3^j\). The denominator of the resulting geometric series is \(1-q^b e^{ibt}\), with magnitude at least \(c_K\tau\), since all roots of \(e^{ibt}=1\) lie on the grid and \(q^b\to1\). The numerator is bounded by \(3bp\|f\|_\infty\). Apply this estimate \(K\) times to \(1\), then apply the uniform domination to the remaining steps.

Near a nontrivial grid root \(t_0\), write \(u=t-t_0,\ s=1-qe^{iu}\), so \(|s|\le p+|u|\le2\sqrt p\). The cyclicity above provides a nontrivial multiplicative character \(\chi\) on \(U_{K+1}\) with \(\chi(2)=e^{it_0}\). In each legal branch \(e^{it_0 e}=\chi(1+3x)/\chi(y)\), \(x=I_e(y)\). Define \(A_s\) by the same rational period formula as \(A_p\), using geometric weights \(s(1-s)^{e-1}\). Here \(|1-s|=q<1\). At bounded input level \(j\) it preserves the mean by the same finite counting argument; also
\[
 \|(A_s-P)f\|_\infty\le C_j |s|\|f\|_\infty.
\]
Indeed the residue weights are \((1-s)^{r-1}/\sum_{i=0}^{b-1}(1-s)^i\), analytic near zero with value \(1/b\) there. Consequently
\[
 B_{t_0+u}f=\phi(u)\,\overline{\chi(y)}
 A_s\big[x\mapsto\chi(1+3x)f(x)\big](y).
\]
The same formula with \(P\) in place of \(A_s\) defines \(\phi(u)R\). The rank-one operator \(R\) has norm at most one and \(R^2=0\), since its iterated scalar is the mean of \(\chi((1+3x)/x)\). The map \(x\mapsto3+x^{-1}\) permutes \(U_{K+1}\), so this nontrivial character has zero mean. On inputs of level at most \(2K+2\) the replacement error is \(O_K(\sqrt p)\), and \(|\phi(u)|\le1\). In the first \(K\) iterates all the multiplying functions and outputs have level at most \(2K+2\). Every pair of consecutive factors therefore has norm \(O_K(\sqrt p)\) on the applicable finite input level, by expanding \((\phi R+E)^2\) and using \(R^2=0\). Thus \(\|B_t^K1\|_\infty=O_K(p^{\lfloor K/2\rfloor/2})\) near each nontrivial root. Later factors are bounded by domination as above.

Near the zero root, \(B_t=\phi(t) A_s\) with \(s=1-qe^{it}\). At the fixed finite levels just used, mean preservation and the complex estimate give \(h_K=A_s^K1=1+O_K(|s|)\), and \(\|A_s h_K-h_K\|_\infty=O_K(|s|^{K+1})\). Telescope \(B_t^{d-K}h_K-\phi(t)^{d-K}h_K\) via \(B_t h_K-\phi(t)h_K\). Using the same uniform domination on the powers of \(B_t\) gives
\[
 B_t^d1=\phi(t)^d(1+O_K(\sqrt p))+O_K(d\,p^{(K+1)/2}).
\]
All bounds on the remainder, and on the nonzero frequency regions, are \(o_A(p/\sqrt d)\) with the chosen \(K\). The comparison transform \(\phi(t)^d\) itself is \(O(p^{d/2}C^d)\) on \(|t|\ge\sqrt p\), with \(-\pi\le t\le\pi\). Finally \(\int_{-\pi}^{\pi}|\phi(t)|^d\,dt=O(p/\sqrt d)\) for \(d\ge3,\ p\le1/2\), since \(|\phi|^2=p^2/(p^2+2q(1-\cos t))\) and the integral of \((1+c t^2/p^2)^{-d/2}\) has this bound. Fourier inversion proves (4). At \(d/m=p\), the elementary negative-binomial formula and Stirling's formula give \(\Pr(G_d=m)\sim p/\sqrt{2\pi d}\), proving (5). The same local estimate holds for displacements \(o(\sqrt d/p)\) from the mean. One can see this by Stirling uniformly on that range.

## A longer horizon for the physical clock

The same conclusions (4) and (5) hold for every fixed \(0<c<1/(32\log3)\) over
\[
 d\le\exp(c\log^2(1/p)),\qquad p\downarrow0,\quad d\to\infty. \tag{7}
\]
Here are the dependence estimates for the previously fixed \(K\). Put \(L=\log(1/p)\) and \(K=\lfloor L/(8\log3)\rfloor\). The fixed-\(K\) proof already covers \(d\le p^{-1}\), so assume \(d>p^{-1}\); in particular \(d\ge K\). Continue to use \(\tau=\sqrt p\) and the grid of size \(2\cdot3^K\).

* Outside the grid neighborhoods, \(b\le2\cdot3^K\) implies \(q^b\ge1/2\) for all sufficiently small \(p\). The distance of \(bt\) from \(2\pi\mathbb Z\) is at least \(b\tau\), because the \(b\)-grid is a subset of the selected grid. Thus \(|1-q^b e^{ibt}|\ge c_0 b\tau\) with an absolute \(c_0>0\). The per-step upper bound is \(C p/\tau\). Across \(K\) steps this is \(\exp(-L^2/(16\log3)+O(L))\).
* At every nonzero root, the complex estimate on level \(j\) can be taken in the form \(C b|s|\) when \(b|s|\le1/4\), with \(b=2\cdot3^j\) and absolute \(C\). In fact \(|(1-s)^i-1|\le i|s|\) for \(|1-s|\le1\), so dividing by the finite mean of these powers gives this estimate term by term. Through the first \(K\) transfers, level \(j\le2K+2\) gives \(b|s|=O(p^{1/4})\). The norms of the rank-one parts remain at most one independently of their conductor. Each consecutive pair gains \(O(p^{1/4})\) from its square-zero leading part. After \(K\) steps the bound is \(\exp(-L^2/(64\log3)+O(L))\).
* At zero the successive centered increments through \(j=K+1\) are bounded by \((C|s|)^j3^{j(j+1)/2}\) for \(|s|\le2\sqrt p\). Their bounds have successive ratio \(O(p^{3/8})\) through \(K+1\), after the initial \(O(|s|)\) term. Thus \(h_K=1+O(\sqrt p)\) and the residual has norm at most \(\exp(-7L^2/(128\log3)+O(L))\). Its contribution after telescoping is at most this bound times \(2d\).

The first two bounds are \(o(p/\sqrt d)\) under (7). The residual after multiplication by \(d\) also has this property since \(3c/2<7/(128\log3)\). The real positivity domination is available by (3). This proves the extension using the same Fourier inversion and scalar local limit. For example \(d/m\) may be of size \(\exp(-C\sqrt{\log m})\) with fixed \(C>\sqrt{32\log3}\) at the centered clock.

## First hits, even sources and physical location

Write \(N_{d,m}(y)\) for the number of all positive ternary-unit integers \(n\) with \(T^m n=y\) and precisely \(d\) odd departures; write \(N^{\rm first}_{d,m}(y)\) when this is also the first time \(y\) is visited. Then, as \(d\to\infty,\ d/m\to0,\ d\le (m/d)^A\) for fixed \(A\),
\[
 N^{\rm first}_{d,m}(y)\sim N_{d,m}(y)\sim 3^{-d}{m\choose d}\quad\hbox{uniformly in }y. \tag{6}
\]
If only odd sources are counted, both counts are asymptotic to the right side of (5). The parity of the source is the only difference between (5) and (6). The bounds under (7) also apply here and to the defect law below: one may require \(d\le\exp(c\log^2(m/d))\) for any fixed \(c<1/(32\log3)\). The change from \(d/m\) to \((d+1)/(m+1)\) in the even-source convolution costs \(O(1/d)\) inside the logarithm, absorbed by any slightly larger admissible \(c\).

Indeed a word of total \(S\le m\) lifts its last odd source \(x\) to \(2^{m-S}x\). The number \(m-S\) is recovered by its two-adic valuation, and the forward orbit uniquely recovers every remaining gap. For sources of either parity convolve (4) with an independent geometric-zero variable \(R\) having \(\Pr(R=r)=p q^r,\ r\ge0\). Convolution has norm one on bounded functions. The scalar comparison is \(G_d+R\), and the exact common factor for each physical clock is \(3^d p^{d+1}q^{m-d}\). Taking \(p=(d+1)/(m+1)\) centers the clock. Equivalently \(G_d+R+1\) has the law of \(G_{d+1}\), giving (6) for all visits.

A repeated visit to the odd target forces a closed nonempty reverse prefix of \(i\le d\) odd gaps. If its sum is \(S_i\), the product along the closed positive orbit is \(2^{S_i}=\prod_j(3+1/x_j)\le4^i\), hence \(S_i\le2i\). The total tilted mass of all such prefixes, including the factor \(3^i\), is at most \((3p)^i{2i\choose i}\le(12p)^i\). For \(i\le d/2\), the remaining words have pointwise mass \(O_A(p/\sqrt d)\) at any total by (4) and the scalar geometric bound, also after convolution by \(R\). The total cost of these returns is \(O_A(p^2/\sqrt d)\). For \(i>d/2\), bound the remaining unrestricted mass by two using (3), and sum the geometric tail. The result is \(o_A(p/\sqrt d)\). First hits therefore have the same asymptotic. All intermediate even states differ from the odd target.

For a path counted in (5) or (6), write \(e_1,\ldots,e_d\) for its reverse gaps, \(S_i=e_1+\cdots+e_i\), and
\[
 \beta=y-\frac{3^d n}{2^m}
      =\sum_{i=1}^d3^{i-1}2^{-S_i}.
\]
Under the uniform counting probability at the fixed \(y,m,d\), with or without the first-hit restriction, \(p e_1\) and \(p(-\log_2\beta)\) converge in law to an exponential random variable of mean one. For the first claim, fix \(M\) and restrict to \(\ell=e_1\le M/p\). The remaining clock is within \(O_M(1/p)\) of its mean, so (4) and its scalar central estimate give a completion weight \((1+o(1))p/\sqrt{2\pi d}\), uniformly in the child and \(\ell\). Out of every six exponents exactly two are admissible, and their combined mass \(3p q^{\ell-1}\) on any fixed scaled interval converges to its exponential probability. Let \(M\to\infty\) using the total mass asymptotic.

With conditional probability \(1-O(p)-o(1)\), every segment \(e_2+\cdots+e_{i+1}\), \(1\le i<d\), exceeds \(2i\). Bound failures by the same \((12p)^i\) count and the remaining pointwise local estimate for \(i+1\le d/2\); the extra first exponent has uniformly bounded total mass by (3). For larger \(i\) use domination and the geometric tail as before. On this event \(2^{-e_1}\le\beta\le4\,2^{-e_1}\). The location assertion follows. In particular these return counts lie close to the grade-\(d\) scale \(2^m y/3^d\); they do not establish coverage of all integers in a prescribed interval.

## Relation to prior work and the convergence question

Tao's Syracuse variable uses the fair positive geometric law. Leen studies tilted three-adic Syracuse laws, including regularity at fixed parameters; Wren's paper 10 explains the relation between valuation-resolved atom probabilities and Wirsching's physical path counts. The terminal-unit condition here removes the factor \(3/2\) in the Haar average over all inverse sources. The quantitative results above concern a sparse limit uniform in the specified target, with a fixed physical clock, optional first arrival and the indicated sparse grade ranges. They use elementary finite unit arithmetic, geometric series and Fourier inversion. [Tao](https://doi.org/10.1017/fmp.2022.8) · [Leen](https://doi.org/10.5281/zenodo.23268832) · [Wirsching](https://doi.org/10.3934/dcds.2003.9.771) · [Wren, §5](https://rstation.ai/problems/collatz/papers/10/v3).

The open convergence estimate concerns a prescribed ordinary **forward** source at all depths, often with a floor or retained energy. These backward sums count all actual sources visiting a prescribed target under a sparse clock weight. The moving negative-shadow integers above also exclude a direct all-target boundedness extension to \(p=1/2\). No summable fixed-source survival estimate follows from (3)–(6).
