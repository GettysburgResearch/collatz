# Persistent carry cuts, finite Hamming cores, and sparse-source orders

**Status: PROPOSED.** The analytic arguments and finite certificates below are new work in this packet, not independently accepted results. No full Collatz proof, external priority claim, or proof-assistant verification is asserted. In particular, a cap exit is not convergence, and a descent from one source is not permission to reset an unrelated comparison source.

## 0. Conventions and sources

Let T(n)=n/2 for even n, and T(n)=(3n+1)/2 for odd n. Physical trajectories stop at 1. Let U(n)=(3n+1)/2^v2(3n+1) for odd n>1. Let s(n) be binary popcount and b(n) binary bitlength. Only in explicitly marked shadow calculations extend U(1)=1, with valuation 2, or T(1)=2, T(2)=1. No physical certificate steps out of killed 1.

The eleven-rule mixed binary/ternary system is credited to Emre Yolcu, Scott Aaronson and Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*, arXiv:2105.14697, v3 (2022), Journal of Automated Reasoning 67, 12 (2023), DOI 10.1007/s10817-022-09658-8. The arithmetic encoding and Collatz equivalence are theirs, not discoveries of this packet.

Repository notation and the administrative potential H are inherited from PR #141 at `b62f56cda3ebe1f77ea843740e37199ae0685bee`, especially `research/ay-return-recovered-20261031/RECOVERY.md`, R3, and the original `ay-swarm-20261030` packet. The previous transversal and inverse-credit statements remain unchanged. This pass does not improve the 7/3 inverse compiler or invoke the old K-rank ancestor-elimination theorem.

A targeted literature search checked the AYH source and searched for bounded Hamming weight, digit-sum and sparse-source stopping statements. It was not an exhaustive priority audit. Classical parity-word affine lifting underlies Section 6; no priority is claimed for that elementary identity or for finite stopping-time density methods.

## 1. A uniform homogeneous escape lemma

**HC-1.** For S>=2 and a positive odd u with s(u)<S, define

    h_S(u) = min { j>=0 : s(3^j u)>=S }.

This is a total integer function, with

    1 <= h_S(u) <= J_S := 2^(S-1)-1.

### Proof

Put m=S+1. Modulo 2^m, powers of 3 form the subgroup of all odd residues congruent to 1 or 3 modulo 8. Its order is 2^(m-2). Indeed v2(3^(2^k)-1)=k+2 for k>=1, by induction using factorization of a difference of squares; the base m=3 is immediate. Thus the orbit of any odd residue under multiplication by 3 is one of two cosets, with low-three-bit sets {1,3} or {5,7}.

The first coset contains 2^m-5, whose popcount is m-1=S. The second contains 2^m-1, whose popcount is m. Each is reached in at most 2^(m-2)-1 multiplications. Popcount of a positive integer is at least popcount of its residue modulo 2^m. This proves the claim. The lower bound is from s(u)<S. No assertion about forward Collatz convergence enters this proof.

For the finite caps used below, complete residue verification modulo 2^20 gives sharper bounds:

| S | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| verified upper bound on h_S | 1 | 3 | 3 | 5 | 6 | 9 | 9 | 10 | 15 |

The producer checks both complete multiplication-by-three cycles. The separate verifier instead starts at each of all 524,288 odd residues and computes its first hit of popcount >=S. This finite calculation lifts to arbitrary positive u because reduction modulo 2^20 commutes with multiplication and cannot increase popcount. It is a universal upper bound, not a census of inputs below 2^20. No claim of optimality over ordinary integers is needed.

## 2. An exact separated-block lemma

**HC-2.** Write an odd input as

    n = 2^D u + v,   u,v positive odd, 0<v<2^D.

Use the shadow odd orbit v_j=U^j(v), set a_j=v2(3v_(j-1)+1), A_j=sum_(i=1)^j a_i, and P_j=2^A_j v_j. If P_h<2^D, then for every 0<=j<=h,

    A_j < D,
    U^j(n) = 2^(D-A_j) 3^j u + v_j,
    0 < v_j < 2^(D-A_j),
    s(U^j(n)) = s(3^j u) + s(v_j).

A sufficient explicit condition is 4^h v < 2^D.

### Proof

P_0=v and

    P_(j+1) = 3P_j + 2^A_j.

