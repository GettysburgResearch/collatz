# Diffusive central-row closure: aggregate amplification and localization

**Status: PROPOSED written mathematics. Collatz remains OPEN.** The full conjecture is reduced to two explicit finite row statistics with near-natural-scale lower bounds under a counterexample. The lower bounds import a source-qualified joint renewal floor. The upper localization uses finite-grid passage and grade-spreading inputs. No missing universal upper bound is assumed. No independent agent or Lean compiler run is claimed in this environment.

## 1. Setup and exact statistics

T is the positive shortcut map, T(2x)=x, T(2x+1)=3x+2. U is the positive odd-to-odd map; the gap e=v2(3x+1) counts shortcut steps. A unit is a positive odd integer prime to three. For a chronological word of b gaps, total s and carry C, the actual affine equation is

    2^s q = 3^b x + C,
    beta = C/2^s,
    D = q 2^s/(3^b x)
      = product_(j<b) (1+1/(3x_j)),
    beta/q = 1-1/D.

Here x_0=x, x_b=q and x_(j+1)=U(x_j). All paths counted below are actual positive unit starts (intermediate unit status follows after the first odd step). A row is **simple** if all b+1 recorded odd states are distinct. This is a finite test, NOT a test of eventual periodicity of q. Let

    G_b = 4^b/3^b
    N_b(q,eps) = number of unit sources in the exact (b,2b) row
                 with beta/q >= eps
    N_b^s(q,eps) = same count, restricted to simple rows.

The superscript s means simple, not physical clock. For b>=1 set L_b=ceil(sqrt(b)), Q_b=2^L_b, eps_star=1-2^(-100). Define

    E_b(eps) = sum_{L_b <= q <= Q_b, q unit, q>1}
                       N_b^s(q,eps)/(q G_b)
    C_b = max_{1<q<=L_b, q unit} sqrt(b) N_b(q,eps_star)/(q G_b)

with empty maximum zero. For an entirely rational test use L_b instead of sqrt(b) in C_b; all statements are unchanged. These statistics are finite. Given b and q, enumerate positive compositions of 2b into b parts, invert and check every actual odd state and valuation; alternatively enumerate positive odd x<=q G_b. The carry test is the exact integer inequality 3^b x <= (1-eps)4^b q. No convergence oracle enters.

**Main theorem (conditional on F):**
* Every positive ordinary orbit is eventually periodic iff for every rational 0<eps<1, liminf E_b(eps)=0.
* There is no nontrivial positive cycle iff liminf C_b=0.
* Consequently Collatz holds iff both conditions hold.

In the true case each applicable statistic is eventually exactly zero. If an escape exists, some fixed eps>0 gives E_b(eps)>=c>0 at EVERY sufficiently large b. If a nontrivial cycle exists, C_b>=c>0 at EVERY sufficiently large b. Constants can depend on the single original orbit or cycle. There is no claim that the conditions on the right have been proved.

The important improvement on the finite-row amplification of PR201 and PR206 is the weighted aggregate: many distinct moving ordinary terminals have almost the full natural fixed-total count at the same b. There is no maximum over a varying supplied gate and no sum of overlapping predecessor densities.

## 2. Inputs and proof boundary

