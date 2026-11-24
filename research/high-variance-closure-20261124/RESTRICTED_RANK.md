# An actual increase of the restricted inverse-tree envelope

**Scope.** Written proofs and exact finite Python certificates, proposed for independent review. The ordinary shortcut map is T(x)=(3x+1)/2 at odd x and x/2 at even x. Odd/even on odd-denominator rationals means the numerator parity in reduced terms. Positive odd valley sources y traverse a consecutive run of a odd, then b even, shortcut inputs to z. Thus P=3^a, Q=2^{a+b}, C=P−2^a, and Qz=Py+C. Use the complete inverse valley tree R of −5, including the root. The inverse branch is F(z)=(Qz−C)/P. This addresses GLOBAL_RANK.md at PR182 checkpoint f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67. PR 197 was inspected at 9ed095c3b3386d66c1dba103117e8dda0268b7aa; its merger and counting theorems are not inputs.

Every center is −h/q below −1 in lowest terms with q a power of three. Every intermediate rational shortcut state also stays below −1: under the specified odd steps the image of a real x<−1 remains below −1, and the subsequent halvings end at a center below −1. At the root the (2,1) branch is a cycle. The exponentiated envelope is

    E(n) = sup_{−h/q in R} 2^v₂(qn+h) / h.

## Uniform tail bound for one fixed ordinary source

Fix positive odd n and put x_k=T^k(n), s_k=number of odd inputs in the first k steps, and
B_k=2^k(x_k+1)/3^{s_k}−n. We have B_0=1. At odd inputs B is unchanged; at even inputs it increases by 2^k/3^{s_k}. If v₂(qn+h)≥k, then n and −h/q follow the same first k shortcut decisions: a common parity step subtracts exactly one from their difference valuation. Their terminal real separation is 3^{s_k}(n+h/q)/2^k. Since the negative endpoint is below −1, we obtain

    h/q > B_k,      2^v₂(qn+h)/h ≤ 1+nq/h < 1+n/B_k.

The same upper bound applies uniformly over all agreement depths ≥k. This estimates the whole infinite inverse tree. For a target threshold t>1, all remaining candidates of agreement depth k below a chosen cutoff satisfy

    q=3^j < h ≤ 2^k/t,      h = 2^k d − nq,      d odd.

For fixed k,q there is at most one possible d, namely floor(nq/2^k)+1. Filter gcd(h,q)=1. Membership need not be decidable in general. A concrete rational reaching −5 is a member if all prior shortcut states stay below −1: starting from odd, valley grouping reaches the −5 cycle, and hence a valley occurrence of −5. A rational entering [−1,∞) or repeating before −5 is excluded. The finite checks below classify all their candidates explicitly.

## A strict increase of the supremum itself

There is a single ordinary (5,1) valley 31→121. After 30 shortcuts from 31 we have x=319 and s=21. Hence B_30=19326434387/10460353203 and 1+31/B_30<18. For k<30 the candidate enumeration at t=18 is empty. In fact d≤(31+1)/18<2, hence d=1, and no (k,j) in this finite box has 3^j<2^k−31·3^j≤2^k/18. Consequently E(31)≤18. At 121 the center −7=F_{1,1}(−5) gives 128/7>18. This disproves descent on individual valleys for the fully optimized envelope, including every inverse-tree center.

The sharper exact values, obtained with the same tail lemma and finite checks, are

| n | E(n) | Maximizing center | Cutoff | Arithmetic candidates | Tree members among candidates |
|---|---:|---:|---:|---:|---:|
| 1 | 8/7 | −7 | 10 | 11 | 1 |
| 31 | 4294967296/291622243 | −291622243/129140163 | 53 | 2 | 1 |
| 121 | 67108864/2804503 | −2804503/531441 | 49 | 3 | 2 |

Run `python -B checks/rank_certificate.py` from this packet directory. `lean/EnvelopeCertificate.lean` separately proves the strict comparison of the two real suprema for the operational definition of a center: a reduced odd rational with power-of-three denominator whose negative shortcut trajectory stays below −1 until it hits −5. Its general matched-prefix transfer, explicit finite box and root cycle are included. An inverse-tree center has this property by its defining valley branches. Conversely a qualifying odd rational groups its shortcuts into full valleys; if its arrival at −5 is internal to a valley it subsequently returns to −5 as an actual valley endpoint by the −5 cycle. Thus this operational definition gives exactly the written tree. The exact maximizing fractions in the table are checked by Python, and the real-density and interpolation arguments are written proofs. No unclassified candidate or computational assertion about all negative integers is used. A decrease on a selected later return remains open. A bounded real-valued envelope with merely strict pointwise decreases need not be well-founded.

## What the real cutoff sees at all depths

