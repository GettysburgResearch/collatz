# Every signed rational cycle needs a larger denominator at almost every period

Let \(d_{\min}(n)\) be the smallest **full reduced denominator** among all nonzero signed rational shortcut cycles of least physical period \(n\), with infinity allowed if the family is empty. Put
\[
           p=\log_3 2,\qquad h_*=H_2(p)=0.9499555271\ldots .
\]
**Theorem.** For every fixed \(0<\theta<1/(1+h_*)=0.5128322087\ldots\), the periods for which
\[
                             d_{\min}(n)>n^\theta                      \tag{1}
\]
have natural density one. In particular \(20/39=0.5128205128\ldots\) is an admissible explicit exponent. Indeed \(3^{6309}<2^{10000}\) and \(10000^{10000}<2^{9500}6309^{6309}3691^{3691}\) give \(p>6309/10000>1/2\) and \(h_*<H_2(6309/10000)<19/20\). Both comparisons use exact integers. This says that at each retained period **every** primitive nonzero rational cycle word, positive or negative, has common reduced denominator larger than the stated power. There is no weighting by the number of words per slice. No assumption about the convergence of integer trajectories, no computational verification floor, no quantitative Diophantine input and no Subspace Theorem are needed.

More quantitatively, for each fixed \(h_*<h<1\), one may choose some \(\theta_0>1/(1+h_*)\) and a constant \(C_h\) such that
\[
 \#\{C:N\le n_C\le2N,\ d_C\le D,\ g_C\ge b\}
                \le C_h D^{1+h}(1+b^{-1})
       \quad (D\le N^{\theta_0},\ b>0)                                 \tag{2}
\]
for all sufficiently large \(N\). This *does* count cycles with multiplicity at the same period vector. The separate small-gap part of the proof of (1) counts distinct physical periods only. Here \(g_C=|n_C\log2-u_C\log3|\) and \(u_C\) is the odd count. The signed dynamics and exact gap formula are as in [DENOMINATOR_CENSUS.md](DENOMINATOR_CENSUS.md).

### Charging cycles with large real minimum

