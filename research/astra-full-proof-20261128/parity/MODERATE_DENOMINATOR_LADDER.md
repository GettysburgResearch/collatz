# Ternary denominators at the moderate critical clock

This note gives an exact telescoping formula for the positive-source parity tail and removes all but \(O(g)\) denominator levels. The remaining positive integer sampling estimate is open. The low-level bound uses the written signed starting-trit theorem in PR215. The finite formula has an independent exact-integer replay.

Write \(\lambda=\log_2 3\), \(\kappa=1/(1-\lambda/2)\), \(N=2^k\), \(g=k^\gamma,\ 1/2<\gamma<2/3\),
\(m=\lfloor\kappa k+g\rfloor,\ a=1/16,\ H=\lceil m/2+ag\rceil\). Use \(T(x)=x/2\) or \((3x+1)/2\) according to its low binary bit on \(\mathbf Z[1/3]\). Write \(Q_t\) for its number of odd departures. The positive-source target is \(\Pr_{1\le n\le N}(Q_m(n)\ge H)=o(1)\). All arguments below also work along an unbounded subsequence. The all-source consumer is treated independently in the sprint.

## The exact ladder

For \(0\le r\le H\), set
\[
P_r=(N3^r)^{-1}\sum_{1\le u\le N3^r}1_{\{Q_m(u/3^r)\ge H\}} .
\]
By pulling back the subgroup \(3\mid u\) one has
\[
\Delta_r=P_{r-1}-P_r=(N3^r)^{-1}\sum_{u\le N3^r}(3\,1_{\{3\mid u\}}-1)1_{\{Q_m(u/3^r)\ge H\}} .
\]
For a binary word \(w\) of length \(t\) write \(F_w(x)=(3^{q}x+C_w)/2^t\), \(B_w=C_w/2^t\), with \(q\) its number of ones. If the last step is odd then \(C_w\equiv2^{t-1}\pmod3\). Let \({\cal W}_{r,t}\) be words ending in their \(r\)-th one. Then
\[
\Delta_r=\sum_{t=r}^{m}\sum_{w\in{\cal W}_{r,t}}\frac{2^{-t}}{Y_{r,t}}
 \sum_{B_w<y\le B_w+Y_{r,t}}\!
 (3\,1_{\{y\equiv2\ (3)\}}-1)\,
 1_{\{Q_{m-t}(y)\ge H-r\}},
 \qquad Y_{r,t}=N3^r/2^t.                                      \tag{1}
\]
The inner sum is over ordinary positive integers. Indeed \(T^t(u/3^r)=(u+C_w)/2^t=y\) for this word. Conversely \(u=2^t y-C_w\) gives its unique congruence class modulo \(2^t\). Integrality after all \(t\) formal steps forces every preceding branch parity, by reducing the affine numerator modulo \(2\) and inducting. The bounds on \(u\) are exactly the given bounds on \(y\). Finally \(3\mid u\) iff \(2^t y\equiv2^{t-1}\pmod3\), or \(y\equiv2\pmod3\), independently of the word. Since \(r\le H\), any source contributing to \(\Delta_r\) has such a stopping word. Also \(2^{-t}/Y_{r,t}=1/(N3^r)\), as required.

## The upper anchor

For \(r=H\), put \(K=k+\lambda H\) and \(L=\lfloor K-3\log_2 k\rfloor\). For all large \(k\), \(L<m\).
The first \(L\) parity bits on \(u/3^H\) form the usual triangular bijection of residues modulo \(2^L\), with the odd denominator invertible. Complete periods give total variation \(O(2^L/(N3^H))=O(k^{-3})\) from independent fair bits. With \(\delta=1-\lambda/2-\lambda a\),
\[
m-L=\delta g+O(\log k),\qquad \delta<2a.
\]
The latter follows from \(\lambda>14/9\) for \(a=1/16\), or \(3^9>2^{14}\). Consequently \(Q_m\ge H\) forces \(Q_L-L/2\ge(a-\delta/2)g-O(\log k)\). Hoeffding's bound and \(g/\sqrt k\to\infty\) give \(P_H=o(1)\). This uses only a fair initial segment and the deterministic maximal contribution of the remaining \(m-L\) steps.

## Long ordinary intervals remove the low levels

