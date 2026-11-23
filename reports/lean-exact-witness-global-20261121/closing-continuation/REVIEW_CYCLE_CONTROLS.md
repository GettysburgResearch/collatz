# Independent review of complementary carries and fractional-part controls

Reviewer: the target-entry research agent, independently of the cycle-lane
author. Date: 23 November 2026.

**Verdict: VERIFIED WITH THE APPLIED WORDING FIX at these exact source
hashes, within the narrow scope below.** This is internal mathematical
reconstruction and a targeted execution. Positive integer cycle exclusion
and the all-residue fiber bound remain OPEN.

| File | SHA256 |
|---|---|
| `research/lean-exact-witness-global-20261121/CYCLE_EXCLUSION_CONTINUATION.md` | `4c16065f7439800b50e429c28ed1b2e64facad4d8df8a01650908d30aea0dcb4` |
| `research/lean-exact-witness-global-20261121/cycle_fiber_controls.py` | `98eacffe0ef3bd2f02e8044764a8dd443c49dbf0bf04a5e9c5b3eeba31e0e24e` |

## Reconstructed identities and quantifiers

The map is the shortcut map on rationals with odd reduced denominator;
parity is numerator parity. For a binary word of length A and weight p,
the complete return denominator is `D=2^A-3^p`. Its correction is
`C=sum_j 2^(d_j)*3^(p-1-j)`. The rational fixed point `C/D` follows the
literal word: rotating the affine return identity and reducing each first
edge modulo two forces its stated parity. The argument does not replace
the whole denominator by selected prime factors.

For the cyclic linear system `L_w x=w`, reduction modulo two gives the
identity matrix. Thus the carry digits `b=c mod 2` are the actual binary
digits of `L_w^(-1)c`. Subtracting `L_w b` and dividing by two gives CE4
and CE5. Checking the four allowed odd-phase carry values and two allowed
even-phase values gives the uniform invariant CE6. A zero carry means the
remaining rational quotient vector is zero, so the original vector has a
finite nonnegative binary expansion. Conversely a nonnegative integral
vector reaches zero after its largest bit length. This proves the stated
equivalence, without a finite-search inference.

For a nontrivial positive integer cycle, multiplying the odd-edge factors
gives `2^A<=4^p`, with equality only when every odd state is one. Hence
`p>A/2`. The complementary denominator is positive; if even one
complementary state were integral, the entire complementary cycle would
be a positive integer cycle and would give `p<=A/2`. Complementary
integrality would therefore close this route, but no such transfer is
proved. The negative integer example is a counterexample to signed
integrality transfer, not to positive zero-carry transfer: a negative
integer retains its negative binary tail instead of reaching zero carry.

Multiplication of the two complementary edge equations gives CE9.
Summing the individual linear balances and the product balance gives
`sum_i (2*x_i-1)*(2*y_i-1)=3*A`, exactly CE10. This identity holds for the
actual signed rational cycles; it supplies no divisibility conclusion.

If two fixed points share a residue modulo the complete D, their initial
difference is an integer. After a common elapsed clock L and a common
odd count h, the affine difference in CE12 has a power-of-two denominator.
Both endpoint denominators are odd, so the difference is an integer.
For a nontrivial excursion of the odd-count difference, the earlier one
positions give the claimed strict comparison of local corrections. The
review caught the empty-interior exception: a one-clock block with
identical bits has equal corrections. The author added this qualification
before the pinned final hash. No stronger sign conclusion for the actual
endpoint difference follows.

## Independently replayed controls

The reviewer executed the frozen script normally and under `python -O`.
Both exited zero and produced byte-identical output with SHA256
`8ab300068e0bc3e87925df330d75ae1c1d1838cb15df4d0f71c6bfcf4a2697e9`.
All guards are explicit exception checks and survive optimization.

The full-fraction replay verifies the following two controls, including
every edge parity, closure, distinctness of all states, and cyclic minima:

- At `(A,p,D)=(16,10,6487)`, the roots `83245/6487` and `109193/6487`
  are distinct primitive cycle minima above twelve and differ by four.
  Their common residue is 5401. This refutes uniqueness of a minimum in
  a fractional-part fiber.
- At `(A,p,D)=(21,13,502829)`, the roots `3703718/502829` and
  `4206547/502829` initially differ by one. At clock fifteen they have
  both taken eleven odd steps, but their difference is minus one. Every
  state is above three. The initial shared residue 183915 is a unit
  modulo D. This refutes the proposed synchronized noncrossing property
  with all of these guards retained.

The script also replays three complementary pairs, checks CE9 on every
edge and CE10 for each pair, and performs 32 carry updates on each of ten
specified rational cycles. The two trivial positive-cycle phases reach
zero carry at update two. The finite carry runs verify these examples;
the all-time alphabet and zero-carry equivalence are justified by the
written argument above, not by observing 32 updates.

## Boundary of the verdict

The zero fiber would contain all A distinct rotations of a nontrivial
primitive positive integer cycle. Thus the proposed bound `N_0(A,p)<A`
would exclude such a cycle. The displayed rational pairs neither prove
nor refute that bound, or the stronger all-residue bound CE2. They refute
two proposed proofs of it. No cycle here is asserted to be a nontrivial
positive integer cycle.

The continuation contains no new Lean declaration. The review does not
claim a fresh execution of the earlier source packets, their larger
enumerations, or the cited external paper. The relevant algebra and
specified rational controls have been reconstructed independently here.
The remaining mathematical obligations are still complementary
integrality at denominator one, or a sufficiently strong zero-fiber
cardinality bound.
