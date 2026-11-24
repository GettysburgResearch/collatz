# Coordinator review of round eight

**Collatz remains OPEN.** This review records the mathematical reconstruction,
cross-review corrections, and executed evidence behind the
[round-eight overview](../../../research/astra-global-closure-20261124/round8/README.md).
The baseline is 0e8a7f9f965416189b30b57b8aa818fbcb7757c7. Three GPT-6.2
Astra streams worked on disjoint unit, arithmetic, and paired lanes. Their
independent reviews are retained alongside the proofs. This is a review of
the load-bearing claims used here, not certification of every statement in
the 162-PR metadata inventory.

## Ordinary descent: existence, legality, and coverage

I checked the construction of a legal inverse prefix with p odd inverses
and raw length A at most 4p. At each odd inverse, one of the exponents 1
through 4 chooses an integral positive unit predecessor modulo nine. The
prefix lifts a target increment of \(3^pL\) to \(2^AL\). A final choice of
one residue modulo \(3^r\), \(r=5p+13\), makes the last ancestor plus one
divisible by \(3^r\). Its all-odd predecessor
\[
             z=2^r(Y+1)/3^r-1
\]
is an actual positive integer. The inequality \(171z<Q\) follows from
\(171\,2^{13}<3^{13}\) and \(512^p\le729^p\). The proof includes every
nonnegative lift on the selected progression; it is not just a single
modular solution. RayGrade.every_cell formalizes this existence statement.

For forward failure at u, the bad target is \(T(3u)=(9u+1)/2<5u\);
reverse failure uses the bad target u itself. The previously proved
direction-preserving paths convert the small bad ancestor to a unit
failure below \(u/5\) or \(u/8\), respectively. These implications apply
on the chosen subprogression. The intersection and CRT arguments retain
both directions and any given odd binary residue. None asserts that every
original unit lies in a contracting subprogression.

I also checked the all-clock grade bound. The physical carry inequalities
and an integral ceiling argument apply for unrestricted meeting clock h.
For \(q>1\) with \(q+1\) divisible by \(2^i\), a smaller positive source z meeting
\(T^iq\) must have \(h>i\) and odd count
\(P_h(z)>i+v_3(q-1)\). The Mersenne construction pays the growing grade
cost on explicit exponent progressions. It is a conditional implication
from a failure on those progressions to a smaller failure.

The Applegate–Lagarias improvement uses the published iterative inverse
certificate with odd fraction \(14/29\) and bounded odd increment 29.
Stopping its concatenation after passing depth p gives
\(p\le b\le p+28\), raw clock at most \(29b/14\), and sufficient final
precision at most \(p+\lceil5p/6\rceil+65\), for \(p\ge1\).
I checked the certificate definition and the iteration argument in the
primary paper. Its 350,688,758-entry certificate was not regenerated.
The elementary \(6p+13\) precision and its Lean proof are independent
of this external computation. [Unit proof](../../../research/astra-global-closure-20261124/round8/unit/README.md)

## Arithmetic: preserving the complete outside-prime divisor

The new written argument treats a fixed positive ordinary source n and
actual prefixes \(x_k=T^kn\), with odd count \(p_k\). A distinct positive
lift \(n+2^kt_k\), \(t_k>0\) eventually, reaches
\(x_k+3^{p_k}t_k\) after the same prefix. A physical suffix with raw
length \(\ell\), odd count h, carry C, and final value r gives
\[
             2^\ell r-3^h x_k-C=3^{p_k+h}t_k.
\]
The general theorem needs a bounded signed presentation of C with
coefficients of logarithmic height \(o(k)\), nonnegative powers of two
and three, and ternary exponents at most \(h+o(k)\).
It also needs \(x_kr/3^{p_k}\le e^{-\delta k}\).
The last condition is automatic for \(r=1\), since the elementary physical
height estimate gives \(x_k/3^{p_k}\le n(2/3)^k\).

After clearing the coefficient denominators, delete zero subsums on the
right-hand side only. The remaining terms, together with the nonzero
displacement term on the left, form a nondegenerate zero sum. Any proper
zero subsum containing the displacement would have a zero complementary
subsum on the right. Divide by the full common content, rather than a
squarefree surrogate.

