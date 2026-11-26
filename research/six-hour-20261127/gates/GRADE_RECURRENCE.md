# A recurrent reversible walk on the support of an escaping ordinary component

**Status.** Written, source-qualified for the Collatz application. The random walk below uses the actual native edges in a hypothetical escaping component. Its exact heat-kernel asymptotic shows why recurrence of a natural reversible chain cannot rule out deterministic escape. It also identifies the invariant measure and its total mass.

## The conserved measure

On an ordinary escaping component \(C\), write \(d_v\) for the natural density of the ordinary predecessor set of \(v\), including even starts. Fix an actual native ray \(a_n=T^n a_0\) and define the signed grade by \(g(v)=n-k\) whenever \(T^k v=a_n\). The absence of cycles makes it well defined. The fixed-target and forward-component results used in [the annular current](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/trace/ANNULAR_ESCAPE_CURRENT.md) give
\[
 d_v=\sum_{Tu=v}d_u,\qquad d_{a_n}\longrightarrow m_C>0 .
\]
The first equality uses disjoint ordinary predecessor basins at a nonperiodic point. The second is the source-qualified ordinary component density, not an assumed invariant law on a compact completion. These are the only nonlocal inputs here. Zero-density vertices are discarded. On the positive support, \(T\) preserves the sigma-finite counting weight \(\pi(\{v\})=d_v\). Its total on **each** integer grade equals \(m_C\). Indeed for \(n\ge\max(0,h)\), iterate the displayed finite-fiber conservation law over \(T^{n-h}u=a_n\). These finite sets increase with \(n\) and exhaust grade \(h\). Sending \(n\) to infinity gives the claim. In particular \(\pi(C)=\infty\). The positive support is connected, since every positive vertex has positive forward orbit and these orbits merge.

For \(0<p<1\) define a chain \(P_p\) on this support. With probability \(p\) follow the deterministic forward edge from \(v\) to \(Tv\). Otherwise choose a predecessor \(u\) with probability \(d_u/d_v\). Both direction kernels separately preserve \(\pi\). The backward choice is a probability by the conserved flow. In addition \(P_p\) is reversible for the measure with masses \(d_v(p/(1-p))^{g(v)}\), by detailed balance on each edge. It has no invariant probability on this irreducible component, since an invariant probability would project under \(g\) to an invariant probability for the nearest-neighbor walk on all of \(\mathbb Z\). Such a probability is impossible, for example by the elementary stationary second-order difference equation. The two asserted sigma-finite measures need not coincide.

## Exact reduction along every finite sequence of directions

Given a sequence of directions, write \(S_j\) for its signed walk with increments \(+1\) forwards and \(-1\) backwards, \(S_0=0\), and put \(M_n=\max_{0\le j\le n}S_j\). Each backward move followed immediately by a forward move returns to the same sampled state with probability one. Cancelling all such pairs leaves \(M_n\) forward moves followed by \(M_n-S_n\) backward moves. One may also check this inductively. A new backward step increases the trailing backward length, whereas a forward step either cancels its last member or creates a new maximum. The consecutive backward transition probabilities telescope along their unique forward paths.

Therefore, for \(x,y\) with \(g(y)-g(x)=h\), the **conditional** transition probability is
\[
 \mathbf1_{S_n=h}\,
 \mathbf1_{T^{M_n-h}y=T^{M_n}x}\,
 \frac{d_y}{d_{T^{M_n}x}}                                          \tag{1}
\]
on sequences with \(S_n=h\), and zero otherwise. Exponents in (1) are used only on that event. For the fixed pair there is an integer \(m_0\ge\max(0,h)\) such that the second indicator is one for every \(M_n\ge m_0\), since the actual forward trajectories coalesce. Its ratio then tends to \(d_y/m_C\).

