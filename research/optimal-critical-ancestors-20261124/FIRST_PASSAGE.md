# A first-passage formulation of one-head closure

The purpose is to isolate a finite-root joint distribution target, using two recent external results. This argument is conditional on their stated mathematical validity, not a claim of independent local verification. References M and N are specified in [README](README.md). The remaining summability assertion is open.

## 1. Equivalence to summable head-edge failures

Use PR197's fixed arc I=[7,8), R_j=81^j, H_j=[7R_j,8R_j) intersect N. Let x~y mean their forward shortcut orbits have a common future, allowing independent clocks. D_j is the number of x in H_j with x not~floor(x/81).

Under M,

    Collatz holds  <=>  sum_{j>=1} D_j/R_j < infinity.

Necessity is immediate. Sufficiency follows by adapting the frozen proof in [PR197 HEAD_EDGE_RIGIDITY](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md); here the summable condition replaces its power-sparse condition.

Let f(n)=1 if n reaches 1 and 0 otherwise. Put F_j(t)=f(floor(R_j t)) on I. The integer truncation identity gives

    ||F_j-F_{j-1}||_1 <= D_j/R_j.

Hence F_j converges in L1 to a binary function g, because binary-valued functions form an L1-closed set.

For fixed k>=0, l integer, c=2^k/81^l, consider t with t,ct in I. On the subcells {R_j t}<2^(-k), the exact identity floor(R_{j+l} c t)=2^k floor(R_j t) and doubling invariance give F_{j+l}(ct)=F_j(t). The indicators of the subcells converge weakly against every fixed integrable function to 2^(-k): prove this on interval step functions by cell averaging and then use L1 approximation. Apply to |g(t)-g(ct)|. Its integral on these subcells tends to zero by L1 convergence and the change of variables. Therefore g(t)=g(ct) almost everywhere on I intersect c^(-1)I. All the pairs k,l are countable.

In log base 81 coordinates the interval is a proper arc of the circle and the identities give invariance under every forward return of the irrational rotation by log_81(2). If both colors had positive measure, the union of all nonnegative translates of one color would be conull by ergodicity yet disjoint modulo null sets from the other. Contradiction. Hence g is constant, as in PR197.

The minority color in H_j now counts o(R_j), rather than o(R_j^alpha) required by the earlier power-sparse route. Summing the geometric octaves gives o(X) head starts below X. Every sufficiently large integer n has a dyadic multiple 2^k n in a head H_j with k bounded by an absolute constant: apply compactness to the backward translates of the interior of the log arc. This map has bounded multiplicity, preserves f and increases height by a bounded factor. Thus the minority color on all positive integers has upper natural density zero.

If Collatz fails, select an odd ternary unit b on the bad orbit. M gives positive lower natural density both to A(b), all of which have color 0, and to A(1), all of which have color 1. This contradicts the zero-density minority. No uniform lower bound in b is necessary. This completes the equivalence.

The analogous summability mechanism for tripling variation was already identified in PR146; credit also goes to PR197 for the exact one-arc head argument. The new quantitative interface is below.

## 2. Uniform barrier transfer to polylogarithmic root labels

Let M_j be positive integers. Define h_M(x) as the first actual shortcut iterate at most M, undefined if no such iterate exists. For the pair (x, floor(x/81)), let E_j count x in H_j for which both hits at M_j exist but their hit values are not equivalent under ~. Both values are actual points of their respective orbits, so a merger between them is equivalent to a merger between the original pair. This uses equivalence of forward intersection on deterministic paths, not a fresh law of random first-passage positions.

Under N, the number of x in H_j with undefined first hit is <=8 K R_j M_j^(-gamma). For undefined first hit of the parent, the same estimate on the parent interval times the maximal preimage multiplicity 81 gives <=8 K R_j M_j^(-gamma). Therefore

    E_j <= D_j <= E_j + 16 K R_j M_j^(-gamma).

All constants apply simultaneously in X and M. In particular for any fixed L>1/gamma, take M_j=ceil(j^L). Then sum M_j^(-gamma)<infinity. Since j is proportional to log R_j, this uses a polylogarithmic root range, with an enormous but fixed exponent if gamma is tiny.

**Exact closure criterion (M+N):**

    Collatz holds <=> sum_{j>=1} E_j/R_j < infinity.

