# A computable diffuse rank off a fixed sparse physical reset section

**Status.** Proposed constructive theorem for ordinary inputs. No assumption about the basin of 1 or a distribution of later orbit states is needed. Every positive odd input has a uniformly bounded (in path horizon) finite source potential. Its uniform debit holds off one specified decidable set of relative natural density zero. The debit on all marked returns remains open. The phase selection is adapted from PR 197, `research/ayh-resource-reset-20261124/continuation/GROWING_HEAD.md` at `9ed095c3b3386d66c1dba103117e8dda0268b7aa`. The simpler selector here requires only the qualitative covering argument, proved below; it uses no merger estimate and no asymptotic cutoff to run.

## A total selector with decidable image

For n≥1 put D=⌊log₂ n⌋ and H=min(⌊√D⌋,⌊D/2⌋). For t≥0 let

    W_t = ⋃_{m≥0} [7·3^m,(7+3^{−t})3^m).

Examine the actual states x_j=T^j(n), 0≤j≤H. Among integer t from 0 to D for which some x_j lies in W_t choose the largest, then the least eligible j at that t. Output x_j. If none qualify, output n. Every step uses finite integer comparisons, including membership in W_t. Since j≤D/2 and each shortcut sends an input to at least half its value, every output x satisfies x≥n/2^j≥√n. Therefore membership in the image S is decidable at x by evaluating the selector on the finite interval 1≤n≤x². No unknown small exceptions are required in this algorithm. In particular 1 belongs to S.

For every fixed t all sufficiently large sources have an output in W_t. In the circle coordinate log₃ n modulo one, the ideal multiplicative clock advances by −log₃2 regardless of parity. Irrationality follows by prime factorization. The translates of the projected open interval (7+3^{−t}/4,7+3^{−t}/2) by nonnegative powers of this rotation cover the circle, hence finitely many initial clocks suffice, say at most K_t. The actual multiplicative correction through any of those clocks is a product of factors 1+1/(3T^i(n)) at odd inputs. Every T^i(n)≥n/2^{K_t}; the product tends to one uniformly for those finitely many clocks as n→∞. The interior interval has a fixed positive margin inside W_t, the scale 3^m becomes large, and eventually H≥K_t and D≥t. Thus some eligible actual hit exists; the greatest depth selected is at least t, and nestedness gives an output in W_t.

For each fixed t the number of positive ordinary members of W_t up to X is O(3^{−t}X+log(2+X)), with absolute constants, by summing interval lengths 3^{m−t} and rounding errors. The outputs of the finitely many smaller sources are a finite set. Thus S itself (the **image**, not a set of input exceptions) has upper natural density at most O(3^{−t}) for every t, hence density zero.

## The marked odd valleys still have density zero

For a positive odd y write a=v₂(y+1)≥1 and b=v₂(3^a((y+1)/2^a)−1)≥1. Its next valley is z=T^{a+b}(y). Mark y if some T^j(y) belongs to S for 0≤j<a+b, and call the resulting odd set M. The rule is finite and decidable. The half-open interval attributes a hit at a valley endpoint to the following source. All positive odd sources reach M: the guaranteed selected hit happens within H(y) actual steps and the containing valley starts no later. In particular 1 belongs to M.

For fixed j, the positive preimage (T^j)^{-1}(S) has density zero. The at most 2^j parity words give injective affine maps separately on their source classes, and inputs ≤X have endpoints ≤(3/2)^j(X+1). For a fixed K only the finite union over j<K matters except at valleys of length >K. On the uniform odd residue classes a given pair (a,b) has relative asymptotic frequency 2^{−a−b}. Indeed the inverse valley prescription chooses one odd residue modulo 2^{a+b+1}, as the terminal odd 2-adic input ranges over all odd values. Equivalently, the starting run a has probability 2^{−a} and its odd cofactor is uniform odd, giving the same conditional b law. For K≥1 the event a+b>K is recognizable from a finite parity prefix (or by summing the complementary finitely many pairs), and its relative density is

    Σ_{r>K}(r−1)2^{−r} = (K+1)/2^K.

It follows by first taking the upper density in y and then K→∞ that M has relative natural density zero among the positive odd integers.

## An actual finite proper rank and its diffuse realization

From each odd y follow its physical valley orbit to the first marked source u. Let τ be the full shortcut clock expended before reaching u (zero if y itself is marked), and set F(y)=τ+u. This is finite and computable on **every** positive odd source because τ≤H(y). It also gives the independent horizon-uniform bound

    F(y) ≤ H(y)+(3/2)^{H(y)}(y+1).

Conversely F(y)≤R implies τ≤R, u≤R and y≤2^τ u≤2^R R, so F is proper with an explicit finite sublevel search. For every unmarked y, including a hypothetical nonconvergent one, the next valley satisfies the exact identity F(y)=a+b+F(z). This is a statement on the physical orbit, with no replacement jump.

Apply the interpolation construction in DIFFUSE_RANK.md with any 0<ε<1 and arbitrary positive mass bound η. A single finite singular continuous μ then satisfies F≤H_μ≤F+ε on **all** positive odd inputs, and H_μ(y)−H_μ(z)≥2−ε on **all** edges from unmarked y. The L¹-density alternative works also. These choices can be effective: F-sublevels can be exhaustively searched up to 2^R R and the geometric error/mass budgets can be prescribed in advance. In the Haar version, each previous finite potential is locally constant at a computable depth; in the singular version the fair-bit base has the explicit uniform tail Σ_{m>M}2^{−ceil(m/2)}, supplying a modulus for the earlier finite sum. One can choose rational spike masses (at rationally evaluated ordinary centers the base potential is computable; for this specific base it is rational at each ordinary or dyadic-rational argument, since binary digits are eventually constant) and computably large depths. At any fixed ordinary input its stage is computable; once processed, every later contribution is bounded by the summable predetermined leakage. Thus the limiting potential at each such input is computable at arbitrary precision.

There is a concrete failure if the marks are ignored. The selector outputs 7 on input 7, since it lies exactly on a left endpoint at time zero. It outputs 13 on input 13, since its only tested states 13 and 20 lie outside W_0. Both are marked; hence F(7)=7 and F(13)=13. The ordinary (3,1) valley 7→13 increases the actually interpolated potential too, since ε<1. Long time between resets cannot be replaced by a uniform debit at a reset.

More precisely, on the induced actual first-return map of M the terminal values satisfy F(s)=s. A later marked return w<s implies H_μ(s)−H_μ(w)≥1−ε. Every positive orbit reaches M and repeatedly returns to it, so a proof that every marked s>1 has some later marked return below s would finish by ordinary induction (1 is marked). This remaining assertion is about actual repeated visits to the same sparse section. Its natural density, the source bound for F, and the size of μ supply no such return estimate.
