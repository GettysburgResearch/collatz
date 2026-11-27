# Distribution of the full reduced denominator on a fixed weight slice

Fix \(0<\epsilon<1/2\). Give the words \(w\in\{0,1\}^n\) of exact weight \(u\) the uniform probability measure, where \(p=u/n\in[\epsilon,1-\epsilon]\). At an initial cut write \(s_i=\sum_{t<i}w_t\). The chronological affine numerator and the absolute determinant are
\[
 C(w)=\sum_{i:w_i=1}2^i3^{u-1-s_i},\qquad D=|2^n-3^u| .
\]
Here \(D\) is positive and prime to 6. Set \(G=\gcd(C,D)\), \(d=D/G\). In a positive determinant slice \(d\) is the common reduced denominator of the genuine positive rational shortcut cycle. Negative determinant slices produce signed rational cycles and obey the same counting statements.

**Theorem 1 (all residue classes).** There are \(c_\epsilon,C_\epsilon>0\) such that uniformly in every integer \(g\ge1\) coprime to 6 and every residue \(a\bmod g\),
\[
 \left|\Pr(C\equiv a\bmod g)-1/g\right|
 \ \le C_\epsilon e^{-c_\epsilon\sqrt n}.                            \tag{1}
\]
The modulus can grow arbitrarily quickly with \(n\). This is an additive estimate on each mass. At fixed \(g\) the proof gives exponential decay in \(n\), with no hypothesis on the order of 2 or 3.

**Theorem 2 (entire divisor distribution).** The law of \(d\) has total variation distance at most \(C_\epsilon e^{-c_\epsilon\sqrt n}\) from the probability measure
\[
                         e\longmapsto\frac{\varphi(e)}{D},
                  \qquad e\mid D .                                    \tag{2}
\]
The same statements about \(G,d\), including the variation bound, hold for uniform **primitive necklaces** of type \((n,u)\) whenever the class is nonempty. An individual residue \(C\bmod g\) needs a rooted cut; \(G\) and \(d\) are rotation invariant.

In particular, with natural logarithms,
\[
 \mathbb E\log G
  =\sum_{\ell^j\mid D,\ \ell\ {\rm prime},\,j\ge1}\frac{\log\ell}{\ell^j}
      +O_\epsilon(n e^{-c_\epsilon\sqrt n})
  =O_\epsilon(\log(n+2)).                                             \tag{3}
\]
For each fixed \(\delta>0\) the probability that \(\log G\ge\delta n\) is at most \(e^{-c_{\epsilon,\delta} n}\) for all sufficiently large \(n\). Thus the loss of denominator bits is logarithmic in mean even on critical weight slices. A probability bound of the size in (1) or (2) leaves room for exceptional individual necklaces.

