# Independent reconstruction: analytic gluing and actual boundary support

Reviewer: `global_source_synthesis`, a different in-session researcher from
the note's author. This is a scoped internal reconstruction, not external
peer review and not an acceptance upgrade for the upstream existence or
recent-manuscript inputs.

Reviewed file: `ANALYTIC_GLUING.md`.

Exact SHA256:
`99f7c7249141006d94a18af8db13a546ebea7081c980360c78bcfff189e4be85`.

**Verdict: VERIFIED in the stated written, source-qualified scope for
Sections 2--6.** No additional correction was required at this hash.
The claims retain assumptions (2)--(5), the specified ordinary trace
inputs for (26), and Paper37v4's count for Section6. I independently
reconstructed the new implications; I did not reprove the upstream
harmonic-reference construction, the path-packing theorem, or Paper37's
deep count. No infinite conclusion is asserted to have been kernel checked.

## Reconstruction of the component coordinate and support

1. The common-future construction of `chi` is consistent. Continuing two
   meeting paths past their common endpoint multiplies both by the same
   factor. Each forward edge adds one ternary exponent and subtracts the
   actual binary gap, giving `chi(n)=2^d 3^ell` at the normalized clock.
   The edge identity gives `y(Un)-y(n)=1/(3chi(n))` and
   `lambda(n)=y(n)/y(Un)` without a completion or a changed parity word.

2. The inherited uniform reciprocal bound gives a strictly positive lower
   bound for every path product. Thus each forward `y` orbit has a finite
   limit, common on the coalescing component. Its infimum is positive.
   Every legal unit parent strictly lowers `y`, so the infimum is not
   attained. Equality of two `y` coordinates would make the ratio of two
   positive integers coprime to six a power of two times a power of three;
   the two integers must be equal.

3. For the support equality, only finitely many parent cones of a fixed
   `q` contain any integer at most `M`. A low integer has a deterministic
   forward route to `q` and one last parent on that route; `q` itself is
   not in a parent cone because it is nonperiodic. One can therefore choose
   a large legal unit parent with its whole inverse cone above `M`.
   The reciprocal tail estimate bounds its boundary loss uniformly, while
   its actual path event has positive mass `nu(p)/c_E`. This proves that
   each `y(q)` is in the canonical boundary support. The reverse inclusion
   follows by taking the backward limit on each actual path. The parent
   approximation also proves perfectness. Nondegeneracy, strict interior
   mean and positive variance follow from this exact support, not from a
   heuristic branching assertion.

## Reconstruction of the fibre identification

4. The inherited inverse product for `h(q)/nu(q)` excludes the root and
   includes each inverse parent. Its product through endpoint `x` is
   `y(x)/y(q)`. Thus the infinite product is `Z/y(q)` and the conditional
   mean is exactly `s(q)=y(q)h(q)/nu(q)`.

5. On a finite inverse path, the likelihood of `K_h` relative to `K` is
   `s(x)/s(q)`. Here `s(x)` is the conditional expectation of the same
   random boundary variable `Z` given that prefix. Bounded martingale
   convergence gives the terminal density `Z/s(q)`. This justifies the
   change of measure on the actual path space, including its orientation.

6. The events that a whole path passes through successive `q_k` increase
   to an event of full mass because `nu(q_k)/c_E` tends to one. Conditional
   path laws therefore converge in total variation. The real rescaling
   varies with `y(q_k)`, so only weak convergence of the rescaled real
   pushforwards follows; the note correctly states that distinction.
   Under the `Z/s_E` tilt, the moment in (25) is `b_E/s_E`, and the mean
   intercept is `1-E(Z^2)/(b_E s_E)`. The displayed variance difference
   and recovery of `F_E` are exact.