To turn the criterion into a sufficient finite certificate problem, replace E_j by an upper bound which counts pairs of defined roots not certified equivalent within any specified finite clock budget. Missing certificates on the two arms must be counted using their actual joint first-passage distribution, with all multiplicities. A marginal hitting estimate for each root or arm does not bound E_j. The first-passage clocks themselves are not asserted to have an effective uniform upper bound by N. A finite-time variant requires an additional tail estimate on these clocks.

This reduction removes the need for a fixed positive power in the all-time head-edge count, but **does not prove the required summability**. For example an O(j^(-1/2)) upper bound for normalized E_j is insufficient. Even an upper bound tending to zero is insufficient for the L1 Cauchy argument.

## 3. Another consequence of the uniform bound: finite component tightness

Let m(n)=min_{i>=0} T^i(n), an attained positive integer. N says that the empirical distributions mu_X of m(n) for uniform 1<=n<=X have uniform tails mu_X((M,infinity))<=K M^(-gamma). Dyadic binning gives, for every 0<a<gamma, a uniform bound on E_X[m(n)^a], using the geometric series sum 2^{(a-gamma)k}. This is a moment of the actual orbit minimum, not a moment of stopping time or of a trajectory conditioned on survival.

It also gives uniform Shannon entropy tails. For bin B_k=[2^k,2^{k+1}), mass p_k<=C 2^{-gamma k}; conditional entropy within B_k is <=log |B_k|<=k log 2, and the contribution to entropy is at most p_k log(1/p_k)+p_k k log 2. The sum for k>=h is O((h+1)2^{-gamma h}), uniformly in X. For sufficiently large h use monotonicity of p log(1/p) on [0,1/e]; finitely many small bins do not affect the tail estimate. Any subsequential pointwise limit is a probability measure by tightness, and its entropy is the limit of the entropies along that subsequence. In addition for 1/(1+gamma)<a<1, Holder's inequality gives

    sum_{m in B_k} mu_X(m)^a <= (2^k)^{1-a} p_k^a
                              <= C^a 2^{(1-a-a gamma)k}.

Thus the corresponding Renyi entropy sums also converge along each such subsequence. No existence of a unique density limit is claimed. Under M, if Collatz fails, there is uniform positive mass at m=1 and uniform positive mass in m>=2 for large X. In particular the liminf of the Shannon entropy is positive. Entropy vanishing along *any* unbounded sequence of cutoffs would therefore settle Collatz. The analytic task is to derive actual concentration of these distributions; tightness alone does not give it.

For a fixed orbit C in the equivalence class of a positive start, choose a forward ray q_i (which may be periodic). For every fixed M, the finitely many points in C at most M each merge with the ray at a finite index; choose i sufficiently large for all of them to reach q_i. For any n in C that does not reach q_i, its entire orbit stays above M, since otherwise it would visit one of those points. Consequently

    #( (C \ A(q_i)) intersect [1,X] ) <= K X M^(-gamma)

uniformly in X for all i beyond the chosen index. This upgrades increasing ancestor-set exhaustion of an actual class to uniform-in-cutoff approximation. It does not force the class to have a smaller member or any periodic member, and it gives no effective bound on the required index. In particular a uniform high-root density estimate tending to zero along any escaping ray would contradict M+N; available fixed-target lower bounds are not such an upper estimate.

## 4. The failed attempt and exact next steps

It is tempting to apply N at successively larger barriers, use M to claim a bad component is too dense, then conclude convergence. That comparison is invalid. N bounds mass of components whose minimum is large; M gives only a target-dependent positive density which may be smaller than the barrier bound. Even for a least counterexample there is no contradiction from these two inequalities alone. Likewise every fixed-target population can hit a different small root, and the two arms in a head comparison can have different components after individually successful barrier hits.

A genuine closing result must exploit the actual coupling of the two roots, or prove a power-sparse exceptional set on the optimal section J constructed in README. This note is a finite-root reformulation and compactness improvement, not the missing theorem.

## 5. Verification boundary

The argument is written mathematics. The external release pages report formal verification, but this checkpoint did not rebuild them. The phase/ancestor route uses only M and R; this route uses M and N plus the explicitly pinned one-arc proof. No conditional statement is represented as an unconditional proof of Collatz, and there are no admitted axioms in the accompanying finite arithmetic candidate.
