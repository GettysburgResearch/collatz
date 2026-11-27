# The canonical inverse path at a specified ordinary root

**Source-qualified written theorem.** Fix a positive odd ternary unit \(a\). Use the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). Let \(X_0=a,X_1,X_2,\ldots\) follow the canonical inverse law \(P_{h,a}\), and write \(E_j=v_2(3X_j+1)\). Put \(D=\log(4/3)\). Almost surely,
\[
\begin{split}
\log X_n&=Dn+O\!\left(\sqrt{n\log\log n}\right),\\
\sum_{j=1}^n E_j&=2n+O\!\left(\sqrt{n\log\log n}\right),\\
N_w(n)&=2^{-\sum w}n+O_w\!\left(\sqrt{n\log\log n}\right)
\end{split}                                                    \tag{1}
\]
simultaneously for all fixed finite positive exponent words \(w\). Here \(N_w(n)\) counts overlapping occurrences completed through \(n\) in inverse chronological order. In addition, for every \(\epsilon>0\), almost surely
\[
 h(X_n)\le n^{5/2+\epsilon}\ \text{eventually},\qquad
 -\log P_{h,a}[E_1,\ldots,E_n]
    =Dn+O\!\left(\sqrt{n\log\log n}\right).                     \tag{2}
\]
The probability in (2) is that of the realized cylinder from this same specified root. When \(a\) is nonperiodic the natural-density entrance law \(Q_a\) satisfies all of (1)–(2), with its own cylinder probabilities. Constants in pathwise estimates may depend on the realized path. The iterated-logarithm bound is an upper estimate for fluctuations. Its optimal constants are undetermined.

The inputs are Valbuena's natural basin densities, his first-passage comparison on a geometric ladder of logarithmic heights, the bounded equivalence of the two inverse laws, the positive ordinary trace floor, and the finite-quotient Haar \(L^p\) estimate for \(1<p<2\). The argument transfers the ladder to the **last** backward visit to each low interval. It does not sample independent inverse exponents along an integer path. Weaver's Paper 12, Theorem 9, supplies a fixed positive lower bound on the *upper* occurrence frequency of each word and proves profile oscillation. The rate, frequency limits, polynomial upper bound along the sampled path, and cylinder information in (1)–(2) use the additional first-passage and sparse-set argument below. Weaver's Paper 175, §§8–9, already obtains the single-gap frequencies with \(O(n^{3/5})\) errors, the mean gap two, and the information exponent \(D\) for the natural inverse law conditioned on a *first-minimum cell* of positive density. Its common-landing argument is a direct predecessor of this proof. The arbitrary-root result here uses the full natural predecessor law and the stationary \(h\)-transformed law; its simultaneous word-count rate and polynomial trace bound are more quantitative. [Weaver, Paper 175, Theorem 1 and §§8–9](https://rstation.ai/problems/collatz/papers/175) [Valbuena, fixed source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [Weaver, Paper 12, §§9–10 and 12](https://rstation.ai/problems/collatz/papers/12) · [Weaver, Paper 127, §10](https://rstation.ai/problems/collatz/papers/127/v1)

## Last visits transfer the passage estimates

First take \(a\) nonperiodic. Let \(d_x\) be relative odd natural predecessor density, write \(B_x\) for the ordinary odd basin of \(x\), and include \(x\) in its own basin. At a fixed depth the positive unit ancestor basins are pairwise disjoint. Their probabilities \(d_x/d_a\) sum to one and determine \(Q_a\). An odd source taken logarithmically in \([Y^\alpha,Y^{\alpha^2}]\), \(\alpha=1001/1000\), conditional on belonging to \(B_a\), converges to \(Q_a\) on each fixed depth partition of its reversed word as \(Y\to\infty\). Indeed each individual cylinder probability converges by partial summation of the natural density. The limiting masses sum to one, so convergence is in total variation, including a cemetery state for sources having too few steps. In particular the conditioning denominator tends to \(d_a>0\). The identity of relative odd and all-integer densities here follows by stripping initial powers of two.

For \(r\ge a\) let \(L(r)\) be the last inverse index with \(X_{L(r)}\le r\). It is finite and is determined by a finite initial segment uniformly over inverse paths at this particular root. Its index is bounded by the maximum first-hit time of \(a\) among those finitely many odd \(x\le r\) which reach \(a\). Nonperiodicity makes the depth of each such \(x\) unique. When an ordinary source larger than \(r\) hits \(a\), its **first** forward landing at or below \(r\) is this same last backward visit on its finite reversed word. All properties of the stages between any two fixed thresholds are therefore tests of a fixed finite inverse prefix. The bound on its length may depend on \(r,a\).

