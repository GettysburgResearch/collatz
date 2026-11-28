# The physical size of the boundary conductor

**Proposed written identity and source-qualified obstruction.** A chronological cut cannot reduce the conductor of the normalized colored Apéry boundary. The complete conductor measures the physical maximum-to-minimum ratio to within the total logarithmic correction. In particular the known occupation of large physical heights forces any hypothetical sequence of distinct positive integer cycles out of the small-conductor regime in the [selected-root theorem](COLORED_SELECTED_ROOT.md).

Use the displayed shortcut period $n=gN$, weight $u=gU$ and $U_i=\sum_{j<i}b_j$. Define $H_i=Ui-NU_i$ for $0\le i<n$ and $R=\max_i H_i-\min_i H_i$. Let $c$ be one plus the greatest hole height, or zero if the colored semimodule has no holes. Then exactly
$$ c=\max(0,R-N+1).                                                     \tag{1}$$
Every clock point begins its own $Y$-ray at normalized height $H_i-\min H$, and the preceding point of the same ray is absent and has height $H_i-\min H-N$. These are the last potential holes on the rays, with negative heights outside the half-cylinder. Taking the maximum proves (1). Changing the initial clock cyclically permutes the heights after a common translation, preserving $R$ and $c$. Changing the Bezout pair only relabels the colors in a height-dependent manner and leaves (1) intact.

Let $x_i>0$ be the closed rational physical values with this word, and write $p=\log_3 2$,
$$ \delta=np-u=\sum_{i:b_i=1}\log_3(1+1/(3x_i)),\qquad
 E_i=\sum_{0\le j<i:b_j=1}\log_3(1+1/(3x_j)). $$
The product of the exact steps gives
$$ H_i/N = -\log_3(x_i/x_0)+E_i-i\delta/n. $$
For $i<j$, both $E_j-E_i$ and $(j-i)\delta/n$ lie in $[0,\delta]$. Hence the oscillation of $E_i-i\delta/n$ across the full period is at most $\delta$, giving
$$ \left|\,R/N-\log_3(\max x_i/\min x_i)\,\right|\le\delta.            \tag{2}$$
These two statements apply at every positive physical circle without an ordinary integrality premise.

For completeness, $\delta\to0$ along any sequence of distinct positive integer cycles. The following elementary sparsity proof is given in Weaver's paper 210, §7. Denote by $F(X)$ the number of states at most $X$ on one least-period integer cycle and put $L=\lfloor\log_2 X\rfloor$. If a starting integer at most $X$ has at most $3L/5$ odd bits in the next $L$ steps, its final state is at most $(3^{3/5}/2)^LX+(3/2)^L-1\le X/2$ for all sufficiently large $X$. The additive bound follows by replacing every step with the odd affine map. Images of distinct cycle starts are distinct. Every remaining parity word selects a single residue class modulo $2^L$, hence at most two starts in the indicated range. There are at most $2^{L\kappa}$ such words where $\kappa=H_2(3/5)<1$: assign independent bits with probability $3/5$ for a one, so each upper-tail word has probability at least $2^{-L\kappa}$. Therefore $F(X)\le F(X/2)+2X^\kappa$ eventually with absolute constants, giving $F(X)=O(X^\kappa)$ uniformly over cycles. A dyadic sum of reciprocals above the cycle minimum $M$ now gives $\delta=O(M^{\kappa-1})$. Along distinct cycles the minimum tends to infinity, since disjoint deterministic cycles cannot share an integer. This proves the asserted convergence. [Weaver, paper 210/v1, §7](https://rstation.ai/problems/collatz/papers/210/v1)

Weaver's physical occupation theorem gives, for every fixed $K<K_*=3.849030770060326\ldots$, a positive fraction of shortcut departures above $KM$ in every sufficiently high ordinary cycle. We use the consequence $\max x_i>KM$ and the same shortcut convention. Its asymptotic threshold uses external Diophantine input. Applying (1)–(2) and sending $K\uparrow K_*$ gives the necessary condition
$$        \liminf \frac cN\ge \log_3(K_*/3)>0.                        \tag{3}$$
Consequently any proof that integrality forces $c\log(2+gc)=o(N)$ on all those words would already contradict an existing necessary property of any infinite sequence of such cycles. The identity alone leaves an isolated cycle possible. [Weaver, paper 181/v1, asymptotic occupation theorem](https://rstation.ai/problems/collatz/papers/181/v1)

The [finite arithmetic controls](colored_selected_controls.py) check (1) on every noncoprime necklace through length fifteen and both sides of (2) on all 1,918 positive examples, using integer powers and original raw numerator ratios. Numerically $\log_3(K_*/3)=0.2268398801\ldots$.