In the extended half-line [1,∞], let S(n) consist of limits of |r_j| along centers with v₂(n−r_j)→∞, always for this one n. Then

    S(n) = [B_∞(n),∞],     B_∞(n) = lim_k B_k(n).

Here [∞,∞] is the singleton {∞}. The lower inclusion constraint follows from the tail bound above. To prove every value above the cutoff occurs, the first generation of the tree has real magnitudes

    |F_{a,b}(−5)| = 1 + (5·2^b−1)(2/3)^a.

These are dense in (1,∞): for any target 1+u with u>0 choose unbounded a and integers b with b−a log₂(3/2)→log₂(u/5), by irrational rotation (irrationality follows from prime factorization). Then b eventually is positive. The subtracted (2/3)^a tends to zero. For a full actual valley prefix of clock k the inverse of the common affine map transports the entire magnitude interval (1,∞) onto (B_k,∞), since |F_w(−v)|=B_k+2^k(v−1)/3^{s_k}. These centers agree with n for at least k bits. Take increasingly long full valley prefixes; every positive ordinary orbit has infinitely many of them, since an infinite run of all odd would require n=−1 and a positive run of halvings always ends. Density lets one approach any specified finite limit ≥B_∞, including the boundary from above, or choose images tending to infinity.

In fact n+B_k is multiplied by 1+1/(x_k+1) on each even input and unchanged on odd inputs. Therefore B_∞ is finite exactly when the sum of 1/(x_k+1) over even inputs converges. A bounded-real sequence of arbitrarily precise centers is equivalent to this summability condition and certifies that the fixed ordinary orbit tends to infinity. Indeed an orbit failing to tend to infinity repeats an integer, giving a periodic tail with at least one even input and divergent reciprocal sum. The converse for **all** escaping orbits follows using a separate written input. PR 182, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md` at `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, proves a strict-power upper counting bound on the positive odd states of any one injective forward orbit. Dyadic shell summation gives Σ_i 1/q_i<∞ for its successive odd states q_i, as also used in PR 192, `research/astra-closure-attack-20261124/FIXED_SOURCE.md` §1 at `d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`. Each block of even states immediately before an odd state q_i is 2^e q_i,...,2q_i; the sum of their reciprocals is less than 1/q_i. Thus the even shortcut reciprocal sum converges for every escaping orbit. With that source-qualified counting input, finite B_∞, existence of one bounded-real sequence of centers converging dyadically to this same fixed n, and actual escape to infinity are all equivalent. No existence of such a tower for a positive source has been shown. Both eventual arrival at 1 and a hypothetical nontrivial positive cycle have B_∞=∞. The criterion is about the full set of centers with unweighted dyadic agreement; it does not characterize the height-weighted supremum by itself.

### A prescribed antipode and a finite positive test

There is a stronger source-qualified normalization. For a hypothetical escaping odd input n, write q_i for its odd states and A_i for the shortcut times at those odd states. The complete odd affine identity gives

    2^{A_i} q_i / 3^i = n ∏_{j<i}(1+1/(3q_j)).

Since q_i→∞, the left side tends to n+B_∞, using the preceding finite B_∞ result. The distinct-state product estimate of PR 182, `research/astra-round13-20261124/CYCLE_BUDGET.md` at `9b02334f27ff59694a91fe7f018e0aaabad7620b`, uses the published positive convergence floor and the explicit sum bound 17/50 to give ∏(1+1/(3q_j))<117/83 uniformly over all finite initial arcs (the strict upper bound on the full correction sum also gives a strict bound on the limiting product). Its domain applies because an escaping positive orbit is injective and lies entirely above the verified convergence floor. Thus B_∞<34n/83<n. Consequently, with these written inputs,

* a positive odd n escapes iff there are centers converging to **n in the dyadic metric and −n on the real line**;
* a positive odd n is eventually periodic iff for some k, 2^k(T^k(n)+1)>2n·3^{s_k}.

For periodic or preperiodic inputs B_∞=∞. For escaping inputs the product estimate makes the latter strict inequality impossible. The single finite prefix test for eventual periodicity does not distinguish a nontrivial cycle from the standard one. It supplies no proof that every n passes the test.

### Quantitative construction at both places

On positive real magnitudes the two inverse branches G_{2,1}(v)=(8v+5)/9 and G_{3,1}(v)=(16v+19)/27 cover the interval I=[19/11,5] between their fixed points: their images are [23/11,5] and [19/11,11/3]. For every u∈I recursively choose a branch with image containing u and take its inverse, which stays in I. Replacing that residual after t choices by 5 makes an absolute error at most |I|(8/9)^t. Reversing those chosen branches from the root produces a genuine rational inverse-tree center.

