# Physical spacing of a zero-entropy ordinary orbit limit

Work with the positive shortcut map and entropy measured in bits. Let $P\to\infty$ index finite simple ordinary trajectories of $P$ consecutive states $x_i$, allowing the initial sources to vary. Suppose their empirical parity processes converge to $\nu$ on a subsequence. It is shift invariant. Fix $B>0$, choose $i$ uniformly among these dates, and put $K_P=\lfloor x_i/P^B\rfloor$. The integer-valued physical cell label can be arbitrarily large.

**Theorem.** The entropy rate obeys

$$
h(\nu)\ \ge\ \limsup_{P}\frac{\log_2 P-H(K_P)}{B\log_2 P}
=\frac1B\limsup_P\frac{\mathbb E[\log_2 n_{K_P}]}{\log_2 P},
$$

where $n_j$ is the number of the $P$ dates in cell $j$, and all limits are on the selected subsequence. More generally, if at least $(\alpha-o(1))P$ dates lie in any family of at most $P^{\gamma+o(1)}$ moving intervals of diameter $P^{B+o(1)}$, with $\alpha>0$ and $0\le\gamma<1$, then $h(\nu)\ge\alpha(1-\gamma)/B$. The intervals' positions, overlap and total span are unrestricted.

Thus a zero-entropy limit requires, for every $B,\epsilon>0$, that only $o(P)$ dates lie in cells with occupancy at least $P^\epsilon$. No union of $P^{1-\epsilon}$ arbitrary intervals of diameter $P^B$ can contain a positive limiting fraction. One can select $P^{1-o(1)}$ physical states mutually separated by at least $P^B$ on that subsequence. This statement includes the possibility of superpolynomial spread on an escaping orbit.

### Proof

Take $m=\lceil B\log_2 P\rceil+1$. Remove the last $m-1$ dates so the full length-$m$ parity windows are available, and draw a remaining date $I$ uniformly. Write $W$ for its parity window and $K$ for its physical cell. The pair $(K,W)$ determines $x_I$, because $W$ determines the residue modulo $2^m$ and the cell has diameter less than $2^m$. Simplicity then determines $I$. Hence

$$
H(W)\ge\log_2(P-m+1)-H(K).
$$

The discarded fraction is $O(m/P)$. A binary keep/discard indicator has entropy $o(1)$, and both component cell laws have support at most $P$, so $H(K)=H(K_P)+O(H_2((m-1)/P)+(m/P)\log_2P)=H(K_P)+o(1)$. The identity for $\mathbb E\log_2 n_{K_P}$ follows by summing $n_j/P$.

For fixed $k$, the chain rule as in the transient entropy manuscript gives $H(W)\le k+(m-k)H_{Q_k}(V\mid W_k)$, with the last conditional law obtained by averaging the $k+1$ interior blocks over starts and offsets. At each fixed internal offset only $O(m)$ of the $P$ parent dates are omitted, uniformly, so $Q_k$ tends to the $k+1$ marginal of $\nu$. Divide by $m$, take the limsup and then let $k\to\infty$ to get the theorem.

For the moving family, choose $m=(B+o(1))\log_2P$ large enough for every diameter. There are $a\ge(\alpha-o(1))P$ covered starts after deleting the right boundary. Each length-$m$ parity word is realized at most once in each interval, hence at most $P^{\gamma+o(1)}$ times in their union. The entropy of the window conditional on a uniform covered start is at least $\log_2 a-(\gamma+o(1))\log_2 P$. The unconditional window entropy is at least $a/(P-m+1)$ times this value by concavity. The same fixed-$k$ bound proves the claim.

If $h(\nu)=0$, Markov's inequality applied to $\log n_{K_P}$ proves the vanishing occupied-cell fraction at every power threshold. Among the other $(1-o(1))P$ states, each cell holds at most $P^\epsilon$. At least half their occupied cells have one fixed index parity; two distinct cells of that parity are separated by at least a full cell width. This gives $\gg P^{1-\epsilon}$ separated states for every fixed $\epsilon>0$, and therefore exponent $1-o(1)$.

### Digit-window consequence, with an imported rigidity theorem

The transient entropy manuscript proves $h(\nu)\ge1/B$ under a bound $P^{B+o(1)}$ on the entire path. Its fixed-$k$ chain rule is also used here. Paper 170 explicitly asks in §6, open problem S5, whether every limit measure of a divergent positive integer orbit has positive entropy. The preceding conditions answer the question on subsequences with the stated physical clustering. The general question remains open.

For an explicit consumer take any proved lower bound $s>0$ on $h(\nu)$ above, let $\rho$ be the odd frequency of $\nu$, and set $f=H_2^{-1}$ on $[0,1/2]$ in the sense of the inverse of the increasing branch. The proportion of Lebesgue measure in any time-first, then scale-averaged digit-window limit on the odd states satisfies

$$
                       c\ \ge\frac{s f(s)}{\rho}.
$$

Indeed Paper 170, Theorem 2 and Corollary 3, bounds $c$ below by $\rho^{-1}\int r_\omega h_\omega\,d\omega$ in bit units, where $r_\omega$ and $h_\omega$ are the odd frequency and entropy of an ergodic component of $\nu$. We use that theorem as a source-qualified input, including Rudolph's measure rigidity theorem in its proof. Since the entropy rate is at most the single-symbol entropy, $r_\omega\ge f(h_\omega)$. The function $t f(t)$ is increasing and convex on $[0,1]$, as $f$ is nonnegative, increasing and convex. Jensen's inequality and affinity of binary shift entropy yield the display. The time and scale limits retain the order of the cited theorem. The averaged digit-window conclusion does not imply fair parities on the physical orbit.

- [Transient entropy source, frozen SHA-256 960aa9089c4c23c63f76cd6e1182528753642994093c63e084876e5280f1078f](TRANSIENT_ENTROPY_AND_CRITICAL_TRACE.md)
- [Paper 170, Theorem 2, Corollary 3, and open problem S5](https://rstation.ai/problems/collatz/papers/170/v1)
