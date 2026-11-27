# An integrable part of the actual predecessor potential

Let h(a) denote the natural density of positive ordinary sources whose shortcut trajectory visits the positive odd target a. The existence of these fixed-target densities is an external input. This argument uses finite additivity and an elementary property of ordinary trajectories. It does not assume eventual periodicity or the existence of a nonconverger. [Valbuena, theorem-to-Lean map, rows 16–18, pinned source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/basin-lean-claims.md)

## Antichains and neighborhoods of component minima

Call a set A of distinct odd positive targets an antichain if no one of them ever visits another. For any such **fixed** A,

    Σ_{a∈A} h(a) ≤ 1.

Indeed every finite subcollection has disjoint ancestor sets and hence total natural density at most one. Taking the supremum of the finite sums gives the bound without invoking countable additivity of natural density.

More generally, let D be any fixed set of targets with Σ_D h(a)<∞. Its entire normalized potential obeys

    lim_{X→∞} (1/X) Σ_{a∈D, a≤X} a h(a) = 0.

For fixed a, the summand after division by X tends to zero; it is dominated by h(a). Also

    sup_{X≥1} (1/X) Σ_{a∈D, a≤X, a h(a)>M} a h(a)
       ≤ Σ_{a∈D, a h(a)>M} h(a)  → 0        as M→∞.

Both statements remain valid if h is multiplied by an X-dependent stopping indicator, since all terms are nonnegative.

Choose one odd positive representative r_C in every ordinary component C, for instance its least odd member. Let U(a) be the next odd value. For fixed j, consider all a whose first U-visit to their own r_C is at precisely j. The nonperiodic members of this layer form an antichain. Indeed if a≠b in one layer and U^d(a)=b for d>0, a visit to b before the first visit to r_C would give j=d+j. A visit at or after r_C places b on the forward orbit of r_C. Since b also reaches r_C, b is periodic. Members in different components are incomparable by definition. The periodic members of this layer also form an antichain: at most one vertex of a given directed cycle has a prescribed first-hit distance to its specified representative.

Let D_J be the union of layers 0 through J. We have proved

    Σ_{a∈D_J} h(a) ≤ 2(J+1).

Consequently both potential conclusions apply to D_J. For example, taking r_C=1 in its component includes infinitely many arbitrarily large odd inverse parents of 1 already at J=1. For any fixed selection of representatives there also exists a nondecreasing J(X)→∞ with

    (1/X) Σ_{a∈D_{J(X)}, a≤X} a h(a) → 0.

Choose increasing cutoffs X_j→∞ beyond which the j-layer normalized sum is at most 1/j, and use the largest j with X_j≤X. This diagonal construction provides no claimed rate for J(X).

## What remains in the stopped bound

In Sultanow's Appendix D, β=1/200 and X₁=X^(1−2β). For X₁<a≤X set h↓_X(a)=h(a) if a's future visits [1,X₁] and zero otherwise. Thus an actual component minimum in this window makes zero contribution. A forward suffix minimum on any escaping trajectory makes zero contribution as well, even though the **unstopped** ancestor density can be large there. Proposition A7 gives, under its explicit coupling hypotheses, a sufficient uniform-integrability condition for the clipping tail. Corollary A1 separately requires a return-from-below estimate. [Sultanow, Corollary A1 and Proposition A7, v3](https://www.preprints.org/manuscript/202610.2552/v3)

We can now delete D_{J(X)} from Proposition A7's nonnegative sum at a cost o(X), uniformly in the clipping threshold. The outstanding high-potential sum is over targets a in (X₁,X] that do return below X₁ and have either infinite first hitting time to their selected representative or finite first hitting time exceeding J(X). A fixed finite collection of antichains contributes o(X) to that residual as well. For a fixed X and a finite selection F of those targets one has the exact identity

    (1/X) Σ_{a∈F} a h(a)
       = lim_{N→∞} (1/N) Σ_{1≤n≤N} (1/X) Σ_{a∈F∩Orb(n)} a.

The right side counts distinct selected targets along actual ordinary forward trajectories. The comparable target visits under this mean are the remaining arithmetic quantity. A finite antichain decomposition depending on X gives no uniform estimate by itself: a single large target a≈X with h(a) bounded below would already contribute order one. No bound on the residual or on the separate return term follows from the argument above.

## A direct cylinder attempt

Suppose q_i is a hypothetical escaping odd orbit, with q_0 a ternary unit. Actual inclusion of predecessor sets gives h(q_i)≥h(q_0)>0, where positivity is supplied by the fixed-target predecessor theorem. The published weighted/unweighted comparison therefore makes the integer trace at q_i at least c q_i for a fixed c>0. This uses neither countable additivity of natural density nor an interchange of the growing target and source-cutoff limits. Let ρ_k(q) be the normalized mass of q's ternary cylinder at depth k under the canonical stationary Syracuse law. The published maximum-cylinder estimate gives

    ρ_k(q) ≤ (2k+3)(3/2)^k.

Therefore observing ρ_k(q)≥c q at a positive target q→∞ requires k≥log_(3/2)(q)−O_c(log log q). By contrast, mere L^p integrability for fixed p<2 gives only an upper bound of size O_p(3^(k/p)). The trace identification is at each fixed integer before the cylinder-depth limit; it supplies no uniform observation clock at moving targets. [Maximum-cylinder proof, pinned source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/formal-basins-native/source/CanonicalSyracuseCylinderLaw.lean) · [Integer trace and integrability, pinned summary](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/tree/a7275d5a73814d3d9a400c6fe6577de9542b03a3)

To test propagation from the fixed beginning of that orbit, take j actual Syracuse steps. Their stationary affine branch sends a depth-k cylinder into one of depth k+j, and contributes the multiplicative density factor 3^j/2^(e₁+⋯+e_j)≤(3/2)^j. The image cylinder has Haar volume 3^(−j) times the initial volume. Thus the L^p energy attributable to that one branch is multiplied by at most ((3/2)^p/3)^j, which decays even at p=2. Along a single propagated seed the lower estimate never forces a failure of stationary integrability. Controlling overlap from other actual predecessor branches at the relevant target-dependent depths, or bounding the comparable visits in the preceding display, is the missing estimate. Archimedean recurrence of corrected logarithmic heights alone supplies neither estimate.