Take an escaping n and late actual full-valley clock k. To target real magnitude n after the actual inverse prefix, the required terminal magnitude is v=1+(n−B_k)3^{s_k}/2^k. This tends to infinity because n−B_k stays bounded away from zero while T^k(n)→∞ and (2^k/3^{s_k})(T^k(n)+1)=n+B_k. For all sufficiently large k choose b≥1 and u∈I with v=G_{1,b}(u)=(2^{b+1}u+1)/3. Such a b exists since the ratio of interval endpoints is 55/19>2, covering all sufficiently large magnitudes. Replace u by its t-branch approximation, apply G_{1,b}, and then pull back through the actual prefix. For every t≥0 the resulting center r=−h/q satisfies

    v₂(n−r) ≥ k,      ||r|−n| ≤ 4n(8/9)^t,      q ≤ 3^{s_k+1+3t}.

For the middle estimate the rescaling slope is (v−1/3)/u≤v/(19/11); the actual inverse prefix then multiplies by 2^k/3^{s_k}. The product (2^k/3^{s_k})v = n−B_k+2^k/3^{s_k} ≤ 2n, since B_k<n and T^k(n)≥1. The constant 2|I|/(19/11)=72/19 is below four. The denominator estimate counts odd steps; reductions can only lower it. Taking t=k gives simultaneous positive powers of convergence relative to denominator, while both approximations refer to the same fixed source.

One precise obstruction is the finite-place Subspace Theorem, in the form cited in PR 192 FIXED_SOURCE.md §2. For fixed n>0 and any δ>0, only finitely many distinct reduced centers with h/q near n can satisfy

    |h−nq| · 2^{−v₂(h+nq)} < q^{−δ}.

Indeed use the primitive integer vector (q,h), the forms q,h−nq at infinity, q,h+nq at 2, and q,h at 3. Their determinants are one. The q-factors cancel because q is a power of three. The remaining 3-adic factor is at most one. The height is comparable to q in this range. Infinitely many solutions would give one rational line containing infinitely many distinct primitive pairs, which is impossible. The case h=nq is harmless by reduction. This is a source-qualified application of a written external theorem, not a Lean result. If a hypothetical escaping positive n furnished the displayed power gain for some δ along infinitely many centers, it would be excluded. The constructive estimates above bound the product only by 12n(3^{s_k}/2^k)24^t, which does not provide the gain. Neither qualitative two-place closure nor iteration through arbitrarily many switches fills this gap.

### Attainment on the whole basin of 1

If B_∞=∞ and E(n)>1, then some finite center attains E(n). Choose a threshold t strictly between 1 and E(n). At sufficiently high k the uniform bound 1+n/B_k is below t; below that cutoff the candidate set is finite. In particular every ordinary odd n reaching 1 satisfies both hypotheses. For E(n)>1, pull back −7 from 1 along an actual complete-valley itinerary from n to 1 (the empty itinerary works at 1). Its difference numerator starts at 8; each matched pullback multiplies the difference numerator by Q/g with g an odd divisor of that numerator, so g=1 at every step and it stays a power of two. The normalized score is then (qn+h)/h>1. If a source has E(n)>1 and no maximizing center, its orbit therefore escapes. Attainment does not force a decreasing step, as 31→121 shows.

## A bounded nonlinear repair that transports through arbitrary switches

For c>1 put K_c(n)=sup 2^v₂(qn+h)/(h+cqn), over the same tree. This is positive and at most one. For a target center −h/q the pulled center has magnitude numerator h'=(Qh+Cq)/g and q'=Pq/g, with g=gcd(Qh+Cq,P) a power of 3. On an actual y→z,

    q'y+h'=Q(qz+h)/g.

The ratio of its source score to the original target score is

    Qg(h+cqz) / (Qh+Cq+cPqy)
    = g [1 + (c−1)Cq/(Qh+Cq+cPqy)] > 1.

Thus K_c(y)≥K_c(z) at every actual valley regardless of switches, and strictly if a target maximizer exists. The general strict per-center real inequality is checked in `lean/NonlinearTransport.lean`; the tree pullback and supremum implications are written here. This exact monotonicity is universal; it supplies no uniform debit. In fact K_c=1 everywhere on the ordinary basin of 1. At 1 pull back −7 repeatedly through the (1,1) valley 1→1. The unreduced denominator becomes 3^j and the magnitude numerator becomes 8·4^j−3^j (no factor 3 cancels for j≥1). The difference numerator is 8·4^j and the score tends to one. Backward monotonicity propagates this value to the entire basin. No individual center attains it there. More generally K_c(n)=1 iff there exist centers with qn+h a power of 2 and h/q tending to infinity. Indeed a nontrivial odd part bounds each score by 1/3, and for odd part one the score is (h/q+n)/(h/q+cn). A source with K_c(n)<1 would therefore be a counterexample; no such source is established.

The discrete score min oddpart(qn+h) has a minimum and is nondecreasing along the forward valley path by the same transfer. It equals one on the 1-basin. An upper bound along an arbitrary forward orbit and a strict well-founded return are missing.
