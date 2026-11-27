# The critical denominator exponent with a logarithmic gain

Put $p=\log_3 2$, $h_*=H_2(p)$, and let $d_{\min}(n)$ be the minimum full reduced denominator over all nonzero signed rational shortcut cycles of least physical period $n$, with value infinity for an empty family. Write $L(x)=1+\log x$ for $x\ge1$, using natural logarithms. Set

$$
 \theta_*=\frac{1}{1+h_*},\qquad
 \beta=\frac32-h_*,\qquad
 \lambda_*=\frac{\beta}{1+h_*}=\frac52\theta_*-1=0.2820805\ldots .
$$

**Theorem.** For each fixed $\lambda<\lambda_*$, the periods satisfying

$$
                 d_{\min}(n)>n^{\theta_*}L(n)^\lambda                 \tag{1}
$$

have natural density one. In particular one can take $\lambda=7/25$. This includes every word shape and both signs. Individual exceptional periods remain possible.

The proof refines the positive-prefix charge and last-crossing arguments in [ASCENT_CENSUS.md](ASCENT_CENSUS.md). The classical $t^{-3/2}$ ballot factor for a tilted walk at the critical slope already enters Weaver's all-clock first-meeting estimate, which credits Paper 28/v3, Proposition 4. We give an elementary proof uniform in the nearby slopes and bounded intercepts needed here. The new application varies the real floor and charge coefficient with the full denominator and uses every prefix of the low-minimum witness. All estimates below are written mathematics. [Weaver 178/v1, §2](https://rstation.ai/problems/collatz/papers/178/v1)

## Uniform count for all prefixes

For $\alpha\in[3/5,2/3]$, $0\le a\le1$, let $W_t(\alpha,a)$ be the binary words of length $t$ whose every prefix of length $j$ has odd count at least $\alpha j-a$. There is an absolute bound

$$
          |W_t(\alpha,a)|\ll \frac{2^{H_2(\alpha)t}}{(1+t)^{3/2}}.   \tag{2}
$$

Give each bit independent Bernoulli law with odd probability $\alpha$, and write $S_j$ for its count minus $\alpha j$. We first record the one-sided survival estimate for this centered walk or its negative. For every $A\ge0$ and $s\ge1$,

$$
       \Pr(S_j\ge-A\text{ for all }1\le j\le s)
                       \ll\frac{A+1}{\sqrt{s}}.                      \tag{3}
$$

The step has absolute value at most one and variance $v=\alpha(1-\alpha)$ bounded below. If $A>\sqrt s$, (3) is immediate. Otherwise set $K=\sqrt s$ and stop at the first value below $-A$ or at least $K$, with stopping time $\sigma$. For any finite cutoff $m$, $Z=S_{\min(\sigma,m)}$ lies in $[-A-1,K+1]$ and has mean zero. Since $(Z+A+1)(K+1-Z)\ge0$, the stopped second-moment identity gives
$$
          v\,\mathbb E\min(\sigma,m)=\mathbb E Z^2\le(A+1)(K+1).
$$
Consequently $\sigma$ is finite almost surely, with the same expected-time bound divided by $v$. Bounded convergence gives $\mathbb E S_\sigma=0$. The probability of exiting at the top is at most $(A+1)/(K+A+1)$, by comparing the top value to $K$ and the bottom value to $-A-1$. Survival to $s$ requires a top exit or $\sigma>s$. Markov's inequality proves (3). The two stopped identities here also follow by summing the mean and variance increments multiplied by the indicator that stopping has not yet occurred.

For $t\ge6$, partition the steps into three consecutive groups whose lengths differ by at most one. Fix the total centered endpoint $x=k-\alpha t\ge-a$. On a surviving word the first group stays above $-a$. The centered reverse partial sums of the last group stay below $x+a$, because the complementary forward prefixes stay above $-a$. These events depend on independent groups and cost at most $C(a+1)/\sqrt t$ and $C(x+a+1)/\sqrt t$ by (3). Conditional on the two outer groups the middle group must have a prescribed count. Its maximal binomial mass is $O(t^{-1/2})$ uniformly on the compact slope interval, by the binomial mode and Stirling's bounds. Thus the tilted probability of survival and this endpoint is at most $C(a+1)(x+a+1)t^{-3/2}$.

