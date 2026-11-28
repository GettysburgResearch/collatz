# Short rank intervals of a two-grade integer cycle are Sidon sets

Write \(p,m,X\) for the primitive odd period, least odd state and greatest odd state of a positive ordinary Collatz cycle, \(A\) for its total native division exponent, and \(\gamma=\log_2 3\). Fix \(2<R<4\). Along any sequence with \(p\to\infty\) and \(X/m\le R\), the following assertions hold.

1. In the folded octave described below, every sufficiently short rank interval has **all** unordered pair sums in the strict order of the corresponding sums of \(2^{j/p}\). Endpoints can repeat within a pair. The admissible interval length is a fixed positive fraction of \(p\) depending only on \(R\).
2. Every subset \(S\) of this cycle's full shortcut state set, or of its full ordinary state set, satisfies \(E_+(S)\ll_R |S|^2\) and \(|S+S|\gg_R |S|^2\). Here \(E_+\) counts ordered ordinary integer quadruples with equal pair sums.
3. Put \(\eta=\log_2(R/2)\) and \(d=0.5753\). Then
\[
 \limsup \frac{\log p}{\log m}\le \frac{d\eta}{\gamma},
 \qquad 0<A/p-\gamma\le p^{-\gamma/(d\eta)+o(1)}.                  \tag{1}
\]
If the widths tend to \(3\), the required approximation exponent is at least \(4.7097\). At widths bounded strictly below four the exponent exceeds \(2.7550\). More generally, if \(\mu(\gamma)\le M\) in the ordinary sense of rational approximation, every growing sequence of ordinary cycles satisfies
\[
          \liminf X/m\ \ge\ \min\{4,\,2^{\,1+\gamma/(Md)}\}.        \tag{2}
\]
At \(M=3\) the right side exceeds \(3.7798\). This numerical substitution is conditional. The classical Bondareva–Luchin–Salikhov exponent \(5.116201\) leaves the unconditional width-three boundary open in (1).

The four-rank extension previously had both an exact rational counterexample and a finite integer counterexample in a wider **three-grade** chart. Three-rank midpoint order was proved earlier in that chart. Weaver's height-one source estimates include hereditary energy of exponent \(\log_2 6\) with logarithmic losses, including for the full shortcut states of one cycle. The two-grade width hypothesis here allows a bounded Sidon partition and quadratic energy for every subset of the one cycle. The argument below uses the global integer rank order as well as the source congruence. [PR213, four-rank controls and prior midpoint result](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/TETRAD_RANK.md) · [Weaver, Paper 145/v1, Theorem 7](https://rstation.ai/problems/collatz/papers/145/v1)

## A synchronized octave

Take \(v=(1-\eta)/2>0\) and \(L=2^{1-v}m\). Thus \(m>L/2\), \(X\le 2^{v+\eta}L<2L\), and \(2m=2^vL>L\). Write each odd phase \(x\) as the label \(Z=cx\in[L,2L)\), taking \(c=2\) when \(x<L\), \(c=1\) otherwise. Distinct odd phases have distinct dyadic rays. Order the labels \(Z_0<\cdots<Z_{p-1}\), and extend them and their tags by \(Z_{r+p}=2Z_r,\ c_{r+p}=2c_r\). We use the rank and angle calculation of PR213, which requires just these two grades and strict margins at both octave ends. [Rank translation and uniform angles in PR213](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md)

