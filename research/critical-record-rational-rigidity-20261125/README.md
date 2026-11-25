# Critical records: exact rational trace, signed inverse rigidity and a Subspace Theorem route

**Status: PROPOSED written theorems. Collatz remains OPEN.** This attack follows the actual critical-record residue tree of PR206, rather than an average-case distribution. It classifies its entire rational trace, gives a finite rational membership test, and obtains a new arithmetic transcendence criterion (see SUBSPACE.md). The final Lean candidate is a finite ordinary-path consumer with its missing hypothesis explicit. No local Lean compiler or independent subagent runtime was available in this session.

## 1. Actual records and the universal critical tree

Use the positive ordinary shortcut T(2n)=n, T(2n+1)=3n+2 and U for the odd-to-odd map. A unit means an odd positive integer prime to three when referring to ordinary sources. Let e_i>=1 be inverse gaps, ordered **backwards** from the terminal, S_j=sum_{i<=j}e_i and A_j=2^S_j/3^j. Put
    beta_j=sum_{i=1}^j 3^(i-1)2^(-S_i).
The inverse recurrence is y_j=(2^e_j y_(j-1)-1)/3 and its exact solution is y_j=A_j(z-beta_j), with y_0=z.

Call a word critical if A_j<1 for EVERY nonempty prefix j. Let R be the subset of Z_3 given by all convergent ternary series beta_infty over infinite critical scripts. Equivalently R is the intersection over b of the finite unions of residue cylinders beta_b+3^b Z_3 over length-b critical words. Indeed, the prefix constraints imply S_j<j log_2 3, hence the tree is finitely branching at every depth. Membership in all nested unions gives a coherent infinite script by König's lemma. Conversely its series has the required residue at each depth. This shows R is compact; every first gap is 1, so R lies in the unit class 2 mod 3.

Take one nonrepeating ordinary odd ray x_k=U^k(a), total clock s_k, M_k=3^k/2^s_k. The resident simple-path reciprocal sum bound implies x_k=a M_k D_k with 1<=D_k<=D_*(a)<infinity. Since distinct positive integers tend to infinity, M_k tends to infinity too. Its strict upper records are cofinal; at each record k, for every 1<=j<=k,
    2^(s_k-s_(k-j))<3^j.
Thus every ternary cluster point of these actual record endpoints is in R. This is precisely the critical-record mechanism of PR206, not a change to a typical source or a different limiting orbit.

PR206 at 45a6a111321f947a8482c9e96e898435b57cee09 (research/clock-itineraries/EscapeRecords.md) excludes fixed positive integer cluster points. The present theorem treats every rational in Z_3, including signed fractions and those with a dyadic denominator. The distinction matters: some **positive** fractions with even denominator do occur in R.

## 2. A signed finite-path lemma

We require a simple-path estimate for both signs of the generalized odd integer map
    2^e u_next=3u+c,  c=d or -d,
where d is a fixed positive odd integer, all u are positive odd, the recorded path is injective, and every e>=1 is exact because u_next is odd. These are literal signed numerator paths of rational shadows, not an assumed ordinary positive Collatz ray. Classical context: Lagarias, The set of rational cycles for the 3x+1 problem, Acta Arithmetica 56 (1990), 33–53, and Bell–Lagarias' 3x+k convention. Clearing a fixed odd denominator gives precisely the generalized map. We prove the estimate directly, without assuming convergence of any generalized map.

Let theta=39/40. Every finite such path satisfies
    #{u<=X on path} <= 10(d+1) X^theta   (c=d),
    #{u<=X on path} <= 10 X^theta       (c=-d),            (S)
for X>=1. Here distinctness is essential; endpoints may be counted. This is a signed extension of the resident T-A3-651 argument recalled in PR201, 2978d84f8a1fda9083593b26c6bf724d5976d859, escape-analysis/README.md.

For completeness take m=floor((3/5)log_2 X). The m=0 case follows from X<2^(5/3). Otherwise set B=floor(5m/3); discard at most m final positions lacking m further edges. A word of m positive gaps, sum E, determines the initial residue modulo 2^(E+1), since the affine formula has odd coefficient 3^m and the exact final odd bit. For E<=B, 2^E<=X, so at most (3/2)X2^-E starts per word. Using the composition generating function with t=4/5,
    sum_(E<=B) binom(E-1,m-1)2^-E
       <= t^-B [t/(2-t)]^m <= rho^m,
    rho^3=3125/3456.
