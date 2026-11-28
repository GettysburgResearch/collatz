# Full small-prime signatures and the fates of smooth divisors

Write $I_X=(X,2X]$ and $D_z(n)=\prod_{p\le z}p^{v_p(n)}$, the complete prime-power part of $n$ supported on primes at most $z$. Knowledge of $D_z$ is equivalent to knowing the entire vector of these prime valuations. Write $C(n)$ for the actual eventual shortcut Collatz component, with equality when the two forward orbits meet. The countable set of labels includes every hypothetical escaping component.

**Full signature theorem.** If $z\ge2$ and $\log(2z)=o(\log X)$ and $N$ is uniform on the ordinary integers in $I_X$, then
\[
 d_{\rm TV}\big(\mathcal L(C(N),D_z(N)),
     \mathcal L(C(N))\otimes\mathcal L(D_z(N))\big)=o(1).                 \tag{1}
\]
The estimate permits every bounded joint test of both exact discrete records. The signature marginal may equivalently be replaced by the independent geometric-valuation law below. The same estimate holds with $C(N)$ replaced by the full discrete first-hit record, including the miss option, time, accumulated odd count, landing and final $\ell$ parity bits, for any stopping set in $[1,B]$ with $2^\ell B\le X^{4/5}$. Adding the exact real survival coordinate permits bounded-Lipschitz testing in that coordinate. The discrete component law needs no density-existence hypothesis.

**Nested divisors.** Fix $k$, let $z_1\to\infty$, suppose $\log z_{i-1}=o((\log z_i)^{1/200})$ for $2\le i\le k$, and assume $\log z_k=o(\log X)$. Set $D_i=D_{z_i}(N)$ and $D_{k+1}=N$. For any fixed component unions or fixed-odd-target visit events $E_i$ with ordinary natural densities $d_i$,
\[
            \Pr(D_i\in E_i\text{ for all }1\le i\le k+1)
                      \ \longrightarrow\ \prod_{i=1}^{k+1}d_i .          \tag{2}
\]
In particular if a second positive cycle exists, every prescribed finite pattern of visits to its basin and the basin of one occurs with positive limiting probability along these *deterministically selected divisors of ordinary integers*. Positivity in this consequence uses the cited predecessor-density input. The estimates for integer orbits use the arbitrary-offset counted-fusion result attributed to Leen. The arithmetic inputs are the fundamental lemma of sieve theory, Mertens' theorem and the 2016 short-interval theorem of Matomäki and Radziwiłł. Only the proof of (2) needs the last input. [Exact counted offset estimate, Paper 209/v1, Theorem 4.2](https://rstation.ai/problems/collatz/papers/209) · [Ordinary predecessor densities, Paper 12/v1, Theorem 1 under Inputs C–D](https://rstation.ai/problems/collatz/papers/12/v1)

## Conditioning on a complete signature

Put $V(z)=\prod_{p\le z}(1-1/p)$. Independent random exponents with $\Pr(v_p=a)=(1-1/p)p^{-a}$ give the signature probability $V(z)/d$ for each $z$-smooth integer $d$. For ordinary $n\in I_X$, the event $D_z(n)=d$ instead means exactly $n=dm$, where $m\in I_{X/d}$ has no prime factor at most $z$. There is no coprimality correction: a prime dividing $d$ is among those already excluded from $m$.

