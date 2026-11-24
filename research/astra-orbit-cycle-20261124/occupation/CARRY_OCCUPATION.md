# Carry occupations and square-root separation from a critical mechanical word

**Status.** Proposed written mathematics and supplementary finite checks. The finite Lean kernels have a separate replay receipt. The asymptotic and arithmetic applications below are written proofs. Collatz remains open.

## Setup and exact dependencies

Let q_i be the positive odd ordinary orbit of the same fixed q_0, and let a_i=v_2(3q_i+1), so that 2^{a_i}q_{i+1}=3q_i+1. The actual scalar and its right-closed representative are from PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md, R10-G1–G3, and PR188 at beed685ab713923191ae40c9559bf7400298d2d3, research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md. Thus h_i=Σ_{j≥0}a_{i+j}/3^{j+1}, 1/2<h_i≤1+(log₂q_i)/3, and h_i=c_i+p_i with c_i a nonnegative integer and 1/2<p_i≤3/2. The canonical digit b_i=3p_i−p_{i+1} belongs to {1,2,3}; the exact carry equation is
a_i+c_{i+1}=b_i+3c_i.

Use ℓ=log₂3, K_n=Σ_{i<n}c_i, d_n=nℓ−Σ_{i<n}b_i, P_n=2^{d_n}, H_N=max_{0≤j≤N}d_j and E_n=∏_{i<n}(1+1/(3q_i)). Summing and multiplying the ordinary and carry equations respectively yields

    log₂ q_n + 2K_n = d_n + c_n − c_0 + log₂(q_0 E_n).             (1)

In particular the scalar bound c_n<1/2+(log₂ q_n)/3 gives

    (2/3)log₂ q_n + 2K_n ≤ d_n + 1/2 + log₂(q_0 E_n).            (2)

The hypotheses for the infinite distinct-state arguments are ordinary nonperiodicity, equivalent to injectivity of this infinite forward sequence. No moving-source passage is used. On a finite injective prefix the elementary bound
log E_j≤(1/3)Σ_{i<j}1/q_i≤(1+log(max(1,j)))/3
holds by ordering distinct positive integers. The stronger E_* = sup_n E_n <∞ follows on an infinite nonperiodic orbit from the sublinear counting estimate at PR182, a7fd3ac9e5bff7412858df23d776bb847e9c1371, research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md, §§1–6. Only Section 1 uses this stronger input. The existing PR182 round 12 result, cbec52dde5bed390a693310dd04e911033ba0cc9, research/phase-packing-round12-20261124/README.md R12-1–2, gives logarithmically weaker canonical occupation and superpolynomial growth for the critical zero-entropy branch. Its optimized local carry exponent is unnecessary here.

## 1. Exceptional clocks transfer the physical packing estimate without logarithmic loss

Let F(Y)=#{n:q_n≤Y} and C=q_0E_*. At any clock with c_n≤2K_n+c_0, (1) gives q_n≤C P_n. A remaining clock has c_n>2K_n+c_0≥2K_n, so K_{n+1}=K_n+c_n≥3K_n+1. This works even at K_n=0. At every selected clock with P_n≤X, (2) gives 2K_n≤log₂(CX)+1/2. Write T=max(0, floor((log₂(CX)+1/2)/2)) for X≥1. If r exceptional clocks are selected in increasing order, their masses before their respective updates obey K_{n_t}≥(3^{t-1}−1)/2 for t=1,...,r, by monotonicity between selections and the jump. Consequently

    #{n:P_n≤X} ≤ F(CX) + 1 + floor(log₃(2T+1)).                   (3)

This bound holds on every finite selection and hence globally. For θ=H₂(log₃2) the cited elementary physical count gives

    #{n:P_n≤X} = O_q(X^θ / sqrt(1+log X)),   X≥1.                 (4)

