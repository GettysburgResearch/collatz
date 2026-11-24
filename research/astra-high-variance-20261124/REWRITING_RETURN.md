# A finite total phase budget for the whole delayed residual execution

**Status.** Written proofs. The total budget and eventual exact binary-clock identity concern the actual generated return process of ARITHMETIC_RETURN.md. They need no hypothesis on the distribution of return states. All-cycle exclusion and ordinary convergence remain open.

## The delay disappears from the sum

Let (q_i) be an injective positive odd orbit. At its j-th generated mark n_j=q_{t_j}, put s_j=r(n_j) and R_j=(floor(log₂ n_j)+2)^3. The exact equal-clock merger gives U^{R_j}(s_j)=q_{t_j+R_j}. The return search restarts only AFTER settling and takes a positive number of odd steps. Thus the intervals [t_j,t_j+R_j) are pairwise disjoint. This argument is for the generated delayed chain; arbitrary marked visit times can have overlapping settlement intervals.

For each integer time k=t_j+h in those intervals, choose either q_k or U^h(s_j), independently for each k. The resulting set of chosen integers is admissible in PR193's sense: at every common nonnegative odd clock the images of distinct choices at distinct times are distinct. Indeed, if two images coincide, advance both by the same further clock past both remaining settlement delays. The result would be equal q-values at two distinct ordinary times. This also proves that none of the originally chosen integers repeat. Use both choices separately if costs on both paths are to be counted. The omitted times can also be filled by the actual q_k.

Write θ=H₂(log 2/log 3)<1 and ε(z)=log₂(1+1/(3z)). PR193 bounds admissible sets in any interval of length L≥2 by C L^θ/√log(2L), uniformly. The critical sharpened count follows from its common-clock bound, since the image map on an admissible set is injective. Summing over dyadic intervals above H≥2 bounds the sum of ε(z) there by C H^{θ−1}/√log(2H). The contribution below 2 is bounded absolutely. Apply this twice to obtain the uniform genuine-source budget

    Σ_j Σ_{h<R_j} [ ε(q_{t_j+h}) + ε(U^h s_j) ] ≤ C.             (1)

The disjoint-cost argument was independently obtained in the arithmetic lane using the minimum representative at each intrinsic clock; see ARITHMETIC_COST.md. The constant is absolute, including over starting sources. The same upper-tail estimate applies if only entries ≥H are counted. Even the sum of the larger of the two corrections at each time is bounded by one application of the estimate. This construction of a transversal through whole replacement paths is the point of using the actual delays, which can grow arbitrarily.

Let d_j=floor(log₂ n_j), e_j=floor(log₂ s_j), X(z)=log₂ z−floor(log₂ z), and let A_j and B_j be the total numbers of halvings in the R_j accelerated odd steps of the original and replacement arms, respectively. Exact telescoping to their common endpoint gives

    A_j−B_j−(d_j−e_j) = X(n_j)−X(s_j) + E_j−F_j,               (2)

where E_j and F_j sum ε on the respective arms. The left side is an integer. Both n_j and s_j tend to infinity because their ordinary time tags are distinct, hence each sequence consists of distinct positive integers. Both are marked, so 0≤X(n_j)≤log₂(1+70/(d_j+1)) and likewise for s_j. By (1), E_j+F_j tends to zero. For every sufficiently late tile the integer in (2) must equal zero. In particular,

    A_j−B_j = d_j−e_j ≥ 0,
    Σ_j | X(n_j)−X(s_j) | < ∞.                                 (3)

There is even an absolute bound on the number of exceptional tiles: fix one large octave threshold past which both marked phase sizes are <1/4. Each arm's distinct starts account for only boundedly many smaller starts. Every remaining nonzero integer in (2) requires E_j+F_j≥3/4, charged to (1). These statements control the full binary-clock cost of the actual rewrites between equal odd clocks. Small signed discrepancies of the logarithmic mantissas have finite total absolute cost. They do not bound the sum of the nonnegative octave drops in (3).

