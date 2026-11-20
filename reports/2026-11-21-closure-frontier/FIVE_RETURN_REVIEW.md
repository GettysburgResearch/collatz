# Scoped reconstruction of the five-return packet

**Verdict: VERIFIED at the claim scopes below. Full five closure remains
OPEN.** This is an internal independent reconstruction by a separate agent,
not external referee acceptance or proof-assistant verification.

## Exact checkpoint

The review read the complete note and complete executable. It applies to
these bytes, not later versions:

| File | SHA256 |
|---|---|
| `FIVE_RETURN_LANGUAGE.md` | `12e4b77e5ef6469c102170a252a56c87405a81e403a573ecb139b69298a5e773` |
| `five_return_compiler.py` | `95d8c552528992fd15479cd8e5484b8d924e5763a33ece431d4e2d88943f4d57` |
| `five_return_report.json` | `cd836cf0e13e274a22db68c23a4f9201e4d53f60d6d9e19047b5a9a83ccb414b` |

The final code/report checkpoint clarifies the distinction between density
of binary cylinders and natural density of their ternary-unit restriction.
The claimed relative density and all mathematical calculations are unchanged.
The note uses accelerated odd words and the shortcut clock exactly as stated.

## Claims reconstructed

| Claim | Verdict | Reconstruction and boundary |
|---|---|---|
| FR1 | VERIFIED | Necessity, sufficiency, uniqueness, and ordinary positivity for the supplied balanced return word. Complete only for equal odd count and equal clock. |
| FR2 | VERIFIED | Four infinite source families, exact source cylinders, and unbounded first-hit specializations. The source is an actual positive integer, not only a formal inverse. |
| FR3 | VERIFIED | Finite-input termination, successful witness correctness, concatenation closure, left cancellation, and completeness of greedy decomposition within that language. `UNRESOLVED` is essential. |
| FR4 | VERIFIED | The finite 486-row certificate bounds the whole infinite incoming sum, with the correct ordinary endpoint domain and cutoff. It reduces energy finiteness to the complement and does not bound that complement. |
| FR5 | VERIFIED | Adding the valid r=9,b=8 branch destroys the stated uniform column contraction. The overloaded sources are positive odd ternary units in disjoint source cylinders. |
| OPEN-FR and imported global payoff | OPEN / source-qualified | No proof of the absolute remainder estimate, no new audit of every external dependency of PR163 FE1, and no full Collatz theorem. |

### FR1: why the greedy correction is complete

For a word of p odd inputs, its correction is
\(\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j}\), with \(A_0=0\).
After removing its leading \(3^{p-1}\), the remaining sum has valuation
exactly \(A_1\), because its first residual term is odd after division
and every later residual term is even. Repeating gives each subsequent
position uniquely. The last test M=1 checks the remaining terminal term;
the clock test forces the last gap to be positive. This proves the stated
algorithm rather than merely its agreement with small examples.

The affine identity requires exactly B(v)=5B(w). Final divisibility by
\(3^p\) propagates backwards through the inverse branches: modulo three
the lowest surviving correction term forces the last inverse to be
integral, then division gives the next congruence. Positive odd endpoints
and positive exponents make every resulting integral inverse positive odd.
Thus every displayed gap is the actual valuation, including the final gap.

### FR2--FR3: universal families and certificate semantics

For the one-run source, its correction is \(3^{r+1}-2^{r+1}\).
The four displayed target patterns have five times that correction; only
the final gap depends on b. Checking the fixed positions therefore proves
the identity for all b in the stated ranges. The endpoint-one progression
comes from the exact order of two modulo \(3^{r+1}\):
\(2^{b-1}=-1\) exactly for b=1+3^r modulo2*3^r. Positivity and the
initial increasing one-run show that 1 has not been visited prematurely.

The source cylinder at threshold b0 imposes first r exact gaps equal to
one and the next gap at least b0; it does not assert the final gap equals
b0 on every lift. This distinction is implemented correctly.

Successful compilation ends each block at 5q>=5. An accelerated orbit
that had reached 1 earlier could never leave 1, so the target cannot have
an earlier hit. Appending the exponent four at 5 gives a first-hit word.
Its odd count and total shortcut clock have the asserted increments one
and four. The procedure verifies a first-hit input rather than silently
accepting arbitrary padded certificates in that count identity.

