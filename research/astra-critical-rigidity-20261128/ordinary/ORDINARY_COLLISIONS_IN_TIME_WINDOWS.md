# What intersections of ordinary trajectories reveal about all positive components

**Proposed, source-qualified written result.** Fix \(k\ge2\), and sample \(n_1,\ldots,n_k\) independently and uniformly among positive integers through \(X\). Use the genuine shortcut map. Set \(s_X=\sigma\sqrt{\log X}\),
\[
 H=\lfloor\mu\log X+u s_X\rfloor,\qquad
 \mu=2/\log(4/3),\quad \sigma^2=2(\log3)^2/\log^3(4/3),
\]
where \(u\) is fixed. A component consists of all starts whose forward orbits meet. Let \(d_C\) denote its positive-integer natural density, \(P_C\) its least shortcut period when it is periodic, and write
\[
       S_k^{\rm cyc}=\sum_{C\ {\rm periodic}}d_C^k,\qquad
       S_k^{\rm div}=\sum_{C\ {\rm divergent}}d_C^k .
\]
These sums concern components of the genuine map, regardless of the truth of Collatz.

For integer \(b_X\to\infty\) with \(b_X/s_X\to w\in[0,\infty]\), put
\(J_X=[\max(0,H-b_X),H]\cap\mathbb Z\).
The probability that the \(k\) trace sets \(\{T^j n_i:j\in J_X\}\) have a common integer tends to
\[
        \Phi(u)^k S_k^{\rm cyc}+
          \Pr(\max_i Z_i\le u,\ \max_i Z_i-\min_i Z_i\le w)\,S_k^{\rm div},
                                                                         \tag{1}
\]
where the \(Z_i\) are independent standard normals. Each arm can visit the common value at its own date.

In particular, compute two events on the same finite data: all complete traces through \(H\) have a common integer, and their last \(1+\lfloor(\log X)^{1/4}\rfloor\) observations have none. The probability of their conjunction tends to \(\Phi(u)^k S_k^{\rm div}\). For two samples at \(u=0\) the limit is one quarter of the sum of squared divergent basin densities. Mazur's positivity input makes a zero limit equivalent to the absence of divergent positive trajectories. This test involves no prescribed high shell, moving orbit representative, minimum date or search past \(H\).

A second set of finite tests recovers the periods. For a fixed integer \(t\ge1\), ask whether the single value \(T^Hn_1\) occurs among the last \(t\) values through \(H\) on **each** of the other arms. Divide its limiting probability by \(\Phi(u)^k\), and call the result \(b_k(t)\), with \(b_k(0)=0\). Then
\[
                  b_k(t)=\sum_{C\ {\rm periodic}}
                       d_C^k \min(1,t/P_C)^{k-1}.                       \tag{2}
\]
Varying \(k,t\) therefore identifies the multiset of basin densities at each period, and (1) separately identifies the multiset of divergent basin densities. Identifying a mass spectrum by a limit involves no effective convergence rate or finite proof of its zero entries.

## A common value and the individual minimum dates

Write \(m_i\) for each true global minimum and \(\tau_i\) for its first attainment. The proper minimum law \((p_r)\) exists, sums to one, and for each fixed \(r\) the joint limit of \(m_i=r\) and \((\tau_i-\mu\log X)/s_X\) is \(p_r\) times the standard normal law. For periodic \(C\) and each of its \(P_C\) phase classes, the mass in that phase which has actually entered the cycle by \(H\) tends to \(d_C\Phi(u)/P_C\); the resulting vertex at \(H\) is a common phase permutation. These source-qualified inputs and the original sources appear in the [ordinary synchronous phase proof](SYNCHRONOUS_PHASE_DISPERSION.md). The uniform all-height estimate supplies a further fact: with probability \(1-o(1)\) no common vertex at a height at least \(R\) is visited by any one arm on or before its minimum, as \(X,R\to\infty\) independently. Indeed condition on any other arm's **entire** orbit. Its high states form a legal mask, uniformly over that orbit, then sum the \(k\) bounds. The inequality is valid regardless of deadlines, and the same conclusion in the iterated limit \(R\to\infty\) after \(\limsup_{X\to\infty}\) follows from uniform joint convergence. [All high targets](../literature/ALL_HIGH_TARGETS.md) · [Leen, original proper minimum law, physical clock and uniform interval sparsity](https://doi.org/10.5281/zenodo.23269488) · [Mazur, positivity of fixed-target predecessor densities](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)