[PR193, escape.md, §§1a–1b, c6cb5e66516a86c33a757154983bbddc822510de](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/escape.md) · [PR182, critical residual construction, 9b02334f27ff59694a91fe7f018e0aaabad7620b](https://github.com/GettysburgResearch/collatz/blob/9b02334f27ff59694a91fe7f018e0aaabad7620b/research/astra-round13-20261124/LATEST_BAND.md).

## Quantitative shrinking arcs without a tightness assumption

Fix effective constants c>0 and κ≥1 for which ||h alpha||≥c h^{−κ} for every positive h, alpha=log₂ 3. Matveev's two-log bound supplies them: take h log 3−a log 2 with a nearest integer to h alpha, fixed bases 3 and 2, nonzero by unique factorization, and integer coefficients O(h). A sharper direct source gives every κ>4.1163051. Wu and Wang, Theorem 1, bound |p+b ln 2+c ln 3| below by H^{−4.1163051−δ} for all integer p,b,c with H=max(|b|,|c|) above an effective threshold depending on δ>0. Take p=0, b=−a, c=h. Then H is comparable to h; division by ln 2 and shrinking the constant to cover the finitely many remaining h prove the assertion. In particular take κ=17/4 throughout. The argument uses their simultaneous linear-form theorem, rather than a single-logarithm irrationality measure. The implied constant here is effective but has not been evaluated.

For N consecutive distinct states of an injective trajectory or one simple periodic lap, let x_i=X(q_i), e(y)=exp(2πiy). Such states are admissible, including on a primitive cycle because later common iterates permute its states. Thus Σ ε(q_i)≤C independently of length. Telescoping the phase equation from REWRITING_FRONT.md gives

    |1−e(h alpha)| · |Σ_{i<N} e(hx_i)| ≤ 2 + 2π h Σ_{i<N} ε(q_i).

By Erdős–Turán, the absolute interval discrepancy of the empirical probability is at most C(1/H + H^{κ+1}/N). Take H comparable to N^{1/(κ+2)}. Uniformly in the starting source, arc and clock, the discrepancy is O(N^{−1/(κ+2)}), in particular O(N^{−4/25}). For a finite collision-free prefix of an eventually periodic orbit that may enter a cycle later, admissibility need not hold. On that larger class elementary harmonic summation over the distinct positive states gives an extra log(2N) in the numerator of the H term. This distinction matters when invoking the uniform packing input.

If all sampled states are at most M, a phase arc [0,c₀/(1+log M)] with fixed sufficiently small positive c₀ lies inside the mark section for every state. Consequently when (1+log M) N^{−1/(κ+2)} tends to zero there are at least c₁ N/(1+log M) marks, for a fixed c₁>0 and all sufficiently large windows. This is a quantitative theorem about ordinary times before imposing delayed sampling. A rate from phase errors tending to zero alone would not follow. At exponential heights, the required mark arc can have width of order 1/N, much below the discrepancy scale just established.

[Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [Matveev, Corollary 2.3](https://www.mathnet.ru/eng/im314) · [Erdős and Turán, original discrepancy paper](https://users.renyi.hu/~p_erdos/1948-03.pdf).

## A polylogarithmic clock to a marked source

There is an absolute effective C such that from every positive odd n there is a marked visit within C(1+log n)^κ odd steps, in particular O((1+log n)^{17/4}). Increasing the constant gives the same conclusion on the ordinary shortcut clock. This improves the square-root clock in PR173 by importing the two-log lower bound. It does not reduce PR182's independent settlement delay.

For a sufficiently large current n put d=ceil(log₂ n) and choose an integer N comparable to (d+2)^κ, with constant large enough that cN≥(d+2)^κ. Dirichlet gives coprime a,q with 1≤q≤N and |q alpha−a|≤1/N; reduction of the fraction preserves this bound. Hence q≥d+2. If any of the first q iterates falls below 4N², restart there. For sufficiently large n the new starting octave satisfies ceil(log₂(4N²))≤d/2 because N=O(d^κ). Otherwise corrections up to that time are at most 1/(4N²) per step, so the total perturbation before q steps is at most 1/q. The residues x(n)+ja/q for 0≤j<q form an equally spaced grid. Choose a point in [2/q,3/q] modulo 1. Replacing a/q by alpha moves it by at most 1/q and the positive ordinary perturbation by at most a further 1/q. For large n, the attained phase therefore lies in [1/q,5/q]. Since U(z)≤2z, its octave index D is at most d+q. For sufficiently large q, 2^{5/q}−1≤10/q≤70/(D+1), proving the exact marked inequality. A successful trial costs ≤N odd steps; every failed one at least halves the binary octave index. Summing the geometric series in d^κ therefore costs O((1+log n)^κ) odd steps. The finitely many starts below the fixed cutoff use PR173's unconditional visit theorem; alternatively use its explicit upper clock there. Summing all costs proves the claim. For the shortcut clock telescope total gaps A along J odd steps: 2^A q_end≤4^J n gives A≤2J+log₂ n. A strictly positive marked return follows by starting at U(n), whose size is at most 2n.

[PR173 actual forward section and previous clock](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean).

## A divergent integer cost on every cubic-delay arm

There is an unconditional resource debit larger than any fixed multiple of log d. Uniformly over **all** positive odd starting integers z≤2^{d+1}, a section of R=(d+2)^3 odd steps contains ω(log d) indices with a_i≥2 as d→∞. In particular the total extra consumption Σ(a_i−1) also is ω(log d). This applies separately to both arms of every sufficiently high residual tile, without requiring a nonperiodic orbit. Continue the ordinary map on its fixed odd state 1 when needed.

Indeed expand the segment into its literal L=Σ a_i shortcut inputs. Split the resulting word into k maximal constant-bit runs. Their affine centers are 0 and −1. Neither can fix a positive entry. Apply the fixed-dimensional **open segment** estimate (2) of the reviewed CYCLE_EXTENSION.md to successive groups of at most m runs, with d_den=1 and constant center height. At a boundary put Y=z_boundary+6. Within each group of length ell one has ell log 2≤2 log Y +O_m(1), choosing the epsilon parameter 1. Each shortcut increases Y by at most a factor 3/2. Therefore for an absolute ρ=1+2 log₂(3/2)>1, iterating gives L≤C_m ρ^{ceil(k/m)}(1+d). This uses only the open segment estimate; a periodic starting point and the cycle-minimum rotation are unnecessary. Since L≥R, one obtains liminf k/log d ≥2m/log ρ for each fixed m. Sending m to infinity proves k/log d→∞. Every zero run comes from a distinct odd gap ≥2; a binary word with u zero runs has at most 2u+1 runs in total. This proves both assertions.

The uniform assertion uses Evertse's Corollary 1 as in the cited written estimate. The lower cost can remain o(R), so it does not force more than αR halvings. The exact equality (3) makes the difference of the two arms' costs the octave drop, while the new bound applies to each arm's separate baseline consumption. Subtracting the separate lower bounds would be invalid. [Open-segment estimate and its arithmetic hypotheses](../astra-closure-attack-20261124/CYCLE_EXTENSION.md).

## Test of recurrence

For the full fixed-source orbit, (1) applied to the actual trajectory yields a limiting rotation phase, already implicit in prior reciprocal-summability work. For the marked replacement chain, (3) establishes absolute summability of changes to the fractional phase. It leaves the integer octave coordinate and physical sampling times free to grow. A shrinking mark can be reached repeatedly at increasing heights with arbitrarily small positive mass s_j^{−θ}. In particular, an identity projection at a mark charges zero in (2) for its fractional discrepancy and zero for its octave drop, irrespective of the positive settlement time. The theory gives no requirement that the eventual projections be proper with enough frequency. Even a proper octave drop is exactly offset by fewer trailing consumptions on the alternative arm, so adding this drop twice to a budget would be incorrect. No invariant probability on the countable return states follows from the compact phase marginal. The source still needs an independent resource that bounds those integer octaves or forces quantitative progress on the settled observations.

The analytic bounds, common-clock admissibility and whole-path budget in this file are written arguments. No Lean verification of these theorems is claimed.
