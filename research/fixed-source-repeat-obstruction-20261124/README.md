# Fixed-source repeated-factor obstruction: all finite digit-weight scripts

Date: 2026-11-24. **Status: PROPOSED written proofs and exact arithmetic controls; Lean source supplied but compiler replay pending. Collatz remains OPEN.**

This attacks the explicit surviving fifth automatic family in PR182, R10-A3, and the critical ordinary-source branch. It strengthens the previous lacunarity mechanism by comparing *two actual states on the same fixed orbit*. No change of source with horizon is allowed. The result excludes every finite popcount cap, and more generally every finite nonzero-digit cap in every integer radix, for rational physical sources of either sign. It does not exclude all arbitrary L/P schedules or establish universal triadic membership.

## Frozen inputs and context

* PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ARITHMETIC_TOWER.md, R10-A1--A4: exact L/P cylinders, shifted recurrence, symbolic scalar 7/8, lacunarity obstruction for caps 1--4, explicitly inconclusive at cap 5.
* Same head, research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md, R10-G1--G3: actual scalar construction and Lean convergence iff triadic membership. GENERAL_PHASE_RETURN.md and RETURN_TOWER.md: finite paid returns, changing centers and actual finite expanding towers.
* PR182 at a7fd3ac9e5bff7412858df23d776bb847e9c1371, research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md, §§1--6: count of distinct ordinary orbit states and reciprocal moment. PR175 at 67664c6bf555bf7f7fcec987acb79500071dce4b, research/lean-global-closure-20261121/risk26/root/UNCONDITIONAL_CYCLE_BOUNDARY.md, §4: finite E-infinity normalization for actual escaping rays.
* PR183 at 68345f60a4f757acb42a69a4ac95910f8ce26163: independent repeat-block arithmetic; unlike that result we compare two possibly separated occurrences, without assuming a bounded collection of repeated atoms.
* Main at ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a, research/integrated/factor-complexity/README.md: the resident 64-to-81 centered-cylinder recurrence-cone argument is an important antecedent. The mechanism is credited; the present affine word, complete ordinary source, and all-cap application differ. No broad priority claim.

Related attacks inspected: PR173/184 forced band and exact source-bounded mergers; PR177 all-template bounds and arithmetic-germ criterion; PR178/185 full numerical denominator after polynomial cancellation; PR180 original-law collision/Fourier interface; PR176 original-source edit and occupation bounds; PR174/179/181 reverse closure and finite-budget induction. None provides the required global ordinary-source assertion. This packet imports none of their unproved global hypotheses.

## 1. Full shifted affine law on rational sources

Use U(q)=(3q+1)/2^g, g=v2(3q+1), on rational q in Z_2^× (when g is finite). The prescribed two-odd-step blocks are L=(2,1), P=(1,4). Their exact maps are L(q)=(9q+7)/8 and P(q)=(9q+5)/32. For s_j=0 or 1 respectively, X_j=q_(2j)+7 satisfies

    8*4^(s_j) X_(j+1) = 9 X_j + 166 s_j.          (1)

This is R10-A1's law; it also holds for negative ordinary states and rational 2-adic odd states following the specified finite valuations. Write q=a/d in lowest terms, d>0 odd, and Y_j=d X_j. All Y_j are integers: when q_i has numerator a_i over the same odd d, exact division by 2^g gives another integer numerator over d. Cancellation of common odd factors is unnecessary. Therefore

    8*4^(s_j) Y_(j+1) = 9 Y_j + 166 d s_j.         (2)

With B=|Y_0|+42d, for every realized prefix,

    |Y_j|+42d <= (9/8)^j B.                       (3)

Indeed the L map is multiplication by 9/8; P gives |Y'| <= (9/32)|Y|+83d/16 <= (9/8)|Y|+83d/16, and 83/16<42/8. Induct. No positivity is required. For a positive ordinary source one may instead use X_j>0 and the sharper R10-A1 bound X_j<=(9/8)^j(q+7).

## 2. The shared-factor cone (FSR-1)

