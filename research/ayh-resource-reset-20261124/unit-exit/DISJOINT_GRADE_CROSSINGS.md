# A summable part of the true two-head graph from reversed grade order

**Status.** PROPOSED written proof on positive ordinary shortcut sources. The complete-grid pair merger estimate of PR 146 and the original-source regeneration and envelope of PR 197 retain their source qualifications. This result bounds a weighted part of the genuine graph, including its entire square-root-size exponent menu. No theorem about a third class is assumed. Universal convergence and control of the nested-grade remainder remain open.

## 1. Which original comparisons are controlled

Write \(R=81^j,\ d=\log_2R,\ j\ge1\), and use the true binary orbit-invariant label, actual smaller heads, fixed interior mantissa arc if desired, and bounded-intercept marks of PR 197 [WEIGHTED_TWO_HEAD_GRAPH.md](../crossing-step/WEIGHTED_TWO_HEAD_GRAPH.md). Let
\[
 I_0=[3d,3.01d],\qquad I_1=[3.03d,3.04d],\qquad I_2=[3.07d,3.08d],
 \qquad h=\lfloor .01d\rfloor,\quad h'=\lfloor h/2\rfloor
\]
denote integer clock windows. Choosing \(t_i\in I_i\) on one original source gives its earlier smaller head \(z=z_0\) and later heads \(y_i=z_i\). For \(v_i=t_i-t_0\) and the effective trit difference \(w_i=k_i-k_0\), the actual arithmetic gives
\[
 y_i=\lfloor 3^{w_i}2^{-v_i}z\rfloor+b_i,\quad |b_i|\le C_A,\qquad
 |w_i-v_i/2|\le C_A\sqrt{d\log d}.                         \tag{1}
\]
Here \(k_i\) uses the common original *parent* convention, and \(v_i\asymp d\). In particular \(w_i\ge4\) and \(3^{w_i}2^{-v_i}<1\) eventually. A single good original source sample suffices. Formula (1) follows from \(z_i=3^{k_i}2^{-t_i}n+O_A(1)\) on that sample, including when the original upper arm changes.

