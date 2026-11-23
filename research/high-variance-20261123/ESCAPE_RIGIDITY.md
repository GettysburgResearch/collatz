# Escape rigidity: direct attempt and the retained arithmetic step

Date: 2026-11-23. **Attempted closing argument; no escape-exclusion theorem
was obtained.** This note records the high-variance route tried in parallel
with the positive arithmetic construction in this packet. It contributes
no new Lean declaration or claimed analytic theorem.

## The specific mechanism attempted

The starting point was the exact ordinary harmonic inverse law, not a
replacement geometric policy. On a hypothetical escaping odd-unit orbit
`q_j`, write `v_j = nu(q_j)`, with `v_j` increasing to `C > 0` and

\[
K(q,x)=\mathbf 1_{Ux=q}\frac{\nu(x)}{\nu(q)}.
\]

PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`,
`research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`,
proves that moving inverse windows are uniformly close in total variation
to windows on this same ordinary orbit, at every inverse depth. The
actual-orbit entropy ceiling therefore transfers to those inverse laws.

The attempted completion was to obtain an opposing entropy estimate from
the many actual same-future siblings, using the canonical harmonic weights.
Along the supplied forward path, however, the exact retracing edge has
probability `v_j/v_(j+1)`. Its discarded sibling probability is

\[
1-\frac{v_j}{v_{j+1}},\qquad
\sum_{j\ge0}\left(1-\frac{v_j}{v_{j+1}}\right)
\le \log\frac C{v_0}<\infty.
\]

The inequality is immediate from `1-t <= -log t` and telescoping finite
products; it is a useful diagnostic of the already constructed flow,
not a new closing theorem. A comparison with a nondegenerate inverse
policy would have to preserve this actual path and its exceptional
ordinary values. Fixed-root limiting laws do not give that comparison.

## Where the arithmetic smoothing attempt stopped

The newest relevant source is PR180 at
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
`research/retained-source-attacks-20261122/SIBLING_MASS.md`.
Its source-qualified modular-routing multiplicity gives a genuine
all-root lower bound for nonnegative finite-cylinder observables.
Applied to one specified depth-`r` Bellman spike, however, its displayed
bound retains the factor `3^(-r-1)`.

I tried to avoid that factor by using the full observable mean. The same
source gives uniformly bounded Haar means for the finite Bellman
obstacles. Thus a spike of height comparable to its ordinary integer
does not, on the available estimates, occupy a comparable fixed fraction
of the residue classes. Replacing its actual value by the Haar mean
loses the information the closing argument needs.

The canonical escape label from the previous PR182 checkpoint supplies
another formulation: it is positive on an escaping component and is
orthogonal, with a positive approximation gap, to the established
polynomial-phase class. No ordinary mean approximation of this particular
label was constructed. The whole-component minimum in its upper bound
cannot be replaced by the growing minimum of a late forward suffix.

## A second route tested: finite descent and shift entropy

I also tried to turn density-one finite descent into regularity of the
ordinary invariant label. The tempting line is that most labels can be
recovered from labels at smaller integers, so the initial prefix has a
short description. That line does not identify the entropy of the
ordinary shift-empirical law: small description size alone does not
control its consecutive-block frequencies. Nor does exact doubling
invariance supply the missing conclusion.

For a concrete check of the latter inference, assign independent fair
bits `xi_m` to positive odd integers and set `b(n)=xi_(oddpart(n))`.
Then `b(2n)=b(n)` exactly. For each fixed length `L`, the odd parts of
`n,...,n+L-1` are pairwise distinct once `n>L`, so each such block has
the uniform `L`-bit distribution. Two block indicators can be dependent
only if their positions share an odd part. Among positions at most `N+L`,
the number of such pairs is `O(N)`: grouping by odd part bounds it by

\[
\sum_{k\ge0}(k+1)^2\frac{N+L}{2^k}=O(N+L).
\]

Consequently the variance of each fixed word frequency is `O_L(1/N)`.
Chebyshev on the square cutoffs, followed by interpolation between them,
proves almost-sure convergence of every word frequency to `2^(-L)`.
There are countably many words. Thus some exactly doubling-invariant
sequences have the fair Bernoulli shift-empirical law. This is a control
for the doubling/shift-entropy inference only; these random sequences
are not asserted to satisfy the odd Collatz equation or canonical
harmonic identities.

The unproved step remains a specifically arithmetic regularity or
sibling-mass estimate for the actual canonical values. Neither this
attempt nor the control replaces that step with an assumption. Periodic
states were excluded from the harmonic domain, so nontrivial cycles
would remain a separate obligation even if this escape route succeeded.