For E>B, the actual endpoint is <=sigma^m X+d((3/2)^m-1) if c=d and <=sigma^m X if c=-d, with sigma^3=27/32<rho^3. The positive carry inequality follows by iterating (3v+d)/2, since each divisor >=2. The negative one drops the nonpositive carry. Advancing by m edges is injective on the given distinct segment; hence the high-clock count is at most half the endpoint bound plus one. Now 2/3<rho<2^(-1/24) (raise to integer powers), so Xrho^m<=1.5 X^theta; (3/2)^m<=X^theta, and m<=2 sqrt(X). Combining terms gives (S) with room in both constants. No random law or independence has entered.

A useful consequence for a finite distinct positive-magnitude path under c=-d is
    sum_(u>=d) 1/u <=400 d^(-1/40).
Indeed use 1/u=integral_u^infty dt/t^2 and (S). If a chain is read backwards, the same estimate holds by reading each finite segment forwards before applying it.

## 3. Uniform finite signed-shadow bound

Let d be fixed positive odd, 3 not dividing d. Let a_0=a be a nonzero odd signed numerator, and consider a finite literal inverse sequence
    3 a_j = 2^e_j a_(j-1)-d,
    e_j>=1, a_j integral,
with A_j<=H for every j, H>=1. Every numerator is odd, hence nonzero. Each edge reversed is the deterministic accelerated signed map U_d(v)=(3v+d)/2^v2(3v+d), which is defined for all nonzero odd v since 3 does not divide d. We do not assume the sign of U_d(v) except as supplied by the path.

**Finite lemma.** If a_0,...,a_b are all distinct, then
    b+1 <= C_d (H|a|)^theta,
where C_d is an explicit finite constant depending only on d. In particular the weaker integer bound
    b+1 <= 20(d+1)^2 K_d ceil(H|a|), 
    K_d=(3d)^d 2^(400d)                                  (B)
is sufficient for a finite decision algorithm.

Proof: any positive prefix satisfies a_j<=A_j a<=Ha by the full inverse affine identity; each corresponding positive segment is covered by (S). Once a_j<0, all further reverse numerators stay negative. Write u_j=-a_j. For two successive negative entries, 3u_j=2^e_j u_(j-1)+d. Hence for a negative tail starting at index l,
    u_j = u_l (A_j/A_l) prod_(l<i<=j) (1-d/(3u_i))^-1.     (3.1)
Every u_i with i>l satisfies 3u_i>d. For u_i<d the individual factor is <=3d, and there are at most d such distinct integer values. For u_i>=d, -log(1-d/(3u_i))<=d/(2u_i); apply the reflected-map reciprocal bound to the same negative-magnitude path. Its product is at most (3d)^d exp(200 d^theta)<=K_d. The last inequality uses log 2>1/2.

If a<0 take l=0, u_l=|a|, A_l=1. If a>0 crosses sign at index l>=1, then u_l<=d/3, and positivity of a_(l-1) gives a A_(l-1)>=1. Since A_l>=2A_(l-1)/3, we have u_l/A_l<=da/2. Consequently in all cases
    |a_j| <= (d+1) H|a| K_d
on the entire distinct path. Apply (S) separately to its positive and negative segments, or simply use the finite integer height bound, to obtain the displayed power bound and (B). The bound depends on the original shadow denominator, not on the positive ordinary q being compared to it.

## 4. Exact rational classification of R

**Theorem R1.** For z=a/d in lowest terms with d positive, odd, prime to three, and a odd, z belongs to R iff z lies on a NEGATIVE rational odd cycle and the uniquely defined backwards period from that phase satisfies the critical prefix constraints. More generally for ANY rational z in Z_3, membership in R is equivalent to the existence of a finite critical inverse prefix leading to an odd-numerator, odd-denominator negative rational cycle, whose backwards periodic continuation respects the remaining prefix budget. Every infinite critical script representing a rational z is eventually periodic.

