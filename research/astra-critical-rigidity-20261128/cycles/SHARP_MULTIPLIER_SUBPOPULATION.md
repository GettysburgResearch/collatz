# A sharp two-thirds subpopulation of uniformly independent ordinary multiplier paths

**Proposed written theorem.** Use the shortcut Collatz map \(T\), choose \(x\) uniformly in any interval of \(N\) consecutive positive integers, and set \(t=\lfloor\log_2N\rfloor,\ B=\sqrt t\). Let \(m=m_t\to\infty\) satisfy \(\log m=o(B)\). For a positive odd \(A\), a positive even \(D\) with \(v_2(D)=o(B)\), and arbitrary integer offsets \(b_i\), let \(y_i=(A+Di)x+b_i\) be positive throughout the interval, \(0\le i<m\). Neither the odd parts of the slopes nor the magnitudes of the offsets or the interval origin are bounded. Put \(\gamma=\log_23,\ b=1-\gamma/2\) and interpolate the true paths
\[
                  Y_i(k/t)=\frac{\log_2 T^k y_i-\log_2 y_i+bk}
                                       {\gamma B},\qquad 0\le k\le t.
\]

There is a deterministic residue \(c_t\bmod3\) such that the set
\[
               S_t=\{0\le i<m:\ i\not\equiv c_t\pmod3\}
\]
has the following uniform property. For each fixed \(k\), **every** sequence of \(k\) distinct indices in \(S_t\) gives joint convergence of the corresponding actual paths to \(k\) independent Brownian motions of variance rate \(1/4\). The probability of a numerical meeting of any pair among those selected arms at any date through \(t\) tends to zero, uniformly over the choices of the \(k\) distinct indices. The single residue \(c_t\) can serve all fixed \(k\) and is independent of the random ordinary input. In particular \(|S_t|\ge2m/3-O(1)\).

The constant \(2/3\) is sharp for this **uniform-over-selections** assertion, already with \(A=1,\ D=2,\ b_i=0\). For these pure odd multipliers any subset of cardinality exceeding \(2m/3+O(1)\) contains a pair whose normalized paths have the same Brownian limit along the pair, precluding a uniform independent-pair limit. This does not diminish the [translated population theorem](../literature/TRANSLATED_MULTIPLIER_POPULATIONS.md): it proves the empirical Wiener law for the entire progression, allows arbitrary \(m\to\infty\), and need discard only a negligible fraction of random *pairs*. Here a single deterministic subset works against individual choices of indices. It does not imply simultaneous independence of a growing number of full paths.

## One rational center for the whole exceptional graph

Use the following short-sum consequence of the Subspace Theorem, proved in the [population paper, first section](../literature/TRANSLATED_MULTIPLIER_POPULATIONS.md). For fixed \(s,C\), a nonzero sum of at most \(s\) terms \(u_j3^{h_j}\), with \(|h_j|\le CB,\ \log(2+|u_j|)=o(B)\) and integral coefficients, has binary valuation \(o(B)\) in the upper-bound sense. This allows negative exponents. Its fixed forms, primitive scaling, and induction on a proper exceptional subspace are the only ineffective arithmetic input here.

Fix \(R,\varepsilon>0\). Call a pair \(i\ne j\) exceptional if for some integer \(|h|\le RB\)
\[
       v_2\big((A+Dj)/(A+Di)-3^h\big)\ge\varepsilon B .               \tag{1}
\]
The relation is symmetric under reversing the pair and exponent. The exponent is nonzero, since \(v_2(D(j-i))\le v_2(D)+\log_2m=o(B)\). It is unique for large \(t\): for different admissible exponents the binary valuation of the difference of their powers of three is \(O(\log(2+RB))\) by lifting the exponent, smaller than \(\varepsilon B\). Orient each edge using its positive exponent.