The empirical residue model in Eldar Sultanow's *Same Shadows, Different Forests*, v3, §5, predicts precisely (2) and measures relative discrepancies on large algebraic factors at lengths through forty. This theorem supplies an asymptotic in total variation on macroscopic exact-weight slices. It gives no relative approximation for events whose model probabilities are smaller than its absolute error. In particular, the integral-cycle event \(d=1\) has model probability \(1/D\). Tsui's project report §7 states a fixed-prime estimate under an order condition. The proof below is independent of that report. The estimate here covers moving composite moduli and the arithmetic law of their full gcd with \(C\). The integer numerators' injectivity at fixed length and weight is classical and appears explicitly in freelan_lab's Paper 208, Lemma 4, which credits Tao and Weaver. [Denominator heuristic following Proposition 3](https://www.preprints.org/manuscript/202610.2552), [Tsui's Theorem 4](https://github.com/lucastsui/collatz-research/blob/main/REPORT.md), [freelan_lab 208 v1, Lemma 4](https://rstation.ai/problems/collatz/papers/208/v1)

## 1. Fourier contraction for small and intermediate moduli

There are \(m=\lfloor n/2\rfloor\) consecutive disjoint pairs. When \(n\) is odd leave the last site as a singleton. First choose all bits independently, each with probability \(p=u/n\) of a one, then condition on total weight \(u\). The conditioning event has probability at least \(1/(n+1)\), since \(u\) is a mode of \({\rm Binomial}(n,p)\). Under the unconditioned law the pair weights \(r_j=w_{2j}+w_{2j+1}\) are independent binomial variables with two trials. Given these weights and the singleton, mixed pairs have independent fair orientations. Conditioning the original law on total weight preserves that conditional orientation law.

Fix \(1\le k<g\) and define modular frequencies on **all** unconditioned pair-weight sequences by
\[
 K_j=k\,2^{2j}3^{u-1-\sum_{i<j}r_i}\pmod g,\qquad
 3^{r_j}K_{j+1}=4K_j\pmod g.                                         \tag{4}
\]
Negative powers away from the conditioning event are defined using invertibility mod \(g\). No \(K_j\) is zero, even for imprimitive characters \(k\), since each multiplier in (4) is a unit. On total-weight-\(u\) sequences, exchanging a mixed pair \(10\to01\) changes \(kC\) by \(K_j\). The pair contains exactly one odd, located after \(\sum_{i<j}r_i\) earlier odds. Other contributions remain fixed. Thus conditioning on all pair weights and the singleton, then averaging over orientations, bounds the absolute value of the \(k\)-th Fourier coefficient by the conditional mean of
\[
                            \prod_{j:r_j=1}|\cos(\pi K_j/g)|.
\]
The absolute cosine is independent of the representative. Dropping the condition in this nonnegative average costs at most \(n+1\).

Let \(L_g=1+\lceil\log_4 g\rceil\). Among every \(L_g\) consecutive frequencies, some centered representative has \(|K_j|\ge g/20\). Otherwise each internal congruence in (4) would be an equality of centered integers: the absolute difference of its sides is at most \(13g/20<g\). Iteration gives \(4^{L_g-1}K_{\rm first}=3^R K_{\rm last}\) with \(R\ge0\). Hence \(4^{L_g-1}\mid K_{\rm last}\), impossible for a nonzero integer of magnitude less than \(g/20\).

Partition the \(m\) complete pairs into disjoint groups of \(L_g\), ignoring the final remainder. Given the history before such a group, the first large-frequency index is determined from weights strictly before that index. Its own pair has mixed probability \(2p(1-p)\). This statement can be verified by summing over the possible first indices: each determining event is measurable with respect to the earlier pairs. Every group has such an index regardless of its future weights. On a mixed pair at that index the cosine factor is at most \(\cos(\pi/20)\); all other factors are at most one. The expected product within each group conditional on its starting history is thus at most
\[
 \rho_\epsilon=1-2\epsilon(1-\epsilon)(1-\cos(\pi/20))<1 .
\]
Iterated conditional expectation gives, after the exact-weight conditioning,
\[
 |\widehat\mu_g(k)|\le(n+1)\rho_\epsilon^{\lfloor m/L_g\rfloor},\qquad
 |\Pr(C=a\bmod g)-1/g|\le(n+1)\rho_\epsilon^{\lfloor m/L_g\rfloor}.   \tag{5}
\]
The second bound is finite Fourier inversion. For \(2\le g\le\exp(\sqrt n)\), (5) is \(O_\epsilon(e^{-c_\epsilon\sqrt n})\). It also gives relative equidistribution uniformly over \(g\le\exp(a_\epsilon\sqrt n)\) for a sufficiently small positive \(a_\epsilon\).

## 2. Recovery of a missing contiguous block

An \(s\)-bit block of fixed weight \(r\) has distinct integer numerator for every possible word. For \(r>0\) its first odd index is \(v_2(C)\), since the coefficient of the lowest power of 2 is odd. Subtract that contribution \(2^i3^{r-1}\) and repeat to recover the remaining odd indices. The all-zero case has just one word. Every such numerator lies in \([0,3^s-2^s]\), by induction under appending a bit, which sends \(C\) to \(C\) or \(3C+2^s\).

If \(3^s\le g\) and the outside \(n-s\) bits are fixed, their weight determines the weight of the omitted block. In the full numerator its block numerator is multiplied by \(2^{\text{prefix length}}3^{\text{suffix weight}}\); all other terms depend only on the outside bits and that block weight. This multiplier is invertible mod \(g\). Distinct block numerators lie in an interval shorter than \(g\), so at most one completion can give any prescribed residue. This holds at any fixed block position, in particular at the initial one.

Write \(q=\max(p,1-p)\le1-\epsilon\). Also under the unconditioned Bernoulli law, for each outside configuration the simultaneous conditions \(|w|=u\) and \(C(w)=a\bmod g\) allow at most one internal word. Its probability is at most \(q^s\). Dividing by the weight probability gives the finite bound
\[
                    \Pr(C=a\bmod g)\le(n+1)q^{\min(n,\lfloor\log_3 g\rfloor)}. \tag{6}
\]
In particular when \(g>\exp(\sqrt n)\), (6) and \(1/g<e^{-\sqrt n}\) complete (1). The cap at \(n\) covers moduli larger than every possible numerator.

If \(D>0\) or \(D=|2^n-3^u|\) is the negative-determinant magnitude, always \(D<3^n\). The event \(G\ge e^{\delta n}\) implies \(g\mid C\) for some divisor \(g\mid D\) with \(g\ge e^{\delta n}\). Formula (6) gives exponentially small probability at each such divisor. The elementary bound \(\tau(D)=e^{o(n)}\) suffices to sum them. To see this bound uniformly for \(D<3^n\), fix \(\eta>0\). For every sufficiently large prime \(\ell\), \(a+1\le2^a\le\ell^{\eta a}\), and for each of the finitely many smaller primes \(a+1\le C_{\eta,\ell}\ell^{\eta a}\) for all \(a\). Multiply over prime powers to obtain \(\tau(D)\ll_\eta D^\eta\).

## 3. Logarithmic cancellation

A uniform residue \(R\bmod D\) obeys \(\Pr(\ell^j\mid R)=\ell^{-j}\) for every prime power dividing \(D\). Summing the logarithmic divisibility indicators gives
\[
 \mathbb E\log G=\sum_{\ell^j\mid D}(\log\ell)\Pr(\ell^j\mid C).
\]
The total coefficient weight is exactly \(\log D=O(n)\). Theorem 1 immediately gives the main term and error in (3). To obtain its final bound, majorize the main term by \(\sum_{\ell\mid D}\log\ell/(\ell-1)\). For \(\ell>n\) the sum is bounded by \(\log D/(n-1)=O(1)\). For \(\ell\le n\), dyadic grouping and the elementary Chebyshev estimate \(\sum_{\ell\le t}\log\ell=O(t)\) give \(O(\log(n+2))\). Chebyshev here follows, for example, by noting that all primes \(m<\ell\le2m\) divide \(\binom{2m}{m}<4^m\) and summing dyadic intervals.

## 4. From divisible events to total variation

Let \(G_0=\gcd(R,D)\) for \(R\) uniform modulo \(D\), so \(\Pr(b\mid G_0)=1/b\) for \(b\mid D\). Write \(E_n=C_\epsilon e^{-c_\epsilon\sqrt n}\) for the error in any one divisibility probability from (1). We explain why inversion on the divisor lattice preserves stretched-exponential accuracy even when \(\tau(D)\) itself is larger than \(1/E_n\).

The total number \(N=\sum_{\ell\mid D}v_\ell(D)\) of prime-power choices is \(O(n)\). Indeed \(2^N\le D<3^n\). The number of divisors with at most \(h\) distinct prime factors is at most \((N+1)^h\), by choosing up to \(h\) prime powers and padding the ordered list with an empty symbol. Write \(\omega(b)\) for the number of distinct primes of \(b\). Set \(S_D=\sum_{\ell\mid D}1/\ell=O(\log(n+2))\), using at most \(N\) distinct positive integers. Also
\[
 \sum_{b\mid D}\frac1b\le\prod_{\ell\mid D}(1-1/\ell)^{-1}
                  \le \exp(2S_D)=(n+2)^{O(1)} .                     \tag{7}
\]

Fix \(b\mid D\) with \(\omega(b)\le h\). The event \(G=b\) is \(b\mid G\) with none of \(b\ell\mid G\) over primes \(\ell\mid D/b\). This includes primes already dividing \(b\) at a smaller exponent. Use ordinary inclusion–exclusion through order \(h-1\). The absolute remainder lies below the positive sum of all order-\(h\) intersections \(b\prod_{\ell\in I}\ell\mid G\). The same statement holds for \(G_0\). The two truncated sums differ by at most \((N+1)^h E_n\) after increasing the harmless fixed counting constant if needed; the subsets of size at most \(h-1\) inject into padded lists. The actual order-\(h\) remainder bound differs from its model bound by at most \((N+1)^h E_n\). The model remainder bound is at most
\[
                             \frac1b\,\frac{S_D^h}{h!}.
\]
Summing over all such \(b\), their total absolute mass discrepancy is at most \(2(N+1)^{2h}E_n+2(n+2)^{O(1)} S_D^h/h!\). For the omitted tail \(\omega(G)>h\), the union bound over products of \(h\) distinct primes gives a further \((N+1)^h E_n+S_D^h/h!\); for \(G_0\) it costs at most \(S_D^h/h!\).

Take \(h=\lfloor a_\epsilon\sqrt n/\log(n+2)\rfloor\) with fixed \(a_\epsilon>0\) sufficiently small. The first error remains \(e^{-\Omega_\epsilon(\sqrt n)}\). By \(h!\ge(h/e)^h\) and \(S_D=O(\log n)\), the factorial term has the same type of bound. Enlarge constants for small \(n\). This proves stretched-exponential total variation for \(G\). The bijection \(b\mapsto D/b\) preserves the distance and the uniform-residue count gives (2).

Finally, if \(H(p)=-p\log p-(1-p)\log(1-p)\), the number of imprimitive rooted words in the slice is at most \(\sum_{j\ge2,j\mid\gcd(n,u)}\binom{n/j}{u/j}\le n e^{nH(p)/2}\). There are at least \(e^{nH(p)}/(n+1)\) rooted words in the slice because \(u\) is a binomial mode. Conditioning on primitivity therefore changes the law by \(e^{-\Omega_\epsilon(n)}\). Every primitive necklace has exactly \(n\) distinct cuts, and the rotation identity \(2C(\mathrm{rot}\,w)=3^{w_0}C(w)+w_0(2^n-3^u)\) preserves the full gcd. This proves the necklace assertion.

## Scope at the integer extreme

For a critical sequence \(u=\lfloor n\log_3 2\rfloor\), \(\binom nu=\exp(nH(\log_3 2)+o(n))\) with \(H(\log_3 2)<\log2\), whereas \(D=2^{n-O(\log n)}\) by Rhin. Hence the distribution of \(C\bmod D\) itself has support in an exponentially small fraction of all \(D\) residue classes. Its total variation distance from uniform tends to one. The rooted probability of the single class \(C=0\bmod D\) is either zero or at least \(1/\binom nu\). Since \(D/\binom nu\) grows exponentially on this critical sequence, relative asymptotics \( \Pr(C=0\bmod D)\sim 1/D\) are impossible there, whatever the answer to ordinary cycle exclusion. Projecting that residue to the gcd loses enough information for (2) to hold. The error in (2), multiplied by the number of necklaces, is still too large to decide whether any individual ordinary cycle exists.
