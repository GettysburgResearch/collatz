# Counting actual critical-section ancestors of one fixed target

**PROPOSED written theorem.** For the shortcut Collatz map, write `A(b)` for all positive integers whose forward orbits contain the *same fixed* positive integer b. Let B be the eight-excess marked section of PR 197, frozen at `2fb1f11c959e35eba875338833d84969222dc089`. For every b coprime to three,
$$
 \limsup_{X\to\infty}\frac{\log(1+\#(B\cap A(b)\cap[1,X]))}{\log X}
 \ \ge\ \frac{52(0.84)}{(5/4)(52+3-\log_2 3)}>0.654 .
$$
Consequently, if E is **any** set of upper counting exponent strictly below the displayed threshold, convergence on B outside E is equivalent to convergence on all positive integers. This permits deleting even an infinite, arithmetically unstructured exceptional subset. The analogous bound exceeds 0.701 on the stronger source-qualified predecessor exponent 0.901. Universal convergence remains OPEN.

## A common-scale proof with the vendored four-clock inverse

This first construction gives the weaker threshold 0.629753… (0.675485… for the stronger external input). The twelve-class policy below sharpens the same argument to the headline result.

Let G=16/3 and let Q tend to infinity along denominators of convergents a/Q to the irrational α=log₂3. Thus a and Q are coprime and |α−a/Q|≤1/Q². Put Y=2^(36Q). The following construction works **simultaneously** for every integer q with Q²≤q≤Y and 3∤q. All constants in its error estimates are absolute. Binary logarithms in what follows measure height, while ln is the natural logarithm.

Take the six-branch four-clock inverse L of PR 197's vendored `ShellCover.lean`. For yₛ=Lˢ(q), its checked bounds are
$$
 T^{4s}(y_s)=q,\quad 3\nmid y_s,\quad
 G^s(q-1)+1\le y_s\le G^s q.
$$
For s≥1, its explicit six residue formulas give yₛ mod 16 in {4,8,10,5}; hence yₛ=2ʰuₛ with uₛ odd and h≤3. The first h clocks are physical halvings, so T^(4s−h)(uₛ)=q. Uniformly for 1≤s≤Q one has log₂ yₛ=log₂ q+s log₂ G+O(1/Q²), and uₛ≥q/8.

For any sufficiently large odd unit u, choose the unique exact-surplus candidate n from its fiber, provisionally ignoring the mark. The odd predecessors are nₑ=(2ᵉu−1)/3, starting at e=1 or 2 and then increasing e by two. Their next odd value is u. Since nₑ₊₂=4nₑ+1, floor(log₂ nₑ) rises by exactly two and the surplus 5e−(floor(log₂ nₑ)+1) rises by eight. Its starting value is negative for large u, which gives exactly one e having surplus in {0,…,7}. For this candidate,
$$
 n\le C u^{5/4},\qquad C=(2^{8/5}/3)^{5/4}.
$$
Indeed 2ᵉ≤2^(8/5)n^(1/5) and 2ᵉu=3n+1≥3n. Apply this choice to each uₛ, writing nₛ for the result. Then, modulo integers, log₂ nₛ equals log₂(q/3)−sα up to O(Q⁻²). Here the two additional factors are the exact integer shift e−h and the ratio 1−1/(2ᵉuₛ), whose logarithm is O(Q⁻²).

The Q transfer phases s=1,…,Q have a one-sided mesh of length at most 2/Q. To see it, replace sα by sa/Q. The resulting phases form a translated complete grid. The signed perturbations −s(α−a/Q) all lie in a *single* interval [l,l+1/Q], since their pairwise differences have magnitude ≤1/Q. Given any real t, choose a grid value modulo one in [t−l,t−l+1/Q]; its true phase has a representative in [t,t+2/Q]. Take t=K/Q² with K greater than an absolute bound on the phase errors of the actual nₛ. Some nₛ therefore has fractional binary logarithm δ∈[0,2/Q+O(Q⁻²)].

Its bit length d+1 satisfies d+1≤D Q+O(1) for D=(5/4)(36+log₂ G)<49, by the bound on n and yₛ≤G^QY. Thus
$$
 (d+1)(n_s/2^d-1)=(d+1)(2^\delta-1)
 \le 2D\ln2+o(1)<70 .
$$
The last strict inequality also follows from D<49 and ln2<0.7. This nₛ is in B. It reaches its own odd endpoint u, which reaches the **original** q in at most 4Q further clocks. In particular nₛ≤X_Q:=C(G^Q Y)^(5/4). Once nₛ has been fixed, its odd endpoint is unique. At most 4Q+1 distinct q can occur as its selected target, since all must be drawn from u,T(u),…,T^(4Q)(u). No independence assumption enters this multiplicity estimate.

## Feeding the inverse basin through the row

Suppose |A(b)∩[1,Z]|≥c_b Z^α₀ for all large Z, where α₀>0 and c_b>0. The imported lower bound counts all starts. Enough of them give *unit* targets for the row. For each x≤Y/2 in A(b), take q=x if 3∤x. Otherwise write x=2ʲm with m odd and put q=(3m+1)/2≤Y. Every state up through m is a multiple of three and q is a unit, so b occurs at q or later. For fixed q there is at most one possible m, and at most 1+log₂ Y choices of j in this second case. Including the identity case, we obtain ≫_b Y^α₀/(1+log Y) distinct q in A(b)∩[1,Y]. Dropping q<Q² costs at most Q². Applying the common row and its clock multiplicity now yields
$$
 \#(B\cap A(b)\cap[1,X_Q])\gg_b\frac{2^{36\alpha_0Q}}{Q^2}.
$$
Since log₂ X_Q=DQ+O(1), the exponent 36α₀/D follows. The limsup is deliberate: this argument never bounds gaps between consecutive favourable denominators. It works separately for every fixed positive unit b, including periodic targets.

Krasikov and Lagarias, *Bounds for the 3x+1 problem using difference inequalities*, Theorem 6.1, gives α₀=0.84 for this map and every such b. The paper's computer-assisted linear-program proof is used as a published input; no new replay of that calculation is claimed. [Author's paper](https://websites.umich.edu/lagarias/doc/krasikov.pdf). For α₀=0.901 the input is the repository's separate source-qualified import, with its target-dependent constant and cutoff. [Frozen import status](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/external/mazur-2026/predecessor-x090.md).

For the deletion conclusion, suppose some positive integer fails to hit one. Its orbit contains a positive ternary unit b, by halving to an odd state and taking its next odd-input step if necessary. Every element of A(b) also fails to hit one, since one is on the closed cycle 1,2. The bound forces B∩A(b) to have an element outside E, contradicting convergence there. Equivalently, any actual set of nonconvergent B members either is empty or has upper counting exponent at least the threshold. This strengthens the earlier unboundedness alternatives.


## The improved threshold from a variable-cost inverse policy

The twelve-class policy below was supplied by the companion critical-compression analysis. Each listed exponent e is the ordinary accelerated inverse Iₑ(y)=(2ᵉy−1)/3, an odd source that reaches y in e shortcut clocks. The argument permits y to be even on the first application. Subsequent outputs are odd ternary units.

| Input classes | Exponents, in order |
| --- | --- |
| 1,4 modulo 9 | 2 |
| 2,8 modulo 9 | 1 |
| 5 modulo 9 | 3 |
| 7,16 modulo 27 | 4,2 |
| 25,52 modulo 81 | 6,1,2 |
| 79 modulo 243 | 4,6,1,1 |
| 160,241 modulo 243 | 4,4,2,1 |

For a word of length r the modulus is 3^(r+1). Adding a multiple of that modulus to the input changes the value after i inverses by an integer multiple of 2^(e₁+…+eᵢ)3^(r+1−i). All divisibility, parity and unit tests therefore hold on the full cylinder once checked on its positive residue. All e are positive and every legal Iₑ at a positive unit has positive output. The twelve residues partition the units modulo 243. Every full word has total cost at most 3r. At every intermediate prefix of length i its cost is at most 3i+4. The independent exact routine `verify_inverse_cost.py` checks the twelve-cylinder partition against all 162 unit residues, each intermediate ordinary division, and both cost bounds. Concatenating full words and then a partial word gives total clocks Aₛ≤3s+4 **at every** inverse-odd index s.

Take infinitely many convergents a/Q of α=log₂3 satisfying |α−a/Q|≤1/(2Q²). For two consecutive convergents on opposite sides of α, the sum of the two absolute errors is exactly 1/(QQ′). Both cannot be at least 1/(2Q²), 1/(2Q′²) respectively, as the sum of those two bounds exceeds 1/(QQ′) when Q≠Q′. With Y=2^(52Q), apply the concatenated policy simultaneously to unit targets 2^Q≤q≤Y. The lower cutoff discards only 2^Q points, negligible for either predecessor exponent here (more generally require 52α₀>1).

Write u₀=q and uᵢ=Iₑᵢ(uᵢ₋₁). Because uᵢ+1≥(2/3)(uᵢ₋₁+1), all values through the first Q inverse steps are at least (4/3)^Q−1. The factors 1−1/(2ᵉⁱuᵢ₋₁) in the product formula for uₛ therefore have total binary-logarithmic error O(Q(3/4)^Q)=o(Q⁻²), uniformly. The binary logarithm of uₛ equals log₂q+Aₛ−sα up to that error. Also uₛ≤2^(Aₛ)q/3ˢ≤16·2^((3−α)Q)Y. These are already odd endpoints for s≥1. Use the same unique exact-surplus predecessor nₛ as above, adding only an integer shift to its phase relative to uₛ/3, with exponentially small error.

The one-sided rotation mesh is now at most (3/2)/Q: the signed perturbation interval has width at most 1/(2Q). Using the same positive margin of order Q⁻², some nₛ has nonnegative fractional logarithm at most 1.5/Q+O(Q⁻²). Its bit length is at most D′Q+O(1), where D′=(5/4)(52+3−log₂3)=66.768796874…. The mark holds because 1.5 D′ ln2 <70 (already D′<67 and ln2<0.694 suffice). Thus nₛ∈B, its endpoint uₛ reaches the original q in Aₛ≤3Q+4 physical clocks, and nₛ≤X′_Q=C(16·2^((3−α)Q)Y)^(5/4). A selected B source accounts for at most 3Q+5 targets. The same unit conversion and finite multiplicity proof give ≫_b 2^(52α₀Q)/Q² B ancestors up to X′_Q, hence the exponent 52α₀/D′. Its values are 0.654197799645… and 0.701705020810… for 0.84 and 0.901, respectively. These are sufficient thresholds without an optimality claim.

## What the argument can and cannot couple

One can use the proved inequality with a bound on the number of B starts that survive above one fixed verified floor forever. A source that visits an uncertified number smaller than itself is still a potential survivor. Likewise a small count of inputs lacking a smaller same-component B partner does not bound the number of nonconvergent starts. Formally, a directed rooted tree with one bad root can give each other vertex a smaller partner in its own bad component, however many vertices lie in the tree. Applied to Collatz, a genuine transfer estimate would have to control the full set that can flow into the remaining bad roots, or route below the particular original target b. A bound only on the failure set of a one-step merger is insufficient even if that set is finite.

At a reset the comparison retains the source and odd endpoint separately; multiplying separate one-step success rates would drop the source dependence. For a countable deterministic smaller-partner selector F on its successful domain, write μ_X for counting measure on B∩[1,X], and P for pushforward on successful inputs (killing unsuccessful inputs). Every positive source decreases in the ordinary order while the selector runs. Its terminal failure distribution is **exactly** the sum over j≥0 of (Pʲμ_X) restricted to failed inputs, with successful terminal bases retained separately or treated as failures of known convergence. A bound on μ_X of the failure set controls only the j=0 term. A size reduction by a fixed factor or power bounds the number of terms; it places no bound on their transported masses. The first unsupported step is a fixed-floor estimate or effective multiplicity control on those actual terminal fibers. The trivial bound for all B is X^(4/5+o(1)), above both thresholds.

## Formal scope

`BasinCounting.lean` proves the lift's mod-16 assertion, the remaining physical clocks after stripping the first halvings, the finite joint cardinality inequality, and the deletion witness at one finite scale. The rotation asymptotics, candidate selection, unit-basin conversion, external lower bound and final limiting corollary above are written mathematics. The module imports the frozen `CriticalSection` suite. Replay with Lean 4.34.1, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, and the built PR 197 imports on LEAN_PATH, using `lean -j1 -DautoImplicit=false -DwarningAsError=true BasinCounting.lean`.

## Joint consequence for the bounded-time ternary head

The separate checked `TernaryHeadDescent.head_or_small` theorem supplies a stronger count for its different section H. Here H is the union of [7·3ᵏ,8·3ᵏ) over k≥4. Every positive source reaches H or a value below 600 within at most ten shortcut clocks. For each fixed unit b, every ordinary inverse-basin lower bound |A(b)∩[1,X]|≥c_b X^α₀ therefore gives

$$
\#(H\cap A(b)\cap[1,X])\ \gg_b\ X^{\alpha_0}
$$

for **all** sufficiently large X. Indeed take n∈A(b) larger than 2¹⁰ max(600,b). Every Tʲn for 0≤j≤10 is at least n/2ʲ>max(600,b). The selected head occurs strictly before n reaches b. Write x for the head; then x+1≤(3/2)¹⁰(n+1), since 2(Ty+1)≤3(y+1) at every step. Every value has at most two one-step predecessors, namely the even one and at most one odd one. Summing 2ʲ for j=0,…,10 shows that any x has at most 2047 selected ancestors n. Apply the original result up to (say) X/120 and discard the finite small set. The selected heads lie below X for large X.

Thus any E with |E∩[1,X]|=o(X^0.84) can be discarded when testing **convergence** on H, with exponent 0.901 available if using the source-qualified input above. More sharply, it suffices to have small-o along a single unbounded sequence of X, because the lower bound holds for all large X. The B theorem above only guarantees its lower bound along its constructed scales and requires an appropriate upper bound on those same scales. The head estimate does not establish that testing only the **truncation mergers** x with floor(x/81) outside E suffices: on a hypothetical nonconvergent basin many successful local mergers can feed an exceptional failed one. An estimate on *actual nonconvergent* H members or fixed-floor survivors would complete the convergence argument.

The **growing-head image** in the companion `GROWING_HEAD.md` is simultaneously of natural density zero and robust for this convergence test up to counting exponent α₀. Let J consist of the actual selected head values, and let h(X) be the maximum allowed clock over starts up to X, including the bounded fallback. Its schedule gives h(X)=o(log X) and n/2^h(n) tends to infinity. In forming J use the physical selection before testing any merger, so a successful comparison is not a condition for membership. To bound |J∩A(b)∩[1,X]|, use all b-ancestors up to Z=floor(X/(2(3/2)^h(X))). Then Z=X^(1−o(1)), and the growth inequality puts every selected hit below X for sufficiently large X. Discard finitely many small starts: every remaining selected hit precedes b since all sampled orbit states exceed b by the lower bound n/2^h(n). Each head accounts for at most 2^(h(X)+1) earlier starts. Consequently for every sufficiently large X,

$$
  \#(J\cap A(b)\cap[1,X])\ \ge\ X^{\alpha_0-o(1)}.
$$

In particular, convergence on J outside any set of upper counting exponent <α₀ is equivalent to universal convergence, with α₀=0.84 available from the published theorem. This uses only the deterministic hitting, clock and density-zero conclusions of the growing schedule. It is independent of its source-qualified merger-density estimate. Once again these are counts of actual fixed-target ancestors, not of failed local comparisons.
