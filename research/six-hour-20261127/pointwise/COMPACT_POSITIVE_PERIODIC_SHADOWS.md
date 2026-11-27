# Compact positive rational cycles shadowing critical prefixes

Let $b_0,b_1,\ldots$ be shortcut parity bits, $q_i=\sum_{j<i}b_j$, $C_i=3^{q_i}/2^i$, and $S_i=\sum_{j<i:b_j=1}1/(3C_j)$. Assume $C_i>1$ for all $i>0$ and $S_\infty<\infty$. On every prescribed prefix the real affine terminal from $x$ is $C_i(x+S_i)$.

**Closure.** For every sufficiently large $n$, append $k=1+\lceil\log_2 C_n\rceil$ zeros to the first $n$ bits and repeat the resulting word with period $N=n+k$. This gives a genuine positive rational shortcut cycle of primitive period exactly $N$. Its starting phase $z_n$ lies in $(1/9,S_\infty]$. Every phase has the same full reduced denominator $d_n$, prime to six, and

$$
z_n=\frac{rS_n}{1-r},\qquad r=C_n/2^k\in(1/4,1/2],\qquad
d_n\mid (2^{n+k}-3^{q_n}).
$$

Indeed the positive affine fixed point is the displayed $z_n$. The first bit is one by strict supercriticality, so $S_n\ge1/3$. If $A_n$ is the integer intercept in $2^n y=3^{q_n}x+A_n$, then $z_n=A_n/(2^N-3^{q_n})$. The denominator before reduction is positive, odd and coprime to three. The congruence $3^{q_n}z_n+A_n\equiv0\pmod{2^N}$ in the ring of rationals with odd denominators gives precisely the required length-$N$ parity cylinder by the finite coding bijection. Thus actual rational shortcut iteration realizes the whole cyclic word. Every step preserves the full denominator: both two and three are units modulo $d_n$, and adding $d_n$ to an odd numerator times three leaves it coprime to $d_n$. The affine offset of any nonempty positive periodic lap is positive, so its gain must be strictly below one. A proper period of the orbit divides $N$ and is at most $N/2\le n$ eventually, since $k\le1+\lceil n\log_2(3/2)\rceil$. This contradicts the strict prefix condition. For $i\le n$ the actual rational state $C_i(z_n+S_i)$ is bounded above and below by fixed positive multiples of $C_i$ independently of $n$.

**Complete cyclic controls.** Apply the construction to the maximal-dimension critical trace family with $C_i=i^{B+o(1)}$, $B>1$. Now $k=O(\log n)$ and the maximum actual real height on the entire primitive rational cycle is $n^{B+o(1)}$. All fixed-order moving parity tests remain asymptotically Bernoulli-$p$, $p=\log_3 2$, even on the full cycle, for every sequence of consecutive cyclic start calendars of length $\ell\le N$ with $\ell/\log n\to\infty$ and every tuple of distinct offsets modulo $N$. Use the sharp linear-calendar version of the countermodel. Cut the start calendar at its own wrap, at each translated wrap, and where a translated position enters or leaves the appended interval. At most $rk$ starts use an appended bit for a test of order $r$. The other starts form $O_r(1)$ intervals with fixed translates into $[0,n)$. Their offsets are still distinct, after reordering and common translation if necessary. Discard the intervals of length below $\sqrt{\ell\log n}$ at an additional cost $o_r(\ell)$. The remaining lengths divided by $\log n$ tend to infinity, so the linear-calendar test applies uniformly. This proves the claimed cyclic control.

For a full-measure subset of the countermodel law, still of dimension $H_2(p)$, every fixed compact interval of positive real sources obeys the following denominator floor. Any odd-denominator rational in that interval matching the first $n$ bits has denominator at least $2^{(H_2(p)/2-o(1))n}$. In a fixed interval $[0,M]$ there are $O_M(D^2)$ reduced rationals of denominator at most $D$. Each length-$n$ parity word has probability at most $2^{-nH_2(p)+o(n)}$ uniformly, by the unedited complete block bound. For $D=2^{(H_2(p)/2-\epsilon)n}$ the exceptional probabilities are summable. Take countably many positive rational $\epsilon$ and positive integer $M$. In particular our full common denominator on these periodic shadows lies between $2^{(H_2(p)/2-o(1))n}$ and $2^{n+o(n)}$.

**The ordinary denominator obstruction.** Suppose the original infinite word comes instead from one fixed positive integer $x$ whose orbit escapes, with all its prefixes strictly supercritical. Such a representative exists in every escaping component, by the corrected-height minimum. The reciprocal packing estimate gives $S_\infty<\infty$. For *any* positive periodic rational shadow $a/d$ of the first $n$ bits in a fixed compact interval, $2^n\mid a-dx$ and $a-dx\ne0$. Hence $d\ge 2^n/(M+x)$ when $a/d\le M$. Our closures at subexponential $C_n$ therefore satisfy $d_n=2^{n+o(n)}$. A proof that every such hypothetical path has compact periodic shadows with $d=o(2^n)$ along an unbounded subsequence would exclude all escaping paths. No such saving is established here.

For the displayed closure the exact gcd condition at a genuine integer seed is

$$
d_n=\frac{D_n}{\gcd(D_n,x_n-2^k x)},\qquad D_n=2^{n+k}-3^{q_n},\qquad x_n=T^n x.
$$

In fact $A_n-xD_n=2^n(x_n-2^k x)$ and $D_n$ is odd. This shows where a needed full-denominator saving would enter the specific construction. An upper bound for the unreduced denominator, agreement of the real orbit through $n$ steps, or realizability in both local rings alone supplies no saving.

**Precedents.** Rational periodic parity formulas, global affine offset normalizations and exact denominator reductions already appear in the earlier cycle and moving-shadow packets. The additional controls here are bounded real starting phases, a logarithmic closing calendar for the critical countermodels, full cyclic versions of their moving statistics, and the comparison with the denominator threshold for a fixed ordinary source.

- [Toric cycle windows and exact denominators](https://github.com/GettysburgResearch/collatz/blob/df2f17a117bea06bb34040a5a97e7dc9711d9871/research/six-hour-20261127/cycles/TORIC_CYCLE_WINDOWS.md)
- [Moving rational shadows](https://github.com/GettysburgResearch/collatz/blob/df2f17a117bea06bb34040a5a97e7dc9711d9871/research/six-hour-20261127/pointwise/MOVING_RATIONAL_SHADOWS.md)
- [Weaver, corrected heights and escaping representatives](https://rstation.ai/problems/collatz/papers/207/v1)
- Prerequisite trace manuscripts are frozen at SHA-256 960aa9089c4c23c63f76cd6e1182528753642994093c63e084876e5280f1078f, 85cdf780817e0a9c0aa3882e6f092b068a27b4cd0f560c017eb12bfa8839abae, and c2d4e7cc8b1ad5501ab4264ec287581f7eeda1b07fcce8ba3ea7c303e390cab8.
