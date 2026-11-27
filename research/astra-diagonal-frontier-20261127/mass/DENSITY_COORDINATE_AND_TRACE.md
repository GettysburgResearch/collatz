# Predecessor density controls the real correction on every ordinary branch

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on the positive odds. Write \(B_a=\{x:U^jx=a\text{ for some }j\ge0\}\), and let \(d_a\) be its odd-relative natural density. Write \(d_C\) for the density of a complete component. Put \(c_x=1/(3x+1)\), \(w_x=1-c_x\) and \(\kappa=\frac12\log(4/3)\). For nonperiodic \(a\), let \(\beta_a=h(a)/(\kappa a)\), where \(h\) is the stationary trace of the original geometric law. At a nonunit odd site both \(d_a\) and \(h(a)\) vanish.

**Source-qualified written result.** The source inputs are the ordinary predecessor density floor \(d_z\ge b/z\) for every positive odd ternary unit, with absolute \(b>0\), natural first-hit laws, and the stationary first-arrival identity. The floor follows from Wren's Theorem 1 with its stated averaged joint mixing input. For an odd target, stripping an initial power of two preserves hitting, so odd-relative and all-positive densities agree whenever they exist. The results below concern the actual positive integer graph. [Wren, Paper 10 v3, Thm. 1 and Cor. 3.6](https://rstation.ai/problems/collatz/papers/10/v3) · [Weaver, Paper 12 v1, natural first-hit laws](https://rstation.ai/problems/collatz/papers/12/v1) · [Prior stationary component budget, equations (2)–(4)](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md).

## A density increment at each ordinary transient edge

On every actual edge \(x\mapsto y\) with \(y\) nonperiodic,
\[
                  c_x\le L(d_y-d_x),\qquad L=7/b .                    \tag{1}
\]
Indeed the unit sibling of \(x\) used in PR 193 is \(z=4x+1\) for \(x=1\bmod3\) and \(z=16x+5\) otherwise. It shares the same successor, is distinct, and satisfies \(z\le21x\). Since \(y\) is nonperiodic, the predecessor sets of its two distinct parents are disjoint. Hence \(d_y-d_x\ge b/(21x)\). This needs neither a density-rate estimate nor an assumption on the next clock. [Prior explicit sibling, §1](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/arithmetic/PERIODIC_TRACE.md).

For a genuine path from \(x\) until its first hit of a nonperiodic \(a\), summing the stronger bound \(1/(3z)\le L(d_{Uz}-d_z)\) gives
\[
 \sum_{z\text{ before }a}\frac1{3z}\le L(d_a-d_x),\qquad
 e^{-L(d_a-d_x)}\le \prod_{z\text{ before }a}w_z\le1.               \tag{2}
\]
Here \(-\log w_z=\log(1+1/(3z))\le1/(3z)\). The first-hit formula \(\beta_a=\lim_X\mathbb E[1_{B_a}(x)\prod w_z]\), with an ordinary odd source growing to infinity, therefore gives
\[
            d_a e^{-L d_a}\le \beta_a\le d_a .                        \tag{3}
\]
In particular \(h(a)/(\kappa a)=d_a+O(d_a^2)\), uniformly even as the specified positive target varies. On an escaping component the same argument applies to all future prefixes. The actual correction starting at \(x\) lies in \([e^{-L(d_C-d_x)},1]\). Taking an increasing sequence of nonperiodic targets on the component and using \(d_{a_j}\to d_C\), \(h(a_j)/a_j\to H_C\), gives
\[
                 \kappa d_C e^{-L d_C}\le H_C\le\kappa d_C .         \tag{4}
\]
These statements describe the accuracy of linearization for a small-density target or component.

## A convergent expansion in the densities of actual ancestors