Let H be the maximum absolute primitive coordinate and P the product of
their parts outside a fixed finite prime set S containing two and three.
A surviving right-hand coordinate supplies the ternary pivot. The
finite divisibility statement in SparseTerminal.pivot_divisibility is
\[
                   3^{p_k+h}P\mid 3^v V R,
\]
with the exact primitive displacement V and the full product R of the
right-hand coefficient magnitudes. It retains all prime multiplicities.
The bound on v and the coefficient height yield
\[
                       P/H\le e^{-\delta k/2}
\]
eventually. This remains valid if pruning removed one or both clock
coordinates. A two-coordinate primitive zero sum instead has \(P/H=1\),
so cannot occur at these late depths.

I inspected the printed Corollary 1 of Evertse's 1984 paper, including
collective gcd one, all proper nonempty subsums, and the complete
outside-S product. It gives \(P\ge c_\epsilon H^{1-\epsilon}\)
for every fixed \(\epsilon>0\). Combined with the last display this
forces \(\log H/k\to\infty\). The product upper bound
\(P\le (t_k)_{S'}x_kr\exp(o(k))\), followed by the case
\(\epsilon=1/2\), then gives
\[
                       \log(t_k)_{S'}/k\to\infty.
\]
No separate Subspace Theorem argument is needed in the final proof.
The published analytic theorem and this asymptotic deduction are written
mathematics; Lean checks the finite physical and divisor identities.

For a power of one physical word, the carry is the difference of two
pure powers times a rational coefficient whose height is exponential in
the root length. Concatenating a bounded number of powers therefore
meets the hypotheses when the sum of root lengths is \(o(k)\), even
when the total suffix duration and odd count are unbounded.
The explicit two-run first-hit construction shows the language is
nonempty at every positive source and depth. Its displacement pays the
large outside-prime cost. It does not give a small witness for an
unresolved n. PR192's earlier bounded-odd full-displacement theorem and
moving-target extension are credited in the final manuscript.
[Arithmetic proof](../../../research/astra-global-closure-20261124/round8/arithmetic/README.md) ·
[Unit review](unit/ARITHMETIC_REVIEW.md) · [Paired review](paired/ARITHMETIC_REVIEW.md)

## Paired families and the analytic assumptions

I checked the two clock regimes separately. The unconditional native
profile bound uses the shared real input coordinate to count pairs of
endpoints. It does not multiply two independent one-arm probabilities.
The square-root carry moment is bounded by its affine recursion; the
dyadic counting and trimming then retain the advertised partners.
Cross-review corrected the trimming exponent to \(3w+8\), before the
source and control freeze.

The stronger landing families retain H as a named input. Each selected
record includes both actual endpoints, clocks, odd counts, and the
ternary source residue. Trimming the first and last members within each
record at every dyadic interval scale costs a summable polynomial
budget. The partners belong to the original eligible record class;
they are not asserted to survive every subsequent trimming operation.
Thus this is not a recursively closed descent set.

Under F, PR203's fixed-target depth bank supplies positive lower density
for each fixed ordinary component. The use of multiple odd depths
depends on choosing a nonperiodic target, so that the corresponding
source sets are disjoint. A single-word predecessor count alone would
not justify the stronger density conclusion.

I read the late PR201 directed covers and their semantic checker, then
replayed both certificate tables. The query maps are positive affine
maps on whole progressions, each individually injective. Their finite
number and comparable height bounds transfer odd-cut reciprocal
divergence to either orientation in either chosen residue modulo six.
Removing landing or native-profile exceptions of summable reciprocal
mass preserves the divergence.

For every cut separating two specified distinct actual components,
the tail capacity is infinite. Compactness of the binary cut space
gives a common finite upper cutoff at which every separating cut has
capacity greater than any prescribed M. Finite max-flow/min-cut then
gives the stated finite flow. The actual component relation defining
this graph is an existential object, and the flow may use intermediate
components. There is no contradictory upper bound in the packet.
[Paired proof](../../../research/astra-global-closure-20261124/round8/paired/README.md) ·
[Native profiles](../../../research/astra-global-closure-20261124/round8/paired/PAIRED_PREFIX.md) ·
[Directed upgrade](../../../research/astra-global-closure-20261124/round8/paired/LATE_PR201.md)

## The two routes meet at a fixed positive prefix

Under F, the paired compression and subsequent fixed-target floor give
exponentially many positive m of height \(2^{Dk}\) with both prescribed
k-bit histories of n and 3n. Their arms merge by \(40(k+1)\), and both
reach one within \(O(k)\) steps. I checked the level-decreasing binary
cost, the logarithmic additive-gap absorption, and the additional
precision budget in F. The large absolute constant D absorbs all
these linear costs.

On these witnesses the lift displacement is at most exponential in k.
The arithmetic theorem therefore forbids \(o(k)\) total root length
for any fixed number of repeated blocks. A subsequence contradiction
gives a uniform positive linear lower bound, for each fixed source and
block budget. The constant is ineffective through Evertse. These m
are different ordinary integers; matching every individual finite
prefix by other convergent integers does not prove convergence of n.
[Cross-route proof](../../../research/astra-global-closure-20261124/round8/paired/CROSS_ROUTE.md)

## Why the latest reductions do not close the conjecture

The least directed failure forces every vertex on its bad arm to stay
above a constant multiple of that least failure. Multiplying the actual
step ratios gives odd fraction at least
\(\log_3 2-O(1/h+1/u)\), rather than the near-half count in the typical
profile estimates. The finite rotation argument also retains
\(\binom hp/[h(1+h/2)]\) exact profiles at the critical grade.
This obstructs an unsupported extrapolation from typical profiles; it
does not construct an infinite nonconvergent trajectory.

The late PR193 review makes the obstruction explicit at every first
checkpoint of its repeated descent. The same review gives pointwise
same-direction contractions at two sparse ternary centers, but the
new smaller failure can leave those sparse sets.
[Critical profiles](../../../research/astra-global-closure-20261124/round8/unit/CRITICAL_PROFILES.md) ·
[PR193 review](unit/LATE_PR193_REVIEW.md)

The late PR201 exact-clock row criterion retains both escape and cycles,
with an unproved upper bound on its maximal row count. Its amplified
sources satisfy \(9(x-n)=2^tz-(9n+3+2^f)\). For fixed positive n and
large t, the two elementary valuation cases give
\[
                    v_2(x-n)\le\lfloor\log_2(18n+6)\rfloor.
\]
That particular exponential family therefore cannot supply witnesses
with increasingly many common parity bits at n. Other row sources
are not bounded by this argument. [PR201 review](arithmetic/LATE_PR201_REVIEW.md)

## Executed evidence and final review

The root runner rebuilt all three new Lean sources into an empty
project output cache, using Lean 4.34.1, Mathlib
d13f23b723b8a846827a245b89c10fc7d3f11612, and warnings as errors.
All 31 selected axiom reports contain only propext, Classical.choice,
and Quot.sound. Existing Mathlib and package objects were reused.
The source bytes were unchanged during the build.

Four finite scripts ran in both ordinary and optimized Python, for
eight canonical-output matches. Independently, the pinned upstream
directed covers passed in both modes on 2,211 leaves and 84,642
letters. This upstream replay is scoped to the four pinned files.
[Lean receipt](lean/receipt.json) · [Finite replay](CONTROL_REPLAY.json) ·
[Upstream cover replay](UPSTREAM_COVERS.json)

All three agents also reviewed the coordinator's final overview.
Their review restored explicit subprogression eligibility, sufficient
rather than necessary precision, the signed-carry ternary exponent
bound, and the nontrivial-cut antecedent. These editorial corrections
leave the frozen lane proofs unchanged.

The source ledger and manifest record exact source identities.
The final publication step additionally runs the repository's complete
clean-checkout validator. These checks certify the stated local
execution and repository integrity. They do not establish an unproved
analytic input or the remaining universal ordinary-source implication.
