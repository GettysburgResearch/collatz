# Typical geometric prime bands give the empirical law of every prime addition

Use the independent geometric valuations, signatures $S_z$, history $\mathcal A_w$, and ordinary orbit event $F$ of [the prime-band calculation](PRIME_BAND_MIXING.md). Write $d$ for its ordinary natural density. The events are fixed component unions or visits to a fixed odd target. The underlying orbit input is the counted-pair synchronization theorem used in the preceding calculation. The analytic arguments here use the classical prime number theorem, the Vinogradov–Korobov bound for prime Dirichlet polynomials and elementary mean values. **Ordinary RH is unnecessary for the following two conclusions.**

1. For $z\to\infty$ and $\log(2w)=o(\log z)$, the expected absolute difference between $\Pr(F(S_z)\mid\mathcal A_w)$ and $d$ tends to zero. The full conditional component law converges in expected total variation under the corresponding ordinary component-TV input. This gives the exact finite-word frequencies at deterministic cutoffs stated in the preceding paper, including the choice $\log z_j=j!$.
2. For an ordinary integer $n$, list its distinct prime factors in increasing order and put $s_j=\prod_{i\le j}p_i^{v_{p_i}(n)}$. Then
   \[
      \frac{1}{\max(1,\omega(n))}\sum_{j=1}^{\omega(n)} F(s_j)
                    \longrightarrow d
   \]
   in natural probability. With the full ordinary component-TV input, the empirical probability measure of components at these individual prime additions converges in total variation in natural probability to the ordinary component law. In particular an additional positive-density basin would occupy its own ordinary density of the full prime-factor chain on typical integers. This strengthens the earlier mean occupancy calculation. It gives no independence formula for immediately consecutive links. Prescribing a word of consecutive one-prime additions with positive lower frequency in the preceding paper still uses its single-prime estimate under RH.

## Smoothing with one smaller prime factor

Use the logarithmic product boxes and continuous reference of the preceding paper. Allow each logarithmic interval to have width $2/K$ for a fixed integer $K\ge r$, where $r$ is the number of factors and $Y=\prod_{i\le r} P_i$ is the product of their lower endpoints. Use the same fixed smooth bump throughout. Assume all $P_i\ge Y^\theta$ with fixed $\theta>0$. To prove the smoothed density comparison in its equation (2) without RH it suffices that one factor satisfies $P_s\le Y^{\gamma/2}$, where the log-smoothing width is $Y^{-1+\gamma}$ and $0<\gamma<1/2$ is fixed. This requires at least two factors when $Y$ is large.