Since v_j>=1, 2^A_j<=P_j, so P_j is strictly increasing and P_j<=4^j v. The hypothesis implies P_j<2^D and A_j<D at every intermediate index.

Induct on j. In 3U^j(n)+1 the upper summand is divisible by 2^(D-A_j), whereas the lower summand has valuation a_(j+1)<D-A_j because A_(j+1)<D. Thus the actual valuation is exactly the shadow valuation. Division gives the displayed next state. P_j<2^D gives the disjointness of the upper and lower bit blocks, so popcounts add exactly. The actual large source cannot hit 1 during this separated interval: its upper summand remains positive and even. The shadow state 1 is therefore not being mistaken for an actual physical continuation out of 1. QED.

This is a fixed-source carry argument. The cut, upper prefix, lower shadow and accumulated valuation all belong to one original integer. No neighboring integer is substituted for the actual trajectory.

The strict inequality matters. With S=2, u=v=1, D=2 and h=1, equality 4^h v=2^D holds. The input is 5 and U(5)=1, not a disjoint sum with three set bits.

## 3. A finite core for every popcount cap

Define A_S by the following finite prefix tree. Start with u=1. A node with fewer than S set bits has children

    2^d u + 1,   1 <= d <= 2h_S(u).

Stop each branch once it has S set bits. The nodes themselves, including 1, form A_S. This is an ordered binary-gap construction, not just a scalar digit count.

**HC-3 (finite-core theorem).** For every S>=2:

1. A_S is a finite, explicitly computable set. Its maximum bitlength is at most 1+(S-1)(2^S-2), and its size is at most sum_(j=0)^(S-1) (2^S-2)^j.
2. If n is odd, s(n)<=S and n is not in A_S, some U^j(n), with 1<=j<=J_S, has more than S set bits.
3. Every positive odd orbit whose popcount stays at most S lies entirely in A_S and is eventually periodic (with reaching killed 1 counted as termination).
4. Consequently an ordinary positive orbit is eventually periodic if and only if its odd-state popcount is bounded. Every nonperiodic positive orbit has unbounded odd-state popcount.

### Proof

Part 1 follows from HC-1: each next gap is at most 2J_S=2^S-2, and there are at most S-1 gaps.

For part 2, parse the set bits of n from high to low. Its canonical upper-prefix construction fails membership in A_S at some next gap d>2h_S(u). Let D be the position of the lowest bit of that upper prefix in the full integer. Then n=2^D u+v with v positive odd and

    v < 2^(D-d+1).

With h=h_S(u), the integer inequality d>2h implies 4^h v<2^D. Apply HC-2. At index h, the upper block has at least S ones and the lower positive block at least one. Thus the actual orbit has more than S ones within h<=J_S steps. This is not a chosen future residue or a changing-source statement.

For part 3, apply part 2 at every actual state: a capped orbit cannot contain a state outside A_S. Repetition or termination follows from finiteness. Conversely every eventually periodic ordinary orbit uses only finitely many values, so its popcount is bounded. QED.

**Important non-invariance.** A_S itself is not forward invariant. For example 27 belongs to A_4, but U(27)=41 has only three ones and is outside A_4. HC-3 says that such an outside excursion must soon exceed the cap, not that it cannot occur. The complete checker follows these excursions rather than deleting them.

**Effective decision consequence.** For a fixed S, every capped orbit either terminates, exits the cap, or exhibits a repeated state within |A_S|+J_S odd steps. An orbit starting outside A_S exits within J_S. Starting in A_S, it either repeats while in the finite core or leaves it within |A_S| steps, after which HC-3 supplies the remaining exit bound. Thus the universal capped-termination problem is a finite decision problem, which may correctly return an explicit nontrivial cycle rather than a rank.

This does not supply a uniform cap for an unrestricted ordinary Collatz source.

## 4. Exact finite certificates through cap ten

`run.py core` enumerates the complete adaptive cores and follows every source until 1 or cap exit, detecting repeated states. Its memoization is only an optimization. `verify.py core` independently regenerates the tree by an iterative stack and follows every source directly, without the producer's orbit memo. Both hash the full canonical sequence of (source, outcome, clock), not merely selected examples.

