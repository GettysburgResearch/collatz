# A sharp bound for a divisor retained across successive ordinary resets

**Status.** Proposed ordinary-integer theorem, extending the companion single-reset result. The classical inequality on sums of integers used in the upper bound has a possibly ineffective constant. The matching construction uses ordinary parity cylinders and the Chinese remainder theorem. The upper bound applies to a single supplied trajectory. The lower construction varies its positive starting integer.

Let \(r\ge1\) be fixed. Follow \(r\) complete Syracuse ascent-and-reset blocks from an arbitrary positive odd ordinary integer \(x_0\) to successive odd landings \(x_1,\dots,x_r\). Write
\[
 Y_j=x_j+1=2^{t_j}w_j\quad (w_j\text{ odd}),\qquad
 2^{b_j}x_{j+1}=3^{t_j}w_j-1\qquad(0\le j<r).
\]
Here \(t_j\ge1\) counts the odd steps in block \(j\), and \(b_j\ge1\) is one less than its final odd division exponent. The terminal \(t_r=v_2(Y_r)\) uses just the terminal value, with no further block required. Put
\[
 Y=Y_0,\qquad T=\sum_{j<r}t_j,\qquad B=\sum_{j<r}b_j,\qquad
 g=\gcd(w_0,\ldots,w_r),\qquad \alpha=\log_2 3,\quad\beta=\alpha-1 .
\]

**Theorem D.** For every \(\epsilon>0\) there is a constant \(C_{r,\epsilon}\) such that on every such path
\[
                g^{r+1}2^{T+t_r}\le C_{r,\epsilon}Y^{1+\epsilon}.          \tag{1}
\]
In particular the *full integer* gcd \(G=\gcd(Y_0,\ldots,Y_r)\) satisfies \(G^{r+1}\le C_{r,\epsilon}Y^{1+\epsilon}\). If the number of complete blocks tends to infinity as \(Y\to\infty\), at any rate, this full persistent gcd is \(Y^{o(1)}\). These conclusions impose no lower floor on intermediate values and no restriction on later fates or repeated states.

If \(\lambda>0\) and \(0\le\sigma<\alpha\) are fixed, the sharp exponent for the **odd** persistent divisor under a terminal floor is
\[
 \limsup_{\substack{Y\to\infty\\ x_r\ge\lambda Y^\sigma}}
 \frac{\log g}{\log Y}
  =\min\left\{\frac1{r+1},
       \frac{\alpha-\sigma}{r+(r+1)\beta}\right\}.                        \tag{2}
\]
The exponent is the same on restricting to positive odd multiples of three as initial sources. At \(\sigma=1\) the lower examples can keep all intermediate odd and shortcut states above the starting value after its first departure, through all \(r\) blocks. This gives the precise size of a single unknown common factor sustainable by any fixed number of complete resets that stay at this scale. No arithmetic support for that factor is specified.

### Positive sums after one common integer division

The block equations give
\[
 2^{t_j+b_j}Y_{j+1}=3^{t_j}Y_j+2^{t_j}(2^{b_j}-1).
\]
The odd \(g\) divides both \(Y_j,Y_{j+1}\), hence divides \(2^{b_j}-1\) for every \(j\). Put \(T_j=\sum_{i<j}t_i\), \(D_j=\sum_{i<j}(t_i+b_i)\) and \(D=T+B\). Unroll the preceding identity, divide by \(2^{t_0}g\), and obtain the following sum of \(r+1\) **positive ordinary integers**:
\[
 \frac{2^{D-t_0}Y_r}{g}=Z_*+\sum_{j=0}^{r-1}Z_j,\quad
 Z_* = 3^T\frac{w_0}{g},\quad
 Z_j=3^{T-T_{j+1}}2^{D_j+t_j-t_0}\frac{2^{b_j}-1}{g}.                   \tag{3}
\]
The exponent of 2 at \(j=0\) is zero. At \(j>0\), \(D_j\ge t_0\). Thus all displayed coefficients are integers. The initial coordinate \(Z_*\) is odd. The positivity of every coordinate excludes every nonempty vanishing subsum without deleting any term.

