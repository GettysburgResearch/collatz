# Ordinary inverse entropy at every clock and across all roots

For a specified positive nonperiodic odd unit \(a\), write \(d_a\) for its relative odd natural predecessor density, \(Q_a\) for its natural inverse entrance law, \(h_a=\mathsf H(Q_a(X_1\in\cdot))\), and \(\mathsf H_{a,k}\) for its depth-\(k\) entropy in nats. The root row is the countable distribution \(p_x=d_x/d_a\) on actual unit parents \(Ux=a\). Throughout this note the symbol \(h_a\) denotes **one-step Shannon entropy**, distinct from the canonical harmonic trace normally written \(h(a)\).

The results below use [the natural Shannon law](NATURAL_SHANNON_FRONT.md), [the entire-path side-branch moment](STRICT_CYLINDERS_AND_BRANCH_MASS.md), and the external source inputs specified there. For the depth-uniform lower estimate we use the retained fixed-total estimate in [Weaver and Wren, Paper 200 v2, Input 3.3, (3.4)](https://rstation.ai/problems/collatz/papers/200). The extra gain in the R4 marker exponent is unnecessary here. With \(\beta=7/4\), the elementary alternate estimate in the Shannon note supplies some exponent \(H<1\) in all the moment arguments.

## A positive floor on the original ordinary distribution

For absolute \(c>0\), every nonperiodic odd unit \(a\), and \(k\ge0\),
\[
 \mathsf H_{a,k+1}-\mathsf H_{a,k}
   \ \ge\ {c\over d_a}\sum_{\substack{U^kx=a\\x\ \mathrm{unit}}}
               {\log(2+x d_x)\over x}
   \ \ge\ {c'\over a d_a}.                                               \tag{1}
\]
In particular \(\mathsf H_{a,n}\gg[n+\log(2+a d_a)]/(a d_a)\) for \(n\ge1\). These are finite-clock estimates with absolute constants, including at roots whose eventual entropy-rate onset is unknown.

Every such \(x\) has two distinct unit odd parents at most \(64x/3\): among the first three candidates with the legal parity of their exponents, two are units, as shown in [Weaver, Paper 12, §2](https://rstation.ai/problems/collatz/papers/12). The ordinary density floor \(d_y\ge c_0/y\) gives each of their probabilities at least \(u=c_1/(x d_x)\), with \(c_1\) small enough that \(u\le1/4\). One of the two has probability in \([u,1/2]\). The binary indicator of this parent has entropy at least \(-u\log u-(1-u)\log(1-u)\gg \log(2+x d_x)/(x d_x)\). The chain rule on the actual countable cylinders gives
\[
       \mathsf H_{a,k+1}-\mathsf H_{a,k}
             ={1\over d_a}\sum_{U^kx=a,\ x\ \mathrm{unit}}d_x h_x.
\]
All these finite-depth entropies are finite by the preceding Shannon note. This proves the first bound in (1).

For all sufficiently large \(k\), let \(s\) range over the integers \(|s-2k|\le\sqrt{k}\). At the unit class \(a-3^k2^{-s}\bmod 3^{k+1}\), Paper 200's (3.4) gives at least \(c2^s/(3^{k+1}\sqrt{k})\) inverse gap words with this total and affine offset in this class. Each is legal from the very same \(a\) and its terminal ordinary \(x\) is \(1\bmod3\). Indeed the full congruence modulo \(3^k\) gives every intermediate integrality congruence by reduction, and at each step \((2^e v-1)/3\) is positive at positive \(v\) when integral. The excess digit gives \(x=2^s(a-B_k)/3^k\equiv1\bmod3\). Distinct total/word pairs have distinct ordinary starts because one fixed source has only one forward word of \(k\) steps. Each \(x\) satisfies \(x\le a2^s/3^k\). Summing \(1/x\) over these words and the \(\asymp\sqrt{k}\) totals yields \(\sum_{U^kx=a,\ x\ {\rm unit}}1/x\gg1/a\). The finitely many smaller \(k\) follow by repeatedly choosing a unit parent of size at most \(64/3\) times its child and decreasing the absolute constant. The extra terminal ternary digit matters here, since a nonunit leaf carries no ordinary entrance mass.

For the finite ternary density \(\rho_k\) used by Weaver, an equivalent form is \(\sum_{U^kx=a,\ x\ {\rm unit}}1/x\asymp\rho_{k+1}(a)/a\), uniformly in nonperiodic \(a,k\). Each legal word carries \(w=3^k2^{-s}=(a/x)\prod_{\text{word}}3v/(3v+1)\). The product is bounded away from zero on every simple ordinary word by [Weaver, Paper 176 v1, §5.1](https://rstation.ai/problems/collatz/papers/176/v1). The recursion for \(\rho_{k+1}\) multiplies each such weight by \(\rho_1(x)\), which is \(1\) or \(2\) at units and zero at nonunits. This gives the comparison directly. A height-dependent reciprocal floor is compatible with tiny entropy on long old ordinary histories.

## Summable entropy on a single path and the density threshold

Fix \(H<p<1\) as in the entire-path side-branch theorem. On an actual finite forward path of nonperiodic units \(a_0,\ldots,a_N\), the union of the off-spine unit parents at \(a_i,\ i\ge1\), has \(\sum d_x^p\le C_p\), uniformly in the path and its length. The one-row bound \(\sum_{Ux=a}d_x^p\le C_p\) holds at its initial vertex too, by the finite-depth estimate.

First suppose every \(d_i=d_{a_i}\) on the path is between \(t\) and \(2t\), \(0<t\le1\). The side-parent masses \(w_x=d_x\) have sum \(d_N-d_0\le t\). In row \(i\), the main probability \(u=d_{i-1}/d_i\) costs \(-u\log u\le1-u\). The side terms cost at most \(\sum_{x\text{ at }i}(w_x/t)\log(2t/w_x)\). Put all the \(w_x/t\) into one subprobability vector and complete it by a dummy atom. Its \(p\)-power sum is at most \(1+C_pt^{-p}\), so its Shannon entropy is at most \(\log(1+C_pt^{-p})/(1-p)\). Consequently
\[
       \sum_{i=1}^N h_{a_i}\ \ll_p\ 1+\log(1/t).                        \tag{2}
\]
The row at \(a_0\) obeys the same bound by the one-row \(p\)-moment. For an arbitrary path, the indices in each density octave form one contiguous interval since \(d_i\) is increasing. Apply (2) to that whole interval including its first row. Summation gives the uniform bound \(\sum_{i=0}^N h_{a_i}\ll_p(1+\log(1/d_{a_0}))^2\).

For any fixed root \(a\) and \(0<t\le d_a\), take the tree of its unit ancestors of density at least \(t\), including \(a\). This is finite. Every node has at most \(d_a/t\) high parents across an antichain, by disjoint natural basins. If the finitely branching high tree had unbounded depth it would have an infinite path, whose \(Q_a\) probability is at least \(t/d_a\) by continuity of its nested cylinders. The fixed-root information law \(-\log Q_a([X_1,\ldots,X_k])/k\to\log(4/3)>0\) almost surely excludes this. Write \(\Gamma_{a,t}\) for the actual unit parents just outside this high tree, so each path first crosses below \(t\) there. It is a prefix-free cut of total mass \(\sum_{\Gamma_{a,t}}d_y=d_a\).

There are at most \(d_a/t\) terminal high vertices. Cover the high tree by the paths from these vertices forward to \(a\), allowing overlap. Every \(y\in\Gamma_{a,t}\) is a side parent on one such path, or a parent of its initial vertex. The whole-path estimate and the one-row estimate give
\[
      \sum_{y\in\Gamma_{a,t}}d_y^p \le C_p d_a/t.                        \tag{3}
\]
This is a cut of actual ordinary density, as distinct from fixing the integer height or the inverse clock.

## An exact global limit at exponent one

For all nonperiodic positive odd units together,
\[
 \lim_{L\to\infty}{1\over L}
       \sum_{d_z\ge e^{-L}}d_z h_z=1,\qquad
 \lim_{\theta\downarrow0}\theta\sum_z d_z^{\,1+\theta}h_z=1.            \tag{4}
\]
In particular the sum is finite at each exponent \(1+\theta>1\) and diverges at exponent one. Both limits use relative density among *all* positive odd sources. Periodic root rows are excluded throughout, even if a nonperiodic source eventually reaches a cycle.

For one \(a\) use \(t=e^{-L}\le d_a\) and let \(T\) be the first inverse date with \(d_{X_T}<t\). Write \(I_j=\log(d_a/d_{X_j})\). Since \(I_j/j\to D=\log(4/3)>0\) almost surely, \(T\to\infty\), \(T/L\to1/D\) and \(I_T/L\to1\) as \(L\to\infty\), by bracketing \(\log(d_a/t)\) between \(I_{T-1}\) and \(I_T\). By (3),
\[
  \mathbb E_{Q_a} e^{(1-p) I_T}
       =d_a^{-p}\sum_{\Gamma_{a,t}}d_y^p
       \le C_p d_a^{1-p}/t\le C_p e^L.                                  \tag{5}
\]
Concavity gives a bounded exponential moment for \(I_T/L\) at any fixed positive exponent for sufficiently large \(L\). This proves uniform integrability. In particular \(\mathbb E I_T/L\to1\) and Jensen gives \(\mathbb E I_T\le(L+\log C_p)/(1-p)\), with constants independent of \(a\). By the chain rule for the finite high tree with countable exit edges,
\[
  \sum_{\substack{z\in B_a\ {\rm unit}\\d_z\ge e^{-L}}}d_z h_z
        =d_a\mathbb E_{Q_a}I_T
        \sim d_a L.                                                       \tag{6}
\]
If \(t>d_a\) the left sum is empty. The upper bound \(C d_a(1+L)\) therefore holds uniformly for every \(a,L\ge0\). Equation (5) also gives convergence of every fixed positive moment of \(I_T/L\) to one and of \(\sum_{\Gamma}(d_y/d_a)^{1+\xi/L}\) to \(e^{-\xi}\) for each real \(\xi\), at fixed \(a\).

To pass to all roots, decompose the ordinary functional graph into its countably many connected components. In a component with a cycle \(C\), take as base roots all unit parents of cycle vertices outside \(C\). Their basins are pairwise disjoint, and their total natural densities equal the density of \(B_c\) for any \(c\in C\). Here is the countable-additivity check at the cycle. Label an input by the last parent outside \(C\) before its first entry into \(C\), with a cemetery value for inputs that never enter \(C\) or already lie in \(C\). This label changes only at immediate off-cycle parents, of which there are \(O_C(1+\log Y)\) below \(Y\). The [countable sparse-passage law](RELATIVE_SPARSE_PASSAGE.md) gives total variation convergence. The cemetery has mass \(1-d_c\), and each unit parent label has mass equal to its own nonperiodic basin density. Nonunit parent labels occur only on their own singleton inputs, so each has zero mass. This proves the claimed equality without applying a nonperiodic row identity at \(c\).

In an escaping component choose an actual unit ray \(a_0,a_1,\dots\). Its forward density increases to a number \(d_*>0\); after moving the initial index forward once, one can assume \(d_{a_0}\ge d_*/2\). Take the base roots \(a_0\) and all the unit off-spine parents at \(a_i,\ i\ge1\). Their basins are disjoint and their masses sum to \(d_*\) by the finite nonperiodic row identity and telescoping. These rooted trees contain all unit component vertices apart from the sites \(a_i,\ i\ge1\). A unit in the component has a forward common successor with the chosen ray. Any basin of such a vertex is contained in \(B_{a_N}\) for some finite \(N\).

Across components all the base trees are disjoint. Their densities sum to one. Indeed finite sums of their masses are at most one. Conversely the set hitting one of the finitely many odd sites at most \(M\) has density tending to one as \(M\to\infty\), by the [global forward-minimum bound](PREDECESSOR_MINIMUM_POWER.md); its qualitative tightness suffices. Each such nonunit site has zero basin density. In each of the finitely many touched cyclic components the union has density at most its full \(d_c\), already represented above. In each of the touched escaping components the finitely many small-site basins are all included in one \(B_{a_N}\) of density at most its \(d_*\), also represented above. This proves the other inequality, without countable interchange of upper densities.

By (6) and its uniform dominator, the contribution of all base trees to the first limit in (4) is the sum of their densities, hence one. On a single residual escaping ray (2) gives \(\sum_{i\ge1}d_i h_{a_i}\le C d_*(1+\log(1/d_*))\). For fixed component this contributes zero after division by \(L\) and passage to infinity. If any of those rows has \(d_i\ge e^{-L}\), then \(\log(1/d_*)\le L\), providing the summable dominator \(C'd_*\) for \(L\ge1\). Thus the union of residual rays contributes zero in the limit.

Finally define \(F(L)=\sum_{-\log d_z\le L}d_z h_z\). We have just proved \(F(L)/L\to1\) and \(F(L)\le C(1+L)\), uniformly for \(L\ge0\). Tonelli gives
\[
 \theta\sum_z d_z^{1+\theta}h_z
       =\theta^2\int_0^\infty e^{-\theta L}F(L)\,dL
       =\int_0^\infty e^{-u}\,\theta F(u/\theta)\,du\longrightarrow1.
\]
This finishes (4). The critical divergence arises inside ordinary fixed-root inverse trees even in a terminating component. An escaping forward ray, if present, has summable row entropy and contributes zero to this residue. The exact normalization alone therefore does not exclude such a ray.
