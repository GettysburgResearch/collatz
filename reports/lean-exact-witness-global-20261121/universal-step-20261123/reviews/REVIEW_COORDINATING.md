# Coordinating reconstruction of the new universal-step packet

23 November 2026. Reviewer: root coordinating agent. This is an internal
reconstruction at the listed source hashes, not external acceptance.
Root contributed to the negative-phase idea and the cycle minimum/gcd
strengthening, and authored the unequal-shape extension. Independence of
idea origin is therefore not claimed. Separate lane reviews are retained.

## Candidate recognition — VERIFIED at written/formal scopes

Sources:

- `NEGATIVE_NUMERATOR_RECOGNITION.md`:
  `ff00acf44c7b99eef45baec24a59c76c71777e610c8f103f1dbe997d1176d2eb`.
- `NegativeCandidate.lean`:
  `6f4739e252c100b501dc0a1fbaaf10644631f075e3ff82f497dee2dec7e3b8cd`.
- `negative_candidate.py`:
  `f1995c7e5552044c7e8a73aac48e8a5ad9a2aa9ec6f093d46fed10298a05556a`.

I independently checked the literal numerator update in each branch:
while both numerators are negative and the denominator remains positive,
`2|w'|<=|w|`. This gives the binary-length budget without `F(r)`.
The supplied negative true dual has the inherited forced terminal
segment through `(8,-1/9)`, so its hit at one is at most `bl(A)+2`.
For `b=r-2` even-original positions before 8, the full complementary
carry identity is `A=2^K+9D_K`, with `K>=b` and `D_K>=3^b-2^b`.
This proves `A>=3^r-2^(r+1)`, with equality only on the all-even prefix,
and the stated `3^r<=9A` filter.

The Python recognizer reduces before applying these filters, rejects a
giant binary exponent before constructing its power, checks the literal
parity before each integral update, and accepts only the first crossing
`(4,1,1)`. A negative exhausted denominator and zero crossing are rejected.
No unbounded orbit search is called by `recognize`; the fixture generator
is separately bounded and called only by the finite self-test. The emitted
odd-input tuple is reconstructed from the actual path and checked against
the entire original integer equation, including the length-zero input 1.

Polynomial bit complexity follows because surviving r is at most `E+1`,
all powers have O(E) bits, there are at most E paired transitions, and
the ordinary state has at most `bl(n)+E` bits. This is not a claim of
linear bit operations. Exact crossing is essential: the short matching
prefix of `(24,-1,2)` is explicitly rejected.

The thirteen Lean declarations were freshly compiled and audited by root.
Their completeness theorem consumes a literal first-crossing certificate;
the implication from Omega equality to such a certificate is the written
use of the pinned prior triadic rigidity theorem, not a new Lean axiom.
Universal candidate existence remains OPEN.

## Equal-shape full-denominator capacity — VERIFIED at stated positive scope

Sources:

- `BLOCK_CARRY_CAPACITY.md`:
  `1998aac23dad7772f335f82d2c236175e923fbe40e091de6ae33c3d7c85795fb`.
- `BlockMixture.lean`:
  `4f7dc5cc1673df8088a3345f62e9f705de61c3fc1eb0166b58b77e5d29f2ec3d`.

Unrolling every cyclic cut gives `D_N x_i == C_0 S_N (mod G)` for the
whole `D_N=Q^N-P^N`. Cancellation gives the common difference lattice
`G/gcd(G,D_N)`. An incoming edge and an outgoing edge at the same minimum
value need not be adjacent: using their two equations gives the exact
lower span `(P+Q)G/gcd(G,D_N)`, even with repeated minimum plateaus.
Thus no primitiveness premise is silently added.

For two distinct blocks, a mixed path cannot have constant boundary
values. The period-dependent gcd bound and its all-period 6-free
consequence follow. The complete carry difference acquires only
`2^|F|3^p(H)` under common contexts. I checked the swap and homogeneous-run
formulas and the arbitrary U/V conclusion, including pure repetitions of
their nonintegral fixed points. Arbitrary word coverage is not supplied.

The Lean proof uses the complete geometric sum and strict mixed-weight
interval `0<E_N<S_N`; coprimality with a 6-smooth carry difference then
contradicts divisibility. Eight public declarations, including the closed
integer-path corollary at arbitrary length, compiled and audited. The
larger gcd-capacity theorem remains written scope.

## Ordinary basin and inverse transport — VERIFIED conditionally

Sources:

- `SIBLING_BASIN_COLLAPSE.md`:
  `da21d0b98230fd190f318a07e04cd2a3069740c7a7a4eba52594ca4165303db2`.
- `BALANCED_INVERSE_TRANSPORT.md`:
  `58f5af3b205fb1ac720593865ea2bcba60fa918c5432f0c1917a467edfa94b9b`.

I reconstructed `A(q)=mu(q)Z_s(q)` using unique ordinary hitting depths,
the disjoint predecessor-tree conservation law, and `A(q_j)↑1` on the
unchanged component. Every upper sibling joins the original ray in one
step; the injectivity of that ray makes all their basins disjoint.
The factor `64^(-hs)` and division by `A(q_j)>=A(q_0)` give the stated
double summability. The local formula retains the mass at `q_(j+1)`.
The exponential ordinary growth upper bound justifies the divergent
reciprocal clock comparison, including the extra logarithm.

For the transport, the six-residue table is the unique solution to
`2^e q ==3c+1 (mod9)`, and every parent has unique address `(c,j)`.
Preserving that address keeps the parent colour equal and permits exact
recursive reversal at every depth. The signed cost belongs to
`{-4,-2,0,2,4}`; no assumption of centered or independent increments is
introduced. Telescoping the two actual edge identities verifies both
the ancestor-height formula and the pressure density
`64^(-s)2^(-s Delta)` for sibling roots.

The finite-depth compiler yields a discounted Green lower bound, not the
unproved near-logarithmic comparison. I also considered roots approaching
the negative fixed point and its sibling anchor; no valid uniform control
of the remaining Green tail was obtained, and no refutation or closure is
claimed from that investigation.

## Execution and limits

Root freshly executed the two new Lean modules and four new exact
checkers, normal and optimized: all ten commands pass, all 21 audits have
only standard axioms, and paired Python outputs are byte-identical. See
`../ROOT_REPLAY.json`. These checks concern this checkpoint only.
The unrelated historical corpus, full arbitrary-cycle exclusion, universal
candidate construction, and escape exclusion were not proved or replayed.
