# Exceptional dyadic multipliers and a prescribed time of Brownian separation

Let \(x\) be Haar in \(\mathbb Z_2\), let \(\alpha\) be a fixed odd dyadic unit, and write \(g_k(y)\) for the count of odd departures of the shortcut map through time \(k\). At every positive integer scale \(t\) observe the linearly interpolated centered grade pair
\[
       Z_t(\alpha,x)(k/t)=t^{-1/2}\bigl(g_k(x)-k/2,\ g_k(\alpha x)-k/2\bigr).
\]
Write \(\mathcal L_t(\alpha)\) for its law in \(C([0,1])^2\). Define \(\mathcal B_{\theta,\delta}\), for real \(\theta\) and \(0\le\delta\le1\), as follows. Start coalescing Brownian motions of variance rate \(1/4\) at \(0,\theta\), subtract \(\theta\) from the second coordinate, and observe these two paths through time \(\delta\). After \(\delta\) attach two independent variance-\(1/4\) Brownian increments to their respective current positions, independently of the past. For \(\delta=0\) this is the two-independent-motion law. For \(\theta=0\) the first segment consists of two copies of a single motion.

**Proposed theorem.** The odd dyadic units for which \(\mathcal L_t(\alpha)\) fails to converge to the two-independent-motion law form a set of ordinary dyadic Hausdorff dimension zero. Nevertheless, on a comeager subset of the open-and-closed subgroup \(H=\overline{\langle3\rangle}\) every \(\mathcal B_{\theta,\delta}\) is a subsequential law. In particular normalized paths can stay together for a prescribed positive time and then separate. This describes contact in a path limit. An equality of two actual shortcut states persists forever.

There is an ordinary integer version. Fix \(\theta,\delta\). For each large \(t\) one can choose an integer \(c_t>1\) prime to six with \(c_t\le3\cdot2^t\) such that on **every** interval of \(N\) consecutive positive integers with \(t=\lfloor\log_2N\rfloor\), the actual log-height change pair
\[
 \frac1{\gamma\sqrt t}
 \left(\log_2 T^k x-\log_2 x+bk,\
       \log_2 T^k(c_t x)-\log_2(c_t x)+bk\right)
\]
has limit \(\mathcal B_{\theta,\delta}\). Here \(\gamma=\log_23,\ b=1-\gamma/2\), and \(x\) is uniform on the interval. The same construction admits a different positive representative \(4^t<c_t\le4^t+3\cdot2^t\) for which the two actual numerical states remain distinct at **all** dates through \(t\) for **every** positive integer \(x\). Each observed trajectory is centered at its own initial log height. The parameter \(\theta\) describes a dyadic approximation by three-powers.

## The dimension-zero upper bound

Use the stationary classification and one-dimensional local-time estimate in the [independent multiplier proof](INDEPENDENT_MULTIPLIER_PATHS.md). Outside \(H\) the compact kernel has only product Haar as a stationary law, so the joint normalized cross bracket vanishes and the limit is independent. Inside \(H\), omit the countable set of actual three-powers, and write \(e(h)=v_2(\alpha3^h-1)\) for \(h\in\mathbb Z\). We claim that \(e(h)=o(|h|)\) as \(|h|\to\infty\) suffices for the independent limit. Here the initial state has ordinary level zero and offset zero.

For a fixed \(r\ge1\), partition the ordinary levels into intervals of length \(L=\lceil\sqrt t\rceil\) as in the [moving-multiplier bound](MOVING_MULTIPLIER_PATHS.md). In the block at distance \(jL+O(L)\), \(\max e(h)\le C_\epsilon+\epsilon(j+2)L\) for each fixed \(\epsilon>0\). At every precision the levels near the absorbing point form one residue class. Their expected native proportion through time \(t\), with the precision fixed at \(r\), is thus at most
\[
 C(r+1)2^{-r}+\frac{C}{L}\sum_{j\ge0}e^{-cj^2}
                     \{r+C_\epsilon+\epsilon(j+2)L\}.
\]
This uses the conditional expected holding bound \(e(h)+2\) at each embedded simple-walk visit. Take first \(t\to\infty\), then \(\epsilon\downarrow0\), then \(r\to\infty\). No occupation-limit mass can remain at the absorbing point. The only possible limit is product Haar, and the bracket argument yields independent motions. In particular the exceptional parameters, apart from the countable powers, lie in
\[
 \bigcup_{m=1}^\infty\limsup_{|h|\to\infty}
       \{\,\alpha:\ |\alpha-3^{-h}|_2\le 2^{-|h|/m}\,\}.
\]
For every \(d>0\) the sum of the \(d\)-th powers of these diameters over \(h\) converges at each fixed \(m\). The Hausdorff dimension claim follows.

## A finite residue with the prescribed change of law

