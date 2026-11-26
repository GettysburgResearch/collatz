# Can the subcritical branch bound annihilate the ordinary exit mass?

**Post-publication written test.** The two moment estimates admit an exact comparison on one ordinary component. They also hold simultaneously in a sparse modification of the positive-integer dynamics with an explicit escaping component. The modification can be placed above any prescribed finite cutoff. It tests the proposed interpolation argument and makes no assertion of an escaping orbit for the original map. [PR197, entry-edge gains](https://github.com/GettysburgResearch/collatz/blob/4234561fd59ab0d49dacee40e4d4ef690b1be764/research/ayh-resource-reset-20261124/unconventional/ENTRY_EDGE_GAINS.md) · [PR201, physical exit gates](https://github.com/GettysburgResearch/collatz/blob/3eb251fae9082fef33c047079a511d1c3f4c5969/research/unconventional-20261126/operator/EXIT_GATES.md)

## The common measure on an actual component

Assume an escaping ordinary component \(D\) exists. Choose its odd spine \(q_j=U^j(a)\). Let \(P\) denote the corrected height, extended to even towers by \(P(2^k v)=2^kP(v)\) for odd \(v\). Write \(V(y)\) for all odd sources hitting the odd state \(y\), including \(y\) itself. Let \(F_j\) be the immediate odd predecessors of \(q_j\) other than \(q_{j-1}\), for \(j\ge1\). Put \(B_y(t)=\sum_{v\in V(y)}P(v)^{-t}\).

For the PR201 component atom \(Z_D(t)\), \(t>1\), there is an exact disjoint partition
\[
 (1-2^{-t})Z_D(t)=B_a(t)+
   \sum_{j\ge1}\left(P(q_j)^{-t}+\sum_{y\in F_j}B_y(t)\right).
\]
Each off-spine odd source first enters at one \(q_j\), and for \(j\ge1\) its last off-spine state selects one \(y\in F_j\). Summing even towers gives the factor on the left. Deeper marked generations overlap and cannot be inserted in this partition as additional independent masses.

Writing \(w_y=G_y/P(a)=1/\min_{v\in V(y)}P(v)\), one has
\[
       w_y^t\le B_y(t)\ll_{t,K}w_y^{t-1}
\]
because \(v\le P(v)\le Kv\) and all these distinct positive sources have \(v\ge1/(Kw_y)\). Thus convergence of \(\sum w_y^\sigma\) at \(\sigma<1\) bounds the sum of the branch masses by this comparison for \(t\ge1+\sigma\). Disjointness already gives convergence for every \(t>1\). Neither comparison makes the mass zero. In particular \(B_a(t)\ge P(a)^{-t}\). This is the limiting contribution of the one original source along its own moving gates \(g_X(a)\) as \(X\to\infty\). Normalizing by \(t-1\) removes this single term, but need not remove the whole basin of that source.

## A positive-integer map realizing both estimates

Given any cutoff, take an odd \(q_0\) prime to three above it. Using the original shortcut \(T\), recursively put \(q_{j+1}=T(q_j)\) if this value is odd, and \(q_{j+1}=T(q_j)+3\) otherwise. The \(q_j\) are odd, grow by a factor greater than \(3/2\) at each step, and \(q_j\equiv2\bmod3\) for \(j\ge1\). Define \(S(q_j)=q_{j+1}\), and \(S(x)=T(x)\) at every other positive integer. The even branch is unchanged. An odd branch of \(S\) is \((3x+c_x)/2\) with \(c_x=1\) or \(7\). Both principal slopes and positivity of the additive correction are preserved. All input changes belong to one geometrically spaced sequence. All finite gate calculations at cutoffs through \(q_0\) agree exactly with those of \(T\), since the inputs before their first exits are smaller than the cutoff. For example, \(q_0=101\) gives \(101,155,233,353,\ldots\). At cutoff 102 the new gate 155 replaces the ordinary gate 152 from input 101.

This component has genuine inverse branching. At any \(q_j\), \(j\ge1\), and arbitrarily large \(e\) in a suitable residue class modulo six, \((2^e q_j-1)/3\) is an odd positive number congruent to \(0\bmod3\). Choosing a different class makes it \(1\bmod3\). This follows by prescribing \(2^e q_j\equiv1\) or \(4\bmod9\). These preimages are off the modified sequence apart from the one possible \(q_0\). They reach the target under \(S\) by the ordinary odd step and subsequent halvings. The latter unit preimages themselves have such predecessors to every finite odd depth. A multiple of three is an odd leaf because \(3x+c_x\) is a ternary unit at every odd input.

**Uniform ordinary interval compression survives.** In an interval of \(M\ge2\) consecutive positive starts \([A,A+M)\), consider the first \(h\) shortcut steps. Before first contact with \(\{q_j\}\), the word is ordinary. Any possible contact value lies between \(2^{-h}A\) and \((3/2)^h(A+M+1)\). For \(A\ge M\) the ratio of these bounds is \(O(3^h)\). For \(A<M\) use the lower bound one. In either case at most \(O(h+\log(2M))\) distinct \(q_j\)'s occur, uniformly in \(A\). After contact the path stays on the new spine. Its \(h\)-step endpoint and total odd count have at most \(O((h+1)^2(h+\log(2M)))\) possibilities, by choosing the first site, its clock and the odd count. All paths that avoid contact retain their ordinary labeled endpoint. It follows that
\[
 G^S_h(M)\le G^T_h(M)+O((h+1)^2(h+\log(2M))).
\]
In particular the elementary bound \(\operatorname{polylog}(M)M^\rho\) at \(h=\lceil\log_2 M\rceil\), \(\rho=\max(H_2(3/5),(3/5)\log_2 3)<1\), survives. A further direct count shows that at most \(O(2^h(h+\log(2M)))\) starts in the interval encounter the spine by clock \(h\). Indeed an ordinary word of a prescribed length and a prescribed terminal has at most one source for each parity word. Thus in translated intervals the fraction of changed paths tends uniformly to zero even at \(h\le(1-\epsilon)\log_2 M\), for each fixed \(\epsilon>0\).

**The full branch-max estimate survives.** Given an \(S\)-word of length \(h\) and a terminal, it has at most \(h+2\) possible starts. Either it avoids the spine and ordinary inverse steps are unique, or choose its first spine clock. The spine suffix then has one possible starting point because \(S\) shifts the simple spine, and the preceding ordinary inverse bits determine the rest uniquely. This applies also to segments of length below \(h\). In the three entry-time cases of \(\mathrm{ENTRY\_EDGE\_GAINS}\), recovering a marked preimage from its terminal and its subset of odd clocks therefore costs at most an extra \(h+2\). The case with marker after the comparison clock still follows the determined forward path. This proof works for every supplied escaping ray of \(S\), including a ray distinct from the modified spine.

The uniform short-clock bound also bounds the number of sites of any simple infinite \(S\)-orbit in a dyadic interval of size \(M\) by \(\operatorname{polylog}(M)M^\rho\), since \(S^h\) is injective on that orbit. Thus the reciprocal sum is uniformly bounded. On every escaping component the corrected product with odd factor \(1+c_x/(3x)\) consequently satisfies \(x\le P_S(x)\le Kx\) and the exact multiplicative slope law. The original entry-label proof and dyadic summation now give
\[
 \sum_{1\le r_y\le(\log_2 m_y)/512}
       \left(\frac{G^S_y}{P_S(a)}\right)^\sigma <\infty
 \quad \text{for any }\rho+H_2(1/512)<\sigma<1.
\]
Here \(G^S_y\) is the maximum over all ordinary odd ancestors of \(y\) under \(S\). The parameter \(r_y\) restricts only the marked generation, as in the original theorem.

**The positive atom survives, even under a density test.** Retention along a path under \(S\) still multiplies as \((xC_k(x)/S^k(x))^t\le1\), where \(C_k\) is the principal multiplier. For \(t>1\) the substochastic transport of successive first-exit vectors, monotonicity of the augmented total, and convergence of the sorted weights to the corrected-height component atoms follow from the PR201 proof. The proof uses positivity, coalescence and domination by \(\sum x^{-t}\), all verified here. The component of \(q_0\) supplies \(Z_D^S(t)\ge P_S(q_0)^{-t}>0\). If the fixed-unit positive predecessor lower-density input from the threshold supplement is allowed, even \(\liminf_{t\downarrow1}(t-1)Z_D^S(t)>0\): every original \(T\)-ancestor of \(q_0\) meets the modified spine either there or earlier along its original path. Its positive lower density passes to \(D\), and partial summation using \(P_S(x)\le Kx\) gives the claim. This optional last inference is unnecessary for the positive atom at each \(t>1\).

**Where exact arithmetic enters.** The support of the ordinary exit gates at *all* cutoffs, together with even halving, actually recovers every ordinary odd branch. For odd \(x\) let \(y=(3x+1)/2\). The ordinary support formula makes \(x+1\) the first cutoff admitting \(y\) as an exit. At that cutoff the last step comes from a vertex at most \(x\), and any smaller predecessor of \(y\) would already have supplied an exit at an earlier cutoff. Hence the predecessor is \(x\). This distinguishes full gate support from the abstract positive transport and moment identities. An argument using that extra information must still use its arithmetic consequences on the original map. The countermodel establishes that the two moment estimates, even with ordinary integer labels, usual slopes, uniform translated-interval compression, infinite branching and an arbitrarily large exact cutoff, do not by themselves force the escape mass to vanish.