On $|t|\le(\log Y)^B$, the smoothed prime characteristic functions are within $O_{K,\theta,B,A}((\log Y)^{-A})$ of their continuous counterparts for every fixed $A$. Apply the prime number theorem with its classical zero-free error and partial summation; the differentiations cost only a fixed power of $\log Y$. Normalizing the harmonic mass of one box costs $O(K\log Y)$. On $(\log Y)^B\le |t|\le Y$, the normalized characteristic function of the designated smaller prime is $O_{K,\theta,D}((\log Y)^{-D})$ for every required $D$ on choosing $B$ sufficiently large. In the Vinogradov–Korobov estimate for $\Lambda$ take the parameter larger than $1/\theta$ and sufficiently large for the desired logarithmic saving. It controls subintervals of a dyadic interval. Partial summation with the smooth weight and $1/\log p$, followed by deletion of proper prime powers, gives the assertion. If necessary, split the box into a bounded number of dyadic pieces. [Matomäki, Radziwiłł, Shao, Tao and Teräväinen, *Higher uniformity of arithmetic functions in short intervals II*, Lemma 3.2](https://doi.org/10.1007/s00222-026-01408-6)

For the other factors put $N=Y/P_s$ and write their combined characteristic function, up to a modulus-one scalar, as $\sum_{N\le n\le e^2N} b_n n^{-it}$. Here $b_n\ge0$, $\sum b_n=1$, and
\[
       \max b_n\ll_{K} (\log Y)^{r-1}/N.
\]
Indeed each ordered tuple has at most that normalized weight and a fixed integer has at most $(r-1)!$ such ordered prime factorizations, including repeated factors. Hence for $1\le T\le N$,
\[
  \int_{-T}^{T}\left|\sum b_n n^{-it}\right|^2dt
        \ll_K (\log Y)^{r}.
\]
For completeness, the diagonal is $2T\sum b_n^2$. Each off-diagonal integral has absolute value $O(N/|m-n|)$ in this support. The inequality $2b_nb_m\le b_n^2+b_m^2$ and the harmonic sum give $O(N\log(2N)\sum b_n^2)$.

Take $T=Y^{1-\gamma/2}\le N$. Multiplying the last integral by the squared pointwise smaller-prime saving makes the product law's Fourier contribution above $(\log Y)^B$ and below $T$ tend to zero. The continuous reference has the same conclusion by integration by parts in any one factor. Below $(\log Y)^B$ the low-frequency estimate controls the difference. Above $T$ the smoothing kernel's rapid Fourier decay pays the whole integral, just as in the preceding paper. Its Plancherel argument proves an $o(1)$ total-variation error between the two smoothed log-product densities. All constants discarded into $o(1)$ may depend on $K,\theta,\gamma$ held fixed.

The binary-cell Brun–Titchmarsh comparison and the original physical smoothing argument of equation (3) in the preceding paper now apply. With interval width $2/K$, the largest-prime class upper stays $C/2^t$: its normalized prime atom bound is $CK\log P/P$, while its interval has length $O(P/K)$. The reference density has sup norm and variation $O(K)$. Thus the error for an earlier odd multiplier $D$ with $\log(2D)\le\lambda\log Y$ is at most
\[
           C\bigl(\sqrt{r(\lambda+\gamma)}+K\sqrt\lambda\bigr)
                +o_{K,\theta,\gamma}(1),                                  \tag{1}
\]
uniform over the same ordinary orbit tests. The absolute leading constant is independent of $K$. Fixed powers of two in $D$ may first be removed by the exact invariance of these tests.

## A typical band provides the smaller prime

Fix $K_0>1$, $0<a<1$ and $0<\delta<a$ sufficiently small. Include all primes through $z^{\delta^2}$ in the earlier multiplier after conditioning on their geometric valuations. Apart from earlier histories or increments of total probability $O(1/K_0)$ it has log at most $3K_0\delta^2\log z$, by the mean log-signature bound and $\log(2w)=o(\log z)$. Among the remaining primes require at least one in $(z^{\delta^2},z^\delta]$ and one in $(z^a,z]$. Their absence probabilities tend respectively to $\delta$ and $a$ by Mertens' product. Repetitions above $z^{\delta^2}$ have probability $o_\delta(1)$. Take $K=2+\lceil(1+2\log(1/\delta))/a\rceil$. Exceeding $K-1$ distinct remaining primes costs $O(a)$ by their mean count.

Conditional unordered squarefree prime products have harmonic weights. Randomly ordering the tuple, smoothly boxing all factors at the common width $2/K$, deleting boxes crossing the fixed power boundaries, and dropping the collision restriction work as in the preceding proof. Each boundary costs $o_{K,\delta}(1)$ by the prime number theorem; each normalized factor atom tends uniformly to zero. On every retained list $Y\gg_K z^a$, $Y\le z^K$ and all factors obey $P_i\ge Y^{\delta^2/(2K)}$. A designated smaller prime obeys $P_s\le z^\delta\le Y^{2\delta/a}$. Take $\gamma=6\delta/a<1/2$, $\lambda=4K_0\delta^2/a$ and use (1). For fixed $K_0,a$ its leading error tends to zero as $\delta\downarrow0$, since $K\ll_a1+\log(1/\delta)$. Choose $K_0$ large, $a$ small, and then $\delta$ small before passing to large $z$. This proves the first claim including conditional expected TV. The typical subpopulation has almost full probability. A single fixed prime interval by itself lacks the smaller prime used by this proof.

## Sampling each individual prime addition

Put $z_j=\exp(e^j)$ for integers $j\ge1$, $I_j=(z_{j-1},z_j]$, $u_j=\sum_{p\in I_j}1/p=1+o(1)$, and let
\[
   B_j=\sum_{p\in I_j}1_{v_p\ge1}F(S_p),\qquad
   C_j=\sum_{p\in I_j}1_{v_p\ge1}.
\]
The $C_j$ have uniformly bounded second moments by independence. We claim
\[
    \mathbb E\big|\mathbb E(B_j\mid\mathcal A_{z_i})-d u_j\big|\to0
                         \quad(j-i\to\infty,\ j\to\infty,\ i<j).        \tag{2}
\]

Weight a tagged prime $p\in I_j$ by $1/p$, of total mass $u_j$. Conditional on $v_p\ge1$ its exponent is one plus a fresh geometric variable, which exceeds one with probability $1/p$. The total weighted error from replacing it by one is $o(1)$. Box the tagged prime with the same smooth width $2/K$ as above, omitting the two boundary overlaps at total harmonic cost $o_K(1)$. In a box $[P,e^{2/K}P]$ we can use $F(S_P p)$ in place of $F(S_p)$: the expected number of other occupied primes in $(P,e^{2/K}P]$ is $O_K(1/\log P)$, uniformly in the sampled prime, and all such valuations are independent after conditioning on the tag. A coincident lower endpoint may be omitted or included at the same negligible cost. The tagged prime now has an independent normalized harmonic box law. All errors described here bound expected absolute conditional errors by averaging.

Apply the typical-band argument to the ordinary random primes in $(z_i,P]$ and append the already-boxed tagged prime. The earlier scale obeys $\log(2z_i)/\log P\ll e^{1+i-j}$ uniformly. In fact the tagged prime itself guarantees $Y\gg P$, so it already supplies the required large factor; the earlier band still supplies a smaller one except for the same $O(\delta)+o(1)$ probability. There are at most $K$ factors after appending the tag, by the choice above. All factors and the earlier multiplier satisfy the bounds in (1) with $P$ as the outer scale and, if needed, a decreased fixed $\theta$. This proves (2) after summation of the harmonic box masses. The absence of an independently sampled smaller factor at a fixed tagged prime is the reason we average the tag inside its box. Conditioning on its exact numerical value would not justify this argument.

To pass from conditional expected counts to empirical counts, note that $0\le\mathbb E(B_j\mid\mathcal A_{z_i})\le u_j$ whenever $i<j$, since the new $C_j$ is independent of that history. Truncating the older $B_i$ at a large fixed height, using its bounded second moment, shows from (2) that $\operatorname{Cov}(B_i,B_j)\to0$ whenever $j-i\to\infty$ and $j\to\infty$. It also gives $\mathbb E B_j\to d$ by taking the earlier history fixed. Summing bounded near-diagonal covariances and the uniformly vanishing far-diagonal covariances gives
\[
              J^{-1}\sum_{j\le J}B_j\longrightarrow d
                          \qquad\text{in }L^2 .
\]
The total number of geometric links divided by $J$ tends to one in $L^2$. A partial last bin has bounded second moment. These assertions give the second claim for geometric signatures with any cutoff tending to infinity. Transfer at $z=\exp(\log X/\log\log X)$ by the full-signature TV approximation and omit the higher primes, whose number is $o(\log\log X)$ in ordinary probability. The first finitely many primes likewise change a vanishing fraction. Dyadic octave convergence implies the stated natural probability conclusion. [Signature comparison and omitted-prime bound](CANONICAL_PRIME_VARIATION.md)

For a countable ordinary component law $\pi$, choose a finite subset carrying all but $\varepsilon$ of its mass. Apply the scalar conclusion to each of its singletons and to its complement. This bounds the full total variation in probability and then lets $\varepsilon\downarrow0$. The same argument applies to a finite joint alphabet of specified orbit tests when the associated fixed joint events have the ordinary limits and finite-merge invariance used above.