We use the following direct form of the fundamental lemma. In any interval of $U$ consecutive integers, the number avoiding every prime at most $z$ is $UV(z)(1+o(1))$ uniformly when $\log(2z)=o(\log U)$. In a prescribed odd class modulo $Q=2^t$ inside an interval of length $Y$, the number is $O((Y/Q)V(z))$ when $\log(2z)=o(\log(Y/Q))$. For the second assertion parameterize the progression, omit $p=2$, and forbid one residue per odd prime. In both cases the sieve sequence has remainder $O(1)$ per squarefree divisor. Upper and lower sieve weights of modulus at most $\sqrt U$ (respectively $\sqrt{Y/Q}$) cost at most this level in the remainders. Their main terms are the displayed Euler products with relative error tending to zero, and omitting two multiplies the product by two. We also use the upper bound $O(UV(z))$ when $U\ge z^{10}$ and $z\ge2$ by the same upper sieve with bounded-away-from-zero sifting ratio. [Kevin Ford, *Sieve methods*, Theorem 3.6(a), p. 38](https://ford126.web.illinois.edu/sieve2023.pdf)

Let $L=\log X$, $l=\log(2z)$, $D_0=\exp(\sqrt{Ll})$, $H=\lfloor D_0\rfloor$, $t=\lfloor(\log_2 X)/10\rfloor$, $Q=2^t$. Here $\log z=o(\log H)$ and $D_0 H=X^{o(1)}$. In the independent model $\mathbb E\log D_z=\sum_{p\le z}\log p/(p-1)\ll l$. The actual expectation has the same upper bound plus $O(z\log(2X)/X)$: sum $\log p$ over divisibility by $p^a\le2X$, whose octave probability is at most $1/p^a+O(1/X)$. Consequently $d>D_0$ has probability $O(\sqrt{l/L})+o(1)$ in both models. For each smooth $d\le D_0$, the first sieve estimate for $Y=X/d$ gives actual signature probability $(V(z)/d)(1+o(1))$ uniformly in $d$. Summation proves total-variation convergence of the signature marginal to the independent model.

Fix such a $d$, put $a=2^{v_2(d)}$ and $w(m)=1_{P^-(m)>z}$, with $w(1)=1$. Let $F$ be a component test bounded by one, or a test of the cleared stopped record. It may depend arbitrarily on $d$. Compare $F(dm)$ with $F(d(m-j))$ for $1\le j\le H$. The counted-fusion theorem bounds the fraction of bad binary cells for the lower source at offset $dj$ by
\[
            O(\varepsilon),\qquad \varepsilon=\sqrt{\log(2D_0 H)/t}=o(1).
\]
Multiplication by $d$ followed by a translation takes a uniform residue modulo $Q$ to a residue with at most $a$ preimages. The rough count bound per binary cell therefore gives normalized weighted failure $O(a\varepsilon)$ on $I_Y$. The comparison applies to discrete records because every compared source exceeds $2^{t+\ell}B$ and a counted merger preserves its remaining path. The two real survival values at a merged pair differ by at most $O(H/Y)$, by their source ratio. For actual and independent signatures, $a>\varepsilon^{-1/2}$ has probability $O(\sqrt\varepsilon+1/X)$ by the geometric tail of the two-adic valuation (or direct counting of multiples). Discard these signatures.

On every retained signature we can now average the comparison over $j$. Uniformly in $u$, the sieve estimate at length $H$ gives $\sum_{j\le H}w(u+j)=HV(z)(1+o(1))$. Moving the endpoints costs $O(H/(YV(z)))=o(1)$. Therefore
\[
 \frac{\sum_{I_Y}w(m)F(dm)}{\sum_{I_Y}w(m)}
                  = \mathbb E_{u\in I_Y} F(du)+o(1).
\]
Finally compare $F(du)$ with $F(du+i)$ for $0\le i<d$ by the same binary-cell bound without the sieve weight. Each bad cell on the $u$ side has at most $Y/Q+1$ representatives. The error is $O(a\varepsilon(1+Q/Y))=o(1)$ uniformly. The tiled intervals cover $I_X$ up to $O(d)$ endpoints. This proves that for every retained $d$ the conditional expectation differs by $o(1)$ from the ordinary $I_X$ mean *of its own test*. Taking the supremum over joint tests costs nothing more, which proves (1). Real marks retain the stated Lipschitz qualification throughout.

In particular if membership in one basin has octave probability tending to $d\in(0,1)$, every predictor based on the entire signature $D_z(N)$ misclassifies the fate with probability at least $\min(d,1-d)-o(1)$. An arbitrary Boolean combination of the valuations is allowed. A correlation bound against individual multiplicative functions alone does not yield this uniform conditional statement.

## The factor bands in the geometric model

Set $z_0=1$, $V(1)=1$. In the independent model let $M_i$ be the product of prime powers with primes in $(z_{i-1},z_i]$. These increments are independent. At a single stage write $w=z_{i-1}$, $z=z_i$, $M=M_i$ and $c=V(z)/V(w)$. The exact law is
\[
             \Pr(M=m)=c\,b(m)/m,\qquad
             b(m)=1_{\text{every prime factor of }m\text{ lies in }(w,z]} .
\]
Mertens' theorem gives $c\asymp\log(2w)/\log z$. Here $b(1)=1$. Also $\mathbb E\log M\ll\log z$, whence $\Pr(M>z^K)\ll1/K$. For $0<\alpha<1$, we claim
\[
                      \Pr(M<z^\alpha)\ll \alpha+c .                     \tag{3}
\]
For $w=1$ this follows from the harmonic sum bound. For $w\ge2$, the reciprocal sum over $m\le w^{10}$ supported on primes in $(w,z]$ is at most $\prod_{w<p\le w^{10}}(1-1/p)^{-1}=O(1)$. Above $w^{10}$, discard the upper prime cutoff. At $T\ge w^{10}$ the count of $w$-rough integers up to $T$ is $O(TV(w))$ by the upper sieve just stated. Partial summation up to $z^\alpha$ bounds the remaining reciprocal sum by $O(V(w)(1+\alpha\log z))$. Multiplication by $c$ proves (3).

The preceding product $d=\prod_{h<i}M_h$ has the geometric signature law on primes through $w$. Except on a set of probability $O(1/K')$, it satisfies $\log d\le K'\log(2w)$ and $2^{v_2(d)}\le K'$ by the expectation and the two-adic geometric tail. For the first band take $d=1$. Fix $K',K$ and $\alpha>0$. Let $F$ indicate the desired fixed component or visit event with ordinary natural density $d_F$. We show uniformly over the retained $d$ that
\[
                         \mathbb E F(dM) = d_F+o(1)+O(\alpha+1/K).         \tag{4}
\]
The $o(1)$ may depend on the three fixed truncation constants.

For any $z^{\alpha/2}\le T\le 2z^K$, put $h=\lfloor e^{\sqrt{\log T}}\rfloor$ and $q=2^{\lfloor(\log_2T)/10\rfloor}$. The function $b$ is real multiplicative with values in $[0,1]$. The published short-interval theorem with parameter $\delta=(\log T)^{-1/150}$ gives
\[
   \mathbb E_{u\in I_T}\left|h^{-1}\sum_{j\le h} b(u+j)-\mathbb E_{I_T}b\right|
            \ll(\log T)^{-1/150}.                                         \tag{5}
\]
This is an *absolute* bound. The implied constant is independent of the band endpoints. The term from exceptional intervals is bounded by the normalized exceptional count with the trivial bound two there. The logarithmic exponent follows directly from Theorem 1 and is the one used in the existing Collatz multiplicative test below. [Matomäki–Radziwiłł, *Multiplicative functions in short intervals*, Annals 183 (2016), Theorem 1](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf) · [PR 213, precise exponent calculation for the unmultiplied source](https://github.com/GettysburgResearch/collatz/blob/f2fb6bd2ed9dd4172d9e2040ca6b9ca012ca8ae0/research/astra-global-rigidity-20261128/mersenne/REAL_MULTIPLICATIVE_OBSERVABLES.md)

Compare $F(dm)$ with $F(d(m-j))$ for $j\le h$, now using $b\le1$ and ordinary absolute errors. Failed binary cells cost
\[
      O\!\left(K'\sqrt{\frac{\log(2dh)}{\log T}}(1+q/T)\right)
                       \ll_{K',\alpha}(\log T)^{-1/4}.
\]
Indeed $\log d\ll_{K'}\log(2w)=o((\log z)^{1/200})$ when $i\ge2$. For fixed target visits all sources remain above the target until the merger comparison date. Endpoints cost $O(h/T)$. After averaging, (5) gives the factorization of the marked octave sum up to $O_{K',\alpha}((\log T)^{-1/150})$. A further comparison of $F(du)$ with $F(du+j')$, $0\le j'<d$, tiles the whole ordinary octave $I_{dT}$ up to an error of the same order. Since $F$ has ordinary density $d_F$, we have
\[
 \left|\mathbb E_{m\in I_T} b(m)(F(dm)-d_F)\right|
     \ll_{K',\alpha} (\log z)^{-1/150}+\eta_z\,\mathbb E_{I_T}b,         \tag{6}
\]
where $\eta_z=\sup_{U\ge z^{\alpha/2}/2}|\mathbb E_{I_U}F-d_F|\to0$. Keeping the factor $\mathbb E b$ on this last, unquantified error is essential.

To pass to the harmonic law, sum (6) on dyadic octaves descending from any $Y\in[z^\alpha,z^K]$ until the lower endpoint becomes less than $z^{\alpha/2}$. The remaining count is $O(z^{\alpha/2})$. Thus the cumulative signed sum in (6) is bounded by $O_{K',\alpha}(Y(\log z)^{-1/150}+z^{\alpha/2})+\eta_z\sum_{m\le Y}b(m)$. Partial summation over $z^\alpha\le m\le z^K$, followed by multiplication by $c$, bounds its harmonic signed mass by
\[
 O_{K',\alpha,K}\big(\log(2w)(\log z)^{-1/150}+z^{-\alpha/2}\big)+O(\eta_z)=o(1).
\]
For the term involving $\eta_z$, the cumulative endpoint divided by $Y$ is at most $\sum_{m\le Y}b(m)/m$, and the positive integral of the cumulative count against $Y^{-2}$ is at most $\sum_{m\ge1} b(m)/m=1/c$. The lower and upper omitted tails cost $O(\alpha+c+1/K)$ by (3) and Markov. This proves (4) and explains the spacing condition.

Conditional on all previous bands, (4) holds outside an earlier-signature exceptional set of probability $O(1/K')$. One may multiply it by **any** $[0,1]$ test of all earlier bands. Let the scales grow, then send $\alpha\downarrow0$ and $K,K'\to\infty$. Iteration yields the product law of the desired events on $D_1,\ldots,D_k$ in the geometric model. The marginal signature approximation transfers this entire statement to ordinary $N$, since each $D_i$ is a function of $D_{z_k}(N)$. Finally (1) decouples the event at $N$ from all the earlier events simultaneously. A fixed visit uses the cleared stopped-record version. This proves (2).

The distinction between $D_z(N)$ and $N$ matters. For $z\ge2X$ the signature identifies $N$ outright. Also, no independence is asserted between two values of $N$ differing by one: counted fusion often gives those starts identical fates. The proof uses sparse *multiplicative* divisor scales inside one integer. None of the displayed laws decides whether a second cycle exists.

## Many prime-factor fate changes on almost every ordinary integer

For a positive integer $n$ write its distinct prime factors in increasing order $p_1<\cdots<p_{\omega(n)}$. Its canonical divisor chain is $s_0=1$ and $s_j=\prod_{i\le j}p_i^{v_{p_i}(n)}$. Thus each link adds the entire native prime power dividing $n$. For a fixed basin or fixed-target hit indicator $F$ with ordinary natural density $d$, define
\[
                   V_F(n)=\sum_{j=1}^{\omega(n)} |F(s_j)-F(s_{j-1})|.
\]
If $0<d<1$, then for every $c<2d(1-d)/\log201$, the set of ordinary integers satisfying
\[
                        V_F(n)\ \ge\ c\log\log\log n                    \tag{7}
\]
has natural density one. In particular if any positive orbit misses one, the test for actually visiting one changes truth value an unbounded number of times along this canonical chain on density-one ordinary populations. If a second cycle exists, the same holds for visiting its basin. Neither assertion is restricted to almost-prime sources, special divisors chosen after knowing their fates, or a rare subset of source integers.

Here the harmonic band argument supplies a growing number of observations without multiplying a fixed-dimensional error by that number. Choose a deterministic increasing sequence, for example $z_1=e^2$ and $\log z_{j+1}=(\log z_j)^{201}$. On one probability space take independent geometric valuations for **all** primes. Write $S_j$ for their product signature up to $z_j$, $X_j=F(S_j)$, and $\mathcal A_j$ for the sigma-field of all valuations up to $z_j$. The single-stage estimates (3)–(6), first with the three truncation constants fixed and then relaxed, give
\[
                    \mathbb E|\mathbb E(X_j\mid\mathcal A_{j-1})-d|\to0.
                                                                            \tag{8}
\]
Indeed all retained earlier signatures have the *same uniform* conditional error from (4), while discarded signatures have probability $O(1/K')$. Successive deterministic cutoffs satisfy precisely the spacing of that result. The fixed first band is irrelevant.

For $k\to\infty$ the average of $X_j-\mathbb E(X_j\mid\mathcal A_{j-1})$ has $L^2$ norm at most $k^{-1/2}$ by orthogonality of martingale differences. Cesàro averaging (8) gives $k^{-1}\sum_{j\le k}X_j\to d$ in $L^1$. Apply the same argument to the switch indicator $Y_j=|X_j-X_{j-1}|$ for $j\ge2$. Its conditional expectation differs in $L^1$ by $o(1)$ from $d(1-X_{j-1})+(1-d)X_{j-1}$. Consequently
\[
                    k^{-1}\sum_{2\le j\le k}Y_j\ \longrightarrow\ 2d(1-d)
                                  \qquad\text{in }L^1.                   \tag{9}
\]
In fact for any fixed finite word of basin or fixed-hit events with densities $d_1',\ldots,d_h'$, the proportion of consecutive length-$h$ windows on this cutoff chain realizing the word tends in $L^1$ to $\prod_i d_i'$. To see this, write each word indicator as the length-$(h-1)$ prefix times the last indicator. Subtract the conditional expectation of that last indicator given the entire earlier history. The resulting products are bounded martingale differences. The conditional-mean error tends to zero in $L^1$ by (8) for the indicated last event. Induct on $h$.

At ordinary scale $X$ take $k=k(X)$ maximal with $\log z_k\le\sqrt{\log X}$. Thus
\[
                      k=\frac{\log\log\log X}{\log 201}+O(1).
\]
The full signature marginal at $z_k$ is within $o(1)$ in total variation of the independent geometric model, by the sieve proof of (1). All $k$ observed divisor fates and the bounded switch fraction in (9) are functions of that *single finite signature*. Their transferred errors therefore still tend to zero even though $k$ grows. On the actual integer, the visited cutoffs form an ordered subsequence of its canonical divisor chain, possibly with repetitions. Each change between consecutive observed cutoffs costs at least one canonical link, which proves (7) on every large octave and hence in natural density. This argument never asserts that the full infinite factorization of a fixed positive integer is independent of its fate.

Under the cited positive predecessor densities, universal convergence is consequently equivalent to the following statement about ordinary positive integers:
\[
  \text{for some finite }K,\quad
    \{n:V_{\mathbf1_{\mathrm{visits}\ 1}}(n)\le K\}
       \text{ has positive upper natural density}.                        \tag{10}
\]
Under universal convergence this variation is identically zero. If a positive orbit misses one, an odd unit in its component has a positive-density predecessor set disjoint from the basin of one, whereas the latter itself has positive density. Thus $0<d_1<1$, and (7) makes every bounded-variation set in (10) have density zero. A proof of the positive-upper-density bound in (10) is missing.

For any two positive-density cycle basins and any fixed alternating pattern of visits to them, the length-$h$ window conclusion gives its positive limiting frequency on the cutoff chain in probability. In particular, on a natural-density-one set of ordinary $n$ the full canonical divisor chain contains this prescribed pattern as an ordered subsequence. The event times at which these different divisors visit the cycles can be different.

For a concrete event available without an extra-cycle hypothesis, the predecessor sets of $5$ and $85$ are disjoint. The first follows $5,8,4,2,1,2,\ldots$, and the second follows $85,128,64,32,16,8,4,2,1,\ldots$. Neither fixed starting target ever hits the other. Both have positive density under the all-unit predecessor input. Hence (7) already applies to the actual test of ever visiting five. Every prescribed alternating word of visits to $5$ and $85$ also occurs in order on almost every canonical chain.

There is an Euler-sum form of the forced changes. Let $S_{p^-}$ be the independent geometric signature on primes strictly below $p$, and let $z\to\infty$. For $0<d<1$,
\[
 \liminf_{z\to\infty}\frac{1}{\log\log\log z}
   \sum_{p\le z}\frac1p\Pr(F(pS_{p^-})\ne F(S_{p^-}))
       \ \ge\ \frac{2d(1-d)}{\log201}.                                  \tag{11}
\]
Indeed the expected canonical variation up to $z$ dominates the expected switches on all lacunary cutoffs not exceeding $z$. Formula (9) gives the lower bound. Independence of $v_p$ and $S_{p^-}$ expands the expected canonical variation as the sum over $p\le z$, $a\ge1$ of $(1-1/p)p^{-a}\Pr(F(p^aS_{p^-})\ne F(S_{p^-}))$. The total error on retaining the single-prime term with coefficient $1/p$ is $O(\sum_p p^{-2})=O(1)$. Thus the divergence concerns actual multiplication by individual primes even though the canonical chain adds whole prime powers.

[Exact smooth-signature and Euler variation checks](check_divisor_meetings.py) · [Recorded counts](../../../reports/astra-global-20261128/cycles/DIVISOR_MEETINGS.json)