| S | complete core | reaches 1 inside cap | exits cap | maximum odd-event clock |
|---|---:|---:|---:|---:|
| 2 | 3 | 3 | 0 | 2 |
| 3 | 21 | 14 | 7 | 8 |
| 4 | 53 | 45 | 8 | 10 |
| 5 | 637 | 144 | 493 | 17 |
| 6 | 1,801 | 479 | 1,322 | 28 |
| 7 | 24,775 | 1,687 | 23,088 | 37 |
| 8 | 82,275 | 11,296 | 70,979 | 63 |
| 9 | 842,305 | 40,936 | 801,369 | 78 |
| 10 | 3,409,915 | 151,320 | 3,258,595 | 79 |

No cycles or unfinished cases occur in these complete cores. The maximum cap-ten core value is 18,014,402,808,710,485 (55 bits). The reported clocks are odd U events, NOT shortcut T steps and not microscopic SRS rewrites.

**HC-4 (computer-assisted universal statement).** Every positive odd integer either already exceeds cap ten, reaches 1, or exceeds ten set bits within at most 79 odd events. Therefore every orbit whose odd values never exceed ten ones converges to 1.

Proof: combine the full core certificate, whose maximum is 79, with the universal outside-core bound 15 from Section 1. The theorem quantifies over arbitrarily large ordinary inputs; the finite inventory is justified by HC-2/3, not extrapolated from a numeric search cutoff. A core witness 97,313 requires 79 odd events, so the universal bound for this capped hitting problem is attained.

### A complete finite inverse basin

Let B_S be the set of all odd sources that reach 1 without ever exceeding S ones. This set is finite for every S, even before checking for other cycles, because HC-3 places it in A_S. It can be enumerated completely from 1 by inverse BFS:

- A target q divisible by 3 has no odd U-predecessor.
- Otherwise choose a=1 if q=2 mod3 and a=2 if q=1 mod3. The smallest predecessor is m=(2^a q-1)/3.
- Every other odd predecessor is obtained by repeatedly replacing m by 4m+1. Each replacement adds exactly one set bit, so this fan has a finite cap-S cutoff.

Skip already visited states, including the root self-loop at 1. Every newly visited source has a genuine physical path to 1. Conversely every capped path is found by induction backward along its final edge. Since all visited states lie in A_S, the BFS terminates unconditionally for every fixed S.

The verifier compares the actual inverse-BFS set with the actual forward-success set, not just their cardinalities. In particular B_10 has exactly 151,320 odd elements, with largest element 1,099,516,035,413. Even starting values have the same capped behavior as their odd parts.

**Not claimed:** every input whose initial popcount is <=10 converges. Such a source can leave the cap, and that is an EXIT certificate, not a convergence certificate. For instance the cap-four source 39 immediately moves to 59, which has five ones.

## 5. A well-founded order for all eleven rules, with an exact guard

Proper words have form c w d. At c start with value 1; letters a,b apply 2x,2x+1, and e,f,g apply 3x,3x+1,3x+2. The rules are

    ad -> d      bd -> gd
    ae -> ea     af -> eb     ag -> fa
    be -> fb     bf -> ga     bg -> gb
    ce -> cb     cf -> caa    cg -> cab.

The first two perform one shortcut T step. All others preserve value. Retain the inherited H(w): sum, over ternary letters e,f,g, of bitlength of the prefix value immediately before that letter.

Let q(n) for positive odd n be the first U-hit time of {1} union {s>S}, with S=10. Section 4 proves q is a total function bounded by 79; q is zero on these terminal states. It is computed using at most 79 odd steps, not by assuming eventual Collatz convergence.

**HC-5.** On proper words, permit the original eleven rules only while s(oddpart(value(w)))<=10, stopping as soon as the cap is exceeded. The lexicographic natural-number triple

    rho(w) = (q(oddpart(value(w))), v2(value(w)), H(w))

strictly decreases on every permitted rewrite. Equivalently use the ordinal

    omega^2 q + omega v2(value) + H < omega^3.

### Proof

An administrative rule preserves value and decreases H exactly one. For an internal binary/ternary swap, the moved ternary letter's prefix changes from 2x or 2x+1 to x, losing one bit of bitlength. Later prefix values agree by the affine identity. Each c-boundary rule removes a ternary letter of weight one. This is the inherited administrative-potential argument, included to expose the exact dependence.

