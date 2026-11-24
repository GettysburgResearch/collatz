# Reverse renewal domination and ternary harmonic pressure

**PROPOSED written proof; source-qualified probability estimates and Tao's published theorem are explicit inputs. Full Collatz is OPEN.** This is an infinite-dictionary continuation of PR200 RATIO_PRESSURE.md, not another finite-pressure exponent improvement.

## 1. The stationary measure of the exact first-return dictionary

Use T(n)=n/2 for even n and (3n+1)/2 for odd n. At a ratio-five root the actual paired affine profiles have equal odd count and ratio five. Start at a root with its next source parity prescribed odd; stop at the first positive root h and then consume all following even bits until the next odd bit, which is the next mark. Write e=h+b for the consumed length. A block w consists of these e chronological source parity bits, starting with 1; its following sentinel bit is 1 but not consumed. Denote by p>=1 its odd count and by C its affine carry. The affine map is

    F_w(z) = (3^p z+C)/2^e.

The root and padding rule implies both original arms follow this map in ratio five at the new mark. Its conditional binary-Haar probability is precisely 2^(-e): the initial bit is prescribed, the following e-1 consumed bits and the terminal odd bit are fair. The first return is almost surely finite by PR146 (pinned input P below); padding is geometric. Thus these weights sum to 1.

Every F_w maps the compact ternary unit group U=Z_3^× into U: the carry C is a unit modulo 3 since the last odd input supplies its only nonzero term modulo 3. Every map has 3-adic Lipschitz constant 3^(-p)<=1/3. Let W_1,W_2,... be independent blocks with this law, and compose outermost first,

    Z = lim_j F_(W_1) o ... o F_(W_j)(z_0).

The sequence is Cauchy, uniformly in z_0 in U, so it defines a unique stationary probability nu. Uniqueness follows by coupling any two initial points under the same j blocks; their mod-3^k values agree after j>=k blocks. The distribution of forward composition is identical by reversing the iid finite list. In particular its mod-3^k marginal is EXACTLY nu_k after k random blocks from any fixed or random initial point. This is an exact statement for the artificial harmonic Markov operator, not a claim about the itinerary of a fixed ordinary q.

For normalized Haar mu on U, the density of a single pushforward term is

    2^(-e) 3^p 1_(q in F_w(U)) V(F_w^(-1)(q)).

Thus this is exactly the harmonic operator of PR200, not a new probability tilt. The pushforwards from mu converge weakly to nu; no L1 convergence of their densities is claimed. Every marginal is effectively computable by truncating the countable dictionary: discard weight delta=1-sum of retained branch probabilities, renormalize, and couple k iid blocks. The mod-3^k TV error is at most k delta. The discarded weight can be computed exactly from the finite retained dictionary and tends to zero. No a priori cutoff rate is needed for this computability claim.

## 2. The key estimate: only linear killed occupation near the root

Input P is the written ratio-five chain estimate of PR146, FIVE_RETURN_CLOCK_AND_TERMINALS.md, at f431078244e868dc699fad011044f0d5e7f76437. Let k_t be the signed difference of odd counts. In the three-clock skeleton, increments have conditional mean 0, absolute value <=3, and conditional variance >=1/4. P constructs a nonnegative Lyapunov W>=|k| with nonpositive drift outside a finite set and finite expected pre-absorption visits to that set. In particular, from the fixed nonroot state after the initial odd step, for sigma the first root at a skeleton time,

    sup_j E |k_(sigma wedge j)| <= D < infinity.

This follows from P's displayed stopped drift bound by choosing its strip width larger than every possible level through j. No optional stopping at an unbounded time is needed. P also proves that the first positive root h is finite a.s. The skeleton can be based at time 1 (the initial forced odd step has been consumed).

For L>=1 set a=L+3 and use the convex differentiable function

    H_L(u) = u^2                   if |u|<=a,
             2a|u|-a^2             otherwise.

