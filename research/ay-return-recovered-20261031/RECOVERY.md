# Recovery of the unpublished AYH return pass

**Status: PROPOSED. Collatz remains unresolved.** This is a mathematical reconstruction of the interrupted `ay-return-20261031` pass, not a byte-for-byte restoration or a new independent review. The published predecessor is PR #141 at `ccf1887cd07502c3772f8ccbd77c8dab22ea51c5`.

## Provenance and what was not recovered

The previous session ended at an expired publication approval. Its tool record contains an 18-file staged packet and local tree identity `bca68ca5c1c58a5e1424c702657bccfce7152cb8`, but no successful publication. The current session found PR #141 still at the predecessor above. The previous workspace is absent, and fetching that staged tree from GitHub returned 404. Recorded source outputs and mathematical statements were recoverable from the conversation record. The original 18 files have **not** been recovered byte-for-byte.

This document preserves the five scientific tracks, their main proofs, counterexamples, and the boundaries of the recovery. A new self-contained checker accompanies the reconstruction; its executions are distinct from the previous session's receipts. No new independent-agent launch, external review, proof-assistant verification, complete-repository execution, or restoration of the old commit is claimed.

The earlier intended packet comprised `README.md`, `SOURCES.md`, `carry-renormalization.md`, `joint-order.md`, `relational-orders.md`, `run-cancellation.md`, `section-return.md`; five correspondingly named Python programs and five JSON outputs; and `verify_packet.py`. Missing original implementations and raw receipts are not silently represented as recovered bytes.

## Conventions and dependencies

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n; kill state 1. For odd n>1, U(n)=(3n+1)/2^v2(3n+1). Write s(n) for popcount. The mixed-base representation uses initial value 1 at `c`, with `a,b` acting by 2x,2x+1 and `e,f,g` by 3x,3x+1,3x+2; `d` is the right boundary.

The eleven rules are `ad→d`, `bd→gd`, `ae→ea`, `af→eb`, `ag→fa`, `be→fb`, `bf→ga`, `bg→gb`, `ce→cb`, `cf→caa`, `cg→cab`. These rules and their Collatz equivalence originate with Emre Yolcu, Scott Aaronson and Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*, arXiv:2105.14697; see the predecessor packet for source pins. No external priority claim is made for this reconstruction. Earlier project section and merging results remain credited in the predecessor and research map.

## R1. Explicit first-return map and complete inverse fan

Label the section state 6p+2 by p≥1; label the killed state 1 by 0. Define F(0)=0 only as bookkeeping. The first positive T-return to `{6p+2:p≥1} ∪ {1}` is

- p≡1 (mod 4): F(p)=(p−1)/4;
- p even, 3p+2=2^r t, t odd: F(p)=(3^(r−1)t−1)/2;
- p≡3 (mod 4), p+1=2^h t, t odd: F(p)=(3^(h−1)t−1)/2.

The physical shortcut clocks are respectively 2, r+1, h+1, except p=1 has clock 3. These formulas follow by initial halving and the exact odd-run identity T^j(2^a u−1)=3^j 2^(a−j)u−1 for j≤a. The intermediate values are odd until the final even section hit, so the returns are first returns, not merely sampled meetings. The single-`g` return described in the predecessor projects to F; no new well-foundedness of its iteration is established.

For q≥1 write 2q+1=3^k t with 3∤t. The **complete** positive inverse fan is

    {4q+1}
    ∪ {2^(i+1) 3^(k−i) t−1 : 1≤i≤k}
    ∪ {(2^(k+1)t−2)/3 : t≡(−1)^k (mod 3)}.

To prove completeness, solve the three disjoint source branches above. The odd branch has h=i+1 and its odd unit forces i≤k. In the even branch, integrality of the source forces r=k+1 and the displayed unit congruence. Every displayed source is positive and lies in its claimed branch. These are distinct sources.

Put m(0)=0 and m(q)=min F^−1(q). Among the odd candidates the smallest is at i=k; whenever the even candidate exists it is smaller still. Consequently m(q)<q exactly on the four disjoint residue classes

    q≡7 mod 9; q≡4 mod 27; q≡67 mod 81; q≡40 mod 81.

Also F(p)<p exactly when p is neither 2 mod 4 nor 31 mod 32. Both assertions follow by substitution and sign comparison in the formulas; they are not statistical drift statements.

## R2. A five-certificate reduction and its exact failure language

Define

    Lambda(p)=min{F(p), m(p), m(F(p)), F²(p), m(F²(p))}.

Then Lambda(p)≤p because p belongs to the inverse fan of F(p). Each term gives an actual common-endpoint certificate with F-clock pairs (1,0), (0,1), (1,1), (2,0), (2,1), respectively. At label 0 the physical trajectory has already stopped; F(0)=0 must not be interpreted as a new physical step. Strict applications therefore preserve convergence equivalence and terminate by ordinary natural-number descent.

The equality set Lambda(p)=p is exactly this periodic language:

1. Even part: p mod 32 belongs to {2,30}, or p mod 64 belongs to {42,58}, or p mod 256 belongs to {10,74,138}; remove all four predecessor classes in R1.
2. Odd part: p mod 768 belongs to {159,447,255}, or p≡639 mod 1536.

Its period is 41472 and it contains 3807 residues, density **47/512**. This is the density of the failure set of this particular finite certificate menu, NOT a density of nonconvergent integers.

Here is an algebraic route to the classification. After direct descent and one-step coalescence, a possible least obstruction is p≡2 mod 4 or p≡63 mod 96. Set q=F(p)>p; then q≡1 mod 3. For these sources,

    min(F(q),m(F(q))) = 3q/4              if q≡0 mod 4,
                      (q−1)/4           if q≡1 mod 4,
                       q                if q≡2 mod 4,
                      (q−1)/3           if q≡3 mod 4.

For an even source with r=v2(3p+2), success against the ORIGINAL source p occurs for q mod 4 in {0,1,3} when r=2; in {1,3} when r=3,4; in {1} when r=5; and never when r≥6. For an odd surviving source with h=v2(p+1), success occurs in {0,1,3} when h=5, in {1,3} when h=6,7, and never when h≥8. Substitution gives the binary residue lists above. The even list has 27 residues mod 256 and the predecessor exclusion retains 67 residues mod 81, giving 67/768. The odd list has density 7/1536. Their sum is 47/512.

**Preserved counterexample to naive iteration:** 42→F 364→Lambda 42 is an artificial cycle caused by changing the comparison floor. The actual F-orbit is 42,364,273,68,51,19,7,4,3,1,0. The kernel is not forward invariant (already 2→4 leaves it). A future proof must retain one original source and actual joining clocks, not treat this reduction as a freely switchable dynamical rule.

A positive unbounded family was also recovered. Let p=(2^r t−2)/3, r≥2, t odd and t≡(−1)^(r−1) mod 3. If 3^r t≡1 mod 2^(2j+1), j≥1, then after its first expanding return the next j returns use (x−1)/4. Their final value is

    y=(3^r t−2^(2j+1)−1)/(3·2^(2j+1)).

Exactly y<p iff `(2^(r+2j+1)−3^r)t > 2^(2j+1)−1`. Choosing j with `2^(2j+1)(2^r−1)≥3^r` makes this true for all eligible positive t. CRT supplies infinitely many such t for every r. Example: 5546→71077→17769→4442. This conditional family does not cover every source.

## R3. Complementary carry rank and why it is not a global order

For odd n define

    K(n)=s(n)(s(n)−1)/2 + v2(n+1),
    X(n)=(n+1)/2^(s(n)−1)−1,
    B(n)=min{k≥0 : 4^k·2^(s(n)−1) ≥ 3^k(n+1−2^(s(n)−1))}.

Thus B is the ceiling of log base 4/3 of X, implemented by exact integer comparison. X≥1. Whenever n>1 and K(U(n))≥K(n), one has X(U(n))≤3X(n)/4, hence B(U(n))≤B(n)−1.

Proof: K orders the pair (s,v2(n+1)) lexicographically. If r=v2(n+1)≥2, the odd step has valuation 1 and new trailing run r−1; failure of K-descent therefore forces new popcount at least s+1. Substitution gives X(U(n))≤3X(n)/4−1/4. If r=1, the valuation is at least 2 and failure forces new popcount at least s. Substitution gives X(U(n))≤3X(n)/4 + 2^(−s)−1/4≤3X(n)/4 since s≥2.

Writing Z=bitlength(n)−s(n), one has B(n)≤3Z+1. For Z≥1, X(n)<2^(Z+1)−1 and `(4/3)^(3Z+1)≥2^(Z+1)−1` by induction; Z=0 gives X=1. Therefore the first locally K-decreasing odd step occurs within B(n)+1≤3Z+2 odd steps. **A local decrease at that last step is not necessarily a net decrease from the original source.**

For proper SRS words let H be the sum, over ternary letters, of bitlength of the prefix value immediately before the letter. Each administrative rewrite preserves value and lowers H by one. The two lexicographic ranks `(K(oddpart(value)),v2(value),H)` and `(B(oddpart(value)),v2(value),H)` together cover every literal rewrite, but their union is not established as well founded.

An explicit obstruction is n=21·2^r−1, r≥3. Its first locally good return has two odd steps, net K increase r, and B values 8→4→9. Thus endpoint dominance blocks every coordinatewise nondecreasing fusion of just K and B on this return schedule. Do not advertise complementary descent as a global termination theorem.

## R4. Unbounded carry-cancellation modules

For n=2^r t−1 with t odd and 1≤j<r, U^j(n)=3^j 2^(r−j)t−1. Since s(n)=r+s(t)−1, exact original-source K-descent at j is equivalent to

    s(3^j t)≤s(t)+j.

