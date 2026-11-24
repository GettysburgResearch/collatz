# The central least-source target and an exact shifted-moment test

**Collatz remains open.** The universal target is a meeting with a smaller ordinary source, required only under the original induction floor. A direct inverse-word calculation converts the entire conjecture, including positive cycles, to vanishing of one explicitly defined negative moment of independent geometric gaps. The conversion does not prove its vanishing. A hypothetical single surviving source contributes a fixed positive amount through just one word per depth, even when that word has exponentially small sampling probability.

## The quantified floor

Let U be the positive odd map and call x good if an iterate is one. The following statement is equivalent to universal convergence:

> For each odd x>1, if all smaller positive odds are good, there exist a positive odd y<x and clocks a,b≥0 such that U^a(x)=U^b(y).

Necessity uses y=1. Sufficiency is strong induction: the common future inherits convergence because U(1)=1. There is no bound on the clocks, restriction on the initial word, synchronized-time assumption, or requirement that x itself visit a smaller value. The generic equivalence was checked in Std Lean for any map fixing one, restricted to odd initial inputs. The existence assertion on its right remains unproved for U. The word “least” throughout refers to this fixed original floor, even when a comparison is constructed at a later height.

## A single independent-word criterion including cycles

Fix any real s>1, for example s=3/2. Draw N independent positive integers e₁,…,e_N with

    P(e=j)=(2^s−1)2^(−s j), j≥1.

Set E_i=sum_{j≤i}e_j, E=E_N, C=sum_{j=0}^{N−1}3^{N−1−j}2^{E_j}, and c=C/2^E. For the resulting word w, choose y_w to be the unique odd integer in [1,2·3^N) satisfying

    2^E y_w ≡ C modulo 3^N.

The law and observable below use only the sampled word and integer arithmetic, with no undefined infinite trajectory. Put a_s=3^s/(2^s−1), and

    Z_N(s)=a_s^N E[ 1_{y_w>1} (y_w−c)^(−s) ].

Then the exact limiting identity is

    lim Z_N(s) = Σ_{x positive odd, x never reaches 1} x^(−s).       (1)

In particular, liminf Z_N(s)=0 for any *one* s>1 is necessary and sufficient for full Collatz. The least positive odd nonconverger f, if one exists, gives lim Z_N(s)≥f^(−s).

**Proof.** The affine equation for a word from x to y is 2^E y=3^N x+C. Conversely, any odd positive y in the indicated congruence gives a positive odd integer inverse path with the prescribed gaps. Indeed, writing C=3C_prev+2^{E_{N−1}} proves 2^{e_N}y−1 divisible by three. Its quotient is positive and odd, and the congruence with the previous carry follows after dividing by three. Repeat. The oddness of each forward endpoint enforces the exact valuation. In particular x_w=(2^E y_w−C)/3^N is a positive odd integer, y_w>c, and x_w<2^{E+1}. The other odd endpoints are y_w+2k·3^N for k≥1, with original sources x_w+2k·2^E. These are all positive ordinary sources of this word.

Sum x^(−s) over each word and each such endpoint except y=1. Since P(w)=(2^s−1)^N 2^(−sE), the sum equals the expectation of a_s^N times the sum of (y−c)^(−s) over the allowed lifts of y. Only the least lift contributes Z_N. All remaining lifts together cost at most

    a_s^N Σ_{k≥1}(2k·3^N)^(−s)=2^(−s)ζ(s)(2^s−1)^(−N).

The full sum is exactly Σ_{x:U^N(x)≠1} x^(−s). Its domains decrease because 1 is absorbing, and the total initial mass is finite. Passing to the limit proves (1). A positive cycle disjoint from one retains its entire starting-source mass in this test.

## Attempts to prove vanishing

**Removing the real shift loses the cycle obstruction.** If one instead keeps all endpoints and replaces y−c by y, summing the lifts gives

    F_N(s)=Σ_x x^(−s) ∏_{i<N}(1+1/(3U^i x))^(−s).

This decreases to positive mass precisely if some orbit is nonperiodic: along a periodic positive tail the product tends to zero, whereas every injective ordinary odd orbit has finite reciprocal sum by the orbit-packing bound. For each fixed endpoint y its unnormalized inverse transfer contribution tends to zero as well. For a nonperiodic y, the inverse depths are disjoint and their contributions sum to at most y^s ζ(s) by positivity. For a periodic y, dominated convergence over original sources applies, since a source visiting it infinitely many times has infinite correction sum. Fixed-y decay does not control mass moving to growing y.

**Average ternary contraction.** Each word selects one residue modulo 3^N. Averaging the unshifted unrestricted inverse transfer over all residue classes therefore gives exactly

    [3^(s−1)/(2^s−1)]^N.

This contracts for 1<s<2 (the strictly concave function ln(2^s−1) lies above its chord joining s=1 and s=2). The endpoint weights in (1) are concentrated near the word's own real carry. Averaging over independent uniform residues would change that joint statistic. For the unshifted statistic alone, even ideal pointwise uniformity through γN ternary digits would supply an exponential estimate by the straightforward mass bound only when 3^γ>a_s. Ordinary total-variation errors in an estimate of this type are multiplied by a_s^N. Fixed-scale equidistribution and unspecified o(1) errors do not suffice.

