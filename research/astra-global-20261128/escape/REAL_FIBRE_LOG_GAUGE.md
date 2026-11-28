# Logarithmic neighborhood bounds for the actual null real fibres

**Source-qualified written deductions.** The lower bound uses the predecessor clock CLT of Leen and the certified first-landing lower count of Weaver. The typical upper gauge uses the all-event first-landing bound, elementary finite geometric-clock deviations, and the earlier joint landing/terminal construction of PR145. Weaver, Paper 175, Theorem 1 supplies the complementary zero-carrier theorem below exponent one half. The null support and its full dimension are previous results. PR193 already proves the same neighborhood order at the terminating target 1 and for an escaping component, there with explicit charge constants. The first part here gives one elementary proof for all fixed odd unit targets. [PR193, critical support neighborhoods](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/CRITICAL_SUPPORT_NEIGHBORHOODS.md).

## A lower bound at every sufficiently small scale

Fix a positive odd unit $a$. Write $b_a(x)$ for the product of $3u/(3u+1)$ up to the first odd visit of $x$ to $a$, if this visit exists. Let $K_a$ be the support of the limiting ordinary first-arrival product on these predecessors. The same support arises on weighting by the product, since the product stays in $[c_0,1]$ on every simple path with an absolute $c_0>0$. Then, as $r\downarrow0$,
\[
       \operatorname{Leb}\{t:\operatorname{dist}(t,K_a)<r\}
             \gg_a (1+\log(1/r))^{-1/2}.                              \tag{1}
\]
It applies in particular at the known terminating target $a=1$. Each $K_a$ has Lebesgue measure zero by the finite-union reduction to minimum residue supports in [PR145, complete integer fibre](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/terminal-residue/SUPPORT.md). Its normalized residue and product coordinates differ by a bi-Lipschitz transformation on this compact range.

Every finite first-arrival product from an odd **unit** $x$ belongs to $K_a$. Take a fixed large $M\ge\max(x,a)$. Arbitrarily distant uniform source octaves contain a proportion $\gg1/M$ that first enter $[1,M]$ at $x$ with accumulated log correction $O(1/M)$. Their subsequent first arrival at $a$ is exactly the prescribed one since no earlier state before $x$ could equal $a$. Pass to the limiting first-arrival law and then let $M\to\infty$. This also works for a periodic $a$ and for $x=a$. [Controlled first landing, PR145](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md).

The unweighted predecessor density of $a$ is positive by the same lower count with $x=a$. The first-arrival odd-clock central limit theorem gives $\gg_a X$ odd sources in $[X,2X]$ that hit $a$ at grades $j$ in a window of $O_a(\sqrt{\log X})$ centered at $(\log X)/D$, $D=\log(4/3)$. The use of a proportional interval and the removal of even source lifts are justified in [the fixed-target clock argument](ORDINARY_PRODUCT_TRANSITION.md). If an original $x$ is divisible by three, replace it by $x'=4x+1$. It is an odd unit, $U(x')=U(x)$, and for large $X$ neither source equals $a$; hence its first-arrival grade is still $j$. Use the identity map on unit sources. The combined map has multiplicity at most two and all resulting unit sources lie in $[X,8X+1]$.

Write $s$ for the native clock on such a source. The product mark is $3^j2^{-s}x/a\in[c_0,1]$. For each fixed $j$, this restricts $2^s$ to a factor interval of bounded ratio, so there are $O(1)$ values of $s$. For each pair $(j,s)$ the marks of distinct sources are separated by $3^j2^{-s}/a\gg 1/X$. Thus, surrounding the marks of that cell by disjoint intervals of radius $c/X$ for a sufficiently small absolute $c$ bounds the number of its sources by $O(X\operatorname{Leb}((K_a)_{1/X}))$. Summing over $O_a(\sqrt{\log X})$ pairs proves (1) with $X=1/r$. The lower bound also passes to the support of the escaping component's stationary product law at any of its unit anchors, since that law contains a positive dilate and a positive scalar multiple of the first-arrival product submeasure by [the canonical path identity](SPATIAL_TRACE_TAIL.md).

## The critical logarithmic Hausdorff exponent

Write $m(n)$ for the least ordinary value visited and $R(n)$ for the sum of $\log_2(1+1/(3u))$ at odd departures before its first visit. Denote their limiting natural pair by $(m,R)$. Put $h_s(r)=r(1+\log(1/r))^s$ for sufficiently small $r$. For **each $s>1/2$** and any centers $a_m\in\mathbb R$, the law of $R-a_m$ is exhausted by an increasing sequence of restricted history measures satisfying
\[
                  \nu_K(I)\le C_{s,K}h_s(|I|)                         \tag{2}
\]
for every sufficiently short interval. The restrictions and constants may be chosen independently of all the centers. Thus the law gives zero mass to every $\mathcal H^{h_s}$-null set. For each $s<1/2$, Weaver's earlier theorem supplies a carrier of zero $\mathcal H^{h_s}$ measure for each positive-mass minimum cell. Countable unions of their translates give such a carrier for $R-a_m$. This identifies the critical logarithmic exponent exactly as $1/2$ and leaves the endpoint gauge $h_{1/2}$ open. [Weaver, Paper 175, Theorem 1](https://rstation.ai/problems/collatz/papers/175) · [PR145, earlier typical interval gauge](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/terminal-residue/REAL_DIMENSION.md).

