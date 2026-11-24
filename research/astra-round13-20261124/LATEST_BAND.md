# Decidable residual marked sources with a finite critical-power sum

**New written theorem.** For the ordinary shortcut Collatz map there is an explicit decidable set S of positive marked integers such that universal convergence is equivalent to convergence on S, and

$$\sum_{n\in S}n^{-\theta}<\infty,\qquad
\theta=H_2(\log 2/\log 3)=0.9499555\ldots.$$

This is a reduction, with convergence on S open. Its analytic input is the written translated-interval synchronization theorem in PR193. Its marked descent input is the checked Round 13 packet in PR182 at cf1f04db7f9f84d3a31bfccf2546431b711312d0. The full new reduction is a written proof.

## Construction and equivalence

Write F for the shortcut map, u(z) for the odd part, and U for the map q↦u(3q+1) on positive odd integers. In octave d use the full inclusive interval

    I_d=[2^d, min(2^(d+1)−1, 2^d+floor(70·2^d/(d+1)))],   L_d=|I_d|.

Its odd elements are precisely that octave's marks. At the explicitly chosen common odd clock R_d=(d+2)^3, partition **all** its integers into fibers of E_d(z)=U^(R_d)(u(z)). Run the Round 13 mixed half-partner rules on each odd member for at most d+1 returns, testing the terminal condition before and after those returns. Use its canonical decomposition z=2^(k+1)v−1 with v odd, starting parameter b=3^k v−1. The disjoint tests are b≡2 mod4 (accept), b=2t+1 (return to 3t+2), and b=64t+56 (return to 9t+8). Failures and timeouts simply supply no certificate.

Discard each fiber containing any even member, or any odd member accepted within the budget. From every other fiber retain just its least member; their union over octaves is S. Membership takes finite integer operations and finite enumeration of a specified interval. It requires no decision about an infinite mixed return sequence and no knowledge of the synchronization theorem's unspecified constants.

To justify discarding an entire fiber, first note that deleting a low binary bit preserves the section inequality. If z=2q+e, q>0 and e∈{0,1}, write j=floor(log₂ q) and a=q−2^j. Then the old octave index is j+1 and the old offset 2a+e. The old inequality (j+2)(2a+e)≤140·2^j implies (j+1)a≤70·2^j. Iterating this implication proves section membership for every positive binary ancestor, including the odd part formed by deleting all trailing zeros. A mark must additionally be odd.

- If a fiber contains an even z, its positive odd part y is marked by the deletion lemma, and y≤z/2<2^d. Every marked n in that fiber shares its ordinary endpoint with y, since U^(R_d)(y)=E_d(n).
- If it contains an accepted odd z, the checked half-partner construction merges z with x=(z−1)/2>0. Its odd part y is marked by deleting the final bit of z and then the trailing zeros of x. It too satisfies y≤x<2^d, regardless of whether z exceeds n. The future of n intersects that of z by the common odd clock. Orbit intersection for a deterministic map is transitive, so convergence of y implies convergence of n.
- For an undiscarded fiber, any nonminimal member n has a strictly smaller marked partner in the same fiber. Its minimum belongs to S.

Strong induction on marked n therefore proves all marks converge if S does. PR173's actual forward visit theorem then proves all positive sources converge. The reverse implication follows immediately. This induction compares the partner to the marked source currently under induction. The ordinary source before its first band visit need not be larger than that mark.

## Size

PR193 bounds the number of distinct odd endpoints from *any* integer interval of length L by C L^θ/√log(2L) after ceil(K(log₂(2L))²) common odd clocks. Later common clocks cannot increase this number. Here log₂(2L_d)≤d+1, so R_d dominates the required clock from some finite d onward. A change to the constant absorbs the finitely many exceptions. For large d, L_d is asymptotic to 70·2^d/d. We obtain

    |S∩I_d| ≤ C' 2^(θd)/d^(θ+1/2).

Each n in this octave contributes at most 2^(−θd) to the displayed series, and θ+1/2>1. This proves convergence, including at exponent θ. No independence between accepted binary scripts and synchronized endpoints was used. One cannot multiply separate counting savings on that basis.

The counting input groups a length floor(log₂ L) shortcut prefix by odd count p. Each class has a translated image interval of width at most 2·3^p+(3/2)^floor(log₂ L)+O(1), with no dependence on the translation. The upper binomial tail gives the square-root logarithmic gain; summing the separate subcritical widths and inducting on shorter intervals retains it. The identity u(F^k z)=U^p(u(z)) advances the correct odd clock. Finite transport identities were reported Lean-checked by PR193; the complete counting theorem remains written. One nonconvergent fiber minimum is compatible with the cardinality bound or the convergent series. Neither argument forces an even or accepted odd member in every fiber.

