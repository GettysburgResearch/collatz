# The precise moment cost of escaping the full-path principle

**Proposed, source-qualified written theorem.** For the genuine positive shortcut let \(\tau_*(n)\) be the native time of its first global minimum. It is finite for each individual \(n\). Define the finite empirical moment index
\[
 p_*=\sup\left(\{0\}\cup
 \{r>0:\ \exists C_r,D_r<\infty,\quad
 M^{-1}\textstyle\sum_{n\le M}(1+\tau_*(n))^r\le D_r(1+\ln M)^{C_r}
 \text{ for all integers }M\ge2\}\right).
\]
Let \(Z_X\) be the actual minimum-capped centered and normalized path on the full interval \([0,1]\) from [the endpoint theorem](MODERATE_DEVIATIONS_AT_THE_MINIMUM.md), and put
\[
 B_*=\sup\left(\{0\}\cup
 \{B>0:\ \exists\text{ compact }K\subset\ell^\infty[0,1],\
  \limsup_{X\to\infty}\frac{\ln\Pr(Z_X\notin K)}{\ln\ln X}\le-B\}\right).
\]
Then, including the possibilities zero and infinity,
\[
                          B_*=p_*/2.                                      \tag{1}
\]
Below \(p_*\) the moment bounds improve to the correct uncentered logarithmic order:
\[
 \frac1M\sum_{n\le M}(1+\tau_*(n))^r\sim(\mu\ln M)^r
                         \qquad(0<r<p_*),\qquad \mu=2/\ln(4/3).           \tag{2}
\]
In particular the full path large-deviation principle holds exactly when finite population moments of every order have some polylogarithmic bound. If it holds, the largest first-minimum time below \(M\) is \(M^{o(1)}\). More generally put \(\omega=\limsup_{M\to\infty}\ln(1+\max_{n\le M}\tau_*(n))/\ln M\). Then \(B_*\le1/(2\omega)\) with reciprocal endpoint conventions. No estimate of \(p_*\) or \(\omega\) is assumed.

