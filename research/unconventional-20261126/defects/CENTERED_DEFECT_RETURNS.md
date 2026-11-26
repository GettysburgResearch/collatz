# Finite returns to multiplicative groups across a bounded number of mismatched Syracuse valuations

**Status.** Proposed proof for positive ordinary integers, using the published finite-rank unit-equation theorem of Evertse, Schlickewei and Schmidt. The physical number of odd steps and the individual division exponents are unrestricted. The conclusion gives no uniform termination proof.

## Statement

Write the actual odd Syracuse trajectory as

\[
 2^{a_i}q_{i+1}=3q_i+1,\qquad q_i\in 2\mathbb N+1,\quad a_i\ge1.
\]

Fix a periodic list of positive exponents \(m_i\) and its rational periodic orbit \(c_i\), at a specified phase. More explicitly, for period \(p\) and \(S_j=\sum_{i<j}m_i\), set
\[
 c_0=\frac{\sum_{i<p}3^{p-1-i}2^{S_i}}{2^{S_p}-3^p},\qquad
 2^{m_i}c_{i+1}=3c_i+1.
\]
The denominator is nonzero and prime to 2 and 3. The rotated numerator at every phase is odd, so every \(c_i\) is nonzero with 2-adic valuation zero. Rotation of the displayed formula verifies periodicity and makes every nominal exponent exact. Both signs of the rational center are allowed. Define \(D_i=q_i-c_i\). Call an index a mismatch if \(a_i\ne m_i\).

**Theorem 1.** Fix finite-rank subgroups of \(\mathbb Q^\times\), or finite unions of their cosets, for the two endpoint distances. Fix \(R\ge1\). There are only finitely many triples consisting of an initial phase, a positive odd ordinary source, and a segment length such that both distances belong to their prescribed sets and the segment has between one and \(R\) mismatches. The multiplicative groups contain only nonzero numbers. Membership at either end can instead be stated for the absolute distance by adjoining \(-1\).

This conclusion applies, for example, to Mersenne-to-Mersenne segments with boundedly many exponents above one, even if their intervening runs of exponents equal to one have no common length bound. The center in this case is \(-1\), and the distance is \(q+1\). Omitting the requirement of a mismatch makes a uniform finiteness assertion false. From \(q_0=2^n-1\), the first \(n-1\) odd transitions all have exponent one. Throughout them \(q_j+1=2^{n-j}3^j\), in one fixed rank-two group.

**Theorem 2.** Fix the template, a rank bound \(r\), and \(s\) allowed cosets. Consider any simple segment of actual positive odd states and list only its mismatch inputs. In any window of \(N\) consecutive such inputs the proportion of centered distances in a union of \(s\) cosets of a rank-\(r\) subgroup tends to zero as \(N\to\infty\), uniformly over the ordinary source, the window, the group and the coset representatives. In particular, a hypothetical nonperiodic orbit has infinitely many mismatches, and each fixed bounded-rank test has zero upper Banach density on this mismatch clock. For the template \(-1\) this concerns the inputs at *ends* of ascent runs, even if those runs grow without bound.

The argument also gives a fixed-floor consequence. For every fixed odd floor \(H\) and \(R\), only finitely many Mersenne sources can reach an odd value at most \(H\) using at most \(R\) exponents above one. Zero-mismatch paths initially increase. For nonzero mismatch paths, the endpoint distance belongs to the finite set \(\{q+1:1\le q\le H\}\).

## The two endpoint terms and the first mismatch

Enlarge to one finite-rank group containing both allowed families, \(-1,2,3\), and every center. Put \(A_i=\sum_{t<i}a_t\). For a segment of \(h\) steps, define
\[
 B_i=3^{h-i}2^{A_i}D_i.
\]
At a mismatch the bank changes by two signed terms
\[
 B_{i+1}-B_i=
 3^{h-i-1}2^{A_i+m_i}c_{i+1}
 -3^{h-i-1}2^{A_i+a_i}c_{i+1}.\tag{1}
\]
At a match the bank is unchanged and no term is recorded. Thus \(B_0\), the correction terms and \(-B_h\) sum to zero. The centered displacements in the interior need not belong to the group.

Suppose \(d\) is the first mismatch. The correction term there with exponent \(A_d+\min(m_d,a_d)\) has strictly smaller 2-adic valuation than every other correction term. Its partner has larger exponent, and any later correction valuation is at least \(A_{d+1}+1=A_d+a_d+1\). This comparison works when the actual exponent is smaller or larger than the template exponent. A subset of correction terms containing this first marker cannot sum to zero, by its unique least 2-adic valuation.

