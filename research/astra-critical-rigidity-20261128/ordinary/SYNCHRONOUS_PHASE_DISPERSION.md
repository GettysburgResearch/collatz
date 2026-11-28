# Independent ordinary starts at a common shortcut date

**Proposed, source-qualified written result.** The external analytic inputs are identified below; this note is not a Lean formalization.

Let \(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\). Take \(k\ge2\) independent uniform samples \(n_i\) from the **positive integers** through \(X\). A synchronous merger means equality of their ordinary values after the same number of shortcut steps. For each genuine positive cycle \(C\), write \(P_C\) for its least shortcut period and \(b_C(X)\) for the fraction of the sample interval in its entire basin. The following statements concern independently sampled starts at macroscopic separation.

1. The probability \(K_k(X)\) of ever synchronizing satisfies
   \[
     K_k(X)=\sum_C b_C(X)^k/P_C^{\,k-1}+o(1).                         \tag{1}
   \]
   This approximation uses only the density-one coalescence of consecutive starts. With the positive-predecessor input below, universal convergence is equivalent to \(\limsup_X K_k(X)=2^{1-k}\).
2. With the published minimum and clock laws, put \(d_C=\lim_X b_C(X)\). For \(u\in\mathbb R\) and any integer clock
   \[
     H_X=\mu\log X+\sigma u\sqrt{\log X}+o(\sqrt{\log X}),\quad
     \mu=2/\log(4/3),\qquad \sigma^2=2(\log3)^2/\log^3(4/3).
   \]
   Then
   \[
     \lim_X\Pr(T^{H_X}n_1=\cdots=T^{H_X}n_k)
        =\Phi(u)^k \sum_C d_C^k/P_C^{\,k-1}.                         \tag{2}
   \]
   Here \(\Phi\) is the standard normal CDF and all logarithms in the clock are natural. The same component sum without the factor \(\Phi(u)^k\) equals \(\lim_X K_k(X)\). In particular Collatz is equivalent, for two independent starts, to an equality probability tending to **\(1/8\)** at the single date \(\lfloor\mu\log X\rfloor\).

The previous pass proved a quantitative anti-concentration bound for integer clocks on cut component trees and equidistribution modulo every fixed modulus. Those results already contain stronger versions of the elementary aperiodic and fixed-period phase controls used here. The present application keeps the wrapped phases of unrestricted genuine cycles, controls the entire long-period tail, and extracts the finite-date independent collision profile. The earlier variance criterion instead uses the variance of odd-departure frequencies at a superlogarithmic deadline. [Cut-clock bound](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase3/CLOCK_DISPERSION.md) · [Joint clock phases](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase3/CLOCK_PHASES.md) · [Source variance](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/SOURCE_VARIANCE.md)

## The genuine phase quotient and its two dilations

Write \(m\sim n\) if \(T^t m=T^t n\) for some \(t\ge0\), and \(c(n)\) for its equivalence class. The induced map \(S c(n)=c(Tn)\) is injective by adding one step and surjective since \(T(2n)=n\). Its orbits are precisely the ordinary asynchronous components, since \(T^a m=T^b n\) identifies the corresponding shifted classes, and equality of two shifted classes supplies an actual common future. A finite \(S\)-orbit of length \(P\) means \(T^{t+P}n=T^tn\) at some actual date \(t\). Conversely every basin of a primitive positive \(P\)-cycle has precisely \(P\) phases, represented by its cycle states. Infinite components have infinitely many phases. For any bounded \(P\) there are finitely many genuine cycles of period at most \(P\). Each binary word of length \(j\le P\) defines an affine map of slope \(3^g/2^j\ne1\) and determines at most one fixed point.