Retain a finite collection \(\mathcal M\) of possible minima with mass at least \(1-\epsilon\). The loss on \(k\) arms is at most \(k\epsilon+o(1)\). Distinct components have disjoint traces. In any represented periodic component, the retained minima enter its cycle within a bounded number of steps after their minimum dates. For a represented divergent component, choose a common vertex \(v\) on the forward tails of all its retained minima. Their actual arrivals from \(r\in\mathcal M\cap C\) take fixed times \(\ell_r\). Write \(a_i=\tau_i+\ell_{m_i}\) for these particular arrivals. The future of \(v\) is injective. Choose \(R\) larger than all the finite prefix heights from the retained minima to their cycle or to their chosen \(v\).

A witness in any finite observation windows has the following consequences with an error whose limiting probability can be made arbitrarily small by increasing \(R\).

* If the witness is at height at least \(R\), with the stated probability all its witnessing dates are after the respective minima. In a represented divergent component the dates must therefore be \(a_i+j\) with **one common** \(j\ge0\), since all high vertices there lie on the chosen injective tail. The bounded forward orbits of the retained minima in represented periodic components can be absorbed below \(R\).
* At a witness below \(R\), every arm observed before its minimum is at most \(K_R=\max_{1\le y<R}\tau(y)\) dates before it: the minimum of its remaining trajectory is the same minimum and has not yet occurred. For a represented divergent component, an arm observed after its minimum is at most a further constant \(K_{R,\mathcal M}\) dates after it, since each of those finitely many injective tails visits the finite interval only at finitely many dates. A periodic arm already past its minimum only needs the inequality \(\tau_i\le H\).

Consequently common values in the terminal window require \(\max\tau_i\le H+O_{R,\mathcal M}(1)\). On divergent components they further require \(\max\tau_i-\min\tau_i\le b_X+O_{R,\mathcal M}(1)\). For the low case this follows from the bounded offsets from every observing date; for the high case it follows from the common \(j\).

Conversely, on a represented periodic component with all minimum dates at most \(H-C_\mathcal M\), choose \(C_\mathcal M\) larger than all the relevant cycle-entry delays plus their periods. For large \(X\), the terminal windows then include at least one full lap on every arm. On a represented divergent component, the two exact inequalities \(\max a_i\le H\) and \(\max a_i-\min a_i\le b_X\) suffice. Indeed \(j=H-\max a_i\ge0\) gives all \(a_i+j\in J_X\) and thus the same actual vertex \(T^jv\).

On any fixed retained tuple, the normalized minimum dates converge jointly to independent normals, with tuple mass \(\prod p_{r_i}\). Their maximum and range have no atoms (including range zero since \(k\ge2\)); for \(w=\infty\) only the maximum restriction remains, by tightness. The bounded offsets vanish on division by \(s_X\). Applying the preceding bounds at fixed \(R,\mathcal M\), then increasing \(R\) and releasing \(\mathcal M\), gives (1) since \(d_C=\sum_{r\in C}p_r\). Taking \(b_X=H\) gives the complete traces; taking \(b_X=\lfloor(\log X)^{1/4}\rfloor\) gives the sub-Gaussian-scale windows. Their events are nested, so their probability difference is exactly the conjunction in the statement.

## Recovering the periodic spectrum from finite lags

For fixed \(t\), an anchored hit as in (2) is contained in the intersection event with the fixed span \(t-1\). In divergent components the same upper calculation requires the range of minimum dates to be \(O_{t,R,\mathcal M}(1)\); after normalization the limiting probability is zero. In a finite collection of periodic components the contribution from sources that have not entered by \(H-t\) is negligible on the anchored event: the upper calculation forces all \(\tau_i\le H+O_{R,\mathcal M}(1)\), while the retained entry delays are bounded, and the minimum clock has a continuous normalized limit. Once all sampled arms are on the same cycle throughout the \(t\) dates, their terminal phases are independently asymptotically uniform there with activated mass \(d_C\Phi(u)\) on each arm. The anchored vertex is among the other arm's observations for exactly \(\min(t,P_C)\) terminal phases. Multiplication, and then release of the finite truncation as in (1), yields (2).

Define
\[
 D_k(t)=\frac{b_k(t)-b_k(t-1)}{t^{k-1}-(t-1)^{k-1}} .
\]
In (2) a component contributes \(d_C^k/P_C^{k-1}\) to this difference quotient if \(P_C\ge t\), and zero otherwise. Hence
\[
                \sum_{P_C=t}d_C^k
                        = t^{k-1}\big(D_k(t)-D_k(t+1)\big).
\]
For each period these power sums for \(k\ge2\) recover the positive masses with multiplicity by successive largest-mass extraction. The same extraction on \(S_k^{\rm div}\) is detailed in [the finite high-trace formula](FINITE_HIGH_ORBIT_INTERSECTIONS.md). All estimators above use finitely many unmarked positive-integer trajectories at each \(X\).
