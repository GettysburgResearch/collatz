# Proper ancestors are redundant; transverse joins are not

**Status: PROPOSED proofs, finite replay supplied, independent review pending.** No assertion here is a proof of Collatz. All sources are positive ordinary integers. Physical clocks use the shortcut map T, killed at 1; U is the accelerated odd map on odd n>1. Let

    K(n)=binom(popcount(n),2)+v2(n+1).

The raw forward language has two kinds of blocks:

- the complete first-locally-K-decreasing U return: all preceding steps have nondecreasing K and the final step decreases K;
- any nonempty forced run `U^j(n)=3^j 2^(r−j)t−1`, where `n=2^r t−1`, t odd, and `j<r`.

Admit a block only if its endpoint has strictly smaller K than its original source. The budgeted variant requires the K drop to pay the number j of odd steps. The total first-good generator is justified by the complementary B rank in the recovery packet; it does not assume Collatz. Each input has finitely many candidates, and strict K bounds every proof branch's length. Hence exhaustive search terminates, possibly with UNRESOLVED.

## T1. General ancestor-elimination theorem

Let f be a deterministic killed map, R a well-founded rank, and G a set of finite forward blocks that is closed under taking nonempty suffixes. Consider finite proofs to a terminal state that use only blocks whose endpoint rank is strictly smaller than their source rank. Adding **arbitrary proper-ancestor edges** `n ⇒ m` satisfying `f^h(m)=n`, h≥1, and `R(m)<R(n)` adds no successful sources.

For natural-number ranks, the same assertion holds for additive nonnegative block costs when every forward block pays its cost from its rank drop and an ancestor edge also has positive paid cost. The cost of a suffix must not exceed that of the whole block.

### Proof

Induct on R(n). If a proof begins with a forward block, apply induction at its smaller endpoint. If it begins with an ancestor edge n⇒m, induction gives an entirely forward proof from m. Its underlying physical path passes through n before termination: the supplied ancestral path has no earlier killed state, and determinism fixes its continuation.

All proof-boundary ranks on that forward proof are at most R(m)<R(n). Therefore the occurrence of n is strictly inside a block, not at a proof boundary. Let z be that block's endpoint and y its source. The suffix from n to z belongs to G. Moreover R(z)<R(y)≤R(m)<R(n), so this suffix is admitted. It can be followed by the remainder of the proof. In the budgeted version, `R(n)−R(z)≥R(y)−R(z)` and the suffix costs no more than the original block, so it is paid as well. This replaces the ancestral first edge by forward blocks and completes induction. ∎

This is a finite-proof normalization theorem, not an algorithm for enumerating infinitely many ancestors. It holds for any well-founded rank in the strict version; the budgeted arithmetic uses a natural-number rank.

### Application to the AYH-derived language

A suffix of a first-locally-good block is again a first-locally-good block. A suffix of a forced run of length j<r is a forced run: after i steps its remaining trailing run is r−i and `j−i<r−i`. These statements concern the **raw** blocks; admission of the suffix is supplied by the proof above. Thus T1 applies exactly to the stated finite language.

In particular it eliminates the earlier proper `f^h` binary ancestor modules and every other properly replayed odd ancestor, not merely a bounded dictionary. This newly written proof resolves the recovery document's explicitly quarantined late claim without claiming to have recovered the old proof bytes. It does **not** eliminate genuinely two-arm coalescence where neither source is asserted to occur on the other's forward orbit.

## T2. A paid transverse rewrite

For odd m>1 put L(m)=4m+1. Then

    3L(m)+1=4(3m+1),  U(L(m))=U(m).

If a=v2(3m+1), the physical certificate is `T^(a+2)(L(m))=T^a(m)`. Both arms contain one odd event. The m=1 case is handled separately: 5 reaches the killed state 1 in three shortcut steps; there is no physical U step out of 1.

Appending binary `01` adds one set bit and gives trailing-1 length 1. With s=popcount(m) and r=v2(m+1),

    K(L(m))−K(m)=s+1−r ≥ 1.

Thus `L(m) ⇒ m` is always a strict K-decreasing merger. It is budgeted whenever s+1−r≥2. The identity is classical. Its role here is a new rule in this *specific* rank language. It is not one of the eleven literal AYH rewrites and must not be recorded as a single Collatz step.

For arbitrary q≥1,

    L^q(m)=4^q m+(4^q−1)/3,
    K(L^q(m))−K(m)=q s+q(q−1)/2+1−r.

The common U endpoint persists, and the shortcut clock difference is 2q.

## T3. An infinite separation family with no old admissible move