If a single rational source has two identical length-h block words beginning at i<j, let S count their common P letters. Subtract the complete affine equations, iterated over the two aligned blocks. Every additive term cancels, giving

    8^h 4^S (Y_(j+h)-Y_(i+h)) = 9^h (Y_j-Y_i).

As gcd(8,9)=1, this implies

    8^h | (Y_j-Y_i).                               (4)

This is ordinary integer divisibility; it is not a fresh congruence sample. If the states differ, (3) and (4) imply

    8^h <= |Y_j-Y_i| <= 2B (9/8)^j.                (5)

Consequently, if 2B(9/8)^j < 8^h then the states coincide. An infinite literal script must thereafter be periodic with period j-i (not necessarily its least period), since U and its valuations are deterministic. For a positive ordinary source, replace 2B in (5) by q+7 using the sharper bound and positivity. This yields the explicit cone: an aperiodic rational physical L/P script with equal factors must satisfy 3h <= log2(2B)+j log2(9/8).

The asymptotic repeat threshold is 3/log2(9/8)=17.654847... . This matches the slope of the historical centered model because (9/8)^2=81/64; we are not claiming a new numerical constant. The stronger useful datum for the present family is the *position of the repeated factor*, not a generic factor-complexity bound.

## 3. Every finite digit-weight cap is excluded (FSR-2)

Fix an integer radix b>=2 and k>=1. Select P at precisely the positive indices with at most k nonzero digits in radix b. All other indices select L, including index zero. For b=2 this is the entire popcount family of R10-A3.

Let h=b^m. For 0<=t<h, both h+t and 2h+t have exactly one nonzero high digit, plus the same low digits of t (for b=2 the leading 2 carries into the next position, still one high digit). Hence

    s_(h+t) = s_(2h+t) for all 0<=t<h.              (6)

If a fixed rational physical source realizes the script, apply (5) at i=h,j=2h. Whenever 4^h>=2B,

    2B(9/8)^(2h) <= (81/16)^h < 8^h.

Thus Y_h=Y_(2h). To contradict even finite realization, choose h>=b^(k-1) and let t=1+b+...+b^(k-2) (t=0 when k=1). Then t<h has exactly k-1 nonzero digits. The indices

    J=(2b-1)h+t,   J+h=2b h+t

have k+1 and k nonzero digits respectively (2b-1 has two nonzero digits; 2b has one, also when b=2). Therefore s_J=0 and s_(J+h)=1. Equality of states at h and 2h would force equality of these two letters by determinism, provided the corresponding finite prefix were realized. This is impossible.

**Explicit finite mismatch budget:** take h to be the least power of b with h>=b^(k-1) and 4^h>=2(|a+7d|+42d). The prescribed first (2b+1)h blocks, i.e. 2(2b+1)h actual odd gaps, cannot all match. The same budget with 4^h>=q+7 suffices for positive ordinary q. The bound depends on one fixed source, not the minimum lift of each finite cylinder.

In particular ALL k>=1 are excluded, including k=5 and beyond, with no lacunarity ratio condition and no imported transcendence theorem. All these scripts still have symbolic scalar 7/8 and all finite words have positive ordinary lifts (PR182 R9-A2--A3); the result is precisely the failure of one rational infinite lift.

PR182 R10-A2 identified the physical completion q_*=-7-(166/9) F_s with F_s=sum_(r>=0)4^r(8/9)^(t_r) in Q_2. This completion exists uniquely by the full odd-terminal cylinders. If it were rational, it would have odd denominator and follow every prescribed finite gap, contradicting FSR-2. Thus q_* and F_s are irrational for every b,k above. This does not equate the real and 2-adic values.

## 4. A universal repeat/height obstruction for actual critical orbits (FSR-3)

Let q_i be a fixed injective positive odd U-orbit, g_i its positive gaps, and M(N)=max_(0<=i<=N) q_i. If two length-m gap words at i<j coincide with total gap A, subtract their actual affine equations:

    2^A (q_(j+m)-q_(i+m)) = 3^m (q_j-q_i).

