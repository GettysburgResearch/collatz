# Independent review of valuation-one transport V1--V4

**Verdict: VERIFIED at the stated elementary mathematical scope.**
Full forward-five closure and Collatz remain open. This review does not
extend to V5, later edits, or the external priority and coverage
comparisons in the source preamble.

## Frozen source and review method

Reviewed file: `VALUATION_ONE_TRANSPORT.md` in the parallel
`completion_witness` packet, SHA-256
`a47dd19445db7cf9f8e3e4522686161b39679866e0701f8ac05ecbda292f3422`.
Reviewed claims: V1--V4 and their explicit ordinary legality and energy
scope. The preceding A-ladder is taken from PR166 at
`5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
FL1--FL3, with its formula independently substituted below.

The reviewer reconstructed the identities, source guards, positivity,
first-hit claims, endpoint residue split, geometric series, and residual
rank lower bound. The separate `check_valuation_one_review.py` was
written independently, uses only the ordinary map and exact rational
arithmetic, and does not import the author's checker.

The source now credits the previously existing triple-one blocks in
PR167--PR169 and describes V1--V3 as rederivations. This review makes
no novelty claim and does not independently certify the preamble's
comparisons of those larger dictionaries.

## V1: paired identity and actual ordinary legality

For four odd steps, the source correction at positions 0,1,2,3 is
\(27+18+12+8=65\). The proposed target correction at positions
0,1,3,8 is \(27+18+24+256=325=5\cdot65\). Both words have
four odd inputs and clock \(b+3\), so their affine inverse equations
agree exactly.

The affine equality alone would not be sufficient. Here the target
exponents \((1,2,5,b-5)\) are all positive for \(b\ge6\).
Integrality of the complete numerator modulo \(3^4\) implies
integrality successively through the reversed word because every
power of two is a unit modulo three. Every integral inverse value is
odd. Starting at \(5q\ge5\), each positive integral inverse value
is again positive and cannot equal one: \(I_a(u)=1\) would require
\(2^a u=4\), impossible for odd \(u>1\). On the source side,
\(I_b(q)\ge21q\) and the three legal \(I_1\) steps also cannot
hit one. Thus no hidden first-hit or guard failure is introduced.

The binary congruence \(81x+65\equiv0\pmod{512}\) is exactly
\(x\equiv271\pmod{512}\), and it imposes the first three exact
exponents one and the fourth at least six. Since the smallest source
is 271, the stated \(q\le x/6\) bound holds. The first exponent
distinguishes this cylinder from every A-cylinder. Its relative
density among odd ternary units is \(1/256\).

## V2: finite certificate composition and the closed family

Both block kinds preserve odd count and shortcut clock. Their ordinary
endpoints can therefore be concatenated, and the final ordinary edge
\(5\to1\) adds exponent four. Each target block avoids one before
its stated endpoint, so a supplied source first-hit word yields the
asserted target first-hit word. The grammar can leave a valid word
unresolved; its successful parser is not claimed to cover every
terminating source.

For \(x_k=(2^{54k+31}-65)/81\), the congruences
\(2^{31}\equiv65\pmod{81}\) and \(2^{54}\equiv1\pmod{81}\)
give integrality. Modulo 243 one has
\(2^{54}\equiv1+81\), which gives
\(x_k\equiv2k\pmod3\). The literal exponent words in V2 follow
from V1 with \(q=1\); their positivity and first-hit assertions
survive without a new assumption. The initial-block union density
is exactly \(1/24+1/256=35/768\), with the source's stated scope.

## V3: the joint subcritical renewal

The A-fiber formula rewrites as

\[
x_b=1+(4/3)^r(2^bq-4)/3.
\]

Integrality puts \(b\) in one progression of period \(2\cdot3^r\).
For the B-family the period is 54. Subtracting a positive correction
makes successive positive sources grow by at least the corresponding
power of two, so the complete geometric upper bounds are valid.
Different initial blocks do not duplicate a source.

For \(q\not\equiv7\pmod{27}\), any A-word with \(r\ge2\)
must have \(b\ge5\): a legal \(b=4\) requires
\(4q\equiv1\pmod{27}\). With \(q\ge5\), the A-tail height
is at least \((52/5)(4/3)^r q\). The independently recomputed
contributions are

\[
\frac{32}{155},\quad\frac{512}{1085},\quad\frac8{31},
\qquad\text{sum}=\frac{1016}{1085}.
\]

For \(q\equiv7\pmod{27}\), the zero-defect endpoint seven can
be removed because both seven and 35 reach one. Remaining odd
endpoints are at least 61, giving A-height
\((324/61)(4/3)^r q\). For B-integrality, reduction modulo 27
forces \(b\equiv12\pmod{18}\), hence \(b\ge12\). The two
independently recomputed contributions are

\[
\frac{3144}{3317},\quad\frac1{128},
\qquad\text{sum}=\frac{405749}{424576}<1.
\]

The second sum is larger than the first, so it is a valid uniform
coefficient. All fractional-power comparisons reduce to strict
integer comparisons at exponent 25; the separate replay checks all
nine used comparisons exactly. The cutoffs \(q\le x/7\) and
\(q\le x/6\) justify the common cutoff \(X/6\). The finite-X
subtraction is legitimate even when the infinite energy is not yet
known finite. No absolute moment estimate on the uncovered domain
is claimed or obtained.

## V4: forced target path and rank growth

For \(z_k=(2^{6k+5}-5)/9\), the first two source exponents are
exactly \((1,6k+4)\). Two odd shortcut steps from \(5z_k\)
give \(5\,2^{6k+3}-5\). For \(e\ge4\), the three-step shadow

\[
2^e c-5\;\longmapsto\;9\,2^{e-3}c-5
\]

has exactly two odd inputs and all positive intermediates when
\(c\) is positive odd. Repeating it \(2k\) times gives
\(40\,81^k-5\). The following three steps give
\(45\,81^k-5\); its valuation is exactly three because
\(81^k\equiv1\pmod{16}\). Three halvings yield

\[
T^{6k+8}(5z_k)=\frac{5(3^{4k+2}-1)}8.
\]

The odd count is \(2+4k+2=4k+4\), and the odd endpoint is at
least five. Any eventual first-hit certificate must therefore add
at least one further odd input. This proves the target rank lower
bound \(4k+5\) while the supplied source rank is two. It does not
prove convergence of the target family, and it does not claim the
rank-expansion phenomenon was previously unknown.

## Independent bounded replay

Both normal and optimized Python runs of the independent checker
produce byte-identical JSON. The replay covers 128 literal B-cylinder
inputs, nine closed-family first-hit certificate pairs, thirteen
residual-family forced trajectories, nine exact fractional-power
comparisons, the two case coefficients, and the finite-energy factor
\(424576/18827\). These bounded checks supplement the preceding
unbounded proofs; they are not finite evidence for Collatz closure.
