# Latest-source review and the direct witness target

**Review boundary: the full source heads below, as read on 2026-11-21.**
These are proposed research branches. Review of a stated clause does not
extend to the full theorem, to neighboring statements, or to later heads.
This pass used repository sources and direct algebra; it did not use
external web research or assume any announced major-conjecture proof.

The mathematical dependencies of the new direct witness results are
explicit in the adjacent notes. Only the least-failure height arguments
need the finite reverse-tripling cover, independently reconstructed here.
The other results below were examined as possible closing mechanisms;
their unresolved inputs are not assumed.

## 1. The frozen reverse-tripling reduction

The main reviewed source is PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md` and its accompanying
checker. [REDUCTION_AUDIT.md](REDUCTION_AUDIT.md) records its exact blob
identities, the complete independent 71-cell replay and the strong
induction proving the equivalence with the original 512 assertion.

The source author supplies the reduction. This packet adds the sharper
direct-query height `213597/23` and its consequences for the least
direct-`R` antecedent. That minimum differs from the least adjacent-pair
failure in PR163; constants and rank exclusions for the two minima are
not interchanged.

PR146 subsequently advanced to
`66970775e4bdc945a68308e37a8eb028ebde42d2` during this pass. Its changes
from the earlier pin add
[`FIVE_RETURN_IN_EVERY_CLASS.md`](https://github.com/GettysburgResearch/collatz/blob/66970775e4bdc945a68308e37a8eb028ebde42d2/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md),
its checker and the README entry. The frozen reverse-cover files used
here are unchanged between those two heads.

The new written construction was read in full. It transports any fixed
odd ternary-unit comparison `(q,5q)` into every prescribed arithmetic
progression, preserving both endpoints at one common ordinary clock.
It first returns the two affine arms to ratio five after any prescribed
binary prefix; it then uses legal paired affine blocks and modular
transitivity to prescribe the endpoint. A simultaneous-shift construction
also produces finite blocks of copies of a comparison.

The proof still retains the labels of `q` and `5q` separately. Thus its
global consequence, using PR157's five criterion, is that five-closure
on any entire arithmetic progression would suffice. It does not prove
five-closure on such a progression. Likewise its smaller-comparison
subprogression inside every progression does not contain every supplied
integer. No new complete direct-`R` dispatcher follows merely by composing
this localization with a known local descent.

This later source was inspected algebraically. Its new standalone
author checker was not rerun in this packet, and its separate
quantitative block-count and minimum-chain-cost claims are not used as
inputs to our proofs.

## 2. New physical five blocks and the energy remainder

PR167 at `e83cc8b35ad614c616df7c00318cc9645a174c34` was read at
`research/least-failure-closure-20261121/`, particularly
[`HOMOGENEOUS_FIVE_TRANSPORT.md`](https://github.com/GettysburgResearch/collatz/blob/e83cc8b35ad614c616df7c00318cc9645a174c34/research/least-failure-closure-20261121/HOMOGENEOUS_FIVE_TRANSPORT.md),
`CLOSING_ENERGY_INTERFACES.md` and `LATEST_FIVE_REDUCTION_BOUNDARY.md`.

The positive-integer correction decoder is complete for a specified
architecture: source and target have equal odd count and equal shortcut
clock, and their endpoints have ratio five. Its three minimal
four-input families beginning with valuation one are

\[
\begin{array}{rcll}
(1,1,1,b)&\mapsto&(1,2,5,b-5),&b\ge6,\\
(1,1,2,b)&\mapsto&(1,5,1,b-3),&b\ge4,\\
(1,1,4,b)&\mapsto&(1,3,5,b-3),&b\ge4.
\end{array}
\]

Its source-level correction proof and ordinary legality were inspected.
These are useful infinite families, but source 7 has no positive
same-clock return with endpoint ratio five, even though both 7 and 35
converge. Therefore completeness of that decoder is not completeness of
an arbitrary output-witness constructor. The source explicitly preserves
this distinction.

The energy note also keeps actual multiplicity: a selected lift of `q`
has weight `(q/lift(q))^s`, and pulling its comparison back uses the
reciprocal factor. Their product is exactly one. The new renewable
families give contraction on their stated domains; they do not supply
absolute finiteness of the complementary energy. The sparse least-failure
sieve restricts a possible minimum, not the full failure set.

The arithmetic-return results in the PR's overview retain their cited
external S-unit dependency. That external theorem was not researched or
reproved in this pass. None of those results is imported into the direct
reverse-tripling proofs here.

## 3. Broader return languages and decreasing-parameter templates

PR168 at `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` was examined at
`research/closure-frontier-20261121/`. The symbolic-induction reviewer
read `FIVE_RETURN_LANGUAGE.md`, `NEGATIVE_TEMPLATE_GRAMMAR.md` and the
closing discussion; the root also read the packet overview.

The balanced-return recognizer and its unbounded block language retain
the architecture restriction just described. The negative-template
grammar supplies exact positive ordinary descents in the adjacent
parameter, while a transported source witness may get longer. Such
growth is legitimate under a decreasing integer parameter, but it does
not supply induction on source witness length. The source-zero Mersenne
reference is outside the proved cycle grammar.

The finite-conductor and ternary-stationary results in the overview
identify concrete approximation inputs. No such ordinary approximation
is constructed there, and this pass does not import its external
density, regularity or occupancy dependencies. Neither the reported
renewal coefficient nor an approximation criterion is substituted for
its missing input.

## 4. Further paired descents and a genuine all-time moment

PR169 at `c47e844299ad2e02e15c2f284ae4abe69e6e5d78` was reviewed at
`research/certificate-renewal-20261121/`. The algebra reviewer
independently reconstructed all eight whole affine prefixes behind
`C5_CERTIFIED_BYPASSES.md`, CB1–CB2, including their ordinary guards and
strict child contractions. They move adjacent comparisons on
`k=14 mod32` to smaller odd child indices. These are valid `P`-to-`Q`
transfers; they do not preserve the direct pair `(27m,9m)`, so their
minimality premises are not silently substituted into our direct-`R`
argument.

The same reviewer reconstructed the correction decoding and the eight
prefix families of `FIVE_WORD_EXTENSION.md`, FW1–FW4. Their density is
`23/384` on the specified unit domain; the important initial `(1,3,...)`
language remains outside. FW5's strict inverse-fiber coefficient retains
its separate 184-leaf certificate; that certificate was not independently
rerun here. No finite full-energy conclusion is inferred.

The root and algebra reviewer both read the complete elementary proof in
[`FIXED_ENDPOINT_SUMMABILITY.md`](https://github.com/GettysburgResearch/collatz/blob/c47e844299ad2e02e15c2f284ae4abe69e6e5d78/research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md),
ES1–ES4. Put `n_q=U^q(n)` and `J_q=3^q/2^(A_q)`. For
`V_q=(J_q/n_q)^4`, exact ordinary multiplication gives

\[
V_q-V_{q+1}
=V_q\left[1-\left(\frac{3n_q}{3n_q+1}\right)^4\right].
\]

The bracket is at least `175/(256 n_q)`, so positive telescoping proves

\[
\sum_{q\ge0}\frac{J_q^4}{n_q^5}\le\frac{256}{175n^4}.
\]

This is a valid all-time estimate, including repeated visits on any
hypothetical positive cycle. It removes the low-endpoint part `r_w<=q`
of the PR's different primitive-word moment. The remaining second-power
endpoint moment on `r_w>q` is unbounded by that argument. The subsequent
quantile criteria retain their pinned simple-path occupancy input; they
also require a separate exclusion of nontrivial cycles for full
convergence. Here “nonperiodic” must mean not eventually periodic when
no-repetition reasoning is used.

Its subsequent head `6cb9bfdc828f91576066b0e4a099d47d8144e915` was also
checked. The only changes are the concurrent-source comparison and two
report indexes; its mathematical files are unchanged. The root read the
complete comparison. It identifies exact overlap between the three
five-return catalogs and realizes two restricted cells of PR168's
separate source-zero grammar. It does not give a complete selector.

## 5. What this review changes in the current attempt

The full reverse-tripling criterion is a cleaner target than separately
solving `P` and `Q`. The current packet proves transfers that preserve
this direct target and makes their well-founded quantity explicit.
The new all-index ladder decreases both the parameter and the source
witness length; its guards are still a restricted family. The supplied
source witness is used constructively throughout.

The latest source results do not eliminate the remaining words in
[LEAST_R_FAILURE.md](LEAST_R_FAILURE.md). In particular the rank-two
first-letter-5 and first-letter-6 Mersenne families were subjected to
separate bounded whole-affine searches with exact guards; neither search
returned a certificate on its entire searched family. A later constructive
use of the source-zero matching equations did yield the restricted
direct-R contraction in [SOURCE_ZERO_DESCENT.md](SOURCE_ZERO_DESCENT.md).
It deliberately permits a longer child witness while decreasing the
ordinary integer. Its exact ternary refinement covers one class in each
of the first-letter-5 and first-letter-6 rank-two families, not either
full family. The
[execution record](../../reports/2026-11-21-witness-global-closure/README.md)
states the budgets and outcomes. Search exhaustion is not nonexistence
of an unbounded or differently structured transformation.

Thus the exact outstanding target is still: from any complete witness
for `27m`, construct one for `9m`, with every recursive call justified
by one common well-founded rule. The results here prove specified
families of that statement and retain the unbounded output allowance.
They do not prove the universal assertion.