On ad->d, oddpart is unchanged, v2 drops one, and H is unchanged. On bd->gd, the original source is odd n>1, the next oddpart is U(n), and q(U(n))=q(n)-1. The other coordinates may increase, but the first strictly decreases. The terminal value 1 has only the proper word cd, so no physical outgoing odd step is needed. QED.

This is a value-guarded semantic order on proper words. It is NOT a context-compatible reduction order on arbitrary strings, and NOT an order for the unrestricted AYH relation. All eleven rules are included, but their arbitrarily long iteration after cap exit is not.

### Explicit microscopic budget

**HC-6.** If an initial permitted proper word has value N, b=b(N), and H=H(w), every capped rewrite sequence has at most

    H + 80(b-1) + 3239

literal rewrites, independently of scheduling.

Let d<=79 be its number of odd dynamic events and k its total dynamic events. Each odd shortcut event multiplies value by at most two; each even event halves it. Since the final value is at least one,

    k <= floor(log2 N) + 2d = b-1+2d.

Only an odd dynamic event creates H, by adding b((n-1)/2)=b(n)-1. Before its j-th odd event the current bitlength is at most b+j-1. Thus total H creation is at most d(b-1)+d(d-1)/2. Administrative events each consume one H. The total is consequently at most

    H + (d+1)(b-1) + d(d-1)/2 + 2d.

Substitute d=79 to obtain 3239=3081+158. This is not an unrestricted Collatz running-time bound.

## 6. A different route: sparse sources without a trajectory cap

The next certificates keep the ORIGINAL numeric source as the decreasing quantity. They place no restriction on the popcount or size of intermediate states.

### Affine lift

A k-step shortcut parity word containing t odd events has an integer C>=0 with

    T^k(n) = (3^t n + C)/2^k

on its residue class modulo 2^k. If the word takes a source v>1 to e<v, then 3^t<2^k. Every n=v+2^d u with d>=k and u>=0 follows the same parity word and has

    T^k(n) = 3^t 2^(d-k)u + e < n.

For v=1 use the explicitly shadow word 1->2->1, k=2,t=1,e=1; the inequality is strict for every proper lift 1+4u with u>0. It does not prescribe a physical trajectory from 1.

The lifting identity is classical. The complete source-bit-position forest and its finite verification are the contribution of this section within this packet.

### The low-set-bit forest

**SC-1 (finite cover certificate).** Begin with prefix v=1. For every node v>1, obtain a finite first-descent word of length k(v), odd count t(v), and endpoint e(v)<v; for v=1 use the shadow word above. Export the cylinder

    n = v mod 2^B(v),   B(v)=max(b(v),k(v)).

It certifies strict descent for every member n>1. Append children

    v + 2^d,    b(v) <= d < k(v),

and repeat until W set bits have been appended in total. If every resulting node has its asserted valid word, the exported cylinders cover EVERY positive odd source of popcount <=W, apart from the already terminal 1.

### Proof and quantifiers

Read the set bits of any source from low to high. At a node v, either the source has no further set bit, and is the node itself, or its next set bit is at a position d>=b(v). If d>=k(v), the full source agrees with v modulo 2^B(v), and the affine lift supplies descent from that full original source. If d<k(v), its next low prefix is exactly one of the enumerated children. A source with at most W ones must finish or enter a certified cylinder within W nodes. The locations of its upper set bits are unrestricted.

The exported cylinders are pairwise disjoint. A descendant has a new one at a position where its ancestor's cylinder requires zero. Different children disagree at the first of their next-set-bit positions. If k(v)<=b(v) there are no children. Thus their natural density is the exact Kraft-type sum sum_v 2^-B(v); conditioning on odd inputs doubles it. The exceptional point 1 does not affect density.

This is a finite certificate implication, NOT a proof that the procedure succeeds at every W. A node with no certified finite descent must be reported as unfinished, not silently assigned a word.

### Complete certificate at W=8

`run.py sparse` uses accelerated arithmetic, accounting exactly for partial final halvings. The separate checker uses literal shortcut steps, recomputes the full affine numerator, checks strict ORIGINAL-source order, regenerates every child inventory, and reconstructs every exported cylinder as an exact dyadic interval after bit reversal. Sorting these intervals verifies pairwise disjointness independently of the tree proof.

