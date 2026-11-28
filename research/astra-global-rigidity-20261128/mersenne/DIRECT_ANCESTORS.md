# The least cost of a smaller direct ancestor near positive one

Use the shortcut map $T(2z)=z$, $T(2z+1)=3z+2$. An ancestor of $N$ is an ordinary positive $x$ satisfying $T^t(x)=N$. Its cost $Q$ counts odd departures over its own clock $t$. The target here is the supplied integer at native date zero. A smaller ancestor can then be followed forward through every point of the supplied orbit.

## The exact first attainable cost

Fix $K\ge1$. In the ordinary inverse tree from integer $1$, stop a word immediately after its $K$th odd inverse step. Its endpoint is an odd integer $w$. Let $L_K$ be the shortest shortcut length of such a word and $W_K$ the set of its minimizing endpoints. Both are finite and computable. Repeating $1\leftarrow2\leftarrow1$ gives $L_K\le2K$. Put

$$m_K=\min\{m\ge1:2^{L_K+m}<3^{K+m}\}. \tag{1}$$

**Theorem.** For an odd $N=1+3^K u>1$ with $N\ge3^{2(K+m_K)}$, every positive $x<N$ visiting $N$ at any clock has cost at least $K+m_K$. That cost is attained exactly when

$$u\equiv-(w+1)2^{-L_K}\pmod{3^{m_K}}\qquad\text{for some }w\in W_K. \tag{2}$$

The classes in (2) are distinct. In each one an explicit smaller ordinary ancestor is

$$x+1=\frac{2^{m_K}(w+1+2^{L_K}u)}{3^{m_K}},\qquad t=L_K+m_K. \tag{3}$$

The same formula works for every positive even $u$ in (2), including below the size threshold. The conditional natural density of optimum attainment in the whole odd class $N\equiv1\pmod{3^K}$ equals $|W_K|/3^{m_K}<2^{-m_K}$. The cost lower bound concerns every candidate, independently of whether any smaller ancestor exists.

**Proof.** A reverse letter is $E(v)=2v$ or the integral $O(v)=(2v-1)/3$. If a reverse word from $N$ uses $q\le K$ odds, reduce its states along the same word from $1$. At each legal step before the $K$th odd the congruence modulo the remaining power of three makes the reference step legal. Every reference state is positive. At total length $t$ the two terminal states differ by $2^t3^{K-q}u$. The reference terminal $w$ satisfies $w\le 2^t/3^q$, by dropping the negative subtractions in the inverse word. Consequently $2^t/3^q\ge1$ and the actual terminal is at least $N$.

Suppose $Q=K+m'$ with $1\le m'\le m_K$. Write $e$ for the total number of even inverses in the full word temporarily. In the shifted height $v+1$, every $E$ increases the ratio by at least $3/2$, and $O$ gives the exact ratio $2/3$. Thus $x<N$ forces $e<Q$ and $t=e+Q<2Q$. The ordinary forward affine numerator is $2^t N=3^Q x+A$, where $0\le A\le3^t-2^t<3^t$ by letter induction. If $2^t>3^Q$, then $N\le(2^t-3^Q)N<A<3^{2Q}$, impossible. Equality $2^t=3^Q$ is impossible. Hence this entire inverse word has $2^t/3^Q<1$.

Cut immediately after its $K$th odd. The reference there is $w$ and the actual value is $w+2^L u$ for $L\ge L_K$. The remaining $m'$ odd letters and $e'$ even letters give $t=L+m'+e'$. It follows from (1) that $m'\ge m_K$. At equality the minimality in (1) yields $2^{L_K+m_K}/3^{K+m_K}\ge2/3$; this also holds for $m_K=1$ since $2^{L_K}>3^K$. A single additional native step would give ratio at least $4/3$. Thus $L=L_K$, $e'=0$. A positive state $z$ permits $m_K$ successive odd inverses exactly when $3^{m_K}\mid z+1$. These steps give (2) and (3). Conversely the reference word lifts legally from $N$ with the displayed difference. The terminal is a positive odd integer. Writing $D=2^{L_K+m_K}/3^{K+m_K}<1$, the strict $w<2^{L_K}/3^K$ gives $(2/3)^{m_K}(w+1)<D+(2/3)^{m_K}<2$. Hence $x+1=D(N-1)+(2/3)^{m_K}(w+1)<N+1$. Finally $1\le w<2^{L_K}/3^K<(3/2)^{m_K}<3^{m_K}$ proves distinctness, the stated count, and the density.

