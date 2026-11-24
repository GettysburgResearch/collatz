# Counting actual Collatz basins on every automatic test

**Written theorem with named external inputs.** Let B be the set of positive inputs whose shortcut Collatz orbit hits 1, and write δ for its ordinary natural density. For every fixed base k≥2 and every fixed k-automatic set S, along *all* integer cutoffs X,

    |B ∩ S ∩ [1,X]| = δ |S ∩ [1,X]| + o(X).

This is an absolute error estimate. If S has positive lower density, its relative basin frequency tends to δ, even if the density of S oscillates. The same conclusion holds for the predecessor set of each fixed target, with its own natural density. Our argument below proves an elementary testing lemma. The Collatz applications use recent preprints on synchronization and natural density. The local Lean module concerns a separate arithmetic kernel.

## 1. Sparse adjacent changes and automatic tests

Let f be a bounded real sequence with Cesàro mean δ and with

    Σ_{n<X} |f(n+1)−f(n)| = o(X).

Let A be any bounded real-valued k-automatic sequence. Then

    Σ_{n<X} (f(n)−δ)A(n) = o(X).                                 (1)

We use a deterministic most-significant-digit automaton for A, with leading zeros ignored (a new initial state gives this convention). Drive its transitions with independent uniform base-k digits, obtaining a finite Markov chain with transition matrix P. Let w be the vector of output values. The probability of still being outside the closed communicating classes after M digits tends to zero. Indeed from every transient state there is a path of length at most the state count into a closed class. Each such path has probability bounded below independently of its starting state.

In a closed class C of period d, assign each state a cyclic index j modulo d so that every transition raises j by one. For any ε>0 there are numbers u(C,j) such that, for every sufficiently large L and every s in every closed class,

    |(P^L w)(s) − u(C, j(s)+L mod d)| < ε.                       (2)

This follows by applying the finite irreducible aperiodic Markov chain convergence theorem to P^d on each cyclic subclass. The numbers u are the stationary means on the terminal cyclic subclasses. Transient periodic behavior requires no estimate beyond the hitting probability.

For an arbitrary large cutoff X choose J with k^(J−1)≤X≤k^J, and pad the expansions below X to J digits. Fix M so that the probability of a transient state after the first M digits is below ε, and fix L for (2). We now take X to infinity with M and L fixed. There are k^M leading-prefix intervals, of length k^(J−M) before truncation at X. Their transient prefixes occupy at most ε k^J ≤ kεX. In each other prefix interval the first M digits already fix a closed class C and a cyclic index j. Every fine interval of length k^L aligned at a multiple of k^L has a single state immediately before its final L digits. Its output mean is (P^L w)(s), within ε of the same number u(C,j+J−M mod d) throughout that leading interval. The final truncated fine interval costs O(k^L).

Put g=f−δ. On each complete fine interval I, replace g by its value at the left endpoint when using the output-mean estimate. The sum of the absolute replacement errors for bounded test weights is at most a fixed multiple of

    k^L Σ_{n<X} |g(n+1)−g(n)| = o(X).

We may therefore replace A in every good prefix interval by its constant u at total cost O(εX)+o(X), including the cost of returning to the actual g. The mean assumption gives sup_{Y≤X}|Σ_{n<Y}g(n)|=o(X). Thus the sum of g on each leading interval, including the last truncated one, is o(X), uniformly in its endpoints. There are at most k^M such intervals. The bad-prefix contribution is O(kεX). Let X tend to infinity and then ε to zero to obtain (1).

## 2. Arithmetic hypotheses on the actual orbit

For any binary label f invariant under shortcut steps above a fixed floor, the set of changes f(n+1)≠f(n) has density zero. Said Duran's Corollary C gives synchronized adjacent-source binary classes of total proportion tending to one with the fixed clock t. Equal odd counts extend each merger to the actual whole class. If n exceeds 2^t times the floor, both shortcut paths stay above it until the merger. Take X to infinity at fixed t and then t to infinity. This implication also appears explicitly as Lemma 2 of *First-landing bounds and canonical inverse laws*. [Said Duran, Corollary C](https://doi.org/10.5281/zenodo.23003524) · [Finite-floor deduction, §3](https://rstation.ai/problems/collatz/papers/12)

Existence of the ordinary natural density for the basin of 1 follows from the fixed-set density theorem of *Same Shadows, Different Forests*, Corollary 4, using Mazur's uniform first-passage transport as an external input. Proposition 7 and the discussion following it give the predecessor version with the stated natural-density input for 3x+1. That manuscript's Theorem 1 separately obtains logarithmic densities by comparing first passages in two incommensurate windows. Tao's Proposition 1.11 is a logarithmic first-passage theorem, and its statement alone supplies no natural-density conclusion. Combining the ordinary mean and the adjacent-variation bound with (1) proves the display above. [Basin and predecessor density theorems](https://www.preprints.org/manuscript/202610.2552) · [Tao, Proposition 1.11](https://doi.org/10.1017/fmp.2022.8)

For these actual fixed-target labels the two hypotheses can also be read directly in Valbuena's accompanying Lean sources. Theorem 16 supplies the ordinary mean through `actual_basin_natural_density`. Lemma 18 supplies `basin_adjacent_variation_tendsto_zero` for every fixed shortcut target, and Lemma 19 already derives the resulting periodic-weight formula. The finite bound before taking limits is at most 2^H t+1+X(1−goodProbability(H))+2^H for target t and prefix depth H. Here the advance over the periodic formula is the extension to every fixed automatic test. The external author reports checking the imported Gao closure and natural-density package; this packet has not rebuilt those thousands of dependencies. [Theorem-to-Lean map, rows 16–19](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/basin-lean-claims.md) · [Adjacent-variation proof](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/formal-periodic-census/source/BasinAdjacentVariation.lean) · [Natural-density proof](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/formal-basins-native/source/NaturalScalarPrefix.lean)

