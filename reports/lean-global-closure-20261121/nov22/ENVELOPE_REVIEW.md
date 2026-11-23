# Independent review of the fixed-resolution envelope obstruction

## Frozen source and verdict

**VERIFIED, at the written-theorem level and within the stated hypotheses.**

Reviewed file:
`FIXED_RESOLUTION_ENVELOPE_OBSTRUCTION.md`, authored in the parallel
analytic task, SHA-256
`898337c461d9a9c23ac38e99a98800a02a500d51d3660bbdbac8b73fb90509e3`.

Reviewer: the independent ordinary-merger task. I reconstructed the finite
row contradiction, the elementary mixed-modulus routing construction, the
positive ordinary lift, and the application of Monks's published
arithmetic-progression theorem. This is not a Lean formalization of the
asymptotic theorem, a review of all PR180 analytic inputs, or a proof of
Collatz. Later changes to the reviewed file need their own scope check.

The claim-level verdicts are:

| Claim | Verdict | Exact scope |
|---|---|---|
| Theorem A, ternary modulus | VERIFIED | Nonnegative excessive F; p<1; fixed finite profile; displayed affine factor limits. |
| Quantitative defect (13) | VERIFIED | Nonzero finite profile with the same limits; nonnegative parent series, possibly infinite. |
| Mixed binary–ternary extension, Section 7 | VERIFIED | Elementary finite routing and positive lifts; stronger affine limit assumption (14). |
| Corollary B, arbitrary modulus | VERIFIED using its explicit published input | Monks's negative arithmetic-progression sufficiency, stated in the author PDF, plus the independently checked positive lift. |

## 1. Finite row and its quantifiers

For the actual positive targets q=2*3^(r+1)k−1, all selected odd
exponents are legal. Their parents are positive odd integers, tend to
infinity with k, and have precisely the displayed residues
−(2^e+1)/3 modulo3^r. The parent ratio tends to2^e/3.

The valuation induction v_3(4^(3^j)−1)=j+1 is correct: after factoring
the cube difference, its remaining factor is1 modulo3. It determines
the order of4 modulo3^(r+1), and consequently the exponents
e=1,3,...,2*3^r−1 cover every parent residue exactly once. The case
r=0 has a single residue and a single retained exponent and is included.

The normalized term limits use only a fixed finite collection of
exponents. The input asymptotic applies to each corresponding ordinary
parent progression; the factor condition supplies the ratio of L values.
No infinite sum/limit interchange is made. Nonnegativity permits dropping
every other parent term before passing to the finite limit.

The e=1 term returns to the target profile residue, with weight
(3/2)^(1−p)>1. Its coefficient must be zero. The finite inequality then
forces every other coefficient to be zero because every weight is
strictly positive and all profile coefficients are nonnegative. Zeros in
some cells do not invalidate the argument.

For the quantitative assertion, when a maximum profile value occurs at
the self residue the defect is at least (s−1)A. Otherwise one distinct
retained parent has value A, contributes at least c_min A, and the self
defect is nonnegative. This proves the stated conservative positive
minimum. An infinite parent sum only strengthens the lower bound; the
target F value is finite in the asymptotic regime.

## 2. Mixed-modulus negative routing

I checked the congruence construction independently. Given an odd binary
residue and any ternary residue b, take k=h+1 actual positive odd steps
from one positive representative u. Their total clock A is greater than
h. With 2^A U^k(u)=3^k u+C, the condition

    y ≡ 2^(−A)(C+3^k b) mod3^(k+r)

indeed makes x=(2^A y−C)/3^k integral and gives x≡b modulo3^r.
Reducing the numerator modulo2^h gives x≡u modulo2^h. The chosen y
is an actual negative odd one-step predecessor of−1; the ternary
residue bijection supplies it without a convergence premise. Since y<0
and C>0, the constructed x is negative.

The step from terminal integrality to full word legality is justified.
Writing C=3C'+2^(A−a_k), divisibility by3 of the full numerator forces
divisibility of2^(a_k)y−1 because powers of two are units modulo3.
After taking that integral parent, the remaining numerator is divisible
by3^(k−1). Repeating proves every inverse letter integral. Starting
from odd negative y, each integral predecessor remains odd and negative;
its prescribed exponent is exact because its successor is odd. This
provides a finite actual odd history, rather than just a terminal affine
identity.

This construction is independent of any assertion that all positive or
negative trajectories converge. It establishes only the selected finite
negative histories and their residue coverage.

## 3. Positive ordinary lift and operator iteration

For a fixed history z<0 to−1, with odd count ell and total clock B,
the identity −2^B=3^ell z+C_W gives exactly

    q_t = −1+2M3^ell t,
    x_t = z+2^(B+1)Mt,
    2^B q_t = 3^ell x_t+C_W.

The finite integrality argument applies to the same word. For large t,
its finite list of affine intermediate values is positive and odd, so
the history is now an actual positive ordinary trajectory. The target
residue is−1 and the source residue is z moduloM. Its slope ratio is
x_t/q_t→2^B/3^ell. Both parameters and the word are fixed before
t tends to infinity; no changing-depth estimate is inferred.

For a nonnegative excessive F, positivity of the kernel gives
P^ell F≤F by induction, with finite intermediate values bounded by F.
Keeping this one actual inverse word therefore gives (21). Its asymptotic
coefficient is (3^ell/2^B)^(1−p), which is strictly positive. A zero
profile at−1 consequently propagates to every covered residue. The
e=1 self-return has both source and target congruent to−1 modulo the
arbitrary fixed M and supplies that initial zero for p<1.

## 4. Exact published bridge to arbitrary moduli

I opened the author's primary PDF independently:

<https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf>.

Its definition on page1 makes sufficiency mean meeting every merger
component. Theorem1.1 is the arithmetic-progression result, and page2
expressly extends it to every negative arithmetic progression for T on
the negative integers, saying the repeated proof is omitted. The reviewed
packet identifies this import accurately; it does not present a new proof
of the whole published theorem.

For any required residue containing odd integers, one can choose a
negative arithmetic progression with step2M, all terms odd and in that
residue. Applying the published sufficiency result to−1 supplies a
member merging with−1. The signed shortcut map has T(−1)=−1, so this
is a finite actual hit of−1. Compressing its even runs supplies the
finite odd gap word needed by the independently verified lift. No
assertion about convergence of every negative integer is involved.

The reviewed text now explicitly distinguishes this signed shortcut map
from the separate minus-one scaffold S. That distinction resolves the
potential notational ambiguity; the map used in Monks and in the
negative-basin argument is the same (3z+1)/2 odd branch.

## 5. Boundaries of this review

The fixed profile is an actual asymptotic limit, not merely an upper
bound or a fitted table. The modulus and finite words are fixed before
the limit. A nonnegative sublinear bound on the canonical envelope does
not automatically satisfy these stronger assumptions or define an
excessive function itself. Accordingly, the theorem rules out the stated
profile architecture and leaves variable-resolution or irregular
excessive functions available.

Sections5–6 discuss existing potential and transport work. Their upstream
analytic assertions are not independently re-proved by this review, are
not needed by the new theorem, and do not inherit this verdict. The
review also makes no judgment about novelty in the wider literature.
