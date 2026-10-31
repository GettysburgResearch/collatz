# Quantitative concentration and a full-problem collision threshold

**PROPOSED.** These are elementary deductions under explicit hypotheses, not a proof of the missing arithmetic regularity hypothesis. All logarithms in entropy formulas are natural unless a base is displayed. This is a continuation of [OCCUPATION.md](OCCUPATION.md), not a recovery of the unavailable previous swarm files.

Write `c=log_2(3)`. Let mu be a U-invariant probability on the odd 2-adics, with finite mean valuation `b=integral a dmu <= d`, where `1<d<2`. The exceptional pole and all its backward preimages have mu-measure zero, by invariance and finite mean. The claims below apply to *every* occupation limit supplied by O1, not just ergodic limits.

## E1. Exact valuation-block relative entropy

Let P_k be the mu-law of k successive valuations, and let `Q_k(w)=2^(-A(w))`, where A is their sum. Define

`I(d)=d ln(2)-d ln(d)+(d-1)ln(d-1)>0`.

Then

`D(P_k || Q_k) >= k I(d)`.

Proof. Let `g_d(a)=d^(-1)((d-1)/d)^(a-1)` for a>=1. Finite mean implies finite Shannon entropy (comparison with a geometric law). Hence

`D(P_k||Q_k) = D(P_k||g_d^k) + k ln(2/d) + (E[A]-k) ln(2(d-1)/d)`.

The first term is nonnegative, `E[A]=kb<=kd`, and the last coefficient is negative. Substitution gives the claimed bound. Equality is attained by the invariant process of independent valuations with law g_d. The exponent I(d) decreases for 1<d<2 because `I'(d)=ln(2(d-1)/d)<0`.

For every p>1 the associated cylinder density moment satisfies

`sum_w P_k(w)^p Q_k(w)^(1-p) >= exp((p-1) k I(d))`.

This follows from Jensen applied under P_k to `(P_k/Q_k)^(p-1)`. It does not presume a density of mu with respect to Haar on the infinite space: only finite/countable cylinder probabilities are used. The moment can be infinite.

## E2. Fixed dyadic precision, without an ergodicity assumption

Let `P_L(r)=mu(r+2^L Z_2)` for odd r modulo 2^L, and let H_L be its Shannon entropy. Define

`kappa(d)=1-H_2(1/d)`.

Then

`limsup_{L->infinity} H_L / ((L-1)ln(2)) <= H_2(1/d)`,

and therefore

`liminf_{L->infinity} D(P_L||Unif(odd mod 2^L)) / (L ln(2)) >= kappa(d)`.

Here H_2 is binary entropy in bits. The result is not obtained by equating accelerated time and dyadic precision.

Proof. Use the shortcut map T from the repository. Its first L parity bits biject with residues modulo 2^L: successively invert `x -> x/2` and `x -> (3x+1)/2`; each inverse branch adds one specified parity bit, and a length-L composition contracts by 2^L in the 2-adic metric. Thus entropy of the parity vector equals H_L. The first bit is one.

For mu-almost every x, Birkhoff's theorem for the integrable return-time function a gives

`(a(x)+...+a(U^(K-1)x))/K -> bbar(x)`,

where `bbar>=1` and `integral bbar dmu=b`. The odd shortcut times are exactly the partial sums of these return times. Consequently the proportion R_L(x)/L of ones in the first L shortcut bits tends to `1/bbar(x)`. Since this proportion is bounded by one, dominated convergence gives

`q_L := E[(R_L-1)/(L-1)] -> q=integral (1/bbar) dmu >= 1/b >= 1/d`.

The last inequality is Jensen; this is the step that handles nonergodic mixtures. Chain-rule subadditivity and concavity of binary entropy yield `H_L <= (L-1) h(q_L)`. Because q>=1/d>1/2 and h decreases on [1/2,1], the entropy estimate follows. Subtract from the uniform entropy `(L-1)ln(2)`.

For every p>1, put `C_{p,L}=2^((L-1)(p-1)) sum_r P_L(r)^p`. Jensen again gives

`liminf (log_2 C_{p,L})/L >= (p-1) kappa(d)`.

In particular the collision moment `C_L=C_{2,L}` has growth exponent at least kappa(d). Do not confuse the valuation-block rate I(d) with this precision-normalized rate. They satisfy `I(d)=d ln(2) kappa(d)`.

## E3. Sharpness and limits of the lower bound

The independent geometric process g_d has mean d and is U-invariant under the inverse-branch coding. Its shortcut parity process, conditional on the first bit being one, has independent later bits with odd probability `q=1/d`. It has full 2-adic support, is non-atomic and mixing, and is singular to Haar when d!=2. Its dyadic entropy is exactly `(L-1)h(q)`. Thus E2's entropy coefficient is sharp.