* **F (source-qualified):** Weaver/Wren, Hierarchical Syracuse renewal and linear valuation budgets for modular routing, paper 48 v2, Lemma 7 (76) and bounded first-exponent spreading in Theorem 8, https://rstation.ai/problems/collatz/papers/48/v2. Use the EXACT count version reconstructed in PR201 at 73a145ca99448a78219bd149e273f33b6e3fda4b, research/killed-green-head-closure-20261124/two-end-bridge/README.md, §1. For every sufficiently large n, any supplied ordinary unit a, prescribed unit residue modulo 3 (K=1 suffices), and |t-2n|<=sqrt(n), the number of literal legal inverse paths of n gaps, total t, ending forward at a, is >=c_F 2^t/(3^(n+1)sqrt(n)). The constant and onset are uniform in a, t and residue. We do NOT require an upper bound, a pointwise limit, a joint two-arm floor, or any uniformity beyond this stated central range. See also PR203, fixed-target depth-bank proof. We do not independently rebuild the paper's analytic proof. Its reported version should be checked against this precise count statement before any promotion.
* **S (elementary resident finite-path estimate):** PR201 head 2978d84f8a1fda9083593b26c6bf724d5976d859, research/killed-green-head-closure-20261124/escape-analysis/README.md, section Why convergence gives eventual zero, recalling main T-A3-651. Every finite simple odd trajectory segment has at most 5 X^(39/40) distinct odd states up to X and reciprocal sum at most 200 M^(-1/40) if all those states are at least M>=1. This input is for a simple path, not all visits to a cycle. The proof is elementary parity-cylinder counting and synchronous injectivity; see the pinned proof. Thus D<=D0=exp(200/3)<2^100 on simple rows. The strict inequality follows from ln 2>2/3, e.g. strict convexity of 1/t integrated on [1,2].
* **P (source-qualified pair estimate, only for the shallow-window upper bound):** PR201 at 084b983fbec6f3d2120ef101946754431f82874e, research/killed-green-head-closure-20261124/continuation/README.md, G1/G2. Exact odd-grade spreading under logarithmic sampling on a full dyadic octave [X,2X), for two actual first-hit records and a common prefix h, gives sum_K sup_p mu(K,p) <= C/sqrt(h)+C/X if 2^h<=X/2, 2^(h+1)Y<X. Target sets lie in [1,Y]; the second may be the sole active target set (take the other empty). Its proof imports PR146's finite-grid symbolic fusion. We use the result for a single first hit to {q}, with no arbitrary conditional new law. We have not independently rebuilt those pair estimates.
* The sharp concentration at a polylog first passage used below is derived explicitly from the original-source entrance fiber argument of PR197 at 578e43911f49d41ef610b368a89b5a1ec269e134, research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md, equations (2)-(5), and the centered-prefix refinement already used in PR193 at ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784, research/astra-closure-20261124/transfer/HEAD_ROOTS.md. We include the derivation rather than quote a Gaussian/local-limit theorem for the first hit to a fixed integer. The concentration statement concerns first entry to a growing polylog barrier, not a time to 1.

For perspective see Tao's published Fourier/renewal argument, https://doi.org/10.1017/fmp.2022.8, and the recent source-qualified results of Weaver, paper 202/v1, https://rstation.ai/problems/collatz/papers/202/v1 (counterexamples to inverse-logarithmic lower gains of predecessor density already on convergent paths), paper 19/v2, https://rstation.ai/problems/collatz/papers/19/v2 (canonical real fibres and finite-depth diagonal trace), and paper 146, https://rstation.ai/problems/collatz/papers/146 (critical weak-L2 stationary ternary density). These motivate the new aggregate formulation, but their estimates are not inserted as pointwise bounds on the integer trace.

## 3. Proof of the main theorem

### 3.1 Uniform small gate for large relative carry

If a simple row has beta/q>=eps, log D>=-log(1-eps)>=eps. If all its odd inputs were >=M, S and log(1+u)<=u would give log D <= (200/3) M^(-1/40). Fix any integer M=M(eps) large enough that this is strictly below eps. Some actual odd input g<M occurs; choose the FIRST such odd input and call it the gate. The suffix from that gate to q has odd length j>=1, physical length B>=j and is part of the same recorded trajectory. In particular, as q varies for a fixed b, the set of possible endpoints of simple high-carry rows has size at most M(b+1): every q is one of U^j(g) for a gate from a finite set and 1<=j<=b. No property of the future beyond the recorded row is assumed.

If all ordinary trajectories are eventually periodic, the union of the complete forward orbits of the finite gate set is finite. Thus for large b no q>=L_b can occur and E_b(eps)=0. This direction allows nontrivial cycles.

### 3.2 One escape amplifies many targets at one exact row

Suppose a positive ordinary escape exists. Choose one fixed odd unit a on that orbit (strip initial twos, take an odd step, strip twos). Write q_i=U^i(a), with cumulative physical count A_i and exact distortion D_i. The q_i are distinct, tend to infinity, and all paths ending there are simple, because a repeated odd vertex would make q_i periodic. We have

    1+1/(3a) <= D_i <= D0               (i>=1),
    3^i/2^A_i = q_i/(a D_i),
    A_i >= i, A_i <= i log_2 3 + log_2(a D0).

