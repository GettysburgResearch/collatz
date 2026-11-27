# A density-one lower bound on the least possible rational denominator

The [ascent census](ASCENT_CENSUS.md) gives the stronger unrestricted denominator exponent by a separate argument. The independent real-affine survival estimate below also applies to finite words far from any periodic orbit.

For each physical period \(n\ge2\) let \(d_{\min}(n)\) be the least common reduced denominator among all nonzero signed rational shortcut cycles of **least** period \(n\), with infinity allowed for an empty family. The following results are unconditional and do not use any quantitative irrationality estimate or the Subspace Theorem.

* For every positive function \(\phi(n)\to0\), the periods satisfying
\[
       d_{\min}(n)>\phi(n)\sqrt{\frac{n\log n}{\log\log n}}
                                                                        \tag{1}
\]
have natural density one. In particular every fixed power \((\log n)^a\) with \(a<1/2\) may multiply \(\sqrt n\) inside this lower bound.
* On a density-one set of periods \(n\), **every negative rational cycle** and every positive rational cycle whose gap obeys \(0<n\log2-u\log3\le\log3\) have \(d_C>n^{1/2+10^{-12}}\). This covers each nearest positive critical slice \(u=\lfloor n\log_3 2\rfloor\), and permits all gaps for the negative cycles. For any other fixed upper gap bound \(G>0\) the same result holds with some fixed exponent \(1/2+c_G>1/2\).

These statements concern **every necklace at the retained periods**, however atypical its parity ordering. A power-law count for distinct period vectors at fixed or growing denominator appears in the [companion arithmetic note](DENOMINATOR_CENSUS.md). Periods repeated by a nonminimal presentation do not count.

### Fair affine words above a real floor

Starting at \(y\ge0\), let the independent fair formal forward branches be \(E(y)=y/2\), \(O(y)=(3y+1)/2\). For absolute constants \(C,c>0\), every \(0<m\le1\), real \(y\ge0\), and integer \(t\ge0\) satisfy
\[
       \Pr_y\{Y_0,\ldots,Y_t\ge m\}
                    \le C(1+\sqrt{y})\exp(-c m t).                    \tag{2}
\]
This is a symbolic counting bound, even when \(y\) is not a native source for the chosen word.

To prove it put \(W(y)=1+\sqrt y\). Subadditivity of the square root gives \(\mathbb E_y\sqrt{Y_1}\le\rho\sqrt y+1/(2\sqrt2)\), where \(\rho=(1+\sqrt3)/(2\sqrt2)<1\). Hence for some fixed \(B>2\), \(r<1\), we have \(\mathbb E_y W(Y_1)\le r W(y)\) whenever \(y>B\). With \(\sigma\) the first time in \([0,B]\), for every \(t\) this gives \(\Pr_y(\sigma>t)\le r^t W(y)\), by iterating the drift killed on entrance. Choose a fixed \(a>0\) with \(e^a r<1\) and \(e^a<2\). Summing tails shows \(\mathbb E_y e^{a\sigma}\le C_0 W(y)\).

When the chain is in \([0,B]\), start a trial by waiting until the next odd letter, at clock \(J\ge1\) with \(\Pr(J=j)=2^{-j}\). Its state is then \((3y/2^{J-1}+1)/2\le(3B+1)/2\). Wait until the next entrance to \([0,B]\), allowing zero delay, and repeat the trial. From every trial's starting state its duration has exponential moment at \(a\) at most a fixed \(C_1>1\), by conditioning on \(J\) and using the entrance estimate at the bounded post-odd state. The full iid letters continue even after an actual visit below \(m\). The probability that the first \(K=\lceil\log_2(2B/m)\rceil\) letters of a trial are all even is \(2^{-K}\ge m/(4B)\); that trial then includes a state strictly below \(m\). Repeated conditioning on trial starts bounds the chance that none of the first \(j\) trials has this event by \((1-m/(4B))^j\). Independently of that calculation, the chance that the initial entrance and these \(j\) trials are not completed by time \(t\) is at most \(C_0 W(y)e^{-at}C_1^j\), by their successive conditional exponential-moment estimates. Take \(j=\lfloor c_1t\rfloor\) for a fixed sufficiently small \(c_1>0\). A union bound proves (2). No independence between the durations and the successful zero runs is needed.

### Rare cyclic states at a positive floor

Consider cyclic rational magnitudes of exact denominator \(d\) whose entire cycle has minimum at least \(m\le1\). For \(X\ge1\), their number through \(X\) is
\[
              O\big((1+\sqrt X)(dX)^{1-c_2m}\big)                    \tag{3}
\]
with absolute constants. Take \(t=\lfloor\log_2(dX)\rfloor\). A prescribed word has at most two possible positive numerator representatives up to \(dX\), by its dyadic congruence and \(dX<2^{t+1}\). For a positive cyclic magnitude through \(X\), applying the same formal word to \(X\) can only increase all intermediate states, by monotonicity; the resulting word from \(X\) stays above \(m\). The same implication holds for negative cycles because the positive-affine branches dominate the reflected branches step by step. Count such words using (2) times \(2^t\). Choose a smaller absolute \(c_2\le1/4\) if needed.

