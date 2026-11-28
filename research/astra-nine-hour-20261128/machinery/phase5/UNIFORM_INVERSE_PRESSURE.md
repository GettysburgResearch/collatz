# An exact variational principle for the pressure at the worst supplied integer

For \(t>0\), \(z\in U=\mathbb Z_3^\times\), put
\[
 Z_n(z,t)=\sum_{w\text{ unit-legal at }z,\ |w|=n}e^{-tS(w)},
 \qquad S(w)=e_1+\cdots+e_n .
\]
The sum includes all positive exponents and requires the final state to remain a ternary unit. Let \(h_i\) be normalized Haar on the two unit trit classes. For a finite-window inverse policy using every legal action up to a finite cap \(r\ge6\) with strictly positive probabilities, write \(A_\pi\) for its stationary mean exponent and \(B_\pi\) for its mean conditional action entropy. Then
\[
\begin{split}
 P(t)&=\lim_n n^{-1}\log\inf_{z\in U}Z_n(z,t)
      =\lim_n n^{-1}\int\log Z_n(z,t)\,dh_i(z)\\
     &=\sup_\pi (B_\pi-tA_\pi),\qquad i=1,2.                  \tag{1}
\end{split}
\]
Every infimum can be taken on positive odd integers coprime to three, since the row is constant on unit classes modulo \(3^{n+1}\). The normalized log row also converges to \(P(t)\) in Haar probability. A signed exceptional point can have a higher pressure. The result treats the worst actual source and the two logarithmic averages, without claiming a common limit at every point.

## Proof

Each unit has a legal branch of cost at most four, and the unrestricted one-letter partition sum is \(k(t)=\sum_{e\ge1}e^{-te}=1/(e^t-1)\). Thus \(-4tn\le\log Z_n\le n\log k(t)\). Concatenation proves \(\inf Z_{m+n}\ge(\inf Z_m)(\inf Z_n)\), so the first limit exists. Write \(m_i(n)=\int\log Z_n\,dh_i\). From any initial trit \(i\), choose one exponent at most six from the first two digits routing to a prescribed trit \(j\). Its tail is Haar on that target trit. The chosen summand and the last-step upper bound give
\[
 -6t+m_j(n)\le m_i(n+1)\le m_i(n)+\log k(t).
\]
Consequently the two class means differ by at most \(6t+\log k(t)\), uniformly in depth.

Fix \(n\) and truncate all actions at a cap \(r\). There are only \(2\cdot3^n\) source cells. Increasing \(r\) approximates every cell's positive partition sum and its logarithm to any prescribed additive error \(\varepsilon\). On each initial cell sample its capped Gibbs word with probabilities proportional to \(e^{-tS(w)}\). The conditional word entropy minus \(t\) times the conditional mean total cost equals that cell's truncated log partition sum. Conditional on each initial cell and stored word, the affine inverse consumes \(n\) trits. The final state has a specified first trit and a fresh Haar tail. A stationary two-class mixture for these block transitions repeats at every boundary. Averaging the normalized word objective against that mixture gives at least \((\min_i m_i(n)-\varepsilon)/n\).

Average the state-action occupation through the stored block. This is a stationary flow for the finite kernel whose successor receives a uniform newly exposed trit. Its mean cost equals the block cost per step. Its conditional action entropy is at least the block word entropy per step: conditioning the next letter on the initial cell and previous letters already accounts for the stored plan, while newly exposed digits remain independent of it. The entropy chain rule and concavity under the average over block positions give the inequality. Mix stationary flows with a strictly positive reference flow before normalizing rows. At this fixed finite cap and precision the action entropy is continuous and the cost linear, so the positive finite policy achieves the preceding objective up to any further prescribed error. These constructions and their Haar-transition justification are spelled out in the earlier transfer proof. [Stationary block occupation argument](../phase4/TILTED_ENTROPY_TRANSFER.md)

