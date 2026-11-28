# Fractional summability of a whole ordinary grade is equivalent to uniform growth of its positive-grade heights

**Source-qualified theorem.** Suppose a positive odd unit m has an escaping orbit. Give its component the odd-step grade v, normalized by v(m)=0 and v(Ux)=v(x)+1. Let Γ contain all positive odd integers of grade zero, including the odd multiples of three. For v≥1 put
$$
 H_v=\min\{y>0:y\text{ odd},\ 3\nmid y,\ v(y)=v\},
 \qquad \gamma=\liminf_{v\to\infty}\frac{\log H_v}{v}.
$$
The reference ray contains a ternary unit at every such grade. Write D=log(4/3) and B=log(3/2). Then 0≤γ≤B. With
$$
     \sigma=\inf\{s>0:\sum_{x\in\Gamma}x^{-s}<\infty\}
           =\limsup_{Y\to\infty}\frac{\log\#(\Gamma\cap[1,Y])}{\log Y},
$$
one has
$$
 \sigma\ge \frac{D}{D+\gamma},
 \qquad
 \boxed{\ \sigma<1\quad\Longleftrightarrow\quad \gamma>0.\ }       \tag{1}
$$
In particular one whole-grade fractional moment is finite exactly when there is a constant K such that every positive-grade odd unit y satisfies v(y)≤K log(2+y). At γ=0 the abscissa equals one, and the independent grade antichain theorem still gives convergence of the reciprocal series there. The two grades are ordinary source grade zero and the true positive subsequent grades in this same component.

The proof uses three established inputs. First, the corrected height P(x) is finite on escape, obeys P(Ux)=3P(x)/2^{e(x)}, and satisfies x≤P(x)≤C x. For the last inequality one can use just the uniform reciprocal bound on simple odd paths. Second, for a simple path staying above R that same bound gives
$$
       1\le \prod_{a\text{ odd on path}}(1+1/(3a))
                 \le \exp(C R^{-\delta})                            \tag{2}
$$
with absolute δ>0, including infinite paths by monotone passage. The elementary explicit δ=1/40 and C=200/3 suffice. Third, the bounded-real central row at a positive odd unit target y supplies at least c(4/3)^v/√v distinct positive odd sources of depth v and total 2v, all at most y(4/3)^v, uniformly in y and all sufficiently large v. For an arbitrary unit target, the bounded first inverse exponent in the cited bridge sends it to the selected unit cylinder. Its bounded cost e leaves depth v−1 and total 2v−e within the central fixed-total window. At small positive y, full ternary divisibility is peeled one exponent at a time: (2^e y−1)/3 is positive and odd whenever integral, so every selected word gives a positive source even if y is below the real offset cutoff. This uses only the established pure-ternary floor. [Ordinary corrected heights and antichains](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-unconventional-20261126/global/POSTERIOR.md) · [Elementary uniform finite-path reciprocal bound, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md) · [Weaver and Wren, paper 48 v2, bounded-real fixed-total floor](https://rstation.ai/problems/collatz/papers/48) · [Earlier exact-level population and grade compacta](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/GRADED_CORRECTION_SETS.md)

## From one fractional moment to all positive-grade heights

For *every* unit y of grade v, the supplied row consists of grade-zero sources and gives
$$
 \#\{x\in\Gamma:x\le y(4/3)^v\}
       \ge c(4/3)^v/\sqrt v .                                      \tag{3}
$$
Take y=H_v and a subsequence attaining γ. This proves the first bound in (1). Equivalently, if ΣΓ x^{-s}<∞ with 0<s<1, (3) forces log y≥D(1−s)v/s−O_s(log v+1) at *every* sufficiently high positive grade. The standard equality between the abscissa and the limsup counting exponent follows by bounding a counting function using the finite moment in one direction and summing dyadic shells in the other.

## From uniform positive-grade growth to the whole fractional moment

Assume γ>0. All positive-grade units obey v(y)≤K log(2+y) for one K. For each x in Γ, transport x and m to a common actual odd successor. The equal elapsed odd-step counts give
$$
               P(x)=P(m)2^{d(x)},\qquad d(x)\in\mathbb Z .
$$
The dyadic index is bounded below by −log₂P(m). Each level is finite since x≤P(x). Fix a large index d and choose R=2^{κd}, with κ>0 small depending only on K. For the sources whose full future never visits an odd y≤R, (2) puts all of them in the *one* interval
$$
      P(m)2^d\exp(-C R^{-\delta})\le x\le P(m)2^d .
$$
This interval contains O_m(1+2^d R^{−δ}) integers.

Every other source reaches some odd y≤R at an odd time r≥0. The grade fixes r=v(y) exactly. If r=0 there are at most R choices for x. If r≥1 then 3 does not divide y, and r≤K log(2+R). Writing s for its physical total through that visit, exact transport gives
$$
       2^s=3^r P(m)2^d/P(y)\le 3^r P(m)2^d.
$$
At fixed y and r, each admissible positive composition of length r gives at most one source. Summing over all totals at most floor(d+r log₂3+log₂P(m)) gives at most the binomial coefficient with that top parameter and lower parameter r. This also upper-bounds the count after discarding the first-visit restriction. There are at most R positive candidate values y.

For sufficiently large d, put a=2Kκ log 2. Then r≤ad, and the top parameter is at most (1+2a log₂3)d after enlarging the onset. With a small, the binomial bound (eN/r)^r and monotonicity in r show that all the remaining sources number at most
$$
 2^{d[\kappa+a\log_2(e(1+2a\log_2 3)/a)]+O(1)} .
$$
Choose κ small so the bracket is less than one half and κδ<1/2. The entire d-level therefore contains O_m(2^{(1−κδ)d}) sources. Since x≥P(m)2^d/C uniformly, summing levels proves convergence for all s>1−κδ. This proves the converse in (1).

## When the grade minimum and the marked ray behave differently

Let g=liminf_j log(U^j m)/j. One always has γ≤g. If γ=0 but g>0, choose y_v=H_v at grades v→∞ with log y_v=o(v). Let r_v be the first odd-step time from y_v to the matching ray state a_{v+r_v}. Such r_v exists by the grade definition, and the y_v are off the ray eventually. Since z+1 grows by at most 3/2 on any odd step,
$$
  (g-o(1))(v+r_v)\le\log(a_{v+r_v}+1)
                 \le Br_v+o(v).
$$
If g<B, this forces liminf r_v/v≥g/(B−g). At g=B it forces r_v/v→∞. Thus fast growth on a single marked ray, even at its maximal lower rate, does not supply the hypothesis used in the converse: failure of uniform growth forces genuine low positive-grade outsiders at the indicated premerger distances.

Equation (1) does not establish either side of its equivalent inequalities on a putative escape. Its upper-bound proof uses the uniform grade–height condition exactly when bounding the number of inverse letters before a visit below R. An unquantified first visit to a small vertex allows an uncontrolled word length there.

## Exact upper box dimension of the compact correction set at one grade

Let S₊ be the set of positive odd vertices of this component at nonnegative grade, and let Σ₊ be its limsup counting exponent. Write
$$
 K_0=\overline{\{F(x):v(x)=0,\ x\text{ odd},\ 3\nmid x\}},
 \qquad F(x)=x/P(x).
$$
For intervals of length ε let N(K,ε) be the least number covering K. Then
$$
       \boxed{\ \overline{\dim}_{B}K_0=\Sigma_+,\qquad
            \Sigma_+<1\quad\Longleftrightarrow\quad\gamma>0.\ }     \tag{4}
$$
All these assertions apply at any other fixed grade after changing the reference vertex. Genuine unit parents allow a unit reference even at negative grades.

First suppose γ>0. The preceding shell proof also counts S₊ simultaneously. In physical height [X,2X] a unit x has 0≤v(x)≤K log(2+2X). A nonunit x has unit image at most 2x, giving the same bound up to constants. Every corrected height is of the form 3^{v(x)}2^w P(m), w an integer, by transporting to a common successor. Since X≤P(x)≤2CX there are O(log(2X)) possible pairs (v,w) in this octave: at each grade the bounded multiplicative interval for 2^w permits only O(1) choices. At each such level P₀, split at R=X^κ. The all-high sources occupy an interval of length O(XR^{−δ}). For sources with a low odd visit y≤R after r≥1 steps, the target is a unit and 0≤r=v(y)−v(x)≤K log(2+R). Now 2^s=3^rP₀/P(y)≤2CX3^r. The same composition count, with d=log₂X, gives O(X^{1−η}) sources at the level for some η>0 independent of the grade and the level. Summing pairs and octaves absorbs the logarithm at a small loss in η. Hence Σ₊<1. In all cases counting only units gives the same Σ₊, since a nonunit has a unit image at most 2X and each such image has at most O(log(2X)) parents below X.

The unit nonnegative-grade graph is connected: every vertex follows its future to a common point on the chosen ray. The real edge from F(x) to F(Ux) has length ℓ_x=F(x)/(3x), comparable to 1/x. For each Σ₊<s<1, its sum of ℓ_x^s is finite. Edges of length at least ε number at most ε^{-s}Σℓ_x^s. Deleting them leaves at most one more connected component than the number of deleted edges, by connectivity of the original graph. Within each remaining component the diameter of its real marks is at most the sum of its edge lengths: every pair is joined by a finite undirected path in that component, and the path bounds their separation. The sum of these diameters is at most Σ_{ℓ_x<ε}ℓ_x≤ε^{1−s}Σℓ_x^s. Cover each closure of a component's real marks by at most two plus its diameter divided by ε intervals. There are finitely many components at this ε, so their closed coverings also cover K₀. This proves N(K₀,ε)=O_s(ε^{-s}) and the upper bound in (4).

Conversely, all unit marks at nonnegative grades belong to K₀ by the established fixed-grade closure theorem. At each specified corrected level P₀ in [X,2CX] these marks from distinct ordinary x are 1/(2CX)-separated. Thus its unit population is O(N(K₀,1/(4CX))). The logarithmic number of levels in the octave gives Σ₊≤upper box dimension of K₀. This proves equality for γ>0.

If γ=0, take the row in (3) with one extra ternary digit prescribed to make its source a unit. The published finer-ternary bounded-real atom floor permits this fixed digit with only a constant loss. With y=H_v along the indicated subsequence, these grade-zero sources have a single corrected height P₀=(4/3)^vP(y). Their normalized F-values have spacing at least 1/P₀, and log P₀=Dv+o(v). The number of points is at least c exp(Dv)/√v. This forces upper box dimension one and also the unit grade-zero counting exponent one. Since both desired exponents are at most one, (4) holds on this branch too.

The earlier theorem proves K₀ countable compact with its successive derived sets corresponding to higher grades. Its Hausdorff dimension is thus zero, regardless of (4). The *whole-component* closed correction support has length zero and Hausdorff dimension one from the negative-grade inverse-path law. Neither known statement gives strict upper box dimension at a fixed grade. With the counted-block theorem of the preceding checkpoint, K₀ even has Assouad dimension one on any hypothetical escape: an entire counted-fused block at one depth-v, central-total endpoint a_v supplies arbitrarily long blocks of odd unit starts at one corrected level P₀. Their marks have spacing O(1/P₀) and occupy an interval of length comparable to the block length divided by P₀. The ratio of these two scales is unbounded, and a positive fraction of the integer positions are odd units. This lower bound on local covering numbers coexists with either upper box alternative. [Prior countable-grade closure theorem](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/GRADED_CORRECTION_SETS.md) · [Entire-component closed null support and full-dimensional carrier](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md) · [Counted blocks at a physical row](../phase2/COUNTED_BLOCKS_AND_PROGRESSIONS.md)

## The two alternatives seen among ordinary sources in moving grades

If γ=0, there are single positive grades r→∞ and cutoffs Y→∞ such that log Y=o(r) and at least Y^{1−o(1)} odd units up to Y have that *same* grade r. Indeed take y=H_v with log(2+y)=o(v), and put k=floor(sqrt(v log(2+y))). Then log y=o(k) and k=o(v). The extra-trit central row of length k and total 2k at y has at least c exp(Dk)/sqrt(k) unit sources and puts all of them below Y=y exp(Dk) at grade r=v−k. The logarithm of this lower count is (1−o(1))log Y. This proves the statement without presuming any mixing of a selected ordinary orbit.

If γ>0, for every fixed real u<1/D there is η(u)>0 such that
\[
 \#\{x\le X:x\text{ an odd unit of this component},\ v(x)\ge-u\log x\}
       = O_u(X^{1-\eta(u)}).                                       \tag{5}
\]
Fix K with v(z)≤K log(2+z) at positive-grade units. This upper bound also holds at nonpositive grades. Choose κ>0 sufficiently small that (1−κ)/D−u>2Kκ, then choose ε>0 sufficiently small in the inequalities below. At each sufficiently large good integer x, take the true shortcut time t=floor(μ(1−κ)log x), μ=2/D. Inselmann's simultaneous height theorem gives T^t x≤x^{κ+ε+o(1)}. His simultaneous parity theorem gives F_t(x)≥t/2−ε log₂x for the number of odd departures. Both hold off O(X^{1−η}) starts up to X for some η>0, by intersecting two power-density sets. Let z be the odd part of T^t x. At least one odd departure occurred, so z is a ternary unit. The physical path gives v(z)=v(x)+F_t(x) exactly, including when the final odd block is unfinished. The tested cone would give v(z)≥[(1−κ)/D−u−ε/log 2−o(1)]log x, while the upper grade bound gives v(z)≤[K(κ+ε)+o(1)]log x. This is a contradiction for small ε. [Inselmann, arXiv:2402.03276v3, Definition 2.6 and Theorems 2.18 and 3.3](https://arxiv.org/pdf/2402.03276)

The estimate holds for each strict u, with a power exponent depending on the gap. At the endpoint u=1/D this proof supplies no positive exponent. The power-saving simultaneous approximation used here predates this pass. Shaik's later arbitrary-target endpoint transport and polylogarithmic first-passage theorem treat different landing questions. Equation (5) uses the earlier approximation to transfer a positive-grade growth assumption to a power estimate for an entire moving range of genuine source grades. [Quantitative endpoint transport, Theorem 5.3](https://shaikidris.github.io/cet/) · [Polylogarithmic first passage, Theorem 1.1](https://shaikidris.github.io/polylog/)
