# Independent reconstruction of the carry compiler

**Reviewer role:** analytic/energy route. **Verdict:** VERIFIED at the
stated narrow mathematical scopes by internal reconstruction. This is
not external referee acceptance or formal proof-assistant verification.
The global closure implication remains OPEN.

Reviewed source:
[CARRY_COMPILER.md](../certificates/CARRY_COMPILER.md), SHA-256
394571cd06d55caa4465cdb7a1d76cefc1d36b29bfc41522ac5a2c136f6cf7ea.
The author checker was read at SHA-256
0f5f09f0621b923717bfde1780f707940256f9fcf6f46f5a1846bf23d8a4f5ca.
The author's frozen report was inspected at SHA-256
cad16a9ff61e16907389c9278ccc9c2599a8199a3a60e9490cd5586fc7041828.
The present reviewer used a separate implementation and did not import
or execute the author checker.

## Claim reconstruction

### CF1: four-step proportional block and its whole cylinder

With the formal variable t=2^b q, independent inverse composition gives
the source (8t-65)/81 and target (40t-325)/81. This verifies the identity
for all b>=6, not merely substituted b values. The total exponent sums
are both b+3 and the odd counts are both four.

The positive source identity implies every target inverse division:
reduce the total numerator modulo three, perform the innermost inverse,
and repeat. The inverse of a positive odd integer, when integral and
with a positive exponent, is again positive and odd. This checks
ordinary realization and exact valuations, not just a rational identity.

Three leading valuation-one steps give (27x+19)/8. The next valuation
being at least six is exactly 81x+65=0 modulo 512, whose unique residue
is 271. It already forces the first three valuations. The displayed
q<x/6 bound is valid for every positive member because x>=271.
The least-failure consequence is correctly restricted to a failed
forward-five implication with a known convergent antecedent.

### CF2--CF3: carry entry, arbitrary loop, and exit

Independent affine composition gives corrections 3709 and 149617 at
clock 15, with difference 4*2^15 after multiplying the source
correction by five. The supplied ordinary base paths and the
2^16 source increment ensure that every intermediate quotient changes
by an even integer. Thus the finite entry table genuinely proves both
whole-cylinder paths.

The carry loop is the identity
3(5z+4)+1=5(3z+1)+8. If the source valuation is one, division by two
gives the odd number 5U(z)+4. No independent residue law is used.

For the exit, if the source has valuations (3,b), put v=U(z).
The condition b>=2 gives v=1 modulo four. The first target numerator
is 8(5v+1), with exact valuation four. Its next odd state is
(5v+1)/2, whose numerator is 5(3v+1)/2; its exact valuation is b-1.
The endpoint is therefore the specific value 5q.

The loop may repeat any finite number r supplied by the actual
certificate. Composing the formulas gives the closed source numerator
1351*3^(r+5)+2^(r+16), odd count r+9, and clock r+b+18. The target
correction is exactly five times this numerator. The proof supplies
every r; the implementation's finite run range does not replace it.

The full family does not always decrease height. The independent
checker includes r=20,b=2 with the actual positive pair
x=275726295529, q=17210549879311. Both arms replay, and q>x.
The separate renewal theorem correctly restricts to b>=r+2.

### CF4: ordinary first-hit witnesses at every rank

The base congruence modulo 3^10 and the unit-selection coefficient were
checked independently. Cubing a congruence with leading deviation at
3^(r+5) raises its precision from 3^(r+10) to 3^(r+11); the quadratic
and cubic error terms vanish at the new modulus. Raising to t_r also
preserves the needed precision. The choice
t_r=88*2^(-r) modulo 243 consequently forces the entire numerator
to equal 3^(r+9) modulo 3^(r+10). This proves integrality and source
unit residue one for every r.

Full inverse divisibility supplies every ordinary intermediate state.
The large final source exponent makes its first reversed state greater
than one. No subsequent integral inverse of a positive odd state above
one can be one, since that would require 2^a u=4. This proves the
source certificate is first-hit. Every target block ends at a number
at least five, so it cannot have previously entered the 1,2 cycle.
Appending the exponent four therefore gives a first-hit target
certificate, with the stated extra odd input and four extra clocks.

As an independent fixture outside the author's four fully expanded
indices, the reviewer constructed r=4, t=127, b=1666492. Its ordinary
source has 1666494 binary digits; exact accelerated replay gives
source rank 13 and target rank 14, with clocks 1666514 and 1666518.
Only its sizes are recorded, not the large integer's decimal expansion.
This is a finite implementation check; the congruence induction is
the all-rank proof.

### CF5: exact language and compiler termination

The three initial block patterns are disjoint. Once a pattern is
chosen, its run length and exit are determined by the supplied word.
Every successful parse removes a nonempty finite block. The target
replacement is an actual proportional path on the current ordinary
endpoint, so induction over the parsed blocks is legitimate. Its
last proportional endpoint is (1,5); appending the known 5-to-1
certificate finishes the target.

The author code validates the complete source first-hit certificate
before parsing. Unsupported valid words return UNRESOLVED, malformed
words raise explicit errors, and the empty certificate is handled at
source one. It does not search an unknown target trajectory or infer
all-source coverage from successful examples.

## Independent executable support

The reviewer implementation is
[check_renewal_phase.py](check_renewal_phase.py), SHA-256
e317cb562598444b85d31c58a5ac3e3ad117eb5f230df57925fc29de664bc448.
It was actually run in normal and optimized (-OO) Python; the outputs
were byte-identical and match
[renewal_phase_report.json](renewal_phase_report.json), SHA-256
cfbb20cfb6e023b3228d4927ab2684a3641572c304b7e2bc3e74df62ef21c978.

Its carry-specific checks include the formal-variable CF1 identity,
171 actual CF1 unit sources, 75 constructed safe CF3 sources for
r=0,...,24, the unsafe expanding control, the CF4 modular congruence
at r=0,...,12, and the independent fully ordinary r=4 first-hit fixture.
Other entries support the separate renewal and phase theorems.
No repository-wide execution receipt is asserted by these authoring
runs in a worktree with new uncommitted files.

## Boundary and attribution

The complete first-hit language is larger than PR166's published
language, but remains a strict sublanguage of all supplied certificates.
The rank-one source words are valid uncovered inputs. The phase
theorem in this packet gives a rigorous limit on one proposed way of
completing the compiler; it does not refute the stated compiler or
Collatz.

The source correctly credits PR157's global one-way criterion,
PR166's valuation-two ladder and signed rational framework, and
PR146's phase/template and localization results. This review makes
no broader originality claim.
