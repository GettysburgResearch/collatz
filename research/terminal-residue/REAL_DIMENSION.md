# The terminal Collatz residue has no atoms and has full lower Hausdorff dimension

**Proposed, using the cited first-landing estimate, power-saving timed descent, and orbit packing.** Let m(n) be the smallest positive value ever visited from n. Let R(n) be the sum of log₂(1+1/(3u)) over all odd inputs u strictly before the first visit to m(n) under the shortcut Collatz map. The terminal pair (m,R) has a limiting natural law by Leen. On the basin m=1, R is the binary logarithm of Roosendaal's multiplicative residue.

For every Borel set E⊂ℝ of Hausdorff dimension <1 and every sequence of real centers a_t,

    Pr(R−a_m ∈ E) = 0.                                                   (1)

This holds, in particular, under the conditional law given any minimum of positive limiting probability. The corresponding terminal law on the basin of 1 gives no mass to any point, positive or zero. Its lower Hausdorff dimension is one. There also exist c,C>0 such that, uniformly over centers a_t and 0<r<1,

    Pr(|R−a_m|≤r) ≤ C r^c.                                               (2)

The two estimates measure different kinds of concentration. Estimate (2) has a uniform exponent for the full measure. To obtain exponents arbitrarily close to one in (1), the proof first restricts to sets of typical landing histories.

Leen's stopping-time histogram paper explicitly asks whether the terminal residue on the basin of 1 has atoms at positive values. It records that the atom at zero vanishes and reports a numerical correlation-dimension estimate near one. His Brownian theorem supplies existence of the terminal law used here. His question about absolute continuity is addressed in the [separate singularity argument](SINGULAR_FIBRES.md). [Leen, histogram theorem and open problems](https://doi.org/10.5281/zenodo.23252397) · [Leen, Brownian motion in Collatz orbits, terminal law](https://doi.org/10.5281/zenodo.23252395)

## Inputs at one height

Use U for the odd Syracuse map. From an odd source let Y_B be its first odd iterate ≤B, including the initial value if eligible and using ∞ if it never enters. For all uniform odd sources in (X/4,X] with X≥4B, paper 102 gives the following bounds for any set A of odd labels:

    Pr(Y_B∈A) ≤ exp(O(√log B)) (|A|/B+B^(−g)),
    Pr(Y_B=∞) ≤ exp(O(√log B)) B^(−g),