We first extract the needed point-mass consequence of the arbitrary-set bound. Write $p$ for an original first-landing law at floor $B$, $A_t=\{y:Bp(y)>t\}$ for $t\ge1$, and $q=p(A_t)$. Then $|A_t|/B\le q/t$ and hence $q\le C(q/t)^\eta+C_K(1+\log B)^{-K}$ for every $0<\eta<1$. If $q$ exceeds twice the last term, rearrangement gives $q\ll_\eta t^{-\eta/(1-\eta)}$. Consequently, for any fixed $P,K$,
\[
        \Pr(Bp(Y)>t,\ Y\ne\dagger)\ll_{P,K}t^{-P}+(1+\log B)^{-K}.    \tag{3}
\]
This bound concerns polylogarithmic thresholds especially effectively; it does not imply uniform ordinary $L^P$ moments of the full grid density because of the additive remainder. [All-event first landing](FIRST_LANDING_ENTROPY.md).

Use the joint limiting history of $R,m$ and the first odd landings $Y_k$ at $B=2^k$ constructed in PR145. Finite-coordinate consistencies give $Y_i=\operatorname{Pass}_{2^i}(Y_k)$ at finite labels for $i<k$, and $m(Y_k)=m$. The simple-segment reciprocal packing gives $|R-R(Y_k)|\ll B^{-\kappa}$ initially, uniformly. These assertions hold also for limits of ordinary all-integer starts after stripping their initial powers of two, as in that construction. The marginal $p_k$ on finite labels and its cemetery is the limiting ordinary landing law at $2^k$.

Fix $\epsilon>0$. By (3), on almost every history we eventually have $p_k(Y_k)\le k^\epsilon/B$. Also $Y_k\ne\dagger$ and $B/k^3\le Y_k\le B$ eventually. Indeed the cemetery obeys every logarithmic power, and $[1,B/k^3]$ has fraction $O(k^{-3})$, so the all-set bound with $\eta=9/10$ is summable. Apply the first Borel–Cantelli lemma; no independence between floors is required.

### Two timed passages from each large dyadic floor

Set $b=2^{\lfloor.97k\rfloor}$ and $J=\lfloor k/8\rfloor$. Under uniform odd input $y\le B$, the first $J$ odd gaps agree in distribution with independent geometric gaps up to total clock $4J$, with a total counting error $O(2^{4J+1}/B)$. In fact all the relevant events are unions of binary classes at precision $4J+1$. The tail $S_J>4J$, where $S_i$ denotes the accumulated gaps, is exponentially small under the geometric law. For every fixed $N$, apart from a set of relative size $O_N(k^{-N})$, all $i\le J$ satisfy
\[
                 |S_i-2i|\le C_N\sqrt{k\log k},\qquad S_J\le4J.        \tag{4}
\]
For example a geometric sum has two-sided bound $2\exp[-c\min(t^2/i,t)]$ at centered deviation $t$: bound the log moment generating function of one centered gap by $C\lambda^2$ on a fixed interval about zero, and minimize the exponential Markov bound there. Sum over $i\le J$ and increase $C_N$. Since $4J+1\le k/2+1$, the rounding error is harmless.

For a good label with $y\ge B/k^3$, let $\tau$ be its first odd entry at or below $b$. Up to and including that entry, on $i\le J$ the departed odd states exceed $b$, and the exact product gives
\[
            \log U^i y=\log y-Di-(S_i-2i)\log2+O(i/b).                \tag{5}
\]
If no crossing had occurred by $J$, (5) at $J$ would place the state below $b$ for all large $k$, since $D/8>.03\log2$. Comparing (5) at $\tau$ and at $\tau-1$ on the two opposite sides of $b$ then gives
\[
        \left|\tau-\frac{\log2}{D}(k-\lfloor.97k\rfloor)\right|
                                     \ll_N\sqrt{k\log k}.              \tag{6}
\]
The fixed bound $3\log k$ on $|\log(y/B)|$ is absorbed here. At large $k$, such $y$ exceeds $b$ so the preceding time exists. The aggregate probability of the bad physical labels under $p_k$ is summable, by the all-set estimate with $N$ chosen large. Thus (6) holds from $Y_k$ to $Y_{\lfloor.97k\rfloor}$ at every sufficiently large $k$ on almost every history.

