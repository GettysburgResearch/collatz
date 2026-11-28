# Exact signed gap-three formula for consecutive original rows

Let \(v_x(d,y)\), \(b_d(x)\) and \(\pi(y)=1/[y(3y+1)]\) be the ordinary all-visit loss, true endpoint mark and target kernel of the [original trace calculation](ORIGINAL_TRACE_VARIATION.md). At every positive odd target \(y\) and every grade \(d\ge0\),
\[
  \pi(y)[\rho_{d+2}(y)-\rho_{d+1}(y)]
     =\tfrac32\sum_{k\ge0}[v_{9k+8}(d,y)-v_{9k+5}(d,y)].             \tag{1}
\]
This identity concerns the unmarked constituent of the original rate test. The two ordinary starts are three apart and retain their actual clocks and target labels.

## Source algebra

Write \(Kf(y)=\sum_{e\ge1}3\,2^{-e} f((2^e y-1)/3)\), summing only integral predecessors and extending \(f\) by zero on ternary nonunits. On odd positive units \(\rho_{d+1}=K^d\rho_1\) with \(\rho_1(x)=x\bmod3\). Put \(\delta=K\rho_1-\rho_1\). Summing the six periodic exponent classes using \(\sum_{r\ge0}2^{-6r}=64/63\) gives
\[
 7\delta(x)=(1,2,4,-10,-5,8)
 \quad\text{for }x\bmod9=(1,2,4,5,7,8),
\]
and zero on the three nonunit classes. Use this table to extend \(\delta\) to even sources. Direct substitution gives
\[
 F(x)=\delta(x)-\tfrac12\delta(2x)
  =\tfrac32\big(\mathbf1_{x\equiv8\pmod9}-\mathbf1_{x\equiv5\pmod9}\big).
\]
An initial coast of \(r\) halvings preserves every odd landing and increases every clock by \(r\), so \(v_{2^ru}=2^{-r}v_u\). For each odd \(u\), the finite sum of \(2^{-r}F(2^ru)\) for \(0\le r<R\) equals \(\delta(u)-2^{-R}\delta(2^Ru)\). Its boundary term tends to zero. Multiplying by \(v_u\) and summing the completed dyadic cones gives (1) by \(K^d\delta=\rho_{d+2}-\rho_{d+1}\). Absolute convergence at a fixed coordinate follows from the row bound \(K^d1\le2^d\) on unit sources and \(\sum_{r\ge0}2^{-r}=2\); the zero coefficients remove nonunits. Every visit is retained.

## A grade-local ordinary upper bound

Fix \(D\ge1\), \(K_0=\lceil 2^{20D}/9\rceil\), \(x_k=9k+5\), \(x'_k=9k+8\). Let \(\chi_d(k)\) be one if the true odd landing and shortcut clock at grade \(d\) differ between the two starts, and zero otherwise. Once zero, it stays zero. Write \(c_d(x)=(b_d(x)-b_{d+1}(x))/x\). Taking absolute values after canceling coincident entries yields
\[
 \sum_{d=D}^{2D-1}\sum_{y>1\ {\rm odd}}\pi(y)|\rho_{d+2}(y)-\rho_{d+1}(y)|
 \le\tfrac32\sum_{k<K_0}\sum_{d=D}^{2D-1}\chi_d(k)[c_d(x_k)+c_d(x'_k)]
         +O(D\theta^D),                                               \tag{2}
\]
where \(\theta=\max\{1/4,36(3/4)^{16}\}<1\). For the tails use \(Y=2^{4D}\). Discarding \(y>Y\) costs \(O(2^d/Y)\) per grade even with all dyadic lifts, whose total weight doubles the former row bound. At \(y\le Y\), omitted sources have \(x\ge9K_0\ge2^{20D}\), hence total clock at least \(16D\). Allow all exponents, including the initial nonnegative halving count \(r\). Its additional exponential moment factor is \(\sum_{r\ge0}2^{-r}(4/3)^r=3\). The remaining positive gaps give the same bound \(O(6^d(3/4)^{16D})\) as before. Summing the target kernel and the grades proves the tail estimate.

The finite sum charges exactly the loss at the tested grades of a still-unsynchronized pair. Earlier failures that have since synchronized disappear. When the two targets coincide with unequal clocks, even (2) can be tightened by taking the absolute difference of those two weights. No exponential estimate for the resulting unpaid loss has been established.

[Original statistic and dyadic mean](ORIGINAL_TRACE_VARIATION.md) · [Lean finite loss telescopes](OriginalLoss.lean) · [Exact source algebra and physical dyadic-cone replay](check_trace_transport.py)