Proof first take odd a,d. Any compatible infinite script gives integral signed numerators by the congruence z=beta_j mod 3^j: explicitly a_j=(2^S_j a-d 2^S_j beta_j)/3^j, and 2^S_j beta_j is an integer. All a_j are odd. Its first repeat must occur by (B) with H=1. Determinism then implies that a_0 is periodic: a repeated value is periodic, and a_0 is a forward iterate of it. In fact every a_l is periodic: apply the same finite lemma to the infinite remaining tail with the fixed slack H=1/A_l. Each is therefore on the same cycle, and each is its unique cycle predecessor in reverse order. Thus the complete script is periodic, starting at a_0. A positive cycle has product 2^s/3^p=prod(1+d/(3a_i))>1, so repeated laps violate A_j<1. A negative cycle has all its odd numerators < -d/3 (forward image stays negative), and product 2^s/3^p=prod(1-d/(3|a_i|))<1. Checking the critical prefixes of one backwards lap is sufficient, since repeating it multiplies all subsequent prefix products by that number <1. This proves the characterization. Each negative rational cycle has at least one critical phase, by rotating the finite log increments  log(2^e/3) to start after a maximum of their partial sums. All nonempty prefixes are strict because 2^S never equals 3^j.

For general rational z=a/d with d possibly even and prime to three, use the same fixed-denominator formula for a_j. If r=v2(d), the recurrence shows v2(a_j)>=min(v2(a_(j-1))+1,r), with the usual infinity convention at zero. After r steps all numerators are divisible by 2^r. Divide numerator and denominator by 2^r; one more step has odd numerator since the denominator is now odd. The tail is an odd-numerator fixed-odd-denominator inverse chain with fixed slack H=1/A_(r+1), where the preceding argument applies (a_l has infinite tail and each such tail has its own finite slack). It is eventually periodic negative. The converse follows by exact inverse composition and decreasing products across a negative lap. A positive z with even denominator is not automatically excluded: z=49/32 has the legal initial inverse word (1,1,1,3) taking it successively to 11/16, 1/8, -1/4, -1; the prefix products are 2/3,4/9,8/27,64/81. Append ones indefinitely. This is a rational point of R, not an ordinary positive integer counterexample.

For odd denominator but even numerator, a single step makes the numerator odd. If z>0 then that step must have e=1 (the first critical inequality). Its value is (2z-1)/3, which is >-1/3. If positive it cannot be a negative cycle; if negative it is in (-1/3,0), which cannot be a negative cycle point because its next odd image is positive. Hence **no positive rational of odd denominator** belongs to R. Zero is excluded by the unit class.

### Effective rational membership