## 3. Exact prediction error and a positive convergence criterion

For binary A=1_S, write m_X=X^(-1)|S∩[1,X]|. Expanding the indicator of a mismatch gives

    X^(-1) |(B △ S) ∩ [1,X]| = δ + (1−2δ)m_X + o(1).            (3)

In particular every fixed machine has limiting lower error at least min(δ,1−δ), and one of the two constant machines attains the bound. This remains the infimum if each candidate has a different radix and arbitrarily many states. Exactly the same formula holds for detecting whether an input ever hits 5. Its target density and complementary density are both positive: the disjoint predecessor sets of 5 and 85 each have positive lower density by Lau. [Lau's fixed-target theorem](https://hexagonmath.org/2610.00249v2)

Consequently Collatz is equivalent to approximability of its basin indicator arbitrarily well in lower asymptotic error by a **family** of fixed finite automata, with each machine evaluated along unbounded cutoffs before the infimum is taken. If (3) gives δ=0 or 1, positive predecessor density of 1 excludes 0. If an actual counterexample exists, its orbit contains an odd target coprime to 6 whose predecessors are all counterexamples, so δ<1. Conversely, under universal convergence the constant-one machine is exact.

There is also a one-sided criterion: on *any one* automatic S, it suffices to exhibit cutoffs X_j→∞ with |S∩[1,X_j]|≥cX_j for some c>0 and only o(X_j) genuine nonconvergers among the admitted sources. The leading display gives (1−δ)c=0, and Lau gives complete convergence. Equivalently it suffices to supply ordinary certificates of convergence for all but o(X_j) of the admitted sources at those cutoffs. A nonconstant predictor with a measured advantage in a finite range supplies neither the asymptotic bound nor the certificates.

## 4. First passage and the remaining mass estimate

For the odd log-uniform law on [y,y^α], label each input by its ordinary component. On finite first passage this label is preserved exactly. By Tao's Proposition 1.11 the total variation distance between the component laws in the two adjacent windows with y=x^α and y=x^(α²) is O((log x)^(-c))+O(x^(-c)). These distances are summable on each fixed grid x=exp(t α^j). This gives a genuine probability limit on the countable set of ordinary components along that grid. Each fixed component has positive mass there by Lau and partial summation. The component masses need not be equal. In fact the scalar fusion/density method also applies to the known distinct basins of 3x−1 under its corresponding analytic inputs.

The remaining quantitative obstacle for a different positive approach is made explicit in *Same Shadows*, Corollary 6 and Appendix D. If h(a) denotes the predecessor logarithmic density, that work proves the lower half of a law for X^(-1)Σ_{a≤X} a h(a). The sharp upper half would exclude unbounded Collatz orbits. Its clipping estimate and its return-from-below estimate are separate obligations. Proposition A7's uniform-integrability hypothesis addresses the clipping term. No argument here bounds the return term, eliminates nontrivial cycles, or supplies the one-sided convergent certificates from §3.

## 5. An explicit density-correct ordinary predictor

There is a deterministic algorithm with a growing integer register that predicts the basin of 1 with zero ordinary natural error density. For input n>0 of binary length L, examine n and the next 7L **ordinary shortcut iterates** and accept exactly on encountering 1. The same guarantee holds for any fixed **odd** target t, including 5. This is a positive construction; its acceptances provide ordinary witnesses.

We use the fixed-threshold first-passage clock from Wren's Theorem 7. For every fixed sufficiently large K and odd input m, except on a set of upper natural density O(1/log K) (take A=1), the first Syracuse iterate ≤K occurs after at most

    log^+(m/K)/log(4/3) + O(sqrt(log m · log log m))

Syracuse steps. This theorem is an external manuscript input. Its one-sided natural-density predecessors and attribution are discussed with its statement. [Fixed-threshold passage clock, v3, Theorem 7](https://rstation.ai/problems/collatz/papers/7/v3)

Choose K≥t. Among the finite set of odd integers ≤K that eventually hit t, their first hitting times have a finite maximum M_K. This constant is used only in the proof. On a source which truly hits t, the first landing ≤K takes place by the time it hits t. If the landing is timely, at most M_K further steps suffice to certify t. Since 3/log 2>1/log(4/3), for all sufficiently large m (with K fixed) this total is ≤3·bitlength(m). Failed detections among true positives have upper density O(1/log K), while false detections never occur. Let K tend to infinity after taking the upper density. Removing the initial powers of two extends the density-zero assertion from odds to all positive integers, by first treating each fixed 2-adic valuation and then making the remaining shells small.

For the 7L clock, if x_i are the successive odd states and e_i=v₂(3x_i+1), then

    e_i = log₂((3x_i+1)/x_(i+1)) ≤ 2 + log₂(x_i/x_(i+1)).

After j≤3L odd steps, sum and include the initial v₂(n) divisions: the elapsed shortcut time is at most 2j+log₂(n)≤7L. Each intermediate value grows by at most a factor two per clock, so the computation uses O(L) bits and O(L²) bit operations with elementary arithmetic. The full decision machine runs only a predetermined number of actual iterates, and never queries which small seeds converge.

Equations (1)–(3) locate the unproved compilation step precisely. This explicit clock predictor agrees with its actual target in asymptotic density, so testing or approximating its output has the same asymptotic error as testing or approximating the target. If the 1-predictor were approximable arbitrarily well by fixed digit automata in the sense of §3, full convergence would follow. The 5-predictor has the same computational rule and clock, yet no such approximation is possible for it because its two true classes already have positive lower density. A successful compilation therefore has to use a property specific to the terminal basin of 1.