Fix a nonempty open cylinder of parameters in \(H\). For each sufficiently large \(t\), choose an ordinary integer \(h=h_t\) with \(h/\sqrt t\to\theta\) and \(3^h\) in the cylinder. This is possible since the allowable exponents contain one fixed ordinary arithmetic progression. Choose \(1\le L=L_t\le t\) with \(L/t\to\delta\) and \(L\) eventually at least the cylinder precision. For \(\delta=0\) one can take \(L=\lceil\sqrt t\rceil\). Randomize the coefficient by
\[
                         \alpha=3^h+2^L K,
                  \qquad K\text{ Haar in }\mathbb Z_2
\]
independently of \(x\). For \(v=v_2(x)<\infty\), write \(x=2^v x'\) with \(x'\) odd. Both arms first take \(v\) even steps. Their comparison with \(x,3^h x\) agrees exactly at every departure through date \(v+L-1\). At the end of the \(L\)-letter word of \(3^h x'\), of grade \(g\), the second state is
\[
                     T^L(3^h x')+3^g K x'.
\]
Conditional on the **whole** \(x\), this state is fresh Haar since \(3^gx'\) is an odd unit. Its successive parity bits are independent and fair; this uses the exact bijection between a word and a binary residue. Thus, conditional on \(x\), the products of its subsequent parity signs with the now deterministic first-arm signs are independent centered signs.

Write \(J_k\) for the sum through dates \(L,\ldots,k-1\) of the signs \(+1\) for parity agreement and \(-1\) for disagreement. The at most \(v\) intervening signs before \(v+L\) cost at most \(v\). The elementary \(L^2\) maximal martingale inequality on the remaining signs gives
\[
       \mathbb E_{K,x}\max_{L\le k\le t}|J_k|
                      \le \mathbb E v+2\sqrt t=1+2\sqrt t.                \tag{1}
\]
All the terms through this deadline depend only on \(\alpha\bmod2^t\). Consequently one residue in the cylinder \(\alpha\equiv3^h\bmod2^L\) has \(\mathbb E_x\max|J_k|\le1+2\sqrt t\). Choose it deterministically. This selection bounds the absolute post-\(L\) cross bracket for that one fixed residue, since the predictable one-step grade covariance is its agreement sign divided by four.

Through \(L\) the quenched path pair is exactly that for \(x,3^h x\). The [critical coalescing pair law](COALESCING_ORDINARY_HEIGHTS.md), in its Haar phase with zero offsets, gives \(\mathcal B_{\theta,1}\) up to this date. For \(h<0\) use \(3^h x\) as the Haar first arm, impose the positive gap \(-h\) on the original first arm, then exchange the labels and recenter. If \(h=o(\sqrt t)\) the subcritical first-return bound gives the same Brownian path on both arms. The two grade martingales are tight for each fixed coefficient. For the selected residue (1) makes the cross-bracket increment after \(L\), divided by \(t\), uniformly \(o_{\mathbb P}(1)\). Their diagonal brackets increment at constant rate \(1/4\). Every limit after time \(\delta\), conditional on its joint past, therefore appends a two-dimensional Brownian motion with independent coordinates. Indeed bounded-increment martingale convergence gives the martingale and bracket identities in the natural limiting filtration; Lévy's characterization applied at deterministic \(\delta\) gives independence of the preceding sigma field. This identifies the whole limiting pair as \(\mathcal B_{\theta,\delta}\).

## Category and ordinary realization

At fixed \(t\), the whole path law is constant on each parameter cylinder modulo \(2^t\). Choose any metric inducing weak convergence of path laws. For fixed rational \((\theta,\delta)\), tolerance \(1/j\) and lower time cutoff \(j\), the union of those cylinders whose laws are within \(1/j\) of \(\mathcal B_{\theta,\delta}\) at some \(t\ge j\) is open. The preceding construction in an arbitrary initial cylinder proves it dense in \(H\). Intersect over this countable family. Continuity of the Brownian laws in both parameters gives all real \((\theta,\delta)\) by diagonalization. For this continuity take two independent Brownian drivers and switch the second driver to the first at their first collision through \(\delta\). The first-passage time to a prescribed level is almost surely continuous under deterministic starting-level perturbations, by immediate two-sided crossing after the first hit, and tends to zero as a nonzero initial gap tends to zero. With the same fresh post-\(\delta\) drivers, uniform continuity of Brownian paths gives the claimed convergence. A deterministic positive \(\delta\) has no atom for a nonzero-gap first-passage time. Since \(\mathcal B_{0,1}\) and the independent law differ, every parameter in this comeager set is exceptional.

For the ordinary statement take the selected odd residue and one positive representative \(c_t>1\) prime to three, up to \(3\cdot2^t\). If desired instead use a representative strictly between \(4^t\) and \(4^t+3\cdot2^t\), still prime to six. The same choice works for all interval placements. The grade comparison transfers from Haar to the integer interval by shortening at \(t-\lceil2\log_2(t+2)\rceil\); full words and grade paths depend only on that source residue, and the omitted part of a centered path costs \(O(\log t/\sqrt t)\). For positive \(y=x\) and \(y=c_tx\), the exact correction identity reads
\[
 \log_2T^k y-\log_2y+bk
       =\gamma(g_k(y)-k/2)+\log_2(1+A_k(y)/y),\qquad
 A_k(y)=\sum_{u<k,\ e_u=1}2^u3^{-g_{u+1}(y)} .
\]
The marginal parity sequences under Haar are fair. Except on a set of exponentially small relative size in any integer interval, both have at least \(t/8\) odd bits by date \(\lfloor t/2\rfloor\). Hence \(A_k\le t2^{t/2}+t2^t3^{-t/8}\) throughout. Uniformly in interval placements one has \(x\ge2^{(1-\epsilon)t}\) except with probability \(O(2^{-\epsilon t})\); choose \(0<\epsilon<(\log_23)/8\). Since \(c_tx\ge x\), both logarithmic corrections are then \(o(1)\). This proves the own-source-centered real limit. With \(c_t>4^t\), the elementary bounds \(T^k(c_tx)\ge c_tx/2^k\) and \(T^k x\le2^kx\) exclude numerical equality at every \(k\le t\). The construction allows growing integer multipliers and gives a strict scope limit to the [sub-square-root-height independent law](MOVING_MULTIPLIER_PATHS.md).