Set \(x_i=M^{\alpha^i}\) for a fixed, sufficiently large \(M\ge a\), and \(s_i=\log x_i\). For \(i\ge1\) the reference source \(V_i\) is odd logarithmic on \([x_i^\alpha,x_i^{\alpha^2}]=[x_{i-1}^{\alpha^2},x_{i-1}^{\alpha^3}]\). Its landing law at \(x_i\), with the source's prescribed default, is \(\nu_{x_i}\). Valbuena's equation \(\mathrm{ct\text{-}stage\text{-}TV}\) says that a source \(V_j\) on any higher such rung \(j\ge i\) has landing law at \(x_i\) within \(Cs_i^{-c}\) in total variation of \(\nu_{x_i}\). We use events depending on the landing state and its subsequent path down to \(x_{i-1}\). An event declared bad on either reference passage failure has bad probability at most its local error plus \(Cs_i^{-c}\) for the higher source, with a successful upper landing understood on the event used for the conditioned source. For sources in \(B_a\) both actual passages succeed. Taking \(j\to\infty\) after conditioning gives the same upper bound divided by \(d_a\) for the corresponding \(Q_a\) stage. A default coinciding with a positive state causes no problem if that state is also marked bad whenever it fails the local stage estimates. [Valbuena, lemma ct-local and proof of proposition ct-time-law](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [Weaver, Paper 176, §§3–5](https://rstation.ai/problems/collatz/papers/176)

## A simultaneous estimate on each local stage

At the bottom threshold \(x=x_{i-1}\) put \(s=\log x\), \(R=\lfloor0.1s\rfloor\), and \(b=\lfloor(\log_2 x)/2\rfloor\). Valbuena's elementary binary-cylinder estimate couples the first \(R\) forward gaps of \(V_i\) to independent \(G_j\) with \(\Pr(G_j=e)=2^{-e}\), except with error \(O(e^{-c s})\). To see the truncation, words of total at most \(b\) are determined modulo \(2^{b+1}\) and the geometric-sum probability of exceeding \(b\) is \(O(e^{-cs})\). The residue discrepancy of the logarithmic source is \(O(2^b/(x^\alpha\log x))\).

Take \(K_s=A\sqrt{s\log\log s}\) at large \(s\). With probability \(1-O((\log s)^{-3})\), all centered gap partial sums through \(R\) are bounded by \(K_s\), on choosing \(A\) sufficiently large. Indeed the centered geometric law has log moment generating function at most \(Ct^2\) for small \(|t|\). Its exponential martingale maximal bound is \(2\exp(-cK_s^2/s)\), with a separate bound for each sign. The same assertion holds for centered counts of a fixed word \(w\), with a constant depending on \(w\). Split possible starting indices into \(|w|\) residue classes so the occurrence indicators within each class are independent bounded variables, then apply the same maximal bound to each class. Differences of two partial sums bound every subinterval discrepancy, up to the \(|w|\) terminal positions.

Uniformly through \(R\), the affine offset and its fraction of the leading term satisfy the estimates in the proof of \(\mathrm{ct\text{-}local\text{-}log\text{-}path}\). The new error \(K_s=o(s^{3/5})\) is admissible there. Hence every prefix log height differs from its initial log height minus \(D\) times its odd length by \(O(K_s)\). Both crossings occur by \(R\). The first landing at threshold \(r=x_i\) or \(x_{i-1}\) has log height \(\log r+O(K_s)\), by the estimates at the crossing and one step before. The stage has length \((s_i-s_{i-1})/D+O(K_s)\). Every subsegment obeys the corresponding height, total-gap and word-count bounds by subtraction. These are properties of the two-threshold passage beginning at the upper landing, including its starting height. They transfer by the previous section.

The transferred bad probabilities sum over \(i\) since \(s_i=\alpha^i\log M\) and \(\log s_i\) grows linearly in \(i\). By Borel–Cantelli almost every inverse path has only finitely many bad stages. Summing later errors costs \(O(\sqrt{s_i\log\log s_i})\) up to rung \(i\), by geometric growth. A finite initial clock and the \(O_w(i)\) word starts straddling stage boundaries are absorbed. The stage endpoints have index \(s_i/D+O(\sqrt{s_i\log\log s_i})\), and the subsegment estimates cover every intermediate index. Reversing a forward word reverses the order of its letters and preserves \(2^{-\sum w}\). This proves (1); intersect the probability-one events over the countable set of words.

## Sparse visits control the trace at the sampled ancestors

For each nonperiodic positive unit, the canonical trace obeys \(0<\alpha_0\le h(x)\le Cx d_x\). At any one inverse depth \(t\) of \(a\), the antichain gives \(\sum d_x\le d_a\). Thus within \([Y,2Y)\) a collection of depths \(\mathcal T\) contains at most \(C d_a\,|\mathcal T|Y/H\) integers whose trace exceeds \(H\). The full finite density \(\rho_j(r)=3^j\Pr(Y_j=r\bmod 3^j)\) has uniformly bounded normalized \(p\)-moment, for each \(1<p<2\). In particular for \(3^j\le Y\),
\[
 \sum_{\substack{y\in A\\y\ \mathrm{odd}}}\rho_j(y)/y
 \ \ll_p (|A|/Y)^{1-1/p}\qquad(A\subseteq[Y,2Y)).
                                                               \tag{3}
\]
Partition into periods to obtain \(\sum_{Y\le y<2Y}\rho_j(y)^p\ll_p Y\), then apply Hölder. The trace bound follows from the corrected natural-basin formula at nonperiodic units. [Weaver, Paper 12, §§8 and 10](https://rstation.ai/problems/collatz/papers/12) · [Weaver, Paper 9/v2, §§1–2](https://rstation.ai/problems/collatz/papers/9/v2)

Use a dyadic partition of the local heights in \([e^{s/2},e^{2s}]\) on a reference rung. For a fixed constant \(K\) and a dyadic \(Y\) in this range, take depths satisfying
\[
 |Dt-\log Y|\le K\sqrt{s\log\log s}.
\]
Their number is \(O_K(\sqrt{s\log\log s})\). Take \(A_Y\) to be the resulting exceptional union in that band with \(H=s^B\). On the good local height event, if a stage visits such a site \(y\) at forward time \(j\le R\) from \(V_i\), all prior states of the reference prefix are above \(e^{s/2}\) for sufficiently large \(s\). The exact ordinary word weight is \(3^j2^{-A_j}=y f_j(v)/v\), with \(f_j(v)=\prod_{\ell<j}3U^\ell v/(3U^\ell v+1)\ge1/2\). A sum of source reciprocals over this event is at most \(2\sum_{y\in A_Y}\rho_j(y)/y\). Here the sum over all legal words is a valid upper bound and each odd source has only one chronological word at time \(j\). We have \(3^R<e^{s/2}/2\) for large \(s\), so (3) applies throughout, including to a dyadic band meeting a range endpoint. The logarithmic normalizer of \(V_i\) is comparable to \(s\).

Union-bounding over \(O(s)\) times and \(O(s)\) height bands and dividing by that normalizer gives
\[
 C_{p,K}s\left(\frac{\sqrt{s\log\log s}}{s^B}\right)^{1-1/p}.
                                                               \tag{4}
\]
For any \(B>5/2\) choose \(p<2\) sufficiently close to two that (4) is \(O(s^{-\delta})\) for some \(\delta>0\). The additional bad local height and TV errors remain summable. The event of visiting any of the preselected vertices **during the stage** is determined by the upper landing and the lower passage, so the finite-prefix transfer and Borel–Cantelli apply again. Do this for every positive integer \(K\). By (1) some \(K\) covers the actual depth at every sufficiently high vertex visited by almost every path. This proves \(h(X_n)\ll n^B\) eventually. Start with \(B\) strictly between \(5/2\) and \(5/2+\epsilon\) to absorb the constant.

For a realized path the exact cylinder probability is
\[
 P_{h,a}[E_1,\ldots,E_n]
     =3^n2^{-\sum_{j\le n}E_j}\, h(X_n)/h(a).
\]
The floor and the new upper bound give \(|\log h(X_n)|=O(\log n)\), proving (2). The path measures \(P_{h,a},Q_a\) are equivalent with density bounded above and away from zero. The same bounds hold for ratios of their cylinder masses, proving the \(Q_a\) assertions. For a periodic \(a\), the probability of \(j\) entire inverse laps is the \(j\)-th power of the true cycle multiplier, strictly below one. After the almost-sure finite departure into a nonperiodic branch apply the preceding results at that new root, including the finite initial cylinder factor.

## Dimensions at every positive ordinary unit

In the gap coding use cylinder size \(e^{-n}\). The canonical law has exact dimension \(D\). In the binary coding which writes each gap as \(0^{E_j-1}1\), use cylinder size \(2^{-m}\) at bit length \(m\). Its exact dimension is
\[
 \frac{\log(4/3)}{2\log2}=1-\frac{\log_2 3}{2}.
\]
Indeed the bit lengths of consecutive complete gap cylinders are \(2n+o(n)\) and \(2(n+1)+o(n)\). An intermediate binary cylinder has probability between those of its two bracketing complete cylinders. These dimension formulae also give lower bounds for the Hausdorff dimensions of the sets of legal inverse words at this specified integer with mean gap two. They are sharp for those mean-two slices. At depth \(n\) and total \(A\le(2+\eta)n\), the distinct integer preimages are at most \(a\,2^{(2+\eta)n}/3^n\) in number, since each has size at most that bound and a source has a unique word. In the binary metric use also \(A\ge(2-\eta)n\). Cover first the paths meeting both inequalities for every \(n\) beyond one fixed index, then take the countable union of those indices and send \(\eta\downarrow0\).

The argument concerns inverse paths sampled from ordinary entrance densities. A deterministic forward path from a fixed source may have a different asymptotic exponent law. In particular the finite offset \(L(M)\) in the last-visit proof is target dependent even when \(d_a\) has a uniform positive lower bound. Its role on a hypothetical escaping ray is analyzed in the companion note.