7. I read PR178's `CANONICAL_TIME_ENTROPY_ATTEMPT.md` at
   `7e4569476e152f6b8537bdc1711df595ec1ffd89`, including its normalization
   `F=h_tr` and its comparison with `G`. The note does not silently set
   `h_tr=G`. The quotient `w=(h_tr/n)/h` is harmonic for `K_h`, with
   bounds `eta<=w<=2`. Its backward terminal martingale `W` gives the
   additional tilt. Conditional expectation under the global `Z/s_E`
   law recovers the finite trace kernels at every clock. Consequently
   (26) retains `ZW/E(ZW)`, and the Radon--Nikodym bounds for the two
   real pushforwards follow by conditioning `W` on `Z`. Formula (25)
   is correctly restricted to the `G` law.

## Reconstruction of coherent deformation and its ordinary domain

8. `x_t(n)=n+tchi(n)` preserves every displayed affine edge. Whole-component
   positivity is equivalent to `t>=-a_E`; equality is allowed because the
   infimum of the ordinary `y` values is not attained. The product and
   conditional expectation give (31) directly. The sole zero `-s_E` is
   strictly outside this positivity range. At the positive endpoint the
   boundary stays positive because `a_E<s_E<b_E`.

9. Equation (33) has the correct direction: `c_E KL(Pi_E || Pi_E,t)` is
   `c_E[log(s_E+t)-E log(Z+t)]`. Strict Jensen inequalities give both
   positivity and the negative derivative. The expansion at positive
   infinity has leading coefficient `c_E Var(Z)/(2t^2)`.

10. Integrality at the reference vertex first forces integer `t`. At
    forward clock `k`, the exact multiplier is `3^k/2^A_k`, so
    integrality forces `2^A_k | t`. Since `A_k>=k`, an entire integer
    shadow requires `t=0`. For a finite prefix the coarsest divisibility
    condition suffices for every earlier vertex. Requiring all vertices
    to remain odd gives one additional factor of two. No nearby ordinary
    parameters have been obtained from the real deformation.

## Reconstruction of the routing support and source cost

11. I checked the use of Paper37v4 against PR180's pinned
    `research/retained-source-attacks-20261122/SIBLING_MASS.md` at
    `5e29f56f6d44669a8aa9134e5617b78d65c074c2`, (S2)--(S5). With one
    prescribed unit endpoint class, the count is at least the integer
    `R_b` in (36). The common odd length and total valuation give the
    exact same multiplier `X=(4/3)^b` on every chosen block. Ordinary
    legality is an explicit upstream consumer, not an assumption that
    a residue prescription realizes an arbitrary infinite source.

12. At depth `j`, all endpoints have denominator scale
    `X^j chi(q)` in their `y` coordinates. Distinct words give distinct
    ordinary endpoints by deterministic forward recovery. Therefore
    their coordinates have separation at least `1/(X^j chi(q))`.
    The remaining offsets sum to at most
    `C_F/(X^j chi(q))`. An interval can meet at most its length divided
    by this spacing, plus `C_F+2`, of the depth-`j` image intervals.
    This bounds the pushforward mass even if different infinite paths
    have the same boundary. No boundary-map injectivity was used.

13. Taking the grid scale comparable to the interval length gives (39)
    with exponent `log R_b/log X`. The elementary interval-cover argument
    then supplies a Hausdorff-dimension lower bound. Each infinite path
    is an actual inverse path in `E`, so its real limit lies in the
    already identified support. The exponents tend to one, giving (40).
    This is dimension of the **support**, not dimension of the canonical
    measure or its ternary time ensemble.

14. The canonical probability of a selected finite word is exactly
    `nu(n)/nu(q)`. Using `nu(n)>=gamma/n` and `n<=X^j q` gives the lower
    bound in the note. Against the uniform selected-word law this yields
    the KL upper bound
    `log(q nu(q)/gamma)+j log(X/R_b)` with the displayed orientation.
    Summing the same individual lower bounds gives (42). This lower
    bound tends to zero; it is correctly not described as an upper bound
    or a proof of zero mass for the infinite selected tree. A small
    relative-entropy rate alone does not erase this mass issue. At a
    moving root the original-root term remains `log q_N+O(1)`.

The route to a contradiction is therefore still missing precisely the
canonical-measure comparison stated in the note. The new support result,
bounded trace tilts, coherent deformation and ordinary-lattice exclusion
do not settle that comparison or the Collatz conjecture.