For one-octave descent take $L=\lceil C\log k\rceil$ and $\log_23<\beta<2$. Except on ordinary relative size $O(e^{-cL}+2^{4L+1}/B)$ one has $\beta L\le S_L\le4L$. If the orbit starts above $B/2$ and does not enter it by $L$, its product correction through $L$ has logarithm $O(L/B)$ and (5), with floor $B/2$, puts its last state strictly below that floor. Labels already below the floor have zero passage cost. Choose $C$ large, use the all-set bound again and Borel–Cantelli. On every typical history, eventually every passage $Y_l\to Y_{l-1}$ takes $O(\log l)$ odd steps. Each contributing odd state exceeds $2^{l-1}$. Therefore summing those successive corrections, and using the packing remainder to identify their limit, gives
\[
                      |R-R(Y_k)|\ll (1+\log k)2^{-k}.                 \tag{7}
\]

### Counting the physical integer labels at one residue interval

Restrict to histories on which all previous eventual estimates hold for every index at least $K$. These increasing restrictions exhaust the measure. Iterate $k\mapsto\lfloor.97k\rfloor$ while the next index is at least $K$. Its terminal index lies in a finite range depending on $K$. For those final floors there are finitely many possible finite labels, each with a finite first clock to its own global minimum. The telescoping main terms in (6) and the geometric sum of its square-root errors give, for $j$ the odd grade from $Y_k$ to $m$,
\[
                   |j-k(\log 2)/D|\ll_K \sqrt{k\log k}.               \tag{8}
\]
The possible minima themselves lie in a finite $K$-dependent set on this restriction. For $t$ the native shortcut clock on the same segment the exact formula reads
\[
                t=j\log_2 3+\log_2(Y_k/m)+R(Y_k).                      \tag{9}
\]
The simple-segment correction is bounded uniformly and $Y_k\in[B/k^3,B]$. Thus for any one $j,m$, the integer $t$ has $O(1+\log k)$ possibilities. For one $j,t,m$ the quantity $R(Y_k)-a_m$ equals $t-j\log_23+\log_2 m-a_m-\log_2Y_k$. If $R-a_m$ lies in an interval of length $2^{-k}$, (7) confines $\log_2 Y_k$ to an interval of length $O((1+\log k)2^{-k})$. It contains $O(1+\log k)$ possible integer labels $Y_k\le2^k$. Consequently the total number of possible labels over the $O_K(\sqrt{k\log k})$ odd grades and all possible minima and clocks is $O_K(\sqrt k(1+\log k)^{5/2})$. Each retained label has unconditional mass at most $k^\epsilon2^{-k}$. This proves (2) on dyadic lengths for $s>1/2+\epsilon$ after absorbing the logarithmic factors. Enlarge any interval to the next dyadic length and choose $0<\epsilon<s-1/2$ to finish.

### Fixed roots, escaping components and almost-everywhere local growth

The result applies conditionally on every positive-mass minimum cell. For a fixed odd unit target $a$, the logarithmic correction to its first visit is, on each predecessor, either $R(n)-R(a)$ if $a$ is visited before or at its minimum, or $R(n)+L_a(m(n))$ otherwise, where $m(n)\le a$ and $L_a(m)$ is the fixed correction from that minimum to $a$. Thus its limiting unnormalized law is dominated by a finite sum of translates of the minimum-cell laws: test the pointwise alternatives against any nonnegative continuous function and pass to the known limits. Such domination, and multiplication by bounded positive first-visit weights, preserves the zero-carrier and absolute-continuity statements on the two sides of $1/2$. The same holds after changing to the product mark on its compact simple-path range. On escaping $C$ one has $-\log_2 F(n)=R(n)-\log_2 F(m(n))$. Restrict the all-center estimate to $C$, reweight by the bounded terminal product, and exponentiate on the compact range. The canonical component law has the same critical exponent by [the ordinary-to-stationary identity (5)](ORDINARY_PRODUCT_TRANSITION.md).

For any of these nonzero laws $\nu$, the following equivalent local conclusion displays the exact exponent at almost every sample:
\[
 \limsup_{r\downarrow0}\frac{\log\big(\nu([x-r,x+r])/r\big)}
                              {\log\log(1/r)}=\tfrac12
                         \quad\text{for }\nu\text{-almost every }x.     \tag{10}
\]
For the upper bound, the restricted measures in (2) increase to the full law. Differentiation with respect to $\nu$ shows that at almost every point one such restriction has positive asymptotic local proportion, transferring its local upper bound. Domination by a finite sum or a bounded weighting gives the same exhaustion by restrictions, using Radon–Nikodym derivatives. For the lower bound, if $\nu([x-r,x+r])\le C h_s(r)$ eventually on a positive-mass subset for some $s<1/2$, take a smaller positive-mass piece with common finite $C$ and onset. The mass distribution bound on its intersections with small intervals gives that piece positive $\mathcal H^{h_s}$ measure inside the zero-measure carrier, a contradiction. Apply the two conclusions at countably many exponents approaching $1/2$. Neither (10) nor (2) decides the critical gauge itself.