In fact (3) transfers any stronger PHYSICAL counting bound verbatim up to the double logarithm. The square-root logarithm in (4) alone does not imply summability at s=θ. For any fixed extra additive threshold on c_n−2K_n, only source-dependent constants change. The physical packing constant is uniform over the injective sets S. Its reciprocal moment estimate therefore bounds E_* by one absolute C_* across all positive nonperiodic sources (apply Σ1/q=∫_1^∞ F(t)t^{-2}dt using θ<1). Taking X to be the threshold for q_0 P_n, the preceding proof gives a source-uniform bound C X^θ/sqrt(1+log X), X≥1. Apply this to the actual suffix starting at any q_j to obtain the same estimate on all n≥j for the normalized multipliers q_j P_n/P_j. The selected-set argument and (2) are unchanged with q_0 X replaced by X. These arguments permit actual exceptional clocks.

## 2. The finite window inequality

For N≥1 put M_N=max_{0≤j<N}q_j and choose the least integer m≥1 with 3^m>M_N. Let p_b(m) denote the number of distinct length-m factors in the whole b-word (local factors from this prefix also suffice). Then on any injective prefix

    N ≤ m + (m+1) K_N + p_b(m).                                    (5)

Indeed remove the first m endpoint indices. A window ending at an index j in [m,N) uses the carries c_{j−m},...,c_j, inclusive. A positive carry can contaminate at most m+1 candidate endpoint indices, so at most (m+1)K_N windows are removed. In each remaining window every actual gap equals the canonical digit. For an actual length-m gap word w of total A and partial sums A_s with A_0=0 the full affine identity is

    2^A q_j = 3^m q_{j−m} + Σ_{s=0}^{m−1}3^{m−1−s} 2^{A_s}.

The multiplier 2^A is invertible modulo 3^m; hence w determines q_j modulo 3^m. Positive endpoints below 3^m are exact from this residue. Injectivity therefore bounds the remaining endpoint count by p_b(m). The argument also covers m≥N, when the right side is already ≥N.

By (2) and the elementary harmonic bound, m and K_N are each at most a source-dependent constant times 1+H_N+log(N+1). If p_b(m)≤C(1+m)^u for some u≥0, let v=max(2,u). Then (5) implies

    H_N ≥ c(q_0,C,u) N^{1/v}    for all sufficiently large N,       (6)
    max_{j≤N} P_j ≥ 2^{c(q_0,C,u) N^{1/v}}.

Here (5) first gives N≤C'(1+H_N+log(N+1))^v; the logarithm is o(N^{1/v}). In particular quadratic-complexity phases require stretched-exponential growth at every sufficiently large horizon. No entropy asymptotic, binomial estimate, or packing theorem is required. For comparison, if p_b(m)≤exp(Cm^a) with 0<a<1, (5) gives H_N≥c(log N)^{1/a} for all sufficiently large N: putting V=1+H_N+log(N+1), its right side is at most exp(C'V^a) eventually, and (log N)^{1/a} dominates log N. The finite inequality applies without a growth-class assumption as well.

## 3. Hamming-distance separation, uniform in intercept

Write α=ℓ−1∈(1/2,1). For real ρ let the baseline word be

    u_i(ρ)=1+floor((i+1)α+ρ)−floor(iα+ρ).

Every prefix of length j has sum within one of jℓ. The union of its length-m factor languages over ALL intercepts has at most m+1 words. Indeed the prefix as a function of fractional intercept changes only at the m+1 points −kα mod 1, 0≤k≤m, and the floor convention assigns each breakpoint to the interval on its right. Shifts of the starting index just change the intercept.

Let e be the number of positions in [0,N) where the actual canonical word differs from u(ρ). For all j≤N we have d_j≤1+e, since a baseline digit is at most 2 and an actual digit at least 1. By (2), m and K_N are O_q(1+e+log(N+1)). Mark every positive carry and every differing digit in the common index set [0,N); at most K_N+e positions are marked. An unmarked past window has its true gap word equal to the baseline. The proof of (5) therefore gives

    N ≤ m+(m+1)(K_N+e)+(m+1).                                      (7)

