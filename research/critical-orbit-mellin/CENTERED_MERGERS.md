# Ternary precision with unequal forward and reverse clocks

**PROPOSED.** Let \(T\) be the shortcut map. Write \(d(x)=v_3(2x+1)\) and \(P(x)=(2x+1)^2/3^{d(x)}\) on all positive integers. The native section is \(x\equiv1\bmod3\). We study high-depth sources \(y=(3^v u-1)/2\), where \(v\ge1\) and \(u>0\) is an odd 3-unit. A cheaper merger has \(P(m)<P(y)\) and \(T^t(m)=T^a(y)\). Allowing every positive \(m\), even outside the section, strengthens the failure statements below.

The repository's [T-ASTRA-026](../astra-critical-mass/REMAINDER_CANCELLATION.md) supplies exact equal-clock remainder cancellation. [T-ASTRA-030](../astra-critical-mass/CLOCK_DEFECT.md) proves its necessity for **every** source when both clocks fit a fixed linear precision budget. Here only the forward clock is bounded in the ternary measure estimate. The reverse clock runs to infinity there. The ordinary transfer in this file permits a reverse clock growing with the range of \(u\).

## Claims

For a binary forward word \(w\) of length \(a\) and weight \(r\), put \(T_w(y)=(3^r y+A_w)/2^a\) and \(g_w=2A_w-3^r\). Call the word resistant if its weight is maximal among length-\(a\) words with the same \(g_w\). This is exactly a bucket of equal shifted remainders at fixed length. For \(a=0\) use the empty word.

1. Fix any \(1/2<\theta<1\). For some \(K>1\), independently of \(v,a,w\), the normalized Haar probability on \(u\in\mathbb Z_3^\times\) that the target \(T_w(y)\) admits any **off-center** ideal cheaper-rank reverse word is at most \(K^{a+1}(3/4)^{\theta v}\). The exact necessary ideal test and the meaning of off-center appear below. Every reverse depth is covered by this bound.
2. In an on-center merger the arm lengths agree, the centered numerators agree, and an actual strict rank reduction requires a larger weight on the competing arm. For \(v>a\), every such alternative really gives a cheaper ordinary section source for each \(y\) following \(w\). The proportion of resistant length-\(a\) words is at least \(2^{-a}\binom{a}{\lfloor a/2\rfloor}\).
3. There are absolute \(c,C,\eta>0\) such that for all sufficiently large \(v\), \(0\le a\le\eta v\), \(R\ge0\), and \(U\ge C2^a4^R\), at least \(c/\sqrt{a+1}\) of the eligible \(1\le u\le U\) admit **no cheaper merger** with forward arm at most \(a\) and reverse arm at most \(R\). For the special case \(a=0\) the fraction admitting a pure inverse merger through \(R\) is \(O_\theta((3/4)^{\theta v})\). This does not say every resistant word fails for every individual source.

## Necessary rank inequality

Take the reverse arm from \(m\) to the common endpoint without repetitions, removing loops if needed. On finite simple paths the product of \(1+1/(3x)\) over odd inputs is at most an absolute constant \(G\), by the [uniform reciprocal bound](CRITICAL_MOMENT.md). The corresponding product on the forward arm from \(y\) is at least one. Comparing the exact affine products for the two paths gives
\[
 \frac m y\ \ge\ G^{-1}2^{t-a}3^{r-q},
\]
where \(q\) is the reverse word's odd count. Since \((2m+1)/(2y+1)\ge 2m/(3y)\), any genuine cheaper merger requires the ternary test
\[
 4^{t-a}3^{2(r-q)}3^{v-d(m)}\le C_0, \qquad C_0=9G^2/4.       \tag{1}
\]
In the Haar argument only ternary-integral inverse branches and (1) are demanded. Dyadic and positive ordinary realization are not assumed for this upper count.

## Inverse words at a dyadic rational center

