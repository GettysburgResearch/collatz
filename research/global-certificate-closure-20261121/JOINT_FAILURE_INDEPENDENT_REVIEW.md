# Independent review of the directed-five certificate cost theorem

**Result: PASS for the scoped conditional construction, sharp fixed-cover cost,
and joint-minimum inequalities. No full Collatz closure is supplied.**

## Reviewed snapshot

The sibling files were read in full at these SHA-256 values:

| File | SHA-256 |
|---|---|
| `JOINT_FAILURE_CERTIFICATE_COSTS.md` | `b7cb2190fb0b726a06f061c2c8b9ca9f0aadcc2ba6b9ff686145154461ff358d` |
| `check_joint_failure_costs.py` | `d83caa500af3f42a0e9fd585aee932d43ded83202664cee1088fb6dfa5b4eee3` |

The copied `directed_five_certificate.json` has SHA-256
`751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1`.
Its bytes were independently compared with the exact Git object
`64361ecca770092d6c8242dc6211e38818af2e50:reports/2026-11-20-global-closure/merger-certificate.json`
and matched. The reverse-budget source
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc:research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`
was also read directly. Its all-lift cost is indeed `2025217/23`; retaining
that rational value in its induction, instead of rounding upward to 88053,
is valid with the same strict inequality at the least reverse failure.

The independent checker in this directory imports none of the reviewed
checker, its affine verifier, its ratio maximizer, its program compiler,
or its certificate splicer.

## 1. Directional certificate splicing

The direction of the special `/5` arrow is correct. In a word read from
the proposed source `n` toward the smaller endpoint `q`, an arrow
`x -> y` means `y in C => x in C`. At a division `x=5y`, write
`y=2^t r` with `r` odd. First supply the ordinary certificate for `y`
by reversing the ordinary suffix from the already certified endpoint.
Its first `t` halvings supply a certificate for `r`. The physical query
is then precisely `r in C =>5r in C`. An actual certificate returned for
`5r` can be prefixed by the `t` halvings from `x=2^t 5r`.

Thus the proof never assumes convergence of a large query antecedent from
its size alone. Its certificate is constructed before the query is called.
There is at most one `/5` in a level, so the suffix used for this operation
contains only ordinary equivalences. Reversing the complete sequence of
strictly decreasing levels provides the dependency order from the base 1.

The ordinary splice cases also have their claimed orientation:

* `/2` is an actual forward ordinary edge and is prepended.
* At `x ->3x+1`, with `x` odd, the two values have the same next shortcut
  iterate. Replace the first value of the supplied certificate by `x`.
* At `x -> I_j(x)`, the verified relation is `T^j(I_j(x))=x`.
  The certificate beginning at `I_j(x)` is cut at clock `j`.

The last case sometimes needs a splice clock after the first arrival at 1.
Padding by the actual shortcut cycle `1,2,1` is legitimate. If the cut
leaves terminal value 2, one last actual edge `2->1` completes it. The
reviewed implementation handles both possibilities. Independent explicit
controls checked `I_2(1)=1`, which pads to terminal 1, and `I_1(2)=1`,
which pads to terminal 2 before appending its last halving.

The claim is a finite **conditional proof program**. It does not assert
unconditional termination of an unresolved oracle's search for a target
certificate. This distinction is stated correctly in the reviewed note.

## 2. Sharp whole-cell five-query cost

The independent check reconstructed all 464 affine cells and 55 words,
including the 219 appearances of `/5`. It verified every inverse guard,
odd-input guard, exact division, positive affine state, and ternary-unit
guard on the whole nonnegative lift domain. It also independently checked
the complete disjoint partition of all 497,664 residues coprime to 30
modulo 1,866,240.

For independence from the reviewed ratio helper, each source was rewritten
as `n=m t+n_0`, with `t>=0`, by absorbing the cell's lower parameter into
the intercept. If the unstripped query value is `a t+b`, the checker verified
both coefficients of

\[
\frac{3669265}{2239}(mt+n_0)-(at+b)
\]

are nonnegative. This proves the claimed query budget on every lift,
without sampling integer sources or differentiating a ratio in the code.
Taking the odd part can only decrease the query antecedent.

The sharp witness is exactly the stated cell and word:

\[
n=8640u+2239,\qquad
r=14155776u+3669265,\qquad u\ge0,\qquad\text{word W17}.
\]

This entire antecedent family is odd. At `u=0`, no odd normalization is
lost and the ratio is exactly `3669265/2239`. This proves sharpness for
the frozen cover and the specified compiler, as claimed. It does not
establish optimality among other covers or conditional programs.

The all-lift endpoint contraction was independently verified by checking
both coefficients of `19n-20q`. The largest exact endpoint ratio is
`13403/14119`, which is below `19/20`.

## 3. Termination and query count

The even and divisible-by-five special cases preserve the positive ternary
unit domain and contract by `1/2` and `1/5`, respectively. Every other odd
unit lies in exactly one affine cell and has `q<=19n/20<n`. The proposed
program therefore reaches 1 by strict decrease of positive integers.

If there are `K` levels and `n_K=1`, then

\[
1=n_K\le (19/20)^K n.
\]

Consequently `K<=log(n)/log(20/19)`. The stated ceiling bound is a valid
slightly weaker integer bound. Since each level contains at most one five
query, the same stated bound applies to query count. Each later level
source is smaller than the original source, so every antecedent is at most
`B n` with `B=3669265/2239`.

Thirteen independent finite executions reconstructed actual ordinary
certificates and supplied each oracle with its already completed actual
antecedent certificate. The execution controls used exact integer checks
`n*19^K>=20^K`; no floating logarithm was used as evidence for the bound.
Those bounded executions test the implementation and dependency order,
not universal physical-five closure.

## 4. Least-five and joint-minimum logic

The least-five interval is valid. If `Bn<f_*`, every requested odd unit
antecedent lies below the **same** global least failure `f_*`. Minimality
makes its forward-five implication true, and the program supplies the
antecedent certificate in the correct order. The resulting ordinary
certificate proves `n in C` for positive ternary units.

For a general positive integer, strip powers of two to an odd `v<=n`.
When `3|v`, its successor `(3v+1)/2` is a ternary unit, and because `v>=3`,
it is at most `5v/3<=5n/3`. Thus the all-integer factor `5B/3` is valid.

The failure-localization statement also has the correct logical strength.
Along the finite list of decreasing program sources, choose the last source
outside `C`. Its next endpoint is in `C`. Its word must contain `/5`, since
ordinary equivalences alone cannot connect those labels. The ordinary
suffix certifies the antecedent; the ordinary prefix transfers the bad
label to its multiplied target. This identifies an actual failed forward
implication of the proved size. It does not pretend that nonconvergence
can be detected by a finite numerical test.

With `A=2025217/23`, the joint bounds are correct:

\[
X_*/(5A)\le f_*
\le B(27X_*+101)/128.
\]

The left inequality follows by applying the exact unit interval to the
bad ternary unit `5f_*`. The right follows from the six-clock ordinary
identity

\[
T^6(64k+1)=27k+1=(27X_*+101)/128,
\]

whose endpoint is a bad ternary unit, followed by failure localization.
All minima are global minima of the same fixed failure sets; no minimum
is restarted within a rank or after a query.

The generic return bound is therefore `5Af=10126085f/23`. Combining it
with the older forward bound `q<X/4` does not provide a contracting scalar
rank: the product is `10126085/92>1`. Even the sibling's newer forward
bound `q<X/13` would leave product `10126085/299>1`. This latter observation
does not review the separate proof of the newer reduction; it simply states
the consequence if that interface is used. The incompatibility is between
the currently proved uniform bounds, not a theorem excluding a better
certificate-dependent return or nonlinear measure.

## Outcome and retained evidence

No correctness defect was found in the reviewed scope. The conditional
construction concretely supplies its oracle antecedent certificates and
their all-source budgets. It does not supply the missing return with
strictly smaller reverse upper antecedents, so its own `OPEN` conclusion
is required.

The independent checker is `check_joint_failure_costs_independent.py`.
Its report `joint-failure-independent-review-report.json` records all
reviewed hashes, the sharp witness, complete-cover counts, thirteen program
replays, and the padding controls. The source-pin comparison is recorded
in `execution_receipt.json` in this directory.
