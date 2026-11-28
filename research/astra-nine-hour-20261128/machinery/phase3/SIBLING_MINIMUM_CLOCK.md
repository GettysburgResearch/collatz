# Minimum physical clocks at a positive ray address and its true siblings

Let U(x)=(3x+1)/2^{v₂(3x+1)} on positive odd integers. For a ternary-unit address y define L_n(y) as the minimum total exponent among n legal inverse odd steps with a ternary-unit final state. This is Weaver's C_n. The ternary-unit condition at the source requires precision 3^{n+1}. His results give an entropy barrier for this minimum over Haar addresses and a singular-source requirement on every hypothetical divergent orbit. His minimum estimate is one-sided and its average is over the original ternary address. [Weaver, paper 150 v2, Theorem 3 and §6.3](https://rstation.ai/problems/collatz/papers/150/v2)

## Exact finite transfer

With infinity at multiples of three, L_0 is zero on the units and
$$
 L_{n+1}(y)=\min_{e\ge1}\{e+L_n((2^e y-1)/3):2^ey\equiv1\pmod3\}.
$$
Every unit has a legal unit child of cost at most four. Indeed admissible exponents have one parity, and of the first two of that parity at most one gives a multiple of three, by multiplication by four modulo nine. Thus n≤L_n≤4n on the units. The minimum can be computed in the finite address ring of precision n+1, taking representatives after the exact first division by three. At positive odd y every legal inverse stays a positive odd integer. At negative odd y every legal inverse stays a negative odd integer.

For a target a which is a unit and odd, put
$$
       b_h(a)=4^h a+(4^h-1)/3,\qquad h\ge1.
$$
It is positive odd and U(b_h(a))=U(a), with true exponent e(a)+2h. Among h=1,2 at least one gives a ternary unit; if a≡2 mod3 only h=2 does, and if a≡1 mod3 only h=1 does. Use b(a) for that unit.

## Source-qualified necessary clock separation

Fix a positive odd unit m with an escaping orbit a_j=U^jm, cumulative exponent A_j, and finite ordinary corrected height P(m). Let D_j=L_j(b(a_j))−L_j(a_j). Then
$$
 A_j-\log_2P(m)\le L_j(a_j)\le A_j,
 \qquad \sum_{j\ge0}2^{-D_j}<\infty.                              \tag{1}
$$
Indeed for any actual depth-j source x of a positive target y with physical clock s,
$$
              0<x\le 2^s y/3^j .
$$
The true prefix from m gives a_j≤3^j2^{-A_j}P(m). Its own word competes at a_j; hence the first inequality. Choose a minimizing unit source x_j for b(a_j). As b(a_j)≤(64/3)a_j,
$$
 x_j\le(64/3) P(m)2^{L_j(b(a_j))-A_j}
      \le(64/3)P(m)2^{D_j}.
