# A single finite ternary rule predicts every low-entropy ordinary inverse word

**Proposed theorem, conditional on O15's stationary inverse entropy dichotomy.** Let $D$ be a finite alphabet of positive Syracuse exponents and let $S\subset D^{\mathbb Z}$ be a nonempty closed shift-invariant set. Suppose its topological entropy $h(S)$ is strictly below $\log3$. For every $\epsilon>0$ there exist integers $h,N\ge1$ and a single function
$$g:\mathbb Z/3^h\mathbb Z\longrightarrow D$$
with the following property. For every $n\ge N$, each positive odd endpoint $a_0$, and every word $e_0,\ldots,e_{n-1}$ of $S$ which can be followed backwards from $a_0$, put $a_{j+1}=(2^{e_j}a_j-1)/3$. Then
$$
 \#\{0\le j<n:e_j\ne g(a_j\bmod 3^h)\}<\epsilon n.
$$
The rule is uniform over ordinary endpoints, words, and horizons. For an arbitrary closed subshift the proof gives existence without an effective depth or onset. In particular this applies for each fixed $C\ge0$ to all exponent words satisfying $\sum_{j=t}^{t+\ell-1}e_j\le\ell\log_2 3+C$ on every internal interval, by O18's composition count and extension by ones.

## Measures on the projected subshift

For $\mathbf e\in S$ let $X_j=\pi(\sigma^j\mathbf e)$ be the point of $\mathbb Z_3$ encoded by the contractions $G_e(y)=(3y+1)/2^e$ applied in the order $e_j,e_{j+1},\dots$. Its $k$ lowest ternary digits are determined by $e_j,\dots,e_{j+k-1}$. Thus the compact projected set $K=\pi(S)$ meets at most $|\mathcal L_k(S)|$ different depth-$k$ cylinders.

Take any invariant probability $\nu$ on $S$, possibly nonergodic. Let $\eta$ be its joint law of $(X_0,E_0)$, $\mu$ the first marginal, and $q(x)$ the conditional letter probabilities. The legal inverse edge maps preserve the required endpoint marginal under $\eta$ by stationarity. Construct the stationary Markov inverse process with marginal $\mu$ and transition kernel $q$. This operation preserves the single-edge law. The Markov process may give positive probability to words outside $S$. Its state marginal remains concentrated on $K$.

Disintegrate this Markov process into stationary ergodic components. Almost every component is concentrated on $K$ at the present state and uses the same $q$ at almost all its states. For the latter assertion the invariant field is contained in the completed past including the present state, so conditional transition residuals continue to integrate to zero after conditioning on that field. Since $D$ is finite, each component has integrable exponents. For each such component every depth-$k$ state entropy is at most $\log|\mathcal L_k(S)|$. Hence its upper state entropy per depth is at most $h(S)<\log3$. The dichotomy of O15 for an ergodic Markov inverse process gives $\int H(q(x))\,d\mu_{\rm comp}(x)=0$. Integrating the components yields
$$H_\nu(E_0\mid X_0)=0. \tag{1}$$
The conditioning in (1) uses only the ternary coordinate. Besides the compact projection and the Markov dichotomy, the argument uses no entropy formula for the non-Markov path. In particular it does not assert that the Markovized process lies in $S$.

## One rule for all invariant measures

Write $\mathcal M$ for the compact convex set of invariant Borel probabilities on $S$. For $h\ge1$, $f_h(\nu)=H_\nu(E_0\mid X_0[h])$ is continuous on $\mathcal M$: both finite partitions are clopen. These functions decrease pointwise to zero by (1) and martingale convergence. Dini's theorem gives $\sup_{\nu\in\mathcal M} f_h(\nu)\to0$.

Choose $h$ so that this supremum is below $\epsilon/8$. Let a randomized predictor $P$ assign to every $h$-digit ternary cell a probability vector on $D$, and measure loss by $L(\nu,P)=\mathbb E_\nu[1-P_{X_0[h]}(E_0)]$. For fixed $\nu$ its minimum is the average of $1-\max p_e$ for the cell posteriors. For probability vectors this is bounded by their entropy, since $1-\max p_e\le-\log\max p_e\le H(p)$. Thus each invariant law has optimal loss below $\epsilon/8$.

The set of randomized predictors is a finite-dimensional compact convex polytope; $L$ is continuous affine in each argument on the two compact convex sets. The minimax theorem gives one $P$ with $\sup_{\nu\in\mathcal M} L(\nu,P)\le\epsilon/8$. Choose $g$ as a maximizer of $P$ on each cell, with any fixed method for ties. If $g(b)\ne e$ then $P_b(e)\le1/2$. The deterministic mistake indicator therefore never exceeds $2(1-P_b(e))$. The resulting deterministic rule has worst invariant loss at most $\epsilon/4$.

## Transfer to every finite ordinary word

The indicator $F(\mathbf e)=1_{e_0\ne g(X_0[h])}$ is continuous. Uniformly over $\mathbf e\in S$, the limsup of its length-$n$ empirical averages is at most $\sup_{\nu\in\mathcal M}\int F\,d\nu$: otherwise choose high-average orbit segments and take a weak limit of their empirical probability measures. Such a limit stays in $S$, is invariant by telescoping, and has the limiting average by continuity. Hence all sufficiently long segments have average at most $\epsilon/2$.

Extend the prescribed legal ordinary word to any element of $S$. Through $j\le n-h$, the next $h$ exponents determine the same $h$-digit cylinder for $a_j$ and the coded $X_j$. The remaining fewer than $h$ guesses cost at most $h$ mistakes. Taking $N$ sufficiently large gives the claimed strict bound. This step handles ordinary endpoints that have no exact coding in $S$ beyond the prescribed finite word.

The theorem bounds the proportion of exceptions in every such word. A particular positive integer orbit could follow all, or almost all, of the predicted exponents. The theorem therefore supplies no first descent or first mismatch for that orbit.
