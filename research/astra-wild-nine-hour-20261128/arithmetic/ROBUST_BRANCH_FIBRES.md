# Entropy and multiplicity of Collatz endpoints after conditioning on a complete parity bridge

**Proposed written theorem.** Let \(U_{k,p}\) be uniform on the \(k\)-bit parity words with exactly \(p\) odd departures of the shortcut \(3x+1\) map. Equivalently it is uniform on the corresponding canonical low input residues. Write \(V\) for the canonical integer endpoint, \(P_{k,p}\) for its law, and \(m_{k,p}(v)\) for the number of those inputs with endpoint \(v\). Put \(\gamma=\log_2 3\), \(f(a)=\min\{h_2(a),\gamma a\}\). All entropies in this note use bits.

For **every** sequence \(p/k\to a\in[0,1]\) and every \(\epsilon>0\), there is \(c>0\) such that for all sufficiently large clocks on that sequence
\[
 U_{k,p}\!\left(\left|-\frac1k\log_2 P_{k,p}(V)-f(a)\right|>\epsilon\right)
 \le 2^{-ck}.                                                        \tag{1}
\]
Thus a typical input has \(2^{[h_2(a)-f(a)+o(1)]k}\) companions including itself at its own affine branch. The deviation probability at **each fixed** positive error in this exponent decreases exponentially in \(k\). At \(a\) above the entropy-critical parameter, the typical multiplicity is subexponential. This permits multiple inputs on the same branch.

The conclusion survives arbitrary subexponential conditioning. Let \(A_k\) be **any** set of words on that exact row for which \(U_{k,p}(A_k)=2^{-o(k)}\), and write \(P^A_{k,p}\) for its endpoint law under uniform sampling from \(A_k\). Then (1) holds with \(U_{k,p}(\cdot\mid A_k)\) and \(P^A_{k,p}\) in place of the two original laws, with possibly a smaller \(c>0\). In particular
\[
 \frac1k H(P^A_{k,p})\longrightarrow f(a),\qquad
 \frac1k\log_2|\{V(w):w\in A_k\}|\longrightarrow f(a).             \tag{2}
\]
The fibres inside \(A_k\) have the same typical multiplicity exponent and exponential tails. This determines more than the support count in our [branch-spectrum theorem](AFFINE_BRANCH_SPECTRUM.md). A full entropy rate alone gives neither the exponential tail in (1) nor the stability in (2).

## The power sums on successive ternary blocks

