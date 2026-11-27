# Fourth checkpoint: located cycle counts and an ordinary harmonic criterion

**Collatz remains open.** This checkpoint adds a self-contained finite exclusion for the bounded cycle branch, an exact original-law trace for the full conjecture, and further ordinary returns on the delayed family. The infinite estimates stated as open below have not been supplied.

## A restricted cycle would need more than \(10^{1000}\) odd phases

Let an ordinary positive odd cycle have minimum \(s\), all exact valuations in \(\{1,2\}\), and maximum at most \((16s+7)/3\). Every nontrivial primitive cycle satisfying these hypotheses has odd period
\[
                         p>10^{1000}.
\]

The proof combines the preceding complete period screen with two new exact computations. Located CRT histograms eliminate all 25 residual pairs above minimum \(2^{71}\). A separate sorted CRT search covers possible minima below \(2^{71}\): the 692,056 candidates at heights at least \(2^{20}\) all leave the physical strip or use a valuation above two within 53 odd edges; the smaller odd minima are checked directly. No general Collatz trajectory-verification result is needed for this combined restricted conclusion.

The CRT method retains the positions of past and future cylinders on one product-modulus circle. Integer histograms, an exact centered second-moment bound, and an explicit rounding allowance give an upper bound for every possible location of a compulsory rank interval. At the closest retained comparison the upper population is \(7,219,532,352\), while the rank estimate requires at least \(8,814,019,611\).

[Located counts and proof](arithmetic/CRT_PERIOD_EXCLUSION.md) · [Independent minimum census](arithmetic/MINIMUM_CENSUS.md) · [Earlier complete screen](arithmetic/PERIOD_GAP.md)

This does not bound all possible periods, and it does not address the separate first-crossing alternative. The logarithmic rank estimates, finite enumeration completeness and algorithm-to-mathematics arguments are written proofs with exact computational replay. The Lean modules check the stated arithmetic and order kernels; they do not contain a formal theorem asserting this entire period exclusion.

## One finite original-law trace detects the full conjecture

For a chronological exponent word \(w\) of length \(n\), keep it exactly when every prefix obeys \(4A_j(w)\le7j\), where \(A_j\) is its cumulative division clock. Let \(m(w)\) be the least positive ordinary seed of its exact dyadic cylinder. Define the finite rational sum
\[
                         J_n=\sum_{\text{kept }w}\frac1{m(w)}.
\]

The same sum is a centered harmonic observable of the original geometric exponent law, retaining the probability of each accepted word. Its limit exists and equals the sum of \(1/m\) over the fixed ordinary seeds whose entire words satisfy the gate. Consequently
\[
             J_n\longrightarrow0
       \quad\Longleftrightarrow\quad
             \text{every positive integer reaches one}.
\]

The proof keeps ordinary realization explicit. Principal seeds increase along a nested script; new seeds have a summable harmonic birth budget, while each fixed seed either eventually leaves the gate or persists. A least seed in any hypothetical bad component stays above its own minimum and satisfies the gate. The ordinary cycle at one eventually fails it.

A finite inequality \(J_n<1/L\) already certifies convergence for every positive integer at most \(L\). The rational debt reserve
\[
 V_n=\mathbb E_{\rm original}\!
       \left[\mathbf1_{\rm gate}(7n-4A_n+8)\right]
\]
makes \(J_n+V_n\) nonincreasing, starting at nine and tending to the same limit. This reserve controls future births. It gives no uniform time at which a currently present seed must die.

The related uncentered trace detects escape alone. A rational parameter \(1/n\) separates the escape and cycle masses at one common finite depth. The sharper no-adjacent-twos language admits a full-cell posterior trace with a summable ordinary-seed domination at every moment above \(0.551463\ldots\).

[Global prefix trace](escape/GLOBAL_PREFIX_TRACE.md) · [Full posterior trace on the fixed language](escape/PRINCIPAL_SAFE_TRACE.md) · [Harmonic birth kernel](escape/HarmonicBirth.lean)

The missing step is a proof that the displayed centered mass tends to zero. The equivalence and its finite controls do not establish that step.

## Uniformly earlier returns on the delayed Mersenne family

For every \(k\ge1\), set \(m=12\cdot2^{18k}-1\). Under the two already stated consequences of a least canonical disagreement, every positive Mersenne exponent through \(m-3\) is now good. Thus the only possible first bad exponents are \(m-2\) and \(m\).

The new gap-four query is the actual smaller canonical integer \(W=(z-31)/2\). Its two physical paths lead to \(M_{m-4}\) and a negative-seventeen chart. Five periodic phase rows, together with six initial parameters, return that opposing path to an earlier already good Mersenne. Lean checks the all-parameter construction.

After their complete ascents and \(H=18k+4\) additional shortcuts, the three ordinary Mersennes at \(m,m-2,m-4\) reach
\[
                    U_{18k},\qquad27Y_k+2,\qquad Y_k+2,
 \qquad Y_k=3^{9k-3}U_{18k}.
\]
The last two are a fixed affine pair. A source-qualified finite-word absorption theorem and exact stabilization of \(U_{18k}\) give their merger for a density-one set of the original parameters, including every fixed odd-stride progression. On that set the possible first bad exponent is exactly \(m\). Exceptional individual parameters remain.

[Gap-four closure](coupling/OFFSET_FOUR.md) · [Exact delayed positive sources](coupling/DELAYED_UNIT.md) · [Growing native clock obstruction](coupling/POST_VALUATION_WINDOW.md)

## Additional interfaces and failed strengthenings

Monotone upper and lower rounding maps on the full dyadic grid give a cycle exclusion whenever their rotation numbers differ. Equality is only necessary: exact wider-grid controls at minima 9 and 11 have coincident rotations and no physical cycle. Arbitrarily long common physical paths force a growing oscillation cost on a proposed bounded corrector.

The compressed no-adjacent-twos system has exact positive branches \(3t/2\) and \((9t+1)/8\). Its two own-height tests through \(3^{42}\) leave 23 hits, all with finite exits. The translated exceptional set has small ternary Hausdorff dimension, but the unshifted ordinary point remains unresolved.

For the completed escape trace expressed in Dirichlet characters, the nonprincipal coefficient norm is at least \((3/2)^k-3/2\). A character-by-character triangle bound therefore loses exponentially. The required correlated signed L-value estimate remains open, including after accepting the reported Dirichlet GRH verification.

[Extremal grids](arithmetic/EXTREME_COMPLETIONS.md) · [Two-place ordinary test](escape/TWO_PLACE_DIAGONAL.md) · [Character cancellation](MELLIN_CANCELLATION.md)

## Verification boundary

The root independently reconstructed the written arguments and replayed the new Lean sources and complete finite outputs. The replay uses fresh project objects with pinned Lean 4.34.1 and mathlib. The fourth packet has 30 new printed declaration audits and 31 dependency audits, with only the standard axioms, plus seven deterministic controls run in ordinary and optimized Python. The minimum and global-trace additions were replayed as explicit supplemental groups.

The [root review](../../reports/six-hour-20261127/ROOT_FOURTH_REVIEW.md), [execution receipt](../../reports/six-hour-20261127/FOURTH_REPLAY.json), and [source manifest](../../reports/six-hour-20261127/FOURTH_CHECKPOINT_MANIFEST.json) state the exact coverage. Repository integrity checks are separate from these mathematical checks. This checkpoint is a research result with explicit remaining obligations, not a complete proof of Collatz.