Conversely, for any such positive policy and **each actual supplied starting state**, the Gibbs inequality gives
\[
 \log Z_N(z,t)\ge H_\pi(w\mid z)-t\,\mathbb E_\pi[S(w)\mid z].
\]
Both right-hand terms are Cesàro sums of continuous one-step functions under the actual policy on \(U\). Weaver 127, Theorem 5 gives convergence divided by \(N\) to \(B_\pi-tA_\pi\), uniformly in \(z\). Therefore \(P(t)\ge\sup_\pi(B_\pi-tA_\pi)\ge\limsup_n m_i(n)/n\). Since the infimum is at most either mean, (1) follows. Under either Haar class the nonnegative difference between the actual log row and its minimum, divided by \(n\), has expectation tending to zero. This gives the asserted convergence in probability. [Weaver 127 v1, Theorems 5, 6 and 11](https://rstation.ai/problems/collatz/papers/127/v1)

## Exact reverse-entropy rate and the critical endpoint

For \(\theta=1-e^{-t}\), let \(\mu_\theta\) be the iid geometric Syracuse law, and let \(h\) be normalized unit Haar. Each contributing word has probability \((e^t-1)^n e^{-tS(w)}\). Its remaining trit mass belongs to a fixed pair of positive numbers depending only on \(\theta\). Therefore, uniformly in the source,
\[
 \frac{\mu_{\theta,n+1}(z)}{h_{n+1}(z)}
    \asymp_\theta [3(e^t-1)]^n Z_n(z,t).
\]
It follows that the normalized reverse relative entropy always has a limit, and that the worst unit cylinder has the identical exponential rate:
\[
\boxed{\ \Lambda(t)=\lim_n\frac1n D(h_{n+1}\Vert\mu_{\theta,n+1})
=\lim_n\frac{-1}{n}\log\inf_z\frac{\mu_{\theta,n+1}(z)}{h_{n+1}(z)}
=P_0(t)-P(t),\quad P_0(t)=-\log[3(e^t-1)].\ }                    \tag{2}
\]
In particular \(P\le P_0\). The function \(P\) is convex by (1). On the certified tilt interval the original-source exact row theorem implies equality: at mean \(a=1/\theta\) keep one exact total to obtain \(P(t)\ge H_\theta-\log3-ta=P_0(t)\). This includes each endpoint certified by the reserve argument. [Exact row transfer](../phase4/TILTED_ENTROPY_TRANSFER.md) · [Extended tilt interval](../phase4/EXTENDED_TILTED_INTERVAL.md)

For all finite policies,
\[
 B_\pi\le H_{1/A_\pi}-\log3.                                       \tag{3}
\]
Indeed start at its stationary locally Haar law. A stationary W-digit state, the chosen letter, and the fresh successor trit have joint entropy \(H(Z_W)+B_\pi+\log3\). The letter and the new W-digit state determine the old state from \(A_e(x)=(1+3x)/2^e\bmod 3^W\), and conversely contain the one disclosed lift. Stationarity therefore gives \(B_\pi+\log3=H(E\mid Z'_W)\le H(E)\le H_{1/A_\pi}\). The final inequality is the maximum entropy of positive integer laws at prescribed mean. This finite-state identity is an input also used by Weaver 150. Since every \(A_\pi\ge L=1/\Theta_\infty\) and positive policies approximate \(L\), (1) and (3) imply \(\lim_{t\to\infty}-P(t)/t=L\): for sufficiently large \(t\), \(H_{1/A}-tA\) decreases on \([L,\infty)\), and \(-tL\le P(t)\le H_{1/L}-\log3-tL\). [Weaver 150 v2, §5 and reverse-entropy construction question in §7](https://rstation.ai/problems/collatz/papers/150/v2)

At \(t_*=-\log(1-\theta_*)\), \(H_{\theta_*}=\log3\), \(a_*=1/\theta_*\), the following statements are equivalent:
\[
 L=a_*,\qquad \Lambda(t_*)=0,\qquad
 P(t)=-ta_*\ \text{for every }t\ge t_*.
\]
For the second equivalence start with \(L=a_*\). The entropy derivative at mean \(a_*\) is \(\log(a_*/(a_*-1))=t_*\), so (3) gives \(B_\pi-tA_\pi\le-ta_*\) for all \(t\ge t_*\). Policies approaching \(a_*\) and nonnegative choice entropy give the opposite inequality. Conversely evaluate the line at \(t_*\), where \(P_0(t_*)=-t_*a_*\), and apply the original-source reverse-entropy criterion. For \(t>t_*\) the iid mean \(1/\theta<a_*\le L\). The critical criterion's Chernoff argument, with the geometric parameter replaced by \(\theta\), gives \(\Lambda(t)\ge I_\theta(L)>0\). Thus the analytic function \(P_0\) agrees with \(P\) on an open certified interval and differs throughout \((t_*,\infty)\). Some failure of real analyticity of \(P\) between these ranges follows from the identity theorem. Neither its location nor equality at the critical endpoint is determined here. [Critical original-source comparison](../phase4/CRITICAL_REVERSE_ENTROPY.md)