It is nonnegative and <=2a|u|. At a live skeleton point with |k|<=L, the entire three-clock increment lies in the quadratic region, so its conditional expected increment of H_L is at least 1/4. At other live points convexity and the martingale increment imply nonnegative drift. Killing at sigma stops the function. Finite telescoping through j and the bound D yield

    E sum_(i<sigma wedge j) 1_(|k_i|<=L) <= 8(L+3)D.

Monotone convergence yields O(L+1) expected visits. In physical time t<h, the preceding skeleton sample is live, and its signed level differs by at most two. Charging at most three physical times to each sample gives

    sum_(t>=1) Pr(t<h, |k_t|<=L) <= C(L+1).           (G)

This is a first-return-from-root estimate; it is NOT a uniform bound independent of arbitrary initial state. It uses the same binary-source law at all clocks. Compare PR201 and PR197's killed-Green arguments for equality mergers. Here (G) is specialized to the ratio-five return dictionary, with the Lyapunov bound from P.

## 3. Reverse suffix likelihood bound

Fix a binary string u of length l>=1. For a single sampled block W, consider the event that its length e>=l and its last l consumed bits equal u. Set t=e-l, and sum over possible t. For t>=1, conditional on the past through t, the probability of the next l prescribed source bits is 2^(-l).

If t<h, the subsequent first root occurs by t+l, so |k_t|<=l. The condition t<h and level k_t are past-measurable. If t>=h, all bits between h and t must have been zero (the end has not yet been determined). The total expected number of these possible padding start clocks is <=E(b+1)=2. At t=0 the first odd bit was prescribed, costing at most a factor of 2. Dropping the additional constraints for the end of the block only increases the probability. Summing with (G) gives

    Pr(W has suffix u) <= C(l+1) 2^(-l).              (S1)

Next form the reverse infinite chronological bit stream by reading W_1 backwards, then W_2 backwards, etc. For every prescribed reverse prefix v of length l,

    Pr(reverse stream begins v) <= C(l+1)^2 2^(-l).  (S2)

Proof: reverse v back into chronological order. Its earliest partial block has a suffix of length j for exactly one j in [1,l]. The remaining l-j bits are whole blocks. Once j is specified those whole blocks have at most one legal parsing: start from the marked root, follow the exact first-return rule, consume zeros up to the next 1, reset, and append a terminal sentinel 1 at the known final mark. This argument works although a block string with appended zeros need not be prefix-free without a sentinel. For any legal parsing the probabilities of the whole blocks multiply to 2^(-(l-j)). The earlier independent block suffix has probability at most C(j+1)2^(-j) by (S1). Sum over j. No renewal mean, independent parity law at a stopping time in reverse, or uniform conditional endpoint law is assumed. The polynomial loss is retained.

## 4. Import Tao's theorem through an upper domination, not through false independence

For a reverse bit stream let A_i be the number of consumed bits through its i-th one (positive increasing clocks). Modulo 3^k, once k ones have appeared the affine expansion of Section 1 gives exactly

    Z mod 3^k = sum_(i=1)^k 3^(i-1) 2^(-A_i) mod 3^k.

This follows by expanding each shortcut step's carry, reading backwards from the endpoint. The contribution of the earlier state vanishes after k odd steps. The same formula under genuinely iid fair bits has Tao's Syracuse offset distribution S_k, with A_i-A_(i-1) iid geometric of mean 2 on the positive integers.