## Guarded visits and ordinary predecessors

PR193's ternary guard at h=0 selects odd r≡121 modulo 162 and returns the smaller m=(64r−49)/81 at the endpoint F(r). PR194 LS3 therefore bounded a guarded visit on the orbit of a least ordinary nonconverger n₀ by 64r≥81n₀+49. There is a stronger conclusion at the original endpoint r. For any s with 3^s dividing 2r+1 let z=(2r+1)/3^s and x=2^s z−1. The first s odd-run clocks give F^s(x)=3^s z−1=2r; one halving gives F^(s+1)(x)=r. For s≥2, 2·2^s<3^s, which gives 0<x<r. Thus there is already a physical smaller predecessor for odd r≡4 mod9. This is a direct application of the existing odd-run identity; no priority claim for that identity or inverse-word construction is intended.

For r>0 the x above is positive also when s<2 (s=0 gives x=2r, s=1 gives x≥1). Taking s=v₃(2r+1), an ordinary least nonconverger n₀ must satisfy

    (3/2)^s ≤ (2r+1)/(n₀+1)

at every visit r, since x would otherwise be a smaller nonconverger. On the specific PR194 guard, s=4 is always available. Put r=162t+121; the partner is 64t+47, and F⁵(64t+47)=r. Therefore **32r≥81n₀+65**, strengthening LS3. No guarded visit within this stronger threshold has been forced. For guarded marked r/2^d→1, the partner (32r−65)/81 has limiting normalized octave mantissa 128/81, separated from 1. Hence the guarded partner in general fails to remain marked. This ordinary predecessor theorem alone cannot discharge a residual marked minimum.

## Compatibility with the independent-clock obstruction

The linear-horizon family in Round 13 rules out two specific tests: direct descent through 3T+1 shortcut clocks and a merger with the canonical half-partner through independent clocks 3T+1 and 3T. It does not rule out PR193's alternative partners. Indeed, for T≥8 put k=2T and choose 1≤r≤81·2^T by CRT so that

    3^k r≡1 mod 2^T,    2^(k+1)(2^(2T−1)+r)−1≡40 mod 81.

Both coefficients are units for their respective moduli, which are coprime. Put v=2^(2T−1)+r and n=2^(k+1)v−1. Then n is odd with the h=0 guard, v is odd, and 2^T divides 3^k v−1. The offset of n above 2^(4T) is below 162·2^(3T), within the octave for T≥8. It lies in the marked band since 162(4T+1)≤70·2^T for T≥8 (check T=8 and induct). Also v>4·2^T. These are precisely the hypotheses used for shared parity prefixes, slope spacing, and intercept separation in LINEAR_HORIZON.md. Thus the same source has the specified independent-clock obstruction and the explicit five-step smaller predecessor. It immediately rejects the half-partner grammar because its starting b is divisible by 64. No determination of its status as a full-band fiber minimum follows.

## Frozen source review

- PR173, fa0c9e2a2851e6324391e39c17afcb5913185aec, research/lean-shell-cover/ForwardSection.lean, bounded_visit and collatz_iff_marked.
- PR182, cf1f04db7f9f84d3a31bfccf2546431b711312d0, research/astra-round13-20261124, AffinePairReturn, PairedLanguage, MarkedHalfReturn and LINEAR_HORIZON. The checked statements supply physical half partners and section preservation. The independent-clock obstruction is a written theorem.
- PR193, c6cb5e66516a86c33a757154983bbddc822510de, research/astra-universal-descent-20261124/escape.md §§1a–1b, shadow.md S1–S6, SHADOW_COVERAGE_LIMIT.md and README.md. The stronger first-endpoint obstruction concerns a logarithmic excess budget and ordinary lower density at each fixed positive ternary height, with no exclusion of later endpoints or other partners. It does not imply a lower density of surviving marked fiber minima.
- PR194, b1bf1f151a2da8936f80d229f132d0b7539ba42c, research/astra-birth-rigidity-20261124/LATEST_SOURCE_SYNTHESIS.md, LS1 and LS3. That note itself pins an earlier PR193 head 52beff703fd3ce798c430e5af8199eb58d41bf93. LS1 concerns a conditional separation statistic for a fixed empirical orbit law. It neither produces a partner for a specified fiber minimum nor bounds its ordinary height. LS3 retains the original least source; the strengthened inequality above uses precisely that rank.
