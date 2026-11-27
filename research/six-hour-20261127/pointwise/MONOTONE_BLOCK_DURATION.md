# A monotone order of complete blocks has polynomial duration in log height

**Status.** Written theorem for one supplied positive ordinary source. The repeated-block identity is kernel-checked in the companion Lean module. Phase counting and the duration estimate are written mathematics.

At an odd entrance put \(Y=x+1=2^t w\), with \(w\) odd. After \(t\) odd and \(b=v_2(3^tw-1)\) even shortcut departures the next odd entrance is \(z=(3^tw-1)/2^b\). Thus
\[
 F(Y)=\alpha Y+\beta,\qquad \alpha=3^t/2^{t+b},\quad
 \beta=1-2^{-b},\quad
 k(t,b)=\frac{\alpha-1}{\beta}=\frac{(3/2)^t-1}{2^b-1}-1.
\]
Both \(t,b\ge1\).

**Theorem.** Fix \(K>-1\). There exist \(C_K,D_K>0\) such that every finite segment of consecutive complete blocks from \(x\), with pairwise distinct block-boundary states, has at most
\[
                         C_K(1+\log(x+1))^{D_K}
\]
physical shortcut transitions if its keys are monotone and at most \(K\). Either monotonicity direction is allowed. The constants are independent of the alphabet, repetition lengths, source and minimum height.

For two shifted block maps \(A,B\), direct expansion gives
\[
             F_BF_A(Y)-F_AF_B(Y)=\beta_A\beta_B(k_B-k_A).
\]
All later multipliers are positive. Thus sorting a fixed multiset in nondecreasing key order maximizes its affine endpoint and carry in the real order. Since \(v_2(k+1)=-t\) and \(k\) then determines \(b\), distinct block types have distinct keys. The sorted word is the unique maximizing block word. Sorting alone does not ensure a compensating entrance is integral.

## Bound for one constant run

Write \(Y_j\) for the shifted height after \(j\) blocks and \(M=\max(2,2+\max(K,0))\). Then \(Y_{j+1}\le M Y_j\). For \(S_j=2+\log_2Y_0+j\) there is \(L=L_K\ge1\) with
\[
         \log_2Y_j\le L S_j,\qquad t_j\le\log_2Y_j\le L S_j .
\]
Also \(2^{b_j}\le 3^{t_j}Y_j/2^{t_j}\), hence \(b_j\le\log_2Y_j+t_j\log_2(3/2)\).

For a run of \(l\) identical blocks starting at \(j\), put \(A=3^t,\ B=2^{t+b},\ D=2^t(2^b-1)\). Iterating \(BY_{r+1}=AY_r+D\) gives
\[
 B^l\big((A-B)Y_{j+l}+D\big)=A^l\big((A-B)Y_j+D\big).
\]
The initial marker \((A-B)Y_j+D\) is a nonzero integer: if zero, the first step of the run repeats its boundary. Since \(A\) is odd, \(B^l\) divides the marker. We have \(D<B\), \(A/B\le1+\max(K,0)\), and \(Y_j\ge2\), so its absolute value is at most \((2+\max(K,0))BY_j\). Taking logarithms gives
\[
          l\le1+\frac{\log_2Y_j+O_K(1)}{t+b},
          \qquad S_{j+l}\le S_j(1+C_1/t) .                         \tag{1}
\]
The second inequality uses \(t\le LS_j\). The constant \(C_1\) depends only on \(K\).

## Chronological intervals of keys

Under monotonicity, the blocks with \(k\le-1/2\) form at most one interval. On this interval \(\alpha=1+\beta k\le3/4\). When \(Y\ge8\), \(F(Y)\le3Y/4+1\le7Y/8\). When \(Y<8\), it remains below eight and can take at most a fixed number of distinct positive boundary values. This interval has \(O(1+\log Y_j)\) blocks from its first index \(j\), increasing \(S_j\) by at most a constant factor. This also proves the needed estimate when \(K\le-1/2\).