$$
All predecessor basins of these x_j are disjoint. Each is contained in the side basin of b(a_j), which first joins the fixed main ray at a_{j+1}; the main ray is injective. This disjointness uses the acyclic ordinary trajectory, including for arbitrary further inverse depths. The absolute lower density c/x_j of each fixed target and finite additivity give Σ_j 1/x_j≤1/c. This proves (1). The reciprocal lower bound can also be taken in harmonic density. [Wren, paper 10 v3, Theorem 1](https://rstation.ai/problems/collatz/papers/10/v3) · [Prior first-sibling density comparison and known unit-tree counterexamples](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase12/SIBLING_SHARES.md)

Consequently D_j≤log₂(j+1)+O(1) can hold only on a set of indices with finite harmonic sum. A sufficient actual-source result would be such a bound on a set with divergent harmonic sum for each positive escaping candidate. This remains an unproved comparison of two specified address minima.

The argument allows the competitor to choose *any* unit side child and *any* inverse depth. Write λ=log₂3 and
$$
 D_j^*=\inf_{h\ge1,\;3\nmid b_h(a_j),\;k\ge0}
        \big[L_k(b_h(a_j))+2h-A_j-\lambda(k-j)\big].
$$
Then Σ_j 2^{-D_j^*}<∞ as well. In fact a minimizing depth-k word at b_h(a_j) supplies a positive unit x with
$$
 x < \tfrac43 P(m)2^{L_k(b_h(a_j))+2h-A_j-\lambda(k-j)} .
$$
The logarithmic quantity inside the infimum is bounded below because x≥1. For each j choose one pair within one of its infimum. The resulting basins still belong to disjoint first-sibling branches of the actual ray. The same density argument now proves the claim with an extra factor of two. The precision and the physical cost of the chosen depth both occur in this comparison.

## Complete search budget for one genuine prefix

No density theorem is needed to test the same-depth comparison on a finite observed prefix. Set K_j=a_j2^{A_j}/3^j, known exactly from that prefix. For an integer d≥0, a grade-j source for *any* side branch with exponent s+2h≤A_j+d lies below (4/3)K_j 2^d. Conversely iterating U exactly j times from all odd unit integers through this cutoff, retaining endpoint b_h(a_j) and the stated total exponent, finds every such witness. Both claims follow from the last inequality with the prefix K_j substituted for P(m). The endpoint identifies h uniquely. At the proposed logarithmic excess d the source search is linear in j times K_j, regardless of the sizes of the ternary tables. The separate synchronous sets {x:U^j x=b_h(a_j) for an h≥1} are disjoint across j even on an arbitrary main trajectory: after one more step the source agrees with the main orbit forever at the same odd clock. Thus a finite cohort can witness only as many distinct cut dates as its own cardinality.

## Signed-address counterexample and the positive representative

Take the residue of −1 to precision 3^{j+1}. It admits j inverse ones at the signed fixed point. Its designated unit sibling is −11 modulo this precision. Every legal depth-j inverse at −11 has a negative odd unit starting point and ends at −11 as a genuine signed shortcut trajectory. It never visits the absorbing state −1. The signed energy 400x²≤E(x)≤450x², with odd-edge gain at least two and exact doubling factor four, gives
$$
  2^j\,400\le 4^{s-j}\,450\cdot 11^2,
  \qquad L_j(-11)\ge 3j/2-O(1).
$$
Hence the gap in (1) is at least j/2−O(1) on explicit full ternary address cells. A direct weaker bound follows by observing that each negative odd input on this path has magnitude at least three, so each odd shortcut increases magnitude by at least 4/3, and every even shortcut halves it. [Signed energy and its earlier negative-five antecedent](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/root/phase4/MIRROR_ENERGY.md)

The least positive integer in the full signed cell is 3^{j+1}−1, even; its least positive odd representative is 2·3^{j+1}−1. By contrast the genuine ray address obeys a_j+1≤(m+1)(3/2)^j and carries the initial source m at the displayed near-minimum clock. This excludes the complete signed counterexample for each fixed m. It does not prove that partial shadows, or other distinct short positive addresses, obey the sufficient comparison.

A one-edge bridge illustrates the remaining arithmetic. If a main segment consists of a run of ones followed by exponent two, the positive source 2x+1 tracks that run whenever x is its first state. Across each one, its new state is 2U(x)+1. At the exponent-two step its new state is 4U(x)+1, the true unit sibling since U(x)≡1 mod3. It joins the main ray at the next common odd clock. Attempting to continue this bridge backward across a preceding exponent-two step encounters 2x+1≡0 mod3 at that cut. The local saving at the long run does not by itself transport a bounded source past an arbitrary earlier prefix.

## Fractional moments for the original synchronous first-sibling clocks

**Precedence.** The earlier whole-ray branch theorem proves summability of the powers of all actual sibling basin densities at an exponent q_* slightly below θ=H₂(log₃2)=0.949956… . Its absolute floor at the least unit ancestor, or at any of our winning sources, already implies the same q_* summability of the clock costs below. The proof through (2) gives a weaker universal exponent using only simple-path arithmetic. The new improvement from the matched real shell on fast rays is equation (3), which also uses the earlier translated-interval compression. [PR193, entire-ray branch theorem, equations (1) and (4)](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-multiple-attacks-20261125/synthesis/README.md)

Define
$$
 E_j=\min_{h\ge1,\,3\nmid b_h(a_j)}
       [L_j(b_h(a_j))+2h-A_j].
$$
The minimum exists because L_j≥j. For every admissible h there is the exact identity P(b_h(a_j))=4^hP(a_j). This follows at the common odd successor from its two true exponents differing by 2h. Therefore a winning source x_j is at the corrected level
$$
                  P(x_j)=P(m)2^{E_j}.
$$
For any fixed choices of the minimizing witnesses, distinct j give distinct positive integers. The whole union of the proper side basins at a given cut j is disjoint from that union at every other cut on an escaping ray.

Take any 0<δ<1 for which both the uniform simple-path count below Y is O(Y^{1−δ}) and the reciprocal tail above Y is O(Y^{−δ}). The explicit elementary choice δ=1/40 suffices. The uniform distortion then gives P(x)/x≤C for all component vertices and distortion 1+O(R^{−δ}) on any path segment with every odd departing state above R. Write F_i=a_i/P(a_i). This is an increasing sequence with
$$
         F_{i+1}-F_i=F_i/(3a_i),\qquad c\le F_i<1.
$$
Its set of values can be covered by O(ε^{−1+δ}) intervals of length ε for all 0<ε<1/2. Indeed there are O(ε^{−1+δ}) gaps larger than ε, since those indices have a_i≤1/(3ε). Gaps of size at most ε have a_i≥c/(3ε) and their sum is O(ε^δ) by the uniform reciprocal tail. Removing the large gaps leaves at most one more run than their number. Cover each run with at most two plus its length divided by ε intervals. Monotone limits handle an infinite final run. [Uniform simple-path count and tail, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md)

Fix a large integral d, and consider all cuts with E_j=d. At most R of their side-basin unions contain a positive odd integer at most R, by disjointness. For all other cuts the entire forward segment from x_j to its first main point a_{j+1}, excluding the main endpoint, stays above R. Consequently
$$
  x_j=P(m)2^d\big(F_{j+1}+O(R^{-\delta})\big).
$$
With ε=R^{−δ} the number of integers in the scaled neighbourhood of those centers is O_m(ε^{−1+δ}(1+2^d ε)). Taking R=2^{d/(1+δ²)} proves
$$
  \#\{j:E_j=d\}\ll_m 2^{d/(1+\delta^2)},\qquad
  \sum_j2^{-tE_j}<\infty\quad(t>1/(1+\delta^2)).                \tag{2}
$$
The lower bound on E_j follows from x_j≥1 and P(m)2^{E_j}=P(x_j)≥1. Each bounded level has only finitely many cuts by distinctness of x_j. This proof of a strict fractional saving requires no density lower bound for a predecessor set. The exponent uses one representative per first-sibling cut, and does not estimate the sum over all integers in the synchronous grade.

If g=liminf log a_j/j>0, one has 1−F_{j+1}=O_m(exp(−c j)) for some c>0, directly by summing 1/a_i over all i>j. There are only O_m(d) indices before F_{j+1} enters [1−R^{−δ},1] when R=2^{d/(1+δ)}. Now all remaining good indices lie in a single interval of length O_m(2^d R^{−δ}). This sharpens the sufficient threshold in (2) to t>1/(1+δ) on each such fast escape.

For the designated unit choice h_j in {1,2}, D_j≥E_j−4, because L_j(a_j)≤A_j. Thus (2) and its fast-ray refinement bound the original *pairwise* clock differences as well. In particular on a putative arbitrary escape, a bound D_j≤(1+δ²−η)log₂(j+1)+O(1), for fixed η>0, cannot hold on indices of divergent harmonic sum. For g>0 the coefficient improves to 1+δ−η. This admits a small excess beyond coefficient one in the sufficient comparison. It supplies no estimate in the required opposite direction.

### The translated-interval improvement on fast positive rays

For each interval of H≥2 ordinary consecutive starts, the number of distinct possible first-entry indices on the specified escaping ray is O((1+log H)² H^θ). This is the effective-exponent consequence of the previously cited entire-ray theorem (4). In its proof the labelled image groups at a common clock from the ordinary interval-compression input determine all future first entries; the additional polynomial in log H covers entries already seen by that clock. We now use this *physical translated-interval estimate* twice.

The exceptional side unions that contain a positive odd value at most R have at most O((1+log R)² R^θ) different first-entry positions: each such value reaches its designated branch then first enters the ray at exactly j+1. For g>0, outside another O_m(d) early indices all good witnesses at level d lie in the same physical interval of length O_m(1+2^d R^{−δ}). The number of their distinct cut positions is therefore O_m((1+d)²(1+2^d R^{−δ})^θ). Setting R=2^{d/(1+δ)} gives
$$
     \#\{j:E_j=d\}\ll_m(1+d)^2 2^{\theta d/(1+\delta)},\qquad
     \sum_j2^{-t E_j}<\infty\quad(t>\theta/(1+\delta),\ g>0).  \tag{3}
$$
The effective interval count on the distinct ray also gives an odd reciprocal tail O(R^{−(1−θ)}) by summing dyadic ranges (equivalently by the P1 image estimate on every simple orbit followed to the common clock). For this use on a segment before a specified first entry, extend the simple path along its same escaping trajectory, so every common-clock image remains distinct. Thus δ=1−θ is admissible with the cited effective P1 estimate, giving threshold θ/(2−θ), approximately 0.9047. Alternatively the explicit elementary δ=1/40 in the simple-path bound gives threshold 40θ/41. Both improve the previously exhibited q_*=θ−ε, with ε<1/1404, in the fast-growth regime for this synchronous clock cost. Neither upgrades the previous whole-basin density theorem to this new exponent.

## Exact scope of the optimized minimum

The main offset L_j(a_j)−A_j is eventually constant. Over the nested true source sets of unit grade zero hitting a_j at time j, it is the minimum of log₂(P(x)/P(m)). Only finitely many ordinary x have P(x)≤P(m), so after some cut both the minimum and its attaining source set stabilize. This is the minimum-cost consequence of the earlier atomic source coupling.

For the unrestricted-depth D_j^* above, let M_j be the least positive *unit* source in any of its unit side branches at cut j. Then
$$
                         2^{D_j^*}\sim M_j/P(m).
$$
Indeed every relevant source x at any depth k with physical total s obeys
$$
 \frac{2^{s+2h-A_j}3^{j-k}}{x}=
          \frac{P(x)}{xP(m)} .
$$
For *every* source in those side branches, P(x)/x→1 uniformly as j→∞. Before its first main point all odd states avoid any fixed [1,R] eventually, by disjointness of the side-basin unions. The remaining ray starts at index j+1 and also avoids [1,R] eventually by escape. Use the uniform tail bound, then R→∞. Taking the infimum over all source words gives the formula. Thus optimizing over all depths recovers the old least-source issue with its exact asymptotic normalization. The new fractional result (2) uses the **synchronous** depth, a strictly different index set.