For A_h=(4^h−1)/3, r≥h+1, the first such j is exactly h and the K drop is h. Indeed s(A_h)=h, whereas s(3^j A_h)=2h for 1≤j≤h. The identity follows from `3^j A_h=3^(j−1)(2^(2h)−1)` and

    s(b(2^m−1))=m  for odd 0<b<2^m.

To prove the latter, write the product as `(b−1)2^m+(2^m−b)`; the lower block complements b−1. Every intermediate odd value in the A_h family grows, and the endpoint/source ratio exceeds (3/2)^h. This is genuinely non-numeric rank descent, not ordinary size decrease.

One active A_h block can be combined with arbitrarily many disjoint neutral blocks a(2^m−1), with a odd, 3^h a<2^m. Reserve 4h bits for the active block and 2m for each neutral block, preserve their order and offsets, and ensure an odd core. Up to multiplication by 3^h these reservations prevent inter-block carries; each neutral block retains popcount m. The same first-return proof applies. The original pass contained a finite current-word parser for this language, with unique height candidate h=s(3t)−s(t); its original implementation has not been restored here.

## R5. Opaque-prefix relational orders

Delete the three c-boundary rules and regard a positive prefix x as opaque. The eight remaining rules terminate by lexicographic decrease of (number of binary letters, number of binary-before-ternary inversions). Distinct redexes do not overlap, so the normal form is unique. If a binary suffix has length k and numeric residue r and its all-ternary normal form has length t and residue c, then for EVERY x≥1,

    T^k(2^k x+r)=3^t x+c,

with exactly t odd steps. This is a universal affine cone identity with one shared prefix, not a finite sample.

A nonempty ternary suffix has a binary preimage precisely when its final digit is f or g, equivalently c is not divisible by 3. An explicit inverse compiler uses at most 4t−2 shortcut steps. Starting from `3^t x+c`, inverse blocks are `(2^a Y−1)/3`. Choose a=1 if the current constant is 2 mod 3, otherwise a=2; unless this is the final block, add 2 when the resulting constant is 0 mod 3. This ensures each next inverse exists, uses a≤4 before the final a≤2, and yields `2^k x+r` with 0<r<2^k. Each inverse block is positive and odd. The original pass also implemented canonical shortest preimage search; that implementation has not been restored.

For f^h specifically the canonical binary preimage is a b^h. Consequently

    T^(h+1)(2^(h+1)x+2^h−1)=3^h x+(3^h−1)/2.

For h≥2 and x≥1, the binary source is strictly smaller than the ternary source. In particular Mersenne n=2^e−1, e≡5 mod 6, has a smaller coalescing witness with h=v3(2n+1)=1+v3(e+1)≥2. This supplies an infinite relational-descent family, not convergence of its witnesses.

**A hard scope boundary:** the complete union of forward orbits of 1,…,26 has 34 states, and 27 first meets it after exactly 59 shortcut steps, at 23. Every proper mixed representation of 27 has at most four interior letters. An opaque normalization consumes at most four binary letters and thus at most four dynamic steps. Therefore arbitrary mixed recoding plus ONE opaque normalization cannot meet any smaller source, regardless of the partner clock or dictionary size. This revisits the source-budget obstruction from PR #139 rather than claiming priority for it.

## R6. Recovered joint proof-search architecture; missing late proof

The interrupted pass combined four types of physically verified edges on odd sources: one locally K-decreasing U step; a forced-run cancellation module from R4; the total first-locally-good return from R3, admitted ONLY when it repays original-source K; and the proper f-suffix backward witness from R5. Admit an edge n→m only when K(m)<K(n), or more stringently when K(n)−K(m) pays for the total odd events on both joining arms. A finite candidate generator and strict natural rank make exhaustive DFS terminate with PROVED or UNRESOLVED. This is completeness for that finite proof language, not for all integers.

For a successful budgeted proof from n0 with R=K(n0)−1, the sum of odd-event costs is at most R; node and joining-arm values are bounded by 2^R n0. The shortcut work is at most R(bitlength(n0)+K(n0)); the binary-to-binary literal SRS work is at most 2R(bitlength(n0)+R). These bounds use distinct joining arms, not an invented single forward orbit. Actual stopping clocks compose by signed differences of the two physical clocks.

The prior record additionally states a late theorem that f-suffix backward edges add no successful sources to the forward-only language, under either admission policy. **The final proof and final implementation of that theorem were not recovered in full, so it is quarantined here as UNRECONSTRUCTED, not adopted as proved.** Likewise earlier recorded pass counts and replay hashes are archival observations, not fresh execution claims.

## Current boundary

R1–R6 leave a precise, nonempty obstruction: an ordinary source can remain outside every currently justified net-decreasing certificate. Neither two-rank edge coverage, finite proof-search termination, periodic kernel sparsity, nor an unbounded family supplies global coverage. Further work should seek a source-persistent order across interacting carry intervals or a genuinely stronger relational certificate language, and retain the 42 and 27 counterexamples as regressions.
