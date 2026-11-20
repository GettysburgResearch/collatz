# Independent reconstruction of the finite-conductor inequalities

**Verdict: VERIFIED for FC1--FC4 and FC6; VERIFIED WITH THE NAMED
EXTERNAL INPUT for FC5.** This is an internal reconstruction by a separate
agent from the author, not human acceptance or proof-assistant verification.
No approximation to the actual Collatz basin, and no full Collatz theorem,
is approved by this verdict.

The reviewed note is `FINITE_CONDUCTOR_RIGIDITY.md`, SHA-256
`c0808a9550c9e2420fb4a2daaa71602278e891866f2c9e7df55a4487b8f1f526`.
Its mathematical wording and the complete companion checker were read.

## Reconstruction

**FC1.** For each fixed low residue modulo `2^r`, the first `r` branches
are fixed, and the endpoint is an odd-slope affine function of the next
`r` input bits. Thus the initial residue and the endpoint residue are
independent and uniform when sampling modulo `2^(2r)`. Each intermediate
one-step distribution is still uniform at enough binary precision.
Summing the `r` edge costs proves the claimed inequality for any metric.
This includes the residue-zero class without an ordinary zero-orbit claim.

As a different finite reconstruction, the independent checker constructs
the two-successor quotient transition matrix. Every column has total
integer weight two, and its `r`th power has every integer entry one
before division by `2^r`. This verifies exact decorrelation from every
initial row for `1<=r<=7`. It also checks 56 non-Boolean rational label
assignments, separately from the author's Boolean census.

**FC2.** The actual source error contributes `delta`. Even-image error
has mean at most `delta/2`; the injective odd images lie below `3X/2`
and contribute at most `3delta/2`. These are inequalities for positive
sums, with no assumption that an error subsequence has the ambient density.
The result is `3delta`. The anchor argument uses a finite average over
quotient values and is valid for metric labels. Its conclusion is explicitly
constancy in mean, not pointwise constancy.

**FC3.** The two finite defects really satisfy `A<=3delta` and
`B<=8delta`: the second is derived from odd ordinary inputs before passing
to the quotient. The four-edge commutator uses inverse two and inverse
three only where both are units. Its endpoint difference is exactly one,
giving `D<=2A+2B`. The binary random affine walk has uniform intermediate
states and covers each terminal residue at least once in `2^k` choices.
The two positivity comparisons give the displayed constant `28k`.
The independent replay checks all commutator edges on the 99 eligible
moduli between 5 and 300. No conductor divisible by three is smuggled
into this permutation proof.

**FC4.** Exact period divisibility of `N` is load-bearing and is stated.
It makes the finite average of the edge defect its quotient average.
All three error sums are contained in the same enlarged interval for
the same `f,p`; their total is bounded by three times its error count.
The chosen constant value then bounds the smaller actual label class.
The coprime-conductor variant uses its own enlarged interval `6N` and
the finite bounds `A,B<=2E(6N)/N`, giving `1+12k` as claimed.

**FC5.** The original paper by Krasikov and Lagarias was opened directly
at [Theorem 6.1](https://arxiv.org/pdf/math/0205002), printed page 16.
Its shortcut normalization, unit-target condition, exponent `.84`, and
target-dependent large-cutoff threshold match the note. Its large linear
program was not independently rerun here.

The antichain amplification was separately reconstructed and compared with
PR146 at `fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/TWO_SCALE_TRIPLING.md`, section
“Arbitrarily large predecessor coefficients.” An off-cycle odd unit
has two unit predecessors, and equal-depth inverse leaves are distinct
and incomparable: an intersection would make the chosen root periodic.
For each fixed finite depth one can take the maximum of the finitely
many predecessor thresholds. This proves a coefficient tending to infinity;
it does not claim a uniform threshold across an infinite tree. Combining
this with FC4 gives the stated lower error bound uniformly over the
permitted conductors and approximations at each scale.

**FC6.** The first `r` parities are independent fair signs on the dyadic
quotient. The tent sum has variance `V=m(m+1)(2m+1)/3` and fourth moment
at most `3V^2`. The stated Paley--Zygmund estimate yields two opposite
sign tails of mass at least `3/32` each. Clipping at the specified integer
height gives the nonzero oscillation bound. The shift difference has
squared coefficient sum exactly `r`, whereas `V>=r^3/12`; hence its
defect is at most `sqrt(12)/r`. The independent checker verifies those
algebraic identities at all 500 even lengths from 2 through 1000.
The proof covers every even length. These approximate invariants are
never identified with an actual separating Collatz label.

## Actual execution and limits

The independent program `independent_quotient_review.py` was run normally
and with `-O`. Both runs returned PASS with identical output; the report
SHA-256 is
`523402c81ccddfdb01b00c922f1a234ca44bd61aa7456ec4f891216842ab9066`.
The author's source was also inspected for its explicit failures,
bounded ordinary `3n-1` control, and finite-versus-universal scope.
Full checkout executions are recorded separately in the publication
receipts, rather than inferred from this inspection.

No mathematical defect was found. The decisive missing input remains a
periodic approximation with the stated error bound for the actual ordinary
invariant label. The existing prefix-survivor count is neither such an
approximation nor small enough at its current exponent. The proof and
this review keep both distinctions explicit.
