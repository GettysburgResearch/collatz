# Pinned arithmetic progressions and chronological branching in the actual two-color remainder

**PROPOSED written deductions.** Every typical ordinary source is itself the midpoint of many progressions inside its exact ordered future fiber. Successive ternary choices can be made in disjoint early binary windows while preserving both physical futures. These statements hold with original-source exceptions smaller than any prescribed inverse power of the bit depth. A separate short-interval result disposes of locally isolated true discordance with summable weight. Neither result forces a cross-color collision.

Use the shortcut map and the fixed positive odd-slope affine arms of the preceding [ordered projection](https://github.com/GettysburgResearch/collatz/blob/6eb986b0ce0b1836a356474d25d709ed4e948b67/research/ayh-resource-reset-20261124/two-class-descent/ADAPTIVE_PAIRED_PROJECTION.md). At clock h on a full ordinary block of length 2^h, the record retains the endpoint and odd count of **each** arm. Fix A>1. The projection discards original probability O_A(h^(-A)); its polynomial parameters may be enlarged in what follows. Each retained fiber S satisfies

    |S| ≥ F/J,     diam S ≤ LF,     F=2^h/max_i(a_i 3^{p_i}),

where L,J are bounded by fixed powers of h+2. For each fixed γ smaller than 1−(log_2 3)/2, one may restrict to F≥2^(γh), with exponentially small extra cost, using the original complete-grid scalar odd counts and fixed slopes. The proofs below give per-fiber relative bounds; multiplying by the actual fiber weights yields their stated original-source costs. A conditional estimate inside a selected event of mass w divides an absolute discard by w.

## A centered progression through the actual original point

In a retained fiber choose positive integers q,K, after seeing its entire record, subject to

    qK ≤ F,     K ≥ exp(C'_A [log(h+2)]^12).

Except for relative mass O_A(h^(-A)) in that fiber, the marked point n itself has at least

    K exp(−C_A [log(h+2)]^12)

distinct positive v≤K with **both** n−qv and n+qv in S. The constants may depend on a fixed power bound for the number of tests: polynomially many choices of (q,K) per record can be imposed simultaneously with the same final error order, by starting with a larger exponent. A list chosen independently in every retained fiber is allowed. An unrestricted point-dependent choice from exponentially many tests is not asserted.

Here is the counting input and the finite argument. Bloom and Sisask's exposition of the Kelley–Meka theorem, Theorem 21, bounds the number of three-term progressions in a subset of density η of {1,…,K} below by K² exp(−C[log(2/η)]^12). Subtract K possible constant triples and divide by two if ordered orientations were counted. For all K≥4 exp(C[log(2/η)]^12), the number with positive difference is therefore at least K² exp(−C[log(2/η)]^12)/4. [Publication, Theorem 21](https://msp.org/ent/2023/2-1/ent-v2-n1-p02-s.pdf) · [DOI](https://doi.org/10.2140/ent.2023.2.15).

Take any subset S' of S; this extra freedom is needed for the tree below. Partition the integers of its enclosing interval of length N≤LF+1 into residue classes modulo q, and along each class into consecutive tiles of K positions; pad the terminal tile with empty positions. Total padded size is at most N+qK≤(L+2)F for F≥1. In a tile, call a point of S' poor if it has fewer than δK positive symmetric q-steps with both endpoints in S' in the same tile. If the poor points occupied ηK or more positions, the preceding lower bound on progressions within the **poor set** would exceed δK², for δ=exp(−C[log(2/η)]^12)/8. Every such progression has a poor center, and any poor center has fewer than δK qualifying steps even in S'. This contradicts the count. Thus all tiles together contain fewer than η(L+2)F poor points. This also bounds the points poor when all steps of size ≤qK are allowed. Choosing η=(h+2)^(-A-2)/[J(L+2)] pays the padding and gives the assertion for S'=S. It provides an absolute loss relative to the **original** S even if S' has already been trimmed. No lower bound on the density of S' in any particular residue or boundary tile is used. The finite poor-center inequality is checked in SymmetricFutureForks.lean, with the supremum theorem as an explicit input.

For the head arms n and 81n+r all three parents share the first recorded future, and all three children share the second. At a truly discordant center none of the nine cross pairs meet at any finite clocks. On a fixed record, a physical cross-meeting between *any* two members is equivalent to the endpoints having a common future. If the cross-meeting occurred before the record time, continue both trajectories beyond both record clocks to see the implication. This equivalence does not depend on q.

## A full ternary tree of ordinary sources in one fixed record

Assume F≥2^(γh). Fix a large constant C and take an integer w=ceil(C[log(h+2)]^12). Put K=2^w, k_i=i(w+2), and take all i≥0 for which k_i+w≤γh. There are m≫_γ h/[log(h+2)]^12 windows for large h. For stage i use q_i=2^(k_i). Starting at S_m=S and working backwards, form S_i from S_(i+1) by deleting the poor points for that stage **with both endpoints tested in S_(i+1)**. At each stage the proof above discards at most η(L+2)F independently of the previous loss. Since m≤h+1, choosing the error exponent larger by two yields

    |S outside S_0|/|S| = O_A(h^(-A)).

For every n∈S_0 build a tree forward. At node b∈S_i choose any admissible v and give it children b−2^{k_i}v, b, b+2^{k_i}v in S_(i+1). The center child belongs because the sets are nested. All descendants preserve the earlier residues: moves at later stages are multiples of 2^{k_(i+1)}. At this split write s=k_i+v_2(v). Since 1≤v≤2^w, k_i≤s≤k_i+w. The three children agree modulo 2^s and are pairwise distinct modulo 2^(s+2): the outer-to-center differences have exact valuation s and the outer-to-outer difference has valuation s+1. Thus different branches can never rejoin as **source integers**, even though all share the exact recorded futures. In particular there are 3^m distinct leaves. The arbitrary choices may vary from node to node. The center path retains the prescribed original n throughout.

For each original affine arm z=a b+c with odd a, write an outer displacement as ±2^s u, u odd. The first s shortcut parities are identical across the three arm inputs. At clock s their values are exactly

    T^s(z) − 3^{p_s(z)}a u,    T^s(z),    T^s(z) + 3^{p_s(z)}a u.

In particular the two outer parities are identical and opposite to the center parity at that clock, simultaneously on every arm. This follows by iterating the one-step affine lifting identity, and the stated common parities follow by applying that identity at each earlier time. Descendants differ by multiples of 2^(s+2) and inherit these first split decisions. The three choices are distinguishable by the first s+2 parity symbols on each odd-slope arm, by the standard bijection of parity words with binary residues. All inputs realized in S are positive on all the physical arms. The prefix-shift and split-parity formulas are separately checked on the integer extension in SymmetricFutureForks.lean.

The original head rows use the earlier tiling by 2^h blocks with h=floor(c log_2 X), fixed 0<c<1. The two partial ends cost O(2^h/X). The estimates therefore apply to the actual weighted discordant rows, including a prescribed orientation. They give many correlated alternative *pasts*, with an explicitly controlled common prefix and split window. A finite native survivor may already have this tree. After the recording horizon all its leaves have the same two fixed endpoints.

## Locally isolated true discordance is summable

Fix one suffix r and any row-dependent subset E of the actual parameters on a parent row I=[7X,8X) with different invariant colors on n,81n+r. One may prescribe the direction of the disagreement, a pair of target components, or an additional selection in E. Let d=log_2 X. For 1≤D≤X/10 and 0≤k≤2D, one has

    # {n∈E : |E∩[n−D,n+D]|≤k}/X
        ≪ (k/D) min(1,(1+log(2D))^4/sqrt(d)).

Indeed sample a length-D window starting at b∈[7X−D,8X). If it contains an E point, at least one of three ordinary certificates failed: common counted fusion of the D consecutive parents, common counted fusion of the 81D consecutive integers beginning at 81b+r, and the fixed-ray fusion of b and 81b+r. All successful by the same depth t=floor(d) implies every parent and its corresponding child have the same color. The upper block starts remain positive and the odd coefficient 81 permutes each complete binary grid of b. A constant number of complete t-bit grids cover the window-anchor interval. The growing-block bound of [Lyapunov Weaver, paper 124 v1, 9 November 2026, Theorem 1](https://rstation.ai/api/v1/papers/collatz_124/versions/1/download) and the [native fixed-head bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) bound the number of active anchors by O(X min(1,(1+log(2D))^4/sqrt(d))). Count incidences between the displayed poor sources and length-D windows containing them. Each such source appears D times, even at a row boundary because anchors were extended there. Any incident window contains at most k poor sources, since it lies in the radius-D neighborhood of each of them. This proves the claim; it needs no independence between certificates.

For any fixed ε>0 and C, take polynomial windows D≤d^C and k=floor(D/d^(1/2+ε)). The sparse part has row mass O_C(d^(-1−ε)(log d)^4), summable in the geometric head rows. A union over O(log d) dyadic radii is still summable. Thus a remaining discordant ordinary source has many nearby failures of the *same selected kind* simultaneously at these radii, whenever the count threshold is nonvacuous. This conclusion permits the nearby failures to have different endpoint records. The centered-fiber theorem preserves the actual records and uses a different count and scale.

**Boundary.** No argument above shows that one of the nine cross pairs meets or that a variable target displacement on a regenerated two-head track must vary across a fiber. In particular, any witness determined entirely by the labeled trajectories after clock h stays fixed across this whole tree. Counting its leaves as distinct later witnesses would be false. A genuine crossing or a derivation which depends transversely on the varied prefix is still needed for universal convergence.