Set eps=1/(3a+1). The relative carry of every actual suffix a->q_i is >=eps. Prepending any positive path preserves this lower bound: affine corrections multiply by the same positive suffix coefficient and add nonnegative carry.

For each sufficiently large b, let i range through the consecutive integers from floor(L_b/4) to floor(L_b/2). Set n=b-i, t=2b-A_i. Then

    |t-2n| = |2i-A_i| <= i+O_a(1) <= sqrt(n)

uniformly over the entire selected range for all large b. Apply F at the SAME ordinary a to obtain legal prefix words of n gaps, total t, in one fixed unit residue modulo 3. Append the actual suffix a->q_i. The resulting path has b gaps, total 2b, and carries at least eps q_i. Each distinct prefix word produces a distinct source at fixed n by determinism. The suffix is not randomly resampled. There is no overlap issue when summing over q_i: these are distinct terminals of the same fixed row.

Therefore

    N_b^s(q_i,eps)
      >= c_F 2^t/(3^(n+1) sqrt(n))
       = (c_F/3) G_b q_i/(a D_i sqrt(n))
      >= c_a q_i G_b/sqrt(b).

At most 5 L_b^(39/40)=o(sqrt(b)) of the distinct q_i are less than L_b, by S. Also q_i<=2^i a, so all selected q_i<=Q_b for sufficiently large b. At least c' sqrt(b) of these actual terminals therefore contribute to E_b(eps), each by >=c_a/sqrt(b). The aggregate is bounded below by a strictly positive constant at every large b. This proves the claimed escape equivalence.

In fact the lower endpoint L_b can be raised to floor(c_1 b^(20/39)) with a sufficiently small absolute c_1>0: S gives <=5 c_1^(39/40) sqrt(b) excluded terminals (e.g. c_1=2^-10). This variant is optional. The outer q-window is not inferred from a random terminal law.

### 3.3 Nontrivial cycles give the other finite obstruction

Every nontrivial positive cycle contains an odd unit q>1. Let p>=1 be its least odd period, A its total shortcut clock, and lambda=3^p/2^A. Positivity and the exact product identity give 0<lambda<1. Choose a FIXED r>=1 with lambda^r<=2^(-100). Append r full actual laps at q to a prefix supplied by F at q, with remaining depth n=b-rp and total t=2b-rA. The central condition holds for all large b because |t-2n|=r|2p-A| is a fixed constant. Every resulting row has relative carry >=1-lambda^r>=eps_star. For fixed b the distinct prefix words give distinct sources, even when q is periodic (no first-hit claim needed here). Consequently

    N_b(q,eps_star) >= c_F G_b lambda^r/(3 sqrt(n)),
    C_b >= c_F lambda^r/(3q)

for all large b, since this fixed q<=L_b eventually. No assumption about the number or distribution of cycles is used.

If there is no nontrivial positive cycle, any path ending at q>1 is simple: a repeated recorded odd state would put q on that same cycle, whereas the trivial odd cycle is {1}. By S its distortion D<2^100, so its relative carry is STRICTLY below eps_star. Thus C_b=0 for EVERY b. This proves the cycle equivalence and completes the full-conjecture conditional equivalence.

## 4. Upper localization: the critical suffix window is diffusive

For the rest of this section all rows are simple. This is an arithmetic condition on the recorded row, so even a first hit of a periodic terminal is included when no state repeats. Write N_b^s(q,eps;I) for the count whose selected gate suffix length j lies in an integer interval I.

**Theorem (using S and, for the shallow bound, P).** With eps fixed, put

    W_b(I) = sum_{q>1 unit} N_b^s(q,eps;I)/(q G_b).

The sum is finite (beta<= (3/2)^b-1 implies q<=(3/2)^b/eps). Then for every fixed eta>0,

    W_b([1,eta sqrt(b)]) <= C_eps (eta+b^(-1/2)),              (U1)

and for each A>0 there is C_A,eps with

    W_b([C_A,eps sqrt(b log b), b]) = O_A,eps(b^(-A)).          (U2)

Moreover, the sum over ALL simple high-carry rows with q>=exp(C_A,eps sqrt(b log b)) is O_A,eps(b^(-A)), regardless of gate suffix length. In these statements restricting the q-sum to any subset only improves the upper bound. Thus every nonsummable or nonvanishing contribution has been localized to the finite-gate forward-time band between a small multiple of sqrt(b) and a large multiple of sqrt(b log b), up to the explicit errors. The log factor is not optimized.

