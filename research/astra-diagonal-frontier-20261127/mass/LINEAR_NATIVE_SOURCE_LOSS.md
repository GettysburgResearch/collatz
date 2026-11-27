# Linear-delay loss in every original dyadic interval

Write \(T(x)=x/2\) for even \(x\), \(T(x)=(3x+1)/2\) for odd \(x\), and let \(Q_j(x)\) count odd departures before shortcut time \(j\). Fix
\[
  \tfrac12<p\le\alpha=\log_3 2,\qquad R=1/p,\qquad
  \lambda=\log_2 3,\qquad h=H_2(p).
\]
Let \(W_K(p)=\{x: Q_j(x)\ge pj\ (1\le j\le K)\}\). The case \(p=4/7\) is the native gate in the principal reciprocal-mass problem. Time here is shortcut time. The actual starting integer is retained throughout.

### Count and rate

For each \(d\in(h,1)\) there is a constant \(\delta_d>0\) such that, on every fixed band \(0<\delta_1\le b/L\le\delta_2<\delta_d\), eventually uniformly for every integer interval \(I\) of \(2^L\) consecutive positive integers,
\[
 \#(I\cap W_{L+b}(p))\ \le\ C(L+b)\,2^{hL-(d-h)b}.                 \tag{1}
\]
In fact the upper bound counts the larger set with first departure odd and \(Q_{L+b}(x)\ge p(L+b)\), without its intermediate restrictions. Constants can depend on \(p,d,\delta_1,\delta_2\). The eventual threshold is ineffective.

For \(p=4/7\), on the very same interval the initial count is
\[
 \#(I\cap W_L)=2^LP_L\asymp L^{-3/2}2^{hL}.                     \tag{2}
\]
This follows from the parity-vector bijection and the weak ballot estimate in NATIVE_SOURCE_SHELL_LOSS.md. Consequently every initial interval retains at most \(C L^{5/2}2^{-(d-h)b}\) of its original population after the \(b\) further physical steps. If \(\max I/\min I\le A\), the same bound multiplied by \(A\) holds for reciprocal mass. In particular this applies to every original octave \([2^L,2^{L+1})\) and to every translated interval \(q2^L+[0,2^L)\), \(q\ge1\). The dyadic source shell \([2^{L-1},2^L)\) at depth \(L\) also satisfies this conclusion, by (1) for the encompassing interval and the initial reciprocal mass \((1+o(1))(\log2)P_L\) from NATIVE_SOURCE_SHELL_LOSS.md. Longer follow-up times retain its resulting upper bound by inclusion.

In particular the global count of physically permanent positives of size at most \(X\) is \(O(X^{h-\eta})\) for some \(\eta>0\) at the *specified* \(4/7\) gate: apply (1) once at a fixed small \(b/L\) and use \(L=\lceil\log_2(X+1)\rceil\). Earlier critical, real-source R4 estimates give a stronger numerical exponent for permanent paths at slopes sufficiently close to \(\alpha\); those paths are a smaller set.

There is a sharp derivative in (1). Put \(b=\lfloor\delta L\rfloor\) and, for \(p=4/7\),
\[
 F(\delta)=\limsup_{L\to\infty}L^{-1}\log_2
  \max_{0\le q<2^b}\#\{x\in q2^L+[0,2^L): x\in W_{L+b}(p)\}.
\]
Including \(x=0\) in a test interval contributes zero. Averaging these \(2^b\) counts gives exactly \(2^L P_{L+b}\). Thus \(F(\delta)\ge h-(1-h)\delta\) for every \(\delta>0\). By (1), \(F(\delta)\le h-(d-h)\delta\) for all sufficiently small fixed \(\delta>0\). Now take \(d\uparrow1\), *after* taking the large-\(L\) limits. This proves
\[
 \lim_{\delta\downarrow0}\frac{F(\delta)-h}{\delta}=-(1-h).       \tag{3}
\]
Replacing inner \(\limsup\) by \(\liminf\) gives the same derivative. For each fixed \(d\) and sufficiently small fixed \(\delta\), at least \(c L^{-5/2}2^{d b}\) of the high parts achieve at least half the fair mean. Indeed the other blocks contribute at most half of the total; divide the remainder by (1). Such a lower bound locates many physical intervals within a full period. It gives no such lower bound on a particular specified interval.