Take **any** two oriented edges \(i\to j,\ k\to l\), whose initial vertices may be different. Set \(z=3^h-1,\ w=3^{h'}-1,\ u=j-i,\ v=l-k\). Since \(A+Di\) and \(A+Dk\) are odd, (1) gives \(Du\equiv(A+Di)z\) and \(Dv\equiv(A+Dk)w\) modulo \(2^{\lceil\varepsilon B\rceil}\). Eliminate \(A\) and cancel \(D\) at cost \(v_2(D)\):
\[
                   v_2\big((i-k)zw-uw+vz\big)
                           \ge\varepsilon B-v_2(D).                    \tag{2}
\]
Expansion gives at most four ternary monomials, with exponents at most \(2RB\) and integer coefficients \(O(m)\). Since \(\log m=o(B)\), the short-sum result forces the expression in (2) to be exactly zero. This holds simultaneously for all edge pairs at all sufficiently large \(t\), for the fixed \(R,\varepsilon\): otherwise pick a violating pair along a subsequence. Dividing by \(zw\ne0\) gives \(i-u/z=k-v/w\). Thus when there is any exceptional edge at all, there is **one** rational center \(C\), common across the entire graph, for which each oriented edge satisfies
\[
                           j-C=3^h(i-C).                               \tag{3}
\]
One edge alone defines the same center. A denominator of \(C=i-(j-i)/(3^h-1)\) is prime to three, also after reduction. This argument was found independently in the multiplier and cycle lanes by eliminating the two different initial positions; the population paper proves its common-initial-position version.

Write \(C=P/Q\) in lowest terms with \(Q>0\), and choose \(c\equiv P Q^{-1}\pmod3\). For an increasing-exponent edge (3) its terminal point satisfies \(Qj-P=3^h(Qi-P)\), so \(j\equiv c\pmod3\). Thus removing **one residue class of indices** eliminates every exceptional edge. If no exceptional edge exists, choose any residue class to remove.

The same center yields the more precise count \(|E|\le m/2+O(\log(2m))\), uniformly after the ineffective onset. For \(1\le h\le\log_3(2m)\), possible initial integers \(i\) with \(0\le3^h i+(1-3^h)C<m\) lie in an interval of length at most \(m/3^h\). Summing gives \(m/2+O(\log m)\). For larger exponents, (3) implies \(|i-C|=|i-j|/(3^h-1)<1\), leaving at most two initial integers. Each has at most \(O(\log m)\) neighbors: the distinct \(|i-C|3^h\)'s have integer differences, grow by factors at least three, and fit in an interval of length \(m\). For \(n\ge2\) such ordered positive values, the second is at least one, so the last minus the first is at least \(3^{n-2}\). The case \(i=C\) cannot be an edge. This proves the count. For \(A=1,D=2\), the exact power-of-three pairs already have \(m/2+O(\log m)\) edges, by summing the odd source counts at \(3^h(2i+1)\le2m-1\).

## Uniform paths and sharpness

For each fixed integer \(J\ge1\), the preceding graph conclusion holds on the data sequence for \(R=J,\ \varepsilon=1/J\) at all sufficiently large \(t\). Diagonalize these onsets, choosing a deterministic \(J_t\to\infty\) slowly enough that the conclusion holds for \(J_t,1/J_t\). Take its discarded class as \(c_t\). For *any* distinct selected indices \(i,j\in S_t\) and every fixed \(R\), their odd dyadic ratio \(\alpha_t=(A+Dj)/(A+Di)\) now satisfies
\[
             B^{-1}\max_{|h|\le RB}v_2(\alpha_t3^h-1)\longrightarrow0 .
\]
The sign change of the exponent is harmless since \(3\) is a binary unit. The [deterministic raw-occupation criterion and arbitrary-offset transfer](../literature/TRANSLATED_MULTIPLIER_POPULATIONS.md) therefore give independent Brownian limits for any fixed selected tuple, testing its finitely many pair brackets. That proof also gives vanishing probability of a numerical coincidence at the deadline for each selected pair: the own-source-centered difference has a continuous normal limit, while the initial log ratio off a set of measure \(\eta\) lies in a bounded interval about its deterministic right-endpoint value. For a fixed pair of actual trajectories, an earlier meeting persists until the deadline. A union bound proves the finite-tuple statement. Uniformity in choices follows directly by selecting an offending deterministic tuple if any worst-case discrepancy fails to tend to zero.

For the sharpness example, the odd multipliers \(1,3,\ldots,2m-1\) divide into classes by their prime-to-three part. The number of classes is the number of these odd integers not divisible by three, namely \(2m/3+O(1)\); each odd core in the range is itself a multiplier. Any larger selection contains two multipliers in a ratio \(3^h,\ 1\le h\le\log_3(2m-1)=o(B)\). For the two raw grade paths the lower arm under dyadic Haar is uniform even when its odd multiplier varies. The [zero limiting gap case in the coalescing proof](../literature/INDEPENDENT_MULTIPLIER_PATHS.md) gives the same Brownian motion for both arms, since the initial exponent difference divided by \(B\) tends to zero and the relative affine offset is zero. The common shortened-word transfer and own-source height correction in the population paper give the same result on the sampled ordinary intervals; each initial height here is at least \(x\). Identical limiting motions are incompatible with independent ones. This proves optimality.