Use the independent positive geometric gaps \(\Pr(g=d)=a(1-a)^{d-1}\) for \(0<a<1\), their partial sums \(S_i\), and the ternary word residue
\[
 \beta_n=\sum_{i=1}^n 3^{i-1}2^{-S_i}\pmod {3^n},\qquad
 \mu_n=\operatorname{Law}(\beta_n).
\]
The deep input is Leen’s Theorem C, \(H(\mu_n)/n\to D=\min(\gamma,h_2(a)/a)\). The primary theorem concerns projective ternary entropy at fixed odd count with independent gaps. [David Leen, version-specific record 23268832, Theorem C and §6](https://doi.org/10.5281/zenodo.23268832)

For real \(q>1\) write \(M_q(n)=\sum_z\mu_n(z)^q\) and \(H_q(n)=-\log_2M_q(n)/(q-1)\). For every \(m,n\ge1\),
\[
                             M_q(n+m)\le M_q(n)M_q(m).                \tag{3}
\]
To see the exact conditional permutation, keep the first \(n\) gaps and write \(u=\sum_{i=1}^n3^{i-1}2^{-S_i}\) in \(\mathbb Z_3\), before taking a residue. If \(z\in[0,3^n)\) is its representative modulo \(3^n\), the higher \(m\) trits of the full offset, in their usual integer order, are
\[
   \frac{u-z}{3^n}+2^{-S_n}\beta'_m \pmod {3^m}.
\]
Here \(\beta'_m\sim\mu_m\) is independent of all those first gaps. Translation and unit multiplication give a permutation. Conditional only on \(z\), the high-trit law is a convex mixture of such permutations of \(\mu_m\). There are finitely many permutations on the \(3^m\) residues, even for the infinite gap alphabet. Convexity of the power function and invariance of the counting sum under a permutation bound its \(q\)-power sum by \(M_q(m)\). Multiplying by the actual \(\mu_n(z)^q\) and summing over \(z\) proves (3). The same reasoning with Shannon entropy gives superadditivity, by concavity.

Fekete’s lemma gives \(D_q=\lim_nH_q(n)/n=\sup_n H_q(n)/n\). By monotonicity in \(q\), continuity at 1 on each **fixed finite** residue space, and the preceding superadditivity,
\[
 \lim_{q\downarrow1}D_q
 =\sup_{q>1}\sup_{n\ge1}H_q(n)/n
 =\sup_{n\ge1}H(\mu_n)/n=D.                                         \tag{4}
\]
In particular, for any \(\eta>0\) some **fixed** \(q>1\) satisfies \(H_q(n)\ge (D-\eta)n\) for all sufficiently large \(n\). For illustration this implies \(\mu_n\{\mu_n(z)>2^{-(D-2\eta)n}\}\le 2^{-(q-1)\eta n}\), by summing \(\mu_n(z)^q\). The argument provides no effective uniform rate in \(\eta\) and evaluates only the limit of \(D_q\) as \(q\downarrow1\).

## Transfer to each prescribed physical clock and any surviving subfamily

For a uniform \(k\)-bit parity word with \(p\) odd letters at positions \(0\le i_1<\cdots<i_p<k\), the distances of its odd departures from the right endpoint are \(k-i_p,\ldots,k-i_1\). Their successive positive differences are \(g_1,\ldots,g_p\). Adjoin \(g_{p+1}=i_1+1\). This is a bijection with the positive compositions of \(k+1\) into \(p+1\) parts. Under any geometric parameter these compositions are equiprobable conditional on \(S_{p+1}=k+1\). The complete extra gap records leading even letters and contributes no term to \(\beta_p\). For the shortcut odd branch \((3x+1)/2\), the formal intercept is \(\sum_{i:w_i=1}3^{\#\{j>i:w_j=1\}}2^{-(k-i)}\). The canonical integer endpoint lies in \([0,3^p)\) and so is exactly the representative of \(\beta_p\). The binary prefix dictionary and the bound on the canonical endpoint are in [Wren, paper 64 v2, Lemmas 4–5](https://rstation.ai/problems/collatz/papers/64/v2).

The conditioning probability under the one **fixed** parameter \(a\) is
\[
 \Pr(S_{p+1}=k+1)=\binom{k}{p}a^{p+1}(1-a)^{k-p}=2^{-o(k)}
 \quad\text{whenever }p/k\to a\in(0,1).                             \tag{5}
\]
This follows from the binomial entropy estimate. No central-limit window or approximation rate of \(p/k\) to \(a\) is required. Including \(A_k\) multiplies (5) by \(U_{k,p}(A_k)=2^{-o(k)}\). Denote the combined probability by \(b_k\). For the conditioned endpoint law \(P\), cellwise \(P(v)\le\mu_p(v)/b_k\). Thus
\[
             H_q(P)\ge H_q(p)+\frac{q}{q-1}\log_2 b_k .
\]
Choose \(q\) from (4) for a sufficiently small \(\eta\) and let \(k\to\infty\). For each \(\epsilon>0\) this gives \(H_q(P)\ge [f(a)-\epsilon/2]k\) eventually. Summing \(P(v)^q\) over the cells with \(P(v)>2^{-[f(a)-\epsilon]k}\) gives the heavy-cell bound \(2^{-(q-1)\epsilon k/2}\). At the other end, there are at most \(\min(\binom{k}{p},3^p)=2^{[f(a)+o(1)]k}\) possible cells. Summing the probabilities of those below \(2^{-[f(a)+\epsilon]k}\) gives \(2^{-[\epsilon-o(1)]k}\). This proves (1) and its conditioned version. At \(a=0,1\), even the total number of words is \(2^{o(k)}\). Every nonempty subfamily then has all its occupied cell probabilities at least \(2^{-o(k)}\), proving the endpoint cases. For any row/subfamily the self-information is at most \(k\), so (2) follows. Each conditioned fibre has exactly \(|A_k|P(v)\) elements.

The Shannon conclusion also holds under an arbitrary word law \(Q_k\) of relative entropy \(D(Q_k\Vert U_{k,p})=o(k)\). The binary relative-entropy inequality transfers each exponentially rare event in (1) to an event of \(Q_k\)-probability \(o(1)\). Since \(-\log_2P_{k,p}(V)\le k\), its \(Q_k\)-expectation divided by \(k\) tends to \(f(a)\). Subtracting the output divergence, at most \(D(Q_k\Vert U_{k,p})\) by data processing, gives the entropy rate of the \(Q_k\)-output. This variant asserts a Shannon rate and permits rare spikes under \(Q_k\).

## Exact fractional moments of the unconditioned branch law

Let the \(k\) shortcut parity letters be independent Bernoulli\((\pi)\), \(0<\pi<1\), and let \(P_{k,\pi}(p,v)\) be the law of the grade and canonical endpoint together. For every \(0\le q<1\),
\[
 \lim_{k\to\infty}\frac1k\log_2\!\sum_{(p,v)\ {\rm occupied}}P_{k,\pi}(p,v)^q
    =\max_{0\le t\le1}\left\{(1-q) f(t)-q\,D_2(t\Vert\pi)\right\}.  \tag{7}
\]
Here \(D_2\) is binary relative entropy in bits, and the occupied-atom convention includes the branch count at \(q=0\). For \(0<q<1\) the maximizer is unique. If \(t_*\) denotes the interior meeting point \(h_2(t_*)=\gamma t_*\), set
\[
 t_-=\frac{\pi\,3^{(1-q)/q}}{1-\pi+\pi\,3^{(1-q)/q}},\qquad
 t_+=\frac{\pi^q}{(1-\pi)^q+\pi^q}.
\]
The maximizing grade fraction is \(t_-\) when \(t_-<t_*\), \(t_+\) when \(t_+>t_*\), and \(t_*\) otherwise. In particular the critical grade remains exactly maximizing throughout a nonempty interval of orders adjacent to zero for every fixed input bias \(\pi\). Under weights proportional to \(P_{k,\pi}(p,v)^q\), the chance of a grade fraction outside any fixed neighborhood of this maximizer decays exponentially.

Indeed on each uniform word row the Rényi entropy of order \(q<1\) lies between the Shannon entropy and the logarithm of the occupied support. These bounds have common limiting rate \(f(t)\) for every sequence of grades converging to \(t\). Compactness and continuity give uniformity after subtracting \(f(p/k)\). The grade mass has logarithm \(-kD_2(p/k\Vert\pi)+O(\log(k+1))\) uniformly by the binomial bounds. Summing the resulting \(k+1\) terms proves (7). Its objective is strictly concave for \(q>0\) because \(f\) has a linear left branch, a strictly concave right branch, and a downward jump in derivative at \(t_*\). Differentiation on either open branch gives \(t_-\) and \(t_+\), respectively. The probability assertion follows by the strict maximizer gap on a compact closed complement. No positive-order moment at \(q>1\) is evaluated by (7).

## Full physical no-descent in an arbitrarily slowly widening band

Fix **any** sequence \(R_k\to\infty\). In **every** interval \(I_k\) of exactly \(2^k\) consecutive positive integers, count **distinct integer endpoints at time \(k\)** of all starts \(x\) with
\[
                    x\le T^j(x)\le R_k x\quad (0\le j\le k).
\]
Their number is
\[
                        2^{[h_2(1/\gamma)+o(1)]k}.                    \tag{6}
\]
The error in the exponent is uniform over the interval location for a prescribed \(R_k\). If the start is sampled uniformly from the entire band-surviving family across all grades, its unmarked endpoint self-information divided by \(k\) tends to \(h_2(1/\gamma)\), with the convergence uniform even over the individual survivors. In the canonical grade \(p=\lceil k/\gamma\rceil\) the same exponent holds for the endpoint entropy of a uniform start passing that whole physical test. Its atypical endpoint information has exponentially small probability as in (1).

Here is a direct subexponential lower bound on the whole-prefix event at this grade. For any interior row with \(p/k\to a\), put \(P_j=\sum_{i<j}w_i\). Choose integers \(b=b_k\to\infty\), \(b=o(k)\). Split the word into consecutive blocks of length \(b\), followed by a possibly shorter block. At every block boundary \(t\) prescribe \(P_t=\lfloor tp/k\rfloor\). The choices on the full blocks are independent as a counting matter. Each full block has quota \(bp/k+O(1)\). Stirling’s estimate, uniformly on a fixed compact interior interval, gives at least \(2^{b h_2(p/k)-O(\log(b+1))}\) choices there. The last block always has an admissible quota. Their joint count is \(2^{[h_2(a)-o(1)]k}\). Within each such word, \(P_j-jp/k\) lies in \([-b-1,b+1]\). Rotate the word to start at a minimum of this centered walk. The total centered increment is zero, so every new partial sum lies in \([0,2b+2]\). Each rotated word has at most \(k\) preimages. This constructs a fraction \(2^{-o(k)}\) of the row satisfying the two barriers throughout.

Now put \(p=\lceil k/\gamma\rceil\) and \(G_j=3^{P_j}/2^j\). Choose \(b\to\infty\) slowly enough that \(2\cdot 3^{2b+3}\le R_k\) eventually. The constructed words have
\[
 1\le G_j\le 3^{2b+3},\qquad
 T^j(x)=G_j\left(x+\sum_{\substack{i<j\\w_i=1}}\frac{1}{3G_i}\right).
\]
The identity uses the original physical start on its compatible cylinder. Each word has exactly one compatible start in the given interval. After omitting at most \(k\) starts with \(x<k\), one has \(1+k/(3x)<2\). Since each \(G_i\ge1\), the rest of the constructed family satisfies the full physical test, uniformly in the interval location. In particular, the set of all grade-\(p\) words passing that test occupies fraction at least \(2^{-o(k)}\) of the row. Apply the conditioned theorem. On this arbitrary interval, the quotient \(\lfloor x/2^k\rfloor\) takes at most two integers. At fixed \(p\) the actual endpoint is \(3^p\lfloor x/2^k\rfloor+V\). Its residue modulo \(3^p\) recovers \(V\), so the integer endpoint law splits each canonical atom into at most two. Heavy atoms are still exponentially rare by the power-sum bound since splitting only decreases the \(q\)-power sum. The light-tail proof pays at most a factor of two in the support bound. This proves the physical entropy assertion and the lower rate in (6), with constants independent of the interval location.

For the upper bound, multiply all actual one-step ratios to get \(T^k(x)/x=G_k\prod_{i<k:w_i=1}(1+1/(3T^i(x)))\). All the intermediate states are at least \(x\), and \(T^k(x)\ge x\). Hence \(G_k\ge e^{-k/(3x)}\), giving \(p\ge k/\gamma-O(1)\) whenever \(x\ge k\), with an absolute constant. This threshold exceeds \(k/2\) for large \(k\). There is one representative of each word in the interval, so the sum of the binomial counts at all such grades is \(2^{[h_2(1/\gamma)+o(1)]k}\). The discarded \(x<k\) add at most \(k\). This completes (6). There is an elementary proof of the whole physical conclusion, including the input-weighted endpoint law. For any physical survivor with \(x\ge k\) and every \(j\le k\), the same product identity gives \(G_j\ge e^{-1/3}\). Write \(C_w=2^k d(w)\) for the integer numerator of the full formal intercept. Its real normalized value satisfies
\[
          0\le C_w/3^p=\sum_{\substack{i<k\\w_i=1}}(3G_i)^{-1}
                         \le e^{1/3}k/3 .
\]
Within a fixed grade, equal unmarked integer endpoints imply equal \(C_w\bmod3^p\). Distinct input words at fixed \((k,p)\) have distinct numerators because \(C_w\) specifies the compatible low input \(r\equiv-3^{-p}C_w\bmod2^k\), hence the parity word. Each normalized numerator therefore occupies a distinct point of one translate of \(\mathbb Z\). There are at most \(1+\lfloor e^{1/3}k/3\rfloor\) such points. At fixed actual endpoint \(y\), a word also identifies its unique ordinary input \(x=(2^k y-C_w)/3^p\). This step needs no interval restriction. Summing over the \(k+1\) grades and adding the \(x<k\) gives \(O(k^2)\) inputs per **unmarked** output, uniformly over all positive sources in the full no-descent family and every subfamily, even without an upper ceiling. Thus the corridor source count alone proves (6) without importing Leen. On a uniform survivor family of cardinality \(J\), each observed endpoint has information between \(\log_2 J-O(\log k)\) and \(\log_2 J\). The lower and upper source counts above identify its uniform limit, with or without the upper ceiling \(R_k\). The same polynomial fibre bound also gives the fixed-grade physical assertion directly. This shortcut uses the actual source-relative floor. The all-slope theorem (1)–(2) applies to arbitrary filters.

**Prior comparisons and remaining gap.** The exact first-window entropy of no-descent *starts* and the cyclic-minimum lower construction are prior. Weaver’s first-window theorem already obtains a \(k^{-3/2}\) factor for the number of labelled images of a symmetric logarithmic-boundary family, with a matching lower bound on the distinct integer endpoints of the central grade. Its proof uses actual coefficient-positive bridges, the same normalized correction, its bounded conditional mean on that family, and Rees’s earlier affine-offset comparison. The unconstrained-height first-window lower exponent is already present there. Here the physical ceiling may diverge arbitrarily slowly, and the input-weighted endpoint statement is uniform through that confinement. Paper 184 treats the random last state before descent conditioned on a previous smaller-orbit-meeting barrier, with a different clock and an exact small-precision dimension. PR215 gives almost-sure tilted fusion multiplicity under iid sampling and stronger central exact-clock mean-fibre conclusions on a restricted slope range. The present all-grade statement supplies exponential probability tails under each individual clock, and their stability under **any** subexponential word filter. Formula (6) concerns ordinary starts and their distinct endpoints with the same original-source floor and upper ceiling on every date. One fixed supplied integer specifies a single word at each length. Its membership in these growing finite populations is uncontrolled. No descent theorem for such an integer follows. [Repository fixed-height results](../../integrated/exceptional-mass/README.md) · [Weaver, paper 28 v2, §6 and Proposition 4](https://rstation.ai/problems/collatz/papers/28/v2) · [Weaver, paper 184 v1](https://rstation.ai/problems/collatz/papers/184/v1) · [PR215, exact-clock fusion and tilt](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase11/COLLISION_CLOCK_LIMITS.md)

[Finite control script](check_robust_fibres.py) · [Review and replay](../../../reports/astra-wild-nine-hour-20261128/arithmetic/ROBUST_FIBRE_REVIEW.md)
