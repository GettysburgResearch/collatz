# Full exponential denominator for every short periodic closure

Use the maximal-dimension law of critical traces in MOVING_LAG_CRITICAL_COUNTERMODELS.md (SHA-256 85cdf780817e0a9c0aa3882e6f092b068a27b4cd0f560c017eb12bfa8839abae), with the one-transposition square edit of SHARP_MOVING_CORRELATION_SCALE.md (c2d4e7cc8b1ad5501ab4264ec287581f7eeda1b07fcce8ba3ea7c303e390cab8). Fix $B>1$ and put $p=\log_3 2$. For almost every trace, every family of periodic closures obtained by appending $o(n)$ arbitrary bits to its first $n$ bits has the following property. On every subsequence where the resulting rational starting phases stay in a fixed bounded real interval, their *full reduced* denominators satisfy

$$
                         d_n=2^{n+o(n)}.
$$

The statement is simultaneous over all choices of suffixes, including adaptive ones. It applies to signed phases as well as positive ones. The full-measure family can be chosen transcendental of dimension $H_2(p)$. In particular the true positive, compact, primitive cycles in COMPACT_POSITIVE_PERIODIC_SHADOWS.md (b33f4e6ab8b433121c62662a44e0bf3f61e82c6fd6fdc386ad6569964a0f6f5e) attain this exponent. Their cyclic correlation tests still hold.

**Proof.** For a word $v$ of length $N$ and weight $Q$, let $A(v)$ be its affine integer intercept in $2^N y=3^Q x+A(v)$. The periodic value is $A(v)/D$ with $D=2^N-3^Q\ne0$. Here $Q>0$, so $D$ is coprime to six. Fix $0<\epsilon<1$. We show that almost surely, from some $n$ on, all suffixes of length at most $\gamma n$ have $\gcd(A(v),D)<2^{\epsilon n}$, for a sufficiently small constant $\gamma=\gamma(\epsilon)>0$.

Use as an initial chunk the longest sequence of complete trace blocks of total length $L\le\epsilon n/(2\log_2 3)$. The maximal block length is $O(\sqrt{\ln n})$, so $L=\epsilon n/(2\log_2 3)+o(n)$. This chunk has fixed total weight. Condition on the independent reference blocks outside the chunk through the final block intersecting the prefix. Enumerate assignments to *all* edited square-block letters through that block, including initial deterministic choices if necessary, at cost $2^{o(n)}$. This enumeration permits even impossible assignments and absorbs every dependence of later edited blocks on earlier reference choices. The final outside partial block causes no additional dependence. Fix one appended suffix as well. Outside the chunk the resulting word is fixed; call its affine intercept $A_2$ and its weight $Q_2$. The chunk intercept $A_1$ enters through

$$
                       A(v)=3^{Q_2}A_1+2^L A_2 .
$$

For any divisor $g\mid D$ with $g\ge2^{\epsilon n}$, the condition $g\mid A(v)$ fixes $A_1$ modulo $g$. Since $0\le A_1\le3^L-2^L<g$, it fixes $A_1$ integrally. For its fixed weight $Q_1$, this specifies at most one chunk word: its length-$L$ parity residue is $-A_1 3^{-Q_1}\bmod 2^L$, and the coding is bijective. All complete unedited reference blocks inside the chunk are independent and uniform on their fixed-weight lists. The probability of any one specified collection of their words is at most $2^{-H_2(p)L+o(n)}$, by the binomial bound and the $o(n)$ total length of edited blocks. This bound is uniform in all outside assignments.

For $N\le(1+\gamma)n$ and $Q\le N$ there are $O(n^2)$ possible $D$, each of magnitude $2^{O(n)}$ for $\gamma<1$. Their divisor counts are uniformly $2^{o(n)}$: for any $\eta>0$ the large prime factors contribute at most $|D|^\eta$ using $a+1\le2^a\le p_0^{\eta a}$ for large primes $p_0$, while finitely many small primes contribute only a power of $n$. There are at most $2^{\gamma n+1}$ suffixes. Summing all bounds, including the enumerated edits, gives an exponentially small probability on choosing $\gamma<H_2(p)\epsilon/(4\log_2 3)$. Borel–Cantelli, then countably many decreasing $\epsilon$, gives $\gcd(A(v),D)=2^{o(n)}$ simultaneously for every sublinear suffix schedule.

For such a schedule, $N=n+o(n)$ and $Q=pn+o(n)$, hence $|D|\le2^{n+o(n)}$. The first bit is one, which contributes $3^{Q-1}$ to $A(v)$. If the starting phase has absolute value at most a fixed $M$, then $|D|\ge A(v)/M\ge3^{Q-1}/M=2^{n+o(n)}$. Reduction by the full gcd proves the assertion. No real logarithmic-forms estimate is used.

An actual fixed positive escaping source also forces $d_n\gg 2^n$ for distinct compact periodic shadows by the integer congruence in the companion closure paper. The theorem attains exactly its leading exponential rate on nonordinary critical models, independently of the chosen sublinear closing word. A subexponential factor in $d_n/2^n$ can still distinguish the situations. Neither a saving at that finer scale on all escaping paths nor a denominator bound for unrestricted closing lengths has been proved.