In the remaining range, \(u=\log_2(1+k)\) lies in the compact interval \([-1,\log_2(1+K)]\). Choose \(\eta>0\) with \(3\eta<1\) and \(4C_1\eta\le1/2\). Partition this interval into finitely many consecutive bins of width at most \(\eta\), assigning each endpoint to exactly one bin. Each bin is visited in at most one chronological interval. Fix a bin \(I\), and write \(\theta=\log_2(3/2)\). The exact identity
\[
 t\theta-b=u-\log_2(1-(2/3)^t)+\log_2(1-2^{-b})                   \tag{2}
\]
follows from the definition of the key. The bound \(b=t\theta+O_K(1)\) is uniform on the compact range, by \(2^b=1+((3/2)^t-1)/(1+k)\). Therefore both correction terms in (2) tend uniformly to zero. Above a threshold depending only on \(K,\eta\), \(t\theta-b\) lies in the enlargement of \(I\) by \(\eta\) on each side. This interval has length at most \(3\eta<1\), so each such \(t\) determines at most one integer \(b\) in the bin. The bounded exceptional \(t\) allow only finitely many \(b\).

The number \(\theta\) is irrational by unique factorization. The phases \(t\theta\bmod1\) are uniformly distributed: every nonzero integral frequency has vanishing Weyl average by the geometric-series formula, and approximation of intervals by trigonometric polynomials yields their frequencies. The circle projection of the enlarged bin has measure at most \(3\eta\). Its eligible \(t\le T\) thus eventually number at most \(4\eta T\). Partial summation, absorbing the finitely many small types in a constant, gives
\[
        \sum_{\substack{(t,b)\ {\rm distinct\ in\ this\ bin}\\ t\le T}} \frac1t
                       \le c_I+4\eta\ln(1+T).                      \tag{3}
\]
This counts possible block types, with no statistical assumption on the supplied trajectory. There are finitely many bins, so the constants can take their common maximum.

Let \(s,e\) be the starting and ending indices of the bin. Monotonicity and injectivity of \(k\) put each distinct block type in a single run. Sum \(\ln(S_{j+l}/S_j)\le C_1/t\) from (1) over the runs and use (3) with \(T\le L S_e\). This gives
\[
         \ln S_e-\ln S_s \le C_2+4C_1\eta\ln(1+LS_e).
\]
Our choice \(4C_1\eta\le1/2\) gives \(S_e\le C_3 S_s^2\) uniformly across bins and starting heights. Iterate through the fixed finite list of bins and the single possible contracting interval to obtain \(S_{\rm final}\le C_4 S_0^{D'}\). Each block has at most \(O_K(S_{\rm final})\) physical transitions by the bounds on \(t_j,b_j\). There are at most \(S_{\rm final}\) blocks. This proves the theorem after doubling \(D'\).

## Consequences for a supplied infinite trajectory

An ordinary trajectory with a monotone bounded-above key tail must repeat a boundary. The resulting periodic key tail is constant by monotonicity and hence repeats one block type. An increasing affine map has no real periodic points other than its fixed point. Thus the odd trajectory eventually repeats a single complete block. The classification of positive one-block cycles is unnecessary here.

If every prefix of a hypothetical escaping trajectory maximizes the unrestricted real carry over its multiset of blocks, its keys must be nondecreasing by the adjacent exchange formula. They must then tend to \(+\infty\) by the theorem. Since \(\beta\ge1/2\), this forces \(Y_{j+1}/Y_j\to\infty\) and \(t_j\to\infty\). Modular-class maximality alone does not force this order. The companion note gives unordered, reverse-decodable dictionaries for which every permitted carry class is a singleton.

**Earlier work.** The dependence of affine block composition on order and noncommutation appear in [Paper 201](https://rstation.ai/problems/collatz/papers/201). Finite dictionary-piece duration estimates with a cost per piece appear in [Paper 15](https://rstation.ai/problems/collatz/papers/15). The theorem above permits an unrestricted input-dependent alphabet, with a monotonicity condition on the actual keys and one common upper bound on them.
