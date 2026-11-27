# A finite positive current on the strict ascent section

Let \(C\) be a hypothetical component of positive odd escaping integers. Use the corrected height \(P(x)=x\prod_{j\ge0}(1+1/(3U^j x))\) and physical exponent sums \(A_n(x)\). Put \(a_*=\log_2 3\) and \(\theta=H_2(1/a_*)\). For fixed \(a_*\le a<2\), an ordinary vertex is called passing here if \(A_i(x)\le ai\) for all \(i\ge1\). Denote these vertices of \(C\) by \(S_a\). At \(a=a_*\) they are exactly the future minima of corrected height: \(P(U^i x)\ge P(x)\) at every \(i\). At each \(a\) every escaping orbit has infinitely many passing vertices, since \(A_n-an=\log_2(P(x)/P(U^n x))+(a_*-a)n\to-\infty\); the successive maxima of the remaining tails of this sequence give such indices.

Define \(\mathcal W_a\) as the outward inverse words \(w=(e_1,\ldots,e_l)\) for which \(D_i=\sum_{r\le i}(e_r-a)>0\) for \(0<i<l\) and \(D_l\le0\). Let \(I_w\) be the composition outward from its target, \(\omega_w=3^l2^{-\sum e_i}\), and include a word only if all of its ternary divisions are integral. On an eligible positive odd target every inverse endpoint is again a positive odd integer. For \(t>H_2(1/a)\) set
\[
 \Xi_{a,t}=\sum_{x\in S_a} P(x)^{-t}\delta_{(x_2,x_3)},\qquad
 (K_{a,t} f)(y)=\sum_{w\in\mathcal W_a,\ \mathrm{eligible}}\omega_w^t f(I_w y).
\]
Both local coordinates of a physical site mean the same positive integer. For a nonnegative Borel test, interpret the transfer by monotone summation. This gives an exact **finite, nonzero, atomic** fixed measure
\[
                         K_{a,t}^*\Xi_{a,t}=\Xi_{a,t}.                     \tag{1}
\]
Indeed let \(y\in S_a\). If a word of length \(l\) is eligible, its ordinary starting endpoint \(x=I_w(y)\) passes forever exactly when \(D_l\le D_i\) for every \(0\le i<l\). This is the chronological prefix inequality reversed, continued beyond the word using that \(y\) passes. A nearer inverse endpoint at distance \(i\) passes when \(D_i\) is at most all its preceding partial sums. Thus the first preceding passing vertex is selected precisely by \(D_i>0\) for \(0<i<l\) and \(D_l\le0\). Paths joining an escaping component have no repeats. Each passing \(x\) has one next passing vertex on its future, and \(P(x)^{-t}=\omega_w^tP(y)^{-t}\). Reindexing proves (1).

For finiteness, the first \(k\) physical shortcut departures from a passing odd source include at least \(k/a\) odd departures. To see this, take the first odd clock \(i\) with \(A_i\ge k\); its \(i\)-th odd departure is included in the first \(k\) shortcuts and \(i\ge k/a\). The parity-word bijection bounds the number of such positive sources in \([2^k,2^{k+1})\) by \(O((k+1)2^{kH_2(1/a)})\). Summing \(P(x)^{-t}\le x^{-t}\) proves the claim. The same argument gives finiteness of every logarithmic moment and of \(\int P^u\,d\Xi_{a,t}\) for \(0\le u<t-H_2(1/a)\). This uses the source entropy estimate in [PR200's joint pressure calculation](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md). Its fixed-slope first-moment endpoint remains open. The [prior ordinary record theorem](../../astra-unconventional-20261126/boundary/ORDINARY_RENEWAL.md) considered chronological first records at ordinary positive-density sources.

## What happens at the quadratic exponent

At \(a=a_*\) an induced inverse word has \(1<\omega_w\le3/2\). Equality at 1 is impossible by multiplicative independence. Its terminal ancestor \(x=(y-\beta_w)/\omega_w\) is strictly smaller than the positive target \(y\). On an actual passage between two consecutive passing phases, all intermediate corrected heights strictly exceed the higher endpoint, by \(D_i>0\). Thus the induced inverse ancestry of each fixed positive target has finite depth, whether or not it is a passing point.

The scalar Haar integral on the ternary coordinate is explicit. Each outward word has an eligible cylinder of Haar measure \(3^{-l}\) and maps its uniform restriction to full Haar scaled by \(3^{-l}\). Hence \(K_{a_*,t}^*m_3=p_t m_3\), where
\[
       p_t=\sum_{w\in\mathcal W_{a_*}}3^{-|w|}\omega_w^t
           =\sum_w 2^{-S_w}\omega_w^{t-1}.
\]
The original geometric law gives \(p_1<1\) and \(p_2=1\). In fact \(M_n=3^n2^{-S_n}\) under iid mass \(2^{-e}\) is a positive martingale tending to zero almost surely. Stop at its first strict crossing of one, with overshoot at most \(3/2\), or at clock \(n\); bounded convergence gives \(\sum_w2^{-S_w}\omega_w=1\). Since every overshoot is strictly greater than one, \(p_1<1\). Consequently the quadratic *ternary* transfer fixes Haar as well as the ternary projection of the finite atomic measure in (1). The binary marginal of an induced word is weighted by its own stopping code, so product odd Haar is not asserted here.

The singular mechanism can be quantified. Give letters the centered geometric law with success probability \(r=\log_3 2\), so their mean is \(a_*\). Every completed word has strict surplus \(l-rS_w>0\). The exact entropy identity is
\[
  \frac{2^{-\theta S_w}}{r^l(1-r)^{S_w-l}}
      =\left(\frac{1-r}{r}\right)^{l-rS_w}<1 .
\]
The outward first-return words are prefix-free in this outward order. Therefore \(q=\sum_w3^{-\theta |w|}\le\sum_w 2^{-\theta S_w}<1\), where the single letter \(1\) makes the inequality strict even if the centered law gives all first returns. For any \(k\) induced words the Haar mass of eligible roots is at most \((\sum_w3^{-|w|})^k\le q^k\). Thus for Haar-almost every ternary root the quadratic transfer of 1 at induced depth \(k\) is eventually zero despite its constant integral one. For every individual positive integer root it is eventually zero by strict decrease in ordinary height. Under a hypothetical \(\Xi_{a_*,2}\), (1) gives another constant integral; pointwise eventual vanishing is compatible with it because the surviving roots move to increasing ordinary heights. [Prior critical record dimension argument](../../astra-unconventional-20261126/boundary/ALL_RECORDS.md).

At general \(a\in[a_*,2)\), write \(d=H_2(1/a)\), \(q_a=\log_2(a/(a-1))\), and \(\Gamma(a,t)=3^{t-1}2^{a(d-t)}\). For \(d<t\le1\), an outward first-return word satisfies
\[
 3^{-|w|}\omega_w^t=\Gamma(a,t)^{|w|}
  (1/a)^{|w|}(1-1/a)^{S_w-|w|}2^{(q_a-t)(S_w-a|w|)}.
\]
The last factor is at most one. Here \(\Gamma(a,d)=3^{d-1}<1\), and \(\Gamma(a,t)\) is nonincreasing in \(t\) for \(a\ge a_*\). Prefix-freeness gives \(p_{a,t}\le\Gamma(a,t)<1\). The finite ordinary current thus survives inside an induced Haar-defective regime. Reinstalling all inverse words between visits creates a possibly infinite tower; in the unrestricted positive escaping component the original predecessor density already makes its physical \(1/P\)-mass infinite. These comparisons do not prove a conflicting bound on a particular high-density sibling.
