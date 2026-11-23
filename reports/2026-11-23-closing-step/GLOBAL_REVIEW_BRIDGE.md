# Review of the conditional cycle-resolvent bridge

Date: 2026-11-23. Reviewer: `global_construction`.

**Verdict: VERIFIED at the stated source-qualified written-proof scope.
No changes requested.** The new implication is a bounded scalar
Blaschke product and cancellation of the simple finite-rank poles
strictly inside the critical circle. It neither establishes the input
(P) nor extends any function across that circle.

## Exact artifacts and reviewer scope

| Artifact | SHA256 |
|---|---|
| `research/closing-step-20261123/CYCLE_RESOLVENT_BRIDGE.md` | `a6161661ad69c730fd90c72f0ad91b3dacad9977b9818f19d4ac9beb54a64173` |
| `research/closing-step-20261123/POSITIVE_CYCLE.md` | `7157db774bc3c944c4cc3259f0742fd74f5bc294ba2f09d0cfe894135e8e80ee` |
| `research/closing-step-20261123/GLOBAL_CONSTRUCTION.md` | `6293818c1de954c12ed04031680d43a807ff9544f083a29ba4568518f260c0b5` |

I reconstructed the grouped factors and compact-convergence estimate
before reading the bridge draft. I am the author of the frozen global
operator dependency; that dependency has its separate review by the
cycle author in `CYCLE_REVIEW_GLOBAL.md`. This report checks the new
bridge's normalization, multiplicities, convergence, cancellation,
and conditional scope. It does not present the operator dependency as
an independently authored result or freshly audit the inherited (P).

## 1. Full cycle root set and summability

For a primitive shortcut cycle with period `A_C` and odd count `p_C`,
the exact operator poles satisfy `z^A_C=3^p_C`. Under `w=z/2`, their
equation is `w^A_C=a_C`, where

\[
 a_C=3^{p_C}/2^{A_C}=e^{-\delta_C},\qquad
 \delta_C=A_C\log2-p_C\log3>0.
\]

The root radius is therefore `exp(-delta_C/A_C)`, rather than
`exp(-delta_C)`. Retaining all `A_C` roots gives precisely

\[
 \sum_C A_C(1-e^{-\delta_C/A_C})
       \le\sum_C\delta_C\le 22/(3c_0).
\]

The first inequality follows termwise from `1-exp(-u)<=u`; the second
is the explicit conditional input from the cycle note. Each primitive
cycle is counted once, and roots shared by different cycles retain
their multiplicities. The known `1,2` cycle has `a_C=3/4`, agreeing
with its normalized poles `w=+/-sqrt(3)/2`.

## 2. Explicit product, positivity at zero, and exact zeros

The proposed grouped factor

\[
 \beta_C(w)=\frac{a_C-w^{A_C}}{1-a_Cw^{A_C}}
\]

is a finite Blaschke product: it is the disc automorphism
`v -> (a_C-v)/(1-a_C*v)` composed with `v=w^A_C`. Its denominator
does not vanish in the unit disc, and its `A_C` roots are simple.
The normalization `beta_C(0)=a_C>0` is essential for the product
value at zero and is correct.

For `|w|<=r<1`, direct subtraction yields

\[
 |1-\beta_C(w)|
 \le (1-a_C)\frac{1+r}{1-r}
 \le\delta_C\frac{1+r}{1-r}.
\]

The sum of these uniform bounds is finite on every compact subdisc,
which proves locally uniform product convergence independent of the
cycle enumeration. At zero the finite products are
`exp(-sum_C delta_C)`, so the limit is nonzero there and bounded below
by `exp(-22/(3c_0))`. Every finite product has modulus at most one,
and hence so does the holomorphic limit.

The full root-summability bound permits at most
`[22/(3c_0)]/(1-r)` roots, counted with multiplicity, in `|w|<=r`.
Thus only finitely many factors can vanish near an interior point.
For the remaining tail, the same uniform estimate permits analytic
logarithms near one, whose series converges absolutely. The tail
product is nonzero. Consequently the zero order at a point is exactly
the number of primitive cycle factors vanishing there; there are no
additional interior zeros. This justifies the multiplicity assertion
without dropping common roots or assuming finitely many cycles in
total.

## 3. Operator cancellation is local and sufficient

The frozen operator theorem gives a meromorphic resolvent on `|z|<2`
with simple poles and finite-rank principal coefficients. At a pole
`z_0`, its Laurent expansion has the form

\[
 (I-zK)^{-1}=P_{-1}/(z-z_0)+H(z).
\]

The scalar factor `B(z/2)` has zero order at least one there, so its
product with this expansion is operator-norm holomorphic near `z_0`.
These removable extensions agree with the original product off the
locally finite pole set, giving the asserted holomorphic family on
the open disc. Distinct cycles with a common pole add scalar zero
multiplicity but do not increase the resolvent pole order, because
the operator theorem establishes semisimplicity. Applying the
operator family to the fixed vector `g` is continuous and yields the
claimed regularization of the actual forcing.

No estimate in this argument bounds the operator norm uniformly as
`|z|` tends to two. Boundedness of the scalar multiplier alone does
not give that estimate. No continuation of the multiplier or the
regularized resolvent across a boundary point follows from compact
convergence inside the disc. The source explicitly preserves these
limitations and distinguishes the previously proved boundary of the
original forcing from the unclassified boundary behavior of its
regularization.

## 4. Arithmetic and provenance limits

The product is over actual positive ordinary cycles, with their
complete clocks; it is not a product over arbitrary formal parity
words or over successive laps of one cycle. Its existence does not
enumerate these cycles, give an effective tail bound, or imply that
only the known cycle occurs. In particular a summable family of
additional positive defects is allowed by the hypothesis.

The input (P), its uniform constant, its exact pinned repository
source, and the earlier inaccessible-manuscript qualification are
visible in the bridge. It is accurately presented as an inherited
source-qualified premise. The proof of the new conditional implication
does not silently upgrade that premise into a freshly checked
unconditional theorem or into a pointwise continuation statement for
an original ordinary source.