Put \(r_*=\kappa k/2=k/(2-\lambda)\), \(h=\sqrt{k}\log k\), \(r_-=\lfloor r_*-h\rfloor\). We claim
\[
\sum_{1\le r\le r_-}|\Delta_r|=o(1).                              \tag{2}
\]
For one such \(r\), set \(K_r=k+\lambda r,\ S=K_r-2r=(2-\lambda)(r_*-r)\) and \(t_0=\lfloor2r+S/2\rfloor\). We have \(S\gg h,\ t_0<m,\ 2^{t_0}/(N3^r)\le2^{-S/2}\).
Under the true \(u\)-law, the first \(t_0\) bits have total variation \(O(2^{-S/2})\) from fair bits. In particular the mass whose \(r\)-th odd step is later than \(t_0\) is \(O(\exp(-cS^2/k)+2^{-S/2})\) by the binomial lower-tail bound. Its signed contribution is at most twice this mass.

Under the fair infinite-bit law write \(E_i\ge1\) for the time between successive odd departures, including the odd step itself. These are independent with \(\Pr(E_i=e)=2^{-e}\). At those stopping times the successive real offsets satisfy \(B_0=0,\ B_i=3\,2^{-E_i}B_{i-1}+1/2\). Hence
\[
\mathbf E \sqrt{B_i}\le \frac{\sqrt3}{2^{3/2}-1}\mathbf E\sqrt{B_{i-1}}+2^{-1/2},
\qquad \sqrt3/(2^{3/2}-1)<1 .
\]
Thus \(\sup_i\mathbf E\sqrt{B_i}<\infty\). On the true law the mass of words stopping by \(t_0\) with \(B_w>2^{S/4}\) is \(O(2^{-S/8}+2^{-S/2})\), by total variation and Markov. This excludes long and large-offset words on their *actual source mass*, before using a lower bound on \(Y\).

For all remaining words, \(Y\ge2^{S/2},\ B_w\le2^{S/4}\). Apply the written, uniform-in-residual-time count-marginal starting-trit estimate to \(1_{\{Q_{m-t}(y)\ge H-r\}}\) through \(B_w+Y\). The deleted lower segment costs \(O(B_w/Y)\). The normalized inner sum of (1) is therefore \(O_A((1+S)^{-A}+2^{-S/4})\); the total fair stopping-word weights \(\sum 2^{-t}\) are at most one. This proves (2) after summation (take \(A>4\)); the claimed estimate is source-qualified by [PR215, equation (3), count-only version](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md).

## What the middle levels require

Telescoping and the preceding bounds give
\[
P_0=\sum_{r_-<r\le H}\Delta_r+o(1).                               \tag{3}
\]
The interval contains \(O(g)\) levels. For \(r=r_*+v g\), \(v>0\), and a word of typical fair stopping length \(t=2r+O(\sqrt k)\), one has \(Y=2^{-(2-\lambda)vg+O(\sqrt k)}\). Then the ordinary integer \(y\) samples a tiny left neighborhood of \(y\) under \(B_w\). The prefactor \(1/Y\) matters. Uniform additive \(o(1)\) errors for individual conditioned Fourier characters do not estimate (1). The full signed sum in (3), or a different estimate implying its decay, remains to be proved. The finite replay checks (1), not this asymptotic.

For comparison, conditional on exactly \(q\) ones in \(m\) bits and with \(p=q/m\), the first \(L=o(m)\) bits in either order are within \(O(L/m)\) total variation of iid Bernoulli(\(p\)), uniformly for \(0<p<1\): at step \(i+1\) the conditional parameter is \((q-S_i)/(m-i)\); the chain rule and the Bernoulli upper bound on relative entropy give \(D\le\sum_{i<L}i/((m-1)(m-i))\) by the hypergeometric variance. Pinsker gives the result. Replacing \(p\) by \(1/2\) adds \(O(|q-m/2|\sqrt L/m)\) when \(p\) is bounded away from 0 and 1. In the range \(L=O(g),\ |q-m/2|=O(g),\ g=o(m^{2/3})\), this is still \(o(1)\). This controls short-digit cylinder tests. Multiplying that additive error by \(1/Y\) in the middle levels would invalidate the argument. [Fixed-character real and ternary argument, primary discussion](https://rstation.ai/r/collatz/posts/36)