It follows that e≥c_q sqrt(N) for all sufficiently large N, uniformly in ρ. The intercept may be chosen anew, even adversarially, for each horizon. There is an absolute asymptotic constant. Put T_N=3/2+log₂(q_0)+(1+log(N+1))/(3 log 2). Then m≤1+3(e+T_N)/(2ℓ), K_N≤(e+T_N)/2. Since T_N=o(sqrt(N)) for fixed q_0, (7) implies

    liminf_{N→∞} inf_ρ e(N,ρ)/sqrt(N) ≥ 2 sqrt(ℓ)/3.

To see this, it suffices to take any sequence with bounded e/sqrt(N), divide (7) by N and take a subsequence where e/sqrt(N) tends to its lower limit. The resulting inequality is 1≤(9/(4ℓ))liminf(e/sqrt(N))². The same conclusion holds for the PHYSICAL gap word a itself. For that version, use d'_j=jℓ−Σ_{i<j}a_i≤1+e and the physical identity log₂q_j=d'_j+log₂(q_0 E_j); only the e disagreements have to be marked. Large positive gaps cannot invalidate the one-sided bound d'_j≤1+e. Here m≤1+(e+T_N)/ℓ, and N≤m+(m+1)e+(m+1), giving the stronger absolute asymptotic constant sqrt(ℓ) on the physical gap word.

For an eventually periodic ordinary trajectory both gap and canonical words are eventually periodic (the deterministic discounted sum is periodic on the cycle). Their eventual means are rational, distinct from the irrational ℓ, and their digits are bounded along this fixed trajectory. Comparison of prefix sums shows e=Ω_q(N) for each, uniformly in ρ. Thus the square-root conclusion holds for every positive odd source; the nonperiodic proof is the substantive case.

### Insertions, deletions, and independent changes of intercept

The same constants hold for Levenshtein distance from either actual prefix to the union of ALL mechanical factors of arbitrary lengths. Fix an alignment with e edits. At a given actual prefix choose the matched prefix of the baseline determined by this alignment, stopping when that actual prefix has been consumed (trailing baseline-only deletions may be discarded). Its discrepancy is less than one. An actual-only letter x contributes ℓ−x≤ℓ−1<1 to the discrepancy difference; a baseline-only letter u contributes u−ℓ≤2−ℓ<1; a substitution contributes u−x≤1. Matches contribute zero. Thus d_j≤1+e for every j, exactly as before. Mark the position of any actual-only letter or substitution, and the next actual position after a baseline-only deletion when one exists. A clean window containing no such position consists of matched letters aligned to a contiguous baseline factor. The number of marks is at most e. With the same positive carry marks for the canonical version, (7) and both constants follow.

There is a stronger description allowing unrelated intercepts on different fragments. Partition a prefix of N actual symbols into r nonempty contiguous pieces, each either a critical mechanical factor of arbitrary intercept or one arbitrary positive symbol. Every prefix has positive discrepancy ≤r: each complete or partial mechanical piece contributes less than one, and a singleton x contributes ℓ−x<1. Mark only the first index of each piece. Any past window avoiding these r marks lies inside a single mechanical piece, since any nonempty singleton piece would itself be marked. Thus (7) applies with e replaced by r. It follows that the minimum number of such pieces, divided by sqrt(N), has lower limit at least 2 sqrt(ℓ)/3 for the canonical word and sqrt(ℓ) for the physical word. No common intercept, alignment across pieces, or fixed prechosen decomposition is assumed. For an eventually periodic physical or canonical word, let W be its finite digit bound. If its mean exceeds ℓ, each whole mechanical piece contributes a negative discrepancy of magnitude less than one, and even an arbitrary singleton contributes one of magnitude at most W+2. If its mean is below ℓ, positive discrepancy is already at most r. Hence r=Ω_q(N) in this case too. The same bounded-digit two-sided estimate applies to arbitrary edit alignments and shows their linear lower bound for periodic tails.