### 4.1 Exact grade upper bound on a full row

For a simple row with total 2b,

    q G_b/D0 <= x <= q G_b.

Its visit to q is the first visit (q odd and no repeated odd state). Cover this real interval by dyadic octaves [X,2X), at most a constant number depending on D0, with sum of X=O(qG_b). Take h=floor(b/10) and target set {q}; the conditions of P hold on each octave for all large b, uniformly q>=1. Indeed X>=qG_b/(2D0) and G_b grows as 2^(0.415... b). The single active target in the two-arm notation of P can be taken to be the identity arm, with the other target set empty. The first-hit absolute odd count is b for each counted source, so G2 bounds this probability by O(1/sqrt(b)). Logarithmic weights on a dyadic octave and natural counts are comparable. Thus

    N_b^s(q,eps) <= C q G_b/sqrt(b).                          (U3)

This applies uniformly to each q, independent of the relative-carry threshold. If j<=eta sqrt(b), at most M(eta sqrt(b)+1) endpoints are possible by the finite gate count. Summing (U3) gives (U1). This step does not multiply a rare-survival probability by a conditional grade law.

### 4.2 Concentration of the ordinary early passage: derivation

We give the two-sided clock estimate in the needed uniform form. On an octave [X,2X), X large, d=log_2 X, for each A>0 choose D>0 large and M_X=d^D. Except on O_A(X d^(-A)) original sources,

    tau_(M_X)(x) >= mu log x - C_A sqrt(log X log log X),
    mu=2/log(4/3).                                            (U4)

Here tau is the first shortcut clock entering [1,M_X), not first hitting any specified fixed gate. In fact an analogous upper bound holds. This is derived using the same original-source entrance accounting as PR197 and the centered-prefix idea already in PR193; no clock CLT is assumed.