For this particular process the collision formula is

`C_L=[2(q^2+(1-q)^2)]^(L-1)`.

That rate is generally *larger* than kappa(d); entropy sharpness alone does not prove collision-rate sharpness.

A separate block construction shows that kappa(d) is also the infimum of possible collision exponents under only invariance and the mean constraint. Take integers B and 0<K<B with `q_B=K/B>=1/d`. Form a two-sided binary process from independent uniform length-B blocks containing exactly K ones, and randomize the block phase uniformly. It is shift-invariant and ergodic. Induce on the event that the current bit is one and apply the Collatz parity coding. The resulting odd-time invariant probability has mean return time `1/q_B<=d`.

Let `J=binom(B,K)`. For a fixed block phase, a length-L cylinder contains full blocks and at most two partial end blocks. Every nonzero cylinder probability is between positive constants depending only on B times `J^(-L/B)`. The same bounds hold after the finite phase mixture and conditioning on a first one. Therefore `sum P_L(r)^2` has exponential rate `-(ln J)/B`, and the collision exponent is exactly

`1-(log_2 binom(B,K))/B`.

Choose `K=ceil(B/d)` and let B grow. Stirling's formula makes this exponent tend to kappa(d). This establishes sharpness as an infimum; it does not assert that one block model attains it exactly. None of these measures is asserted to be an occupation limit of one fixed positive source.

## E4. A rational threshold covering cycles and divergence

The standalone checker proves by literal odd-step induction that every positive start through 4096 reaches 1. It checks each odd n from 3 through 4095 until its first smaller odd value; smaller starts have already been certified. Even starts halve to a smaller value. This is a bounded computation, with a replay and transcript digest, not a universal stopping theorem.

Any counterexample orbit would therefore have every odd state at least 4097. O1 applies with

`d_*=log_2(3+1/4097)`.

The exact rational logarithm enclosures in the checker certify

`0.050008338007577073 < kappa(d_*) < 0.050008338007577074`,

so in particular `kappa(d_*)>1/20`. They also give singular mass at least approximately 0.414920125887338735. The strict decimal inequalities are supported by outward enclosures whose endpoints are not attained by the computed rational bounds.

Thus **any** counterexample, periodic or divergent, would have every weak odd-time occupation limit satisfying

`liminf_L (log_2 C_L)/L > 1/20`.

This is a necessary condition, not an exclusion. Nontrivial finite cycles would have collision exponent one, and are entirely consistent with the necessary condition.

## E5. The exact missing arithmetic theorem

A sufficient remaining statement is:

> For every fixed positive odd source whose orbit never reaches 1, at least one weak odd-time occupation limit has collision exponent `liminf_L (log_2 C_L)/L <= 1/20`.

E4 and this statement would prove Collatz. This statement is **OPEN**, not derived from stationarity, mixing, finite-state models, an almost-all theorem, or the computations here.

An explicit pair-count version clarifies what to attack. Write

`c_{N,L}(r)=#{0<=j<N : U^j(n)=r mod 2^L}`.

Along a common occupation subsequence `N_i -> infinity`,

`C_L=2^(L-1) lim_i N_i^(-2) sum_r c_{N_i,L}(r)^2`.

It would suffice, for each putative counterexample source, to find such a subsequence and finite source-dependent constants A,B with

`lim_i N_i^(-2) sum_r c_{N_i,L}(r)^2 <= A L^B 2^(-19L/20)`

for all sufficiently large L. The same source and the same subsequence must work across precisions. This is the proposed **fixed-source pair-recurrence target**.

The limits cannot be reversed. For a finite list of distinct integers, large enough precision separates every state; deleting diagonal pairs then misleadingly gives zero collisions. The occupation limit requires N to tend to infinity at each fixed precision before L tends to infinity. Conversely the diagonal contribution `2^(L-1)/N` is a finite-sample bias, not infinite-orbit concentration.

## Relation to the integrated repository and literature

The coefficient `H_2(log(2)/log(3))` already appears in the integrated native-horizon exceptional-mass results. This packet does not claim a new numerical entropy constant. Its contribution is the explicit conversion to every fixed-orbit occupation limit, including nonergodic limits, the optimal abstract collision boundary, and a source-specific pair-count target.

Parity coding is classical (Bernstein--Lagarias, linked in OCCUPATION.md). The proof above supplies the needed bijection and return-clock argument. The standard tools are Birkhoff's theorem, Jensen's inequality, entropy subadditivity, and Stirling's formula. No unverified recent claimed Collatz proof is a dependency.
