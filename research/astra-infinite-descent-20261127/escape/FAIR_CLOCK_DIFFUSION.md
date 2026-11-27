# A universal closed correction set and uniform first-arrival row bounds

**Source-qualified written theorem.** The ordinary correction factors of all finite simple positive odd-map segments, over all starting integers, endpoints, grades and physical clocks, belong to a single compact set \(K\subset[c,1]\) of Lebesgue measure zero. Its shrinking neighborhoods give a uniform cutoff on the *starting integers* contributing to every exact first-arrival row at the fair weight \(3^d2^{-m}\). Consequently the largest normalized row mass has a limit as \(d\to\infty\). A positive limit is attained by an actual finite synchronized class of escaping integers.

The two imported inputs for these statements are the uniform high-vertex reciprocal tail on finite simple odd orbits and the zero length of the **closed** correction support at each *fixed* positive odd root. The latter uses the retained joint floor, the ordinary trace floor, the fixed-root inverse-path law and the synchronization results listed in PR193. Neither input is formalized here. The argument below passes from the fixed-root statement to simultaneous control of arbitrary moving targets. [Uniform simple-path estimate](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-unconventional-20261126/boundary/TILTED_TRACE.md) · [PR193, fixed-root closed support and dependencies](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md) · [Weaver, Paper 175](https://rstation.ai/problems/collatz/papers/175/v1)

The precise fixed-root input is equation (1) of PR193’s [closed-support note](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CLOSED_CORRECTION_SUPPORT.md). Its one-sided cylinder estimate uses Weaver 12/v1, Lemma 13, equation (39) and the proof of Theorem 14. Its singular carrier uses Weaver 175/v1, Theorem 3, and the fixed-root law in PR193, whose inputs include Valbuena’s passage stabilization, natural predecessor densities, the ordinary trace floor and the finite-quotient moment bounds. These are manuscript inputs, with the review status in the pinned source. The uniform high-vertex tail itself has the elementary dyadic packing proof in the linked tilted-trace note. [Weaver 12/v1](https://rstation.ai/problems/collatz/papers/12/v1) · [Fixed-root inverse law and input statements](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md)

## All simple segment corrections

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odds, \(w(x)=3x/(3x+1)\). For an odd path \(x_0,\ldots,x_d=y\) put \(m=\sum_{i<d}v_2(3x_i+1)\). Write \(\omega=3^d2^{-m}\). Its normalized affine correction is exactly
\[
       b(x_0,y)=\omega x_0/y=\prod_{i<d}w(x_i).
\]
Call the path simple when its states are pairwise distinct. Include the empty path with correction one. An ordinary first visit has this property, since a repeated state before the destination would prevent a first visit at the specified time. The normalized correction stays the same on prefixing the shortcut path by any number of initial halvings. Cutting at any intermediate odd state multiplies the two correction factors.

The reciprocal-tail input states that \(T(H)=\sup_{\rm simple}\sum_{i<d,\ x_i>H}1/x_i\to0\), together with finite uniform full reciprocal sum. Thus every simple correction exceeds an absolute \(c>0\). An entire segment with all departures above \(H\) has correction at least \(\exp(-T(H)/3)\).

Let \(K\) be the closure of the set of simple corrections. For each positive odd \(q\), let \(K_q\) be its fixed-root normalized first-visit correction closure. It is compact and null by PR193 after the affine change \(r\mapsto 1-r/q\). A multiple of three can only be a target of the empty odd path. Let \(D_q\) be the closure of the corrections of simple forward prefixes *starting* at \(q\). A single deterministic orbit gives either finitely many such prefixes or one monotone sequence and its limit. Hence \(D_q\) is countable and compact.

If \(t\in K\) and \(t<1\), choose \(H\) with \(\exp(-T(H)/3)>t\). Every sufficiently late member of a sequence of simple corrections approaching \(t\) has an odd departure at most \(H\). A subsequence passes through the same \(q\le H\). Splitting there shows that all its corrections belong to \(K_qD_q\), which is compact by continuity of multiplication, and null as a countable union of dilates of \(K_q\). Therefore
\[
                K\subseteq\{1\}\ \cup\!\bigcup_{q\ {\rm odd}} K_qD_q,
                \qquad |K|=0.                                      \tag{1}
\]
The low-vertex extraction is what permits taking the *closure* before measuring the full union.

## Source tightness at the fair clock weight

For every positive odd target \(y\), grade \(d\) and shortcut clock \(m\), consider all positive integer starts \(z\) whose first visit to \(y\) takes exactly \(m\) shortcut steps, including exactly \(d\) odd departures. Initial powers of two are allowed. Take any subset \(A\) of those starts. With \(h=3^d2^{-m}/y\) one has \(hz\in K\) for each \(z\in A\). The points \(hz\) have spacing at least \(h\). If one such \(z>R>0\), then \(h\le 1/z<1/R\). The disjoint half-open intervals of length \(h\) based at each marked point belong to the \(1/R\)-neighborhood \(K_{1/R}\). In particular
\[
   \sup_{y,d,m}\frac{3^d2^{-m}}{y}
       \#\{z>R:z\hbox{ first visits }y\hbox{ at }(d,m)\}
       \ \le\ |K_{1/R}|\ \xrightarrow[R\to\infty]{}0.                 \tag{2}
\]
Compactness and nullity give the vanishing neighborhood length. The normalization in (2) is critical: the individual estimate \(h\le 1/z\) alone yields a nonsummable majorant. An explicit rate would require additional quantitative information on the length of these neighborhoods. In particular, every consecutive synchronized block \([z,z+L]\) first visiting one odd \(y\) at one clock and grade satisfies \(L/z\to0\) as \(z\to\infty\), uniformly in every other parameter. Apply (2) to the block with \(R=z-1\) and use \(hz\ge c\). This is compatible with the unconditionally constructed fixed patterns in [the merger packet](../merger/FINITE_BLOCKS.md).

At a fixed odd target \(y\), each of the finitely many sources \(z\le R\) can first visit \(y\) at most once. Hence (2) implies
\(\sup_m 3^d2^{-m}\#\{z:\text{first at }(d,m)\}\to0\) as \(d\to\infty\). The same fixed-\(y\) statement holds with **all visits**. If \(y\) has a positive return, let its first lap have grade \(D\ge1\), physical clock \(H\), multiplier \(\lambda=3^D2^{-H}<1\). The all-visit weighted row is the sum over \(j\ge0\) of \(\lambda^j\) times the first-visit weighted row at \((d-jD,m-jH)\), with impossible indices zero. First rows are uniformly bounded at fixed \(y\) by (2) plus a finite source cutoff. Apply dominated convergence to the geometric series. If \(y\) has no positive return all visits are already first visits.

## The limiting largest row

Write \(W_d=\sup_{y,m}h\,\#\{z:\text{first at }(d,m)\}\). For an escaping start \(z=2^r u\) with \(u\) odd, set \(b_\infty(z)=\prod_{j\ge0}w(U^ju)>0\). Two escaping starts belong to the same class if, at some common number of odd departures, they are at the same odd vertex and have spent the same total shortcut time including their respective initial halvings. Both agreements persist at every later odd grade. The relation is an equivalence relation. In a class \(G\), \(b_\infty(z)/z\) has the same value for every member, by taking the limit of the common values \(3^d2^{-m}/y\). In particular all its members obey \(z\le z_0/b_\infty(z_0)\) for any fixed \(z_0\in G\), so each class is finite. Then
\[
  \lim_{d\to\infty} W_d
       =\sup_{G}\sum_{z\in G}\frac{b_\infty(z)}{z},                  \tag{3}
\]
taking the supremum to be zero when no escaping start exists. Whenever positive this supremum is a maximum.

Indeed truncate the source set at \(R\). For large enough \(d\), no bounded-orbit source in the truncation contributes a first visit after \(d\) odd departures. There are finitely many remaining pairs. Each pair agreeing at some odd grade and clock agrees eventually forever. For sufficiently large \(d\), the nonempty truncated rows are thus exactly the classes restricted to \([1,R]\), and each row mass tends to its indicated finite sum. The error from removing the cutoff is at most \(|K_{1/R}|\) uniformly in \(d\). Let \(R\to\infty\). If the supremum is positive, choose \(R\) with \(|K_{1/R}|\) below half that value. Classes disjoint from \([1,R]\) have total at most this bound by passing to their eventual row limits; only finitely many classes remain in contention. Formula (3) detects unbounded positive orbits and leaves arbitrary finite cycles untouched.

## Allowing arbitrary repeated visits

For the odd map, let \(\widetilde K\) be the closure of all finite segment corrections, now allowing repetitions. If there are only finitely many distinct positive odd cycles, \(\widetilde K\) is compact null: split each repeated visit at the first visit to its endpoint, then remove whole laps. More explicitly a normalized correction ending on a cycle is the first-visit correction multiplied by a power of its cycle multiplier. If the endpoint is nonperiodic the original segment was simple. The set consisting of \(K\) times these powers and zero is compact null for finitely many multipliers in \((0,1)\).

If there are infinitely many cycles, distinct cycles have minima tending to infinity along a sequence. Their once-around multipliers \(\lambda_i<1\) tend to one. A lap of minimum \(M\) is a simple prefix up to its last departure, followed by one edge of reciprocal cost at most \(1/M\). Thus its full reciprocal cost is at most \(T(M-1)+1/M\), even under the convention that the repeated final vertex prevents the complete lap itself from being simple. For a last return to its own initial vertex, the repeated-lap path has correction \(\lambda_i^k\). Every \(t\in(0,1)\) is a limit of such powers, by approximating \(\log t/\log\lambda_i\) by an integer. The endpoints zero and one are also present in the closure. Thus \(\widetilde K=[0,1]\) in this case. The argument supplies no upper bound on the number of actual positive cycles.