The lower transfer uses Weaver's actual uniform clocked first-landing theorem under its stated selected-word and joint mixing inputs. Leen's moderate-deviation supplement gives sufficient odd-clock tail bounds and a separate polylogarithmic worst-case sufficient condition. Here a uniform lower transfer **from each individual ordinary clock** is responsible for the necessity and the exact factor \(1/2\). [Weaver, Paper 12 v1, Theorem 14, equations (40)–(41)](https://rstation.ai/problems/collatz/papers/12/v1) · [Leen, sufficient conditions at the minimum](https://zenodo.org/api/records/23269488/files/collatz-brownian-motion-md.tex/content)

## Moments give compact containment

Take any \(r\) satisfying the displayed moment hypothesis. On an odd octave \([Y',2Y')\) its \(r\)-th moment is bounded by a constant times \((1+\ln Y')^{C_r}\), by counting inside \([1,2Y']\). Write \(L=\ln Y\). At the moving gate \(z=\exp(L^e)\), \(0<e<1/2\), the reference \(Y'=z^{1.001}\) thus has
\[
 \Pr(\tau_*(W_{Y'})>\rho\sqrt{L\ln L})
              \ll_{r,\rho} L^{-r/2+eC_r}(\ln L)^{-r/2}                  \tag{3}
\]
for any fixed \(\rho>0\). On a successful reference passage its odd landing \(P\) has \(\tau_*(P)\le\tau_*(W_{Y'})\) since every prior value exceeds \(P\). The relative unmarked landing law, with arbitrary \(O_A((\ln z)^{-A})\) floor, transports the bounded large-\(\tau_*(P)\) test to every outer odd \(W_Y\). As proved in the endpoint theorem, missing this moving gate or a final halving run longer than \(C_A\ln L\) cost \(O_A(L^{-A})\) for any desired \(A\) after choosing the local exponent. Every subsequent passage time is between its native entrance date and the actual minimum date. Hence the whole uniform discrepancy between the actual path and the moving-cutoff path exceeds \(\rho\) with limsup log probability at speed \(\ln L\) at most \(-r/2+eC_r\). The all-integer disintegration there uses a deterministic larger gate with \(\ln z=2L^e\) to handle the variation of \(\ln n\); this costs only a fixed multiplicative factor in (3).

The moving-cutoff paths are exponentially tight by the polygonal approximation in that theorem. Fix \(B<B'<r/2-eC_r\). For each integer \(j\ge1\) choose a compact set for the moving-cutoff paths at exponent larger than \(B'\) and a finite \(1/j\)-net for it. Estimate (3) with tolerance \(1/j\) yields a finite \(3/j\)-ball cover for the actual paths with exceptional probability at most \(2^{-j}(\ln X)^{-B}\) for all sufficiently large \(X\) depending on \(j\). Add the finitely many paths at smaller integer \(X\) to the centers. The intersection over \(j\) of the finite unions of closed balls is closed and totally bounded, hence compact in the uniform norm; its exceptional probability is at most \((\ln X)^{-B}\). Sending \(e\downarrow0\) proves \(B_*\ge p_*/2\).

## A slow individual source contributes at every higher scale

Suppose a compact set witnesses \(B>0\), and take any \(0<b<B\). Bounded evaluation at the endpoint gives some finite \(K>0\) such that for all large integer \(X\), with \(L=\ln X\),
\[
 X^{-1}\#\{n\le X:\tau_*(n)-\mu\ln n>K\sqrt{L\ln L}\}\ll_b L^{-b}.     \tag{4}
\]
For any \(M\ge2,\ X\ge C M\), and any odd positive \(a\le M\) prime to three, the cited Theorem 14 supplies at least \(cX/M\) odd \(n\in(X/4,X]\) whose first odd iterate at or below \(M\) is precisely \(a\). On the selected paths its native entrance date \(D\) satisfies
\[
 D=\mu\ln(X/M)+\log_2(M/a)+O(\sqrt{\ln(X/M)}+1)
\]
with absolute constants. All earlier odd values exceed \(M\). Any earlier even state is strictly larger than its following odd endpoint, which until this entrance is either above \(M\) or equal to \(a\). Consequently every earlier native state exceeds \(a\) and \(\tau_*(n)=D+\tau_*(a)\), also for periodic \(a\). Distinct \(a\)'s contribute disjoint sets. Thus if \(\tau_*(a)\ge u\), all these \(n\) have
\[
          \tau_*(n)-\mu\ln n\ge u-\mu\ln M-C_1(\sqrt L+1).              \tag{5}
\]

For \(u\ge C_2(1+\ln M)\) choose the integer \(X\) nearest to \(\exp(u^2/(C_3\ln(u+2)))\). First choose \(C_3\) large in terms of \(K,C_1\); then choose \(C_2\) large in terms of the previous constants and the onset in (4). This ensures \(X\ge CM\), \(\mu\ln M\le u/4\), and \(C_1(\sqrt L+1)+K\sqrt{L\ln L}<u/2\). Equations (4) and (5), summed over the distinct atoms, now give the uniform tail bound
\[
 \frac1M\#\{a\le M:\gcd(a,6)=1,\ \tau_*(a)\ge u\}
                      \ll_b \left(\frac{\ln(u+2)}{u^2}\right)^b .       \tag{6}
\]
This choice of the outer scale is available at every \(u\), with no target-dependent onset in the landing theorem.

For an odd \(a\) divisible by three use the injective unit \(\phi(a)=4a+1\le4M+1\). Its first three native steps arrive at the same state as the first native step of \(a\), with the two intervening states strictly above \(a\). If \(\tau_*(a)>0\), its future global minimum is strictly below \(a\), so \(\tau_*(\phi(a))=\tau_*(a)+2\). Equation (6) at \(4M+1\) bounds these odd sources as well. For even sources write \(n=2^i a\) with \(a\) odd, giving \(\tau_*(n)=i+\tau_*(a)\). Increase \(C_2\) so that \(i<u/2\), apply the odd bound at each \(M/2^i\) with threshold \(u/2\), and sum with weights \(O(2^{-i})\). This proves (6) for all ordinary starts with an adjusted constant.

Integrating (6) above \(C_2(1+\ln M)\) gives \(M^{-1}\sum_{n\le M}(1+\tau_*(n))^r=O_r((1+\ln M)^r)\) for every \(r<2b\), because \(u^{r-1-2b}(\ln(u+2))^b\) is integrable at infinity. Therefore \(p_*\ge2B_*\), completing (1). For \(r<p_*\) the same argument gives a bounded normalized moment of some order \(r'>r\). Leen's actual minimum clock law implies \(\tau_*(n)/(\mu\ln M)\to1\) in probability for uniform \(n\le M\); uniform integrability gives (2). A single maximal summand is at most \(M\) times the empirical moment, so \(\omega\le1/r\) for each \(r<p_*\). The full-path and record consequences follow using the endpoint theorem.