| set bits | nodes at this level | largest node bitlength | largest first-descent clock |
|---|---:|---:|---:|
| 1 | 1 | 1 | 2 (shadow root) |
| 2 | 1 | 2 | 4 |
| 3 | 2 | 4 | 7 |
| 4 | 5 | 7 | 59 |
| 5 | 103 | 59 | 137 |
| 6 | 1,786 | 137 | 214 |
| 7 | 31,207 | 214 | 365 |
| 8 | 585,311 | 365 | 552 |

There are exactly 618,416 nodes and disjoint cylinders. All node words pass; their clocks total 72,618,524 shortcut operations, including the two explicitly marked root-shadow operations. The full certificate stream hash is recorded in `sparse.json`.

**SC-2 (computer-assisted universal descent).** Every integer n>1 with s(n)<=8 has T^k(n)<n for some 1<=k<=552. Odd sources follow the forest argument; even sources descend immediately. Intermediate popcounts are unrestricted. The clock bound is attained by the weight-eight witness recorded in `sparse.json`.

This excludes at-most-eight-one values as the LEAST counterexample, not all such values as possibly belonging to a hypothetical nonconvergent component: descent could reach a smaller source with more ones. A minimal nontrivial cycle point must also fail the selector. No proof that every sparse starting value converges is claimed solely from SC-2.

Every exported cylinder uses at most 552 low bits. Their exact conditional density among odd integers is the numerator in `sparse.json` divided by 2^552, approximately 0.9058716686001891. Thus this explicit finite selector covers about 90.59% of odd sources, including every source with <=8 ones regardless of magnitude, and many denser ones. This is a selector-domain density, not a fraction of Collatz resolved and not an improvement over the known density-one theorem for unrestricted finite stopping time.

The total selector `compile_descent(n)` follows at most eight certified low prefixes. It returns (clock, smaller endpoint) or None. Its None is FAILED_GUARD, not evidence of divergence. Its endpoint uses the exact affine lift, so it can handle enormous upper bits without enumerating them.

**SC-3 (source-persistent augmented order).** During an admitted macro retain the original source N, remaining dynamic clock k, and administrative H. The lexicographic order (N,k,H) decreases on every literal rewrite inside that macro: administrative steps lower H, dynamic steps lower k. At macro completion, the verified endpoint N'<N permits a fresh macro with first coordinate N'; otherwise the controller stops at 1 or FAILED_GUARD. All finite or infinite interleavings of admitted macros therefore terminate. There is no resetting to a larger comparison floor. This is an order on a guarded augmented controller, not the unrestricted SRS.

## 7. Exact boundary and next mathematical target

The carry-core theorem and sparse-source theorem solve different restricted problems. The first controls whole trajectories that stay within a digit cap; the second guarantees a numeric decrease from every covered source while permitting large intermediate digit counts. Their ranks cannot simply be switched after a failed guard.

A simple warning is that q_2(7)=0 because 7 is already outside cap two, whereas q_3(7)=5. Raising the cap can raise the rank. Likewise local numeric decreases above an unchanged original floor do not provide a decrease below that floor. The earlier repo's 42/364 comparison-floor counterexample is not repaired merely by a larger menu.

The generic finite-core argument is not enough to distinguish convergence from cycles. For the odd 3n-1 map, 5->7->5 is an explicit bounded-popcount cycle, and source 7 nevertheless has an immediate numeric decrease. Our control suite retains it. The cap-ten no-cycle conclusion depends on the actual 3n+1 core verification.

The remaining target is a source-dependent, globally paid envelope controlling cap increases or a total extension of the sparse-source selector. The present work supplies neither. Equivalently, HC-3 reduces eventual periodicity to bounded popcount on each fixed ordinary orbit, but bounded popcount on every orbit and exclusion of all nontrivial positive cycles remain unproved. An infinite chain of successful finite caps is not a proof about one fixed source without a finite bound for that source.

The next useful direction is not merely a larger digit census: retain the separated carry cut and its valuation debt across a cap increase, and prove that a numeric source decrease or a paid compatible carry-coordinate decrease must occur. The two explicit orders above provide checkable endpoints for such a bridge; its coverage is the first unsupported step.