Write \(y_i>0\) for the magnitudes around one least cycle and \(r_i=1/y_i\). At an even input let \(g_i=0\); at an odd input use \(g_i=\log(1+1/(3y_i))\) for positive cycles and \(g_i=-\log(1-1/(3y_i))\) for negative cycles. These local gaps sum to \(g_C>0\). Choose two large fixed positive numbers \(M,B\), with \(M\ge2\), and first assume all \(y_i\ge M\). Then \(0\le g_i\le b_i:=\mathbf1_{i\,\mathrm{odd\ input}}r_i/2\) for both signs. Use the rational majorant to define
\[
 Q_i=b_i+B(r_i-r_{i+1}),\qquad S_{i+1}-S_i=Q_i,\qquad
 D_i=\min_{j\ge i+1}S_j-\min_{j\ge i}S_j .
\]
Indices are extended along the infinite repeated cycle when defining the minima. They exist since \(S_{i+n_C}=S_i+\sum b_j\), with the sum over one lap positive. The charges are nonnegative and periodic, and their sum in one lap is \(\sum b_j\ge g_C\). When \(B\) is a positive integer this construction uses only rational arithmetic. Whenever \(D_i>0\), \(S_i=\min_{j\ge i}S_j\). Thus \(D_i\le Q_i\le(B+1/2)r_i\) there, and **all** forward partial sums of \(Q\) from that index are nonnegative. The use of future minima to turn cyclic telescoping charges into nonnegative masses is prior in Paper 217. Our coefficient \(B\) is a tunable constant, and the next step exploits all partial sums to count charged rational phases uniformly over denominators. [Paper 217, “Residue weights and the reciprocal sum”](https://rstation.ai/problems/collatz/papers/217)

For such a charged index and every \(j\ge1\), nonnegativity and the bound on local gaps yield
\[
 r_{i+j}\le r_i+B^{-1}\sum_{s=0}^{j-1}b_{i+s}
      \le r_i+(2B)^{-1}\sum_{s=0}^{j-1}r_{i+s}
      \le r_i(1+1/(2B))^j .
\]
The last estimate is the elementary geometric-sum induction. If \(q\) of these \(j\) steps have odd inputs, the true ratios at floor \(M\) give
\[
 (1+1/(2B))^{-j}\le y_{i+j}/y_i
            \le (3+1/M)^q/2^j .
\]
It follows that a charged phase has at least \(p_{M,B}j\) odd bits in **every** prefix, where
\[
              p_{M,B}=\frac{\log(2/(1+1/(2B)))}{\log(3+1/M)} .
\]
As \(M,B\to\infty\) this tends to \(p\). Take fixed \(M,B\) so large that \(1/2<p_{M,B}<p\) and \(H_2(p_{M,B})<h\). We may also arrange
\[
                p_M=\log_{3+1/M}2>1/(1+h_*).
\]
The latter is possible since \(p>0.63>1/(1+h_*)\).

For fixed denominator \(d\ge1\) and sign, count distinct charged phases \(y=a/d\le X\), \(X\ge1\), by the first \(t=\lfloor\log_2(dX)\rfloor\) parity bits. Each word allows at most two such positive numerators: it selects one residue modulo \(2^t\) because \(d\) is odd, and \(dX<2^{t+1}\). The binomial upper tail at \(p_{M,B}t\) supplies \(O_h(2^{ht})\) admissible words, the polynomial factor absorbed by strict entropy slack. Thus there are \(O_h((dX)^h)\) charged phases through \(X\). At fixed sign and reduced denominator, distinct cycles have disjoint numerator states, so the same bound holds for the entire collection. Finally sum the bound \((B+1/2)/y\) dyadically on \(y\ge M\). Since \(h<1\), this proves
\[
             \sum_{C:d_C=d,\ \min_i |x_i|\ge M}g_C\ll_h d^h.          \tag{3}
\]
Both signs can be included at the cost of a factor of two. There is no restriction on the individual gaps, periods or maximum heights in (3). The finite rational cyclic charge, positive-prefix implication, telescoping lap and discrete Gronwall consumer are checked by [RationalCycleCharges.lean](RationalCycleCharges.lean).

### A bounded-height witness on every other long cycle

Take \(n_C\in[N,2N]\) and \(d_C=d\le N^{\theta_0}\), with a fixed \(1/(1+h_*)<\theta_0<p_M\). The \(n_C\) different phase magnitudes are different positive integer numerators divided by \(d\), hence their largest magnitude is at least \(N/d\). For all large \(N\) this exceeds \(2M\) uniformly. If the cycle has minimum below \(M\), follow it to a largest phase and take the **last** crossing from below \(M\) to at least \(M\) before that phase, traversing at most one lap. Its new state \(z\) satisfies \(M\le z\le c_M M\le2M\), where \(c_M=(3+1/M)/2\). All magnitudes from \(z\) through the selected maximum remain at least \(M\), and each step increases magnitude by at most factor \(c_M\). Thus the segment from \(z\) to the maximum has length at least
\[
                   \log_{c_M}\!\left(\frac{N}{2Md}\right).
\]
This is at least \(\lfloor\log_2 d\rfloor\) for all sufficiently large \(N\), uniformly in the displayed range. Indeed \(d^{1+\log_2 c_M}\le N^{\theta_0/p_M}=o(N)\). No frequency assumption on the word or lower bound on the minimum was used.

Take \(t=\lfloor\log_2 d\rfloor\) from this crossing phase. The endpoint is at least \(M\) and \(z\le2M\), so the upper step-ratio bound gives \(1/2\le(3+1/M)^q2^{-t}\); hence \(q\ge p_M(t-1)\). Since \(p_M>p_{M,B}>1/2\), the number of such words is \(O_h(2^{ht})\). Each one allows \(O_M(1)\) numerator representatives in the fixed real interval \([M,2M]\), because its numerator interval has width \(dM\) and \(2^t>d/2\). Choosing one witness per actual cycle is injective into phases at this fixed denominator and sign: two distinct cycles cannot share a phase. Consequently
\[
    \#\{C:N\le n_C\le2N,\ d_C=d,\ \min_i|x_i|<M\}\ll_h d^h.         \tag{4}
\]
Unlike (3), (4) already counts every such cycle, including arbitrarily small gaps. Low \(d\) and \(t=0\) are harmless with the same enlarged constant.

### From the gap split to density one

For large-minimum cycles with \(g_C\ge b\), divide (3) by \(b\). Add (4) and sum \(d\le D\) to obtain (2). Now fix \(\theta<1/(1+h_*)\); by decreasing the amount of slack in \(h>h_*\), arrange \(\theta(1+h)<1\). At physical periods in \([N,2N]\) a counterexample to (1) has \(d_C\le (2N)^\theta\), which lies within the allowed cutoff for large \(N\). Set \(b=N^{-\sigma}\) with fixed \(0<\sigma<1-\theta(1+h)\). Bound (2) counts \(o(N)\) such cycles with gap at least \(b\). Every smaller gap forces \(\|np\|<b/\log3\), since \(u\) is integral. Irrationality of \(p\) and ordinary equidistribution of its multiples give \(o(N)\) possible period values in the dyadic interval: compare first against a fixed arc around 0 and then shrink its length. Summing dyadic intervals or using their upper densities proves (1). A fixed irrationality-measure input can give an explicit power for that last exceptional count, but is unnecessary here.

Each denominator statement concerns a full common reduced denominator and true least-period orbits, across all word shapes. The known Bernoulli-type exact-slice law concerns the probability of cancellations when choosing a word at one fixed length and weight. Bounds for mechanical, sparse-feature or two-interval schedules can give much stronger pointwise denominator exponents on those families. Positive rational cycles of every length \(n\ge2\) exist, e.g. the primitive word with one odd departure and \(n-1\) evens, so (1) has content without any integer-cycle existence assumption. [Halbeisen–Hungerbühler](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf), [Paper 216, two-interval schedules](https://rstation.ai/problems/collatz/papers/216), [fixed-type law](../phase4/DENOMINATOR_LAW.md)
