# Independent internal review of the full-word Mahler and torus attack

Date: 2026-11-23. Reviewer: `closure_collision`, a separate in-session
mathematical lane from author `closure_cycle`.

**Verdict: VERIFIED for the elementary statements enumerated below;
SOURCE-QUALIFIED for the stated Adamczewski--Bell implication. Full positive
cycle exclusion remains OPEN.** This review does not certify the neighboring
PRs, the complete external proof, or a full Collatz theorem.

## Exact reviewed files

The files were read in the shared worktree based on
`2169884b64871b448cda16c7d74a0d5914ed870b`. The hashes below were computed
after the author applied the narrow wording clarification described below.

The final publication normalization removed one extra terminal newline from
each of these three files. I independently verified that appending exactly
`b"\n"` to each normalized file reproduces its previously reviewed SHA-256.
No other byte changed; the mathematical review therefore applies unchanged
to the normalized hashes below. Each file now has one terminal newline.

| Path | SHA-256 |
|---|---|
| `research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md` | `3361b2a3d1e2fc9bbbbd92f5d5618125abbaecd3e641aa03169dc9105b5c488a` |
| `research/global-closure-20261123/cycles/README.md` | `e6019b067b4af7bd24aecf68bb4db740cef76528ee8d4f6fb3a5e958f7235422` |
| `reports/2026-11-23-global-closure/cycles-sources.md` | `ca1b1e174d4a9e1184c1dfc5426a1b68d7fd4a0871c3884c4d441dfa09104cfb` |

## Reconstructed claims

### 1. The full word and physical cycle condition

I reconstructed the shortcut numerator
`C = sum_i 2^d_i 3^(p-1-i)` and full denominator `D = 2^A - 3^p`.
With `D>0`, `C/D` is positive and has odd reduced denominator. A first
incorrect formal parity creates a factor of two in its reduced denominator;
afterward either formal branch increases that two-primary denominator.
It cannot return to the odd-denominator fixed point. In particular `D | C`
gives the supplied ordinary positive itinerary, not just an unrelated
integrality test. Restricting to primitive words removes repetitions of
the trivial period; the primitive trivial words are `10` and `01`.

### 2. Polynomial identity and sparse-series nonrationality

The even/odd decomposition gives the claimed identity because the shortcut
images are `k` for `2k`, and `3k+2` for `2k+1`. The odd-to-odd edge
partition also reconstructs equation (6): its finite tails cover each
state of the supplied cycle once.

For Proposition 1, two distinct positive odd numbers cannot generate the
same dyadic ray exponent. Hence a nonzero coefficient remains nonzero at
infinitely many exponents, while the number of supported coefficients up
to X is at most a constant times log X. This gives arbitrarily late zero
blocks of every finite length. A rational formal power series with a
denominator nonzero at zero satisfies an eventual forward linear recurrence.
A zero block as long as the denominator degree, beyond the recurrence
onset, forces every later coefficient to vanish. The contradiction is
valid over the stated characteristic-zero field. The proof also gives
linear independence of these rays modulo rational functions.

### 3. Exact independent-base hypothesis

I independently opened the primary journal PDF of Adamczewski--Bell,
*A problem about Mahler functions*:

<https://journals.sns.it/index.php/annaliscienze/article/download/574/560/792>

Definition 1.1 and equation (1.3), printed p. 1303, permit the displayed
inhomogeneous polynomial relation. Theorem 1.3, printed p. 1306, states the
characteristic-zero, multiplicatively independent-base rationality
conclusion used here. Thus the finite odd-ray series is 2-Mahler, and its
proved nonrationality excludes a 3-Mahler equation for that same series.
The theorem's full proof was not reconstructed or formalized in this review.

The distinction in equations (11) and the following display is real: the
factor `z^(2^j)` depends on the dyadic clock and cannot be replaced by a
single outside factor `z`. The trivial cycle example also verifies that
the actual second relation can have base four, without an independent
base-three relation. No absent hypothesis is promoted to a conclusion.

### 4. Integral lattice and actual reduced denominator

For `r=C/gcd(C,D)` and `s=D/gcd(C,D)`, I recomputed the second-coordinate
exponents in the claimed semiconjugacy. Equality is exactly
`alpha*r + C*s = beta*r`, or `D*r=C*s`. The torus map
`(x,y) -> (x,x^r*y^s)` is surjective over the complex torus and has kernel
`{(1,zeta) : zeta^s=1}`, so its degree is s.

Any triangular monomial map of the stated form has the same exponent
equation. Coprimality of the reduced pair forces s to divide its second
exponent. This proves minimality within precisely the specified triangular
class. Degree one gives the explicit integral monomial inverse; a larger
degree gives a nontrivial kernel. The complete numerical denominator is
retained, rather than one factor or the polynomial denominator before
evaluation.

I requested one wording clarification in equation (17): an “integral
triangular diagonalization” there must be **by an integral triangular torus
automorphism**. Integral triangular isogenies already exist at every degree.
The author made this change before the hashes above were recorded. With
that qualification, all equivalences in (17) are correct.

The character `x^r*y^s` has dilation factors 2 and `2^A` under the two
displayed maps. These are dependent for every s. The presence of `3^p`
in another coordinate does not add an independent action on that same
series. I also recomputed the two examples: `11010` gives `(C,D)=(23,5)`;
`10` gives `(C,D)=(1,1)`.

## Scope and final assessment

No mathematical defect remains in the reviewed elementary arguments after
the wording clarification. These are written reconstructions, not Lean
checks. The new packet has no Lean additions and no new cycle census, and
none was requested for this review. The external source survey beyond the
specific Adamczewski--Bell statement remains the author's attributed
inspection; this review does not widen that scope.

The packet correctly stops before proving `D/gcd(C,D)>1` for every
nontrivial primitive positive word. Its natural Mahler series cannot have
the proposed independent equation, and its torus normalization allows both
degree-one and higher-degree cases. The README and evidence record preserve
that no-exclusion status.