There is a stronger elementary obstruction to full pointwise uniformity: all-one gaps lead to residue −1 by evaluating the word on its negative fixed point. This one word already has probability (1−2^(−s))^N. Its least positive odd endpoint is 2·3^N−1, so the relevant one-sided small-positive-endpoint problem is strictly finer than the maximum residue probability. At s=3/2 the independent gap law has mean 2^s/(2^s−1)≈1.547 and entropy s E[e] ln 2−ln(2^s−1)≈1.005 nats, below ln 3. Near s=1 its entropy instead exceeds ln 3, but then its mean exceeds log₂3. High positive surviving paths can occupy a large-deviation set of words under this tilt. The prescribed-modulus conclusions of PR188 concern the empirical law of a particular actual source and do not control these rare inverse-word coincidences. [PR188, AR1–AR6](https://github.com/GettysburgResearch/collatz/blob/f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d/research/astra-global-step-20261124/AUXILIARY_RESIDUES.md)

**The exact cost of the one missing word.** For a fixed odd x and all N with 2^{N+1}>x, the word selected by its actual first N gaps has x_w=x and y_w=U^N x, since x is already the least positive lift in its dyadic cylinder. If y_w>1, its individual contribution is exactly

    a_s^N P(w) (y_w−c)^(−s)=x^(−s).

Its probability is at most (1−2^(−s))^N. Thus even an exponentially small exceptional event can contain a fixed nonvanishing contribution at every depth. This is not an assertion that any source survives. The uniform bound Σ_{w:x_w>K}x_w^(−s)≤Σ_{x>K}x^(−s) follows because different words at the same depth have different least sources. It identifies the exact hard locus: bounded positive dyadic source residue, a terminal value y_w≠1, and closeness to the *same word's* real carry. Bulk results on typical residues alone cannot discard that locus. The elementary test above makes no use of a purported quantitative local mixing theorem for these rare events.

## The unrestricted corrected clocks

PR193 assigns corrected heights M(z)>z on each synchronous class of an injective component. Their ratios on a class are powers of two and M(Uz)=3M(z)/2^{v₂(3z+1)}. At late indices let M_i be its least corrected unit height and write ell(y)=log₂(M(y)/M_{i+1}) for its nonnegative integer excess on the next class. Taking the full inverse minimum, with b(y) the least valuation of an odd ternary-unit predecessor of y, gives the *equality*

    a_i = min_{y in next class, y a unit} [ b(y)+ell(y) ].

Indeed every possible predecessor is in the preceding class, and every unit in that class appears among these edges. The minimum is attained. The bound b≤4 means only excess levels 0 through 3 can win, but the minimizer need not be on excess level zero. Advice to follow just one minimum therefore does not furnish a new ordinary edge.

A separate attempt sums over every unit rather than discarding nonoptimal branches. Weight a state y by M(y)^(−s) and let the transfer on test functions be

    Lw(y)=Σ_{e : x=(2^e y−1)/3 is a positive odd ternary unit} (3/2^e)^s w(x).

The total weighted test mass on level i equals the mass of Lw on level i+1, exactly. Any positive bounded w with Lw≤w on every positive ordinary ternary unit would therefore exclude escape: positive forward-level masses would be nondecreasing, while their sum is finite by distinctness of all the ordinary states and M(y)>y. Such a certificate by itself does not exclude an alternate positive cycle.

A nonzero continuous nonnegative ternary-residue certificate of this kind is impossible. Extend to the compact ternary unit group by continuity (positive odd integer units are dense and the transfer series converges uniformly for bounded w). At −1 its e=1 self-predecessor has weight (3/2)^s>1, forcing w(−1)=0. Every unit predecessor of −1 must also have weight zero. Those predecessors are dense: for any unit residue r modulo 3^k choose e so 2^e≡−(3r+1) modulo 3^{k+1}, possible since 2 is primitive there. Then (−2^e−1)/3≡r modulo 3^k. This obstructs a continuous residue-only supersolution, not a positive-domain certificate with height dependence.

The natural Green candidate G(y)=Σ_{h≥0} L^h 1(y) satisfies LG=G−1 and is finite pointwise on a nonperiodic ordinary component: disjoint ancestor depths and positivity give G(y)≤y^s ζ(s). Yet along the original orbit it contains the contribution from the fixed original ancestor q₀, of size (M(q_i)/M(q₀))^s. Its weighted mass is therefore not summable across forward levels. This is the specific failure of the Green construction. The periodic and finite-window optimality examples in PR193 also show why arbitrary bounded-depth checking cannot be silently extended to the entire corrected word. [PR193, full synchronous classes](https://github.com/GettysburgResearch/collatz/blob/d35bdfd9d0c75effda50bbb8040c136482431e24/research/astra-global-synthesis-20261124/section/proof.md)

**Formal coverage.** The accompanying Lean file checks the strong-induction meeting equivalence and the affine propagation of paired source/endpoint lifts. The shifted negative-moment formula and the analytic attempts above are written arguments. No local estimate establishing (1)'s vanishing, full termination proof, or nonstandard-cycle exclusion has been found.