The two endpoints are odd. Coprimality and A>=m imply 2^(A+1) divides q_j-q_i. Injectivity gives |q_j-q_i|>=2^(m+1). Hence for every N,m>=1,

    M(N)<=2^(m+1)  =>  the N+1 gap words at 0,...,N are pairwise distinct.

Let p_g(m) count all distinct length-m factors, allowing infinity. If p_g(m) is finite, M(p_g(m))>=2^(m+1)+1. In particular:

* If log q_j=o(j), then p_g(m)/m -> infinity (in extended reals). For every fixed C>0 take N=floor(Cm); the maximum M(N) has log M(N)=o(N), hence the N+1 factors must be distinct for sufficiently large m.
* If q_j<=K(j+1)^D for fixed K,D>0, then p_g(m)>=( (2^(m+1)+1)/K )^(1/D)-1, an exponential factor-complexity lower bound. This is a necessary condition, not a proved polynomial envelope for an escape.
* A finite-alphabet radix-b automatic word has p_g(m)=O(m). To see this directly, pad the digit automaton with a leading-zero initial state, take the least b^r>=m, and consider aligned length-b^r blocks. Each block is determined by the state after reading the prefix index. Each length-m factor lies inside two consecutive such blocks and is determined by their two states and one offset, giving at most |Q|^2 b^r <= b |Q|^2 m factors. Thus **no injective positive ordinary orbit of subexponential height can have an automatic gap sequence**, in any integer radix. The same argument applies to any coding with linear factor complexity.

To attach to the central critical branch without assuming independent words, use PR182's injective-orbit count and PR175's UB8--UB9 on exactly this orbit. Writing A_j=sum_(i<j)g_i, the normalization E_j=2^(A_j)q_j/3^j tends to a finite strictly positive E_infinity. Then

    log_2 q_j = j log_2 3 - A_j + log_2 E_j.

If A_j/j -> log_2 3 (the critical branch), log q_j=o(j), so the preceding superlinear-complexity exclusion applies. This is a consumer of the actual count, not a proof of criticality for every escape or an exclusion of high-complexity critical words. It avoids changing the selected source or probability law.

## 5. Full-proof attempt and first unproved step

The rational scalar phase and physical itinerary are different objects. PR182's actual h(q) belongs to Z[1/3] iff q reaches 1; rational phase with fixed denominator does NOT force automatic carries. Indeed even the L/P two-block sublanguage admits arbitrary symbolic binary scripts. The new arithmetic result therefore attacks an actual explicitly surviving unbounded family, but does not justify assuming all low-phase returns lie in it.

Potential next theorem for the L/P branch: prove that every aperiodic *ordinary-realizable* schedule has an efficient recurrence violating (5), or find a different ordinary arithmetic obstruction to high-complexity schedules. For arbitrary gaps at critical height, an analogous target is to prove a low-complexity bound from the complete source-specific carry equations, not to assume it from finite phase or iid statistics. Generic stationary words can have exponential factor complexity and escape these tests.

The central outstanding claims remain universal triadic membership (PR182), full cycle denominator cancellation obstruction (PR175/178/185), ordinary same-law collision upper bound (PR180/185), and source-bounded merger coverage (PR173/184). No one of the results above settles any of these universally. The present mechanism also does not exclude periodic L/P schedules: those are a separate complete cycle-divisibility problem.

## 6. Evidence

RepeatObstruction.lean supplies a proposed Mathlib proof of the finite integer divisibility core (including variable complete denominators and the equality consumer), with no custom axiom or sorry intended. The available execution container has neither Lean nor Lake and cannot resolve GitHub hosts; no Lean compilation, full repository validator or axiom-audit result is claimed. Rebuild with Lean 4.34.1 and Mathlib as used by PR182/185, then run the listed print-axioms commands.

controls.js replays finite digit-weight factors, literal rational L/P words with odd denominator, the shared-block divisibility and size test, and finite mismatches for small ordinary and signed rational sources. These are finite exact arithmetic controls, not the proof of the universal written statements. Run with Node.js; it uses BigInt and explicit errors rather than disabled assertions.