Let \(\mu_X=X^{-1}\sum_{n\le X}\delta_{c(n)}\) for positive integer \(X\) and \(d\) the total variation distance \(\sup_A|\mu(A)-\nu(A)|\) for probability measures. Duran's Corollary C gives counted shortcut mergers on a proportion tending to one of complete dyadic blocks as the clock grows. Equivalently, in Leen's notation the balanced shortcut time \(A\) from \((0,1)\) has \(\Pr(A>t)=O(1/\sqrt t)\); the exact dictionary and binary-cylinder lemma make every success a true shortcut merger on every ordinary lift of the residue. First fix \(t\), count full blocks modulo \(2^t\), then send \(t\) to infinity. Thus \(\#\{n\le X:c(n+1)\ne c(n)\}=o(X)\). No balanced-count condition is imposed on the pairs defining (1). [Duran, Corollary C](https://doi.org/10.5281/zenodo.23003524) · [Leen, original exact rates, binary-cylinder and balanced-shortcut lemmas and uniform pair absorption theorem](https://doi.org/10.5281/zenodo.23268751)

For any fixed modulus \(m\), the distribution of \(c(n)\) on each individual residue among \(n\le X\) is within \(o(1)\) in total variation of \(\mu_X\). In each full block of \(m\) consecutive integers, the \(m\) labels agree unless the block contains a neighboring disagreement. The affected mass is \(o(X)\) and incomplete blocks cost \(O(m)\). From \(c(2n)=S^{-1}c(n)\) and restriction to the even residue it follows that \(d(\mu_{2X},S^{-1}_*\mu_X)\to0\). For odd \(n\), \(Tn=(3n+1)/2=T(3n+1)\), so \(c(3n+1)=c(n)\) exactly. These odd sources map bijectively onto residue \(4\bmod6\) through \(3X+1\), up to bounded endpoints. Restriction to the odd and to the \(4\bmod6\) residues proves \(d(\mu_{3X},\mu_X)\to0\).

For nested integer cutoffs \(U,V\), \(d(\mu_U,\mu_V)\le |U-V|/\max(U,V)\). Iterating each dilation a fixed finite number of times gives
\[
 \limsup_X d(S_*^p\mu_X,\mu_X)
    \le |2^p-3^q|/\max(2^p,3^q)                                     \tag{3}
\]
for all positive integers \(p,q\). The inverse shift from the dyadic dilation has the same distance from the original measure as the forward shift. Irrationality of \(\log_3 2\) makes the right side arbitrarily small, even with \(p\equiv1\bmod P\) for any specified \(P\).

## Finite periods, long periods, and independent samples

Fix a cycle \(C\). Take \(p\equiv1\bmod P_C\) in (3). Restricting the shift discrepancy to each singleton phase shows all \(P_C\) phase masses are \(b_C(X)/P_C+o(1)\). For any integer \(M\), choose \(p,q\) with right side \(<M^{-2}\). Let \(A_X\) pick at most one phase from each infinite orbit or orbit of period \(>Mp\), arbitrarily depending on \(X\). The \(M\) sets \(S^{ip}A_X\), \(0\le i<M\), are disjoint. Their masses each differ from \(\mu_X(A_X)\) by at most \(i\,d(S^p_*\mu_X,\mu_X)\). Consequently
\[
 \lim_{D\to\infty}\limsup_X
   \sum_{C:\ P_C>D\ \text{or infinite}}\max_{a\in C}\mu_X(a)=0.     \tag{4}
\]
Indeed the limsup for \(D=Mp\) is at most \(1/M+(M-1)/(2M^2)\); maxima exist on the finite sample support. This also holds with any bounded number of selected phases per component.

The exact common-future probability is \(\sum_a\mu_X(a)^k\), since equality of all classes supplies a single finite common clock by taking the largest pairwise witness. On a fixed cycle its contribution is \(b_C(X)^k/P_C^{k-1}+o(1)\). On long or infinite components the contribution is bounded by the left-hand sum in (4), since \(\sum_{a\in C}\mu_X(a)^k\le b_C(X)\max_{a\in C}\mu_X(a)\). The proposed cycle terms of period \(>D\) sum to at most \(D^{1-k}\). Truncate to finitely many cycles and then let \(D\) tend to infinity. This proves (1).

There is no positive fixed point of \(T\), and \(1,2\) form a genuine 2-cycle. Let \(b=b_{\{1,2\}}(X)\). If every positive source converges, (1) tends to \(2^{1-k}\). If a counterexample exists, Mazur's positive-predecessor theorem and its corollary give constants \(c,\delta>0\) with \(c\le b\le1-\delta\) for all large \(X\). The ordinary and shortcut convergence basins coincide. Therefore the right side of (1) is at most \(2^{1-k}[b^k+(1-b)^k]\), uniformly strictly below \(2^{1-k}\). Mazur's result, including the transfer between raw and shortcut predecessors, is a prior external theorem. [Mazur, original manuscript, Theorem 1.1, Corollary 1.2 and (1.3)](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)

## Finite-date probability

Here we additionally import Leen's natural minimum law and shortcut clock theorem. With \(m(n)=\min_j T^j n\) and \(\tau_*(n)\) its first attainment, the minimum law converges on the discrete positive integers to a probability \(p_m\); jointly and independently, the centered and normalized time \((\tau_*-\mu\log n)/(\sigma\sqrt{\log n})\) tends to standard normal. Replacing \(\log n\) by \(\log X\) costs \(o_P(1)\) in this normalization since \(n\) is uniform through \(X\). These are imported written results. [Leen, *Brownian motion in Collatz orbits*, minimum-time corollary and arithmetic-progressions theorem](https://doi.org/10.5281/zenodo.23269488)

For any asynchronous component \(C\), \(n\in C\) iff \(m(n)\in C\). Thus \(d_C=\sum_{m\in C}p_m\) exists and the entire component law converges in total variation by tightness. For a fixed cyclic \(C\), on its basin write \(t_C(n)\) for the first entry into the cycle. If this entry is at or before \(\tau_*\), then \(\tau_*-t_C<P_C\), since the minimum occurs on the cycle. Otherwise \(t_C-\tau_*\) is exactly the time from the fixed positive integer \(m(n)\) to the cycle. Truncating the tight minimum gives \(t_C-\tau_*=O_P(1)\) on this subpopulation, with unconditional normalization. Consequently
\[
 X^{-1}\#\{n\le X:n\in C,\ t_C(n)\le H_X\}\longrightarrow d_C\Phi(u).
                                                                        \tag{5}
\]
Every bounded-width interval of entry times at \(H_X\) consequently has mass \(o(1)\). In fact \(\sup_j X^{-1}\#\{n\le X:n\in C,\ t_C(n)=j\}=o(1)\): the finite measures of normalized times converge weakly to the continuous measure \(d_C\,d\Phi\), so finite subdivisions of a compact interval plus its two tails bound the maximal atom.

Within (5), each phase has mass \(d_C\Phi(u)/P_C+o(1)\). To check this at the moving cutoff, apply the dilation proof above to the phase submeasures restricted to \(n\in C,t_C(n)\le H_X\). Neighboring labels and entry times agree whenever neighbors have merged by a fixed date \(t\) before hitting the cycle. Among starts \(n>2^t\max C+1\) (here \(\max C\) refers to the cycle itself), reaching a cycle element by date \(t\) is impossible since \(T^i n\ge n/2^i\). Fix \(t\) then send \(t\to\infty\) as before. The fixed-residue comparison holds also with an inactive label for omitted sources. At the even and odd-triple steps entry times change by \(1\) and \(0\), respectively, apart from finitely many starts adjacent to or on the fixed cycle. For any fixed \(v>0\), \(H_{\lfloor vX\rfloor}-H_X=o(\sqrt{\log X})\); (5) and continuity give negligible mass between those thresholds. For nested neighboring scale cutoffs \(U,V\) in (3), first impose the same threshold and use the ordinary nested empirical bound, then change to the respective thresholds at an \(o(1)\) cost for fixed \(p,q\). This proves the restricted (3) and hence the phase assertion.

For independent starts in a fixed cyclic basin, equality at \(H_X\) occurs on the cycle precisely when all starts have entered and all phases agree. Its probability tends to \(d_C^k\Phi(u)^k/P_C^{k-1}\). Equality away from the cycle forces all entry dates to be *exactly the same* later integer, because their remaining future is then identical. Its probability is bounded by the maximal atom of \(t_C\) for two independent samples, hence tends to zero. Equality on any long-period or infinite component is bounded by its eventual equality contribution in (4). Truncation therefore proves (2) and the corresponding unbounded-time limit. No implication that the unknown cycle weights vanish occurs in the derivation.
