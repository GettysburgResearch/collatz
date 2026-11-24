# Principal review and verification scope

Date: 2026-11-23. Verdict: **verified at the stated boundaries; full closure open**.

The principal researcher reconstructed the mathematics below and ran the
fresh compiler and exact controls recorded in this directory. This is an
internal research review, not an assertion of external peer review. The
principal researcher supplied the ordinary reference/loss decomposition in
the pressure note, so that part is a contribution rather than an independent
review. The separate cycle researcher independently reconstructed it in
`CYCLE_AGENT_PRESSURE_REVIEW.md`.

## Common ordinary maximum

The explicit assumptions are positivity on a nonempty set of positive
ordinary integers, the bound `n*r(n)<=1`, and the physical pressure balance.
Choosing a positive weight `r(p)` leaves only finitely many possible
competitors with `n<1/r(p)+1`; the formal proof actually attains a maximum
there. It does not assume attainment or select different roots for the two
directions.

`GapPath` includes all intermediate positive odd unit guards, positive gaps,
and the equation `3n+1=2^a q`. Oddness of `q` forces the exponent to be the
exact ordinary valuation. Telescoping produces `2^A r(n)=3^h r(q)` for the
entire supplied path. Comparison with the same maximum gives the two strict
opposite inequalities; parity excludes equality of the positive powers.
The all-path quantifiers in `common_root_two_sided` have no length or
exponent cap. They are still conditional on the explicit weight hypotheses.

For the written escaping-component application, I independently reconstructed
PR177's elementary cylinder split: the low-total lane uses one residue modulo
`2^(A+1)` and the generating-function bound, while the high-total lane uses
injectivity of the actual odd orbit and the affine endpoint bound. Its
`4X^(39/40)` estimate yields `sum 1/n<=160` by the displayed integral, hence
a positive correction product. Starting the same integral at the component
minimum gives `160*m_0^(-1/40)` and the stated upper bound for the selected
root. This is written mathematics; the new Lean module does not construct
that infinite product.

The local residue calculation correctly retains `23 mod36`. At a root
congruent to five modulo nine, the gap-one inverse value is divisible by
three and is outside the declared unit component. The finite known basin
graph is disjoint from any escaping component; its supported tests therefore
cannot create a pressure relation between components.

## Complete numerical cancellation

I checked the chronological convention against the imported, unchanged
`CycleWordAlgebra.lean`. Moving one letter across `h` zeroes leaves exactly
the prefix factor `2^|u|`, suffix factor `3^|v|_1`, and displacement `2^h-1`.
For a positive complete denominator, the two/three coprimalities remove
the entire unit factor from the gcd. The zero-residue premise is explicit.

Two scope fixes were made before the final frozen note: `p>=1` is stated
globally, and loss of integrality after an adjacent swap is qualified when
`D=1`. The final six formal statements use the correct hypotheses.

For the written counting deductions, I reconstructed the shorter cyclic arc
argument, including wraparound through `2^A=3^p modD`. Under the stated
separation threshold the normalized cut units cannot coincide up to sign.
With `A>=5`, an origin outside the four affected positions makes two
putative colliding exchanges internal, proving disjoint closed neighborhoods.
For the window injection, carry differences factor through a two/three unit;
the carry bound and first-bit parity reconstruction recover the window.
Neither argument supplies the much stronger `N_0<A` conclusion.

The balanced-unit normalization was checked in the full quotient. Its
coefficient permutation is retained, and its signed differences are not
treated as a bounded-complexity family. I opened the Grieve--Wang Theorem 1.2
and Corvaja--Zannier Theorem 1 in their primary preprints. Their fixed
dimension/degree, height and exceptional-locus obligations do not disappear
under the proposed encodings. These theorems are not used as unproved
Collatz premises. The full numerical denominator transport does not prove
that the polynomial residual denominator cannot cancel at three.

## Original-source pressure accounting

The contribution `sigma_s P_s=sigma_s-d_s` follows by grouping actual
ordinary children under their unique odd image. Iteration gives atom density
`Lambda_k(n)^s`; decreasing convergence retains, rather than removes, the
escaping-component residual. The pole-height estimate, countable weighted
sum, exact unit-Haar shell sum, and periodic-root geometric return factor
were checked directly. The pressure and source agents' independent reviews
record the corresponding boundaries.

The new exact replay transports a finite source function through actual odd
orbits. It groups endpoint collisions, retains repeated periodic visits, and
checks the loss telescope against an independently accumulated product on
each original source. Deliberately dropping repeated visits breaks the
identity. It does not infer that the infinite residual is zero.

## Actual executions

`LEAN_RECEIPT.json` records four successful commands: a fresh build of the
unchanged carry dependency, the two new modules, and the complete eighteen
declaration axiom audit. Only the standard Lean axioms `propext`,
`Classical.choice`, and `Quot.sound` appear. The source hashes are checked
before and after the replay.

`EXACT_RECEIPT.json` records normal and optimized runs of both exact Python
programs. These controls test the mathematical implementation and quantifier
boundaries; they are not a universal Collatz check. Repository-integrity
receipts are reported separately and are not evidence of the mathematical
closing steps.