Use (S2) on the finite word cylinder determining the first k ones. On A_k<=4k the likelihood ratio relative to fair bits is at most C(4k+1)^2. On A_k>4k, the first 4k bits contain fewer than k ones, so (S2) and the elementary fair binomial Chernoff bound give O(k^2 exp(-ck)). Therefore for EVERY set E of residues mod 3^k,

    nu_k(E) <= C(k+1)^2 Pr(S_k in E) + C exp(-c' k).  (D)

The constants are absolute given P. This is a one-sided measure bound; it does not imply the Fourier coefficients of the stopped law have Tao's cancellation. In particular a polynomial likelihood ratio must not be treated as an error in total variation.

Tao, Almost all orbits of the Collatz map attain almost bounded values, Forum of Mathematics Pi 10 (2022), e12, Proposition 1.14, proves that the Syracuse offset distribution modulo 3^k differs in l1 by O_A(m^(-A)), for 1<=m<=k, from its coarse marginal mod 3^m spread uniformly over each fiber. This is the published source https://doi.org/10.1017/fmp.2022.8 (see equations 1.26–1.27). Applying this result ONLY to S_k gives

    Pr(S_k in E) <= |E| 3^(m-k) + C_A m^(-A).

Hence for any fixed 0<delta<1, m=floor(k^delta), and any E with |E|<=3^(k-2m),

    nu_k(E) = O_(delta,B)(k^(-B)) for every B>0.       (F)

Choose A large compared to (B+2)/delta. This is quantitative avoidance of all exponentially thin residue families at ternary resolution k by the exact harmonic return law. The exceptional family can vary arbitrarily with k.

## 5. Almost-everywhere nearly Haar cylinder mass and entropy

Let E_k be the heavy cells with nu_k(a)>3^(-k+2m). Their number is <=3^(k-2m), so (F) gives a summable bound on their nu mass. The light cells with nu_k(a)<3^(-k-m) have total mass <=3^(-m), also summable. Borel-Cantelli, for each fixed delta and then a countable intersection over rational delta in (0,1), proves

    -log_3 nu(q+3^k Z_3) = k + O_(q,delta)(k^delta)

for nu-almost every q and every fixed delta>0. In particular nu is nonatomic and exact-dimensional of dimension 1. Also H(nu_k)>= (k-2m)log(3) [1-O(k^-2)], while H<=k log3, so for every delta>0

    0 <= k log 3 - H(nu_k) = O_delta(k^delta).

These statements do not imply absolute continuity: full dimension and subpower entropy deficit are compatible with singular measures.

The support is the whole ternary unit group by a separate elementary argument. The ordinary A block on x=49 mod64 has its first root at h=6, p=2 and C=7 (direct literal check; see PR146). For every q in U, there is an e in [6,23] with 2^e q=7 mod9 but not mod27, using the order 18 of 2 mod27. The inverse (2^e q-7)/9 lies in U, and A padded to e is a dictionary branch. Repeat this inverse ceil(k/2) times. The corresponding forward composition maps ALL U into the prescribed q mod3^k, and has probability at least 2^(-23 ceil(k/2)). This gives a uniform, but very weak, lower cylinder bound. It is not the near-Haar bound at every q.

## 6. What this buys and what remains open

The infinite dictionary now has a rigorous source-qualified high-entropy stationary law attached to the exact five-return operator; it is not obtained by assuming iid gaps at a root. The harmonic transfer pressure in PR200 is the density evolution of this very measure. The estimates show that a highly sparse ternary exceptional family cannot carry its stationary mass.

The crucial missing assertion is pointwise arithmetic control at one FIXED ordinary target. The near-Haar cylinder bound holds for nu-almost every ternary-adic unit; all ordinary integers form a countable nu-null set. Positive support does not give a useful uniform exponent for these atoms' neighborhoods. Even an L1 stationary density would not by itself supply positive values at specified integers. Also the ordinary inverse branching proof must keep positive height and whole-modulus legality, unlike a purely ternary-adic stationary argument. No implication that all failed-five targets vanish, no harmonic exponent-one ordinary lower count, and no proof of Collatz follows here.

An actionable next target is a lower bound for the exact inverse harmonic sums at each ordinary odd unit, retaining the full clock and carry and adequate height truncation. The present result provides a stationary distribution and a strong upper bound on its exceptional mass, but not that pointwise lower bound.

Finite controls in controls.js check 1003 first-return cylinders through h=18, 5015 padded block cases, 1200 three-block parsings and 14397 exact reversed-offset and composition checks each. These are finite arithmetic evidence only. No independent agent review or Lean compilation was available.