The forward endpoint is
\[
 \xi+2^{-a-1}3^{V}u,\qquad \xi=g_w/2^{a+1},\quad V=v+r.
\]
The numerator \(g_w\) is odd. Reverse letters are \(z\mapsto2z\) and \(z\mapsto(2z-1)/3\), the latter only when ternary-integral. Before and including the \(V\)-th odd reverse letter, a legal reverse word of length \(t\) gives
\[
 m=\zeta+2^{t-a-1}3^{V-q}u,                                  \tag{2}
\]
where \(\zeta\) is its reverse image of \(\xi\) and is ternary-integral. Prefix legality at the center follows by the same formula at each earlier time. Call the full word off-center when its formal reverse image of \(\xi\) differs from \(-1/2\); the image is a rational number whether or not all its branches at \(\xi\) are integral after the cutoff.

There is an absolute \(D>1\) with the following counting bounds for \(q\le V\). The number of center-legal words at \((t,q)\) is at most \(D^{a+1}2^{t-q}\). Among off-center words, the number with \(3^k\mid(2\zeta+1)\) is at most \(D^{a+1}2^{t-q}3^{-k}\) for integers \(k\ge0\). If any such word exists, \(2^{t-q}\ge D^{-a-1}3^k\).

To check this, \(|\xi|\le 2(3/2)^a\) by the finite affine remainder bound. Each real odd inverse keeps the absolute value below \(\max(1,|z|)\) and each even inverse doubles it. Hence \(|\zeta|\le 2(3/2)^a2^{t-q}\). Its reduced denominator divides \(2^{a+1}\), because its only potential other prime factor was 3 and it is ternary-integral. The integers \(2^{a+1}(2\zeta+1)\) therefore lie in an interval about zero of radius \(D^{a+1}2^{t-q}\). The nonzero multiples of \(3^k\) in this interval number at most twice that radius divided by \(3^k\), including when the interval is shorter than the modulus. Finally a given \(\zeta\) occurs for at most \(2^{a+1}\) words. If \(t>a+1\), after the first \(a+1\) reverse steps the center is an ordinary integer (possibly negative). From there every ternary-integral inverse step is a true parity inverse on integers. The last \(t-a-1\) letters are consequently recovered by forward iteration from \(\zeta\); there are at most \(2^{a+1}\) initial choices. For \(t\le a+1\) the same bound is immediate. Enlarge \(D\) to absorb this factor.

## Before the ternary precision runs out

Write \(p=\log_3 2\) and \(c_0=\log_3 C_0\). For \(q<V\), condition (1) reads
\[
 d(m)\ge V-q+2pt-q+r-2pa-c_0.                               \tag{3}
\]
If the last five terms together are negative, then \((2p-1)t<2pa+c_0\), so \(t=O(a+1)\). For an off-center word the nonzero numerator bound above gives \(d(\zeta)=O(a+1)\) in this case. When \(v\) exceeds a sufficiently large constant times \(a+1\), (2) forces \(d(m)=d(\zeta)\), while the right side of (3) is \(v-O(a+1)\). Such a word fails. For smaller \(v\), the final probability bound follows trivially by increasing \(K\).

In the remaining case (3) requires \(d(m)\ge V-q\), so \(3^{V-q}\mid 2\zeta+1\). For each eligible word the next required digits cost probability at most \(C\,4^{a-t}3^{q-r}\): after dividing \(2m+1\) by \(3^{V-q}\), (2) gives an affine unit multiple of Haar \(u\) plus a constant. The law of a shifted Haar unit is bounded by \(3/2\) times full Haar measure. The constant \(C\) absorbs the fixed \(C_0\). Thus at fixed \(q,t\) the total is bounded by
\[
 D_1^{a+1}3^{-V-r}(9/2)^q 2^{-t}.
\]
Nonemptiness requires \(2^{t-q}\ge D^{-a-1}3^{V-q}\), so summing \(2^{-t}\) on its possible tail costs at most \(2D^{a+1}2^{-q}3^{q-V}\). Summing over \(0\le q<V\) gives
\[
 D_2^{a+1}3^{-2V-r}\sum_{q<V}(27/4)^q
 \ \le\ D_3^{a+1}(3/4)^V.                                   \tag{4}
\]

## At and beyond the precision cutoff

