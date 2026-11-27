# Uniform dependence on the largest block key

**Written refinement.** With the hypotheses and notation of the monotone-duration theorem, let \(N\) be the total number of physical shortcut transitions, \(Y_0=x+1\), and \(G=2+\max(0,\log_2(1+K))\). There is an absolute \(C\) such that
\[
       \log(2+N)\le \exp(CG^2)\,\log(2+\log Y_0).                  \tag{4}
\]
All logarithm bases in (4) may be fixed once for all, with a change in \(C\). This inequality covers arbitrarily varying input caps \(K\). No numerical value of the absolute constant is asserted.

To track the constants in (1) of the companion proof, \(\log_2 M=O(G)\). Hence \(t\le\log_2Y_j\le C_0 G S_j\), and
\[
             l\le1+\frac{\log_2Y_j+O(G)}{t+b}
                    \le C_1G S_j/t
\]
with absolute \(C_0,C_1\). Fix an absolute \(c>0\) sufficiently small and use bin width \(\eta=c/G\). The interval \([-1,\log_2(1+K)]\) requires \(O(G^2)\) bins when nonempty. At fixed \(t\), changing \(b\) to \(b+1\) decreases \(u=\log_2(1+k)\) by \(\log_2((2^{b+1}-1)/(2^b-1))>1\). Thus each \(t\) supplies at most one \(b\) per bin, even at small \(t\). Also
\[
 2^b=1+\frac{(3/2)^t-1}{2^u}\ge 1+\frac{(3/2)^t-1}{2^G}.
\]
For \(t\ge C_c G\), both \((2/3)^t\) and \(2^{-b}\) are at most a sufficiently small fixed multiple of \(c/G\). Thus the \(t\) in any bin above this threshold have fractional phase \(t\theta\bmod1\) in an interval of length at most \(3\eta\), as in equation (2). The constant \(C_c\) is absolute after \(c\) is fixed.

Here is an effective uniform substitute for the qualitative equidistribution bound. For \(m\ge1\) and nearest integer \(n\) to \(m\theta\), unique factorization gives \(3^m\ne2^{m+n}\). The mean value theorem and \(2^{m+n}\asymp3^m\) give \(\|m\theta\|\ge c_0 3^{-m}\) with an absolute \(c_0>0\). Take a continued-fraction denominator \(q\) of \(\theta\) that is first to exceed \(20/\eta\). Its predecessor \(q'\) is at most \(20/\eta\). The convergent inequality \(\|q'\theta\|<1/q\) gives \(q\le c_0^{-1}3^{20/\eta}\). In particular
\[
                       20/\eta<q\le\exp(C_c G).
\]
Every \(q\) consecutive phases are within \(1/q\) of a translate of the \(q\)-point grid, by approximating \(\theta\) by its reduced convergent of denominator \(q\) inside that block. Hence at most \(3\eta q+4\le4\eta q\) points of such a block lie in the enlarged bin. The first \(\max(q,C_cG)\) eligible \(t\)'s by *height cutoff* cost only \(O_c(G)\) in harmonic weight. Above that cutoff, grouping into consecutive blocks of length \(q\) costs at most \(4\eta(1+\ln(1+T))\) up to \(T\), by summing \(4\eta q/(jq)\) on the \(j\)-th full-length block, including a final partial block. Thus the contribution in (3) is at most \(O_c(G)+4\eta\ln(1+T)\), uniformly in each bin.

At the end index \(e\) of the bin, \(T\le C_0 G S_e\). Inserting the improved constants in (1) gives
\[
 \ln S_e-\ln S_s
   \le O_c(G^2)+4C_1G\eta\ln(1+C_0GS_e)
   \le O_c(G^2)+\tfrac12\ln S_e
\]
by the fixed choice of \(c\). Thus \(\ln S_e\le2\ln S_s+O(G^2)\) per bin. The at-most-one stratum with \(k\le-1/2\) adds \(O(G S_s)\) blocks and therefore only \(O(\log(2+G))\) to \(\ln S_s\). Over \(O(G^2)\) bins this proves \(\ln S_{\rm final}\le\exp(C G^2)\ln S_0\), absorbing \(G^2\) since \(S_0\ge2\). Each physical block has length \(t+b\le C G S_{\rm final}\), giving (4).

On a fixed ordinary escaping trajectory with nondecreasing keys, take its current key as \(K\) in every prefix. Thus \(\log(1+k)\gg\sqrt{\log\log(2+N)}\) for sufficiently late clocks at block boundaries, with the threshold allowed to depend on the fixed source. The conclusion still concerns monotonicity in the real order, not conditional maximality in a ternary carry class.