A word with this endpoint has tilted mass $2^{-H_2(\alpha)t}(\alpha/(1-\alpha))^x$. Upon converting to counts, the factor $((1-\alpha)/\alpha)^x$ makes the sum over $x\ge-a$ on its shifted unit lattice bounded uniformly, including the factor $x+a+1$. This proves (2), enlarging the constant for short lengths.

## Denominator-dependent charges

Fix one reduced denominator $d\ge1$, and use

$$
              M=B=\lceil100L(d)\rceil,\qquad
 \alpha=\frac{\log(2/(1+1/(2B)))}{\log(3+1/M)},\qquad
 \alpha_0=\frac{\log2}{\log(3+1/M)} .
$$

Both slopes lie in $[3/5,p]$. For the lower end, $(400/201)^5>(301/100)^3$ and $B,M\ge100$. Also $p<2/3$. Uniformly in $d$ the two slopes differ from $p$ by $O(1/L(d))$. Hence either entropy $h=H_2(\alpha)$ or $H_2(\alpha_0)$ satisfies
$$
 h_*\le h\le H_2(3/5)<1,\qquad h-h_*=O(1/L(d)),\qquad
 d^{h-h_*}+M^{h-h_*}\ll1 .                                         \tag{4}
$$

First take all true cycles with this denominator whose magnitudes $y_i$ stay at least $M$. For each sign put $r_i=1/y_i$, $b_i=\mathbf1_{\mathrm{odd}}r_i/2$ and $Q_i=b_i+B(r_i-r_{i+1})$. The future-minimum charges in the earlier proof sum to $\sum b_i\ge g_C$, where $g_C=|n_C\log2-u_C\log3|$. Every positive charge is at most $(B+1/2)/y_i$, and all forward partial sums of $Q$ from that cut are nonnegative. For completeness this implies $r_{i+j}\le r_i+(2B)^{-1}\sum_{s<j}r_{i+s}\le r_i(1+1/(2B))^j$. At floor $M$, either signed branch has $y_{i+j}/y_i\le(3+1/M)^q2^{-j}$ for $q$ odd inputs in that prefix. Therefore every such prefix has $q\ge\alpha j$. Both positive and negative gaps are covered by $b_i$ as in the earlier proof.

For $X\ge M$ let $t=\lfloor\log_2(dX)\rfloor$. At a fixed sign each native $t$-bit word selects one numerator class modulo $2^t$. Indeed the positive magnitude numerator follows $a\mapsto a/2$ on even inputs and $a\mapsto(3a\pm d)/2$ on odd inputs. A prescribed history chooses a unique successive dyadic lift because the slope numerator is odd. The interval of positive numerators up to $dX<2^{t+1}$ contains at most two representatives per word. Distinct primitive orbits at fixed denominator and sign have disjoint states. It follows from (2) that the number of distinct charged phases through $X$ is at most

$$
                  C\,\frac{(dX)^h}{L(dX)^{3/2}},
                 \qquad h=H_2(\alpha).
$$

Now sum their charge bound on the shells $[2^jM,2^{j+1}M)$ for $j\ge0$. The resulting geometric series has ratio $2^{h-1}$ bounded away from one by (4). This gives the quantitative improvement

$$
 \sum_{\substack{C:d_C=d\\\min_i y_i\ge M}}g_C
 \ll \frac{B\,d^hM^{h-1}}{L(dM)^{3/2}}
 \ll \frac{d^{h_*}}{L(d)^\beta}.                                     \tag{5}
$$

The constants are absolute and both signs are now included. The use of a different floor for each denominator occurs before summing over denominators.

## All prefixes of the last ascent