Stop a branch at its first \(V\)-th odd reverse letter, at time \(t_0\ge V\). The number of possible prefixes there is at most \(D^{a+1}2^{t_0-V}\). For each prefix the cutoff state in (2) has a law bounded by \(3/2\) times Haar on \(\mathbb Z_3\).

A fixed continuation of length \(s\) and weight \(l\) selects a single class modulo \(3^l\) of the cutoff state. Each new odd inverse imposes one ternary digit and each even inverse has unit slope in \(\mathbb Z_3\). For full Haar input, conditional on this class the resulting state \(m\) is full Haar. Also \(\mathbb E\,3^{\theta d(m)}<\infty\) for \(\theta<1\) by the geometric distribution of \(d(m)\). Markov's inequality applied to the reciprocal of (1) raised to \(\theta\) gives, after summing over all continuation words and \(s\ge0\), the bound per prefix
\[
 C_\theta (4^a3^v4^{-t_0})^\theta
 \sum_{s\ge0}\left(\frac{1+3^{2\theta-1}}{4^\theta}\right)^s.
\]
The ratio is less than one. Its logarithm is strictly convex in \(\theta\) and equals zero at \(1/2\) and \(1\). Now sum over the possible prefixes. Since \(2^{1-2\theta}<1\) and \(V\ge v\),
\[
 \sum_{t_0\ge V}D^{a+1}2^{t_0-V}(4^a3^v4^{-t_0})^\theta
 \le D_\theta^{a+1}(3/4)^{\theta v}.                         \tag{5}
\]
Combining (4) and (5) proves claim 1.

## Exact center hits and transfer to ordinary windows

An on-center word means \(T_b(-1/2)=T_w(-1/2)\) for the competing forward word \(b\). The denominators in lowest terms are \(2^{t+1}\) and \(2^{a+1}\), hence \(t=a\) and \(g_b=g_w\). The physical equality now gives \(2m+1=3^{r-q}(2y+1)\). If \(q\le r\) this cannot reduce rank. If \(q>r\) and \(v>a\), the formula gives a positive section integer \(m\) with rank \(3^{r-q}P(y)\). Its affine endpoint under \(b\) is an integer, which enforces that exact parity word by the dyadic parity bijection. This is the repository's shared-remainder mechanism. Words of equal weight have distinct \(g\)'s: equality would make their affine maps identical and therefore their unique physical parity residue identical. The middle weight alone now gives the stated lower bound on the number of resistant buckets. If a shorter prefix has a better centered competitor, appending the same suffix yields a better competitor at the full length. Thus a resistant word has resistant prefixes.

For a given \(w\) and \(t\le R\), the ideal test is decided by finitely many ternary digits of \(u\). Without conditioning, admissibility plus a required \(d(m)\ge k\) uses at most \(q+k\) digits of the endpoint. Subtract \(V\) fixed digits, and use \(k=\max(0,\lceil v+2p(t-a)+2(r-q)-c_0\rceil)\). The extra precision is at most \(\max(0,q-V,2pt-q+r-2pa)+O(1)\le 2pR+O(1)\). This is a common modulus \(O(4^R)\), uniform in \(w,v,a\). Prescribing the physical source word uses \(u\) modulo \(2^{a+1}\), independently of ternary precision. In a full CRT period the eligible \(u\) split equally over the \(2^a\) words. Union over shorter forward lengths costs at most \(K_1^{a+1}(3/4)^{\theta v}\) for off-center tests by claim 1. For resistant words exact hits cannot help. Thus the full-period failure fraction is at least
\[
 2^{-a}\binom{a}{\lfloor a/2\rfloor}-K_1^{a+1}(3/4)^{\theta v}.
\]
Choose \(\eta>0\) so that the second term is exponentially small in \(v\) when \(a\le\eta v\). A range \(U\) covering at least two full periods retains an absolute constant times the full-period lower fraction; for the \(a=0\) upper success bound, count complete periods plus one. This proves claim 3. For arbitrarily long reverse clocks the Haar event is a countable union, and transferring it to actual integer density requires a separate tail argument.

**Source pin.** PR #90 at `78ac7c8489f1df81230402808b1f4b77b18fae73`, with the resident proofs linked above, supplies the comparison and the native rank. The argument is proposed pending review.