## How far the extra cost grows

**Unconditional divergence.** $m_K\to\infty$. Otherwise along an infinite subsequence a minimizing odd endpoint $w<(3/2)^{m_K}$ repeats. Its accelerated odd orbit has a determinate first hit at one after $k(w)$ odd steps in $h(w)$ shortcut steps. The remaining $K-k(w)$ odd steps must be laps at one, each of length two. This forces $L_K=h(w)+2(K-k(w))$ on that subsequence, contrary to bounded $m_K$ in (1). Thus direct protection at every odd target sufficiently close to one on this scale improves from $K+1$ to $K+\omega(1)$.

There is an exact asymptotic obstruction to a numerical linear lower bound. Let

$$\Gamma=\limsup_{\substack{w\to\infty\\w\text{ odd, terminates}}}\frac{k(w)}{\log w}.$$

Then, with $1/\infty=0$,

$$\liminf_{K\to\infty}\frac{m_K}{K}=\frac{\min\{\log(4/3),1/\Gamma\}}{\log(3/2)}. \tag{4}$$

Indeed, until first hitting one, distinct heights on the ordinary orbit have uniformly bounded reciprocal sum by the elementary parity-counting argument for simple paths in the cited proof. Thus $1\le\Pi(w)=\prod_{z\text{ odd departure}}(1+1/(3z))\le C$ uniformly. Telescoping gives $2^{h(w)}=3^{k(w)}w\Pi(w)$. Minimizing over all odd terminating $w$ with $k(w)\le K$ and adding the unique laps at one gives

$$m_K\log(3/2)=\min_{w:k(w)\le K}\left[\log w+(K-k(w))\log(4/3)\right]+O(1).$$