Let $N\le n_C\le2N$, $d_C=d\le N^{11/20}$, and suppose the minimum is below $M=M(d)$. The largest magnitude is at least $N/d$, because the $n_C$ positive numerators are all distinct. Take the last upward crossing from below $M$ before reaching such a maximum within one lap. The new value $z$ belongs to $[M,2M]$ and subsequent magnitudes through the maximum stay at least $M$. On this section each single-step increase has factor at most $c_M=(3+1/M)/2$ for either sign.

Set $t=\lfloor\log_2(dM)\rfloor$. Uniformly for the stated $d$, the section from $z$ to the maximum has at least $t$ steps for all sufficiently large $N$. Indeed
$$
 2dM c_M^t \le 2(dM)^{1+\log_2 c_M}=2(dM)^{1/\alpha_0}
       \ll N^{11/12}L(N)^{5/3}=o(N),                                \tag{6}
$$
using $\alpha_0\ge3/5$ and $dM\ll N^{11/20}L(N)$. In particular the maximum exceeds $2M$, so the crossing exists, and its growth to $N/d$ takes longer than $t$.

For **every** $1\le j\le t$, the endpoint-to-source ratio from $z$ is at least $1/2$ and at most $(3+1/M)^q2^{-j}$. This implies $q\ge\alpha_0(j-1)\ge \alpha_0 j-1$. The numerator interval $[dM,2dM]$ has length $dM<2^{t+1}$, so it has $O(1)$ representatives for each native word, uniformly in the varying $M$. Choose one crossing per cycle: a witness phase at this fixed sign and reduced denominator lies on at most one true cycle. The ballot estimate (2), now at intercept one, gives

$$
 \#\{C:N\le n_C\le2N,\ d_C=d,\ \min_i y_i<M(d)\}
    \ll \frac{(dM)^{H_2(\alpha_0)}}{L(dM)^{3/2}}
    \ll \frac{d^{h_*}}{L(d)^\beta}.                                 \tag{7}
$$

This estimate counts true cycles regardless of their gaps.

## From cycles to period values

By (5), the number of high-minimum cycles with $g_C\ge b>0$ is at most the gap sum divided by $b$. Add (7) and sum $d\le D$, where $1\le D\le N^{11/20}$. For all sufficiently large $N$ this gives the multiplicity-counting bound
$$
 \#\{C:N\le n_C\le2N,\ d_C\le D,\ g_C\ge b\}
       \ll (1+b^{-1})\,\frac{D^{1+h_*}}{L(D)^\beta}.                 \tag{8}
$$
The sum over $d$ follows by splitting at $\sqrt D$ and using $L(d)\gg L(D)$ above that point.

For fixed $\lambda<\lambda_*$ put $D=C_\lambda N^{\theta_*}L(N)^\lambda$, large enough to cover all counterexamples to (1) in $[N,2N]$. It satisfies the cutoff for large $N$, since $p<2/3$ and $H_2(2/3)=\log_2 3-2/3>5/6$, giving $\theta_*<6/11<11/20$. Set $b=L(N)^{-\eta}$ with $0<\eta<\beta-\lambda(1+h_*)$. Since $L(D)\asymp L(N)$, (8) then gives $o(N)$ large-gap cycles. Each smaller gap forces the **period value** $n$ to satisfy $\|np\|<b/\log3$. For every fixed neighborhood of zero in the unit circle, irrational equidistribution bounds its limiting dyadic proportion by its length. Taking successively smaller fixed neighborhoods gives $o(N)$ possible periods for the shrinking threshold. Thus the total number of exceptional period values in $[N,2N]$ is $o(N)$, which yields natural density zero on summing dyadic intervals.

Finally $h_*<19/20$ by the exact entropy comparison in the earlier proof. Therefore $\lambda_*=\tfrac52\theta_*-1>11/39>7/25$. This proves the stated explicit logarithmic gain without a quantitative irrationality measure, a finite verification floor or a conjectural cycle assumption. [Exact entropy comparison](ASCENT_CENSUS.md)