Write \(z\prec a\) if \(z\ne a\) is a strict predecessor of the nonperiodic target. With \((Kf)(a)=\sum_{z\prec a}c_z f(z)\), the prior trace budget is \(\beta+K\beta=d\). Set \(A_0(a)=d_a\) and for \(j\ge1\) put
\[
 A_j(a)=K^jd(a)=\sum_{z_1\prec\cdots\prec z_j\prec a}
                          d_{z_1}\prod_{i=1}^j c_{z_i}.
\]
Then for every integer \(J\ge0\),
\[
 \left|\beta_a-\sum_{j=0}^{J}(-1)^j A_j(a)\right|
       \le A_{J+1}(a)\le d_a\frac{(L d_a)^{J+1}}{(J+1)!}.           \tag{5}
\]
The remainder has sign \((-1)^{J+1}\) or vanishes. To prove the factorial estimate, first restrict all marked sites to any finite set of positive odds. Average the corresponding elementary symmetric path sum over the natural odd sources in \(B_a\), dividing by the total number of odd sources. Each fixed strict chain is visited before \(a\) exactly when the source belongs to \(B_{z_1}\), so its limiting weight is \(d_{z_1}\). Pathwise the sum is at most \((\sum_{z\text{ before }a}c_z)^j/j!\le(Ld_a)^j/j!\) by (2). Supremize over increasing finite site sets. Iteration of the positive identity \(\beta=d-K\beta\) now gives the remainder \((-1)^{J+1}K^{J+1}\beta\). It lies in absolute value between zero and \(A_{J+1}\). All rearrangements of the ordered positive sums are justified by this same bound.

Everything passes to an escaping component \(C\). Increase \(a\) along any one ordinary ray; each finite chain in \(C\) eventually occurs strictly before \(a\), and each ordered coefficient increases. Put \(A_0(C)=d_C\) and use all strict chains in \(C\) for the higher coefficients. Then (5) holds with \(\beta_a\) replaced by \(H_C/\kappa\). In particular
\[
 0\le {H_C\over\kappa}-d_C+\sum_{x\in C}{d_x\over3x+1}
            \le \tfrac12 L^2d_C^3,\qquad
 \sum_{x\in C}{d_x\over3x+1}\le Ld_C^2 .                             \tag{6}
\]
For any union of escaping components of total density \(d\), the sum of the absolute remainders after order \(J\) is at most \(L^{J+1}d^{J+2}/(J+1)!\). The earlier stationary identity expresses the deficit as a sum using \(h(x)\) itself. These coefficients use only ordinary predecessor densities and the integer values of ordered sites.

## A two-source interpretation of the first coefficient

For each nonperiodic target \(a\),
\[
       \sum_{x\prec a} d_x(d_{Ux}-d_x)=d_a^2.                          \tag{7}
\]
At a level of the inverse tree the natural first-hit law gives \(\sum_{Ux=y}d_x=d_y\). Thus the contribution between levels \(k-1\) and \(k\) is the decrease of the sum of squared vertex densities. The least ancestor of every vertex at level \(k\) tends to infinity uniformly in that level: the paths to \(a\) of the finitely many bounded potential ancestors have only finitely many pre-hit states. The uniform predecessor-minimum estimate implies \(\max_{U^kx=a}d_x\to0\). Hence the level sum of squares, bounded by \(d_a\max d_x\), tends to zero. Nonunit leaves cause no difficulty. The qualitative decay required here was already available in Weaver's Theorem 11. [Paper 12 v1, Theorem 11](https://rstation.ai/problems/collatz/papers/12/v1) · [Power refinement](PREDECESSOR_MINIMUM_POWER.md).

Increasing \(a\) on an escaping ray gives (7) on all of \(C\) with right side \(d_C^2\). For two independent ordinary sources conditioned to belong to \(C\), let \(X\) be the last vertex of the first path before its first common vertex with the other. Its limiting probability law is
\[
           \Pr(X=x)={d_x(d_{Ux}-d_x)\over d_C^2}\quad(x\in C).
\]
In fact the event for a fixed \(x\) has independent unconditioned factors \(B_x\) for the first source and \(B_{Ux}\setminus B_x\) for the other. These events are disjoint. Their masses sum to \(d_C^2\), so no mass from source comparability escapes the limit. This proves convergence in total variation when both source octaves tend to infinity, with no required coupling of their sizes. Consequently \(A_1(C)/d_C^2\) is the expectation of the bounded observable \(c_X/(d_{UX}-d_X)\) under this true two-source law. Zero-mass states are omitted.