Indeed \(Z\mapsto 3Z+c\) strictly preserves the lifted order inside the fundamental octave by integrality and \(|c-c'|\le1\); at the right seam the incoming doubled tag is at least two. The true odd successor permutes the dyadic rays in a single cycle. The raw lifted map commutes with doubling and is a bijection of the whole ordered grid, hence translates ranks. Its translation is \(A\), since the sum of its \(p\) windings equals the native division sum after telescoping the changes in \(\log_2c\). Thus \(\gcd(A,p)=1\) and \(Z_{r+A}=3Z_r+c_r\). Multiplication of the actual odd edges yields \(0<A/p-\gamma\le1/(3m\ln2)\). Along unbounded period, \(m\to\infty\), since a fixed integer lies on at most one cycle. Hence \(\rho=A/p\to\gamma\); eventually all the calendar letters \(b(r)=\lfloor(r+A)/p\rfloor\), \(0\le r<p\), belong to \(\{1,2\}\). The true angular increments are \(\gamma+O(1/m)\) modulo one. Every weak limit of the angular empirical measures is invariant under the irrational rotation by \(\gamma\), so is Haar by its Fourier coefficients. The uniform cumulative-distribution convergence gives
\[
           \sup_{r<p} |\log_2(Z_r/L)-r/p|=o(1).                      \tag{3}
\]

Choose \(0<\epsilon<\frac18\min(v,1-v-\eta)\). For every sufficiently large candidate, all **unwrapped** tags \(c_{r+j}\), \(0\le j\le\epsilon p,\ 0\le r<p\), belong to \(\{1,2\}\). Near the right endpoint the fundamental labels exceed \(X\), so their tags are two. Near the left endpoint the fundamental labels are less than \(2m\), so their tags are one; across the seam they become two. Elsewhere the unwrapped span stays inside one fundamental octave. In fact, outside the single interval
\[
                   I_\epsilon=[v-2\epsilon,v+\eta+2\epsilon]          \tag{4}
\]
in the base position \(r/p\), all tags on this span have the **same** value at that base. To its left every label is below \(2m\) by (3); to its right the fundamental labels exceed \(X\), with the preceding seam argument for a wrap.

## The order of integer pair sums

For two distinct unordered multisets \(\{i,j\}\), \(\{k,l\}\) of offsets in \([0,\epsilon p]\), put \(P(T)=T^i+T^j-T^k-T^l\) and \(H_r=P(E)Z_r\), where \(E\) increases spatial rank. Write \(r'=(r+A)\bmod p\). The shared-register equations at all offsets give
\[
          2^{b(r)}H_{r'}=3H_r+P(E)c_r,\qquad |P(E)c_r|\le2 .          \tag{5}
\]
All \(H_r\) on fundamental bases are integers. A positive \(H_r\) forces \(H_{r'}>0\), and a negative \(H_r\) forces \(H_{r'}<0\). Transitivity around the entire cyclic rank set gives one strict sign throughout, unless all the \(H_r\) vanish. For \(\xi=2^{1/p}\), wrapping in the following sum is exact:
\[
                 \sum_{r<p}\xi^{-r}H_r=P(\xi)\sum_{r<p}\xi^{-r}Z_r. \tag{6}
\]
The polynomial \(P\) is nonzero of degree less than \(p\). Eisenstein at two for \(T^p-2\) gives \(P(\xi)\ne0\). Thus every comparison has its strict ideal sign at every fundamental origin. In particular the labels in any such consecutive span form a Sidon set.

Partition the \(p\) ranks into \(O_R(1)\) consecutive fundamental intervals as above. Split each by its common tag to transfer the Sidon property to the odd sources. Each native exponent is at most three for large \(m\), since \(2^a=(3x+1)/x'\le3R+1/m<16\). The remaining ordinary states are covered by images of these pieces under the finitely many injective affine maps \(x\mapsto(3x+1)/2^j\) for \(j=0,1,2\), using only departures on which the indicated state occurs before the next odd date. The shortcut uses a subset of the ordinary states. A disjoint refinement by deleting overlaps still has \(K=O_R(1)\) Sidon pieces. For the chosen subset write \(S=\bigsqcup S_i\). For \(F_T(t)=\sum_{a\in T}e^{2\pi iat}\), \(\|F_T\|_4^4=E_+(T)\) and \(E_+(S_i)\le2|S_i|^2\). Minkowski followed by Cauchy gives \(\|F_S\|_4\le2^{1/4}\sqrt{K|S|}\). Cauchy applied to the pair-sum multiplicities gives the sumset assertion, including the empty case directly.

## The physical binary code

Use the starts \(0\le j\le\lfloor\epsilon p\rfloor\), and put \(r_t=tA\bmod p\) with \(r_0=0\). Follow the actual **unwrapped columns** \(Z_{r_t+j}\) under the common base winding \(b(r_t)\); all of them satisfy \(2^{b(r_t)}Z_{r_{t+1}+j}=3Z_{r_t+j}+c_{r_t+j}\), including when just some of the columns have passed the end of the fundamental octave. Let \(n=\lceil\log_3(8L)\rceil+2\). Then \(B_n=\sum_{t<n}b(r_t)=\lfloor n\rho\rfloor\ge n\gamma-1\), so \(2^{B_n}>4L\).

Keep the dates \(t<n\) with \(r_t/p\in I_\epsilon\), writing \(k\) for their number. At other dates all the columns' tags are equal. We have \(k\le(\eta+4\epsilon+o(1))n\): for each fixed nonzero Fourier mode \(h\), the exponential average for the \(n\) consecutive positions is bounded by \(2/(n|1-e^{2\pi ih\rho}|)\to0\), because \(\rho\to\gamma\) is approaching an irrational number. Continuous upper and lower approximations to the interval indicator give the claim. This argument allows both the length and the rational rotation denominator to vary.

Encode each start \(j\) by the \(k\) bits \(c_{r_t+j}-1\) at retained dates, in chronological order. Suppose two unordered pairs of starts have identical coordinatewise **integer** sums of their binary vectors. Their aggregate tags agree at every one of the \(n\) dates, by the forced-date property elsewhere. Iterating the difference of the two aggregate affine maps now gives
\[
               2^{B_n}\mid 3^n(Z_i+Z_j-Z_{k'}-Z_l).
\]
The odd multiplier \(3^n\) cancels, and the absolute initial difference is less than \(2L\). Hence the initial pair sums are equal. By (5)–(6) the two unordered multisets of starts are equal. In particular the codewords are distinct (use doubled pairs), and the resulting binary code has the \(B_2\) property, allowing repeated members in a pair. This implication assumes equality of the **coordinatewise** integer sums and deduces equality of the original unordered starts. It requires no converse decoding statement for arbitrary carries outside the chosen code.

As \(\epsilon p\to\infty\), the \(k\) retained coordinates grow unboundedly by injectivity. Cohen, Litsyn and Zémor, Theorem 1, bound the unrestricted binary \(B_2\) asymptotic rate by a number strictly below \(0.5753\), so \(\log_2(1+\lfloor\epsilon p\rfloor)\le d k\) for all sufficiently large cycles. Their notion uses sums over the integers; in a binary alphabet a doubled word can coincide with no sum of two different words. Divide by \(\log_2 m\), use \(n=(\log_2 m)/\gamma+O_R(1)\), then let \(\epsilon\downarrow0\). This gives (1) after applying the true clock identity. For (2), pass to any subsequence with widths tending to a limit below four, bound it eventually by a slightly larger \(R<4\), and let \(R\) decrease to that limit. Limits below or equal to two can equivalently use \(R\downarrow2\). The lower bound on rational approximation errors at any exponent strictly greater than \(M\) gives (2). [Cohen–Litsyn–Zémor, JCTA 94 (2001), Theorem 1](https://doi.org/10.1006/jcta.2000.3127) · [Authors' conference statement of the pair convention](https://cris.tau.ac.il/en/publications/collusion-secure-fingerprinting-and-bsub2sub-sequences/) · [Della Fiore, 2026, Definition I.1 and the separate constant-weight improvement](https://arxiv.org/html/2603.27639v2) · [Classical linear-form exponent, Theorem 1](https://m.mathnet.ru/links/1d9b9977c1093c37b767dc2d807bd4a2/cheb619.pdf)
