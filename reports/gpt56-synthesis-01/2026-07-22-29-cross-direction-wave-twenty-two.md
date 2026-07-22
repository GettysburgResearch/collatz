# Cross-direction lemma forge -- wave twenty-two

Date: 2026-07-22
Agent: `gpt56-synthesis-01`
Issue: #29
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Status: four source-qualified or internally exact results; no counterexample claimed

## Live reconciliation

This wave began by fetching and reading the live heads rather than treating
the previous packet as a closed world.

- PR #38, head `5ad965771869a647102e22115ed56749dbe2e254`, supplied the
  global counterexample map and atoms `ACL-N016`, `ACL-N017`, `ACL-N024`, and
  `ACL-N070`.
- PR #33 remained at `c9d62bce3e93f5785f72e4520bc576863d9379eb` and was used
  only through the source-qualified reconstruction already frozen in
  `T-9828`.
- PR #19 advanced to `f764bdc2a2620f3a898ce46ab5ac80c27fe64439`; its renewal
  identities were compared with local `L-9889`, `L-9890`, `L-9894`, and
  `L-9897`.
- PR #16 was read at `87478352`, PR #35 at `52d320b6`, and their completion
  claims were kept in separate ordinary and reciprocal orientations.
- PR #20 advanced to `82ca2f932438a9fe0897704ba62959ca23ec830f`. Its delayed
  phasewise construction `L-9418` and period-ten ceiling `R-9410` motivated
  an independent delayed combined-moment audit.
- Issue/branch #39 supplied the first ordinary-spine handoff prompt but had no
  new committed theorem to import.

## Result 1 -- maximal fixed-width Evertse closure

[`T-9831`](../../research/cross-direction-lemmas/claims/T-9831-maximal-fixed-width-almost-s-unit-exclusion.md)
resolves `ACL-N016` at the correct level of generality.

The exact invariant is measured after primitive normalization. For a finite
catalogue of stage types, bounded essential coordinate count and one finite
union of internal prime alphabets reduce every nondegenerate integer zero sum
to Evertse's fixed-dimension setting. If the primitive moving-endpoint product
has exponent

\[
 \Xi<1
\]

relative to primitive height, only finitely many projective points exist.

The raw endpoint exponent `Theta` and gcd exponent `gamma` give the convenient
sufficient gate

\[
 \Theta<d(1-\gamma),
 \qquad d<1,
\]

but this is only a marginal certificate. It is not a necessary replacement
for the joint primitive invariant. The theorem also records the exact
minimal-block, varying-dimension, exponent-one, degeneracy, repeated-point,
and varying-prime-alphabet boundaries.

PR #33 is recovered as the specialization

\[
 N=258,
 \quad S=\{2,3\},
 \quad g\mid216,
 \quad
 \Theta\le{6498\over346819}<{1\over50}.
\]

## Result 2 -- H renewal transfer and its exact escape

[`L-9903`](../../research/cross-direction-lemmas/claims/L-9903-h-renewal-evertse-transfer.md)
performs the previously missing H-to-Evertse conversion.

Every interior renewal gives the primitive nondegenerate zero sum

\[
 (-8^R4^bY,\;9^R3^aX,\;9^R,\;-8^R),
\]

of exact height `H=8^R4^bY` and outside-`{2,3}` product `XY`. Every full bridge
gives

\[
 (4^L8^SV,\;-4^L,\;-3^L9^RU,\;3^L),
\]

of exact height `J=4^L8^SV` and outside product `UV`.

Dimension, support, primitive normalization, nondegeneracy, height divergence,
and projective distinctness all pass. Therefore a nonperiodic survivor must
satisfy

\[
 {XY\over H^d}\to\infty,
 \qquad
 {UV\over J^d}\to\infty
 \qquad(0<d<1).
\]

The sole missing Evertse hypothesis for these canonical tuples is the endpoint
height gate. Exact factorization reduces it to one proportional deficit:

\[
 {XY\over H}
 ={U\over3^a4^b}\left(1-{1\over8^RU}\right),
\]

\[
 {UV\over J}
 ={W\over9^R8^S}\left(1+{1\over4^LW}\right).
\]

The bounded-letter branch fails this gate linearly, and exact local star and
bridge families show that the already available scalar subcritical budgets do
not imply the missing deficit. Those families are deliberately not presented
as globally compatible H chains.

## Result 3 -- oriented completion criticality

[`T-9832`](../../research/cross-direction-lemmas/claims/T-9832-oriented-completion-criticality.md)
resolves `ACL-N070` without conflating its two directions.

For arbitrary coprime `2<=M<N`, the binary completion is injective even when
`M` is composite: first disagreement at `J` gives `M^J` times a quotient
coprime to the whole base. A selected pure-period word of length `d` has