For a pair \((z,y)\) with assigned \(v,w,b\), write \(z=81m+r\), expose \(m\bmod2^v\), and compare **four** affine rays on its remaining high quotient. Give \(m,z\) exactly \(v\) physical steps. Keep \(\lfloor y/81\rfloor,y\) at their start. The initial grade intervals of these two pairs are
\[
 [L,U]=[\min(p_m(v),4+p_z(v)),\max(p_m(v),4+p_z(v))],
 \qquad [w,w+4].
\]
Call the comparison tested here successful if the intervals are strictly disjoint and by \(h'\) further shared bits at most two distinct symbolic affine records remain among its four rays. At equal clocks symbolic equality concerns slopes and integer intercepts on the same unexposed parameter. These records determine future meetings on every positive lift. Only edges with both heads truly discordant enter the graph.

For \(p=1,2\), let \(N_p(x)\) count all choices of the \((p+1)\) marked times and their actual returned discordant heads in \(I_0,\dots,I_p\) on the original source \(x\), requiring success of each comparison \((z,y_i)\). The first head \(z\) is common to all later comparisons. Count each tuple of times and head values once, permit all choices and both original arm orientations. Set the count to zero on the common original envelope exception.

**Weighted conclusion.** With weight \(1/R\) on original children, uniformly at each high row,
\[
 \frac1{R d^{p+1}}\sum_{\substack{x\\\text{original edge discordant}}} N_p(x)
 \ll_A \frac{(\log d)^{\,2p+1/2}}{d^{(p+1)/2}} .              \tag{2}
\]
In particular, for every fixed \(\eta>0\), the normalized mass having at least \(\eta d^3\) such two-comparison triples is **summable** over \(j\), including the original \(O_A(d^{-A})\) exception when \(A>1\). For one comparison its graph degree sum itself obeys
\[
 \sum_{z\in Z_0}\frac{\#\{y\in Z_1:(z,y)\text{ is a successful true graph edge}\}}{z}
 \ll_A d(\log d)^2 .                                          \tag{3}
\]
Here \(Z_i\) are the height bands from the cited graph theorem using \(I_i\). An edge qualifies if it admits a successful representation (1); duplicates can only lower the left side. Its off-diagonal subgraph obeys the same bound. The corresponding bound in (2) for \(p=1\) is near-harmonic and is not claimed summable. Formula (2) does not assert that every discordant source supplies \(\eta d^3\) tested triples: nesting or three surviving records can prevent this.

## 2. The crossing estimate with all trit exponents summed

Fix \(r\), a complete binary grid for \(m\), and a prefix \(m=s+2^v q\). The four affine slopes in \(q\) are exactly \(3^{p_m(v)},3^{4+p_z(v)},3^w,3^{w+4}\). Indeed \(y=81\,3^w q+\lfloor 3^w2^{-v}(81s+r)\rfloor+b\); its suffix modulo 81 is already fixed. In particular the *second* head has the original bounded-suffix pair law on the next bits conditionally on this prefix, uniformly in \(w,b\). Its parent is an odd affine change of \(q\).

Use the nonnegative finite event that the intervals are disjoint, at most two symbolic classes remain at \(h'\), and both original pairs are still internally distinct at \(h\). This event contains the true success under consideration, irrespective of the eventual colors. At \(h'\) it has exactly two classes, with each internal pair using both. The two classes persist separately to \(h\). From the group whose initial interval is strictly below the other, take a member of the class with *larger* grade at \(h'\); from the initially higher group take a member of the other class. A tie of terminal class grades permits either ordering of the two distinct classes. This cross pair has reversed weak grade order at \(h'\), yet it is unfused through \(h\). Its integer grade difference changes by at most one at a clock. It must have a first grade tie \(\tau\le h'\). There are only four cross pairs to test. The two elementary deterministic steps are checked in DisjointGradeCrossing.lean.

Write \(K=\operatorname{dist}([L,U],[w,w+4])\ge1\). Each cross pair has initial grade distance at least \(K\). Conditional on the shared binary past, every individual ray has an odd high coefficient, so each next parity is fair, while their simultaneous increments may be dependent. Each signed cross-grade difference is a martingale with jumps bounded by one. Fix a sufficiently large \(B\). Put
\[
 h_0=\min\{\lfloor h/4\rfloor,\lfloor K^2/(B\log d)\rfloor\}.
\]
For \(h_0\ge1\), maximal Azuma bounds \(\Pr(\tau<h_0)\le 2\exp(-K^2/(2h_0))=O(d^{-B/2})\) per cross pair. At \(h_0=0\) that event is empty. For the other ties the fresh second head must first survive to \(h_0\); its conditional probability is \(O((1+h_0)^{-1/2})\). At a tie of controlled offset \(D_\tau\), the native survival bound for the tied cross pair from that very prefix through \(h\) is
\[
 O\!\left(\frac{1+\sqrt{\log(2+|D_\tau|)}}{\sqrt{h-h'}}\right).
\]
When \(|D_\tau|\le d^C\) this is \(O_C(\sqrt{\log d}/\sqrt h)\). The first survival is measurable by \(h_0\le\tau\). Sum the conditional bound at the stopping prefix over disjoint values of \(\tau\); there is no clock union loss. A pair fused before its tie cannot contribute. This argument uses the finite shared parameter grid, not a random restart on a genuinely discordant physical source.

Here are the offset details needed for that product. At the prescribed \(v\) a good first-head prefix has \(p_m(v),p_z(v)\le .55v\) and each physical scalar intercept \(I_v=T^v u-3^{p_u(v)}2^{-v}u\) at most \(d^{C_0}\) for \(u=m,z\). On a complete prefix grid their bad fraction is \(O_M(d^{-M})\), uniformly at our macroscopic \(v\), by the individual binomial count and scalar fractional-moment drift from PR 197. Such failures can be excluded for all tested \(v\) at polynomial cost. Relative to the common real coordinate \(m/2^v\), each incoming physical arm equals its \(3^{\mathrm{grade}}\) times that coordinate plus an error \(e_i\) of size \(O_A(d^{C_0})\). For the first child the extra suffix is \(r3^{p_z(v)}2^{-v}=O(1)\). For the fresh pair, use \(r3^w2^{-v}=O(1)\), the two floors and bounded \(b\). After \(j\) new steps the leading coefficient is \(3^{\mathrm{grade}_i(j)}2^{-j}\) and the error obeys \(e'=(3^\epsilon e+\epsilon)/2\). For any fixed \(0<\alpha<1\),
\[
 E(|e'|^\alpha\mid\mathrm{prefix})\le
   \frac{1+3^\alpha}{2^{1+\alpha}} |e|^\alpha+1 .
\]
This applies also to signed \(e\). These errors depend only on the already exposed bits, since the common unknown high coordinate cancels. A union over the four rays and \(h+1=O(d)\) clocks followed by Markov gives exceptional probability \(O_M(d^{-M})\) at threshold \(d^{C_M}\), uniformly in all good incoming prefixes and \(w,b\). At a grade tie the two leading coefficients are equal, so their physical integer offset has magnitude at most \(2d^{C_M}\). This proves the required offset estimate before conditioning on a tie.

Consequently the probability of the finite event for fixed \(w,b\), conditional on a good prefix, is at most
\[
 O_M(d^{-M})+
 C_M\frac{\sqrt{\log d}}{\sqrt h}
       \min\!\left(1,\frac{\sqrt{\log d}}{K}+\frac{1}{\sqrt h}\right).       \tag{4}
\]
Constants absorb \(B\), chosen for \(M\). For each positive \(K\), at most **two** integer \(w\)'s have that distance from the known interval while being disjoint. The entire menu has \(O_A(\sqrt{d\log d})\) candidates and \(O_A(1)\) roundings. Summing (4), the harmonic sum over \(K\le O(d)\) gives
\[
 \sum_{w,b}\Pr(\text{finite event for }w,b\mid m\bmod2^v)
                     \ll_{A,M}(\log d)^2/\sqrt d .              \tag{5}
\]
This uniform conditional upper bound replaces the square-root-size census on this part of the graph. It depends essentially on the requirement that both colors of the original two-class partition occur in **each** initially separated pair.

## 3. Genuine graph and original weight

The earlier head rows have \(z\in[7Y,8Y)\), with \(\log_2Y>.35d\) eventually and \(O_A(d)\) choices of \(Y\). For fixed \(r\) the original parameter of this smaller head runs over a consecutive \(m\)-interval of length \(Y/81\). Complete grids through \(v_p+h\le .1d\) cover it with one absolute factor for any nonnegative finite test. On this grid, a genuinely discordant \(z\)-head survives the native \(v_1\) bits. This first event has probability \(O(d^{-1/2})\).

For fixed \(v_1,\ldots,v_p\) let the finite multiplicity at the \(i\)-th comparison count all eligible \(w_i,b_i\) with its finite event. Set that multiplicity to zero on its bad incoming prefix. Its conditional expectation is bounded by (5); it is measurable by \(v_i+h\). For \(p=2\), \(v_1+h<v_2\) uniformly. Iterating conditional expectations on the common grid therefore bounds the expectation of the **product of multiplicities times first survival** by
\[
 O_A(d^{-1/2})\left(C_A(\log d)^2/\sqrt d\right)^p .
 \tag{6}
\]
There is no independence assumption about their actual witnesses. The omitted first-head prefixes have probability \(O_M(d^{-M})\) at each fixed \(v_i\); even bounding both full multiplicities crudely by \(O_A(d^2)\) costs an arbitrarily small power. The scalar record prefix is a finite test, and colored edges are counted only by necessary finite predicates. Covering the true \(m\)-interval by grids does not require colors for extrapolated points; if necessary parity branches on those grids are specified algebraically by the integer affine forms, valid on every positive lift.

Sum (6) over \(O_A(d^p)\) relative-clock tuples, the \(O_A(d)\) earlier rows and the 81 possible suffixes \(r\). On each row the harmonic weight of all \(z\) is \(O(1)\). The result, counting the arithmetic target tuples with their assigned \(v_i,w_i,b_i\), is
\[
 \sum_{\text{tested true target tuples}}\frac1z
              \ll_A d^{(p+1)/2}(\log d)^{2p}.                  \tag{7}
\]
For \(p=1\) this proves (3). For any fixed tuple with its relative clocks, the earlier source proof gives \(O_A(\sqrt{d\log d})\) admissible absolute clocks \(t_0\). At a fixed \(t_0,z\), each original suffix contributes \(O_A(R/(z\sqrt d))\) actual discordant sources on its original strip. The later times are fixed by \(t_0\) and the assigned \(v_i\). Thus the total original incidence is at most \(C_A R\sqrt{\log d}\) times (7), giving (2). This uses the original strip survival once, in addition to the distinct native test on the earlier target \(z\) in (6). There is no extra factor for the possible trit depths of the same returned positive integer. No logarithm-separation theorem is necessary for this upper bound because (7) already sums over the possible arithmetic labels.

**Remaining cases.** The two-head degree can still be carried by overlapping grade intervals, or by four-ray configurations with three or more symbolic classes at \(h'\). Transverse width of order \(\sqrt{d/\log d}\) alone does not force two separated intervals. Uniform triple moments with an initial grade span of order \(\sqrt d\) do not supply an all-purpose discard here. Formula (3) improves the weight bound on an actual portion of the central graph and (2) removes repeated such comparisons at finite total row weight. Neither proves the full sum finite.

**Pinned inputs.** PR 197 \(\mathtt{2c1397d2adcadc620381bca20c465f3bf31a6f8e}\), crossing-step/WEIGHTED_TWO_HEAD_GRAPH.md, LATE_WITNESS_TRACKS.md, and two-class-descent/HEAD_INCIDENCE.md and ADAPTIVE_PAIRED_PROJECTION.md; PR 146 \(\mathtt{f431078244e868dc699fad011044f0d5e7f76437}\), research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md, uniform-location pair estimate (1). The discrete-time crossing proof uses the bounded-increments concentration inequality [Azuma, *Weighted sums of certain dependent random variables* (1967)](https://doi.org/10.2748/tmj/1178243286); its finite maximal version follows from the usual exponential-supermartingale stopping argument.