Use Evertse's Theorem 2, equation (14), over \(\mathbb Q\), at \(S=\{\infty,2,3\}\) and with the subset consisting only of the place 2. In the ordinary-integer notation and the archimedean maximum norm of that theorem, for these \(r+1\) coordinates and each \(\delta>0\) the inequality reads
\[
   \left(\prod_i\prod_{v\in S}|Z_i|_v\right)
   \left|\sum_i Z_i\right|_2
     \ge c_{r,\delta}\max_i|Z_i|_2\,(\max_i Z_i)^{-\delta}.                \tag{4}
\]
Here and below the index \(i\) includes the initial coordinate \(*\). The integer-vector Theorem 2 does not require coprime coordinates. Its condition (13) excludes every vanishing subsum, already checked by positivity. In particular this is distinct from applying a primitive-vector Subspace Theorem directly. [Evertse, *On sums of S-units and linear recurrences*, printed pp. 226, 228, Theorem 2 (13)–(14)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf) · [The same dyadic specialization in Paper 147, Appendix A (31)](https://rstation.ai/problems/collatz/papers/147)

The dyadic maximum is 1. The dyadic norm of the sum is exactly \(2^{-(D-t_0+t_r)}\). The product over the three places of each positive integer is its positive part prime to six. Removing the powers of 2 and 3 from (3) therefore gives
\[
       \prod_i\prod_{v\in S}|Z_i|_v
        \le\frac{w_0\prod_{j<r}(2^{b_j}-1)}{g^{r+1}}
        <\frac{w_0 2^B}{g^{r+1}}.                                        \tag{5}
\]
Substitution into (4) gives \(g^{r+1}2^{T+t_r}\le c_{r,\delta}^{-1}Y(\max_i Z_i)^\delta\).

For completeness, \(\max_i Z_i\le Y^{K_r}\) for a constant depending only on \(r\). Every coordinate is no larger than their positive sum (3). Each complete block satisfies \(Y_{j+1}\le3^{t_j}w_j\le Y_j^\alpha\), and \(2^{b_j}\le3^{t_j}w_j\le Y_j^\alpha\), while \(2^{t_j}\le Y_j\). Consequently \(Y_j\le Y^{\alpha^j}\) and
\[
 \log_2(2^D Y_r)\le
 \left[(1+\alpha)\sum_{j<r}\alpha^j+\alpha^r\right]\log_2 Y.
\]
Choose \(\delta=\epsilon/K_r\) to prove (1). The full gcd equals \(g2^{\min_{0\le j\le r}t_j}\), and \((r+1)\min_jt_j\le T+t_r\). This proves its bound. For a growing number of complete blocks, the full gcd divides the gcd of every fixed initial \(r+1\) boundary values. First take a limsup at fixed \(r\) in (1), then let \(r\to\infty\). No uniform estimate on the constants in (4) at growing dimension is used.

### The terminal floor

The one-block affine formula gives
\[
 Y_{j+1}=Y_j(3/2)^{t_j}2^{-b_j}
   \left(1+\frac{2^{b_j}-1}{3^{t_j}w_j}\right).
\]
The factor in parentheses lies strictly between 1 and 2. Therefore
\[
       Y(3/2)^T2^{-B}\le Y_r\le 2^rY(3/2)^T2^{-B}.                     \tag{6}
\]
By \(g\mid 2^{b_j}-1\), one has \(2^B>g^r\). If \(x_r\ge\lambda Y^\sigma\), (6) implies
\[
     r\log g\le(1-\sigma)\log Y+\beta T\log2+O_{r,\lambda}(1).
\]
Equation (1) gives \((r+1)\log g+T\log 2\le(1+o(1))\log Y\). Elimination of \(T\) proves both upper bounds in (2).

### Exact physical-word realization

Let \(b\to\infty\) through odd positive integers, \(H=2^b-1\), and prescribe positive integers \(t_0,\ldots,t_{r-1}\) whose sum is \(T\). For the positive shortcut map prescribe the input parity word
\[
                  O^{t_0}E^b O^{t_1}E^b\cdots O^{t_{r-1}}E^b O .
\]
The last letter verifies that the last even run ends at an odd state. Each prescribed word of length \(D+1=T+rb+1\) selects one binary residue class modulo \(2^{D+1}\). Indeed the two lifts of an entrance class after its first \(d\) bits differ by \(2^d\); their clock-\(d\) states then differ by an odd power of three, forcing opposite next parities. The displayed runs make each complete block physical with exactly the given ascent length and reset excess \(b\).

Use the Chinese remainder theorem to impose \(x_0+1\equiv0\pmod H\) and \(x_0\equiv0\pmod3\) in addition to this binary class. These moduli are pairwise coprime because \(b\) is odd. If \(M=3H2^{D+1}\), take the unique representative \(x_0\in[M,2M)\). Divisibility of \(Y_j\) by \(H\) propagates through the block recurrence because \(2^b-1=H\) and 2 is invertible modulo \(H\). Conversely, every odd common boundary divisor divides \(2^b-1\) already at the first reset. It follows that the actual odd gcd equals \(H\), including all its prime powers. Uniformly in the selected \(t_j\), (6) and the size of the CRT representative give
\[
   \log_2Y=T+(r+1)b+O(1),\qquad
   \log_2 x_r=\alpha T+b+O_r(1),\qquad \log_2g=b+o(1).                  \tag{7}
\]
Here \(Y_r/2\le x_r\le Y_r\) since \(Y_r\ge2\). If \(0\le\sigma<1/(r+1)\), choose all \(t_j=1\). If \(1/(r+1)\le\sigma<\alpha\), choose
\[
  T=\left\lceil\frac{(r+1)\sigma-1}{\alpha-\sigma}\,b\right\rceil+K
\]
with a fixed positive \(K\ge r\), and partition \(T\) into \(r\) positive integers. The bounded errors in (7) show that large enough \(K\) ensures \(x_r\ge\lambda Y^\sigma\) for all sufficiently large \(b\). The resulting ratios in (7) give the two corresponding lower bounds in (2).

At \(\sigma=1\), take every \(t_j=\lceil b/\beta\rceil+K'\) instead. Then each block's homogeneous gain is at least \(2^{\beta K'}>1\). For large \(b\) and sufficiently large fixed \(K'\), every shifted boundary grows by a fixed factor, and its true odd landing strictly exceeds the original input. Intermediate odd states in an ascent increase, and intermediate even states on the subsequent halving run lie above its landing. Balanced choices of these actual first blocks therefore give the same lower exponent even with that stronger all-clock floor.

**Ordinary scope.** The upper bound applies at every set of consecutive boundaries on one ordinary trajectory, with the common divisor selected after every boundary is known. Choosing a fresh unrelated divisor separately at every boundary is a different condition. Small inherited gcds are compatible with growth, and the theorem offers no reason a nonconvergent orbit must repeatedly carry a large common divisor. The source-normalized duration simplex for fixed shortcut templates, including runs of odd and even inputs, is covered by Paper 147. The additional arithmetic observable here is the exact common divisor, its \(r+1\) powers in (1) and its matching floor profile. [One-reset case](SHARP_RESET_RETENTION.md) · [Paper 147, Proposition 1 and Theorem 3](https://rstation.ai/problems/collatz/papers/147)