\[
 Y_w={CW_w\over N^d-M^d},
\]

and exact rational height yields total approximation slope

\[
 \log_MN=1+\kappa^{-1}.
\]

Equal factors, same-symbol returns, and maximal physical runs use the
`M`-deep orientation and the sharp location slope

\[
 \kappa={\log M\over\log(N/M)}.
\]

Reciprocal phase zero carries use the opposite `N`-deep orientation:

\[
 N^{b+r}\mid z,
 \quad
 |z|\le\theta N^bM^{r+t}+H
\]

forces

\[
 r<\kappa t
 \quad\text{or}\quad
 H>(1-\theta)N^{b+r}.
\]

Both slopes are sharp. The theorem does not identify the two numerators, does
not bound one maximal run from its predecessor without quotient/root height,
and does not identify nonperiodic real and completion limits.

## Result 4 -- delayed combined-moment shift rigidity

[`T-9833`](../../research/cross-direction-lemmas/claims/T-9833-delayed-combined-pade-shift-rigidity.md)
tests the live delayed-window idea directly on the combined moment system.

For order `n` and cancellation window beginning at `M>=n+1`, the exact Cramer
endpoint differences are

\[
 \alpha_k=k\{\zeta+9Sr(M-1)\},
\]

\[
 \beta_k=k\{\zeta+9S(r-1)+9Sr(M+n-k-1)\}.
\]

The first evaluated error has `T`-exponent

\[
 V=\zeta(M+n)
 +{9Sr\over2}\{M^2+(2n-1)M-2n\}.
\]

After ordinary Vandermonde removal, the shifted base Schur core still has
degree

\[
 d_{n,M}
 =d_n+9S(r-1)n(M-n).
\]

The evaluated raw pair is integral after one explicit clearing, its gcd is
prime to six, and

\[
 \log_2N_{n,M}^{\rm raw}
 =(d_{n,M}+L_{n,M})\log_2 81+O_r(n^2).
\]

For every delay sequence and every `r>=2`, splitting at the scale
`M asymp n^(3/2)` gives

\[
 \limsup{V\over d+L}\le1,
\]

so the unreduced approximation exponent remains at most

\[
 \log_{81}(64)=0.9549982179\ldots<1.
\]

At every linear delay, period ten still requires the same almost-total cubic
gcd at primes at least five as `T-9830`. Delay is closed as a standalone
height mechanism; the specialization gcd is not bounded.

## Independent cold review

The authoring lanes did not review their own final claims.

- The completion-master lane reconstructed `T-9831` and `L-9903` from their
  integer equations. It required the marginal-certificate qualification,
  fixed-bin minimal-block extraction, explicit divergent heights, and a narrow
  interpretation of the phrase "sole obstruction".
- The H/Evertse lane reconstructed `T-9832`. It corrected the all-zero
  periodic inequality from `<` to `<=`, required the composite-base unit
  definition, checked overlapping factors and the exact floor, and verified
  the reciprocal equality threshold.
- The fixed-width lane reconstructed `T-9833`. It independently derived every
  shifted determinant formula, found the essential restrictions `r>=2` and
  `M>=n+1`, and verified the arbitrary-delay `n^(3/2)` dichotomy.

All requested corrections are incorporated in the claim files.

## Exact validation

An independent symbolic audit checked:

1. every Cramer exponent difference and the closed formula for
   `d_(n,M)+L_(n,M)-V_(n,M)`;
2. both infinite affine H local families over twenty exact samples; and
3. the arbitrary odd-`R` adjacent-run counterfamily in the `2->3` chart; and
4. same-symbol returns, completed maximal runs, zipper signs, and copied-factor
   difference chains on 120 finite admissible ordinary chains across several
   coprime composite and prime bases.

The audit returned `PASS`. Markdown whitespace and claim-ledger consistency
were then checked across the packet.

## Remaining high-leverage targets

1. Prove a fixed proportional H endpoint deficit from global successive-core
   compatibility, or show exactly why the full chain forces the exponent-one
   boundary.
2. Bound the prime-to-six shifted Schur-core gcd, preferably through a modular
   resultant or primitive-prime theorem uniform in the delay.
3. Feed `T-9831` into any architecture that can prove bounded essential width
   and an exact primitive endpoint budget; do not substitute raw stage count
   for essential coordinate count.
4. Apply the sharpened reciprocal wedge in PR #16 at the deepest physical
   zero-carry blocks, retaining the starting-depth term rather than the old
   coarser bound.

## Boundary

No result in this wave constructs a nontrivial infinite Collatz orbit or
proves the Collatz conjecture. `T-9831` and `L-9903` are source-qualified;
`T-9832` separates real and completion values; `T-9833` is an ungcded-height
no-go whose outside-prime gcd remains open.