For completeness of the greedy segmentation, ordinary realizers of any
finite source word exist at arbitrarily large endpoints in one appropriate
odd residue class modulo a power of three. If u and uv both admit returns,
the deterministic target orbit must use the already fixed return for u
before proceeding through the remaining clock interval. The intermediate
endpoint is odd, so the cut is an actual boundary between accelerated
steps. The remaining target word has v's odd count and clock. Agreement
on infinitely many ordinary endpoints proves its affine identity. This
justifies left cancellation, hence the stated equivalence between greedy
success, any accepted segmentation, and acceptance of the whole word.
The x=17 example correctly separates this language from full five closure.

### FR4: the endpoint quantifiers and infinite sums

For each unit residue modulo729, q_* is the least odd q>=5 in that
class. This handles all q in that class: replacing q by q_* increases
the offset loss B/q and hence decreases the lower bound for x/q.
The endpoint 1 has zero five defect, while other endpoints are odd units
at least five. All chosen returns have q<=x/2, so a source cutoff X
really induces the endpoint cutoff X/2.

For the ladder, integrality simplifies to
\(2^{b-2}q=1\pmod{3^{r+1}}\). Retaining only its congruence modulo
\(3^{\min(r+1,6)}\) enlarges the admissible set. This is legitimate
because all weights are positive. For r>=6 it gives one common b
progression with period486. The exact inverse formula is

\[
 \frac{x_b}{q}
 =\left(\frac43\right)^{r+1}
     \left(2^{b-2}-\frac1q\right)+\frac1q.
\]

Dropping the final positive term yields the note's tail constant. Increasing
b by486 multiplies its lower bound by at least2^486, while increasing
r multiplies it by4/3. Both geometric sums in the infinite tail therefore
have the asserted direction. The nine remaining finite-family terms use
the same endpoint residue and cannot independently choose incompatible
worst residues. This compatibility is the useful improvement.

Every irrational inverse power used in the certificate has a rational
upper bound justified by an integer25th-power inequality. All denominator
replacements make the upper bound larger, and all remain positive. The
finite verification at all486 classes consequently proves the infinite
column bound, rather than merely sampling486 endpoints.

Finally, the energy argument is first performed at finite X. There
E(X/2)<=E(X), so moving the finite term gives
\((97/1000)E(X)<=R(X)\). Monotone limits then give the finite-energy
equivalence. There is no subtraction of infinities and no inference that
a positive-density covered set controls the complementary unknown label.

### FR5: an actual overloaded column

The condition128q=-1 modulo3^11 gives

\[
 x_r=2^{r+1}\frac{128q+1}{3^{r+1}}-1
 \qquad(r=3,5,8,9).
\]

Thus every x_r is integral, odd, and -1 modulo3. For sufficiently large
positive odd q it is positive, and its actual word to q is (1^r,8).
Distinct r give disjoint cylinders because they specify different first
non-one positions. The four separately certified lower bounds66/1000,
130/1000,363/1000,510/1000 sum to1069/1000. This disproves a uniform
column bound below one for that enlarged kernel, while leaving weighted
or label-dependent alternatives untouched.

## Independent computations actually performed

The source executable was run in normal and optimized Python at the
checkpoint above; both outputs were compared byte-for-byte with its frozen
report. A separate checker, `five_independent_check.py`, reconstructs the
coefficient using a different rational grid2^-40, direct searches of the
finite exponent congruences rather than discrete-log tables, and direct
geometric correction sums. Decimal arithmetic proposes candidate grid
numerators; **every accepted upper bound is then certified by a separate
exact integer inequality**. Decimal approximations are not acceptance tests.

The independent checker passed normally and with `python -O`, identically.
It verified:

* all486 infinite-column upper bounds below903/1000;
* the worst class q=547 modulo729, with a certified grid bound displayed
  as0.9028890656721911 (the slightly different source display uses the
  coarser10^-10 grid);
* 48 actual ordinary instances of the four new family formulas, with
  exact final gaps rather than only divisibility;
* 150 direct ladder correction identities;
* the overloaded actual endpoint q=247729 and its four ordinary incoming
  sources, including the ternary-unit guards, with total lower bound
  1069/1000.

`five_review_execution.json` records the source hashes, executed commands,
output hashes and comparison results. `five_independent_report.json`
contains the separate result. These execution receipts are distinct from
the symbolic reconstruction above and do not assert global convergence.

## Remaining issue

No gap was found in FR1--FR5 at this checkpoint. The open step is the
absolute finiteness of R_(21/25) for an arbitrary ordinary component
indicator. A larger return language, an improved positive column factor,
and a successful finite compiler do not establish that statement.
