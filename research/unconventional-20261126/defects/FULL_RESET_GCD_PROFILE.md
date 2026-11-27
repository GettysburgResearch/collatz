# Including powers of two in the persistent reset gcd

Use Theorem D's notation in [the fixed-reset divisor theorem](PERSISTENT_RESET_DIVISOR.md). Write \(m=\min_{0\le j\le r}t_j\). The full common divisor of all \(r+1\) shifted endpoints is \(G=2^m g\). At any fixed terminal floor \(x_r\ge\lambda Y^\sigma\), for \(r\ge1,\ \lambda>0,\ 0\le\sigma<\alpha=\log_2 3\), its sharp exponent is
\[
       \limsup_{Y\to\infty}\frac{\log G}{\log Y}
        =\min\left\{\frac1{r+1},\frac{\alpha-\sigma}{\alpha-1}\right\}.
\]
The same value holds on initial odd multiples of three. As for Theorem D, the asymptotic upper cutoff is potentially ineffective and the sharpness construction is explicit.

Indeed, put \(\beta=\alpha-1\). The bound \(G^{r+1}\le Y^{1+o(1)}\) already gives the first ceiling. Combine
\[
  (r+1)\log g+(T+t_r)\log 2\le(1+o(1))\log Y,\qquad
  \sigma\log Y\le\log Y+\beta T\log2-r\log g+O_{r,\lambda}(1).
\]
Using \(t_r\ge m\) gives the stronger joint estimate
\[
             \beta\log G+r\alpha\log g
                 \le(\alpha-\sigma+o(1))\log Y.
\]
Dropping its nonnegative final term gives the second ceiling.

For the lower bound let \(c\to\infty\) and prescribe \(b_j=1\) at every one of the \(r\) completed blocks. Prescribe \(t_j\ge c\) at their entrances and exactly \(t_r=c\) at the terminal boundary. In shortcut parity bits this appends \(O^c E\) after the \(r\) complete runs \(O^{t_j}E\). A single binary cylinder realizes all these requirements. Intersect it with \(x_0=0\pmod3\) and take a representative between one and two of the joint moduli. The first reset already forces \(g\mid2^1-1=1\). Hence the full gcd is exactly \(2^c\), while
\[
             \log_2Y=T+c+O_r(1),\qquad
             \log_2x_r=\alpha T+c+O_r(1).
\]
Put
\[
  T=\max\left\{rc,\left\lceil\frac{\sigma-1}{\alpha-\sigma}c\right\rceil\right\}+K
\]
with a sufficiently large fixed \(K=K(r,\lambda,\sigma)\). Partition \(T\) into \(r\) positive parts each at least \(c\). The two logarithmic estimates ensure \(\log_2x_r-\sigma\log_2Y\ge\log_2\lambda\) for all sufficiently large \(c\). Evaluating the limit of \(c/(T+c)\) proves the asserted exponent in both regimes. For large \(c\) each block gain is greater than one.

At a comparable terminal height, the full gcd can therefore reach the exponent \(1/(r+1)\) purely through powers of two. The odd persistent part has the smaller sharp exponent \(\beta/[r+(r+1)\beta]\) there. This comparison holds for true positive ordinary segments with any mixture of other factors; neither form forces a large gcd to occur on an arbitrary escaping orbit.