Take integers h≥3, r≥h+1, and 1≤q≤h−2. Define

    A_h=(4^h−1)/3,
    m=2^r A_h−1,
    n=L^q(m),
    z=3^h 2^(r−h) A_h−1.

Then:

1. the old forward language has **no admitted outgoing edge from n**;
2. the new merger n⇒m strictly decreases K and pays its two odd-arm events;
3. the forced-run block m⇒z has h odd steps and K drop exactly h;
4. `T^(h+2q)(n)=T^h(m)=z`, and the total diagram pays its h+2 odd-arm events from K(n)−K(z).

### Proof

Write s=r+h−1=popcount(m). For every 1≤j≤h,

    popcount(3^j A_h)=2h,
    popcount(U^j(m))=r−j+2h−1,
    v2(U^j(m)+1)=r−j.

The first identity follows from `3^j A_h=3^(j−1)(2^(2h)−1)` and the complement identity `popcount(b(2^M−1))=M` for odd 0<b<2^M. Here `3^(h−1)<2^(2h)`, so it applies throughout the claimed range.

At j=h the popcount has returned to s and the trailing run has lost h, proving K(z)=K(m)−h. The wrapper n has popcount s+q and trailing run 1. Its first U image is U(m), with popcount s+h−1. Since q≤h−2, that first step increases popcount, hence is locally bad. The second U image has popcount s+h−2, one less than the first, so the first locally good return from n has exactly two odd steps.

At that return the endpoint popcount is at least the source popcount. If equal, q=h−2 and the endpoint trailing run r−2≥2 is larger than the source run 1. Thus the return has strictly **larger** K than n and is not admitted. Since n has trailing run 1, it has no nonempty raw forced run. This proves item 1 without a bounded scan.

The merger drop equals `q s+q(q−1)/2+1−r`; its minimum over q≥1 is h≥3. Thus it pays cost 2. The m⇒z block pays h. Their physical clocks follow from the wrapper identity and the h valuation-1 steps from m. For q=1, the total K drop is exactly 2h; for larger q it is larger. ∎

**Small example:** h=3,r=4,q=1 gives n=1341, m=335, z=1133 and K values 22,19,16. The old first-good return from 1341 ends at a larger K. The new diagram satisfies `T^5(1341)=T^3(335)=1133` and has total odd-arm cost 5, paid by rank drop 6. This is a lower-rank certificate, not by itself a proof that 1133 reaches 1.

The theorem is a strict enlargement of the candidate language, not a claim of a large convergence-density gain. The tested success census remains small and is reported without extrapolation.

## T4. Further transverse candidates and their bounded scope

For any odd n>1, choose q∈{1,2,3} and a∈{1,2,3,4} for which

    m=(2^a L^q(n)−1)/3

is an integer. It is positive and odd, and `U(m)=L^q(n)`, so

    T^b(n)=T^(a+b+2q)(m),  b=v2(3n+1).

Both sources join after respectively one and two odd events. Admit the candidate only when its K drop pays the required policy (one for strict, three for budgeted). No proper-ancestor interpretation is assumed.

This finite menu did not add successful seeds beyond unwrapping in the supplied 4,096-seed census. Its source identities are retained as tested candidates, not advertised as an empirical breakthrough. The normalization theorem T1 concerns a forward-only base and does not automatically extend to every language that already has transverse edges.

For the budgeted language **without the optional ancestor test menu**, R=K(n0)−1 bounds total odd-arm cost. A new T4 witness is less than 2^9 times its source; its joining arms stay below 2^10 times the source. Forward blocks cost one credit per odd event and increase value by less than a factor two per such event. Unwrapping decreases source value. Consequently all proof nodes are at most `2^(3R)n0`, and all joining-arm states at most `2^(3R+1)n0`. This is a coarse new bound; the previous `2^R n0` claim for the older language must not be imported unchanged after adding potentially larger transverse witnesses.

## Exact finite evidence

`transversal.py` enumerates the complete candidate menu for each visited source and returns PROVED/UNRESOLVED by iterative rank-decreasing DFS. It checks every selected two-arm identity with literal T steps, checks paid costs, and reconstructs the actual stopping clock by signed clock differences; it never concatenates different sources into a fake forward orbit.

For 4,096 odd seeds through 8191: strict forward and proper-ancestor variants each prove 154; adding unwrapping proves 156 (new sources 5725 and 7005). Budgeted forward and ancestor variants each prove 139; unwrapping proves 142 (new sources 5501,5725,7005). The further T4 menu produces no additional successes in this census. The certificate tests include 177 separating-family instances, maximum source size 10,155 bits. These finite counts do not prove T1–T3; the arguments above address their quantifiers.