where g>0. Multiplicative absolute constants are understood. These bounds carry over to any weak limiting source law as X→∞. For a uniform source on [1,X] first strip its initial power of two, which changes neither the minimum nor R. Conditional on this power the odd core is uniform on an odd initial interval. Splitting it into geometric octaves gives the same upper bound in the limit; the bounded lower remainder and the tails of the initial two-adic valuation have vanishing or arbitrarily small probability. [First-landing bounds, paper 102 v1, Theorem 1](https://rstation.ai/problems/collatz/papers/102/v1)

Fix any 0<β<1. Apart from O_β(B^(1−η)) integers y≤B, for some η=η(β)>0, y reaches a shortcut value z≤B^β in at most C_β log B shortcut steps. We always choose the first such z. This follows by applying the timed power-saving descent theorem at the fixed source power β. The state z may be even. Also, there exist absolute κ>0 and C such that the sum of log₂(1+1/(3u)) over any simple pre-minimum odd segment all of whose values exceed B is ≤CB^(−κ). Indeed polynomial orbit packing in [Y,2Y] with exponent <1 bounds its reciprocal sum on each dyadic shell, and the geometric series converges. The segment before the first minimum is simple by determinism. [Timed power-saving descent and comparison to Inselmann](../native-pressure-20261118/README.md) · [Orbit packing and the published antecedents](../critical-orbit-mellin/PRIOR_WORK.md)

Write τ(y),J(y) for the shortcut clock and odd count to the first global minimum. Telescoping gives

    R(y)=τ(y)−(log₂3)J(y)−log₂(y/m(y)).                                (3)

For a label having the timed descent just described, m(y)=m(z). All states before z exceed B^β. Writing i,j for the prefix clock and odd count, the expression R(y)−a_{m(y)} is therefore

    i−(log₂3)j + τ(z)−(log₂3)J(z) + log₂ m(z)−a_{m(z)} − log₂ y.         (4)

For all y≤B there are only O_β(B^β(1+log B)²) possibilities for the part of (4) preceding −log₂ y, among labels having timed descent. No bound on the clocks from z to its own minimum is needed. An interval of length l≤1 for log₂ y contains O(1+B l) integers y≤B. The constants in this counting step do not depend on the centers.

## Uniform small-ball estimate

On Y_B=y<∞, the global minimum and all subsequent visits are those of y, and 0≤R(n)−R(y)≤CB^(−κ). Choose any fixed β<min(κ,1) and B a power of two comparable to r^(−1/κ). To have |R(n)−a_m|≤r, the landing label either fails timed descent or satisfies (4) in an interval of length O(B^(−κ)). For the direct count decrease κ below one if necessary. The total admissible number of labels is

    O_β(B^(1−η)+B^β(1+log B)² (1+B^(1−κ))).

Apply the setwise landing estimate and include its failure atom. Since β<κ, all contributions decay by a positive power of B after absorbing the subpower loss. This proves (2), also after projection onto any minimum cell and normalizing by its positive mass.

## Typical landing histories at all large dyadic heights

Pass along a subsequence to a joint limiting law of (m,R) and all coordinates Y_k=Y_(2^k). Each label coordinate takes finitely many values (including ∞). The minimum is tight and R is bounded by orbit packing on simple segments. Thus such a joint law exists, and its terminal marginal is the previously established one. Equivalently one can form a subsequential limit from any sequence of ordinary source cutoffs. Finite-coordinate consistencies carry over: if Y_k and Y_l are finite, l>k, then the latter runs forward to the former on its first entry at 2^k; m=m(Y_k), and |R−R(Y_k)|≤C2^(−κk). These inequalities and identities pass to every limiting law by restricting to the finite landing labels. The translated center depending on m causes no issue since m has the discrete topology.

Fix ε,β>0 smaller than one. With probability one all sufficiently large k satisfy the following three properties:

1. Y_k is finite.
2. Its *unconditional* point mass in the limiting Y_k law is ≤2^(−(1−ε)k).
3. From Y_k the first shortcut entrance at or below 2^(βk) takes at most C_β k steps.

Indeed there are at most 2^((1−ε)k) finite labels whose masses exceed the bound in item 2. The setwise landing estimate bounds their total mass by exp(O(√k))(2^(−εk)+2^(−gk)). For item 3 use the O(2^((1−η)k)) bad labels and the same estimate. These errors and the failure probabilities are summable over k. The first Borel–Cantelli lemma suffices and uses no independence.

For large l on such a history the count of odd inputs between Y_l and Y_(l−1) is at most C_β l+1. If Y_l≤2^(l−1) the two labels coincide. Otherwise all odd inputs before the next lower-octave landing exceed 2^(l−1). The first shortcut value ≤2^(βl) occurs in at most C_β l steps and is already below the lower octave. If it is even, stripping its remaining doublings to the next odd state introduces no extra odd inputs. Thus

    0 ≤ R(Y_l)−R(Y_(l−1)) ≪_β l 2^(−l).

The universal packing remainder shows R(Y_l)→R. Telescoping the octave bounds improves the correction along each such history to

    0 ≤ R−R(Y_k) ≪_β k 2^(−k)                                          (5)

for all k after the common onset of properties 1–3. The constant is uniform over histories once that onset is fixed.

## Interval masses on the restricted sets

Restrict the joint measure to histories on which properties 1–3 hold for every k≥K; increase K as necessary for 2^(βk)≤2^(k−1). For any interval I of length 2^(−k), event R−a_m∈I requires (4) at Y_k in an interval of length O_β((1+k)2^(−k)) by (5). At B=2^k the counting argument leaves O_β(2^(βk)(1+k)³) possible values for Y_k. Each has unconditional probability at most 2^(−(1−ε)k) by property 2. This bounds the projected restricted mass of I by

    O_β((1+k)³ 2^(−(1−ε−β)k)).

Comparing arbitrary interval lengths with the next larger dyadic length gives a Frostman upper bound of every exponent below 1−ε−β for the restricted measure. Intervals covering a Borel set of smaller Hausdorff dimension therefore show its restricted measure is zero. Let K tend to infinity, then choose ε and β arbitrarily small. This proves (1). Applied to the binary logarithm of the residue or to its exponentiation on its bounded range, the Hausdorff-dimension conclusions agree by bi-Lipschitz change of variables.