## 4. Explicit excluded irrational phases with superpolynomial canonical expansion

For one concrete family put ρ=0. For each k≥2 lower to 1 the first baseline digit equal to 2 at an index ≥k³. Its distance from k³ is at most one because α>1/2 (the mechanical word has no two consecutive 1s). The selected indices are distinct. For the resulting word v, jℓ−Σ_{i<j}v_i=j^{1/3}+O(1); hence P_j=2^{j^{1/3}+O(1)} eventually exceeds every fixed polynomial. But v disagrees with this baseline at only O(N^{1/3}) indices. Section 3 excludes v from every positive ordinary scalar phase and every ordinary physical gap sequence. The same proof works for ANY arbitrary changes at o(sqrt(N)) positions in [0,N) along an unbounded sequence of horizons; there is no assumption that their locations follow a substitution, or even a computable rule.

The example really defines an infinite irrational canonical phase: p=Σ_{i≥0}v_i/3^{i+1} has all suffixes in (1/2,3/2] and produces exactly these canonical digits. The asymptotic frequency of 2 is the irrational α, so the word is not eventually periodic. A rational centered phase would have eventually periodic ternary digits; hence p is irrational. This exclusion applies to every admissible integer translate of p and to all intercepts. As a separate complexity check, v has O(m²) distinct length-m factors. Before a cutoff O(m^{3/2}) there are only that many starts; beyond it the selected cubic indices are separated by more than m, so each length-m factor is obtained from one of the ≤m+1 baseline factors by at most one replacement of a 2 by a 1. This gives at most (m+1)^2 late factors. Thus Section 2 independently excludes this example. Round 12's necessary superpolynomial expansion and its critical zero-entropy density statement alone allow its numerical drift profile.

## Remaining gap

Arbitrary ordinary gap or scalar words are not known to shadow one critical mechanical word with o(sqrt(N)) Hamming error on any subsequence. Arbitrary critical words may have higher complexity, larger fluctuations, or both; low rational phases have linearly growing canonical drift. Equations (3)–(7) give necessary conditions and explicit excluded families, with no upper bound covering all actual nonperiodic orbits and no exclusion of all nonstandard cycles.

## Finite controls and verification boundary

Run `python -B carry_controls.py` and `python -O -B carry_controls.py`; the two outputs were compared byte-for-byte with CONTROLS.json. The script uses exact fractions for scalar computation on ordinary trajectories ending at 1, exact integer powers for the mechanical baseline, and an explicit failure on its stopping-oracle guard. It checked 1,480 distinct-state prefixes of 500 selected starting odd values (the trivial source 1 is skipped for prefix tests), 10,548 full past residues, 8,880 Hamming inequalities, 7,400 finite occupation inequalities, 128 minimum-piece dynamic-programming parses and 384 optimal edit alignments. The 708 exceptional occurrences counted over these overlapping sample horizons show why a pointwise constant-factor physical comparison may not be inferred from the proof. A deliberately constructed finite carry script with two maximum-growth bursts and full resets tests the geometric mass bound, including an exceptional index at mass zero. The script is not asserted to be an infinite ordinary trajectory. None of the controls tests Collatz over an unbounded range.

CarryOccupation.lean, SHA-256 2ea3ba93c2939c77646a56a05d8d0f24b819fe6f515e2094330ae239d4fef9a6, compiled with standalone Lean 4.34.1, warnings as errors, exit 0. LEAN_REPLAY.txt records the exact command, version and six axiom reports. The file proves the exceptional jump, the power bound for successive selected masses (including zero), marked-window membership, the exact size of the interval list with multiplicity, the bound on the number of positive carries, and the finite count given a covering and duplicate-free dictionary words. The applications verifying the cover and word uniqueness on the actual orbit, the scalar identities, limiting constants, occupation asymptotics and explicit infinite family remain written mathematics here.
