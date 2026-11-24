# Independent review of the pointwise cycle-denominator implication

**Verdict.** The dependence estimate (14) and full-denominator consequence (15) follow for each primitive positive rational cycle under the stated normalization. In particular the first \(\lfloor\sqrt A/2\rfloor\) suffix centers of a sufficiently long hypothetical ordinary primitive cycle are nonzero and multiplicatively independent modulo sign. This is a pointwise necessary condition on a cycle. The argument places no upper bound on its period and requires no enumeration of the ambient word family.

I used the conventions \(p_j=\#\{\text{odd inputs before cut }j\}\) and \(n_j/d\) for the actual state. A positive cycle contains an odd input, its full gap \(2^A-3^p>0\) is coprime to 6, hence its common reduced denominator \(d\) is coprime to 6. An even minimum would have a strictly smaller successor. The minimum numerator \(m\) is therefore odd. At each odd step, \(2n_{i+1}=3n_i+d\) shows the next numerator is nonzero modulo 3; division by two preserves that property through subsequent even steps. Cyclicity implies \(3\nmid m\). Primitivity gives \(n_j\ne m\) for every \(0<j<A\).

**Reduced denominators.** The actual endpoints of the suffix give \(dC_j=U_jm-V_jn_j\) with \(D_j=U_j-V_j\). Reducing modulo \(D_j\) and cancelling the unit \(U_j\) gives \(\gcd(|D_j|,dC_j)=\gcd(|D_j|,m-n_j)\). Since \(\gcd(|D_j|,C_j)\le\gcd(|D_j|,dC_j)\), the reduced center denominator satisfies \(b_j\ge|D_j|/|m-n_j|\). For \(i<j\), the relation \(D_i=2^hU_j-3^kV_j\) and the same unit cancellation give \(\gcd(b_i,b_j)\mid |2^h-3^k|\), where \(h=j-i>0\), \(k=p_j-p_i\). This integer is nonzero for all \(0\le k\le h\).

**Numerator cancellation at the other centers.** For \(i<j\), every common divisor of \(b_j,|a_i|\) divides \(dC_i\) and \(D_j\), hence divides \(2^hm-3^kn_i\) after cancelling \(U_j\). For \(k>0\) this difference is nonzero modulo 3. For \(k=0\), the intervening even steps give \(n_i=2^hn_j\), so a zero difference contradicts \(n_j\ne m\). For \(i>j\), the reduction of \(2^hdC_i\) modulo \(D_j\) is \(V_i(3^km-2^hn_i)\). The factor \(V_i\) is either one or a power of 3 coprime to \(D_j\); the remaining bracket is odd. Thus both brackets are nonzero and have absolute value at most \(3^{|i-j|}(3/2)^i(m+d)\), by the actual endpoint bound \(n_i+d\le(3/2)^i(m+d)\). If a center numerator is zero, its denominator is one and the zero case of (14) follows directly below.

**The logarithm estimate.** Lagarias, Lemma 2.2(1), equation (2.4), gives \(|\log_3 2-k/L|\ge 1/(1200L^{14.3})\). With \(c_0=\log3/1200\), multiplication by \(L\log3\) gives \(|L\log2-k\log3|\ge c_0L^{-13.3}\). Factoring \(2^L\) and considering both signs of the logarithmic difference yields \(|2^L-3^k|\ge(c_0/2)2^LL^{-13.3}\). Applying this to \(L=A-j\) and the reduced denominator bound gives, with \(M=\log(m+d)\),
\[
 \log b_j\ge A\log2-j\log3-M-13.3\log A+\log(c_0/2).
\]
On the whole cycle, \(A\log2-p\log3=\sum_{\mathrm{odd}\ i}\log(1+d/(3n_i))\le pd/(3m)\). The same estimate at \(L=A\) gives \(m\le(400/\log3)d A^{14.3}\). [Lagarias primary theorem](https://arxiv.org/pdf/math/0512006)

**Pointwise dependence.** In a nontrivial relation among the absolute values of the nonzero centers choose one index \(j\) of maximal absolute coefficient. The same \(j\) works at *every* prime. If \(\ell\mid b_j\), take the \(\ell\)-adic valuation of the relation, apply the triangle inequality, and divide by that maximal absolute coefficient. This gives \(w=v_\ell(b_j)\le\sum_{i\ne j}|v_\ell(c_i)|\). The same bound holds after truncating each summand at \(w\); either a single summand already attains \(w\), or no truncation affects the sum. Reducedness gives \(|v_\ell(c_i)|=v_\ell(|a_i|b_i)\) with only one factor contributing. Summing the truncated inequality with weights \(\log\ell\) gives
\[
 \log b_j\le\sum_{i\ne j}\{\log\gcd(b_j,|a_i|)+\log\gcd(b_j,b_i)\}.
\]
Bounds (9) and (13) control this sum by \((t-1)M+ t(t-1)\log3+\tfrac12t(t+1)\log(3/2)\). Combining it with the lower bound for \(b_j\) and \(j\le t\) gives exactly (14). If \(c_j=0\) use \(b_j=1\) in the same lower bound; the right side of (14) dominates the resulting expression. Since \(M\le\log d+\log(1+(400/\log3)A^{14.3})\), division by \(t\ge1\) gives (15) with an absolute error \(O(t+\log(2A))\). For \(\log d=o(\sqrt A)\), \(t=\lfloor\sqrt A/2\rfloor\), its explicit predecessor (14) would have right side at most \((\log3/4+\log(3/2)/8+o(1))A <(0.326+o(1))A\). This is incompatible with \(A\log2\).

The same calculation gives an explicit witness to independence. For each \(j\) in this regime, the upper bound for the sum of cross-gcd logarithms is strictly less than the lower bound for \(\log b_j\). Thus there is a prime \(\ell_j\mid b_j\) for which \(v_{\ell_j}(b_j)>\sum_{i\ne j}|v_{\ell_j}(c_i)|\). Otherwise the truncation argument would give the opposite logarithmic inequality. These primes must be distinct; their square valuation matrix is strictly diagonally dominant. This is an independent consequence of the same written estimates.

## Reviewed bytes and verification scope

| Source under research/astra-global-closure-20261124/closing/cycles | SHA-256 |
| --- | --- |
| NEAR_MINIMUM.md | 2d1c75cb221917c038e3929e6c73004a442445537de843f78db2f1ffea26fad5 |
| DenominatorBudget.lean | defafaf8f5fb735e4ad12f7119be0361fb43b787d9061253cf102ee34f0638bb |
| ValuationDominance.lean | c9bc26ec2b1e91d1ac8cbabc8fc510c39bf33475e6f211be34be84e9fead4c39 |

I checked the final source hashes against the author's freeze, inspected the mathematical hypotheses and the valuation declarations, and independently consulted the cited Lagarias theorem. The author reports ten strict Lean checks for the finite components. I did not rerun those compiler jobs. The pointwise logarithmic estimates, the full implication (14)–(15), the infinite-period asymptotic, and the prime-witness corollary above have written proofs. This review does not audit the separate ambient-word counts or a computational period search.

