# Odd departures forced by the arithmetic of a smaller source

**SOURCE-QUALIFIED written theorem.** Let $T(2x)=x$, $T(2x+1)=3x+2$, and count odd departures under this shortcut. Fix any $U=2^p a-1$, with $p\ge1$, $a\ge1$ and $3\nmid a$. Its first $p$ departures are odd. For a supplied smaller ordinary integer $0<x<U$, write $x+1=2^n b$ with $b$ odd. Suppose its trajectory actually visits $T^iU$ for some $0\le i\le p$ at any incoming clock. Then that clock is $n+j$, $j>0$. Write $q$ for the number of odd departures during those $j$ steps following the lower ascent. The grade measured from $x$ is $n+q$.

Put $P=\log(U+1)$, using natural logarithms. Fix a finite set of primes $S$ containing 2 and 3. Remove from the reduced rational number $b/a$ all its prime factors in $S$, including factors in the denominator. Call the remaining positive rational $r$. Let $H(r)$ be the larger of its reduced numerator and denominator, and put $L=\max(1,\log H(r))$. At **every** such meeting,

$$
 (q-i)\log(3/2)\ \ge\ P-C_S L\log(e(1+P)/L).                   \tag{1}
$$

In particular, whenever $\log H(r)=o(P)$ the mandatory surplus is $(1-o(1))P/\log(3/2)$ or greater. If all primes of $b/a$ belong to fixed $S$, the loss in (1) is $O_S(\log(2+P))$. For $U=2^p-1$ and $x=2^f-1$, $1\le f<p$, this means that a visit to **any** site of the entire upper ascent requires, after the lower crest,

$$
             q-i\ \ge\ 1.70951129\ldots\,p-O(\log(2+p)),
             \qquad 1.70951129\ldots=\frac{\log2}{\log(3/2)} .
$$

This applies to every positive exponent $p$ without a congruence condition, to all incoming clocks, and without assuming convergence. The conclusion also applies to every smaller shifted $S$-smooth input. The physical visit is the hypothesis. The theorem does not assert its existence.

## From a physical word to a linear form

Shift heights by one. An odd input multiplies shifted height by $3/2$ and an even input sends $Y$ to $(Y+1)/2$. Thus at a meeting the total number of lower odds exceeds $i$, since $x+1<U+1$ and shifted height never grows on an even step. If the lower clock were $h\le n$, it would equal this count and the lower shifted endpoint would be $2^{n-h}3^h b$. The upper one is $2^{p-i}3^ia$, with ternary valuation exactly $i$. This rules out $h>i$. Thus $h=n+j$ with $j>0$, as in PR197's physical prepeak argument. The lower shifted height after its $n$-step ramp is $3^n b$, which is odd, so its next departure is even.

Let $B_0=0$. After $k$ post-ascent steps, append an even departure by $B_{k+1}=B_k+2^k$, and an odd one by $B_{k+1}=3B_k$. The meeting identity in positive integers is

$$
 Z=2^{p-i+j}3^i a=3^{n+q}b+B_j,\qquad 0<B_j\le3^q(2^{j-q}-1).   \tag{2}
$$