Write \(C=1+\max_i|c_i|\), \(M=\max_i m_i\), and choose an integer \(K\ge16(R+1)(2^M+1)C\). On a step whose two true states exceed \(K\), \(D_i\ge q_i/2>0\). The two absolute terms in (1), divided by \(B_i\), sum to at most
\[
 \eta=4(2^M+1)C/K\le 1/(4(R+1)).
\]
Indeed the low term has ratio at most \(2^{M+1}C/(3K)\). In the high term use the *actual* equality \(2^{a_i}=(3q_i+1)/q_{i+1}\) to bound its ratio by \(8C/(3K)\). This bound does not depend on the size of the division exponent. At a match the ratio added is exactly zero. Summing the resulting geometric bound, the combined absolute size of all corrections is at most \(((1+\eta)^{R+1}-1)B_0<B_0\). In particular, a zero subsum containing \(B_0\) must contain the terminal term.

Partition the entire zero sum into minimal nonempty zero subsums. The block containing \(B_0\) therefore contains the terminal term. The first marker cannot be in a different block, as that block would consist only of correction terms. Hence the same minimal block contains both endpoints and this marker. This argument permits cancellations among the remaining correction terms.

For a fixed finite-rank subgroup \(G\) of \(\mathbb Q^\times\), the set of ratios of two terms that occur in nondegenerate zero sums of elements of \(G\) of arity at most \(2R+3\) is finite. To see this, divide by one term and move it to the other side. This is a nondegenerate unit equation in a subgroup of \(G^{j-1}\) of rank at most \((j-1)\operatorname{rank}(G)\). Arity two is immediate. For greater arity apply Evertse–Schlickewei–Schmidt, Theorem 1.1, over \(\overline{\mathbb Q}\); the rank does not change when the rational subgroup is viewed in that field. Their explicit bound is uniform in the group at fixed arity and rank. No height bound on the individual ratios, or algorithm to list them, is used. [Primary theorem](https://annals.math.princeton.edu/2002/155-3/p04)

For the minimal block just obtained, the ratio of the initial term to the first marker, with its sign, is
\[
 \pm\frac{3D_d}{2^{\min(m_d,a_d)}c_{d+1}}.\tag{2}
\]
All earlier steps were exact matches, so \(B_0=B_d\). Since the minimum in (2) is at most \(M\), the actual first-mismatch **state** \(q_d\) belongs to a finite set. The bound on the cardinality of this set depends only on the template, \(R\) and the rank of the enlarged group.

## Cutting at a small state

If the initial state is at most \(K\) there are already finitely many possible sources. Otherwise, if the segment has a state at most \(K\), cut it at the first such state \(q_j\). Enlarge the group by all integers \(1,\ldots,K\) once. The cutoff and this enlargement depend only on the template and \(R\).

If the truncated segment has no mismatch, its endpoint is already one of finitely many fixed small states. The matched-prefix argument in the next section bounds the start, using \(D_j\ne0\). If \(D_j=0\), every preceding matched displacement was zero. Starting on the reference trajectory then precludes a later mismatch on the original deterministic trajectory.

If the truncated segment contains a mismatch, replace the terminal bank by \(2^{A_j}q_j\). On the final transition the only correction recorded is
\[
 2^{A_{j-1}+m_{j-1}}c_j.
\]
This follows directly from \(2^{a_{j-1}}q_j=3D_{j-1}+2^{m_{j-1}}c_j\), whether or not that final index is a mismatch. All preceding transitions have two states above \(K\). The last correction has the already-bounded low ratio, since only the input needs to exceed \(K\). There are at most \(R+1\) additions of total ratio at most \(\eta\), and the same domination proof applies with the new terminal term.

If an earlier mismatch exists, its first marker is still strictly earlier in 2-adic valuation than the unpaired final low term. If the first mismatch is itself the last transition, the final low term is the only correction and serves as marker. In that last case replace \(\min(m_d,a_d)\) in (2) by \(m_d\), still at most \(M\). Thus a high source that encounters a first mismatch before or at the small cutoff again has only finitely many possible first-mismatch states.

## Recovering the initial source and the terminal clock

Let \(J\) be a common positive odd denominator for the centers. Along any initial matched prefix ending at time \(d\),
\[
 2^{A_d}J(q_d-c_d)=3^d J(q_0-c_0).
\]
The nonzero integer \(J(q_d-c_d)\) is therefore divisible by \(3^d\). The finitely many possible values of \(q_d\) bound \(d\), including when the nominal period is contracting. For each such length, phase and finite endpoint, the displayed identity uniquely determines \(q_0\). This also applies to the no-mismatch prefix ending at the finite small state of the preceding section. A first mismatch cannot occur from a zero displacement because ordinary Syracuse valuation is deterministic and the reference valuation is exact.

There remain finitely many possible starts. If one start admitted arbitrarily long qualifying clocks, its entire future would have at most \(R\) mismatches. After the last one all subsequent steps would match. At the start of that suffix, writing its displacement as \(D\), ordinary integrality gives \(2^{A_t}\mid JD\) for every subsequent prefix of length \(t\). Here \(A_t\ge t\). Thus \(D=0\), after which every endpoint distance is zero and is excluded. This proves Theorem 1 for whole physical segments.

## Uniformity on the mismatch clock

For fixed template, \(r,s,R\), let \(L_R\) bound the number of distinct possible *initial states that are themselves mismatches* in segments covered by Theorem 1. Such a bound is uniform over the group and cosets: the source is either at most \(K\) or is the first-mismatch state in (2). The enlarged group has rank bounded by \(r+s+K+p+3\) when both endpoint tests use the same \(s\) cosets. The arity and the number of phase and marker choices are bounded. The stated uniform form of the unit-equation theorem therefore provides \(L_R\). The bound is on the **number** of candidate states. It does not bound their maximum value uniformly over choices of groups.

In a window of \(N\) consecutive mismatch inputs from a simple trajectory, let \(m\) marks pass the test. Consecutive passing marks cost the number of intervening mismatch indices, counting the first and excluding the last. The sum of these costs is at most \(N-1\). Those of cost at most \(R\) have distinct starting states and there are at most \(L_R\) of them. Those of cost greater than \(R\) number at most \((N-1)/(R+1)\). Hence
\[
 m\le 1+L_R+(N-1)/(R+1).
\]
Send \(N\) to infinity at any fixed \(R\), then increase \(R\). On a nonperiodic positive orbit all states are distinct and every finite change to an eventual exact template would force equality to its rational center as above. This proves Theorem 2.

## Related results and remaining question

The exact affine word and periodic rational-center formula are classical. Existing work bounds multiplicative rank and coset visits of the *raw* odd states on the ordinary odd clock, including source-uniform unit-equation bounds. It does not directly apply to translated states on the mismatch clock. Another result treats long runs with a fixed intervening connector and bounded head coefficients. Repository work at e4ca639326bac73da8c2a698dec8a749e5efbe68 bounds binary run complexity at fixed odd separations; the number of true odd steps here may be arbitrarily large at fixed mismatch count. These are comparisons of hypotheses and conclusions, not historical-priority claims. [Raw-state unit equations](https://rstation.ai/problems/collatz/papers/137) · [Raw-state rank bounds](https://rstation.ai/problems/collatz/papers/138) · [Fixed-connector result](https://rstation.ai/r/collatz/posts/60) · [Repository sparse-endpoint proof](https://github.com/GettysburgResearch/collatz/blob/e4ca639326bac73da8c2a698dec8a749e5efbe68/research/lean-exact-witness-global-20261121/LITERATURE_ARITHMETIC_RETURN.md)

A close antecedent is Theorem 2 of rStation paper 15, which unrolls periodic pieces, dominates correction terms at high states, and prunes vanishing subsums. Its fixed-cost conclusion bounds the upper excursion in terms of the source. The first-mismatch marker in (2) instead pins a particular ordinary internal state from a finite-rank test on both endpoints. Paper 15 also proves a stronger dictionary-cost lower bound for long positive cycles than elementary piece-length estimates. No general dictionary cycle-complexity claim is made here. [Paper 15, Theorems 1–2 and Corollary 4](https://rstation.ai/problems/collatz/papers/15)

Theorems 1–2 provide no reason that the distances of a hypothetical nonperiodic orbit must keep returning to a bounded-rank family. Nor do they prove that an orbit starting at a Mersenne number eventually reaches a floor. Unbounded mismatch counts and increasing arithmetic complexity remain compatible with all the statements here.
