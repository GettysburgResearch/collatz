# Independent formal arithmetic review

23 November 2026. Reviewer: root. Parent:
a9b23dcee61a4b65a63aa4e7ca653d875a405037.

**Verdict: VERIFIED within the exact numerical arithmetic statements.**

The frozen source files are:

| Module | SHA-256 |
|---|---|
| HomogeneousRepunits.lean | b94a7e0ce4223116dced184d4cb08d3b60572e2eac313154513177ff890488dc |
| PacketGCD.lean | cabc44a642841ef376734fed131a708897fca3b5e36c1d571d45f191b8ce892e |

Both live under research/literature-push-20261123/rigidity/lean/.
The exact author and independent build receipts separately bind both
audit modules.

I read every declaration and proof. The repunit definition is a natural
recurrence, and repunit_eq_sum proves its literal homogeneous-sum
interface. The proof of strong divisibility uses its addition identity
and Euclid induction; it assumes base coprimality and derives index
coprimality consequences. It does not import a conjectured repunit
coprimality fact. The quotient interface retains the strict base order
needed to divide by a positive natural difference.

The packet constructor retains the complete product and every numerator
summand. For each factor, all other terms are multiples of that factor;
the surviving term is coprime to it. The specialization derives both
pairwise factor coprimality and the coefficient's coprimality from the
actual powered-repunit hypotheses. The finite set can have any size.

The full_numerical_gcd_dvd theorem controls the natural gcd of the whole
displayed denominator and numerator, including all prime-power
multiplicities. Its proof never assumes coprimality between the small
factor X^r-Y^r and the product of repunits. The small-factor lemma works
even when those factors share primes, matching the written argument's
required boundary. The actual family has X>Y and Y>2^b; the Lean
divisibility is valid even in its more general natural-subtraction
form.

I freshly compiled both modules and both audits into an independent
empty output directory. The exact commands, source hashes, compiler
version, mathlib head and log hashes appear in root-lean-review.json.
All 22 theorem declarations and all six definitions appear in the
audit output; the only axioms are propext, Classical.choice and
Quot.sound. No sorryAx is present.

The finite Collatz-word realization, primitive period, exact polynomial
gcd, and real exponent lower bounds are not theorem statements of these
two modules. Their mathematical review and exact finite controls have
separate records. This formal verdict therefore does not extend to the
whole family theorem, the analytic lanes, or full Collatz.