For the last inequality, divide $B_j$ by $3^q$. The even letter at date $k$ contributes $2^k/3^{Q_k}$, where $Q_k$ is the number of earlier post-ascent odds. If it is the $(e+1)$th even letter, $k=e+Q_k$, so its term is at most $2^e$. The first post-ascent departure guarantees strict positivity. This normalized even-carry bound also appears in the extra-cost portion of [the earlier peak-rigidity packet](https://github.com/GettysburgResearch/collatz/blob/3376695869fcf7d2e34f676a876d2b78a391d799/research/six-hour-20261127/coupling/PEAK_RIGIDITY.md).

Let $\delta=B_j/Z$. Then

$$
    0<\delta < e^{-P}(3/2)^{q-i},\qquad
    \Lambda=\log\frac{Z}{3^{n+q}b}=-\log(1-\delta)>0 .             \tag{3}
$$

If $q-i\ge P/\log(3/2)$ or $\delta\ge1/2$, (1) holds immediately after increasing an absolute constant. In the remaining case $i,n,q,\log a,\log b=O(1+P)$. Also $Z\le2\cdot3^{n+q}b$ forces $j=O(1+P)$, even though the incoming clock was unrestricted. Before removing the $S$-part, the linear form is

$$
      (p-i+j)\log2+(i-n-q)\log3-\log(b/a).
$$

After its removal this is a sum of $\log\pi$ for $\pi\in S$ with integer coefficients $O_S(1+P)$, together with $-\log r$ when $r\ne1$. The latter coefficient is exactly $-1$. Matveev's Corollary 2.3 over $\mathbb Q$ gives $\log|\Lambda|>-C\Omega\log(eB)$. Take fixed $A_\pi=\log\pi$, and order $r$ last with $A_r=L$. Then $\Omega=O_S(L)$ and the theorem's weighted coefficient bound (1.3) is $B=O_S((1+P)/L)$, using $L\le1+P$. When $r=1$ omit that term and use $B=O_S(1+P)$. Multiplicative independence of the full set is unnecessary for the corollary. Finally $\Lambda\le2\delta$ in the remaining case. Inserting (3) gives (1). [Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers II*, (1.3), (2.4), Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314).

The version with only two logarithms has a modest asymptotic constant. If $U=2^p-1$ and $x+1=2^n3^v$, Bondareva–Luchin–Salikhov Theorem 1, with constant coefficient zero, bounds a nonzero $A\log2-B\log3$ below by $\max(|A|,|B|)^{-4.116201}$ for sufficiently large coefficients. Thus for these sources one can take $4.116201\log(2+p)+O(1)$ as the loss on the right side of (1). The coefficient upper bounds are absolute multiples of $p$ and bounded coefficients can be absorbed into the additive constant. [Primary theorem](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [PR213's earlier application to positive cycles](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/ODD_HEIGHT_PRESSURE.md).

## The prime factors required by cheaper visitors

A fixed positive reduction in the leading coefficient of (1) forces $L\gg_S P$. Indeed $u\log(e/u)\to0$ as $u\downarrow0$. This imposes exponential height on the part of the lower-to-upper cofactor ratio that is supported outside any prescribed finite set of primes.

There is also a uniform lower bound on its largest prime factor. Suppose $P\to\infty$ through actual meetings with $(q-i)\log(3/2)\le(1-\epsilon)P$ for a fixed $\epsilon>0$. Then the largest prime dividing the numerator or denominator of $b/a$ is at least

$$
    (1-o(1))\,\frac{\log P\,\log\log P}{\log\log\log P}.             \tag{4}
$$

To see this, fix $\theta<1$ positive, put $y=\theta\log P\log\log P/\log\log\log P$, and suppose $b/a$ is supported on primes at most $y$. Use one logarithm per prime $\le y$ and $B^*=\max|b_k|=O(1+P)$ in Matveev Corollary 2.3, including the primes 2 and 3 in the list. The coefficient bound is uniform in the prime list, since $a,b\le e^P$. Its explicit $C_1(m)\le2^{6m+20}$, where $m=\pi(y)$, and $\Omega\le(\log y)^m$. The classical prime number theorem implies $m=(\theta+o(1))\log P/\log\log\log P$. Thus the lower bound on $\log|\Lambda|$ is $-P^{\theta+o(1)}$. This contradicts the upper bound $-\epsilon P+O(1)$ from (3). Since every $\theta<1$ is excluded, (4) follows.

PR195 bounds the best attainable odd cost at a specified ascent endpoint entered on its other edge, optimizing over the upper cofactor. PR197 proves $h>n+i$ for an unrestricted smaller source and every upper ascent index. The present cost is on **post-ascent odd departures**, uses the reduced cofactor ratio of the actual pair, and has no arrival-edge condition. Their universal-source results continue to apply when the ratio is arithmetically too large for (1) to give a positive surplus. [PR195, exact signed-word cost](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/FIRST_MEETING.md) · [PR197, all source clocks](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/unconventional/ALL_SOURCE_CLOCKS.md).

## Consequence for a finite exponent cover

Take $a=1$ and $p\equiv-1\bmod2^{J-2}$, $J\ge5$. The explicit virtual rational proof in [the prime-exponent packet](PRIME_MERSENNE.md) excludes all weighted earlier-crest comparisons at a common postcrest date through $J$. The cited peak-rigidity classification with $3J<p$ extends this to all positive smaller $x$ at all independently chosen clocks up to $v_2(x+1)+J$, against all $J+1$ upper postcrest sites. By (1), for every shorter Mersenne and all sufficiently large $p$, its entire native path through its own crest plus $J$ also avoids every upper **precrest** site: here $q\le J\le 2+\log_2(p+1)$, far below the mandatory cost. Hence the two whole native paths, through $J$ beyond both crests, are disjoint even as ungraded sets of actual integers. Arbitrarily large primes with this obstruction and arbitrarily large simultaneous ternary protections exist by the prime-exponent construction. On most such primes a growing collection of specified smaller sources subsequently rejoins.

## Bounded ordinary controls

The verifier exhausts every physical visit from $x<U\le1024$ through lower clock 128 and every admissible factorization $U+1=2^pa$, including nonmaximal upper ascents. It checks (2), its normalized carry bound, (3)'s relative carry inequality with signed $q-i$, and the impossibility of $h\le n$. Its 8,934 visits include 3,306 even lower starts, 2,808 with $5\mid a$, 4,883 nonmaximal upper factorizations and 41 with $q<i$. For example, $63$ takes six initial odds and then two even departures to reach the first successor of $121$. Here $q-i=-1$, while the lower full count still exceeds the upper count. The asymptotic logarithm estimate rests on Matveev's theorem. [Integer verifier](check_ascent.py) · [Exact controls](ascent_controls.json).
