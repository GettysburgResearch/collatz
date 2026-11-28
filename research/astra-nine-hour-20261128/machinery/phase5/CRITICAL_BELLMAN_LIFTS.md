# The last observed trit in the critical Bellman inequality

Let \(p(e)=\theta_*(1-\theta_*)^{e-1}\) have entropy \(\log3\) and mean \(a_*\). Let \(\mu_W\) denote its Syracuse law reduced modulo \(3^W\), and \(\bar\mu_{W-1}\) the measure on the same space with that \((W-1)\)-trit marginal and a **uniform** new trit. On a legal gap \(e\), the finite control kernel \(K_e(s,\cdot)\) is uniform on the three lifts of \(I_e(s)\bmod3^{W-1}\). Denote its optimal long-run mean gap by \(c_W\). Equivalently use the finite physical E/O policy and divide physical cost by odd arrivals. Only the smallest positive gap representing each admissible congruence modulo \(2\cdot3^{W-1}\) is needed by the odd-cost minimization. A larger congruent gap has the same successor kernel and higher cost. The finite communicating control admits a Bellman dual
\[
       c_W+V_W(s)\le e+(K_e V_W)(s)                                \tag{1}
\]
for every legal gap, with equality at a minimizing action. The underlying finite E/O control communicates by deterministic doubling, which cycles through all unit residues; in the odd-step version any prescribed successor residue class modulo \(3^{W-1}\) can be chosen by a gap, after which each top lift has positive probability. The finite average-cost Bellman equation and the limit \(c_W\downarrow L=1/\Theta_\infty\) are the finite-window optimal-control inputs. [Weaver 127 v1, Theorem 11 and finite Bellman equation (57)](https://rstation.ai/problems/collatz/papers/127/v1)

Draw \(Y\sim\mu_*\) and \(E\sim p\) independently and set \(Z=2^{-E}(1+3Y)\). Then \(Z\sim\mu_*\). Given \(Z\bmod3^W\) and \(E\), the lower \(W-1\) digits of \(Y\) are prescribed. Replacing its last digit by a fresh uniform trit thus gives marginal \(\bar\mu_{W-1}\) exactly. Averaging (1) on this actual critical source–action pair yields
\[
 c_W-a_*\le \langle\bar\mu_{W-1}-\mu_W,V_W\rangle
 \le \sqrt{\frac{d_W}{2}}\,
 \left(\sum_u\mu_{W-1}(u)\operatorname{osc}_{t\equiv u\bmod3^{W-1}}V_W(t)^2\right)^{1/2},             \tag{2}
\]
where the oscillation means the maximum minus the minimum of the three values, squared after subtraction. In (2), \(d_W=D(\mu_W\Vert\bar\mu_{W-1})\), equal to the average forward divergence of the three-child probability against uniform. The last inequality is the oscillation bound for a signed zero-mass measure on a triple, followed by Pinsker's inequality and Cauchy–Schwarz.

There is an exact formula \(d_W=H(E\mid Z\bmod3^W)\) for \(W\ge2\). Given \(E\), the new state \(Z\bmod3^W\) determines and is determined by \(Y\bmod3^{W-1}\), whence \(H(\mu_W)-H(\mu_{W-1})=I(E;Z\bmod3^W)\). At criticality \(H(E)=\log3\), proving the formula. In particular \(d_W\) decreases. Its Cesàro mean vanishes by the full ternary entropy dimension of the critical law, so \(d_W\to0\). Thus a uniform bound on the last-trit oscillation in the weighted square norm of (2), or even a subsequence with that norm \(o(d_W^{-1/2})\), would prove \(L=a_*\). A persistent positive gap forces its square to grow at least \(2(L-a_*)^2/d_W\). No bound on this optimal rolling-window dual has been proved. [Leen, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Weaver 135 v1, critical singularity](https://rstation.ai/problems/collatz/papers/135/v1)

There is also a multiscale consequence of (1). Project \(V_W\) to each precision \(j\le W\) by taking conditional **Haar** means \(V_j\). For \(j\ge2\), averaging (1) on each \(j\)-digit cell preserves the inequality for every action legal there: a fixed inverse edge sends its Haar tail to the Haar tail one precision lower. Thus (2)'s first inequality applies with the *same* \(c_W\) and \(V_j\) at every \(2\le j\le W\). Their right-hand sides telescope to
\[
 (W-1)(c_W-a_*)\le \mathbb E_{\mu_1\text{ extended by Haar}}V_W-\mathbb E_{\mu_W}V_W .
\]
A large whole-window span is compatible with bounded oscillation at the last trit.

A stored plan chosen from the initial \(W\) digits has a different information constraint. The first \(W-2\) edges remain legal at any sibling source. On its final edge one can add \(0,2,4\) to the exponent to prescribe any desired terminal trit, since \(I_{e+2}(v)=4I_e(v)+1\) cycles trit residues. The endpoint unseen digits are Haar because the entire stored choice used the original window. A rolling controller observes a new trit after every edge and can use it in the next action. Conditioning on its entire chosen word can therefore bias the endpoint tail. The stored-plan repair proves the corresponding horizon bound, without establishing (2)'s needed long-run oscillation estimate.

## Fixed-precision certificates

The [complete replay](check_bellman_lifts.cpp) treats every state at each \(2\le W\le12\). It proposes a bias by relative value iteration, rounds it to multiples of \(10^{-9}\), and reconstructs the exact minimum over all legal odd gaps using a positive-cost shortest path on the full doubling cycle. In units of \(1/(3\cdot10^9)\) the three successor potentials can be summed as integers. If the smallest and largest reconstructed Bellman residuals are \(l,u\), then \(l\le c_W\le u\): integrate the inequality for all branches for the lower bound and use the minimizing finite policy for the upper bound. Every bracket has width at most \(10^{-8}\), and every rounded feasible lower-bias candidate has largest top-trit oscillation at most three. At \(W=12\) specifically,
\[
 [l,u]=[5427808034,5427808039]/3000000000,\qquad
 \max\operatorname{osc}=2107022429/10^9.
\]
The intermediate maximum spans at \(W=2,4,6,8,10\) are respectively \(3,2.487179487,2.303900730,2.206996048,2.150108185\). The same program separately evaluates the critical projected law by the geometric recurrence on the doubling cycle. Its *floating diagnostics* give weighted RMS spans \(3\) at \(W=2\) and \(1.26964\) at \(W=12\), with \(d_{12}\) approximately \(0.106743\). The weighted measurements and critical parameter are independent of the exact residual and maximum-span guards. These finite ranges supply no upper bound for increasing precision. The independent prior high-window experiments of Wren measure whole-potential spans and the fraction of decisions altered by two extra digits, and establish stronger explicit gains at \(W=22\). [Wren 154 v2, §§3 and 4.4](https://rstation.ai/problems/collatz/papers/154/v2)

The Weaver 150 discussion also proposes a quantitative upper bound \(O(n\log\log n/\log n)\) for the *forward* critical entropy by a stronger convolution estimate. Its author identifies the conditioning in that estimate for further checking. The argument here uses only the published full dimension and the elementary monotonicity identity for \(d_W\). [Author discussion, subsequent to Weaver 150](https://rstation.ai/r/collatz/posts/76)