Put a=log_2(2/sqrt(3))>0, choose lambda=1-a/4, Y_0=3X, Y_(r+1)=Y_r^lambda, and k_r=floor(log_2 Y_r/2). Stop at first r with Y_r<=M_X. There are O(log d) stages, and sum k_r <= C d. At the actual first entry z to Y_r, for r>=1 and entrance time t<=H=ceil(C' d), the exact product formula from the ORIGINAL source gives, for fixed (t,p,z),

    1 <= z/(3^p 2^(-t) x) <= exp(t/(3Y_r)).

Thus those sources x in the octave lie in an interval of length O(HX/Y_r); there are at most O(1+HX/Y_r) such integers. Sum over O(H^2) clock/count pairs and entry residues. Entry values lie in [Y_r/2,Y_r). Any event on the next k_r bits of grid probability v has O(Y_r v) possible entries by complete-period covering (2^k_r<=Y_r/2 for large X). Therefore its cost on original sources with timely entry is O(H^3 X v). At r=0 the same bound follows directly from complete binary grids at the original start; no prior entry required. These are counts, not replacement of the selected entrance law by a new uniform population.

For each such prefix impose, simultaneously at all u<=k_r,

    |p_u-u/2| <= B_A sqrt(k_r log d).

The parity-cylinder bijection and Hoeffding's inequality, with a union over u, give exception v<=2(k_r+1)d^(-2B_A^2) for B_A sufficiently large (natural log used in the threshold). Choose B_A so the preceding transfer and union over stages cost O_A(X d^(-A)). Choose D so large that k_r>= (D/3)log_2 d for all active stages and B_A sqrt(k_r log d) <= a k_r/(4 log_2 3). On these prefixes,

    T^k(z) <= 3^p(2^(-k) z+1/3)

by the full affine carry identity (each normalized additive odd summand is at most 2^(j-k)/3). Consequently the next threshold is reached within k_r clocks: use z<=Y_r, p<=k_r/2+a k_r/(4 log_2 3), k_r~(log_2 Y_r)/2, and the strict drift margin between (3a/4)/2 and a/4. Induction, with H large enough in advance, proves timely first passage to M_X. The sum of the centered deviations on the truncated actual stages is O_A(sqrt(d log d)), because log Y_r decreases geometrically. Truncate the last stage at the actual first passage to M_X (it occurs no later than the scheduled next threshold). Before that passage every shortcut input is >=M_X; the exact log correction sums to at most H/(3M_X ln2). The first landing z lies in [M_X/2,M_X). Writing p_tau=tau/2+O_A(sqrt(d log d)) in the exact height identity yields

    a tau = log_2 x - log_2 M_X + O_A(sqrt(d log d)).

Since log_2 M_X=O_A(log d), and 1/(a ln2)=mu, this proves (U4), including its lower bound. Rounding thresholds or using strict inequality changes only O(1) in this proof. The exceptional count is uniform in the octave location.

### 4.3 Long actual suffixes are too early

For a simple high-carry row the original source is in the shell of §4.1. The elementary carry upper bound gives log q<=b log(3/2)+O_eps(1), so log X is comparable to b on the bounded dyadic cover, uniformly for all such q and large b. Since the selected gate g<M(eps) is smaller than the polylog threshold of (U4), the original first passage must occur by the time that gate is reached:

    tau_(M_X)(x) <= 2b-B <= 2b-j.

On the other hand, the exact balanced-row height gives log x= b log(4/3)+log q -log D, with D<=D0. Thus outside the exceptional set of (U4),

    2b-j >= 2b + mu log q - mu log D0 - C'_A sqrt(b log b).

This one inequality retains BOTH the actual gate suffix and the actual terminal height:

    j + mu log q <= C'_A sqrt(b log b)+mu log D0.             (U5)

A row violating (U5) is therefore confined to O_A,eps(qG_b b^(-A)) original sources at each q. There are at most M(b+1) possible terminal values, by §3.1, NOT exponentially many. Sum after division by qG_b and take the requested A larger by two. This proves (U2) and the large-terminal bound. Neither upper bound assumes that the original trajectories eventually converge.

**Consequence:** in the escaping lower construction §3.2 the fixed gate a may not be the first small odd input. Nevertheless (U1)-(U2) apply to the complete aggregate, including all alternative gates. A fixed positive lower for E_b(eps) cannot be supported on suffix lengths o(sqrt(b)) or on lengths above C sqrt(b log b). The open estimate is now on genuinely intermediate suffixes of one actual trajectory after one of finitely many gates.

## 5. A sharper pre-diffusive restriction on each fixed escaping ray

Fix the escaping ray from §3.2 and eps>0. For its q_i any simple high-carry path has a gate g from the same finite set M(eps). If g can ever reach some q_i, its first meeting with this escaping ray is at a finite index i_g. These are finitely many fixed indices, with maximum J. Since the ray is injective, its suffix from g to q_i (if i>=J) has length at least i-J. Thus every high-carry row to q_i with b gaps has j>=i-J. In particular if b<i-J the count is exactly zero. For larger b, apply (U5). For each A>0 there is c_A>0 such that, for all large i and all b <= c_A i^2/log(i+2),

    N_b^s(q_i,eps)/(q_i G_b) = O_A,eps,a(b^(-A)).

Indeed for b>=i-J in this range, log b<=3 log(i+2), and choose c_A so the right side of (U5) is less than i-J. Small b were already excluded. Constants may depend on the original ray via J; no claim of a uniform first meeting with g.

In contrast F and §3.2 give, for eps=1/(3a+1), for each i>=1 and every b>=C_a(i+1)^2,

    sqrt(b) N_b^s(q_i,eps)/(q_i G_b) >= c_a>0,

by the same exact central-window condition. These two quantitative directions demonstrate a real obstruction to interchanging the moving ordinary root with the inner exact-clock limit. The transition window is not an independence assumption or a statement about a typical root. It is constrained on the SAME hypothetical ordinary ray. A proof of the required aggregate upper bound only in the pre-diffusive regime would not address the counterexample lower bound.

## 6. What would actually close the conjecture

One sufficient target is a cofinal estimate tending to zero for the explicitly finite aggregate E_b(eps), for every fixed rational eps>0, and for C_b. The escaping part can discard shallow and very late suffixes by (U1)-(U2). The lower bound is at simultaneous moving targets within [sqrt(b),2^ceil(sqrt(b))], at natural row scale, rather than a single exponential lower of smaller exponent.

In terms of the Syracuse law on R x Z_3, the exact-row sum can be written using the ORIGINAL inverse word probability 2^(-2b). For large b, high carry forces q<=((3/2)^b-1)/eps<3^b, so at most one such positive q per residue. The full offset beta of the word is a rational with power-of-two denominator, whose ternary residue is q modulo 3^b precisely when the full inverse chain is integral. The condition beta<q guarantees positive source (positive intermediate states also follow by reversing integral steps from q). Write q_w for the representative in [0,3^b), and impose unit, positivity and simplicity as in E_b. With indicator of the exact word event denoted I_b,

    E_b(eps) = 3^b E[1_{total=2b} I_b/q_w].

The factor 3^b is essential. This is not a usual Haar L^p estimate for the stationary ternary law, and the normalization cannot be removed using an average-density argument. The missing bound is a relative integer-diagonal trace estimate in this balanced slice. Joint real/ternary regularity, conditional Fourier mixing or a renewal theorem with this retained integer trace could be used; the known unconditioned tail and weak-L2 bounds do not directly give it. In particular the pointwise finite-depth cylinder upper from paper 146 alone loses the factor for sampling an integer point at full precision.

We examined the possible alternative based on a uniform lower gain of predecessor density under successive first odd doublings. Paper 202/v1 exhibits genuine convergent families with relative gains smaller than any inverse log power at those doublings. It does not rule out a gain theorem along a single hypothetical escaping forward ray whose predecessor density is bounded below. No such strengthened theorem is proved here.

## 6.1. Separate cycle-sensitive scale transition

See [NEAR_DIAGONAL.md](NEAR_DIAGONAL.md) for the superdiffusive near-diagonal test: at fixed q=1 the source-qualified bounded-offset floor gives a normalized balanced-row lower bound at k=ceil(b^(2/3)); at every other fixed q>1 the same shell has an upper bound smaller by every inverse power of b. For a nontrivial cycle the fixed physical clock introduces a strictly positive defect per lap; the lower floor is currently justified only up to diffusive shell scales. This is an obstruction to extending the existing floor without accounting for the clock, not a proof that nontrivial cycles cannot exist.

## 7. Frozen repository comparisons and evidence

* Main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. PR201 latest 2978d84f8a1fda9083593b26c6bf724d5976d859, finite-row test and elementary lower exponent; its earlier 73a145ca99448a78219bd149e273f33b6e3fda4b, two-end bridge fixed-q inner liminf is the direct antecedent of §3.2. That proof already has an onset n>=(2i-A_i)^2; this packet exploits it at a simultaneous moving depth and counts many distinct q using S, then proves the opposite pre-diffusive bound. G1/G2 source pinned in §2.
* PR206 37d2b5d644664a746891042c199e58cfb06f1176, exact-clock prescribed residue itineraries and sparse-defect constraints, includes every prefix residue mark but a smaller exponential count. Our near-natural-scale lower bound uses F, unlike its elementary construction; no upgrade of its Lean evidence claimed.
* PR197 7ad81ec56947146fac854d2586651ca0c934a536, directed 17 mod48 closure, strict returns and interior width; PR193 fbe870ec44239e6b6c753bab9d1c7537acfff701, repeated component descent and prescribed pairs; PR195 ef3496b577ed7525d5e0c82a9b782819457403d5, paired families and subcell descent; PR192 26f070c38ad9edd21ed7dac6efaab6554550c2a3 and PR205 32d722c5d5597846da5dad842c8ea15742abc176, minimum disagreement and actual forced excursion. These were reviewed at the relevant statements/interfaces, not fully re-audited. The present aggregate bound is neither a universal smaller partner nor a proof excluding the crossing alternative.
* PR203 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d supplies the joint floor extraction and fixed-target depth bank; PR204 5d4698b692ec102b44cf77a59930a2a80b4104fd gives paired row counts, a different exact law.

The companion Lean file is an **uncompiled candidate for finite row algebra and recorded-path consumers**, with no assertion that the analytic assumptions or full conjecture are formalized. Lean/Lake were unavailable in this session; no compiler/axiom audit, independent subagent review, or full checkout validator has run. Exact bounded arithmetic controls are separate: [controls.js](controls.js) was executed with BigInt arithmetic, and [CONTROLS.json](CONTROLS.json) records the counts (222 matched complete rows, 1541 suffix carry checks, 112 moving-window checks, 36 cycle residual checks). The complete proof remains open.