### Original composition law

Use \(r\) independent positive geometric holdings of parameter \(p\), with \(E_j=e_1+\cdots+e_j,\ E_0=0,\ S=E_r\). Each word codes the bits \(10^{e_1-1}\cdots10^{e_r-1}\) and a unique positive source \(m\in(0,2^S)\). The endpoint may be even after the last truncated gap. For every \(d<1\) there exists \(v_d>0\) such that, on each band \(0<c_0\le b/r\le v<v_d\),
\[
  \sup_{|J|\le2^{-b}}\Pr_p\{m/2^S\in J\}\ \le\ C r\,2^{-d b}.   \tag{4}
\]
Here \(J\) is any real or circular interval of the indicated length. No assertion of independence between \(m,S\), conditional uniformity, or detection of a prescribed exact endpoint is needed.

To deduce (1), put \(K=L+b,\ z=p/(1-p)>1\). Reduction modulo \(2^K\) injects the test interval into one circular interval of relative length \(2^{-b}\). Each \(K\)-bit word with first bit one and \(r\ge pK\) has probability \(w_{K,r}=p^r(1-p)^{K-r}\) in the corresponding \(r\)-holding law, at total exactly \(S=K\). On that event the normalized source is precisely its canonical representative divided by \(2^K\). Bound the count by
\[
 \sum_{r=\lceil pK\rceil}^K w_{K,r}^{-1}
 \Pr_p\{S=K,\ m/2^S\in I/2^K\bmod1\}
 \le C K2^{-db}2^{hK}
       \sum_{r=\lceil pK\rceil}^K z^{-(r-pK)}.
\]
The sum is bounded independently of \(K\). The chosen \(b/L\) band can be made to place all \(b/r\) in one allowed compact band since \(pK\le r\le K\). This is an upper bound inside the original trajectory count, with the exact clock dropped only after its source interval has been identified.

### Parameter extension of the real-source entropy estimate

