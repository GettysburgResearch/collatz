# A harmonic capacity for ordinary reachability antichains

Write P(a) for all positive integer sources reaching a (allowing zero
steps) under the ordinary Collatz map. Let A consist of positive targets
prime to 3, no two of which reach one another. For every 1<r<2, there
exists an absolute c_r>0 such that

    lower_density( union over a in A of P(a) )
       ≥ c_r (sum over a in A of 1/a)^(r/(r−1)).                   (1)

This assertion uses Mazur’s analytic Proposition 3.1 as an external
input. It supplies a uniform polynomial lower bound for an individual
target and bounds the harmonic sum of every antichain, including infinite
antichains. It does not establish that an individual component reaches
a particular target. Mazur §1.2 credits Wirsching’s preliminary manuscript
with a proposed stronger individual bound of order 1/a for noncyclic
targets. No priority claim is made for the individual target exponent.

[Mazur, *Positive lower density of Collatz predecessors*, §§1,3 and Appendix A](https://proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

## A uniform maximal estimate on the ternary weights

Use uniform probability measure on each ternary quotient and its
projective limit. Mazur Appendix A.1 identifies the weights ρ_k with
(2/3) times the density 3^k μ_k of the k-geometric-step offset of Tao.
The offset laws are consistent modulo lower powers of 3, since the older
steps are multiplied by the corresponding power of 3. Their densities
form a nonnegative martingale. The integer spacing calculation gives
||ρ_k||₂ ≤ 4(k+1). Tao Proposition 1.14 gives, for any fixed D>0,

    ||ρ_n−ρ_m||₁ ≤ C_D m^(−D)     (n≥m≥1).

Put θ=2/r−1. Interpolation on m≤n≤2m gives a difference in L^r of
at most C m^(1−θ−Dθ). Choose D so the exponent is negative, sum over
dyadic m, and include the final partial dyadic interval. Consequently
sup_n ||ρ_n||_r ≤ C_r. Doob’s maximal inequality now gives

    ||max_(1≤k≤K) ρ_k||_r ≤ r C_r/(r−1)                          (2)

uniformly in K. Each norm uses the same projective-limit measure.

[Integer spacing estimate](COLLISIONS.md).
[Tao, Proposition 1.14](https://arxiv.org/html/1909.03562v7#S1.SS4).

## Uniform choice of a nonperiodic odd predecessor

Fix the universal constants B₀,q and the favorable unit residue y of
Mazur Proposition 3.1. For 3∤a choose e in {1,2} making 2^e a≡1 mod 3.
The integers R_j=(2^(e+2j)a−1)/3 are positive odd predecessors of a
for j sufficiently large. The difference R_i−R_j has ternary valuation
v₃(i−j) for i≠j, by v₃(4^h−1)=1+v₃(h). Thus every block of 3^q
successive j visits every residue modulo 3^q. Start two such blocks at
a fixed j₀ large enough that R_j≥B₀ even for a=1. Two distinct choices
give favorable R_j in the two blocks. Both have the same odd successor,
the odd part of a. At most one can be on a cycle, since a periodic vertex
has a unique periodic predecessor. Choose a nonperiodic favorable one
R_a. Its exponent is bounded absolutely, so R_a ≤ C a for a universal C.

## Summing weighted path coverage

First take A finite and nonempty. For each R_a apply Mazur Proposition
3.1 with m=1 and a common real X sufficiently large for all targets.
It selects k_a≥1 with 3^k_a≤X, an integer J_a≥0, and exact words w
ending at R_a with sources x_w in [X,32X) and weights v_w satisfying

    2/3 ≤ sum_w v_w sum_(0≤j≤J_a) 4^(−j) ρ_(k_a)(Ψ_j(x_w)),
    0 ≤ v_w ≤ 3^length(w)/2^sum(w) ≤ R_a/X.

Here Ψ_j(x)=4^j x+(4^j−1)/3 permutes every ternary quotient. The last
weight inequality follows from the positive affine intercept. Exact
sources for fixed a are distinct, since two different lengths would give
a positive return of R_a. Sources for different a are disjoint because
a deterministic orbit meeting both targets orders them by reachability.

Write u_w=v_w/R_a, U=sum_w u_w, K=floor(log₃ X), M=max_(k≤K)ρ_k.
Every source carries at most 1/X. Every residue modulo 3^K occurs at
most 33X/3^K times below 32X. Hence for each j, across all chosen sources,

    sum_w u_w M(Ψ_j(x_w))^r ≤ 33 ||M||_r^r.

Divide each coverage inequality by R_a and sum over a. Extend j to all
nonnegative integers using positivity. Hölder, (2), and sum_j 4^(−j)=4/3
give

    (2/3) sum_a 1/R_a ≤ (4/3)·33^(1/r)·r C_r/(r−1)·U^(1−1/r).

At least XU distinct selected sources belong to the union of P(a)
below 32X. Now 1/R_a≥1/(Ca) and X may be any sufficiently large real,
so the lower density obeys (1). Finite subsets establish the assertion
for arbitrary A by monotonicity. In particular their harmonic sums have
a common upper bound since every ordinary density is at most one.

The individual a^(−2−ε) estimate and bounded nonperiodic seed choice are
also present in earlier work, and the later reciprocal bound gives a
stronger linear antichain inequality directly by disjointness. The
maximal-function argument above is an alternate derivation.

[Prior subquadratic regularity and predecessor bound](https://rstation.ai/problems/collatz/papers/9/v1).
[Prior reciprocal bound for all X≥a](https://rstation.ai/problems/collatz/papers/10/v1).