Conditioned on \(S_n=h\), every eligible direction word is equiprobable for every \(0<p<1\). At fixed \(h\) its maximum tends to infinity in probability as \(n\to\infty\) through the correct parity. To see this, fix \(K\ge\max(0,h)\). Reflect each path at its first visit to \(K+1\). Its endpoint becomes \(2(K+1)-h\), and every path from zero to that endpoint visited \(K+1\). The ratio of its binomial count to the count ending at \(h\) tends to one for fixed integers \(K,h\). The conditional probability (1) always lies in \([0,1]\). Consequently
\[
 \frac{P_p^n(x,y)}
 {\binom n{(n+h)/2}p^{(n+h)/2}(1-p)^{(n-h)/2}}
 \longrightarrow \frac{d_y}{m_C}.                              \tag{2}
\]
In fact the ratio on the left, whenever defined, is already independent of \(p\) at every finite \(n\).

In particular
\[
 P_{1/2}^{2n}(x,x)\sim\frac{d_x}{m_C\sqrt{\pi n}} .
\]
The sum of returns diverges. Equivalently the elementary Markov return renewal shows that the probability of returning to \(x\) is one. The chain is null recurrent, by absence of an invariant probability. At \(p\ne1/2\) the binomial return bound is exponentially summable and the chain is transient. The endpoint \(p=1\) is the physical map on this same component and escapes from every vertex by hypothesis.

For the reversible conductance \(c(v,Tv)=d_v\), every grade cut carries \(m_C\). A slab of \(k\) grade steps with each end grade held at one common voltage has effective resistance \(k/m_C\). The voltage linear in grade solves the network equations, and for any admissible voltage the conductance-weighted average potential differences telescope over the grades. Cauchy–Schwarz gives energy at least \(m_C/k\) for a unit voltage difference, attained by the linear function. These statements allow countably many sites on a grade since its total conductance is finite. In particular the conserved unit flow to the forward end has infinite energy through successive grade cuts. This agrees with the recurrent heat law. Unit conductance on the ternary unit core is a different network, for which PR201 proves transience. [PR201, first-parent impedance](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/operator/IMPEDANCE.md)

## The ordinary finite-measure obstruction

For the deterministic map \(T\), every atom \(x\) of a finite invariant measure satisfies \(\pi(Tx)\ge\pi(x)\). If its forward trajectory is injective and \(\pi(x)>0\), infinitely many different atoms have at least that mass, contradicting finiteness. A finite invariant measure can charge a cycle, but charges no strictly preperiodic atom either. Summing the finite incoming balance over the cycle already accounts for its entire outgoing mass, forcing all extraneous incoming weights to vanish, and induction applies to each predecessor layer.

Assani's published finite invariant-measure theorem for this exact shortcut is consistent with this obstruction. Its separate power-boundedness equivalence imposes further conditions on the measure and conservative part. Neither the theorem nor a finite invariant law on a local completion assigns an ordinary probability atom to an escaping starting point. [Assani, Studia Mathematica 275 (2024), 249–261](https://doi.org/10.4064/sm230913-14-12) · [Author preprint, arXiv:2208.11675v3](https://arxiv.org/abs/2208.11675v3)

The same heat theorem also applies to the *weighted harmonic gate charge itself*. On the escaping component let \(D_v\) be the native weighted first-hit density and \(W(v)\) the full future survival. The annular-current source inputs give \(D_v=\sum_{Tu=v}c(u)D_u\), \(W(u)=c(u)W(v)\), \(W(a_n)\to1\), and \(D_{a_n}\to\beta_C=b_C/c_*>0\). Hence \(d'_v=W(v)D_v\) obeys the exact undamped split and every grade has total \(\beta_C\). Repeating (1)–(2) verbatim with \(d'_v,\beta_C\) yields a null-recurrent reversible chain with return coefficient \(W(x)D_x/\beta_C\), even though the directed component was assumed to carry this positive harmonic charge. The conductance, reversible return, and finite gate are three different quantities. A new constraint on the directed arithmetic transport is still needed to force the harmonic gate mass to vanish.