The primary input is lyapunov_weaver, *A power improvement for uniform Collatz interval compression*, Paper 28 v3, sections 7.2–7.11, especially (M8)–(M11), (M19)–(M34) and (R5)–(R15). Section 7.11.5 reports that external review of its real-source argument is pending. The extension here is a written mathematical deduction with an ineffective Subspace Theorem threshold, and has no accompanying formal proof. The stated real-source theorem there uses \(p=\alpha\). We detail its extension to the indicated fixed \(p\). Its arithmetic separation lemma (R6), signed parity/composition entropy lemma (M9), entropy triangle and bounded-product lemma are used with their original hypotheses. [Paper 28 v3](https://rstation.ai/problems/collatz/papers/28)

**Raw coordinate and unconditional separation.** Let
\[
 Z=\sum_{i=1}^r2^{E_{i-1}}[-3^{-i}]_{2^{S-E_{i-1}}}.
\]
Brackets denote least residues. The canonical source is \(m=[Z]_{2^S}\), with \(0<Z<r2^S\), by the word identity (J1), (J7)–(J8). For a chunk of \(\ell\) holdings starting after \(k\) letters put \(n=k+\ell,\ t=S-E_k,\ F_j=E_{k+j}-E_k\). Its unwrapped normalized source contribution is \(U/2^t\), where the raw duality identity (J9)–(J10) is
\[
 2^t V-3^n U=B,\quad B=\sum_{j=1}^{\ell}3^{\ell-j}2^{F_{j-1}},
 \quad 0<U<\ell2^t,\quad 0<V<\ell3^n.                           \tag{5}
\]
After conditioning all selected coarse totals and all exterior letters, \(S,t,n\) and all chunk boundaries are fixed. Unwrapped chunk contributions add exactly and their internal coarse words are independent uniform compositions.

Fix a small \(\varepsilon>0\), a large constant coarse length \(A\), and use chunks of
\[
 \ell=A\left\lfloor(1-\varepsilon)b/(RA)\right\rfloor .
\]
With \(|F_j-Rj|\le\varepsilon b/4\) for every \(j\), the important off-critical estimate is
\[
 B\le\ell\,2^{R\ell+\varepsilon b/4}
   \le2^{(1-\varepsilon/2)b}.
\]
Indeed \(R\ge\lambda\) so \(\lambda(\ell-j)+R(j-1)\le R\ell\). No critical cancellation between the ternary power and the mean holding time is assumed.

Use chunks well inside the middle half of the \(r\) letters. With \(b/r\) sufficiently small one has \(n\ge r/4-O(1),\ t\ge r/4-O(1)\) even using only \(e_i\ge1\); hence \(2^t,3^n\ge2^b\). Treat \(S>C_0r\) separately. Given two signed sums of a fixed number \(j\) of copies of the same chunk with equal quantized source outputs \(\lfloor2^b\sum\pm U/2^t\rfloor\), the difference coefficient \(u\) obeys \(|u|<2^{t-b}\), and the difference of endpoint coefficients \(v\) has \(|v|\le2j\ell3^n\). By (5) their numerator difference \(D\) is \(2^t v-3^n u\), with \(|D|\le2j\,2^{(1-\varepsilon/2)b}\) for retained words. As \(b\ge c_0r\), a nonzero \(D\) violates (R6), setting its \(s=r,p=b,h=0,m=t\) and using its second small-coefficient alternative. Its upper exponent and coefficient bounds hold since \(S\le C_0r\), \(n\le r\), and \(j\) is fixed. Its positive exponential margin can be chosen after \(c_0,\varepsilon\) are fixed. Thus a quantized signed *sum* determines its integer signed numerator on retained tuples. The arithmetic bound is ineffective. Quantization precedes reduction to the circle, so no discarded integer carry enters this inference.

**Conditional information.** For \(j\) independent signed copies let
\[
 h_j=H_2((1-(1-2p)^j)/2).
\]
In a coarse block conditioned on total \(a\), the remaining \(A-1\) ones after the starting one are a uniform subset of \(a-1\) places. If \(a'/n'\) denotes the remaining-one fraction after each successive exposed position, sum the expected binary XOR entropies of the \(j\) independent conditional copies, as in (M8), to obtain \(g_{A,j}(a)\). The entropy of the signed numerator sum modulo \(2^{F_\ell}\) is at least the sum of these budgets over the chunk, by the triangular numerator-bit identity and the chain rule (M9). The sign and all known carries affect the next XOR only by complementation. Here \(0\le g_{A,j}(a)\le a\), and under the stated \({\rm Geo}(p)\) law
\[
 \mathbb E g_{A,j}(a)/A\longrightarrow R h_j\qquad(A\to\infty).
\]
Indeed \(a/A\to R\) in probability and in \(L^2\). Away from a terminal fraction \(\xi\) of the slots the remaining-one fractions have mean \((A-1)/(a-1)\to p\) and variance \(O_\xi(1/a)\), as in (M11). Continuity of the finite XOR entropy, then \(\xi\downarrow0\), and uniform integrability prove the limit. This proof works simultaneously for any chosen finite set of copy counts.

Take a depth \(s\) and a group of \(2^s\) independent chunks. The distinct copy counts needed are \(j=2^i,\ 0\le i\le s\). For every fixed small \(\zeta>0\), choose \(A\) large. With exceptional probability \(Ce^{-a_0 b}\) per group, outside the exception the sum of budgets in every chunk is at least \(\ell(R h_j-\zeta)\) for each selected \(j\). This follows by exponential Markov since the independent coarse totals have exponential moments and \(g\le a\). The unconditional strip failure has probability \(Ce^{-a_1 b}\) by exponential tails for centered \(F_j-Rj\), a union over \(j\le\ell\), and \(\ell\asymp b\). Thus conditional strip-failure probability given the local totals is at most \(e^{-a_1 b/2}\) outside another exceptional set of probability \(Ce^{-a_1 b/2}\) (decrease \(a_1\) to absorb constants). On these environments \(F_\ell=O(b)\). The signed numerator alphabet has logarithm \(O_s(b)\) even on a strip-failing tuple, since \(B\le\ell 3^\ell 2^{F_\ell}\). The elementary entropy trimming bound (M22) and the exact sum decoder (5) therefore give conditional Shannon entropy of each required signed, quantized output at least \(\ell(R h_j-\zeta)-o(1)\).

For independent real random variables, \(Q_b(x)=\lfloor2^bx\rfloor\) obeys
\[
  2H(Q_b(X+Y))\ge H(Q_b(X-X'))+H(Q_b(Y))-3
\]
with \(X'\) an independent copy of \(X\), by the discrete entropy triangle and the one-bit rounding uncertainties (R9). Descending the balanced tree of these \(2^s\) *actual* chunks gives a group entropy lower bound
\[
  \ell\,(R D_s-\zeta)-O_s(1)-o(1),\qquad
 D_s=2^{-s}\sum_{i=0}^s\binom si h_{2^i}\longrightarrow1 .
\]
Indeed \(h_{2^i}\to1\), and a \({\rm Bin}(s,1/2)\) index diverges in probability as \(s\to\infty\). Each differenced law at a leaf uses copies conditioned on the same local environment. The depth is fixed before the arithmetic limit.

**From group entropy to every cell.** Choose \(d<d_1<D<D_s\), then \(A\) large and \(\zeta,\varepsilon\) small enough to secure group entropy \(>Db\) on the retained environments. For completeness the local upper-tail exclusions and the order of limits are as follows. The conditional entropy of a single coarse input of total \(a\) is \(\log_2\binom{a-1}{A-1}\le a\). Since \(p>1/2\), its fixed-\(A\) sum of geometric holdings has \(\mathbb E2^a<\infty\). Discarding coarse factors with total \(a>M\) therefore removes at most \(\xi b\) bits of input entropy except with probability \(Ce^{-a_2 b}\), for a sufficiently large fixed \(M\), by the exponential Markov argument (M31)–(M32). Indeed the exponential moment of the discarded input budget tends to one as \(M\to\infty\), while the number of factors is proportional to \(b\). Removing their *aggregate* from the independent group sum costs at most their total input entropy plus one rounding bit (R11). Each of the remaining \(O(b)\) independent slots, including trivial replaced slots, has cardinality at most \(2^M\); the logarithm of the full quantized group support is \(O(b)\) since the raw group lies in \([0,r]\) and \(b\ge c_0 r\). In fact it lies in \([0,2^s\ell]\), which makes these local constants independent of \(b/r\). The bounded-product blowing-up lemma (R12)–(R13) now bounds its fixed-order Rényi entropy below by its Shannon entropy minus \(\xi b+O(1)\), for a sufficiently small fixed order increment \(\beta-1>0\). Reconvolving the aggregate costs at most one Rényi bit by (R11). Choose \(\xi\) with strict slack in \(D-d_1\). Thus on locally good coarse totals each group has quantized Rényi entropy at least \(d_1 b-O(1)\), uniformly in all retained *exterior* clocks. The analytic local bad probability \(Ce^{-a b}\), its exponent \(a>0\), and \(\beta\) depend only on the fixed single-group choices and \(p\), not on the number of groups or the chosen precision band. The eventual arithmetic threshold can depend on that band.

For \(K_0=\lceil\beta/(\beta-1)\rceil\) good groups, their conditional quantized laws satisfy \(\|\nu_i\|_{K_0/(K_0-1)}\le C2^{-d_1b/K_0}\) by Rényi monotonicity. Young's counting-measure inequality on \(\mathbb Z\) gives maximum convolution atom \(C2^{-d_1b}\). The quantized real sum differs from the sum of the \(K_0\) quantizations by an integer in \([0,K_0-1]\), so multiply by \(K_0\). Reconvolving all remaining independent groups and shifting by the exposed exterior increases the maximum by at most a factor two (R11), (R14).

Take a fixed number \(G\ge K_0\) of disjoint groups with \(a(G-K_0+1)>2\log2\). Their local bad conditions are functions of disjoint vectors of coarse totals. Before imposing any exact clock those vectors are independent, so the chance that fewer than \(K_0\) are locally good is \(O(2^{-2b})\) by the binomial union bound. Now choose \(v_d>0\) so small that these \(G2^s\) chunks fit in the middle half and \(b\le v_dr\) ensures \(t,\lambda n\ge b\). All exterior words are exposed. A Chernoff bound under the original geometric law gives \(\Pr(S>C_0r)\le2^{-2b}\) for a sufficiently large fixed \(C_0\). The two exceptions are simply added. Conditioning on the complete environment now fixes \(S\); a chosen set of good groups remains conditionally independent, without any assertion of independence of the clocks after this conditioning. Mixing gives the unwrapped maximum-cell bound \(C2^{-db}\). Finally \(m/2^S=Z/2^S-\lfloor Z/2^S\rfloor\), with carry in \(\{0,\ldots,r-1\}\). A canonical interval lifts to at most \(2r\) unwrapped grid cells, up to an absolute factor for wrap, giving (4). No independence of the carry is required. This proves (1)–(3).

### Fixed old sources

At fixed \(x\) and \(K\to\infty\), its normalized source lies within \(O_x(2^{-K})\) of zero. The original cell theorem requires \(b/r\) in a small positive constant band, while locating this particular atom requires \(b=K-O_x(1)\) and \(r\le K\). The ratio loss is global within an expanding octave. It permits a persistent individual source in each indicated upper bound. The near-optimal rate (3) is for the largest period block; its existential lower bound also does not locate a given physical atom.

### The ideal band and the inverse-tree counting ceiling

Here is a compatibility calculation beyond the proved small band. Put \(\tau=1/p>\lambda\). If a dimension-one source upper estimate could reach the maximal real-exponent boundary \(b/r\uparrow\lambda\) for the dominant \(r\sim pK\), then \(b/K\to\lambda p\) and \(L/K\to1-\lambda p\). The formal original-interval count exponent would be
\[
   d_*=\frac{h-\lambda p}{1-\lambda p}
       =1-\frac{I(\tau)}{\tau\log2-\log3},\qquad
   I(\tau)=\tau(\log2)\bigl[1-H_2(1/\tau)\bigr],
\]
where the unmarked log is natural. This is exactly the counting ceiling for the return-branch normalization of retained inverse trees. Indeed at fixed inverse odd-clock length \(r\) and holding total \(K\sim\tau r\) there are \(2^{Kh+o(K)}\) compositions, a specified ordinary ternary class costs \(3^{-r}\) on average over roots, and the inverse height scale is \(2^K/3^r\). Dividing the logarithms gives \(d_*\). At \(p=4/7\), \(d_*=0.84336431385\ldots\). This matching of hypothetical exponents does not extend the arithmetic band or give a lower bound at a specified root. The exact same-source lower results closest to slope two allow losses in their constants.

### Higher odd fractions

The same real-source calculation gives a linear-delay gain at every fixed \(p\in(\alpha,1)\), even for this faster-growth fraction. Put \(R=1/p<\lambda\). In the chunk length replace \(R\) by \(B_0=\lambda\); center the strip at \(Rj\) as before. Then \(\lambda(\ell-j)+R(j-1)\le B_0\ell\), giving exactly the required (5) decoding margin. The entropy budget remains \(R h_j\) per holding, so the group rate becomes \((R/\lambda)D_s\). All support, coarse local failure, order selection, central placement and maximum-cell arguments are otherwise identical for this fixed \(p>1/2\). Thus (4) is valid for every \(d<1/(\lambda p)\). The exact-total sum still gives (1) for \(h<d<1/(\lambda p)\).

This interval is nonempty. Binary relative entropy, or two integrations of \(H_2''(p)=-1/(p(1-p)\log2)\le-4/\log2\), gives \(pH_2(p)\le p[1-2(p-1/2)^2/\log2]\). On \([1/2,1]\) the right side has maximum at \(p=(2+\sqrt{1+6\log2})/6\), with value less than \(0.620\); for example \(0.69314<\log2<0.69315\) gives this strict rational margin. Since \(1/\log_2 3>0.630\), one has \(H_2(p)<1/(\lambda p)\). Only the smaller upper dimension is obtained by this calculation at these larger odd fractions; (3)'s matching one-sided derivative was stated at \(4/7\).