Use \(h=49/50\) in the elementary denominator-uniform state count from [DENOMINATOR_CENSUS.md](DENOMINATOR_CENSUS.md), and put \(\delta=c_2m\). For each sign, the total gap over exact-denominator-\(d\) cycles with minimum at least \(m\) is
\[
     \sum_{\substack{d_C=d\\ \min |C|\ge m}}g_C
            \ll (1+\log(1/m))d^{1-\delta/50}.                          \tag{4}
\]
In real magnitudes \([m,1]\), (3) bounds the number by \(O(d^{1-\delta})\), at individual cost \(O(1+\log(1/m))\); negative cycles have floor at least 1. For heights from 1 to \(X=d^\delta\), dyadic-shell summation of (3) at cost \(O(1/y)\) gives \(O(d^{1-\delta}X^{1/2})\), with an absolute constant, since \(0<\delta\le1/4\). For larger magnitudes the elementary bound and partial summation cost \(O(d X^{h-1})\). Substitution gives (4).

There are fewer than \(dm+1\) possible positive integer numerators at minima strictly below \(dm\), and indeed at most \(dm\), since each distinct positive numerator is counted once. Distinct cycles at one denominator and sign have distinct minima. Let \(D\) be large, take
\[
          m=A\frac{\log\log D}{\log D}<1
\]
with fixed \(A\) sufficiently large, and apply (4) for \(\sqrt D<d\le D\). The factor \(d^{-c_2m/50}\le(\log D)^{-c_2 A/100}\) wins any prescribed fixed negative power of \(\log D\) on choosing \(A\). Denominators \(d\le\sqrt D\) have total gap \(O(D)\) by the companion estimate. Counting small minima directly and the other cycles by Markov's inequality yields, uniformly for \(1/\log D\le b\le1\),
\[
        \#\{C:d_C\le D,\ g_C\ge b\}
                   \ll D^2\frac{\log\log D}{\log D}.                  \tag{5}
\]
Each smaller-gap period satisfies \(\|np\|\le b/\log3\). Since \(p\) is irrational, plain equidistribution gives \(o(N)\) such periods through \(N\) whenever \(b\to0\): compare to each fixed arc and then let its length tend to zero. For any \(D=o(\sqrt{N\log N/\log\log N})\), tending to infinity, (5) gives \(o(N)\) other periods. If \(D\le N^{1/4}\) this follows already from \(D^2\le\sqrt N\); otherwise \(\log D\asymp\log N\) in the comparison. To pass to (1) for a variable \(\phi\), discard \(n\le\sqrt N\) and use \(\sup_{n\ge\sqrt N}\phi(n)\to0\). Bounded denominator cutoffs can be increased to some slowly diverging \(D\), preserving the required little-oh relation. This proves (1).

### A concrete power for the critical slice

All negative cycles have magnitude floor at least 1, as proved in the companion note. For a positive cycle with gap at most \(G\), the minimum \(y\) is odd and contributes \(\log(1+1/(3y))\le G\); hence \(y\ge1/[3(e^G-1)]\). For \(G=\log3\) this lower floor is \(1/6\).

At \(m=1/6\), a direct 24-step bound makes the survival exponent in (3) explicit. The square-root drift has \(\rho<31/32\), so \(\mathbb E_y\sqrt{Y_{24}}\le(31/32)^{24}\sqrt y+16\le\sqrt y/2+16\). Put \(p_0=2^{-24},K=64/p_0,r_0=1-p_0/2\). From \(y\le B=2^{23}/6\), the all-even word exits below \(1/6\). Thus the expectation of \((K+\sqrt{Y_{24}})\) restricted to survival is at most \(K(1-p_0)+\sqrt y/2+16\le r_0(K+\sqrt y)\). At \(y>B\) discard the survival condition: the bound is \(K+\sqrt y/2+16\le r_0(K+\sqrt y)\), since \((r_0-1/2)\sqrt B\ge48\). Iterating, and dropping any final short block, gives survival probability \(\ll(1+\sqrt y)2^{-2^{-30}t}\). Indeed \(r_0^{\lfloor t/24\rfloor}\le2\exp(-2^{-24}t/48)\) and \(2^{-24}/48>2^{-30}\log2\).

Use (4) with \(\delta=2^{-30}\). This yields \(O(D^{2-\kappa})\) total gap at denominators through \(D\) for every negative cycle and every positive gap at most \(\log3\), with \(\kappa=2^{-30}/50\). Put \(D=N^{1/2+10^{-12}}\) and separate gaps smaller than \(N^{-10^{-12}}\). The smaller ones have \(o(N)\) distinct possible periods by equidistribution. The others number \(O(N^{10^{-12}}D^{2-\kappa})=o(N)\), since \((1/2+10^{-12})(2-\kappa)+10^{-12}<1\). This proves the stated explicit power. Formula (4) with each fixed positive floor proves the qualitative version for every fixed \(G\). The result does not exclude exceptional periods, including any particular ordinary integer cycle. All positive or negative words are subject to testing their *full reduced* denominator.

The fair-word first-passage idea is related to the existing integer source-floor literature. In that setting the source and its size are large and the additive real correction is correspondingly small. Here the relevant real heights can approach zero while numerator and denominator both vary, so the uniform escape rate linear in the real floor is needed. The steps establishing it above use elementary probability only. [Weaver 176, §5.3](https://rstation.ai/problems/collatz/papers/176/v1), [Weaver 177, §§7–8](https://rstation.ai/problems/collatz/papers/177/v1)