R1 is an actual terminating decision procedure for any supplied rational z in Z_3. Reject a nonunit. Enumerate all critical words of length L=v2(d)+1 (or L=0 when a,d odd), test their exact integer numerator congruences, and discard prefixes failing legality. For each normalized terminal a'/d' (odd numerator, positive odd denominator, 3 not dividing d') retain H=1/A_L. If a'>0 reject this branch. For a'<0 enumerate critical-with-slack inverse words up to the integer bound (B), testing every prefix ratio <H. Accept iff some path returns to its initial negative numerator. A returned negative cycle has inverse multiplier <1, so indefinitely repeating the same lap preserves the slack. If an infinite path existed, the first repeat from the finite bound would be a return to the initial vertex: all points before the repeat are on the same periodic cycle and its inverse predecessor is unique there. Thus the finite search is complete. The enumeration is enormous, not offered as a practical general-purpose rational-cycle detector. It does NOT decide positive Collatz convergence: the input is a rational point of the **backward critical trace**, not a forward source.

### Quantitative exclusion on a finite record word

Let q be an actual positive ordinary endpoint with a critical backward suffix of length b and q≡a/d mod 3^b, where a,d are odd and d>0 prime to 3. The same word lifts to integral odd signed numerators a_j because
    a_j=d x_(k-j) + 2^S_j (a-d q)/3^j.
If z=a/d>0, there can be no repeat in that shadow: any repeat puts z on a positive cycle and the first repeat of a cycle predecessor sequence has A_p>1. If z is negative and nonperiodic under the signed rational odd map, repetition would make it periodic. In either case (S) and (3.1) prove
    b+1 <= C_d |a|^theta.
For d=1 and positive a the sign cannot cross (positive ordinary inverses remain positive), and the sharper bound 10(a+1)^theta follows directly from the ordinary path count (constant 10(d+1) also suffices). This strengthens PR206's linear positive-integer representative cutoff, while the main change is the complete signed rational trace. If the shadow starts at an admissible negative periodic phase and follows the unique backwards cycle for j steps before departing, all later vertices including the departure are distinct and never revisit the cycle. Apply (B) or its power version with starting cycle phase at j and H=1/A_j. Since A_j>=c_z lambda^(j/p), where lambda=2^s/3^p<1 is the inverse period multiplier, one obtains b-j <=C_z lambda^(-theta j/p). Thus every sufficiently long compatible word agrees with the negative cycle for at least c_z log(b+1)-C_z initial gaps. This is a finite rigidity bound, not a claim that the ordinary record itself is negative.

## 5. Topological sharpness of the rational classification

Every finite critical word w of length p and clock A can be completed periodically: its inverse multiplier 2^A/3^p<1, so all prefixes of w^infty are critical. The resulting rational point is
    z_w=C_w/(2^A-3^p)<0,
    C_w=sum_(j=1)^p 3^(j-1)2^(A-S_j).
The denominator is odd and prime to three, the numerator odd and prime to three (last and first summands respectively). It is a negative rational cycle by R1, or directly by rotating the exact inverse affine fixed-point identity. Its ternary residue agrees with the original cylinder through depth p. Hence negative rational periodic phases are DENSE in R. Moreover R is perfect: after any prescribed finite critical prefix append sufficiently many ones to have enough slack, then choose a different next gap (1 or 2), and periodize each extended word. The two rational points cannot coincide, since R1 gives each odd rational point a unique infinite backward cycle script. Both lie in the original cylinder. Thus every relative neighborhood contains distinct points. The compact set R also has Haar measure zero by PR206's composition count (the critical bound is stricter than slope 8/5). There is no contradiction from the rational points being dense in this *restricted* set.

Every individual cylinder has actual positive ordinary finite realizations: choose arbitrarily large odd q in beta_p mod 3^p, reverse the word, and take q large enough for every intermediate state positive. Each is integral and odd, every gap exact, and the terminal is a strict coefficient record relative to that finite beginning by the prefix inequalities. The starts vary with depth; no fixed source is constructed. This explains why a proof cannot simply remove all finite critical residue cylinders.

## 6. A new restriction on a single escaping ray

**Theorem R2.** Suppose the strict coefficient-record indices of one positive nonrepeating odd trajectory have bounded gaps J (in odd clock), from some point onward. Then their ternary accumulation set cannot be a finite set of rational points with odd numerators and odd denominators. More precisely, for any finite set S of such rationals and any fixed J, there is a finite precision B such that the following two conditions cannot both hold at every sufficiently late record:
  (i) its endpoint is congruent modulo 3^B to some point of S;
  (ii) its gap from the preceding record is <=J.

Proof: discard nonmembers of R by the finite word test R1, increasing B. Thus every candidate phase in S is on a negative rational cycle. By the finite periodic-prefix bound in §4, choose B large enough that every compatible critical suffix of length B lifted to any of these phases agrees for its first J gaps with the unique backwards cycle word. Also choose B-J large enough to distinguish every pair of distinct rational points in the finite set consisting of S and all phases of those finitely many negative cycles (their denominators are units at 3). At each sufficiently late record choose its unique phase label in S. The actual word between two successive records has length j<=J. At the later record, its backwards shadow along this word is the corresponding negative cycle predecessor phase. The previous actual record is congruent to that phase mod 3^(B-j), by the exact lift difference. By precision separation it is exactly the previous chosen phase. The actual intervening gap word therefore agrees with a forward segment on the same negative rational cycle. Iterating along the whole late record sequence gives the exact infinite future gap word of that cycle for one fixed positive ordinary record endpoint.

But if positive x and negative rational a/d (odd numerator/denominator) have the same first m odd gaps, total clock S, subtraction of their actual forward affine equations gives
    2^S | (d x-a)
as integer divisibility. Since S>=m and d x-a is a fixed nonzero integer, unbounded m is impossible. This last point is the fixed-source obstruction; changing the source with the prefix would not give it. Contradiction.

For a finite accumulation set S, eventual coverage by any fixed ternary precision neighborhood follows from compactness. This gives the first formulation. It does not show bounded record gaps, rationality, or finiteness of the accumulation set in the first place. Long droughts between critical records and genuinely irrational cluster points remain possible. In particular the positive-density record theorem at the larger slope 18/11 in PR206 does NOT provide the bounded gaps at the exact critical slope needed here.

## 7. Final proof direction and limitations

The [Subspace Theorem](SUBSPACE.md) supplies a genuinely different restriction on the irrational part of the critical residue tree: for nonperiodic critical scripts, stammering with quantified clock height forces transcendence, and asymptotically balanced scripts of bounded linear factor complexity cannot give algebraic irrational coordinates. The rational classification is unconditional written mathematics; the transcendence argument uses the classical p-adic Subspace Theorem with all places and coefficient hypotheses retained.

To prove Collatz through this route would require an additional fixed-source theorem (for example, compact rational confinement plus bounded record gaps on every hypothetical escaping ray), and a separate exclusion of nontrivial positive cycles. Neither follows from this classification or from the algebraic recurrence results in PR192. The companion Lean file gives the finite inverse congruence, cycle sign and fixed-source gap-matching consumer. The ultimate full-conjecture theorem takes its two **unproved** dynamical hypotheses as explicit parameters. It is not a claimed unconditional Collatz proof.

## Source and evidence ledger

* Main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a; PR206 45a6a111321f947a8482c9e96e898435b57cee09, November25.md, EscapeRecords.md, EscapeFrontier.md and TowerFrontier.md: critical-record construction, positive rational integer obstruction (positive integers only), and unresolved tower recurrence.
* PR201 2978d84f8a1fda9083593b26c6bf724d5976d859: escape-analysis/README.md, finite path count; this packet extends the proof to fixed signed numerator paths.
* PR192 07d494324c7ea440d45845d725f5cebad8a67124: FINAL_PROPOSAL.md, Noetherian rational dynamical models and fixed-series Mahler criterion. Our critical residue z is a different 3-adic limit, not its actual dyadic or real scalar.
* PR195 4fd8af31c1ea525252b4d8f7411b5921dd447048: round11/README.md, whole-denominator windows, bounded template-bank finiteness and integer trace zero range; PR197 156652e03fe7a78f9cd4442039779cc622fdf3de source-progress/README.md; PR209 2d0230aa52d85732dbc85b5df20e30108dc1396f: narrow-band and simultaneous tower descent. The present argument does not discharge their frontier-merger premises.
* PR190 ba58227c5a047ff3859a148a5fdaac4fd1451e4c and PR194 b1bf1f151a2da8936f80d229f132d0b7539ba42c: Mahler/substitution rigidity of 2-adic physical words. SUBSPACE.md instead treats a 3-adic critical backwards limit, arbitrary stammering and balanced clock height.
* PR207 b56c4dc2c28a184cf55638bb80c49a9d4662fc81: central inverse-row aggregate; no new opposing trace upper is inferred.
* Lagarias, The set of rational cycles for the 3x+1 problem, Acta Arith. 56 (1990), 33–53, DOI 10.4064/aa-56-1-33-53, classical rational-cycle formula and generalized 3x+d correspondence. No theorem about generalized convergence imported.
* Schlickewei (1977), p-adic Subspace Theorem, Evertse's 2011 exposition Theorem 1.1; precise use and linear forms in SUBSPACE.md. This is classical literature rather than a new claimed analytic theorem from a preprint.

This is a narrow reconstruction of named source interfaces, not a line-by-line independent re-review of all repo files. No Lean compiler was found on PATH or in the usual local toolchain path. The Lean source is proposed and uncompiled; no compiler output, transitive axiom audit, independent subagent review or full checkout validator is claimed. The bounded exact controls are separate.