The same sampling also gives an all-order interpretation and a slightly stronger factorial. Given \(j+1\) independent sources conditioned to reach nonperiodic \(a\), use the first as a distinguished source and let \(X_i\) mark its last vertex before its first common vertex with source \(i+1\). Omit a configuration without that mark. Define \(r_x=c_x/(d_{Ux}-d_x)\) on positive-density branches. For a prescribed finite strict chain \(z_1\prec\cdots\prec z_j\prec a\), the limiting probability that \(X_i=z_i\) for every \(i\) is
\[
             d_a^{-j-1}d_{z_1}\prod_{i=1}^j(d_{Uz_i}-d_{z_i}).
\]
The distinguished path must hit \(z_1\) and the other \(j\) paths must lie in the respective sibling unions. Each individual mark is tight by (7), so the vector is tight. Thus \(A_j(a)\) equals \(d_a^{j+1}\) times the limit of the expectation of \(\prod_i r_{X_i}\) on the strict ordered-mark event. Each factor is at most \(L\). Conditional on an unordered configuration, all source labels are exchangeable when sampled in a common octave. If the event holds, the first pair to meet is the distinguished source and source 2, then source 3 joins their common path, followed one at a time by the rest in that order. Among all \((j+1)!\) permutations at most two have the prescribed strictly ordered marks, from swapping the initial pair. To see uniqueness, remove the unique last singleton branch at the final merge and repeat, until only the first two sources remain. Ties or a merge of two multisource branches cannot realize the strict event. Source comparability at a merge has total probability tending to zero by the two-sample law and symmetry, and a finite union covers every pair. Hence, for \(j\ge1\),
\[
           A_j(a)\le {2d_a(Ld_a)^j\over (j+1)!}.                      \tag{8}
\]
For an independent algebraic check, (1) and the level flow give \(Kd\le Ld^2\), while \(K(d^p)\le Ld^{p+1}/(p+1)\) for integers \(p\ge2\). At each parent with child proportions \(t_i\) summing to one, use
\(\sum_i[(p+1)t_i^p-pt_i^{p+1}]\le\sum_i(3t_i^2-2t_i^3)\le1\).
The first inequality follows by subtracting the expression at \(p+1\) from the expression at \(p\), which gives \((p+1)t_i^p(1-t_i)^2\). The second is the probability that three independent child draws are not all distinct. After multiplication by the parent density to power \(p+1\), telescoping through levels gives the stated estimate. Iterating it gives (8), which also passes to escaping components.

## A complete eventual cycle

If \(x\) is off-cycle and \(Ux\) is on a cycle, choose among the three larger siblings \(4x+1,16x+5,64x+21\). Two are units and at most one lies on the cycle, so one nonperiodic unit sibling \(z\le85x\) has \(B_z\cap B_x=\varnothing\). Both basins lie in the same component. Thus all transient edges satisfy (1) after collapsing the whole cycle to one vertex of density \(d_C\), with \(L'=85/(3b)\). As a result the total stationary loss on transient sites satisfies
\[
              \sum_{x\in C\text{ transient}}{h(x)\over x(3x+1)}
                                  \le\kappa L' d_C^2.                  \tag{9}
\]
For any finite set of such sites, average its reciprocal-cost occupation over sources in \(C\). The costs on each path before its first cycle visit sum to at most \(L'd_C\) by telescoping. Pass to the natural densities, then increase the finite set, giving \(\sum c_x d_x\le L'd_C^2\). Use \(h(x)/x\le\kappa d_x\) here only at transient sites. The prior component budget now leaves at least \(\kappa d_C(1-L'd_C)\) on the periodic phases.

Finally all cycle phases together have \(\sum_{x\text{ on cycle}}1/(3x)\le Ld_C\), by PR 193's disjoint off-cycle unit siblings. The path to a first hit of any one cycle point comprises a transient path and at most a single lap. Its physical correction is therefore at least \(e^{-(L'+L)d_C}\). Writing \(\omega_C=\prod_{x\text{ on cycle}} w_x\), the stationary first-arrival identity, including removal of one primitive terminal lap, gives at each cycle phase \(a\)
\[
 d_Ce^{-(L'+L)d_C}\le (1-\omega_C)h(a)/(\kappa a)\le d_C .
\]
The cycle multiplier is essential. The component and first-arrival identities permit an isolated positive-density exceptional component. The bounds quantify its charge and its correction without giving extinction.
