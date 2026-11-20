# Publication refresh: certificate results in PR168 and PR169

This comparison was added after the local proofs and reports were frozen.
**Collatz and the universal supplied-certificate transformation remain
OPEN.** The refreshed sources materially change the novelty description
of parts of this packet. They do not invalidate its identities.

Both fetched refs were checked against the following full commit hashes:

| Source | Frozen SHA | Manuscripts read in full for this comparison |
|---|---|---|
| PR168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md`, FR1--FR5; `NEGATIVE_TEMPLATE_GRAMMAR.md`, NT1--NT3 and the eight instances; `CLOSING_ATTEMPTS.md` |
| PR169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | `research/certificate-renewal-20261121/FIVE_WORD_EXTENSION.md`, FW1--FW5; `C5_CERTIFIED_BYPASSES.md`, CB1--CB4; `FULL_THEOREM_ATTEMPT.md` |

Links: [PR168 five returns](https://github.com/GettysburgResearch/collatz/blob/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md),
[PR168 witness grammar](https://github.com/GettysburgResearch/collatz/blob/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md),
[PR169 five extensions](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/FIVE_WORD_EXTENSION.md),
[PR169 paired descents](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/C5_CERTIFIED_BYPASSES.md).

## Explicit overlap and supersession

**CF1 is a concurrent reconstruction.** PR168 FR2's first row and PR169
FW3 row B already give precisely `(1,1,1,b) -> (1,2,5,b-5)`, `b>=6`,
the cylinder `271 mod512`, and its ordinary legality. PR168 also gives
the same unbounded final-gap first-hit family. These statements must
not be advertised as a new discovery relative to those heads.

**CF5 is a concrete specialization of PR168 FR1--FR3.** FR1 completely
recognizes all equal-clock/equal-odd-count affine five returns, with a
unique target word. FR3 proves that the return language is concatenation
closed and left unitary; consequently its greedy compiler recognizes
the whole balanced language, rather than only a fixed dictionary.
Our mixed block compiler is a proof-producing implementation on a
specific sublanguage, not a coverage improvement over that recognizer.
PR169 FW1 independently supplies the corresponding complete correction
decoder for a fixed prefix.

This inclusion follows algebraically: every CF3 block has target
correction `5B_r` and the same clock and odd count, so FR1 must recover
exactly that target word by uniqueness. A separate implementation of
the printed decoder recovered our target in 100 finite instances
(`0<=r<=24`, four choices of `b` per run). Those replays corroborate
the implementation comparison; the correction identity proves the
all-parameter inclusion.

**CF2--CF4 retain a distinct explicit construction.** Neither inspected
note displays the entry words
`E=(2,1,1,1,2,1,7)`, `F=(3,6,1,2,1,1,1)`, their carry `+4`, the
arbitrary valuation-one loop, or the closed ordinary unit family with
`t_r=88*2^(-r) mod243`. General recognition of each supplied finite word
does not itself exhibit that unbounded parametric identity or its
ordinary realizations. The difference is an explicit subfamily and
proof, not a larger general recognition architecture.

PR169 FW2 is another genuine unbounded extension, obtained by inserting
valuation-two runs into seeds with prefix clock difference three.
Our carry prefix has clock difference one and repeats valuation one.
The specialized languages are incomparable: our entry starts
`2,1,1,1`, whereas PR169's first-`2,1` rows require fourth letter two
or four. Its `112`, `114`, and initial-valuation-three rows are absent
from our fixed dictionary. Both languages lie inside PR168 FR3.

## Renewal comparison

Endpoint-conditioned inverse-fiber summation is also present in both
new sources and is not claimed as a new method here. PR168 FR4 proves
coefficient `903/1000` at exponent `21/25` with cutoff `X/2` on the old
ladder plus four initial-one rows. PR169 FW5 proves `249/250` with cutoff
`X/3` on its eight-row union, including their infinite two-run tails.

Our CR3 treats another domain: the old ladder, the shared short row,
and the **infinite safe carry sublanguage** `b>=r+2`. Its sources
beginning `2,1,1,1` are outside both sources' selected renewal domains.
Their additional rows are outside ours. Thus the coefficients cannot
be compared as estimates on one common source set; our coefficient is
not the strongest numerical coefficient in the repository.

The explicit carry kernel and its joint three-case estimate remain
the additional positive energy contribution. Adding more return
families requires a new complete kernel bound. PR168 FR5 supplies a
relevant warning with exact content: allowing its ninth-one row at
last gap eight produces incoming column mass greater than `1069/1000`
on an infinite ordinary endpoint family. Validity of every local word
therefore does not guarantee uniform contraction of their union. This
does not refute a different source selection, different weights, or an
estimate using properties of the actual invariant label.

## Do the new descents close the missing selector?

PR168 NT1--NT3 supply a general compiler from two signed reference
calculations to positive ordinary parameter descent. Its eight
displayed rules have `M=-1 mod2048` and strict `M'<M`; they transport
arbitrary complete supplied witnesses, even when rank increases.
The source explicitly leaves the rank-five source-zero reference
outside its grammar. Its eight-row catalog does not cover even the
eligible index 2047.

PR169 CB1--CB4 provide two actual paired equivalences on the
fourth-valuation-five class `k=14 mod32`, with

\[
 k'=(16384k-6049)/59049
 \quad\hbox{or}\quad
 k'=(32768k-9911)/59049.
\]

Both arms preserve their prescribed ordinary endpoints while the
eligible numerical antecedent decreases. These are useful physical
descents, not mere necessary congruences. They cover exactly two
congruence classes out of 59049 within that fourth-gap class. They
exclude corresponding rank-five Mersenne subprogressions from being
the globally least failure; they do not assert unconditional convergence
of all the Mersennes in question.

Combining the two displayed catalogs supplies no immediate complete
dispatcher. The CB child indices are respectively `967` and `417`
modulo 2048, so neither enters the eight displayed NT rules. This is
only a check of those catalogs, not an impossibility theorem for the
general NT compiler or for other recursive rules.

The strongest unresolved interface is unchanged: every eligible
certified input needs a successful terminal rule or a justified
well-founded reduction. PR168's balanced compiler still rejects the
fully convergent pair `17,85`; PR169's compiler still excludes the
full-strength PR146 sufficient progression beginning
`(1,3,3,3,3,3,3)`. Every new energy inequality retains an unbounded
complementary term. No closing estimate or total selector was found
in these sources.

## Evidence scope

The comparison reconstructs the correction decoder, language inclusion,
specific shared identities, prefix-domain distinctions, and catalog
congruences. It reads the complete written renewal and descent proofs,
but does not claim a fresh execution of either source's entire kernel
certificate or research suite. The finite-source arithmetic-moment
results and stationary-regularity lane are outside this certificate
review. Their separate reviewers retain their own scopes.

The original local proof/checker/report bytes were preserved. This
addendum and the packet's updated source/front-door descriptions supply
the explicit concurrent credit and supersession boundary.