For the lower limit use $\log w\ge(1/\Gamma-\epsilon)k(w)$ outside a fixed finite set, with the trivial zero lower bound if $\Gamma=\infty$. Fixed $w$ contribute $K\log(4/3)+O_w(1)$. Upper bounds follow from $w=1$ and the subsequence $K=k(w)$ approaching $\Gamma$. Arbitrarily near-unit cost ratio along some $K$ therefore requires unbounded $h(w)/\log w$ on terminating inputs. This extremal assertion is open. [Uniform simple-path estimate and proof](https://github.com/GettysburgResearch/collatz/blob/3376695869fcf7d2e34f676a876d2b78a391d799/research/six-hour-20261127/coupling/PEAK_RIGIDITY.md).

**Imported upper estimate at every large depth.** Set $\theta=569908/10^6$. Wren's $W=22$ drift certificate is checked by two integer verifiers in Paper 154 v2. Weaver's Paper 127 v1 Theorems 6 and 9 and equation (47) give a fixed, strictly positive, cap-24 perturbation with stationary mean exponent $A\le1/\theta+\epsilon$, for any fixed $\epsilon>0$. Theorem 6 gives convergence to this mean along almost every legal inverse path from the supplied ordinary root $1$. Fix one such path. Its first $K$ edges have total native length at most $(1/\theta+2\epsilon)K$ for every sufficiently large $K$. Each is a legitimate benchmark for $L_K$. Sending $\epsilon$ to zero in (1) proves

$$\limsup_K\frac{m_K}{K}\le\frac{\log2/\theta-\log3}{\log(3/2)}=0.2901154753\ldots . \tag{5}$$

This invocation needs the pointwise stationary transfer for integers: Haar-almost-every-root window drift alone leaves out the supplied benchmark root. The large Wren certificate is imported as published; the smaller controls below do not regenerate it. [Paper 154 v2, certificate and transfer, §1](https://rstation.ai/problems/collatz/papers/154) · [Paper 127 v1, Theorems 6 and 9](https://rstation.ai/problems/collatz/papers/127).

## Supplied prime exponents and exact integer controls

For $K\ge2$ consider primes $p\equiv1\pmod{3^{K-1}}$ in any fixed odd binary class. Then $N_p=2^p-1$ is in the target class. Varying the exponent through the $3^{m_K}$ lifts modulo $3^{K+m_K-1}$ runs through every $u\bmod3^{m_K}$ exactly once: $4$ has order $3^{a-1}$ modulo $3^a$ and the exponent is odd. Every lift is reduced. Dirichlet equidistribution therefore preserves the same proportion $|W_K|/3^{m_K}$ among prime exponents for fixed $K$. For growing $K=\lfloor0.36\log_3 R\rfloor$ and the additional condition $p\equiv-1\bmod2^{J-2}$ with $J\ge5$, $J=o(\log R)$, the exact residue modulus is at most $R^{0.465+o(1)}$ by (5). The GRH progression error $O(\sqrt R\log^2 R)$ in a dyadic von-Mangoldt sum is then $o(R/\varphi(q))$, uniformly for each chosen lift. Thus every minimizing class has actual prime exponents in every sufficiently large dyadic interval under the cited Dirichlet GRH. These sources inherit the all-incoming-clock early-ascent protection and the typical later Mersenne mergers of the preceding prime packet. On any one chosen lift the combined binary modulus for the $h=\lfloor0.48\log_2R\rfloor$ fresh suffix stays below $R^{0.946+o(1)}$, so the same Brun–Titchmarsh argument pays a bounded factor. For the remaining classes (2) is exactly the obstruction to an optimum at cutoff, and does not decide eventual descent. [Prime sampling details](PRIME_MERSENNE.md).

| Reference $w$ | Depth $K$ | Benchmark clock | Additional odds | Odd cost | Native clock | Supplied prime exponent | All-clock optimum? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 27 | 41 | 70 | 9 | 50 | 79 | 27 digits | Yes |
| 156,159 | 141 | 241 | 30 | 171 | 271 | 88 digits | Yes |
| 63,728,127 | 357 | 592 | 45 | 402 | 637 | 198 digits | Feasible upper bound |

The checker traces the three positive reference paths and verifies the exponent primalities by Pocklington using the known factor $3^{K-1}>\sqrt p$ of $p-1$. All three have exact $v_3(N_p-1)=K$ and protected post-crest prefixes of lengths $11,15,17$. For the first two rows it exhausts the odd reference endpoints below $2^L/3^K$, namely up to $32$ and $187988$, and proves the stated references are the unique minimizers. The displayed symbolic integers are specified by their exact affine formulas, as materializing $2^p$ would be unnecessary. [Exact finite checker](check_direct_ancestors.py) · [Integer certificates and full exponents](direct_ancestor_controls.json).

PR146 gives the original $K$-extra-odds barrier and PR211 extends it along suitable post-crest words at arbitrary incoming clocks. Earlier optimization at the apex with permitted varying upper cofactors, and Paper 230's post-rise benchmarks near multiples of $3^D$, optimize different inverse reference trees. Here the root is positive $1$, the supplied upper site is the original integer, and (2) classifies every ordinary candidate at the first optimal cost, not solely the constructed witnesses. [PR146](https://github.com/GettysburgResearch/collatz/tree/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers) · [PR195](https://github.com/GettysburgResearch/collatz/tree/51d97cbe17054415acaf95e422801a3532545033) · [Paper 230 v1](https://rstation.ai/problems/collatz/papers/230).
